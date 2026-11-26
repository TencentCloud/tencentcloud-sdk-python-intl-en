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
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.intl.tencentcloudapi.com'
    _service = 'teo'


    def ApplyFreeCertificate(self, request):
        r"""When applying for a free certificate, if you need to apply through DNS delegation verification or file verification, you can call this API to initiate the certificate application and get the corresponding verification content based on the application method. The order in which to call the API is as follows:
        Step 1: Call ApplyFreeCertificate to specify the verification method for the free certificate application and obtain the verification content.
        Step 2: Configure the content for the corresponding domain as required for verification.
        Step 3: Call CheckFreeCertificateVerification for verification. The free certificate application is completed after verification passes.
        Step 4: Call ModifyHostsCertificate to configure the domain name certificate with an EdgeOne free certificate.

        For the introduction to application methods, see the referenced document: Free Certificate Application Description (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1)
        Description:
        -Only the CNAME access mode can call this API to specify the free certificate application method. The NS/DNSPod hosting access mode uses automatic validation to apply for a free certificate, with no need to call this API.
        -If you need to switch the verification method for a free certificate, you can call this API again to update it by changing the VerificationMethod field.
        -A domain name can only apply for one free certificate. After calling this API, the backend will trigger the free certificate application task. You need to complete the domain name verification info configuration within 2 days, and then complete certificate authentication.

        :param request: Request instance for ApplyFreeCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ApplyFreeCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ApplyFreeCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFreeCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFreeCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSecurityTemplateToEntity(self, request):
        r"""Operate a security policy template. This API is used to bind or rebind a domain name to a designated policy template, or unbind it from a designated policy template.

        :param request: Request instance for BindSecurityTemplateToEntity.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindSecurityTemplateToEntityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindSecurityTemplateToEntityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSecurityTemplateToEntity", params, headers=headers)
            response = json.loads(body)
            model = models.BindSecurityTemplateToEntityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSharedCNAME(self, request):
        r"""Used to bind or unbind a shared CNAME for an acceleration domain name. This feature is in beta test.

        :param request: Request instance for BindSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.BindSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindZoneToPlan(self, request):
        r"""Bind the selected site not bound to a package to an existing package.

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            model = models.BindZoneToPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCnameStatus(self, request):
        r"""When the site access type is CNAME, all domain names under the site must complete CNAME record configuration as specified by the CNAME domain assigned by EdgeOne.
        This API is used to obtain the CNAME domain name assigned by EdgeOne for the integrated domain name, and to validate the CNAME configuration status of the integrated domain name.

        :param request: Request instance for CheckCnameStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCnameStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCnameStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCnameStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFreeCertificateVerification(self, request):
        r"""This API is used to verify a free certificate and obtain the application result. If verification is passed, you can query the free certificate information for the corresponding domain through this API. If the application failed, this API will return the corresponding failure description.
        After triggering the free certificate application API (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1), you can check the free certificate application result through this API. Once the free certificate application is successful, you need to configure it through the domain certificate configuration API (https://www.tencentcloud.com/document/product/1552/80764?from_cn_redirect=1) to deploy the free certificate to the acceleration domain.

        :param request: Request instance for CheckFreeCertificateVerification.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckFreeCertificateVerificationRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckFreeCertificateVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFreeCertificateVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFreeCertificateVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmMultiPathGatewayOriginACL(self, request):
        r"""This API is used to confirm that the latest origin-pull IP ranges have been updated to the origin server firewall when the origin-pull IP ranges of the multi-channel security acceleration gateway change.

        :param request: Request instance for ConfirmMultiPathGatewayOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.ConfirmMultiPathGatewayOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ConfirmMultiPathGatewayOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmMultiPathGatewayOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmMultiPathGatewayOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfirmOriginACLUpdate(self, request):
        r"""This API is used to confirm that the latest origin-pull IP ranges have been updated to the origin server firewall when the origin-pull IP ranges change. After confirming the update to the latest origin-pull IP ranges, related change notifications will stop being pushed.

        :param request: Request instance for ConfirmOriginACLUpdate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ConfirmOriginACLUpdateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ConfirmOriginACLUpdateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmOriginACLUpdate", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmOriginACLUpdateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccelerationDomain(self, request):
        r"""After creating a site, you can create an acceleration domain name through this API.

        In CNAME mode, if site ownership verification is ongoing, this API will return domain ownership verification info. You can verify domain ownership separately. For details, see [Site/Domain Name Ownership Verification](https://www.tencentcloud.com/document/product/1552/70789?from_cn_redirect=1).

        :param request: Request instance for CreateAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAliasDomain(self, request):
        r"""This API is used to create an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxy(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version to create layer 4 proxy instances (https://www.tencentcloud.com/document/product/1552/103417?from_cn_redirect=1).

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationProxyRule(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see [Create Layer 4 Proxy Forwarding Rule].
        ](https://www.tencentcloud.com/document/product/1552/103416?from_cn_redirect=1) .

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCLSIndex(self, request):
        r"""This API is used to create key-value indexes for delivered log fields in the corresponding Tencent Cloud CLS log topic for a specified real-time log delivery task (task-id). If indexes have been created in CLS, this API will append indexes through merging.

        :param request: Request instance for CreateCLSIndex.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCLSIndexRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCLSIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigGroupVersion(self, request):
        r"""In version management mode, this API is used to create a new version of a specified configuration group.

        :param request: Request instance for CreateConfigGroupVersion.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateConfigGroupVersionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateConfigGroupVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigGroupVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigGroupVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContentIdentifier(self, request):
        r"""This API is used to create a content identifier. You can set the description, tag, and other information. At the same time, you need to bind an enterprise package for billing data statistics. A content identifier can only be bound to one billing package, while a billing package can bind multiple content identifiers. This functionality is only available to allowlisted users.

        :param request: Request instance for CreateContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomGroup(self, request):
        r"""This API is used to create a custom group. A custom group is used to centrally manage a set of reusable matching entries. For example, you can save multiple JA3/JA4 TLS fingerprints as a TLS fingerprint group and directly reference the group in security rules, avoiding the need to maintain the same fingerprint list in multiple rules.

        :param request: Request instance for CreateCustomGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCustomGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCustomGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomizeErrorPage(self, request):
        r"""This API is used to create a custom response page.

        :param request: Request instance for CreateCustomizeErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCustomizeErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCustomizeErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomizeErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomizeErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDnsRecord(self, request):
        r"""After a site is created and accessed in NS mode, you can create DNS records through this API.

        :param request: Request instance for CreateDnsRecord.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateDnsRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDnsRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDnsRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeKVNamespace(self, request):
        r"""This API is used to create a KV namespace at a specified site.

        :param request: Request instance for CreateEdgeKVNamespace.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateEdgeKVNamespaceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateEdgeKVNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeKVNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeKVNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunction(self, request):
        r"""This API is used to create and deploy an edge function to EdgeOne edge nodes.

        :param request: Request instance for CreateFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunctionReplica(self, request):
        r"""This API is used to create copies of a specified edge function. After creating copies, when client requests match the configured trigger rules or default domain name, you can access a specific function copy by adding EO-Function-Replica-Name:[copy name] to the request header. Each function supports creating two copies by default.

        :param request: Request instance for CreateFunctionReplica.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateFunctionReplicaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateFunctionReplicaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunctionReplica", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionReplicaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunctionRule(self, request):
        r"""Creates a trigger rule for an edge function. It supports customized filter conditions to determine whether to execute a function. When a function needs to be executed, multiple ways are provided to select the target function, including directly specifying, selecting based on the client's associated region, and weight-based selection.

        :param request: Request instance for CreateFunctionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateFunctionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunctionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInferenceAPIToken(self, request):
        r"""Create an inference API Token for authentication when accessing the inference service. The Token content is returned only once when creating, and each site can create up to 100 tokens.

        :param request: Request instance for CreateInferenceAPIToken.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateInferenceAPITokenRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateInferenceAPITokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInferenceAPIToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInferenceAPITokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInferenceDomain(self, request):
        r"""Create an inference service domain name for accessing the inference service through a custom domain name. An inference service supports creating a maximum of 5 custom domain names.
        After successful creation, complete the following steps to make the domain name function normally for external access:
        1. To validate the CNAME configuration status of a domain, see the CheckCnameStatus api.
        2. To verify ownership, refer to the VerifyOwnership API (https://www.tencentcloud.com/document/api/1552/98879?from_cn_redirect=1);
        3. To configure domain name certificates, refer to the ModifyHostsCertificate api.

        :param request: Request instance for CreateInferenceDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateInferenceDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateInferenceDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInferenceDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInferenceDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInferenceService(self, request):
        r"""This API is used to create an inference service. You can set the service name, listening port, container image configuration, and resource configuration. An access address is provided after successful creation.

        :param request: Request instance for CreateInferenceService.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateInferenceServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJustInTimeTranscodeTemplate(self, request):
        r"""JIT transcoding already provides preset transcoding templates to meet most needs. For personalized transcoding requirements, you can create custom transcoding templates through this API, with up to 100 custom templates.
        To ensure consistency of JIT transcoding effects and avoid video output exceptions caused by template changes during EO cache or M3U8 sharding, the template cannot be modified after creation.
        To learn about JIT transcoding capacity, see EdgeOne Video Instant Processing Function Introduction (https://www.tencentcloud.com/document/product/1552/111927?from_cn_redirect=1).

        :param request: Request instance for CreateJustInTimeTranscodeTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateJustInTimeTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateJustInTimeTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJustInTimeTranscodeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJustInTimeTranscodeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL4Proxy(self, request):
        r"""This API is used to create a layer 4 proxy instance.

        :param request: Request instance for CreateL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL4ProxyRules(self, request):
        r"""This API is used to create Layer 4 proxy instance rules and supports individual and batch creation.

        :param request: Request instance for CreateL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL7AccRules(self, request):
        r"""This API is used to create rules in the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1), with support for batch creation.

        :param request: Request instance for CreateL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        r"""This API is used to create a LoadBalancer. For details, see [Quickly Create Load Balancers](https://www.tencentcloud.com/document/product/1552/104223?from_cn_redirect=1). The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLoadBalancerResponse`

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


    def CreateLogAnalysisDownloadTask(self, request):
        r"""This API is used to create a log analysis download task. After creation, you can query the download task through the DescribeLogAnalysisDownloadTasks API.
        Note:
        1. Supports up to 50 million log entries per download.
        2. Log files will be retained for 3 days.
        3. If multiple tasks exist at the same time, they will be processed sequentially based on task creation time.

        :param request: Request instance for CreateLogAnalysisDownloadTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLogAnalysisDownloadTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLogAnalysisDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogAnalysisDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogAnalysisDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGateway(self, request):
        r"""This API is used to create a multi-channel security acceleration gateway, including Cloud Gateway and Private Gateway. Use the DescribeMultiPathGateway interface to query the status. If the status is online, the creation succeeded.

        :param request: Request instance for CreateMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGatewayLine(self, request):
        r"""This API is used to create lines for integrating with the multi-channel security acceleration gateway, including EdgeOne Layer 4 proxy lines and custom lines.

        :param request: Request instance for CreateMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultiPathGatewaySecretKey(self, request):
        r"""This API is used to create a key for integrating with a multi-channel security acceleration gateway. Customers integrate with the multi-channel security acceleration gateway based on key signatures. Each site contains only one key, which can be used to integrate all gateways under the site. The key can be queried through the DescribeMultiPathGatewaySecretKey API.

        :param request: Request instance for CreateMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOriginGroup(self, request):
        r"""Create an origin server group to manage origin servers by group. The origin server group configured here can be referenced in features such as **adding an acceleration domain name** and **Layer 4 proxy**.

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlan(self, request):
        r"""If you need to use the Edgeone product, you need to create a billing plan through this interface.
        > After creating a package, you need to complete creating a site and binding the plan through [CreateZone](https://www.tencentcloud.com/document/product/1552/80719?from_cn_redirect=1) before Edgeone can provide services properly.

        :param request: Request instance for CreatePlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlanForZone(self, request):
        r"""Purchase a package for the selected site not bound to a package.

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlanForZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrefetchTask(self, request):
        r"""This API is used to create a preheating task.

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrefetchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePurgeTask(self, request):
        r"""When origin server resources update but the node cache TTL has not expired, users still access old resources. At this point, use this API to update node resources. The following two methods can trigger updates: <li>Direct deletion: Delete the node cache without any validation. User requests trigger origin-pull.</li><li>Mark expiration: Mark node resources as expired. User requests trigger back-to-origin validation, which sends HTTP conditional requests with If-None-Match and If-Modified-Since headers. If the origin server responds with 200, the node fetches new resources from the origin and updates the cache. If the origin server responds with 304, the cache will not be updated.</li>

        For details on purging cache tasks, see [Purge Cache](https://www.tencentcloud.com/document/product/1552/70759?from_cn_redirect=1).

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePurgeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRealtimeLogDeliveryTask(self, request):
        r"""This API is used to create a real-time log delivery task.

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

        :param request: Request instance for CreateRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        r"""This API is on an earlier version for creating rule engine APIs. EdgeOne comprehensively upgraded the rule engine APIs on January 21, 2025. For details on the new API for creating layer-7 acceleration rules, refer to [CreateL7AccRules](https://www.tencentcloud.com/document/product/1552/115822?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version APIs will stop update and iteration. New features will only be provided by the latest version interface. The existing capacity supported by the old version APIs will not be affected. To avoid data field conflicts when using the old version APIs, migrate to the new version rule engine APIs as soon as possible.</p>

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityAPIResource(self, request):
        r"""Used to create API resources.

        :param request: Request instance for CreateSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityAPIService(self, request):
        r"""Used to create an API service.

        :param request: Request instance for CreateSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityClientAttester(self, request):
        r"""Create client authentication options.

        :param request: Request instance for CreateSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityIPGroup(self, request):
        r"""Create a security IP group

        :param request: Request instance for CreateSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityJSInjectionRule(self, request):
        r"""This API is used to create JavaScript injection rules.

        :param request: Request instance for CreateSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSharedCNAME(self, request):
        r"""Used to create a shared CNAME. This feature is in beta test.

        :param request: Request instance for CreateSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebSecurityTemplate(self, request):
        r"""Create a security policy configuration template

        :param request: Request instance for CreateWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateZone(self, request):
        r"""EdgeOne offers three access methods: CNAME, NS, and domainless access. You need to finalize site creation through this API first. For CNAME and NS connected site scenarios, see [Quickly access EdgeOne from scratch](https://www.tencentcloud.com/document/product/1552/87601?from_cn_redirect=1). For domainless access scenarios, see [Quickly enable layer 4 proxy service](https://www.tencentcloud.com/document/product/1552/96051?from_cn_redirect=1).

        > It is recommended to call this API to create a site when a package already exists under the account. Please input `PlanId` in the parameter to directly bind the site to the package. If `PlanId` is not input, the created site will be inactive and unable to provide normal services. You need to complete package binding through [BindZoneToPlan](https://www.tencentcloud.com/document/product/1552/83042?from_cn_redirect=1) before the site can provide services normally. If you currently have no bindable package, go to the console to purchase a package to finalize site creation.

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            model = models.CreateZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerationDomains(self, request):
        r"""Delete acceleration domain names in batches.

        :param request: Request instance for DeleteAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAliasDomain(self, request):
        r"""Delete an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxy(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Deleting a Layer 4 Proxy Instance.
        ](https://www.tencentcloud.com/document/product/1552/103415?from_cn_redirect=1) .

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplicationProxyRule(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Deleting L4 Proxy Rules (https://www.tencentcloud.com/document/product/1552/103414?from_cn_redirect=1).

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContentIdentifier(self, request):
        r"""Delete the specified content identifier. The feature is open only in the allowlist.

        :param request: Request instance for DeleteContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomErrorPage(self, request):
        r"""This API is used to delete a custom response page.

        :param request: Request instance for DeleteCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomGroup(self, request):
        r"""This API is used to delete a specified custom group. If the group is referenced by a rule, deletion is not allowed. Remove the reference first.

        :param request: Request instance for DeleteCustomGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteCustomGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteCustomGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDnsRecords(self, request):
        r"""You can use this API to delete DNS records in batches.

        :param request: Request instance for DeleteDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeKVNamespace(self, request):
        r"""This API is used to delete a specified KV namespace. After deletion, all key-value pair data in the namespace will be cleared and cannot be recovered. If the namespace is referenced by an edge function, unbind the relationship before deletion.

        :param request: Request instance for DeleteEdgeKVNamespace.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteEdgeKVNamespaceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteEdgeKVNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeKVNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeKVNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunction(self, request):
        r"""This API is used to delete an edge function. Once deleted, the function cannot be recovered, and associated trigger rules, environment variables, and replicas are also deleted.

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunctionReplica(self, request):
        r"""This API is used to delete a specified edge function replica.

        :param request: Request instance for DeleteFunctionReplica.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionReplicaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionReplicaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunctionReplica", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionReplicaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunctionRules(self, request):
        r"""This API is used to delete a trigger rule for an edge function.

        :param request: Request instance for DeleteFunctionRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteFunctionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunctionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInferenceAPIToken(self, request):
        r"""Delete an inference API Token. Once deleted, the Token expires immediately, and requests using it to access the inference service will not pass authentication.

        :param request: Request instance for DeleteInferenceAPIToken.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteInferenceAPITokenRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteInferenceAPITokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInferenceAPIToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInferenceAPITokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJustInTimeTranscodeTemplates(self, request):
        r"""Delete a just in time transcoding template based on the unique template identifier under the site ID.

        :param request: Request instance for DeleteJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL4Proxy(self, request):
        r"""This API is used to delete a layer 4 proxy instance.

        :param request: Request instance for DeleteL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL4ProxyRules(self, request):
        r"""This API is used to delete l4 proxy rules and supports both individual and batch operation.

        :param request: Request instance for DeleteL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteL7AccRules(self, request):
        r"""This API is used to delete rules from the rule engine (https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). Batch deletion supported.

        :param request: Request instance for DeleteL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancer(self, request):
        r"""This API is used to delete a load balancing instance. If the load balancing instance is referenced by other services, such as a Layer 4 proxy, it cannot be deleted. Remove the reference relationship first. The load balancer feature is in beta test. If you need to use it, contact us (https://www.tencentcloud.com/online?from_cn_redirect=1-service).

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultiPathGateway(self, request):
        r"""This API is used to delete multi-channel security acceleration gateways, including private gateways and Cloud Gateways.

        :param request: Request instance for DeleteMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultiPathGatewayLine(self, request):
        r"""This API is used to delete lines integrated with multi-channel security acceleration gateways. Only custom lines support deletion.

        :param request: Request instance for DeleteMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOriginGroup(self, request):
        r"""Delete an origin group. If the origin group is still referenced by a service (for example, Layer 4 proxy, DNS, load balancing, or a rule), deletion is not allowed.

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRealtimeLogDeliveryTask(self, request):
        r"""This API is used to delete a real-time log delivery task.

        :param request: Request instance for DeleteRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        r"""This API is on an earlier version for deleting rule engine APIs. EdgeOne completed a comprehensive upgrade of rule engine APIs on January 21, 2025. For details on the new API for deleting L7 acceleration rules, see [DeleteL7AccRules](https://www.tencentcloud.com/document/product/1552/115821?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version API will stop update and iteration. New features will only be provided in the new version API, and the existing capabilities supported by the old version API will not be affected. To avoid data field conflicts when using the old version API, migrate to the new version rule engine API as soon as possible.</p>

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

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


    def DeleteSecurityAPIResource(self, request):
        r"""Used to delete API resources.

        :param request: Request instance for DeleteSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityAPIService(self, request):
        r"""Used to delete an API service.

        :param request: Request instance for DeleteSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityClientAttester(self, request):
        r"""Delete client authentication options.

        :param request: Request instance for DeleteSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityIPGroup(self, request):
        r"""Delete a specified IP group. If a rule references the IP group, deletion is not allowed.

        :param request: Request instance for DeleteSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityJSInjectionRule(self, request):
        r"""This API is used to delete JavaScript injection rules.

        :param request: Request instance for DeleteSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSharedCNAME(self, request):
        r"""Used to delete a shared CNAME. This feature is in beta test.

        :param request: Request instance for DeleteSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebSecurityTemplate(self, request):
        r"""Delete a security policy configuration template

        :param request: Request instance for DeleteWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteZone(self, request):
        r"""Delete a site.

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployConfigGroupVersion(self, request):
        r"""In version management mode, this API is used for version release. You can release a version to the testing environment or production environment by EnvId. The version management feature is in beta test and currently only available to the allowlist.

        :param request: Request instance for DeployConfigGroupVersion.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeployConfigGroupVersionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeployConfigGroupVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployConfigGroupVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeployConfigGroupVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerationDomains(self, request):
        r"""This API is used to view domain information under a site, including acceleration domain names, origin servers, and domain name status. You can view information of all domains under a site, or specify filter conditions to query specific domain information.

        :param request: Request instance for DescribeAccelerationDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAccelerationDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerationDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerationDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAliasDomains(self, request):
        r"""Query the list of alias domain names.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAliasDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationProxies(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. The latest version splits into two APIs: one for querying the Layer 4 proxy instance list and the other for querying Layer 4 forwarding rules. For details, see [Query Layer 4 Proxy Instance List](https://www.tencentcloud.com/document/product/1552/103413?from_cn_redirect=1) and [Query Layer 4 Proxy Forwarding Rule List](https://www.tencentcloud.com/document/product/1552/103412?from_cn_redirect=1).

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableCustomActionsForRuleEngine(self, request):
        r"""Queries the list of available custom configurations for site rule engine operations.

        :param request: Request instance for DescribeAvailableCustomActionsForRuleEngine.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailableCustomActionsForRuleEngineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailableCustomActionsForRuleEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableCustomActionsForRuleEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableCustomActionsForRuleEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableOriginACLFamily(self, request):
        r"""This API is used to query detailed information about the origin protection IP range control domain, including the version number and specific IP range information.
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

        :param request: Request instance for DescribeAvailableOriginACLFamily.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailableOriginACLFamilyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailableOriginACLFamilyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableOriginACLFamily", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableOriginACLFamilyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailablePlans(self, request):
        r"""Query the list of available package information for the current account.

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailablePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingData(self, request):
        r"""Query billing data via this API.

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBillingDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigGroupVersionDetail(self, request):
        r"""In version management mode, this API is used to obtain detailed version information, including version ID, description, status, creation time, associated configuration group information, and the content of the version configuration file. The version management feature is in beta test and currently only available to the allowlist.

        :param request: Request instance for DescribeConfigGroupVersionDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigGroupVersionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigGroupVersionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigGroupVersions(self, request):
        r"""In version management mode, this API is used to query the version list of a specified configuration group. The version management feature is in beta test and currently only available to the allowlist.

        :param request: Request instance for DescribeConfigGroupVersions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeConfigGroupVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigGroupVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigGroupVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentIdentifiers(self, request):
        r"""This API is used to query content identifiers in batches. They can be filtered by ID, description, status, or tags. Deleted content identifiers queried by status are only retained for three months. This feature is only open in the allowlist.

        :param request: Request instance for DescribeContentIdentifiers.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentIdentifiersRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentIdentifiersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentIdentifiers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentIdentifiersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContentQuota(self, request):
        r"""Query the content management API quota

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContentQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomErrorPages(self, request):
        r"""This API is used to query the custom error page list.

        :param request: Request instance for DescribeCustomErrorPages.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeCustomErrorPagesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeCustomErrorPagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomErrorPages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomErrorPagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomGroup(self, request):
        r"""This API is used to query the detailed information of a custom group, including all entries in the group (returned with pagination via Limit/Offset). The DescribeCustomGroups list API returns up to the first 500 entries for each group. To obtain all entries, use this API. The GroupId can be obtained from the response of CreateCustomGroup or by querying DescribeCustomGroups.

        :param request: Request instance for DescribeCustomGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomGroupReferences(self, request):
        r"""This API is used to obtain the security policy configuration that uses a custom group.

        :param request: Request instance for DescribeCustomGroupReferences.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupReferencesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomGroupReferences", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomGroupReferencesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomGroups(self, request):
        r"""This API is used to query the list of custom groups under a specified site. This API returns only the first 500 entries of each custom group. To query all entries in a group, use the DescribeSecurityCustomGroup API.

        :param request: Request instance for DescribeCustomGroups.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeCustomGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackData(self, request):
        r"""This API is used to query DDoS attack time-series data.

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackEvent(self, request):
        r"""This API is used to query the list of DDoS attack events.

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSAttackTopData(self, request):
        r"""This API is used to query Top-ranked data of DDoS attacks.

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSAttackTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSProtection(self, request):
        r"""This API is used to query exclusive DDoS protection info of a site.

        :param request: Request instance for DescribeDDoSProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultCertificates(self, request):
        r"""Query the default certificate list
        <p style="color: red;">Note: This earlier version interface is no longer updated. New features will only be provided in the latest version interface. Existing capacities supported by the earlier version interface will not be affected. To query the cert configured for a domain name, please use DescribeAccelerationDomains.</p>

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployHistory(self, request):
        r"""In version management mode, this API is used to query the version release history of production/test environments. The version management feature is in beta test and currently only available to the allowlist.

        :param request: Request instance for DescribeDeployHistory.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDeployHistoryRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDeployHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeployHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDnsRecords(self, request):
        r"""This API is used to view DNS records under a site, including DNS record names, record types, and record content. It supports specifying filter conditions to query specific DNS records.

        :param request: Request instance for DescribeDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeKVNamespaces(self, request):
        r"""Queries the KV namespace list under a specified site. Supports pagination, sorting, and conditional filtering. Returns basic namespace info, storage capacity utilization, and reference relationships. If no data is found, an empty array is returned.

        :param request: Request instance for DescribeEdgeKVNamespaces.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeEdgeKVNamespacesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeEdgeKVNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeKVNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeKVNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        r"""In version management mode, this API is used to query environment information, including the environment ID, type, and current effective version. The version management feature is in beta test and currently only available to the allowlist.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionComponentBindings(self, request):
        r"""This API is used to query the component binding list of a specified edge function. It supports pagination and conditional filtering, and returns detailed information such as the bound component type, variable name, and configuration parameters. The currently supported binding component type is KV namespace (kv_namespace).

        :param request: Request instance for DescribeFunctionComponentBindings.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionComponentBindingsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionComponentBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionComponentBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionComponentBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionReplicas(self, request):
        r"""This API is used to query the replica list of edge functions.

        :param request: Request instance for DescribeFunctionReplicas.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionReplicasRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionRules(self, request):
        r"""This API is used to query the list of trigger rules for an edge function. It supports filtering by rule ID, function ID, rule description, and so on.

        :param request: Request instance for DescribeFunctionRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionRuntimeEnvironment(self, request):
        r"""This API is used to query the runtime environment of an edge function, including environment variables.

        :param request: Request instance for DescribeFunctionRuntimeEnvironment.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRuntimeEnvironmentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionRuntimeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionRuntimeEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionRuntimeEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctions(self, request):
        r"""This API is used to query the list of edge functions. It supports filtering by function ID, name, description, and so on.

        :param request: Request instance for DescribeFunctions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostsSetting(self, request):
        r"""This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. You can use [DescribeL7AccSetting](https://www.tencentcloud.com/document/product/1552/115819?from_cn_redirect=1) and [DescribeL7AccRules](https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1) to obtain detailed configuration of a domain.

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPGroupReferences(self, request):
        r"""This API is used to obtain policy settings that use IP grouping.

        :param request: Request instance for DescribeIPGroupReferences.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIPGroupReferencesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIPGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPGroupReferences", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPGroupReferencesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPRegion(self, request):
        r"""This API is used to query if the IP is an EdgeOne IP.

        :param request: Request instance for DescribeIPRegion.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIPRegionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIPRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdentifications(self, request):
        r"""Queries verification information of a site.

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdentificationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceAPITokens(self, request):
        r"""Queries the list of reasoning API tokens and returns the Token ID, name, content, and creation time. Paging query is supported.

        :param request: Request instance for DescribeInferenceAPITokens.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceAPITokensRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceAPITokensResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceAPITokens", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceAPITokensResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceDomains(self, request):
        r"""This API is used to query the inference service domain name list and return the Cname address, ownership verification, and certificate information of the domain.

        :param request: Request instance for DescribeInferenceDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceHardwareSpecifications(self, request):
        r"""This API is used to query the inference hardware specification list and return the CPU, memory, GPU, and video memory configurations of each specification. You can select the required specification from the list when creating a service.

        :param request: Request instance for DescribeInferenceHardwareSpecifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceHardwareSpecificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceHardwareSpecificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceHardwareSpecifications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceHardwareSpecificationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceServiceDeploymentLogs(self, request):
        r"""This API is used to query the logs of a specified deployment of an inference service, return log content and generation time, and support time range search, pagination, and sorting.

        :param request: Request instance for DescribeInferenceServiceDeploymentLogs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceDeploymentLogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceDeploymentLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceServiceDeploymentLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceServiceDeploymentLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceServiceDeploymentRecords(self, request):
        r"""This API is used to query the deployment history list of an inference service. It returns the operation type, status, duration, configuration snapshot, and whether it is the currently effective configuration for each deployment. Pagination and sorting are supported.

        :param request: Request instance for DescribeInferenceServiceDeploymentRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceDeploymentRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceDeploymentRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceServiceDeploymentRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceServiceDeploymentRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceServiceMonitorData(self, request):
        r"""This API is used to query the monitoring data of inference services, supporting indicators such as CPU, memory, GPU, video memory utilization, and instance count. You can specify the time range and aggregation granularity, and query data from the most recent 30 days.

        :param request: Request instance for DescribeInferenceServiceMonitorData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceMonitorDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServiceMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceServiceMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceServiceMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInferenceServices(self, request):
        r"""This API is used to query the inference service list, support filtering by service name, service ID, and status, and return the service configuration, running state, number of instances, and inference access address.

        :param request: Request instance for DescribeInferenceServices.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServicesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeInferenceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInferenceServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInferenceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJustInTimeTranscodeTemplates(self, request):
        r"""This API is used to retrieve the transcoding template detail list based on the just in time transcoding template name, template type, or unique ID. The returned results include all eligible custom templates and preset templates.

        :param request: Request instance for DescribeJustInTimeTranscodeTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeJustInTimeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeJustInTimeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJustInTimeTranscodeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJustInTimeTranscodeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL4Proxy(self, request):
        r"""This API is used to query the layer 4 proxy instance list.

        :param request: Request instance for DescribeL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL4ProxyRules(self, request):
        r"""This API is used to query the forwarding rule list under a Layer 4 proxy instance.

        :param request: Request instance for DescribeL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL7AccRules(self, request):
        r"""This API is used to query the rule list of the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1).

        :param request: Request instance for DescribeL7AccRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7AccRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL7AccRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL7AccSetting(self, request):
        r"""This API is used to query the global configuration of site acceleration.

        :param request: Request instance for DescribeL7AccSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeL7AccSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7AccSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL7AccSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerList(self, request):
        r"""This API is used to query the load balancing instance list. The load balancer feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for DescribeLoadBalancerList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancerListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLoadBalancerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogAnalysisDetail(self, request):
        r"""This API is used to query log analysis details. The data comes from the log data pushed by real-time log push tasks under the site with the destination "log-analysis".

        :param request: Request instance for DescribeLogAnalysisDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogAnalysisDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogAnalysisDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogAnalysisDownloadTasks(self, request):
        r"""This API is used to query the log download task list for log analysis. Note: Only download task records from the last three days are retained.

        :param request: Request instance for DescribeLogAnalysisDownloadTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisDownloadTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisDownloadTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogAnalysisDownloadTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogAnalysisDownloadTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogAnalysisStatistics(self, request):
        r"""This API is used to query log analysis statistics results. Users append an SQL aggregation statement after the query statement ([retrieval condition] | [SQL statement]). The backend executes the aggregation and returns columnar statistics results (column definition + data row).

        :param request: Request instance for DescribeLogAnalysisStatistics.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisStatisticsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogAnalysisStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogAnalysisStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogAnalysisStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGateway(self, request):
        r"""This API is used to query details of a multi-channel security acceleration gateway, such as name, Gateway ID, IP, port, and type.

        :param request: Request instance for DescribeMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayLine(self, request):
        r"""This API is used to query lines connected to the multi-channel security acceleration gateway, including direct connections, EdgeOne Layer 4 proxy lines, and custom lines.

        :param request: Request instance for DescribeMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayOriginACL(self, request):
        r"""This API is used to query the binding relationship between a multi-channel security acceleration gateway instance and origin IP ranges, as well as origin IP range details. If the MultiPathGatewayNextOriginACL field has a return value, synchronize the latest origin IP ranges to the origin server firewall settings.

        :param request: Request instance for DescribeMultiPathGatewayOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewayRegions(self, request):
        r"""This API is used to query the available region list of user-created multi-channel security acceleration gateways.

        :param request: Request instance for DescribeMultiPathGatewayRegions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewayRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewayRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewayRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGatewaySecretKey(self, request):
        r"""This API is used to query the key for integrating a multi-channel security acceleration gateway. Customers sign with the integration key to access the multi-channel security acceleration gateway.

        :param request: Request instance for DescribeMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiPathGateways(self, request):
        r"""This API is used to query the list of user-created multi-channel security acceleration gateways. Pagination is supported.

        :param request: Request instance for DescribeMultiPathGateways.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaysRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeMultiPathGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiPathGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiPathGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginACL(self, request):
        r"""This API is used to query the binding relationship between L7 acceleration domains/L4 proxy instances and origin IP ranges under a site, as well as origin IP range details. If you want to periodically get the latest version of origin IP ranges through an automation script, you can poll this API at a low frequency (once every three days is recommended). If the NextOriginACL field has a return value, synchronize the latest origin IP ranges to the origin server firewall configuration.

        :param request: Request instance for DescribeOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroup(self, request):
        r"""This API is used to query the origin server group list.

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginGroupHealthStatus(self, request):
        r"""This API is used to query the health status of origin server groups under a load balancing instance. The load balancer feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for DescribeOriginGroupHealthStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupHealthStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroupHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginGroupHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginProtection(self, request):
        r"""This API is on an earlier version for origin protection queries. EdgeOne comprehensively upgraded the origin protection APIs on June 27, 2025. For details on the new version of the origin protection query API, refer to [DescribeOriginACL](https://www.tencentcloud.com/document/product/1552/120408?from_cn_redirect=1).

        <p style="color: red;">Note: Starting from June 27, 2025, earlier version APIs will stop update and iteration, and new features will only be provided in the new version of APIs. To avoid data field conflicts when using earlier version APIs, migrate to the new version of origin protection APIs as soon as possible.</p>

        :param request: Request instance for DescribeOriginProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewL7Data(self, request):
        r"""This API is used to query layer-7 monitoring time series traffic Data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a> API.

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewL7DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlans(self, request):
        r"""Query the package information list with pagination.

        :param request: Request instance for DescribePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrefetchOriginLimit(self, request):
        r"""This API is used to query origin-pull rate limits. This feature is in beta test for allowlisted users.

        :param request: Request instance for DescribePrefetchOriginLimit.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchOriginLimitRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchOriginLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchOriginLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrefetchOriginLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrefetchTasks(self, request):
        r"""This API is used to query the commit history and execution progress of preheating tasks. Tasks submitted via the CreatePrefetchTasks API can be queried through this API.

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrefetchTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        r"""This API is used to query submitted URL refresh and directory refresh records and task progress. All tasks submitted via the CreatePurgeTasks API can be queried through this API.

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealtimeLogDeliveryTasks(self, request):
        r"""This API is used to query real-time log delivery task list.

        :param request: Request instance for DescribeRealtimeLogDeliveryTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRealtimeLogDeliveryTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRealtimeLogDeliveryTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealtimeLogDeliveryTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealtimeLogDeliveryTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        r"""This API is on an earlier version for querying rule engine rules. EdgeOne comprehensively upgraded the rule engine APIs on January 21, 2025. For details on the new version API for querying L7 acceleration rules, see [DescribeL7AccRules](https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the legacy version API will stop update and iteration. New features will only be provided in the new version API. The existing capacity supported by the legacy version API will not be affected. To avoid data field conflicts when using the legacy version API, migrate to the new version rule engine API as soon as possible.</p>

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

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


    def DescribeRulesSetting(self, request):
        r"""This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [RuleEngineAction](https://www.tencentcloud.com/document/product/1552/80721?from_cn_redirect=1#RuleEngineAction).

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAPIResource(self, request):
        r"""Query API resources under a site.

        :param request: Request instance for DescribeSecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityAPIService(self, request):
        r"""Query API services under a site.

        :param request: Request instance for DescribeSecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityClientAttester(self, request):
        r"""Query client authentication option configurations.

        :param request: Request instance for DescribeSecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroup(self, request):
        r"""This API is used to query the configuration information of a security IP group, including its ID, name, and content. In the query result of this API, each IP group returns up to 2,000 IPs or CIDR blocks. If an ultra-large IP group exceeds 2,000 IPs or CIDR blocks, call DescribeSecurityIPGroupContent for paging query.

        :param request: Request instance for DescribeSecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroupContent(self, request):
        r"""This API is used to query the IP address list in a specified IP group by page. When the number of IP addresses in an IP group exceeds 2000, you can use this API to perform a paging query to obtain the complete IP address list.

        :param request: Request instance for DescribeSecurityIPGroupContent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupContentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroupContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityIPGroupInfo(self, request):
        r"""This API is deprecated and will be discontinued on June 30, 2024. Please use the API for querying security IP groups.
        ](https://www.tencentcloud.com/document/product/1552/105866?from_cn_redirect=1).

        This API is used to query the configuration information of an IP group, including the IP group name, IP group content, and the site the IP group belongs to.

        :param request: Request instance for DescribeSecurityIPGroupInfo.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupInfoRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityIPGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityIPGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityIPGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityJSInjectionRule(self, request):
        r"""This API is used to query JavaScript injection rules.

        :param request: Request instance for DescribeSecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicy(self, request):
        r"""Query security protection configuration details.

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTemplateBindings(self, request):
        r"""This API is used to query the binding relationship list of a specified policy template.

        :param request: Request instance for DescribeSecurityTemplateBindings.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityTemplateBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTemplateBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTemplateBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedCNAME(self, request):
        r"""This API is used to query the shared CNAME list, supporting fuzzy search, pagination, and sorting.

        :param request: Request instance for DescribeSharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingFunctionAnalysisData(self, request):
        r"""This API is used to query the time series data of edge function analysis. Note that the data queried by this API has a delay of about 10 minutes. It is recommended to pull data from at least 10 minutes before the current time.

        :param request: Request instance for DescribeTimingFunctionAnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingFunctionAnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingFunctionAnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingFunctionAnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingFunctionAnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL4Data(self, request):
        r"""<p>This API is used to query the L4 time series Data list.</p>

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL4DataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7AnalysisData(self, request):
        r"""This API is used to query time series data of the L7 domain name business.
        Note:
        1. This API queries data with a delay of about 10 minutes. It is advisable to pull data from 10 minutes before the current time.
        2. This interface returns post-protection traffic request data by default. Users can use `Filters.mitigatedByWebSecurity` to custom query defended data.

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7CacheData(self, request):
        r"""This API is used to query L7 cache analysis time series traffic data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a> API.

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimingL7OriginPullData(self, request):
        r"""This API is used to query the origin-pull time series data of an L7 domain.
        You can choose to group queries by specifying the query dimension <code>DimensionName</code>, which returns multiple groups of time series data. For detailed directions and usage limits, see [How to Use APIs to Implement Group Query in a Single Call](https://www.tencentcloud.com/document/product/1552/127501?from_cn_redirect=1).

        :param request: Request instance for DescribeTimingL7OriginPullData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7OriginPullDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7OriginPullDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7OriginPullData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimingL7OriginPullDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopFunctionAnalysisData(self, request):
        r"""This API is used to query the topN data of Edge Functions by a specified dimension. Note that the data returned by this API has a delay of about 10 minutes. We recommend that you query the data generated at least 10 minutes before the current time.

        :param request: Request instance for DescribeTopFunctionAnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopFunctionAnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopFunctionAnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopFunctionAnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopFunctionAnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7AnalysisData(self, request):
        r"""This API is used to query the top N data of the L7 domain name business by specified dimension.
        Note:
        1. This API queries data with a delay of about 10 minutes. It is recommended to pull data from 10 minutes before the current time.
        2. This interface returns post-protection traffic request data by default. Users can use `Filters.mitigatedByWebSecurity` to custom query defended data.

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7AnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopL7CacheData(self, request):
        r"""This API is used to query L7 cache analysis topN data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80646?from_cn_redirect=1"> DescribeTopL7AnalysisData</a> API.

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopL7CacheDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebSecurityTemplate(self, request):
        r"""Queries security policy configuration template details

        :param request: Request instance for DescribeWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebSecurityTemplates(self, request):
        r"""Queries the security policy configuration template list.

        :param request: Request instance for DescribeWebSecurityTemplates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebSecurityTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebSecurityTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebSecurityTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneConfigImportResult(self, request):
        r"""This API is used to query the results of site configuration item import via the site configuration import API.

        :param request: Request instance for DescribeZoneConfigImportResult.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneConfigImportResultRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneConfigImportResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneConfigImportResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneConfigImportResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneCustomVariables(self, request):
        r"""This API is used to query site-level custom variable configurations, including variable definitions and variable operations. If not configured, both variable definitions and variable operations return empty lists.

        If needed, call the DescribeL7AccRules API to query rule-level custom variables.

        :param request: Request instance for DescribeZoneCustomVariables.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneCustomVariablesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneCustomVariablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneCustomVariables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneCustomVariablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneSetting(self, request):
        r"""This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [DescribeL7AccSetting](https://www.tencentcloud.com/document/product/1552/115819?from_cn_redirect=1).

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""This API is used to query site information you have permission to access. You can filter sites based on different query conditions.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

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


    def DestroyPlan(self, request):
        r"""This API is used to terminate a billing plan when you need to stop billing for an Edgeone plan.
        > The following conditions must be met to terminate a billing plan:
        1. The plan has expired (except for the Enterprise Edition Plan);
        2. All sites under the package have been shut down or deleted.

        > The site status can be queried through the [Query Site List](https://www.tencentcloud.com/document/product/1552/80713?from_cn_redirect=1) interface.
        A site can be deactivated by switching the site to a closed status through the [Switch Site Status](https://www.tencentcloud.com/document/product/1552/80707?from_cn_redirect=1) interface.
        A site can be deleted by using the Delete Site API.

        :param request: Request instance for DestroyPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.DestroyPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DestroyPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableOriginACL(self, request):
        r"""This API is used to disable origin protection for a site. Once disabled, resources related to the origin will no longer use only the origin IP range provided by origin protection to request your origin, and update notifications on origin IP ranges will stop simultaneously.

        :param request: Request instance for DisableOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.DisableOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DisableOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.DisableOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL4Logs(self, request):
        r"""This API is used to obtain the offline log download link for a Layer 4 proxy business.
        **Note:** EO stores offline logs and provides a download service only when the offline log feature is enabled. For specific features, see the [document](https://www.tencentcloud.com/document/product/1552/73660?from_cn_redirect=1).

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL4LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadL7Logs(self, request):
        r"""This API is used to obtain the offline log download link for an L7 domain.
        **Note:** EO stores offline logs and provides a download service only when the offline log feature is enabled. For specific features, see the [document](https://www.tencentcloud.com/document/product/1552/73660?from_cn_redirect=1).

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadL7LogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DummyParseZoneFullConfig(self, request):
        r"""This API is used to define the structure of a complete site configuration for reference only. Note: This API does not return actual data.

        :param request: Request instance for DummyParseZoneFullConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.DummyParseZoneFullConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DummyParseZoneFullConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DummyParseZoneFullConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DummyParseZoneFullConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EdgeKVDelete(self, request):
        r"""This API is used to delete one or more key-value pair data in a specified namespace. Batch deletion supported. Data cannot be recovered after deletion.

        :param request: Request instance for EdgeKVDelete.
        :type request: :class:`tencentcloud.teo.v20220901.models.EdgeKVDeleteRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EdgeKVDeleteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EdgeKVDelete", params, headers=headers)
            response = json.loads(body)
            model = models.EdgeKVDeleteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EdgeKVGet(self, request):
        r"""This API is used to batch read key values from a specified namespace. It supports querying up to 20 keys in a single query.

        :param request: Request instance for EdgeKVGet.
        :type request: :class:`tencentcloud.teo.v20220901.models.EdgeKVGetRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EdgeKVGetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EdgeKVGet", params, headers=headers)
            response = json.loads(body)
            model = models.EdgeKVGetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EdgeKVList(self, request):
        r"""This API is used to list all keys in the specified namespace, with prefix filtering supported. Cursor-based traversal is implemented, and the next cursor is returned for continued querying. It is suitable for traversing all keys in a namespace.

        :param request: Request instance for EdgeKVList.
        :type request: :class:`tencentcloud.teo.v20220901.models.EdgeKVListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EdgeKVListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EdgeKVList", params, headers=headers)
            response = json.loads(body)
            model = models.EdgeKVListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EdgeKVPut(self, request):
        r"""This API is used to write key-value pair data to a specified namespace, with support for setting expiration time. If the key already exists, the original value is overwritten. If not, a new key-value pair is created.

        :param request: Request instance for EdgeKVPut.
        :type request: :class:`tencentcloud.teo.v20220901.models.EdgeKVPutRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EdgeKVPutResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EdgeKVPut", params, headers=headers)
            response = json.loads(body)
            model = models.EdgeKVPutResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableOriginACL(self, request):
        r"""This API is used to enable origin protection for a site for the first time. After it is enabled, EdgeOne will use specific origin-pull IP ranges to pull from the origin for layer-7 acceleration domains/layer-4 proxy instances.
        This API supports two modes: **Automatic Protection Mode** and **Specified Protection Mode**. <li>When **Automatic Protection Mode** is used (L7EnableMode/L4EnableMode is set to all), the acceleration domain list and layer-4 proxy instances under the site will be automatically added to the origin protection list in real time without manual intervention;</li><li>When **Specified Protection Mode** is used (L7EnableMode/L4EnableMode is set to specific), you need to manually specify the resources to be added to origin protection. Unspecified resources will not be added to the origin protection list. If resource adjustment is required, you need to actively call the ModifyOriginACL API to make adjustments.</li>

        Instructions for using the Specified Protection Mode:
        <li>The maximum number of layer-7 acceleration domains that can be submitted at a time is 200, and the maximum number of layer-4 proxy instances is 100. Mixed submission of layer-7 acceleration domains/layer-4 proxy instances is supported, with a maximum total of 200 instances;</li>
        <li>When more than 200 resources need to be enabled, you need to first configure the resources of the first shard through this API, and then configure the remaining shards through the ModifyOriginACL API. For example, if 500 layer-7 acceleration domains need to be added, first use this API to set 200 domains, and then use the ModifyOriginACL API to configure the remaining 300 domains in two batches, with no more than 200 domains per batch.</li>

        Note:
        - When enabling, accounts on the allowlist can select other origin-pull IP range versions, such as the simplified version, to achieve the effect of pulling from the origin with fewer IP ranges.
        - Calling this API is deemed as your agreement to the [Special Agreement on Enabling Origin Protection](https://www.tencentcloud.com/document/product/1552/120141?from_cn_redirect=1);
        - Origin-pull IP ranges are subject to change from time to time. EdgeOne will send notifications 14 days, 7 days, 3 days, and 1 day before the change through one or more methods such as in-site messages, SMS, and emails. To ensure that you can receive notifications of origin-pull IP range changes, make sure that you have selected message notifications related to the EdgeOne product in the [Tencent Cloud Message Center Console](https://console.cloud.tencent.com/message) and configured the correct message recipients. For configuration methods, refer to [Message Subscription Management](https://www.tencentcloud.com/document/product/567/43476?from_cn_redirect=1).

        :param request: Request instance for EnableOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.EnableOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.EnableOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.EnableOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportZoneConfig(self, request):
        r"""This API is used to export site configuration by users based on desired configuration items. The exported configuration is used for import via the site configuration import API.

        :param request: Request instance for ExportZoneConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ExportZoneConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ExportZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ExportZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HandleFunctionRuntimeEnvironment(self, request):
        r"""This API is used to operate the runtime environment of an edge function. It supports related settings for environment variables.
        After the environment variables are set, they can be used in the function code and function replica code. For details, see [Edge Functions Referencing Environment Variables](https://www.tencentcloud.com/document/product/1552/109151?from_cn_redirect=1#0151fd9a-8b0e-407b-ae37-54553a60ded6).

        :param request: Request instance for HandleFunctionRuntimeEnvironment.
        :type request: :class:`tencentcloud.teo.v20220901.models.HandleFunctionRuntimeEnvironmentRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.HandleFunctionRuntimeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HandleFunctionRuntimeEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.HandleFunctionRuntimeEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdentifyZone(self, request):
        r"""Used to verify site ownership.

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.IdentifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportZoneConfig(self, request):
        r"""This API is used to quickly import site configuration files. After the import is initiated, the API will return the corresponding task ID (TaskId). Users need to use the site configuration import result query API to obtain the results of this import task.

        :param request: Request instance for ImportZoneConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ImportZoneConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ImportZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ImportZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IncreasePlanQuota(self, request):
        r"""This API is used to purchase additional quotas when the number of sites bound to your plan, the number of rules under "Web Protection - Custom Rules - Precision Matching Policy", or the rules under "Web Protection - Rate Limiting - Precision Rate Limiting Module" reach the plan's quota limit.
        > This interface only supports the Enterprise Edition Plan.

        :param request: Request instance for IncreasePlanQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.IncreasePlanQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IncreasePlanQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IncreasePlanQuota", params, headers=headers)
            response = json.loads(body)
            model = models.IncreasePlanQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomain(self, request):
        r"""Modify acceleration domain name information

        :param request: Request instance for ModifyAccelerationDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerationDomainStatuses(self, request):
        r"""Batch modify accelerated domain status

        :param request: Request instance for ModifyAccelerationDomainStatuses.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAccelerationDomainStatusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerationDomainStatuses", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerationDomainStatusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomain(self, request):
        r"""Modify an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAliasDomainStatus(self, request):
        r"""Modify the status of an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAliasDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxy(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, refer to [Modify Layer 4 Proxy Instance].
        ](https://www.tencentcloud.com/document/product/1552/103411?from_cn_redirect=1) .

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRule(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Modifying Layer 4 Proxy Forwarding Rules.
        ](https://www.tencentcloud.com/document/product/1552/103410?from_cn_redirect=1) .

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyRuleStatus(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Modifying Layer 4 Proxy Forwarding Rule Status.
        ](https://www.tencentcloud.com/document/product/1552/103409?from_cn_redirect=1) .

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationProxyStatus(self, request):
        r"""This API is on an earlier version. If you want to call it, switch to the latest version. For details, see [modify layer 4 proxy instance status](https://www.tencentcloud.com/document/product/1552/103408?from_cn_redirect=1).

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContentIdentifier(self, request):
        r"""Modification content identifier. Only description modification is supported. The feature is open in the allowlist only.

        :param request: Request instance for ModifyContentIdentifier.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyContentIdentifierRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyContentIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContentIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContentIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomErrorPage(self, request):
        r"""This API is used to modify a custom response page.

        :param request: Request instance for ModifyCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomErrorPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomGroup(self, request):
        r"""This API is used to modify the content of a custom group. GroupType cannot be modified after creation. When modifying entries in the group, you can specify replacement, append, or removal operations through GroupItemOperation.

        :param request: Request instance for ModifyCustomGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyCustomGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyCustomGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSProtection(self, request):
        r"""Modify exclusive DDoS protection for a site.

        :param request: Request instance for ModifyDDoSProtection.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSProtectionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnsRecords(self, request):
        r"""You can use this API to batch modify DNS records.

        :param request: Request instance for ModifyDnsRecords.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecords", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnsRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDnsRecordsStatus(self, request):
        r"""You can use this API to batch modify the status of DNS records and enable or disable records in batches.

        :param request: Request instance for ModifyDnsRecordsStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnsRecordsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnsRecordsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDnsRecordsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeKVNamespace(self, request):
        r"""This API is used to modify the attribute information of a specified KV namespace. Currently, only namespace description modification is supported.

        :param request: Request instance for ModifyEdgeKVNamespace.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyEdgeKVNamespaceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyEdgeKVNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeKVNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeKVNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunction(self, request):
        r"""This API is used to modify an edge function. It supports modifying the function content and description. The function will take effect immediately after modification and redeployment.

        :param request: Request instance for ModifyFunction.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionComponentBindings(self, request):
        r"""Modify the binding relationship between edge functions and components. Four operation modes are supported: bind, bind-override, unbind, and rebind. Manage function component binding relationships by specifying the operation type and component list.

        :param request: Request instance for ModifyFunctionComponentBindings.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionComponentBindingsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionComponentBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionComponentBindings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionComponentBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionReplica(self, request):
        r"""This API is used to modify the content and description of a specified edge function replica.

        :param request: Request instance for ModifyFunctionReplica.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionReplicaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionReplicaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionReplica", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionReplicaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionRule(self, request):
        r"""This API is used to modify a trigger rule for an edge function. It supports modifying rule conditions, execution functions, and description. You can first use the DescribeFunctionRules API to get the RuleId of the rule to be modified, then input the modified rule content. The original rule content will be overwritten.

        :param request: Request instance for ModifyFunctionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionRulePriority(self, request):
        r"""This API is used to modify the priority of trigger rules for an edge function.

        :param request: Request instance for ModifyFunctionRulePriority.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyFunctionRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionRulePriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionRulePriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostsCertificate(self, request):
        r"""After domain name creation is completed, you can configure a self-owned certificate for the domain name, or alternatively use the free certificate (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1) offered by EdgeOne.
        If you need to configure a self-owned certificate, upload the certificate to the [SSL certificate console](https://console.cloud.tencent.com/certoverview) first, then import the corresponding certificate ID in this API. For details, see [Deploy self-owned certificates to EdgeOne domain names].
        ](https://www.tencentcloud.com/document/product/1552/88874?from_cn_redirect=1).

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostsCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInferenceService(self, request):
        r"""Modify an inference service to support updates to the listening port, request path, container image, resource configuration, and description. Only passed parameters will be modified, while unpassed parameters remain unchanged.

        :param request: Request instance for ModifyInferenceService.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyInferenceServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4Proxy(self, request):
        r"""This API is used to modify the configuration of a layer 4 proxy instance.

        :param request: Request instance for ModifyL4Proxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4Proxy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyRules(self, request):
        r"""This API is used to modify Layer 4 proxy forwarding rules, supporting both individual and batch modification.

        :param request: Request instance for ModifyL4ProxyRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyRulesStatus(self, request):
        r"""This API is used to enable or disable the status of layer-4 proxy rules, supporting both individual and batch operation.

        :param request: Request instance for ModifyL4ProxyRulesStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyRulesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyRulesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyRulesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL4ProxyStatus(self, request):
        r"""This API is used to enable or disable an L4 proxy instance.

        :param request: Request instance for ModifyL4ProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL4ProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL4ProxyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL4ProxyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccRule(self, request):
        r"""This API is used to modify a rule in the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). Only one rule can be modified at a time.

        :param request: Request instance for ModifyL7AccRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccRulePriority(self, request):
        r"""This API is used to modify the priority of the rule list in the rule engine (https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). It requires the input of the complete rule ID list under the site ID. The rule ID list can be obtained through the API for querying layer-7 acceleration rules (https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1). The final priority order will be adjusted to the order of the rule ID list, executed from front to back.

        :param request: Request instance for ModifyL7AccRulePriority.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccRulePriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccRulePriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyL7AccSetting(self, request):
        r"""This API is used to modify the global configuration of site acceleration.

        :param request: Request instance for ModifyL7AccSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyL7AccSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyL7AccSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyL7AccSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancer(self, request):
        r"""This API is used to modify LoadBalancer configuration. The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for ModifyLoadBalancer.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancerRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGateway(self, request):
        r"""This API is used to modify multi-channel security acceleration gateway information, such as name, gateway ID, IP, and port.

        :param request: Request instance for ModifyMultiPathGateway.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewayLine(self, request):
        r"""This API is used to modify the configuration for connecting lines to the multi-channel security acceleration gateway, including EdgeOne Layer 4 proxy lines and custom lines.

        :param request: Request instance for ModifyMultiPathGatewayLine.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayLineRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayLineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewayLine", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayLineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewaySecretKey(self, request):
        r"""This API is used to modify the key for integrating a multi-channel security acceleration gateway. Customers sign with the integration key to access the multi-channel security acceleration gateway. After modification, the original key becomes invalid.

        :param request: Request instance for ModifyMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMultiPathGatewayStatus(self, request):
        r"""This API is used to update the multi-channel security gateway status.

        :param request: Request instance for ModifyMultiPathGatewayStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyMultiPathGatewayStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMultiPathGatewayStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMultiPathGatewayStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginACL(self, request):
        r"""This API is used to modify the origin protection configuration of a site. The following operations are supported: <li>**Resource addition and deletion**: enable or disable origin-pull from specific origin IP ranges for layer-7 accelerated domains/layer-4 proxy instances. This applies to resource adjustment in **specified protection mode**, and unspecified resources will not change;</li><li>**Mode switching**: adjust the origin protection mode of layer-7 accelerated domains/layer-4 proxy instances. After switching to all, the list of accelerated domains or layer-4 proxy instances under the site will be automatically added to the origin protection list in real time, and subsequent resource changes will also be automatically adjusted without manual intervention; after switching to specific, only the mode is changed, and resources already included in protection remain unchanged;</li><li>**IP range version switching**: for whitelisted customers, it supports switching to other available origin protection IP range versions, such as the simplified version, to reduce origin-pull IP ranges.</li>

        Instructions for specified protection mode:
        <li>The maximum number of layer-7 accelerated domains that can be submitted at a time is 200, and the maximum number of layer-4 proxy instances is 100. Mixed submission of layer-7 accelerated domains/layer-4 proxy instances is supported, with a maximum total of 200 instances;</li>
        <li>When more than 200 resources need to be changed, submit them in batches through this API. For example, to add 500 layer-7 accelerated domains, first submit 200 domains through this API, and then submit the remaining 300 domains in two batches, with no more than 200 domains each time.</li>

        :param request: Request instance for ModifyOriginACL.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginACLRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOriginGroup(self, request):
        r"""Modify origin group configuration. Newly submitted origin records will overwrite the original origin records in the origin group.

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOriginGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPlan(self, request):
        r"""Modify the plan settings. Currently, only the auto-renewal switch of prepaid plans can be modified.

        :param request: Request instance for ModifyPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrefetchOriginLimit(self, request):
        r"""This API is used to configure origin-pull rate limiting. This feature is in allowlist beta test.
        This API is used to create, modify, and delete preheated origin-pull rate limits. Each account supports up to 100 limits.

        :param request: Request instance for ModifyPrefetchOriginLimit.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyPrefetchOriginLimitRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyPrefetchOriginLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrefetchOriginLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrefetchOriginLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRealtimeLogDeliveryTask(self, request):
        r"""This API is used to modify the configuration of a real-time log delivery task. It has the following limits:
        <ul>
        <li>The destination type (`TaskType`) of a real-time log delivery task cannot be modified;</li>
        <li>The data delivery type (`LogType`) cannot be modified;</li>
        <li>The data delivery region (`Area`) cannot be modified;</li>
        <li>When the destination of the original real-time log delivery task is Tencent Cloud CLS, the destination details such as the log set and log topic cannot be modified.</li>
        </ul>

        :param request: Request instance for ModifyRealtimeLogDeliveryTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRealtimeLogDeliveryTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRealtimeLogDeliveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRealtimeLogDeliveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRealtimeLogDeliveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        r"""This API is on an earlier version for modifying rule engine APIs. EdgeOne comprehensively upgraded rule engine-related APIs on January 21, 2025. For details on the new version API for modifying layer-7 acceleration rules, refer to [ModifyL7AccRule](https://www.tencentcloud.com/document/product/1552/115818?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the legacy version API will stop update and iteration. New features will only be provided in the latest version API. The existing capacity supported by the legacy version API will not be affected. To avoid data field conflict when using the legacy version API, migrate to the latest version rule engine API as soon as possible.</p>

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityAPIResource(self, request):
        r"""This API is used to modify API resources.

        :param request: Request instance for ModifySecurityAPIResource.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIResourceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityAPIResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityAPIResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityAPIService(self, request):
        r"""This API is used to modify API services.

        :param request: Request instance for ModifySecurityAPIService.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityClientAttester(self, request):
        r"""Modify client authentication options.

        :param request: Request instance for ModifySecurityClientAttester.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityClientAttesterRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityClientAttesterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityClientAttester", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityClientAttesterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityIPGroup(self, request):
        r"""Modifies a security IP group.

        :param request: Request instance for ModifySecurityIPGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityIPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityIPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityIPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityJSInjectionRule(self, request):
        r"""This API is used to modify JavaScript injection rules.

        :param request: Request instance for ModifySecurityJSInjectionRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityJSInjectionRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityJSInjectionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityJSInjectionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityJSInjectionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        r"""Modify Web & Bot security configuration.

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySharedCNAME(self, request):
        r"""This API is used to modify a shared CNAME. Currently, it only supports modifying the description and settings of a shared CNAME, and associating an IP SSL domain name with an IP SSL shared CNAME. Once created, a shared CNAME itself cannot be modified. This feature is in beta test.

        :param request: Request instance for ModifySharedCNAME.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySharedCNAMERequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySharedCNAMEResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySharedCNAME", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySharedCNAMEResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebSecurityTemplate(self, request):
        r"""Modifies a security policy configuration template

        :param request: Request instance for ModifyWebSecurityTemplate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyWebSecurityTemplateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyWebSecurityTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebSecurityTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebSecurityTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZone(self, request):
        r"""Modifies site information.

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneCustomVariables(self, request):
        r"""This API is used to manage site-level custom variables, supporting the creation, modification, and deletion of variable definitions and variable operations. The submitted list will override the corresponding existing configuration. To clear the configuration, pass in an empty list. Configuration items not passed in remain unchanged. The default values for variable definitions and variable operations are both empty.

        For rule-level custom variable related operations, call the CreateL7AccRules or ModifyL7AccRule API.

        :param request: Request instance for ModifyZoneCustomVariables.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCustomVariablesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCustomVariablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneCustomVariables", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneCustomVariablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneSetting(self, request):
        r"""This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [ModifyL7AccSetting](https://www.tencentcloud.com/document/product/1552/115817?from_cn_redirect=1).

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneStatus(self, request):
        r"""Used to enable or disable a site.

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyZoneWorkMode(self, request):
        r"""This API is used to modify the working mode of each configuration module under a site. Each configuration module of a site can enable version management mode or immediate effect mode by configuration group dimension. For details, see Version Management (https://www.tencentcloud.com/document/product/1552/113690?from_cn_redirect=1).

        :param request: Request instance for ModifyZoneWorkMode.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneWorkModeRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneWorkModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneWorkMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyZoneWorkModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateInferenceDomain(self, request):
        r"""Operate an inference service domain name. You can stop, enable, and delete it. Resources cannot be recovered after deletion.

        :param request: Request instance for OperateInferenceDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.OperateInferenceDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.OperateInferenceDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateInferenceDomain", params, headers=headers)
            response = json.loads(body)
            model = models.OperateInferenceDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateInferenceService(self, request):
        r"""Operate an inference service. You can stop, start, and delete it. Resources cannot be recovered after deletion.

        :param request: Request instance for OperateInferenceService.
        :type request: :class:`tencentcloud.teo.v20220901.models.OperateInferenceServiceRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.OperateInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.OperateInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshMultiPathGatewaySecretKey(self, request):
        r"""This API is used to refresh the key of a multi-channel security acceleration gateway. Customers integrate with the multi-channel security acceleration gateway based on key signatures. Each site contains only one key, which can be used to integrate all gateways under the site. After the key is refreshed, the original key becomes invalid.

        :param request: Request instance for RefreshMultiPathGatewaySecretKey.
        :type request: :class:`tencentcloud.teo.v20220901.models.RefreshMultiPathGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.RefreshMultiPathGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshMultiPathGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshMultiPathGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewPlan(self, request):
        r"""When your plan needs to be extended, you can use this API to renew it. Plan renewal is only supported for the Personal, Basic, and Standard Editions.
        > For cost details, refer to [Plan Cost](https://www.tencentcloud.com/document/product/1552/94158?from_cn_redirect=1).

        :param request: Request instance for RenewPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.RenewPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.RenewPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewPlan", params, headers=headers)
            response = json.loads(body)
            model = models.RenewPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradePlan(self, request):
        r"""When you need features available only in higher-tier plans, you can upgrade your plan through this interface. Upgrades are only supported for Personal and Basic Edition Plans.
        > For differences between different types of Edgeone billing plans, see Edgeone billing plan comparison (https://www.tencentcloud.com/document/product/1552/94165?from_cn_redirect=1)
        For billing package upgrade rules and pricing details, see Edgeone billing package upgrade instructions (https://www.tencentcloud.com/document/product/1552/95291?from_cn_redirect=1)
        If your plan needs to upgrade to the Enterprise Edition, please [contact us](https://www.tencentcloud.com/contact-us).

        :param request: Request instance for UpgradePlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.UpgradePlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.UpgradePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradePlan", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyOwnership(self, request):
        r"""In CNAME access mode, you need to verify the ownership of the site or domain name. This API is used to trigger the verification. If the site passes ownership verification, no need to verify again when adding domains subsequently. For details, see [Site/Domain Name Ownership Verification](https://www.tencentcloud.com/document/product/1552/70789?from_cn_redirect=1).

        In NS access mode, you can also query through this API whether the NS server switch is successful. For details, see [Modify DNS Server](https://www.tencentcloud.com/document/product/1552/90452?from_cn_redirect=1).

        :param request: Request instance for VerifyOwnership.
        :type request: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.VerifyOwnershipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyOwnership", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyOwnershipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))