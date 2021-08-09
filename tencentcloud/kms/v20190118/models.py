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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AlgorithmInfo(AbstractModel):
    """Algorithm name and ID

    """

    def __init__(self):
        """
        :param KeyUsage: Algorithm ID\n        :type KeyUsage: str\n        :param Algorithm: Algorithm name\n        :type Algorithm: str\n        """
        self.KeyUsage = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyUsage = params.get("KeyUsage")
        self.Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyRequest(AbstractModel):
    """ArchiveKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyResponse(AbstractModel):
    """ArchiveKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`\n        :type Ciphertext: str\n        :param Algorithm: Corresponding algorithm when a public key is used for encryption. Valid values: RSAES_PKCS1_V1_5, RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256\n        :type Algorithm: str\n        """
        self.KeyId = None
        self.Ciphertext = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        self.Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        :param Plaintext: Base64-encoded plaintext after decryption\n        :type Plaintext: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`, whose length cannot exceed 256 bytes.\n        :type Ciphertext: str\n        """
        self.KeyId = None
        self.Ciphertext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        :param Plaintext: Base64-encoded plaintext after decryption\n        :type Plaintext: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class BindCloudResourceRequest(AbstractModel):
    """BindCloudResource request structure.

    """

    def __init__(self):
        """
        :param KeyId: CMK ID\n        :type KeyId: str\n        :param ProductId: Unique ID of a Tencent Cloud service\n        :type ProductId: str\n        :param ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.ProductId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ProductId = params.get("ProductId")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudResourceResponse(AbstractModel):
    """BindCloudResource response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyArchiveRequest(AbstractModel):
    """CancelKeyArchive request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyArchiveResponse(AbstractModel):
    """CancelKeyArchive response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of the CMK for which to cancel schedule deletion\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of the CMK for which the schedule deletion is canceled\n        :type KeyId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey request structure.

    """

    def __init__(self):
        """
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1-60 letters, digits, `-`, and `_`, and must begin with a letter or digit. The `kms-` prefix is used for Tencent Cloud products.\n        :type Alias: str\n        :param Description: CMK description of up to 1,024 bytes in length\n        :type Description: str\n        :param KeyUsage: Key purpose. Valid values: `ENCRYPT_DECRYPT` (default value; creating a symmetric key for encryption and decryption), `ASYMMETRIC_DECRYPT_RSA_2048` (creating an RSA2048 asymmetric key for encryption and decryption), `ASYMMETRIC_DECRYPT_SM2` (creating an SM2 asymmetric key for encryption and decryption), and `ASYMMETRIC_SIGN_VERIFY_SM2` (creating an SM2 asymmetric key for signature verification).\n        :type KeyUsage: str\n        :param Type: Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents.\n        :type Type: int\n        :param Tags: Tag list\n        :type Tags: list of Tag\n        """
        self.Alias = None
        self.Description = None
        self.KeyUsage = None
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyResponse(AbstractModel):
    """CreateKey response structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        :param Alias: Alias that makes a key more recognizable and understandable\n        :type Alias: str\n        :param CreateTime: Key creation time in UNIX timestamp format\n        :type CreateTime: int\n        :param Description: CMK description\n        :type Description: str\n        :param KeyState: CMK status\n        :type KeyState: str\n        :param KeyUsage: CMK usage\n        :type KeyUsage: str\n        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error\n        :type TagCode: int\n        :param TagMsg: Tag operation return information\n        :type TagMsg: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class CreateWhiteBoxKeyRequest(AbstractModel):
    """CreateWhiteBoxKey request structure.

    """

    def __init__(self):
        """
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter should be 1 to 60 letters, digits, `-`, and `_`; it must begin with a letter or digit and cannot be left empty.\n        :type Alias: str\n        :param Algorithm: All algorithm types for creating keys. Valid values: AES_256, SM4\n        :type Algorithm: str\n        :param Description: Key description of up to 1024 bytes\n        :type Description: str\n        :param Tags: Tag list\n        :type Tags: list of Tag\n        """
        self.Alias = None
        self.Algorithm = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Algorithm = params.get("Algorithm")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhiteBoxKeyResponse(AbstractModel):
    """CreateWhiteBoxKey response structure.

    """

    def __init__(self):
        """
        :param EncryptKey: Base64-encoded encryption key\n        :type EncryptKey: str\n        :param DecryptKey: Base64-encoded decryption key\n        :type DecryptKey: str\n        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error\n        :type TagCode: int\n        :param TagMsg: Tag operation return message\n        :type TagMsg: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EncryptKey = None
        self.DecryptKey = None
        self.KeyId = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.KeyId = params.get("KeyId")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt request structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: The ciphertext data to be decrypted.\n        :type CiphertextBlob: str\n        :param EncryptionContext: JSON string of key-value pair. If this parameter is specified for `Encrypt`, the same parameter needs to be provided when the `Decrypt` API is called. The maximum length is 1,024 bytes.\n        :type EncryptionContext: str\n        """
        self.CiphertextBlob = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecryptResponse(AbstractModel):
    """Decrypt response structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        :param Plaintext: Decrypted plaintext. This field is Base64-encoded. In order to get the original plaintext, the Base64-decoding is needed\n        :type Plaintext: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial request structure.

    """

    def __init__(self):
        """
        :param KeyId: Specifies the EXTERNAL CMK for which to delete the key material.\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhiteBoxKeyResponse(AbstractModel):
    """DeleteWhiteBoxKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyResponse(AbstractModel):
    """DescribeKey response structure.

    """

    def __init__(self):
        """
        :param KeyMetadata: Key attribute information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self.KeyMetadata = KeyMetadata()
            self.KeyMetadata._deserialize(params.get("KeyMetadata"))
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of IDs of the CMKs to be queried in batches. Up to 100 `KeyId` values are supported in one query.\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys response structure.

    """

    def __init__(self):
        """
        :param KeyMetadatas: List of returned attribute information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyMetadatas: list of KeyMetadata\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDecryptKeyRequest(AbstractModel):
    """DescribeWhiteBoxDecryptKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDecryptKeyResponse(AbstractModel):
    """DescribeWhiteBoxDecryptKey response structure.

    """

    def __init__(self):
        """
        :param DecryptKey: Base64-encoded white-box decryption key\n        :type DecryptKey: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DecryptKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DecryptKey = params.get("DecryptKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints request structure.

    """

    def __init__(self):
        """
        :param KeyId: White-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints response structure.

    """

    def __init__(self):
        """
        :param DeviceFingerprints: Device fingerprint list\n        :type DeviceFingerprints: list of DeviceFingerprint\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DeviceFingerprints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceFingerprints") is not None:
            self.DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self.DeviceFingerprints.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyDetailsRequest(AbstractModel):
    """DescribeWhiteBoxKeyDetails request structure.

    """

    def __init__(self):
        """
        :param KeyStatus: Filter: key status. 0: disabled, 1: enabled\n        :type KeyStatus: int\n        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.\n        :type Offset: int\n        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 0, indicating not to paginate.\n        :type Limit: int\n        :param TagFilters: Tag filter condition\n        :type TagFilters: list of TagFilter\n        """
        self.KeyStatus = None
        self.Offset = None
        self.Limit = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.KeyStatus = params.get("KeyStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyDetailsResponse(AbstractModel):
    """DescribeWhiteBoxKeyDetails response structure.

    """

    def __init__(self):
        """
        :param KeyInfos: White-box key information list\n        :type KeyInfos: list of WhiteboxKeyInfo\n        :param TotalCount: Total number of keys
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfos") is not None:
            self.KeyInfos = []
            for item in params.get("KeyInfos"):
                obj = WhiteboxKeyInfo()
                obj._deserialize(item)
                self.KeyInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyRequest(AbstractModel):
    """DescribeWhiteBoxKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyResponse(AbstractModel):
    """DescribeWhiteBoxKey response structure.

    """

    def __init__(self):
        """
        :param KeyInfo: White-box key information\n        :type KeyInfo: :class:`tencentcloud.kms.v20190118.models.WhiteboxKeyInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfo") is not None:
            self.KeyInfo = WhiteboxKeyInfo()
            self.KeyInfo._deserialize(params.get("KeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxServiceStatusRequest(AbstractModel):
    """DescribeWhiteBoxServiceStatus request structure.

    """


class DescribeWhiteBoxServiceStatusResponse(AbstractModel):
    """DescribeWhiteBoxServiceStatus response structure.

    """

    def __init__(self):
        """
        :param ServiceEnabled: Whether the user's white-box key service is available\n        :type ServiceEnabled: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.RequestId = params.get("RequestId")


class DeviceFingerprint(AbstractModel):
    """Device fingerprint

    """

    def __init__(self):
        """
        :param Identity: Fingerprint information collected by device fingerprint collector. Its format must be in the following regular expression: ^[0-9a-f]{8}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{16}$\n        :type Identity: str\n        :param Description: Description, such as IP and device name. Length limit: 1,024 bytes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        """
        self.Identity = None
        self.Description = None


    def _deserialize(self, params):
        self.Identity = params.get("Identity")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRequest(AbstractModel):
    """DisableKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyResponse(AbstractModel):
    """DisableKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of IDs of the CMKs to be disabled in batches. Up to 100 CMKs are supported at a time\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeysResponse(AbstractModel):
    """DisableKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeyResponse(AbstractModel):
    """DisableWhiteBoxKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeysResponse(AbstractModel):
    """DisableWhiteBoxKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyResponse(AbstractModel):
    """EnableKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of IDs of the CMKs to be enabled in batches. Up to 100 CMKs are supported at a time\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeysResponse(AbstractModel):
    """EnableKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeyResponse(AbstractModel):
    """EnableWhiteBoxKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys request structure.

    """

    def __init__(self):
        """
        :param KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeysResponse(AbstractModel):
    """EnableWhiteBoxKeys response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        :param PlainText: Base64-encoded text to be encrypted. The size of the original text cannot exceed 4 KB.\n        :type PlainText: str\n        :param InitializationVector: Base64-encoded initialization vector of 16 bytes, which will be used by the encryption algorithm. If this parameter is not passed in, the backend service will generate a random one. You should save this value as a parameter for decryption.\n        :type InitializationVector: str\n        """
        self.KeyId = None
        self.PlainText = None
        self.InitializationVector = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PlainText = params.get("PlainText")
        self.InitializationVector = params.get("InitializationVector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptByWhiteBoxResponse(AbstractModel):
    """EncryptByWhiteBox response structure.

    """

    def __init__(self):
        """
        :param InitializationVector: Base64-encoded initialization vector, which will be used by the encryption algorithm. If this parameter is passed in by the caller, it will be returned as-is; otherwise, the backend service will generate a random one and return it.\n        :type InitializationVector: str\n        :param CipherText: Base64-encoded ciphertext after encryption\n        :type CipherText: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InitializationVector = None
        self.CipherText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InitializationVector = params.get("InitializationVector")
        self.CipherText = params.get("CipherText")
        self.RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique ID of the CMK generated by calling the `CreateKey` API\n        :type KeyId: str\n        :param Plaintext: Encrypted plaintext data. This field must be Base64-encoded. The maximum size of the original data is 4 KB\n        :type Plaintext: str\n        :param EncryptionContext: JSON string of key-value pair. If this parameter is specified, the same parameter needs to be provided when the `Decrypt` API is called. It is up to 1,024 characters\n        :type EncryptionContext: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptResponse(AbstractModel):
    """Encrypt response structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: Base64-encoded encrypted ciphertext\n        :type CiphertextBlob: str\n        :param KeyId: Globally unique ID of the CMK used for encryption\n        :type KeyId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        :param KeySpec: Specifies the encryption algorithm and size of the `DataKey`. Valid values: AES_128, AES_256. Either `KeySpec` or `NumberOfBytes` must be specified.\n        :type KeySpec: str\n        :param NumberOfBytes: Length of the `DataKey`. If both `NumberOfBytes` and `KeySpec` are specified, `NumberOfBytes` will prevail. Minimum value: 1; maximum value: 1024. Either `KeySpec` or `NumberOfBytes` must be specified.\n        :type NumberOfBytes: int\n        :param EncryptionContext: JSON string of key-value pair. If this field is used, the same string should be entered when the returned `DataKey` is decrypted.\n        :type EncryptionContext: str\n        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeySpec = params.get("KeySpec")
        self.NumberOfBytes = params.get("NumberOfBytes")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey response structure.

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        :param Plaintext: Plaintext of the generated data key. The plaintext is Base64-encoded and can be used locally after having it Base64-decoded.\n        :type Plaintext: str\n        :param CiphertextBlob: Ciphertext of the data key, which should be kept by yourself. KMS does not host user data keys. You can call the `Decrypt` API to get the plaintext of the data key from `CiphertextBlob`.\n        :type CiphertextBlob: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.CiphertextBlob = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom request structure.

    """

    def __init__(self):
        """
        :param NumberOfBytes: Length of the random number. Minimum value: 1. Maximum value: 1024\n        :type NumberOfBytes: int\n        """
        self.NumberOfBytes = None


    def _deserialize(self, params):
        self.NumberOfBytes = params.get("NumberOfBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom response structure.

    """

    def __init__(self):
        """
        :param Plaintext: Base64-encoded plaintext of the randomly generated number. You need to Base64-decode it to get the plaintext.\n        :type Plaintext: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus response structure.

    """

    def __init__(self):
        """
        :param KeyRotationEnabled: Whether key rotation is enabled\n        :type KeyRotationEnabled: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyRotationEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of a CMK. The CMK for which to get the key parameters must be of the `EXTERNAL` type, i.e., Type = 2 when the CMK is created by the `CreateKey` API.\n        :type KeyId: str\n        :param WrappingAlgorithm: Specifies the algorithm for key material encryption. Currently, `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256` are supported.\n        :type WrappingAlgorithm: str\n        :param WrappingKeySpec: Specifies the type of wrapping key. Currently, only `RSA_2048` is supported.\n        :type WrappingKeySpec: str\n        """
        self.KeyId = None
        self.WrappingAlgorithm = None
        self.WrappingKeySpec = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.WrappingAlgorithm = params.get("WrappingAlgorithm")
        self.WrappingKeySpec = params.get("WrappingKeySpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of a CMK, which is used to specify the CMK into which to import key material.\n        :type KeyId: str\n        :param ImportToken: The token required for importing key material, which is used as a parameter for `ImportKeyMaterial`.\n        :type ImportToken: str\n        :param PublicKey: The Base64-encoded RSA public key used to encrypt key material before importing it with `ImportKeyMaterial`.\n        :type PublicKey: str\n        :param ParametersValidTo: Validity period of the token and public key. A token and public key can only be imported when they are valid. If they are expired, you will need to call the `GetParametersForImport` API again to get a new token and public key.\n        :type ParametersValidTo: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.ImportToken = None
        self.PublicKey = None
        self.ParametersValidTo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ImportToken = params.get("ImportToken")
        self.PublicKey = params.get("PublicKey")
        self.ParametersValidTo = params.get("ParametersValidTo")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID.\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey response structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID.\n        :type KeyId: str\n        :param PublicKey: Base64-encoded public key content.\n        :type PublicKey: str\n        :param PublicKeyPem: Public key content in PEM format.\n        :type PublicKeyPem: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.KeyId = None
        self.PublicKey = None
        self.PublicKeyPem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PublicKey = params.get("PublicKey")
        self.PublicKeyPem = params.get("PublicKeyPem")
        self.RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions request structure.

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions response structure.

    """

    def __init__(self):
        """
        :param Regions: The list of supported regions
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Regions: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        """
        :param ServiceEnabled: Whether the KMS service has been activated. true: activated\n        :type ServiceEnabled: bool\n        :param InvalidType: Service unavailability type. 0: not purchased; 1: normal; 2: suspended due to arrears; 3: resource released\n        :type InvalidType: int\n        :param UserLevel: 0: Basic Edition, 1: Ultimate Edition\n        :type UserLevel: int\n        :param ProExpireTime: Ultimate Edition expiration time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProExpireTime: int\n        :param ProRenewFlag: Whether to automatically renew Ultimate Edition. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProRenewFlag: int\n        :param ProResourceId: Unique ID of the Ultimate Edition purchase record. If the Ultimate Edition is not activated, the returned value will be null.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProResourceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.UserLevel = None
        self.ProExpireTime = None
        self.ProRenewFlag = None
        self.ProResourceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.UserLevel = params.get("UserLevel")
        self.ProExpireTime = params.get("ProExpireTime")
        self.ProRenewFlag = params.get("ProRenewFlag")
        self.ProResourceId = params.get("ProResourceId")
        self.RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial request structure.

    """

    def __init__(self):
        """
        :param EncryptedKeyMaterial: Base64-encoded key material that encrypted with the `PublicKey` returned by `GetParametersForImport`. For the KMS of SM-CRYPTO version, the length of the key material should be 128 bits, while for KMS of FIPS-compliant version, the length should be 256 bits.\n        :type EncryptedKeyMaterial: str\n        :param ImportToken: Import token obtained by calling `GetParametersForImport`.\n        :type ImportToken: str\n        :param KeyId: Specifies the CMK into which to import key material, which must be the same as the one specified by `GetParametersForImport`.\n        :type KeyId: str\n        :param ValidTo: Unix timestamp of the key material's expiration time. If this value is empty or 0, the key material will never expire. To specify the expiration time, it should be later than the current time. Maximum value: 2147443200.\n        :type ValidTo: int\n        """
        self.EncryptedKeyMaterial = None
        self.ImportToken = None
        self.KeyId = None
        self.ValidTo = None


    def _deserialize(self, params):
        self.EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self.ImportToken = params.get("ImportToken")
        self.KeyId = params.get("KeyId")
        self.ValidTo = params.get("ValidTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Key(AbstractModel):
    """Returned CMK list information

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID.\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyMetadata(AbstractModel):
    """CMK attribute information

    """

    def __init__(self):
        """
        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        :param Alias: Alias that makes a key more recognizable and understandable\n        :type Alias: str\n        :param CreateTime: Key creation time\n        :type CreateTime: int\n        :param Description: CMK description\n        :type Description: str\n        :param KeyState: CMK status. Valid values: Enabled, Disabled, PendingDelete, PendingImport, Archived.\n        :type KeyState: str\n        :param KeyUsage: CMK purpose. Valid values: `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, and `ASYMMETRIC_SIGN_VERIFY_SM2`.\n        :type KeyUsage: str\n        :param Type: CMK type. 2: FIPS-compliant; 4: SM-CRYPTO\n        :type Type: int\n        :param CreatorUin: Creator\n        :type CreatorUin: int\n        :param KeyRotationEnabled: Whether key rotation is enabled\n        :type KeyRotationEnabled: bool\n        :param Owner: CMK creator. The value of this parameter is `user` if the CMK is created by the user, or the corresponding service name if it is created automatically by an authorized Tencent Cloud service.\n        :type Owner: str\n        :param NextRotateTime: Time of next rotation if key rotation is enabled\n        :type NextRotateTime: int\n        :param DeletionDate: Scheduled deletion time\n        :type DeletionDate: int\n        :param Origin: CMK key material type. TENCENT_KMS: created by KMS; EXTERNAL: imported by user.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Origin: str\n        :param ValidTo: It's valid when `Origin` is `EXTERNAL`, indicating the expiration date of key material. 0 means valid forever.
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ValidTo: int\n        :param ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`.\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.Type = None
        self.CreatorUin = None
        self.KeyRotationEnabled = None
        self.Owner = None
        self.NextRotateTime = None
        self.DeletionDate = None
        self.Origin = None
        self.ValidTo = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        self.CreatorUin = params.get("CreatorUin")
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.Owner = params.get("Owner")
        self.NextRotateTime = params.get("NextRotateTime")
        self.DeletionDate = params.get("DeletionDate")
        self.Origin = params.get("Origin")
        self.ValidTo = params.get("ValidTo")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlgorithmsRequest(AbstractModel):
    """ListAlgorithms request structure.

    """


class ListAlgorithmsResponse(AbstractModel):
    """ListAlgorithms response structure.

    """

    def __init__(self):
        """
        :param SymmetricAlgorithms: Symmetric encryption algorithms supported in this region\n        :type SymmetricAlgorithms: list of AlgorithmInfo\n        :param AsymmetricAlgorithms: Asymmetric encryption algorithms supported in this region\n        :type AsymmetricAlgorithms: list of AlgorithmInfo\n        :param AsymmetricSignVerifyAlgorithms: Asymmetric signature verification algorithms supported in the current region\n        :type AsymmetricSignVerifyAlgorithms: list of AlgorithmInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SymmetricAlgorithms = None
        self.AsymmetricAlgorithms = None
        self.AsymmetricSignVerifyAlgorithms = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self.SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self.AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricAlgorithms.append(obj)
        if params.get("AsymmetricSignVerifyAlgorithms") is not None:
            self.AsymmetricSignVerifyAlgorithms = []
            for item in params.get("AsymmetricSignVerifyAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricSignVerifyAlgorithms.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail request structure.

    """

    def __init__(self):
        """
        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.\n        :type Offset: int\n        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200.\n        :type Limit: int\n        :param Role: Filters by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service.\n        :type Role: int\n        :param OrderType: Sorts by CMK creation time. 0: descending; 1: ascending\n        :type OrderType: int\n        :param KeyState: Filters by CMK status. 0: all CMKs; 1: CMKs in `Enabled` status only; 2: CMKs in `Disabled` status only; 3: CMKs in `PendingDelete` status only (i.e., keys with schedule deletion enabled); 4: CMKs in `PendingImport` status only; 5: CMKs in `Archived` status only.\n        :type KeyState: int\n        :param SearchKeyAlias: Performs a fuzzy query by `KeyId` or `Alias`\n        :type SearchKeyAlias: str\n        :param Origin: Filters by CMK type. "TENCENT_KMS" indicates to filter CMKs whose key materials are created by KMS; "EXTERNAL" indicates to filter CMKs of `EXTERNAL` type whose key materials are imported by users; "ALL" or empty indicates to filter CMKs of both types. This value is case-sensitive.\n        :type Origin: str\n        :param KeyUsage: Filter by the `KeyUsage` field of CMKs. Valid values: `ALL` (filtering all CMKs), `ENCRYPT_DECRYPT` (it will be used when the parameter is left empty), `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, and `ASYMMETRIC_SIGN_VERIFY_SM2`.\n        :type KeyUsage: str\n        :param TagFilters: Tag filter condition\n        :type TagFilters: list of TagFilter\n        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None
        self.Origin = None
        self.KeyUsage = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")
        self.Origin = params.get("Origin")
        self.KeyUsage = params.get("KeyUsage")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of CMKs\n        :type TotalCount: int\n        :param KeyMetadatas: List of returned attribute information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyMetadatas: list of KeyMetadata\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys request structure.

    """

    def __init__(self):
        """
        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0\n        :type Offset: int\n        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200\n        :type Limit: int\n        :param Role: Filter by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service\n        :type Role: int\n        """
        self.Offset = None
        self.Limit = None
        self.Role = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeysResponse(AbstractModel):
    """ListKeys response structure.

    """

    def __init__(self):
        """
        :param Keys: CMK list array\n        :type Keys: list of Key\n        :param TotalCount: Total number of CMKs\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Keys = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class OverwriteWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints request structure.

    """

    def __init__(self):
        """
        :param KeyId: White-box key ID\n        :type KeyId: str\n        :param DeviceFingerprints: Device fingerprint list. If the list is empty, it means to delete all fingerprint information corresponding to the key. There can be up to 200 entries in the list.\n        :type DeviceFingerprints: list of DeviceFingerprint\n        """
        self.KeyId = None
        self.DeviceFingerprints = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        if params.get("DeviceFingerprints") is not None:
            self.DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self.DeviceFingerprints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverwriteWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt request structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: Ciphertext to be re-encrypted\n        :type CiphertextBlob: str\n        :param DestinationKeyId: CMK used for re-encryption. If this parameter is empty, the ciphertext will be re-encrypted by using the original CMK (as long as the key is not rotated, the ciphertext will not be refreshed)\n        :type DestinationKeyId: str\n        :param SourceEncryptionContext: JSON string of the key-value pair used during ciphertext encryption by `CiphertextBlob`. If not used during encryption, this parameter will be empty\n        :type SourceEncryptionContext: str\n        :param DestinationEncryptionContext: JSON string of the key-value pair used during re-encryption. If this field is used, the same string should be entered when the returned new ciphertext is decrypted\n        :type DestinationEncryptionContext: str\n        """
        self.CiphertextBlob = None
        self.DestinationKeyId = None
        self.SourceEncryptionContext = None
        self.DestinationEncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.DestinationKeyId = params.get("DestinationKeyId")
        self.SourceEncryptionContext = params.get("SourceEncryptionContext")
        self.DestinationEncryptionContext = params.get("DestinationEncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReEncryptResponse(AbstractModel):
    """ReEncrypt response structure.

    """

    def __init__(self):
        """
        :param CiphertextBlob: Re-encrypted ciphertext\n        :type CiphertextBlob: str\n        :param KeyId: CMK used for re-encryption\n        :type KeyId: str\n        :param SourceKeyId: CMK used by ciphertext before re-encryption\n        :type SourceKeyId: str\n        :param ReEncrypted: `true` indicates that the ciphertext has been re-encrypted. When re-encryption is initiated by using the same CMK, as long as the CMK is not rotated, no actual re-encryption will be performed, and the original ciphertext will be returned\n        :type ReEncrypted: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.SourceKeyId = None
        self.ReEncrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.SourceKeyId = params.get("SourceKeyId")
        self.ReEncrypted = params.get("ReEncrypted")
        self.RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique CMK ID\n        :type KeyId: str\n        :param PendingWindowInDays: Schedule deletion time range. Value range: [7,30]\n        :type PendingWindowInDays: int\n        """
        self.KeyId = None
        self.PendingWindowInDays = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PendingWindowInDays = params.get("PendingWindowInDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion response structure.

    """

    def __init__(self):
        """
        :param DeletionDate: Schedule deletion execution time\n        :type DeletionDate: int\n        :param KeyId: Unique ID of the CMK scheduled for deletion\n        :type KeyId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DeletionDate = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionDate = params.get("DeletionDate")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class SignByAsymmetricKeyRequest(AbstractModel):
    """SignByAsymmetricKey request structure.

    """

    def __init__(self):
        """
        :param Algorithm: Signature algorithm. Supported algorithm: SM2DSA.\n        :type Algorithm: str\n        :param Message: The original message or message abstract. For an original message, the length before Base64 encoding can contain up to 4,096 bytes. For a message abstract, the SM2 signature algorithm only supports 32-byte (before Base64 encoding) message abstracts.\n        :type Message: str\n        :param KeyId: Unique ID of a key\n        :type KeyId: str\n        :param MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.\n        :type MessageType: str\n        """
        self.Algorithm = None
        self.Message = None
        self.KeyId = None
        self.MessageType = None


    def _deserialize(self, params):
        self.Algorithm = params.get("Algorithm")
        self.Message = params.get("Message")
        self.KeyId = params.get("KeyId")
        self.MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignByAsymmetricKeyResponse(AbstractModel):
    """SignByAsymmetricKey response structure.

    """

    def __init__(self):
        """
        :param Signature: Base64-encoded signature\n        :type Signature: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Signature = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Signature = params.get("Signature")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag key and tag value

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filter

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: list of str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceRequest(AbstractModel):
    """UnbindCloudResource request structure.

    """

    def __init__(self):
        """
        :param KeyId: CMK ID\n        :type KeyId: str\n        :param ProductId: Unique ID of a Tencent Cloud service\n        :type ProductId: str\n        :param ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.ProductId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ProductId = params.get("ProductId")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceResponse(AbstractModel):
    """UnbindCloudResource response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        """
        :param Alias: New alias containing 1-60 characters or digits\n        :type Alias: str\n        :param KeyId: Globally unique CMK ID\n        :type KeyId: str\n        """
        self.Alias = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription request structure.

    """

    def __init__(self):
        """
        :param Description: New description of up to 1,024 bytes in length\n        :type Description: str\n        :param KeyId: ID of the CMK for which to modify the description\n        :type KeyId: str\n        """
        self.Description = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VerifyByAsymmetricKeyRequest(AbstractModel):
    """VerifyByAsymmetricKey request structure.

    """

    def __init__(self):
        """
        :param KeyId: Unique ID of a key\n        :type KeyId: str\n        :param SignatureValue: Signature value, which is generated by calling the KMS signature API.\n        :type SignatureValue: str\n        :param Message: The original message or message abstract. For an original message, the length before Base64 encoding can contain up to 4,096 bytes. For a message abstract, the SM2 signature algorithm only supports 32-byte (before Base64 encoding) message abstracts.\n        :type Message: str\n        :param Algorithm: Signature algorithm. Supported algorithm: SM2DSA.\n        :type Algorithm: str\n        :param MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.\n        :type MessageType: str\n        """
        self.KeyId = None
        self.SignatureValue = None
        self.Message = None
        self.Algorithm = None
        self.MessageType = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.SignatureValue = params.get("SignatureValue")
        self.Message = params.get("Message")
        self.Algorithm = params.get("Algorithm")
        self.MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyByAsymmetricKeyResponse(AbstractModel):
    """VerifyByAsymmetricKey response structure.

    """

    def __init__(self):
        """
        :param SignatureValid: Whether the signature is valid.\n        :type SignatureValid: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SignatureValid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignatureValid = params.get("SignatureValid")
        self.RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """White-box key information

    """

    def __init__(self):
        """
        :param KeyId: Globally unique white-box key ID\n        :type KeyId: str\n        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1 to 60 letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.\n        :type Alias: str\n        :param CreatorUin: Creator\n        :type CreatorUin: int\n        :param Description: Key description information\n        :type Description: str\n        :param CreateTime: Key creation time in Unix timestamp\n        :type CreateTime: int\n        :param Status: White-box key status. Valid values: Enabled, Disabled\n        :type Status: str\n        :param OwnerUin: Creator\n        :type OwnerUin: int\n        :param Algorithm: Key algorithm type\n        :type Algorithm: str\n        :param EncryptKey: Base64-encoded white-box encryption key\n        :type EncryptKey: str\n        :param DecryptKey: Base64-encoded white-box decryption key\n        :type DecryptKey: str\n        :param ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`\n        :type ResourceId: str\n        :param DeviceFingerprintBind: Whether there is a device fingerprint bound to the current key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeviceFingerprintBind: bool\n        """
        self.KeyId = None
        self.Alias = None
        self.CreatorUin = None
        self.Description = None
        self.CreateTime = None
        self.Status = None
        self.OwnerUin = None
        self.Algorithm = None
        self.EncryptKey = None
        self.DecryptKey = None
        self.ResourceId = None
        self.DeviceFingerprintBind = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreatorUin = params.get("CreatorUin")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.OwnerUin = params.get("OwnerUin")
        self.Algorithm = params.get("Algorithm")
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.ResourceId = params.get("ResourceId")
        self.DeviceFingerprintBind = params.get("DeviceFingerprintBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        