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
        r"""
        :param KeyUsage: Algorithm ID
        :type KeyUsage: str
        :param Algorithm: Algorithm name
        :type Algorithm: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`
        :type Ciphertext: str
        :param Algorithm: Corresponding algorithm when a public key is used for encryption. Valid values: RSAES_PKCS1_V1_5, RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256
        :type Algorithm: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`, whose length cannot exceed 256 bytes.
        :type Ciphertext: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: CMK ID
        :type KeyId: str
        :param ProductId: Unique ID of a Tencent Cloud service
        :type ProductId: str
        :param ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.
        :type ResourceId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyArchiveRequest(AbstractModel):
    """CancelKeyArchive request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique ID of the CMK for which to cancel schedule deletion
        :type KeyId: str
        """
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
        r"""
        :param KeyId: Unique ID of the CMK for which the schedule deletion is canceled
        :type KeyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey request structure.

    """

    def __init__(self):
        r"""
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1-60 letters, digits, `-`, and `_`, and must begin with a letter or digit. The `kms-` prefix is used for Tencent Cloud products.
        :type Alias: str
        :param Description: CMK description of up to 1,024 bytes in length
        :type Description: str
        :param KeyUsage: Key purpose. Valid values: `ENCRYPT_DECRYPT` (default value; creating a symmetric key for encryption and decryption), `ASYMMETRIC_DECRYPT_RSA_2048` (creating an RSA2048 asymmetric key for encryption and decryption), `ASYMMETRIC_DECRYPT_SM2` (creating an SM2 asymmetric key for encryption and decryption), and `ASYMMETRIC_SIGN_VERIFY_SM2` (creating an SM2 asymmetric key for signature verification).
        :type KeyUsage: str
        :param Type: Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents.
        :type Type: int
        :param Tags: Tag list
        :type Tags: list of Tag
        """
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
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        :param Alias: Alias that makes a key more recognizable and understandable
        :type Alias: str
        :param CreateTime: Key creation time in UNIX timestamp format
        :type CreateTime: int
        :param Description: CMK description
        :type Description: str
        :param KeyState: CMK status
        :type KeyState: str
        :param KeyUsage: CMK usage
        :type KeyUsage: str
        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error
        :type TagCode: int
        :param TagMsg: Tag operation return information
        :type TagMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter should be 1 to 60 letters, digits, `-`, and `_`; it must begin with a letter or digit and cannot be left empty.
        :type Alias: str
        :param Algorithm: All algorithm types for creating keys. Valid values: AES_256, SM4
        :type Algorithm: str
        :param Description: Key description of up to 1024 bytes
        :type Description: str
        :param Tags: Tag list
        :type Tags: list of Tag
        """
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
        r"""
        :param EncryptKey: Base64-encoded encryption key
        :type EncryptKey: str
        :param DecryptKey: Base64-encoded decryption key
        :type DecryptKey: str
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error
        :type TagCode: int
        :param TagMsg: Tag operation return message
        :type TagMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param CiphertextBlob: The ciphertext data to be decrypted.
        :type CiphertextBlob: str
        :param EncryptionContext: JSON string of key-value pair. If this parameter is specified for `Encrypt`, the same parameter needs to be provided when the `Decrypt` API is called. The maximum length is 1,024 bytes.
        :type EncryptionContext: str
        """
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
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        :param Plaintext: Decrypted plaintext. This field is Base64-encoded. In order to get the original plaintext, the Base64-decoding is needed
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Specifies the EXTERNAL CMK for which to delete the key material.
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param KeyMetadata: Key attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyIds: List of IDs of the CMKs to be queried in batches. Up to 100 `KeyId` values are supported in one query.
        :type KeyIds: list of str
        """
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
        r"""
        :param KeyMetadatas: List of returned attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
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
        r"""
        :param DecryptKey: Base64-encoded white-box decryption key
        :type DecryptKey: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DecryptKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DecryptKey = params.get("DecryptKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: White-box key ID
        :type KeyId: str
        """
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
        r"""
        :param DeviceFingerprints: Device fingerprint list
        :type DeviceFingerprints: list of DeviceFingerprint
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyStatus: Filter: key status. 0: disabled, 1: enabled
        :type KeyStatus: int
        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.
        :type Offset: int
        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 0, indicating not to paginate.
        :type Limit: int
        :param TagFilters: Tag filter condition
        :type TagFilters: list of TagFilter
        """
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
        r"""
        :param KeyInfos: White-box key information list
        :type KeyInfos: list of WhiteboxKeyInfo
        :param TotalCount: Total number of keys
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
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
        r"""
        :param KeyInfo: White-box key information
        :type KeyInfo: :class:`tencentcloud.kms.v20190118.models.WhiteboxKeyInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param ServiceEnabled: Whether the user's white-box key service is available
        :type ServiceEnabled: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.RequestId = params.get("RequestId")


class DeviceFingerprint(AbstractModel):
    """Device fingerprint

    """

    def __init__(self):
        r"""
        :param Identity: Fingerprint information collected by device fingerprint collector. Its format must be in the following regular expression: ^[0-9a-f]{8}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{16}$
        :type Identity: str
        :param Description: Description, such as IP and device name. Length limit: 1,024 bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: List of IDs of the CMKs to be disabled in batches. Up to 100 CMKs are supported at a time
        :type KeyIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.
        :type KeyIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: List of IDs of the CMKs to be enabled in batches. Up to 100 CMKs are supported at a time
        :type KeyIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.
        :type KeyIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param PlainText: Base64-encoded text to be encrypted. The size of the original text cannot exceed 4 KB.
        :type PlainText: str
        :param InitializationVector: Base64-encoded initialization vector of 16 bytes, which will be used by the encryption algorithm. If this parameter is not passed in, the backend service will generate a random one. You should save this value as a parameter for decryption.
        :type InitializationVector: str
        """
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
        r"""
        :param InitializationVector: Base64-encoded initialization vector, which will be used by the encryption algorithm. If this parameter is passed in by the caller, it will be returned as-is; otherwise, the backend service will generate a random one and return it.
        :type InitializationVector: str
        :param CipherText: Base64-encoded ciphertext after encryption
        :type CipherText: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Globally unique ID of the CMK generated by calling the `CreateKey` API
        :type KeyId: str
        :param Plaintext: Encrypted plaintext data. This field must be Base64-encoded. The maximum size of the original data is 4 KB
        :type Plaintext: str
        :param EncryptionContext: JSON string of key-value pair. If this parameter is specified, the same parameter needs to be provided when the `Decrypt` API is called. It is up to 1,024 characters
        :type EncryptionContext: str
        """
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
        r"""
        :param CiphertextBlob: Base64-encoded encrypted ciphertext
        :type CiphertextBlob: str
        :param KeyId: Globally unique ID of the CMK used for encryption
        :type KeyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        :param KeySpec: Specifies the encryption algorithm and size of the `DataKey`. Valid values: AES_128, AES_256. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type KeySpec: str
        :param NumberOfBytes: Length of the `DataKey`. If both `NumberOfBytes` and `KeySpec` are specified, `NumberOfBytes` will prevail. Minimum value: 1; maximum value: 1024. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type NumberOfBytes: int
        :param EncryptionContext: JSON string of key-value pair. If this field is used, the same string should be entered when the returned `DataKey` is decrypted.
        :type EncryptionContext: str
        """
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
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        :param Plaintext: Plaintext of the generated data key. The plaintext is Base64-encoded and can be used locally after having it Base64-decoded.
        :type Plaintext: str
        :param CiphertextBlob: Ciphertext of the data key, which should be kept by yourself. KMS does not host user data keys. You can call the `Decrypt` API to get the plaintext of the data key from `CiphertextBlob`.
        :type CiphertextBlob: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param NumberOfBytes: Length of the random number. Minimum value: 1. Maximum value: 1024
        :type NumberOfBytes: int
        """
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
        r"""
        :param Plaintext: Base64-encoded plaintext of the randomly generated number. You need to Base64-decode it to get the plaintext.
        :type Plaintext: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param KeyRotationEnabled: Whether key rotation is enabled
        :type KeyRotationEnabled: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyRotationEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique ID of a CMK. The CMK for which to get the key parameters must be of the `EXTERNAL` type, i.e., Type = 2 when the CMK is created by the `CreateKey` API.
        :type KeyId: str
        :param WrappingAlgorithm: Specifies the algorithm for key material encryption. Currently, `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256` are supported.
        :type WrappingAlgorithm: str
        :param WrappingKeySpec: Specifies the type of wrapping key. Currently, only `RSA_2048` is supported.
        :type WrappingKeySpec: str
        """
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
        r"""
        :param KeyId: Unique ID of a CMK, which is used to specify the CMK into which to import key material.
        :type KeyId: str
        :param ImportToken: The token required for importing key material, which is used as a parameter for `ImportKeyMaterial`.
        :type ImportToken: str
        :param PublicKey: The Base64-encoded RSA public key used to encrypt key material before importing it with `ImportKeyMaterial`.
        :type PublicKey: str
        :param ParametersValidTo: Validity period of the token and public key. A token and public key can only be imported when they are valid. If they are expired, you will need to call the `GetParametersForImport` API again to get a new token and public key.
        :type ParametersValidTo: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Unique CMK ID.
        :type KeyId: str
        """
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
        r"""
        :param KeyId: Unique CMK ID.
        :type KeyId: str
        :param PublicKey: Base64-encoded public key content.
        :type PublicKey: str
        :param PublicKeyPem: Public key content in PEM format.
        :type PublicKeyPem: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Regions: The list of supported regions
Note: this field may return null, indicating that no valid values can be obtained.
        :type Regions: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param ServiceEnabled: Whether the KMS service has been activated. true: activated
        :type ServiceEnabled: bool
        :param InvalidType: Service unavailability type. 0: not purchased; 1: normal; 2: suspended due to arrears; 3: resource released
        :type InvalidType: int
        :param UserLevel: 0: Basic Edition, 1: Ultimate Edition
        :type UserLevel: int
        :param ProExpireTime: Ultimate Edition expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProExpireTime: int
        :param ProRenewFlag: Whether to automatically renew Ultimate Edition. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProRenewFlag: int
        :param ProResourceId: Unique ID of the Ultimate Edition purchase record. If the Ultimate Edition is not activated, the returned value will be null.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProResourceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param EncryptedKeyMaterial: Base64-encoded key material that encrypted with the `PublicKey` returned by `GetParametersForImport`. For the KMS of SM-CRYPTO version, the length of the key material should be 128 bits, while for KMS of FIPS-compliant version, the length should be 256 bits.
        :type EncryptedKeyMaterial: str
        :param ImportToken: Import token obtained by calling `GetParametersForImport`.
        :type ImportToken: str
        :param KeyId: Specifies the CMK into which to import key material, which must be the same as the one specified by `GetParametersForImport`.
        :type KeyId: str
        :param ValidTo: Unix timestamp of the key material's expiration time. If this value is empty or 0, the key material will never expire. To specify the expiration time, it should be later than the current time. Maximum value: 2147443200.
        :type ValidTo: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Key(AbstractModel):
    """Returned CMK list information

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique CMK ID.
        :type KeyId: str
        """
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
        r"""
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        :param Alias: Alias that makes a key more recognizable and understandable
        :type Alias: str
        :param CreateTime: Key creation time
        :type CreateTime: int
        :param Description: CMK description
        :type Description: str
        :param KeyState: CMK status. Valid values: Enabled, Disabled, PendingDelete, PendingImport, Archived.
        :type KeyState: str
        :param KeyUsage: CMK purpose. Valid values: `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, and `ASYMMETRIC_SIGN_VERIFY_SM2`.
        :type KeyUsage: str
        :param Type: CMK type. 2: FIPS-compliant; 4: SM-CRYPTO
        :type Type: int
        :param CreatorUin: Creator
        :type CreatorUin: int
        :param KeyRotationEnabled: Whether key rotation is enabled
        :type KeyRotationEnabled: bool
        :param Owner: CMK creator. The value of this parameter is `user` if the CMK is created by the user, or the corresponding service name if it is created automatically by an authorized Tencent Cloud service.
        :type Owner: str
        :param NextRotateTime: Time of next rotation if key rotation is enabled
        :type NextRotateTime: int
        :param DeletionDate: Scheduled deletion time
        :type DeletionDate: int
        :param Origin: CMK key material type. TENCENT_KMS: created by KMS; EXTERNAL: imported by user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: str
        :param ValidTo: It's valid when `Origin` is `EXTERNAL`, indicating the expiration date of key material. 0 means valid forever.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidTo: int
        :param ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`.
        :type ResourceId: str
        """
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
        r"""
        :param SymmetricAlgorithms: Symmetric encryption algorithms supported in this region
        :type SymmetricAlgorithms: list of AlgorithmInfo
        :param AsymmetricAlgorithms: Asymmetric encryption algorithms supported in this region
        :type AsymmetricAlgorithms: list of AlgorithmInfo
        :param AsymmetricSignVerifyAlgorithms: Asymmetric signature verification algorithms supported in the current region
        :type AsymmetricSignVerifyAlgorithms: list of AlgorithmInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.
        :type Offset: int
        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200.
        :type Limit: int
        :param Role: Filters by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service.
        :type Role: int
        :param OrderType: Sorts by CMK creation time. 0: descending; 1: ascending
        :type OrderType: int
        :param KeyState: Filters by CMK status. 0: all CMKs; 1: CMKs in `Enabled` status only; 2: CMKs in `Disabled` status only; 3: CMKs in `PendingDelete` status only (i.e., keys with schedule deletion enabled); 4: CMKs in `PendingImport` status only; 5: CMKs in `Archived` status only.
        :type KeyState: int
        :param SearchKeyAlias: Performs a fuzzy query by `KeyId` or `Alias`
        :type SearchKeyAlias: str
        :param Origin: Filters by CMK type. "TENCENT_KMS" indicates to filter CMKs whose key materials are created by KMS; "EXTERNAL" indicates to filter CMKs of `EXTERNAL` type whose key materials are imported by users; "ALL" or empty indicates to filter CMKs of both types. This value is case-sensitive.
        :type Origin: str
        :param KeyUsage: Filter by the `KeyUsage` field of CMKs. Valid values: `ALL` (filtering all CMKs), `ENCRYPT_DECRYPT` (it will be used when the parameter is left empty), `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, and `ASYMMETRIC_SIGN_VERIFY_SM2`.
        :type KeyUsage: str
        :param TagFilters: Tag filter condition
        :type TagFilters: list of TagFilter
        """
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
        r"""
        :param TotalCount: Total number of CMKs
        :type TotalCount: int
        :param KeyMetadatas: List of returned attribute information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0
        :type Offset: int
        :param Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200
        :type Limit: int
        :param Role: Filter by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service
        :type Role: int
        """
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
        r"""
        :param Keys: CMK list array
        :type Keys: list of Key
        :param TotalCount: Total number of CMKs
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: White-box key ID
        :type KeyId: str
        :param DeviceFingerprints: Device fingerprint list. If the list is empty, it means to delete all fingerprint information corresponding to the key. There can be up to 200 entries in the list.
        :type DeviceFingerprints: list of DeviceFingerprint
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt request structure.

    """

    def __init__(self):
        r"""
        :param CiphertextBlob: Ciphertext to be re-encrypted
        :type CiphertextBlob: str
        :param DestinationKeyId: CMK used for re-encryption. If this parameter is empty, the ciphertext will be re-encrypted by using the original CMK (as long as the key is not rotated, the ciphertext will not be refreshed)
        :type DestinationKeyId: str
        :param SourceEncryptionContext: JSON string of the key-value pair used during ciphertext encryption by `CiphertextBlob`. If not used during encryption, this parameter will be empty
        :type SourceEncryptionContext: str
        :param DestinationEncryptionContext: JSON string of the key-value pair used during re-encryption. If this field is used, the same string should be entered when the returned new ciphertext is decrypted
        :type DestinationEncryptionContext: str
        """
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
        r"""
        :param CiphertextBlob: Re-encrypted ciphertext
        :type CiphertextBlob: str
        :param KeyId: CMK used for re-encryption
        :type KeyId: str
        :param SourceKeyId: CMK used by ciphertext before re-encryption
        :type SourceKeyId: str
        :param ReEncrypted: `true` indicates that the ciphertext has been re-encrypted. When re-encryption is initiated by using the same CMK, as long as the CMK is not rotated, no actual re-encryption will be performed, and the original ciphertext will be returned
        :type ReEncrypted: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param KeyId: Unique CMK ID
        :type KeyId: str
        :param PendingWindowInDays: Schedule deletion time range. Value range: [7,30]
        :type PendingWindowInDays: int
        """
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
        r"""
        :param DeletionDate: Schedule deletion execution time
        :type DeletionDate: int
        :param KeyId: Unique ID of the CMK scheduled for deletion
        :type KeyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Algorithm: Signature algorithm. Supported algorithm: SM2DSA.
        :type Algorithm: str
        :param Message: The original message or message abstract. For an original message, the length before Base64 encoding can contain up to 4,096 bytes. For a message abstract, the SM2 signature algorithm only supports 32-byte (before Base64 encoding) message abstracts.
        :type Message: str
        :param KeyId: Unique ID of a key
        :type KeyId: str
        :param MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.
        :type MessageType: str
        """
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
        r"""
        :param Signature: Base64-encoded signature
        :type Signature: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Signature = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Signature = params.get("Signature")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag key and tag value

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
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
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: list of str
        """
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
        r"""
        :param KeyId: CMK ID
        :type KeyId: str
        :param ProductId: Unique ID of a Tencent Cloud service
        :type ProductId: str
        :param ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.
        :type ResourceId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        r"""
        :param Alias: New alias containing 1-60 characters or digits
        :type Alias: str
        :param KeyId: Globally unique CMK ID
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription request structure.

    """

    def __init__(self):
        r"""
        :param Description: New description of up to 1,024 bytes in length
        :type Description: str
        :param KeyId: ID of the CMK for which to modify the description
        :type KeyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VerifyByAsymmetricKeyRequest(AbstractModel):
    """VerifyByAsymmetricKey request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Unique ID of a key
        :type KeyId: str
        :param SignatureValue: Signature value, which is generated by calling the KMS signature API.
        :type SignatureValue: str
        :param Message: The original message or message abstract. For an original message, the length before Base64 encoding can contain up to 4,096 bytes. For a message abstract, the SM2 signature algorithm only supports 32-byte (before Base64 encoding) message abstracts.
        :type Message: str
        :param Algorithm: Signature algorithm. Supported algorithm: SM2DSA.
        :type Algorithm: str
        :param MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.
        :type MessageType: str
        """
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
        r"""
        :param SignatureValid: Whether the signature is valid.
        :type SignatureValid: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SignatureValid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignatureValid = params.get("SignatureValid")
        self.RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """White-box key information

    """

    def __init__(self):
        r"""
        :param KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1 to 60 letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type Alias: str
        :param CreatorUin: Creator
        :type CreatorUin: int
        :param Description: Key description information
        :type Description: str
        :param CreateTime: Key creation time in Unix timestamp
        :type CreateTime: int
        :param Status: White-box key status. Valid values: Enabled, Disabled
        :type Status: str
        :param OwnerUin: Creator
        :type OwnerUin: int
        :param Algorithm: Key algorithm type
        :type Algorithm: str
        :param EncryptKey: Base64-encoded white-box encryption key
        :type EncryptKey: str
        :param DecryptKey: Base64-encoded white-box decryption key
        :type DecryptKey: str
        :param ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`
        :type ResourceId: str
        :param DeviceFingerprintBind: Whether there is a device fingerprint bound to the current key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeviceFingerprintBind: bool
        """
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
        