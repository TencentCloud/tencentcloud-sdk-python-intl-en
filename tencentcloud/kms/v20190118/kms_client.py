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
from tencentcloud.kms.v20190118 import models


class KmsClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'kms.tencentcloudapi.com'
    _service = 'kms'


    def ArchiveKey(self, request):
        """This API is used to archive keys. The archived keys can only be used for decryption but not encryption.

        :param request: Request instance for ArchiveKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.ArchiveKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ArchiveKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ArchiveKey", params, headers=headers)
            response = json.loads(body)
            model = models.ArchiveKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AsymmetricRsaDecrypt(self, request):
        """This API is used to decrypt data with the specified private key that is encrypted with RSA asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption.

        :param request: Request instance for AsymmetricRsaDecrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.AsymmetricRsaDecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.AsymmetricRsaDecryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AsymmetricRsaDecrypt", params, headers=headers)
            response = json.loads(body)
            model = models.AsymmetricRsaDecryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AsymmetricSm2Decrypt(self, request):
        """This API is used to decrypt data with the specified private key that is encrypted with SM2 asymmetric cryptographic algorithm. The ciphertext must be encrypted with the corresponding public key. The asymmetric key must be in `Enabled` state for decryption. The length of the ciphertext passed in cannot exceed 256 bytes.

        :param request: Request instance for AsymmetricSm2Decrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.AsymmetricSm2DecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.AsymmetricSm2DecryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AsymmetricSm2Decrypt", params, headers=headers)
            response = json.loads(body)
            model = models.AsymmetricSm2DecryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindCloudResource(self, request):
        """This API is used to bind a key with a Tencent Cloud resource. If the key has been set to be expired automatically, the setting will be canceled to ensure that the key will not be invalid automatically. If the key and the resource has already been bound, the call will still be successful.

        :param request: Request instance for BindCloudResource.
        :type request: :class:`tencentcloud.kms.v20190118.models.BindCloudResourceRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.BindCloudResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindCloudResource", params, headers=headers)
            response = json.loads(body)
            model = models.BindCloudResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelKeyArchive(self, request):
        """This API is used to unarchive keys. If a key is unarchived, its status will be `Enabled`.

        :param request: Request instance for CancelKeyArchive.
        :type request: :class:`tencentcloud.kms.v20190118.models.CancelKeyArchiveRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CancelKeyArchiveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelKeyArchive", params, headers=headers)
            response = json.loads(body)
            model = models.CancelKeyArchiveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelKeyDeletion(self, request):
        """Cancel the scheduled deletion of CMK

        :param request: Request instance for CancelKeyDeletion.
        :type request: :class:`tencentcloud.kms.v20190118.models.CancelKeyDeletionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CancelKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelKeyDeletion", params, headers=headers)
            response = json.loads(body)
            model = models.CancelKeyDeletionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKey(self, request):
        """Create a master key CMK (Custom Master Key) for user management data keys

        :param request: Request instance for CreateKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.CreateKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CreateKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWhiteBoxKey(self, request):
        """This API is used to create a white-box key. Up to 50 ones can be created.

        :param request: Request instance for CreateWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.CreateWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CreateWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhiteBoxKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWhiteBoxKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Decrypt(self, request):
        """This API is used to decrypt the ciphertext and obtain the plaintext data.

        :param request: Request instance for Decrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.DecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DecryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Decrypt", params, headers=headers)
            response = json.loads(body)
            model = models.DecryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImportedKeyMaterial(self, request):
        """This API is used to delete the imported key material. It is only valid for EXTERNAL CMKs. Specifically, it puts a CMK into `PendingImport` status instead of deleting the CMK, so that the CMK can be used again after key material is reimported. To delete the CMK completely, please call the `ScheduleKeyDeletion` API.

        :param request: Request instance for DeleteImportedKeyMaterial.
        :type request: :class:`tencentcloud.kms.v20190118.models.DeleteImportedKeyMaterialRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DeleteImportedKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImportedKeyMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImportedKeyMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWhiteBoxKey(self, request):
        """This API is used to delete a white-box key. Note: only disabled white-box keys can be deleted.

        :param request: Request instance for DeleteWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DeleteWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DeleteWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWhiteBoxKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWhiteBoxKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKey(self, request):
        """This API is used to get the attribute details of the CMK with a specified `KeyId`.

        :param request: Request instance for DescribeKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeys(self, request):
        """This API is used to get the attribute information of CMKs in batches.

        :param request: Request instance for DescribeKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteBoxDecryptKey(self, request):
        """This API is used to get a white-box decryption key.

        :param request: Request instance for DescribeWhiteBoxDecryptKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteBoxDecryptKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteBoxDecryptKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteBoxDeviceFingerprints(self, request):
        """This API is used to get the device fingerprint list of a specified key.

        :param request: Request instance for DescribeWhiteBoxDeviceFingerprints.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDeviceFingerprintsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDeviceFingerprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteBoxDeviceFingerprints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteBoxDeviceFingerprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteBoxKey(self, request):
        """This API is used to display white-box key information.

        :param request: Request instance for DescribeWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteBoxKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteBoxKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteBoxKeyDetails(self, request):
        """This API is used to get the white-box key list.

        :param request: Request instance for DescribeWhiteBoxKeyDetails.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteBoxKeyDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteBoxKeyDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteBoxServiceStatus(self, request):
        """This API is used to get the white-box key service status.

        :param request: Request instance for DescribeWhiteBoxServiceStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteBoxServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteBoxServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableKey(self, request):
        """This API is used to disable a master key. The disabled key cannot be used for encryption and decryption operations.

        :param request: Request instance for DisableKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableKey", params, headers=headers)
            response = json.loads(body)
            model = models.DisableKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableKeyRotation(self, request):
        """Disabled key rotation for the specified CMK.

        :param request: Request instance for DisableKeyRotation.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeyRotationRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableKeyRotation", params, headers=headers)
            response = json.loads(body)
            model = models.DisableKeyRotationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableKeys(self, request):
        """This API is used to batch prohibit the use of CMK.

        :param request: Request instance for DisableKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DisableKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableWhiteBoxKey(self, request):
        """This API is used to disable a white-box key.

        :param request: Request instance for DisableWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableWhiteBoxKey", params, headers=headers)
            response = json.loads(body)
            model = models.DisableWhiteBoxKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableWhiteBoxKeys(self, request):
        """This API is used to disable white-box keys in batches.

        :param request: Request instance for DisableWhiteBoxKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableWhiteBoxKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DisableWhiteBoxKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableKey(self, request):
        """Enable a specified CMK.

        :param request: Request instance for EnableKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableKey", params, headers=headers)
            response = json.loads(body)
            model = models.EnableKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableKeyRotation(self, request):
        """Turn on the key rotation function for the specified CMK.

        :param request: Request instance for EnableKeyRotation.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeyRotationRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableKeyRotation", params, headers=headers)
            response = json.loads(body)
            model = models.EnableKeyRotationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableKeys(self, request):
        """This API is used to enable CMK in batches.

        :param request: Request instance for EnableKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableKeys", params, headers=headers)
            response = json.loads(body)
            model = models.EnableKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableWhiteBoxKey(self, request):
        """This API is used to enable a white-box key.

        :param request: Request instance for EnableWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableWhiteBoxKey", params, headers=headers)
            response = json.loads(body)
            model = models.EnableWhiteBoxKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableWhiteBoxKeys(self, request):
        """This API is used to enable white-box keys in batches.

        :param request: Request instance for EnableWhiteBoxKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableWhiteBoxKeys", params, headers=headers)
            response = json.loads(body)
            model = models.EnableWhiteBoxKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Encrypt(self, request):
        """This API is used to encrypt any data up to 4KB. It can be used to encrypt database passwords, RSA Key, or other small sensitive information. For application data encryption, use the DataKey generated by GenerateDataKey to perform local data encryption and decryption operations

        :param request: Request instance for Encrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.EncryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EncryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Encrypt", params, headers=headers)
            response = json.loads(body)
            model = models.EncryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EncryptByWhiteBox(self, request):
        """This API is used to encrypt data with a white-box key.

        :param request: Request instance for EncryptByWhiteBox.
        :type request: :class:`tencentcloud.kms.v20190118.models.EncryptByWhiteBoxRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EncryptByWhiteBoxResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EncryptByWhiteBox", params, headers=headers)
            response = json.loads(body)
            model = models.EncryptByWhiteBoxResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateDataKey(self, request):
        """This API generates a data key, which you can use to encrypt local data.

        :param request: Request instance for GenerateDataKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.GenerateDataKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GenerateDataKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateDataKey", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateDataKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateRandom(self, request):
        """This API is used to generate a random number.

        :param request: Request instance for GenerateRandom.
        :type request: :class:`tencentcloud.kms.v20190118.models.GenerateRandomRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GenerateRandomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateRandom", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateRandomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetKeyRotationStatus(self, request):
        """Query whether the specified CMK has the key rotation function.

        :param request: Request instance for GetKeyRotationStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetKeyRotationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetKeyRotationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetParametersForImport(self, request):
        """This API is used to obtain the parameters of the material to be imported into a CMK. The returned `Token` is used as one of the parameters to execute `ImportKeyMaterial`, and the returned `PublicKey` is used to encrypt the key material. The `Token` and `PublicKey` are valid for 24 hours. If they are expired, you will need to call the API again to get a new `Token` and `PublicKey`.

        :param request: Request instance for GetParametersForImport.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetParametersForImportRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetParametersForImportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetParametersForImport", params, headers=headers)
            response = json.loads(body)
            model = models.GetParametersForImportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPublicKey(self, request):
        """This API is used to get the public key of an asymmetric KMS key (which must be enabled). With the public key, you can encrypt messages and verify signatures.

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRegions(self, request):
        """This API is used to return all regions support KMS service.

        :param request: Request instance for GetRegions.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetRegionsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRegions", params, headers=headers)
            response = json.loads(body)
            model = models.GetRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetServiceStatus(self, request):
        """Used to query whether the user has activated the KMS service.

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetServiceStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportKeyMaterial(self, request):
        """This API is used to import key material into an EXTERNAL CMK. The key obtained through the `GetParametersForImport` API is used to encrypt the key material. You can only reimport the same key material into the specified CMK and set a new expiration time. After the CMK key material is imported, it cannot be replaced. After the key material is expired or deleted, the CMK will remain unavailable until the same key material is reimported. CMKs are independent, which means that the same key material can be imported into different CMKs, but data encrypted by one CMK cannot be decrypted by another one.
        Key material can only be imported into CMKs in `Enabled` and `PendingImport` status.

        :param request: Request instance for ImportKeyMaterial.
        :type request: :class:`tencentcloud.kms.v20190118.models.ImportKeyMaterialRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ImportKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportKeyMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.ImportKeyMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAlgorithms(self, request):
        """This API is used to list the encryption methods supported in the current region.

        :param request: Request instance for ListAlgorithms.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListAlgorithmsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListAlgorithmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAlgorithms", params, headers=headers)
            response = json.loads(body)
            model = models.ListAlgorithmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListKeyDetail(self, request):
        """Get the master key list details according to the specified Offset and Limit.

        :param request: Request instance for ListKeyDetail.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListKeyDetailRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListKeyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListKeyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListKeyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListKeys(self, request):
        """This API is used to list the KeyIds of CMKs in `Enabled`, `Disabled`, and `PendingImport` status under the account.

        :param request: Request instance for ListKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListKeys", params, headers=headers)
            response = json.loads(body)
            model = models.ListKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OverwriteWhiteBoxDeviceFingerprints(self, request):
        """This API is used to overwrite the device fingerprint information of a specified key.

        :param request: Request instance for OverwriteWhiteBoxDeviceFingerprints.
        :type request: :class:`tencentcloud.kms.v20190118.models.OverwriteWhiteBoxDeviceFingerprintsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.OverwriteWhiteBoxDeviceFingerprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OverwriteWhiteBoxDeviceFingerprints", params, headers=headers)
            response = json.loads(body)
            model = models.OverwriteWhiteBoxDeviceFingerprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostQuantumCryptoDecrypt(self, request):
        """u200dThis API u200dis used to decrypt ciphertext using post-quantum cryptography (PQC) algorithm, and return the plaintext.

        :param request: Request instance for PostQuantumCryptoDecrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoDecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoDecryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PostQuantumCryptoDecrypt", params, headers=headers)
            response = json.loads(body)
            model = models.PostQuantumCryptoDecryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostQuantumCryptoEncrypt(self, request):
        """u200dThis API u200dis used to encrypt using PQC. It supports up to 4 KB of data. It is applicable for encryption of database passwords, RSA keys, or other sensitive information. You can also apply `DataKey` generated by API `GenerateDataKey` to encrypt or decrypt your local data.

        :param request: Request instance for PostQuantumCryptoEncrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoEncryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoEncryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PostQuantumCryptoEncrypt", params, headers=headers)
            response = json.loads(body)
            model = models.PostQuantumCryptoEncryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostQuantumCryptoSign(self, request):
        """This API is used to sign u200dusing PQC.

        :param request: Request instance for PostQuantumCryptoSign.
        :type request: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoSignRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PostQuantumCryptoSign", params, headers=headers)
            response = json.loads(body)
            model = models.PostQuantumCryptoSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostQuantumCryptoVerify(self, request):
        """This API is used to verify a signature u200dusing PQC.

        :param request: Request instance for PostQuantumCryptoVerify.
        :type request: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoVerifyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.PostQuantumCryptoVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PostQuantumCryptoVerify", params, headers=headers)
            response = json.loads(body)
            model = models.PostQuantumCryptoVerifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReEncrypt(self, request):
        """Re-encrypt the ciphertext using the specified CMK.

        :param request: Request instance for ReEncrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.ReEncryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ReEncryptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReEncrypt", params, headers=headers)
            response = json.loads(body)
            model = models.ReEncryptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScheduleKeyDeletion(self, request):
        """CMK planned deletion API, used to specify the time of CMK deletion, the optional time interval is [7,30] days

        :param request: Request instance for ScheduleKeyDeletion.
        :type request: :class:`tencentcloud.kms.v20190118.models.ScheduleKeyDeletionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ScheduleKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScheduleKeyDeletion", params, headers=headers)
            response = json.loads(body)
            model = models.ScheduleKeyDeletionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SignByAsymmetricKey(self, request):
        """This API is used to generate a signature with an asymmetric key.
        Note that only when KeyUsage is `ASYMMETRIC_SIGN_VERIFY_${ALGORITHM}` (e.g., `ASYMMETRIC_SIGN_VERIFY_SM2` and `ASYMMETRIC_SIGN_VERIFY_ECC`), the key can be used for signing.

        :param request: Request instance for SignByAsymmetricKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.SignByAsymmetricKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.SignByAsymmetricKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SignByAsymmetricKey", params, headers=headers)
            response = json.loads(body)
            model = models.SignByAsymmetricKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindCloudResource(self, request):
        """This API is used to unbind a key with a Tencent Cloud resource, indicating that the Tencent Cloud resource will not use the key any longer.

        :param request: Request instance for UnbindCloudResource.
        :type request: :class:`tencentcloud.kms.v20190118.models.UnbindCloudResourceRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.UnbindCloudResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindCloudResource", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindCloudResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlias(self, request):
        """This API is used to modify the alias of a CMK. CMKs in `PendingDelete` status cannot be modified.

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.kms.v20190118.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateKeyDescription(self, request):
        """This API is used to modify the description of the specified CMK. CMKs in `PendingDelete` status cannot be modified.

        :param request: Request instance for UpdateKeyDescription.
        :type request: :class:`tencentcloud.kms.v20190118.models.UpdateKeyDescriptionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.UpdateKeyDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateKeyDescription", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateKeyDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyByAsymmetricKey(self, request):
        """This API is used to verify a signature with an asymmetric key.

        :param request: Request instance for VerifyByAsymmetricKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.VerifyByAsymmetricKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.VerifyByAsymmetricKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyByAsymmetricKey", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyByAsymmetricKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))