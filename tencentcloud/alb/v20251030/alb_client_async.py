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
from tencentcloud.alb.v20251030 import models
from typing import Dict


class AlbClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'alb.intl.tencentcloudapi.com'
    _service = 'alb'

    async def AddTargetsToTargetGroup(
            self,
            request: models.AddTargetsToTargetGroupRequest,
            opts: Dict = None,
    ) -> models.AddTargetsToTargetGroupResponse:
        """
        Add a backend service in the target group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddTargetsToTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTargetsToTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateBandwidthPackageWithLoadBalancer(
            self,
            request: models.AssociateBandwidthPackageWithLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.AssociateBandwidthPackageWithLoadBalancerResponse:
        """
        Bind a Bandwidth Package to an application CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateBandwidthPackageWithLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateBandwidthPackageWithLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateListenerAdditionalCertificates(
            self,
            request: models.AssociateListenerAdditionalCertificatesRequest,
            opts: Dict = None,
    ) -> models.AssociateListenerAdditionalCertificatesResponse:
        """
        AssociateListenerAdditionalCertificates is an async API. The system returns a request ID, but the additional cert is not yet successfully added. The add task is still in progress in the system backend. You can call the DescribeListenerCertificates API to query the add status of the additional cert.
        When HTTPS and QUIC listeners are in Associating status, it means certificate expansion is ongoing.
        When HTTPS and QUIC listeners are in the Associated status, the extension cert is successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateListenerAdditionalCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateListenerAdditionalCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHealthCheckTemplate(
            self,
            request: models.CreateHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateHealthCheckTemplateResponse:
        """
        This API is used to create a health check Template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        This API is used to create a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        **CreateLoadBalancer** is an async API. The system returns an instance ID, but the application CLB instance is not created successfully yet, and the creation task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the creation status of the application CLB instance.
        - When an application CLB instance is in the **Provisioning** status, it means the application CLB instance is being created.
        -When an application CLB instance is in the **Active** status, the application CLB instance is successfully created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRules(
            self,
            request: models.CreateRulesRequest,
            opts: Dict = None,
    ) -> models.CreateRulesResponse:
        """
        This API is used to create forwarding rules. It is an async API. After returning successfully, call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.
        A rule supports up to 10 forward Conditions and 5 forward Actions.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        Create a custom security policy for configuring the TLS protocol version and encryption suite of an HTTPS listener. With a security policy, you can flexibly control the security level of HTTPS communication between clients and load balancing.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTargetGroup(
            self,
            request: models.CreateTargetGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTargetGroupResponse:
        """
        Target Group APIs
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHealthCheckTemplates(
            self,
            request: models.DeleteHealthCheckTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteHealthCheckTemplatesResponse:
        """
        Deletes a health check Template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHealthCheckTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHealthCheckTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        Delete a listener
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancers(
            self,
            request: models.DeleteLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancersResponse:
        """
        The **DeleteLoadBalancers** API is an async API. The system returns a request ID, but the application CLB instance is not yet deleted successfully. The deletion task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the deletion status of the application CLB instance.
        - When an application CLB instance is in the **Deleting** status, it means the application CLB instance is being deleted.
        -If the specified application CLB instance cannot be queried, the application CLB instance has been deleted successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRules(
            self,
            request: models.DeleteRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRulesResponse:
        """
        DeleteRules deletes forwarding rules. This is an async API. After returning successfully, call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        Delete one or more custom security policies. Before deletion, please ensure the policy hasn't been referenced by any HTTPS listener, otherwise the deletion will fail.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTargetGroups(
            self,
            request: models.DeleteTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetGroupsResponse:
        """
        Delete a target group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncJobs(
            self,
            request: models.DescribeAsyncJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncJobsResponse:
        """
        Query API for async tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckTemplates(
            self,
            request: models.DescribeHealthCheckTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckTemplatesResponse:
        """
        This API is used to query the health check template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerCertificates(
            self,
            request: models.DescribeListenerCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerCertificatesResponse:
        """
        This API is used to query the list of certificates bound to a specified listener by instance id and listener id.
        If `CertificateType` is set to `SVR`, the information of the extended server certificate and the default server certificate is returned.
        If CertificateType is set to CA, the default CA certificate info is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerDetail(
            self,
            request: models.DescribeListenerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerDetailResponse:
        """
        Queries details of one listener.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerHealthStatus(
            self,
            request: models.DescribeListenerHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerHealthStatusResponse:
        """
        Queries the health status of a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        Queries the listener list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerDetail(
            self,
            request: models.DescribeLoadBalancerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerDetailResponse:
        """
        Queries detailed information of a specified load balancing instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        Query instance configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuota(
            self,
            request: models.DescribeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaResponse:
        """
        Queries the ALB quota configuration of the current account. It supports querying by quota type and allows you to pass a resource ID to query resource-level quotas. You can use DisplayFields to return the used amount and remaining available quantity as needed.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        This API is used to query forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicies(
            self,
            request: models.DescribeSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPoliciesResponse:
        """
        Queries the custom security policy list, supports filtering by security policy ID, name, or tag, and supports paging query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyCapabilities(
            self,
            request: models.DescribeSecurityPolicyCapabilitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyCapabilitiesResponse:
        """
        Query the security policy configuration capacity supported in the current region, including optional TLS protocol versions and the encryption suite list for each version. Before creating or modifying a custom security policy, call this API to get available configuration options.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyCapabilities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyCapabilitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyRelations(
            self,
            request: models.DescribeSecurityPolicyRelationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyRelationsResponse:
        """
        Query the relationship between a security policy and the HTTPS listeners that refer to it. Before deleting or modifying a security policy, it is advisable to call this API to confirm the impact.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyRelations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyRelationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemSecurityPolicies(
            self,
            request: models.DescribeSystemSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemSecurityPoliciesResponse:
        """
        Queries system security policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupTargets(
            self,
            request: models.DescribeTargetGroupTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupTargetsResponse:
        """
        Queries backend services in the target group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroups(
            self,
            request: models.DescribeTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsResponse:
        """
        Query the target group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupsByTarget(
            self,
            request: models.DescribeTargetGroupsByTargetRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsByTargetResponse:
        """
        Query bound target groups based on the slave machine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupsByTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsByTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        Querying Availability Zones
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateBandwidthPackageFromLoadBalancer(
            self,
            request: models.DisassociateBandwidthPackageFromLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DisassociateBandwidthPackageFromLoadBalancerResponse:
        """
        Unbind a Bandwidth Package from an application CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateBandwidthPackageFromLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateBandwidthPackageFromLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateListenerAdditionalCertificates(
            self,
            request: models.DisassociateListenerAdditionalCertificatesRequest,
            opts: Dict = None,
    ) -> models.DisassociateListenerAdditionalCertificatesResponse:
        """
        DisassociateListenerAdditionalCertificates is an async API. The system returns a request ID, but the additional cert is not yet unbound. The unbinding task is still in progress in the system backend. You can call the DescribeListenerCertificates API to query the cert unbinding status. If the cert is in Disassociating status, it is being unbound.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateListenerAdditionalCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateListenerAdditionalCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateLoadBalancer(
            self,
            request: models.InquirePriceCreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateLoadBalancerResponse:
        """
        This API is used to query the price for creating a load balancer.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHealthCheckTemplate(
            self,
            request: models.ModifyHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyHealthCheckTemplateResponse:
        """
        Modify a health check template
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListenerAttributes(
            self,
            request: models.ModifyListenerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerAttributesResponse:
        """
        Modifies listener properties.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListenerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAddressType(
            self,
            request: models.ModifyLoadBalancerAddressTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAddressTypeResponse:
        """
        **Prerequisite:**
        You have created an application CLB instance. For detailed operations, please see CreateLoadBalancer.
        When you need to change the network type of an application CLB instance from private network to public network through this API, you need to create an Elastic IP first.
        **Instructions:**
        The ModifyLoadBalancerAddressType API is an async API. The system returns a request ID, but the network type of the application CLB instance has not been changed yet. The change task is still in progress in the system backend. You can call DescribeLoadBalancerDetail to query the change status of the network type of the application CLB instance.
        When an application CLB instance is in the Configuring status, it means the network type of the instance is changing.
        When an application CLB instance is in the Active status, the network type change of the instance is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAddressType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAddressTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAttributes(
            self,
            request: models.ModifyLoadBalancerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAttributesResponse:
        """
        The **ModifyLoadBalancerAttributes** API is an async API. It returns a request ID, but the application CLB instance attribute has not been modified yet. The modifying task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the modification status of the application CLB instance attribute.
        -When the application CLB instance attribute is in the **Configuring** status, it means the application CLB instance attribute is being modified.
        - When the application CLB instance attribute is in the **Active** status, it means the application CLB instance attribute was modified successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerModificationProtection(
            self,
            request: models.ModifyLoadBalancerModificationProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerModificationProtectionResponse:
        """
        Set load balancing instance modification protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerModificationProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerModificationProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRulesAttributes(
            self,
            request: models.ModifyRulesAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyRulesAttributesResponse:
        """
        This API is used to modify forwarding rule attributes. This is an async API. After the API return succeeds, you can call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.
        A rule supports up to 10 forward Conditions and 5 forward Actions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRulesAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRulesAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicyAttributes(
            self,
            request: models.ModifySecurityPolicyAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyAttributesResponse:
        """
        Modify the properties of a custom security policy, including the policy name, TLS protocol version, and encryption suite. The modified configuration will be applied to all HTTPS listeners associated with this policy immediately.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicyAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupAttributes(
            self,
            request: models.ModifyTargetGroupAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupAttributesResponse:
        """
        Modify the target group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetsInTargetGroup(
            self,
            request: models.ModifyTargetsInTargetGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetsInTargetGroupResponse:
        """
        Modifies backend service information in the target group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetsInTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetsInTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def NotifyUnbindTarget(
            self,
            request: models.NotifyUnbindTargetRequest,
            opts: Dict = None,
    ) -> models.NotifyUnbindTargetResponse:
        """
        Notify load balancing to unbind real servers
        """
        
        kwargs = {}
        kwargs["action"] = "NotifyUnbindTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.NotifyUnbindTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveTargetsFromTargetGroup(
            self,
            request: models.RemoveTargetsFromTargetGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveTargetsFromTargetGroupResponse:
        """
        Removes a backend service from the target group
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveTargetsFromTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveTargetsFromTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerSecurityGroups(
            self,
            request: models.SetLoadBalancerSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerSecurityGroupsResponse:
        """
        The SetLoadBalancerSecurityGroups API supports setting (binding and unbinding) security groups for a public network load balancing instance. To query the security groups currently bound to a load balancing instance, use the DescribeLoadBalancerDetail API (https://www.tencentcloud.com/document/api/1822/133711?from_cn_redirect=1). This API uses SET semantics.
        For the binding operation, input parameters need to be passed in for all security groups that should be bound to the load balancing instance (bound + new binding).
        During unbinding, input parameters need to pass in all security groups bound to a CLB instance after unbinding. To unbind all security groups, omit this parameter or specify an empty array.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)