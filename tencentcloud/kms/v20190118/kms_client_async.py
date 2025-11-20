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
from tencentcloud.kms.v20190118 import models
from typing import Dict


class KmsClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'kms.intl.tencentcloudapi.com'
    _service = 'kms'

    async def ArchiveKey(
            self,
            request: models.ArchiveKeyRequest,
            opts: Dict = None,
    ) -> models.ArchiveKeyResponse:
        """
        This API is used to archive keys.The archived keys can only be used for decryption but not encryption.
        """
        
        kwargs = {}
        kwargs["action"] = "ArchiveKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ArchiveKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AsymmetricRsaDecrypt(
            self,
            request: models.AsymmetricRsaDecryptRequest,
            opts: Dict = None,
    ) -> models.AsymmetricRsaDecryptResponse:
        """
        This API is used to decrypt data with the specified private key that is encrypted with RSA asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption.
        """
        
        kwargs = {}
        kwargs["action"] = "AsymmetricRsaDecrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AsymmetricRsaDecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AsymmetricSm2Decrypt(
            self,
            request: models.AsymmetricSm2DecryptRequest,
            opts: Dict = None,
    ) -> models.AsymmetricSm2DecryptResponse:
        """
        This API is used to decrypt data with the specified private key that is encrypted with SM2 asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption. The length of the ciphertext passed in cannot exceed 256 bytes.
        """
        
        kwargs = {}
        kwargs["action"] = "AsymmetricSm2Decrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AsymmetricSm2DecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindCloudResource(
            self,
            request: models.BindCloudResourceRequest,
            opts: Dict = None,
    ) -> models.BindCloudResourceResponse:
        """
        This API is used to bind a key with a Tencent Cloud resource. If the key has been set to be expired automatically, the setting will be canceled to ensure that the key will not be invalid automatically. If the key and the resource has already been bound, the call will still be successful.
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDataKeyDeletion(
            self,
            request: models.CancelDataKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.CancelDataKeyDeletionResponse:
        """
        This API is used to cancel scheduled deletion for a data key.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDataKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDataKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelKeyArchive(
            self,
            request: models.CancelKeyArchiveRequest,
            opts: Dict = None,
    ) -> models.CancelKeyArchiveResponse:
        """
        This API is used to unarchive keys. If a key is unarchived, its status will be `Enabled`.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelKeyArchive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelKeyArchiveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelKeyDeletion(
            self,
            request: models.CancelKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.CancelKeyDeletionResponse:
        """
        Cancel the scheduled deletion of CMK
        """
        
        kwargs = {}
        kwargs["action"] = "CancelKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKey(
            self,
            request: models.CreateKeyRequest,
            opts: Dict = None,
    ) -> models.CreateKeyResponse:
        """
        Create a master key CMK (Custom Master Key) for user management data keys
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhiteBoxKey(
            self,
            request: models.CreateWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.CreateWhiteBoxKeyResponse:
        """
        This API is used to create a white-box key. Up to 50 ones can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Decrypt(
            self,
            request: models.DecryptRequest,
            opts: Dict = None,
    ) -> models.DecryptResponse:
        """
        This API is used to decrypt the ciphertext and obtain the plaintext data.
        """
        
        kwargs = {}
        kwargs["action"] = "Decrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImportedKeyMaterial(
            self,
            request: models.DeleteImportedKeyMaterialRequest,
            opts: Dict = None,
    ) -> models.DeleteImportedKeyMaterialResponse:
        """
        This API is used to delete the imported key material. It is only valid for EXTERNAL CMKs. Specifically, it puts a CMK into `PendingImport` status instead of deleting the CMK, so that the CMK can be used again after key material is reimported. To delete the CMK completely, please call the `ScheduleKeyDeletion` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImportedKeyMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImportedKeyMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhiteBoxKey(
            self,
            request: models.DeleteWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteWhiteBoxKeyResponse:
        """
        This API is used to delete a white-box key. Note: only disabled white-box keys can be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataKey(
            self,
            request: models.DescribeDataKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeDataKeyResponse:
        """
        This API is used to retrieve data key details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataKeys(
            self,
            request: models.DescribeDataKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeDataKeysResponse:
        """
        This API is used to return the key attribute information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKey(
            self,
            request: models.DescribeKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeKeyResponse:
        """
        This API is used to get the attribute details of the CMK with a specified `KeyId`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeys(
            self,
            request: models.DescribeKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeKeysResponse:
        """
        This API is used to get the attribute information of CMKs in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxDecryptKey(
            self,
            request: models.DescribeWhiteBoxDecryptKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxDecryptKeyResponse:
        """
        This API is used to get a white-box decryption key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxDecryptKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxDecryptKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxDeviceFingerprints(
            self,
            request: models.DescribeWhiteBoxDeviceFingerprintsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxDeviceFingerprintsResponse:
        """
        This API is used to get the device fingerprint list of a specified key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxDeviceFingerprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxDeviceFingerprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxKey(
            self,
            request: models.DescribeWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxKeyResponse:
        """
        This API is used to display white-box key information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxKeyDetails(
            self,
            request: models.DescribeWhiteBoxKeyDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxKeyDetailsResponse:
        """
        This API is used to get the white-box key list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxKeyDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxKeyDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxServiceStatus(
            self,
            request: models.DescribeWhiteBoxServiceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxServiceStatusResponse:
        """
        This API is used to get the white-box key service status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDataKey(
            self,
            request: models.DisableDataKeyRequest,
            opts: Dict = None,
    ) -> models.DisableDataKeyResponse:
        """
        This API is used to disable the data key.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDataKeys(
            self,
            request: models.DisableDataKeysRequest,
            opts: Dict = None,
    ) -> models.DisableDataKeysResponse:
        """
        This API is used to batch disable data keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKey(
            self,
            request: models.DisableKeyRequest,
            opts: Dict = None,
    ) -> models.DisableKeyResponse:
        """
        This API is used to disable a master key. The disabled key cannot be used for encryption and decryption operations.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKeyRotation(
            self,
            request: models.DisableKeyRotationRequest,
            opts: Dict = None,
    ) -> models.DisableKeyRotationResponse:
        """
        Disabled key rotation for the specified CMK.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKeyRotation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeyRotationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKeys(
            self,
            request: models.DisableKeysRequest,
            opts: Dict = None,
    ) -> models.DisableKeysResponse:
        """
        This API is used to batch prohibit the use of CMK.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWhiteBoxKey(
            self,
            request: models.DisableWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DisableWhiteBoxKeyResponse:
        """
        This API is used to disable a white-box key.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWhiteBoxKeys(
            self,
            request: models.DisableWhiteBoxKeysRequest,
            opts: Dict = None,
    ) -> models.DisableWhiteBoxKeysResponse:
        """
        This API is used to disable white-box keys in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWhiteBoxKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWhiteBoxKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableDataKey(
            self,
            request: models.EnableDataKeyRequest,
            opts: Dict = None,
    ) -> models.EnableDataKeyResponse:
        """
        This API is used to enable the data key.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableDataKeys(
            self,
            request: models.EnableDataKeysRequest,
            opts: Dict = None,
    ) -> models.EnableDataKeysResponse:
        """
        This API is used to batch enable data keys.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKey(
            self,
            request: models.EnableKeyRequest,
            opts: Dict = None,
    ) -> models.EnableKeyResponse:
        """
        Enable a specified CMK.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKeyRotation(
            self,
            request: models.EnableKeyRotationRequest,
            opts: Dict = None,
    ) -> models.EnableKeyRotationResponse:
        """
        Turn on the key rotation function for the specified CMK.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKeyRotation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeyRotationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKeys(
            self,
            request: models.EnableKeysRequest,
            opts: Dict = None,
    ) -> models.EnableKeysResponse:
        """
        This API is used to enable CMK in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWhiteBoxKey(
            self,
            request: models.EnableWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.EnableWhiteBoxKeyResponse:
        """
        This API is used to enable a white-box key.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWhiteBoxKeys(
            self,
            request: models.EnableWhiteBoxKeysRequest,
            opts: Dict = None,
    ) -> models.EnableWhiteBoxKeysResponse:
        """
        This API is used to enable white-box keys in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWhiteBoxKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWhiteBoxKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Encrypt(
            self,
            request: models.EncryptRequest,
            opts: Dict = None,
    ) -> models.EncryptResponse:
        """
        This API is used to encrypt any data up to 4KB. It can be used to encrypt database passwords, RSA Key, or other small sensitive information. For application data encryption, use the DataKey generated by GenerateDataKey to perform local data encryption and decryption operations
        """
        
        kwargs = {}
        kwargs["action"] = "Encrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EncryptByWhiteBox(
            self,
            request: models.EncryptByWhiteBoxRequest,
            opts: Dict = None,
    ) -> models.EncryptByWhiteBoxResponse:
        """
        This API is used to encrypt data with a white-box key.
        """
        
        kwargs = {}
        kwargs["action"] = "EncryptByWhiteBox"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EncryptByWhiteBoxResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateDataKey(
            self,
            request: models.GenerateDataKeyRequest,
            opts: Dict = None,
    ) -> models.GenerateDataKeyResponse:
        """
        This API generates a data key, which you can use to encrypt local data.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateRandom(
            self,
            request: models.GenerateRandomRequest,
            opts: Dict = None,
    ) -> models.GenerateRandomResponse:
        """
        This API is used to generate a random number.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateRandom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateRandomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataKeyCiphertextBlob(
            self,
            request: models.GetDataKeyCiphertextBlobRequest,
            opts: Dict = None,
    ) -> models.GetDataKeyCiphertextBlobResponse:
        """
        This API is used to download the encrypted data key.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataKeyCiphertextBlob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataKeyCiphertextBlobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataKeyPlaintext(
            self,
            request: models.GetDataKeyPlaintextRequest,
            opts: Dict = None,
    ) -> models.GetDataKeyPlaintextResponse:
        """
        This API is used to retrieve the key plaintext.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataKeyPlaintext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataKeyPlaintextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetKeyRotationStatus(
            self,
            request: models.GetKeyRotationStatusRequest,
            opts: Dict = None,
    ) -> models.GetKeyRotationStatusResponse:
        """
        Query whether the specified CMK has the key rotation function.
        """
        
        kwargs = {}
        kwargs["action"] = "GetKeyRotationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetKeyRotationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetParametersForImport(
            self,
            request: models.GetParametersForImportRequest,
            opts: Dict = None,
    ) -> models.GetParametersForImportResponse:
        """
        This API is used to obtain the parameters of the material to be imported into a CMK. The returned `Token` is used as one of the parameters to execute `ImportKeyMaterial`, and the returned `PublicKey` is used to encrypt the key material. The `Token` and `PublicKey` are valid for 24 hours. If they are expired, you will need to call the API again to get a new `Token` and `PublicKey`.
        """
        
        kwargs = {}
        kwargs["action"] = "GetParametersForImport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetParametersForImportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPublicKey(
            self,
            request: models.GetPublicKeyRequest,
            opts: Dict = None,
    ) -> models.GetPublicKeyResponse:
        """
        This API is used to get the public key of an asymmetric KMS key (which must be enabled). With the public key, you can encrypt messages and verify signatures.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRegions(
            self,
            request: models.GetRegionsRequest,
            opts: Dict = None,
    ) -> models.GetRegionsResponse:
        """
        This API is used to return all regions support KMS service.
        """
        
        kwargs = {}
        kwargs["action"] = "GetRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceStatus(
            self,
            request: models.GetServiceStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceStatusResponse:
        """
        Used to query whether the user has activated the KMS service.
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportDataKey(
            self,
            request: models.ImportDataKeyRequest,
            opts: Dict = None,
    ) -> models.ImportDataKeyResponse:
        """
        Data key import API, managed by KMS.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportKeyMaterial(
            self,
            request: models.ImportKeyMaterialRequest,
            opts: Dict = None,
    ) -> models.ImportKeyMaterialResponse:
        """
        This API is used to import key material into an EXTERNAL CMK. The key obtained through the `GetParametersForImport` API is used to encrypt the key material. You can only reimport the same key material into the specified CMK and set a new expiration time. After the CMK key material is imported, it cannot be replaced. After the key material is expired or deleted, the CMK will remain unavailable until the same key material is reimported. CMKs are independent, which means that the same key material can be imported into different CMKs, but data encrypted by one CMK cannot be decrypted by another one.
        Key material can only be imported into CMKs in `Enabled` and `PendingImport` status.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportKeyMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportKeyMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAlgorithms(
            self,
            request: models.ListAlgorithmsRequest,
            opts: Dict = None,
    ) -> models.ListAlgorithmsResponse:
        """
        This API is used to list the encryption methods supported in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAlgorithms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAlgorithmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataKeyDetail(
            self,
            request: models.ListDataKeyDetailRequest,
            opts: Dict = None,
    ) -> models.ListDataKeyDetailResponse:
        """
        This API is used to retrieve data key list details based on specified Offset and Limit.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataKeyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataKeyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataKeys(
            self,
            request: models.ListDataKeysRequest,
            opts: Dict = None,
    ) -> models.ListDataKeysResponse:
        """
        This API is used to query the list of data keys.
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListKeyDetail(
            self,
            request: models.ListKeyDetailRequest,
            opts: Dict = None,
    ) -> models.ListKeyDetailResponse:
        """
        Get the master key list details according to the specified Offset and Limit.
        """
        
        kwargs = {}
        kwargs["action"] = "ListKeyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListKeyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListKeys(
            self,
            request: models.ListKeysRequest,
            opts: Dict = None,
    ) -> models.ListKeysResponse:
        """
        This API is used to list the KeyIds of CMKs in `Enabled`, `Disabled`, and `PendingImport` status under the account.
        """
        
        kwargs = {}
        kwargs["action"] = "ListKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OverwriteWhiteBoxDeviceFingerprints(
            self,
            request: models.OverwriteWhiteBoxDeviceFingerprintsRequest,
            opts: Dict = None,
    ) -> models.OverwriteWhiteBoxDeviceFingerprintsResponse:
        """
        This API is used to overwrite the device fingerprint information of a specified key.
        """
        
        kwargs = {}
        kwargs["action"] = "OverwriteWhiteBoxDeviceFingerprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OverwriteWhiteBoxDeviceFingerprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoDecrypt(
            self,
            request: models.PostQuantumCryptoDecryptRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoDecryptResponse:
        """
        This API is used to decrypt ciphertext using post-quantum cryptography (PQC) algorithm, and return the plaintext.
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoDecrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoDecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoEncrypt(
            self,
            request: models.PostQuantumCryptoEncryptRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoEncryptResponse:
        """
        This API is used to encrypt using PQC. It supports up to 4 KB of data. It is applicable for encryption of database passwords, RSA keys, or other sensitive information. You can also apply `DataKey` generated by API `GenerateDataKey` to encrypt or decrypt your local data.
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoSign(
            self,
            request: models.PostQuantumCryptoSignRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoSignResponse:
        """
        This API is used to sign using PQC.
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoVerify(
            self,
            request: models.PostQuantumCryptoVerifyRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoVerifyResponse:
        """
        This API is used to verify a signature using PQC.
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoVerify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoVerifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReEncrypt(
            self,
            request: models.ReEncryptRequest,
            opts: Dict = None,
    ) -> models.ReEncryptResponse:
        """
        Re-encrypt the ciphertext using the specified CMK.
        """
        
        kwargs = {}
        kwargs["action"] = "ReEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScheduleDataKeyDeletion(
            self,
            request: models.ScheduleDataKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.ScheduleDataKeyDeletionResponse:
        """
        Schedule deletion for a data key.
        """
        
        kwargs = {}
        kwargs["action"] = "ScheduleDataKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScheduleDataKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScheduleKeyDeletion(
            self,
            request: models.ScheduleKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.ScheduleKeyDeletionResponse:
        """
        CMK planned deletion API, used to specify the time of CMK deletion, the optional time interval is [7,30] days
        """
        
        kwargs = {}
        kwargs["action"] = "ScheduleKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScheduleKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignByAsymmetricKey(
            self,
            request: models.SignByAsymmetricKeyRequest,
            opts: Dict = None,
    ) -> models.SignByAsymmetricKeyResponse:
        """
        This API is used to generate a signature with an asymmetric key.
        Note that only when KeyUsage is `ASYMMETRIC_SIGN_VERIFY_${ALGORITHM}` (e.g., `ASYMMETRIC_SIGN_VERIFY_SM2` and `ASYMMETRIC_SIGN_VERIFY_ECC`), the key can be used for signing.
        """
        
        kwargs = {}
        kwargs["action"] = "SignByAsymmetricKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignByAsymmetricKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCloudResource(
            self,
            request: models.UnbindCloudResourceRequest,
            opts: Dict = None,
    ) -> models.UnbindCloudResourceResponse:
        """
        This API is used to unbind a key with a Tencent Cloud resource, indicating that the Tencent Cloud resource will not use the key any longer.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCloudResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCloudResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlias(
            self,
            request: models.UpdateAliasRequest,
            opts: Dict = None,
    ) -> models.UpdateAliasResponse:
        """
        This API is used to modify the alias of a CMK. CMKs in `PendingDelete` status cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataKeyDescription(
            self,
            request: models.UpdateDataKeyDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateDataKeyDescriptionResponse:
        """
        This API is used to modify the description of a data key.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataKeyDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataKeyDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataKeyName(
            self,
            request: models.UpdateDataKeyNameRequest,
            opts: Dict = None,
    ) -> models.UpdateDataKeyNameResponse:
        """
        This API is used to modify the data key name.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataKeyName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataKeyNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateKeyDescription(
            self,
            request: models.UpdateKeyDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateKeyDescriptionResponse:
        """
        This API is used to modify the description of the specified CMK. CMKs in `PendingDelete` status cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateKeyDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateKeyDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyByAsymmetricKey(
            self,
            request: models.VerifyByAsymmetricKeyRequest,
            opts: Dict = None,
    ) -> models.VerifyByAsymmetricKeyResponse:
        """
        This API is used to verify a signature with an asymmetric key.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyByAsymmetricKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyByAsymmetricKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)