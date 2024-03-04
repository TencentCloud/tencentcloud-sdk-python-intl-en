# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.tcr.v20190924 import models


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'
    _service = 'tcr'


    def CheckInstance(self, request):
        """This API is used to verify the information of the Enterprise Edition instance.

        :param request: Request instance for CheckInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CheckInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckInstanceName(self, request):
        """This API is used to check whether the name of the instance to be created meets the specifications.

        :param request: Request instance for CheckInstanceName.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceNameRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAccelerationService(self, request):
        """This API is used to create an image acceleration service.

        :param request: Request instance for CreateImageAccelerationService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImageAccelerationServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImageAccelerationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAccelerationService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAccelerationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImmutableTagRules(self, request):
        """This API is used to create the tag immutability rule.

        :param request: Request instance for CreateImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """This API is used to create an instance.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceCustomizedDomain(self, request):
        """This API is used to create a custom domain name.

        :param request: Request instance for CreateInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceToken(self, request):
        """This API is used to create a temporary or long-term instance access credential.

        :param request: Request instance for CreateInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMultipleSecurityPolicy(self, request):
        """This API is used to create multiple public network access allowlist policies of the TCR instance.

        :param request: Request instance for CreateMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMultipleSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespace(self, request):
        """This API is used to create a namespace in an Enterprise Edition instance.

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReplicationInstance(self, request):
        """This API is used to create a replication instance.

        :param request: Request instance for CreateReplicationInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRepository(self, request):
        """This API is used to create an image repository in an Enterprise Edition instance.

        :param request: Request instance for CreateRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRepository", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityPolicy(self, request):
        """This API is used to create a public network access allowlist policy for an instance.

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSecurityPolicyResponse`

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


    def CreateServiceAccount(self, request):
        """This API is used to create a service level account.

        :param request: Request instance for CreateServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSignature(self, request):
        """This API is used to create a signature for an image tag.

        :param request: Request instance for CreateSignature.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSignatureRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSignatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignature", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSignaturePolicy(self, request):
        """This API is used to create an image signature policy.

        :param request: Request instance for CreateSignaturePolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateSignaturePolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateSignaturePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignaturePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignaturePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTagRetentionExecution(self, request):
        """This API is used to execute tag retention manually.

        :param request: Request instance for CreateTagRetentionExecution.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionExecutionRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTagRetentionExecution", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagRetentionExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTagRetentionRule(self, request):
        """This API is used to create a tag retention rule.

        :param request: Request instance for CreateTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebhookTrigger(self, request):
        """This API is used to create a trigger.

        :param request: Request instance for CreateWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImage(self, request):
        """This API is used to delete the specified image.

        :param request: Request instance for DeleteImage.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageAccelerateService(self, request):
        """This API is used to delete an image acceleration service.

        :param request: Request instance for DeleteImageAccelerateService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageAccelerateServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageAccelerateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageAccelerateService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageAccelerateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImmutableTagRules(self, request):
        """This API is used to delete the tag immutability rule.

        :param request: Request instance for DeleteImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """This API is used to delete a TCR Enterprise Edition instance.

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstanceCustomizedDomain(self, request):
        """This API is used to delete a custom domain name.

        :param request: Request instance for DeleteInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstanceToken(self, request):
        """This API is used to delete a long-term access credential.

        :param request: Request instance for DeleteInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMultipleSecurityPolicy(self, request):
        """This API is used to delete multiple public network access allowlist policies of the instance.

        :param request: Request instance for DeleteMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMultipleSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespace(self, request):
        """This API is used to delete a namespace.

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReplicationInstance(self, request):
        """This API is used to delete a replica instance.

        :param request: Request instance for DeleteReplicationInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepository(self, request):
        """This API is used to delete an image repository.

        :param request: Request instance for DeleteRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepositoryTags(self, request):
        """This API is used to batch delete repository tags in an Enterprise Edition instance.

        :param request: Request instance for DeleteRepositoryTags.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryTagsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepositoryTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityPolicy(self, request):
        """This API is used to delete a public network access allow policy.

        Note: When both `PolicyIndex` and `CidrBlock` are specified, `CidrBlock` takes the higher priority

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteSecurityPolicyResponse`

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


    def DeleteServiceAccount(self, request):
        """This API is used to delete a service account.

        :param request: Request instance for DeleteServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSignaturePolicy(self, request):
        """This API is used to delete a namespace signing policy.

        :param request: Request instance for DeleteSignaturePolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteSignaturePolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteSignaturePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSignaturePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSignaturePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTagRetentionRule(self, request):
        """This API is used to delete a tag retention rule.

        :param request: Request instance for DeleteTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebhookTrigger(self, request):
        """This API is used to delete a trigger.

        :param request: Request instance for DeleteWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChartDownloadInfo(self, request):
        """This API is used to return the chart download information in an Enterprise Edition instance.

        :param request: Request instance for DescribeChartDownloadInfo.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeChartDownloadInfoRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeChartDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChartDownloadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChartDownloadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExternalEndpointStatus(self, request):
        """This API is used to query the public network access entry status of an instance.

        :param request: Request instance for DescribeExternalEndpointStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeExternalEndpointStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeExternalEndpointStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExternalEndpointStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExternalEndpointStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGCJobs(self, request):
        """This API is used to query the last ten garbage collection (GC) records.

        :param request: Request instance for DescribeGCJobs.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeGCJobsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeGCJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGCJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGCJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAccelerateService(self, request):
        """This API is used to query the status of an image acceleration service.

        :param request: Request instance for DescribeImageAccelerateService.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageAccelerateServiceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageAccelerateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAccelerateService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAccelerateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageManifests(self, request):
        """This API is used to query the manifest information of a container image.

        :param request: Request instance for DescribeImageManifests.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageManifests", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageManifestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        """This API is used to query the list of image tags or the information of the specified container image.

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImmutableTagRules(self, request):
        """This API is used to list the tag immutability rule.

        :param request: Request instance for DescribeImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAllNamespaces(self, request):
        """This API is used to query the list of all namespaces in an instance.

        :param request: Request instance for DescribeInstanceAllNamespaces.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceAllNamespacesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceAllNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAllNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAllNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceCustomizedDomain(self, request):
        """This API is used to query the list of custom domain names of an instance.

        :param request: Request instance for DescribeInstanceCustomizedDomain.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceCustomizedDomainRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceCustomizedDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCustomizedDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceCustomizedDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceStatus(self, request):
        """This API is used to query the current status and process information of an instance.

        :param request: Request instance for DescribeInstanceStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceToken(self, request):
        """This API is used to query the information of long-term access credentials.

        :param request: Request instance for DescribeInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query the instance information.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternalEndpoints(self, request):
        """This API is used to query the VPC URLs for private network access to an instance.

        :param request: Request instance for DescribeInternalEndpoints.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInternalEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternalEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternalEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespaces(self, request):
        """This API is used to query the namespace list or the information of the specified namespace.

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to get the available regions in TCR.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstanceCreateTasks(self, request):
        """This API is used to query the task status of creating a replication instance.

        :param request: Request instance for DescribeReplicationInstanceCreateTasks.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceCreateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstanceCreateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstanceSyncStatus(self, request):
        """This API is used to query the synchronization status of a replication instance.

        :param request: Request instance for DescribeReplicationInstanceSyncStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceSyncStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstanceSyncStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationInstances(self, request):
        """This API is used to query the list of replication instances.

        :param request: Request instance for DescribeReplicationInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositories(self, request):
        """This API is used to query the image repository list or the information of the specified image repository.

        :param request: Request instance for DescribeRepositories.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicies(self, request):
        """This API is used to query the public network access allowlist policies of an instance.

        :param request: Request instance for DescribeSecurityPolicies.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeSecurityPoliciesResponse`

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


    def DescribeServiceAccounts(self, request):
        """This API is used to query service accounts.

        :param request: Request instance for DescribeServiceAccounts.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeServiceAccountsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeServiceAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionExecution(self, request):
        """This API is used to query tag retention execution records.

        :param request: Request instance for DescribeTagRetentionExecution.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionExecution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionExecutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionExecutionTask(self, request):
        """This API is used to query tag retention execution tasks.

        :param request: Request instance for DescribeTagRetentionExecutionTask.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionTaskRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionExecutionTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionExecutionTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionExecutionTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRetentionRules(self, request):
        """This API is used to query tag retention rules.

        :param request: Request instance for DescribeTagRetentionRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeTagRetentionRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRetentionRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRetentionRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookTrigger(self, request):
        """This API is used to query triggers.

        :param request: Request instance for DescribeWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookTriggerLog(self, request):
        """This API is used to get trigger logs.

        :param request: Request instance for DescribeWebhookTriggerLog.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookTriggerLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookTriggerLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadHelmChart(self, request):
        """This API is used to download a Helm chart in TCR.

        :param request: Request instance for DownloadHelmChart.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DownloadHelmChartRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DownloadHelmChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadHelmChart", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadHelmChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DuplicateImage(self, request):
        """This API is used to duplicate the Enterprise Edition repository image version.

        :param request: Request instance for DuplicateImage.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DuplicateImageRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DuplicateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DuplicateImage", params, headers=headers)
            response = json.loads(body)
            model = models.DuplicateImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageExternalEndpoint(self, request):
        """This API is used to manage the public network access of an instance.

        :param request: Request instance for ManageExternalEndpoint.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageExternalEndpointRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageExternalEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageExternalEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ManageExternalEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageInternalEndpoint(self, request):
        """This API is used to manage VPC URLs for private network access to an instance.

        :param request: Request instance for ManageInternalEndpoint.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageInternalEndpointRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageInternalEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageInternalEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ManageInternalEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageReplication(self, request):
        """This API is used to manage the instance synchronization rule.

        :param request: Request instance for ManageReplication.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageReplication", params, headers=headers)
            response = json.loads(body)
            model = models.ManageReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImmutableTagRules(self, request):
        """This API is used to update the tag immutability rule.

        :param request: Request instance for ModifyImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImmutableTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """This API is used to update instance information.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceToken(self, request):
        """This API is used to update the status of the specified long-term access credential in an instance.

        :param request: Request instance for ModifyInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceToken", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNamespace(self, request):
        """This API is used to update the information of a namespace. Currently, only the namespace access level can be modified.

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRepository(self, request):
        """This API is used to update the information of an image repository. The repository description can be modified.

        :param request: Request instance for ModifyRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRepository", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicy(self, request):
        """This API is used to update the public network access allowlist of an instance.

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifySecurityPolicyResponse`

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


    def ModifyServiceAccount(self, request):
        """This API is used to update a service account.

        :param request: Request instance for ModifyServiceAccount.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceAccountPassword(self, request):
        """This API is used to update the password for a service level account.

        :param request: Request instance for ModifyServiceAccountPassword.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountPasswordRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyServiceAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTagRetentionRule(self, request):
        """This API is used to update a tag retention rule.

        :param request: Request instance for ModifyTagRetentionRule.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyTagRetentionRuleRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyTagRetentionRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTagRetentionRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTagRetentionRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookTrigger(self, request):
        """This API is used to update a trigger.

        :param request: Request instance for ModifyWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        """This API is used to renew a prepaid instance or change the billing mode from pay-as-you-go billing to monthly subscription billing.

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))