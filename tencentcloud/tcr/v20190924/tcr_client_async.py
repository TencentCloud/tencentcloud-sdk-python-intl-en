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
from tencentcloud.tcr.v20190924 import models
from typing import Dict


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.intl.tencentcloudapi.com'
    _service = 'tcr'

    async def CheckInstance(
            self,
            request: models.CheckInstanceRequest,
            opts: Dict = None,
    ) -> models.CheckInstanceResponse:
        """
        This API is used to verify the information of the Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckInstanceName(
            self,
            request: models.CheckInstanceNameRequest,
            opts: Dict = None,
    ) -> models.CheckInstanceNameResponse:
        """
        This API is used to check whether the name of the instance to be created meets the specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageAccelerationService(
            self,
            request: models.CreateImageAccelerationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateImageAccelerationServiceResponse:
        """
        This API is used to create an image acceleration service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageAccelerationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageAccelerationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImmutableTagRules(
            self,
            request: models.CreateImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.CreateImmutableTagRulesResponse:
        """
        This API is used to create the tag immutability rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        This API is used to create an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceCustomizedDomain(
            self,
            request: models.CreateInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceCustomizedDomainResponse:
        """
        This API is used to create a custom domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceToken(
            self,
            request: models.CreateInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceTokenResponse:
        """
        This API is used to create a temporary or long-term instance access credential.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultipleSecurityPolicy(
            self,
            request: models.CreateMultipleSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateMultipleSecurityPolicyResponse:
        """
        This API is used to create multiple public network access allowlist policies of the TCR instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultipleSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultipleSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        This API is used to create a namespace in an Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReplicationInstance(
            self,
            request: models.CreateReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateReplicationInstanceResponse:
        """
        This API is used to create a replication instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRepository(
            self,
            request: models.CreateRepositoryRequest,
            opts: Dict = None,
    ) -> models.CreateRepositoryResponse:
        """
        This API is used to create an image repository in an Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        This API is used to create a public network access allowlist policy for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceAccount(
            self,
            request: models.CreateServiceAccountRequest,
            opts: Dict = None,
    ) -> models.CreateServiceAccountResponse:
        """
        This API is used to create a service level account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSignature(
            self,
            request: models.CreateSignatureRequest,
            opts: Dict = None,
    ) -> models.CreateSignatureResponse:
        """
        This API is used to create a signature for an image tag.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSignature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSignatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSignaturePolicy(
            self,
            request: models.CreateSignaturePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSignaturePolicyResponse:
        """
        This API is used to create an image signature policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSignaturePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSignaturePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTagRetentionExecution(
            self,
            request: models.CreateTagRetentionExecutionRequest,
            opts: Dict = None,
    ) -> models.CreateTagRetentionExecutionResponse:
        """
        This API is used to execute tag retention manually.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTagRetentionExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagRetentionExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTagRetentionRule(
            self,
            request: models.CreateTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateTagRetentionRuleResponse:
        """
        This API is used to create a tag retention rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebhookTrigger(
            self,
            request: models.CreateWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.CreateWebhookTriggerResponse:
        """
        This API is used to create a trigger.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImage(
            self,
            request: models.DeleteImageRequest,
            opts: Dict = None,
    ) -> models.DeleteImageResponse:
        """
        This API is used to delete the specified image.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageAccelerateService(
            self,
            request: models.DeleteImageAccelerateServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteImageAccelerateServiceResponse:
        """
        This API is used to delete an image acceleration service.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageAccelerateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageAccelerateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImmutableTagRules(
            self,
            request: models.DeleteImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteImmutableTagRulesResponse:
        """
        This API is used to delete the tag immutability rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        This API is used to delete a TCR Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceCustomizedDomain(
            self,
            request: models.DeleteInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceCustomizedDomainResponse:
        """
        This API is used to delete a custom domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceToken(
            self,
            request: models.DeleteInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceTokenResponse:
        """
        This API is used to delete a long-term access credential.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultipleSecurityPolicy(
            self,
            request: models.DeleteMultipleSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteMultipleSecurityPolicyResponse:
        """
        This API is used to delete multiple public network access allowlist policies of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultipleSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultipleSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespace(
            self,
            request: models.DeleteNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespaceResponse:
        """
        This API is used to delete a namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReplicationInstance(
            self,
            request: models.DeleteReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteReplicationInstanceResponse:
        """
        This API is used to delete a replica instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepository(
            self,
            request: models.DeleteRepositoryRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryResponse:
        """
        This API is used to delete an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepositoryTags(
            self,
            request: models.DeleteRepositoryTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryTagsResponse:
        """
        This API is used to batch delete repository tags in an Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepositoryTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        This API is used to delete a public network access allow policy.

        Note: When both `PolicyIndex` and `CidrBlock` are specified, `CidrBlock` takes the higher priority
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceAccount(
            self,
            request: models.DeleteServiceAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceAccountResponse:
        """
        This API is used to delete a service account.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSignaturePolicy(
            self,
            request: models.DeleteSignaturePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSignaturePolicyResponse:
        """
        This API is used to delete a namespace signing policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSignaturePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSignaturePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTagRetentionRule(
            self,
            request: models.DeleteTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteTagRetentionRuleResponse:
        """
        This API is used to delete a tag retention rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebhookTrigger(
            self,
            request: models.DeleteWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.DeleteWebhookTriggerResponse:
        """
        This API is used to delete a trigger.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChartDownloadInfo(
            self,
            request: models.DescribeChartDownloadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeChartDownloadInfoResponse:
        """
        This API is used to return the chart download information in an Enterprise Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChartDownloadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChartDownloadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalEndpointStatus(
            self,
            request: models.DescribeExternalEndpointStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalEndpointStatusResponse:
        """
        This API is used to query the public network access entry status of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalEndpointStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalEndpointStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGCJobs(
            self,
            request: models.DescribeGCJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeGCJobsResponse:
        """
        This API is used to query the last ten garbage collection (GC) records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGCJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGCJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAccelerateService(
            self,
            request: models.DescribeImageAccelerateServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAccelerateServiceResponse:
        """
        This API is used to query the status of an image acceleration service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAccelerateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAccelerateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageManifests(
            self,
            request: models.DescribeImageManifestsRequest,
            opts: Dict = None,
    ) -> models.DescribeImageManifestsResponse:
        """
        This API is used to query the manifest information of a container image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageManifests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageManifestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        This API is used to query the list of image tags or the information of the specified container image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImmutableTagRules(
            self,
            request: models.DescribeImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeImmutableTagRulesResponse:
        """
        This API is used to list the tag immutability rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAllNamespaces(
            self,
            request: models.DescribeInstanceAllNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAllNamespacesResponse:
        """
        This API is used to query the list of all namespaces in an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAllNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAllNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCustomizedDomain(
            self,
            request: models.DescribeInstanceCustomizedDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCustomizedDomainResponse:
        """
        This API is used to query the list of custom domain names of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCustomizedDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCustomizedDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceStatus(
            self,
            request: models.DescribeInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStatusResponse:
        """
        This API is used to query the current status and process information of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceToken(
            self,
            request: models.DescribeInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTokenResponse:
        """
        This API is used to query the information of long-term access credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternalEndpoints(
            self,
            request: models.DescribeInternalEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeInternalEndpointsResponse:
        """
        This API is used to query the VPC URLs for private network access to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternalEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternalEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNamespaces(
            self,
            request: models.DescribeNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNamespacesResponse:
        """
        This API is used to query the namespace list or the information of the specified namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to get the available regions in TCR.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstanceCreateTasks(
            self,
            request: models.DescribeReplicationInstanceCreateTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstanceCreateTasksResponse:
        """
        This API is used to query the task status of creating a replication instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstanceCreateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstanceCreateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstanceSyncStatus(
            self,
            request: models.DescribeReplicationInstanceSyncStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstanceSyncStatusResponse:
        """
        This API is used to query the synchronization status of a replication instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstanceSyncStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstanceSyncStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationInstances(
            self,
            request: models.DescribeReplicationInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationInstancesResponse:
        """
        This API is used to query the list of replication instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositories(
            self,
            request: models.DescribeRepositoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoriesResponse:
        """
        This API is used to query the image repository list or the information of the specified image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicies(
            self,
            request: models.DescribeSecurityPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPoliciesResponse:
        """
        This API is used to query the public network access allowlist policies of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceAccounts(
            self,
            request: models.DescribeServiceAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceAccountsResponse:
        """
        This API is used to query service accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionExecution(
            self,
            request: models.DescribeTagRetentionExecutionRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionExecutionResponse:
        """
        This API is used to query tag retention execution records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionExecutionTask(
            self,
            request: models.DescribeTagRetentionExecutionTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionExecutionTaskResponse:
        """
        This API is used to query tag retention execution tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionExecutionTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionExecutionTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRetentionRules(
            self,
            request: models.DescribeTagRetentionRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRetentionRulesResponse:
        """
        This API is used to query tag retention rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRetentionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRetentionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebhookTrigger(
            self,
            request: models.DescribeWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookTriggerResponse:
        """
        This API is used to query triggers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebhookTriggerLog(
            self,
            request: models.DescribeWebhookTriggerLogRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookTriggerLogResponse:
        """
        This API is used to get trigger logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookTriggerLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookTriggerLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadHelmChart(
            self,
            request: models.DownloadHelmChartRequest,
            opts: Dict = None,
    ) -> models.DownloadHelmChartResponse:
        """
        This API is used to download a Helm chart in TCR.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadHelmChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadHelmChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DuplicateImage(
            self,
            request: models.DuplicateImageRequest,
            opts: Dict = None,
    ) -> models.DuplicateImageResponse:
        """
        This API is used to duplicate the Enterprise Edition repository image version.
        """
        
        kwargs = {}
        kwargs["action"] = "DuplicateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DuplicateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageExternalEndpoint(
            self,
            request: models.ManageExternalEndpointRequest,
            opts: Dict = None,
    ) -> models.ManageExternalEndpointResponse:
        """
        This API is used to manage the public network access of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ManageExternalEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageExternalEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageInternalEndpoint(
            self,
            request: models.ManageInternalEndpointRequest,
            opts: Dict = None,
    ) -> models.ManageInternalEndpointResponse:
        """
        This API is used to manage VPC URLs for private network access to an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ManageInternalEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageInternalEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageReplication(
            self,
            request: models.ManageReplicationRequest,
            opts: Dict = None,
    ) -> models.ManageReplicationResponse:
        """
        This API is used to manage the instance synchronization rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ManageReplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageReplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImmutableTagRules(
            self,
            request: models.ModifyImmutableTagRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyImmutableTagRulesResponse:
        """
        This API is used to update the tag immutability rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImmutableTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImmutableTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to update instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceToken(
            self,
            request: models.ModifyInstanceTokenRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceTokenResponse:
        """
        This API is used to update the status of the specified long-term access credential in an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNamespace(
            self,
            request: models.ModifyNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyNamespaceResponse:
        """
        This API is used to update the information of a namespace. Currently, only the namespace access level can be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRepository(
            self,
            request: models.ModifyRepositoryRequest,
            opts: Dict = None,
    ) -> models.ModifyRepositoryResponse:
        """
        This API is used to update the information of an image repository. The repository description can be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicy(
            self,
            request: models.ModifySecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyResponse:
        """
        This API is used to update the public network access allowlist of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceAccount(
            self,
            request: models.ModifyServiceAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceAccountResponse:
        """
        This API is used to update a service account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceAccountPassword(
            self,
            request: models.ModifyServiceAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceAccountPasswordResponse:
        """
        This API is used to update the password for a service level account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTagRetentionRule(
            self,
            request: models.ModifyTagRetentionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyTagRetentionRuleResponse:
        """
        This API is used to update a tag retention rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTagRetentionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTagRetentionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebhookTrigger(
            self,
            request: models.ModifyWebhookTriggerRequest,
            opts: Dict = None,
    ) -> models.ModifyWebhookTriggerResponse:
        """
        This API is used to update a trigger.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebhookTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebhookTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        This API is used to renew a prepaid instance or change the billing mode from pay-as-you-go billing to monthly subscription billing.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)