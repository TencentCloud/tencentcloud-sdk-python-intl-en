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
from tencentcloud.ssm.v20190923 import models
from typing import Dict


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.intl.tencentcloudapi.com'
    _service = 'ssm'

    async def CreateProductSecret(
            self,
            request: models.CreateProductSecretRequest,
            opts: Dict = None,
    ) -> models.CreateProductSecretResponse:
        """
        This API is used to create a Tencent Cloud service credential.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProductSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSSHKeyPairSecret(
            self,
            request: models.CreateSSHKeyPairSecretRequest,
            opts: Dict = None,
    ) -> models.CreateSSHKeyPairSecretResponse:
        """
        This API is used to create a secret that hosts SSH keys.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSSHKeyPairSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSSHKeyPairSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecret(
            self,
            request: models.CreateSecretRequest,
            opts: Dict = None,
    ) -> models.CreateSecretResponse:
        """
        This API is used to create a KMS-encrypted Secret. You can create and store up to 1,000 Secrets in each region.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecret(
            self,
            request: models.DeleteSecretRequest,
            opts: Dict = None,
    ) -> models.DeleteSecretResponse:
        """
        This API is used to delete a Secret. You can set whether to delete the Secret immediately or on schedule using the `RecoveryWindowInDays` parameter. For a Secret to be deleted on schedule, its status will be `PendingDelete` before the scheduled deletion time. You can use `RestoreSecret` to restore a deleted Secret during this time. A deleted Secret will not be restorable after the scheduled deletion time. A Secret can only be deleted after being disabled using `DisableSecret`.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecretVersion(
            self,
            request: models.DeleteSecretVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteSecretVersionResponse:
        """
        This API is used to directly delete a single credential version under the specified credential. The deletion takes effect immediately, and the credential version in all status can be deleted.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecretVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecretVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        This API is used to query the execution result of an async task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRotationDetail(
            self,
            request: models.DescribeRotationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRotationDetailResponse:
        """
        This API is used to query the details of a credential rotation policy.
        This API is only applicable to Tencent Cloud service credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRotationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRotationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRotationHistory(
            self,
            request: models.DescribeRotationHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeRotationHistoryResponse:
        """
        This API is used to query the historical versions of a rotated credential.
        This API is only applicable to Tencent Cloud service credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRotationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRotationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecret(
            self,
            request: models.DescribeSecretRequest,
            opts: Dict = None,
    ) -> models.DescribeSecretResponse:
        """
        This API is used to obtain the detailed attribute information of a Secret.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedProducts(
            self,
            request: models.DescribeSupportedProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedProductsResponse:
        """
        This API is used to query the list of supported Tencent Cloud services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSecret(
            self,
            request: models.DisableSecretRequest,
            opts: Dict = None,
    ) -> models.DisableSecretResponse:
        """
        This API is used to disable a Secret and will change its status to `Disabled`. The plaintext of a disabled Secret cannot be obtained through APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSecret(
            self,
            request: models.EnableSecretRequest,
            opts: Dict = None,
    ) -> models.EnableSecretResponse:
        """
        This API is used to enable a Secret and will change its status to `Enabled`. You can call the `GetSecretValue` API to obtain the plaintext of this Secret. Secrets in `PendingDelete` status can only be enabled after being restored by using `RestoreSecret`.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRegions(
            self,
            request: models.GetRegionsRequest,
            opts: Dict = None,
    ) -> models.GetRegionsResponse:
        """
        This API is used to obtain the list of regions displayed on Console.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSSHKeyPairValue(
            self,
            request: models.GetSSHKeyPairValueRequest,
            opts: Dict = None,
    ) -> models.GetSSHKeyPairValueResponse:
        """
        This API is used to obtain the plaintext value of the SSH key secret.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSSHKeyPairValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSSHKeyPairValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSecretValue(
            self,
            request: models.GetSecretValueRequest,
            opts: Dict = None,
    ) -> models.GetSecretValueResponse:
        """
        For user-defined credentials, this API is used to get the plaintext information of a credential by specifying the credential name and version.
        For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSecretValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSecretValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceStatus(
            self,
            request: models.GetServiceStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceStatusResponse:
        """
        This API is used to obtain the SecretsManager service status of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSecretVersionIds(
            self,
            request: models.ListSecretVersionIdsRequest,
            opts: Dict = None,
    ) -> models.ListSecretVersionIdsResponse:
        """
        This API is used to obtain list of versions of a Secret.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSecretVersionIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSecretVersionIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSecrets(
            self,
            request: models.ListSecretsRequest,
            opts: Dict = None,
    ) -> models.ListSecretsResponse:
        """
        This API is used to obtain the detailed information list of all Secrets. You can specify the filter fields and sorting order as needed.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSecrets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSecretsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutSecretValue(
            self,
            request: models.PutSecretValueRequest,
            opts: Dict = None,
    ) -> models.PutSecretValueResponse:
        """
        This API adds the new version of the credential content under the specified credential. One credential can have up to 10 versions. New versions can be added to credentials only in `Enabled` or `Disabled` status.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "PutSecretValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutSecretValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreSecret(
            self,
            request: models.RestoreSecretRequest,
            opts: Dict = None,
    ) -> models.RestoreSecretResponse:
        """
        This API is used to restore a `PendingDelete` Secret, canceling its scheduled deletion. The restored Secret will be in `Disabled` status. You can call the `EnableSecret` API to enable this Secret again.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RotateProductSecret(
            self,
            request: models.RotateProductSecretRequest,
            opts: Dict = None,
    ) -> models.RotateProductSecretResponse:
        """
        This API is used to rotate secrets for Tencent Cloud services or Tencent Cloud API key pairs.
        Note that only the secrets with the "Enabled" status can be rotated.
        """
        
        kwargs = {}
        kwargs["action"] = "RotateProductSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RotateProductSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDescription(
            self,
            request: models.UpdateDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateDescriptionResponse:
        """
        This API is used to update the description of a Secret. This API can only update Secrets in `Enabled` or `Disabled` status.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRotationStatus(
            self,
            request: models.UpdateRotationStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateRotationStatusResponse:
        """
        This API is used to set a Tencent Cloud service credential rotation policy, including the following parameters:
        Specifies whether to enable rotation
        Rotation frequency
        Rotation start time
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRotationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRotationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSecret(
            self,
            request: models.UpdateSecretRequest,
            opts: Dict = None,
    ) -> models.UpdateSecretResponse:
        """
        This API is used to update the credential content of the specified credential name and version number. Calling this API will encrypt the content of the new credential and overwrite the old content. Only credentials in `Enabled` or `Disabled` status can be updated.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)