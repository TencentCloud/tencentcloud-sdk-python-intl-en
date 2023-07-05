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
        :param _KeyUsage: Algorithm ID
        :type KeyUsage: str
        :param _Algorithm: Algorithm name
        :type Algorithm: str
        """
        self._KeyUsage = None
        self._Algorithm = None

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm


    def _deserialize(self, params):
        self._KeyUsage = params.get("KeyUsage")
        self._Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyRequest(AbstractModel):
    """ArchiveKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyResponse(AbstractModel):
    """ArchiveKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`
        :type Ciphertext: str
        :param _Algorithm: Corresponding algorithm when a public key is used for encryption. Valid values: RSAES_PKCS1_V1_5, RSAES_OAEP_SHA_1, RSAES_OAEP_SHA_256
        :type Algorithm: str
        """
        self._KeyId = None
        self._Ciphertext = None
        self._Algorithm = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Ciphertext = params.get("Ciphertext")
        self._Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _Ciphertext: Base64-encoded ciphertext encrypted with `PublicKey`, whose length cannot exceed 256 bytes.
        :type Ciphertext: str
        """
        self._KeyId = None
        self._Ciphertext = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Ciphertext = params.get("Ciphertext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _Plaintext: Base64-encoded plaintext after decryption
        :type Plaintext: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class BindCloudResourceRequest(AbstractModel):
    """BindCloudResource request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK ID
        :type KeyId: str
        :param _ProductId: Unique ID of a Tencent Cloud service
        :type ProductId: str
        :param _ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.
        :type ResourceId: str
        """
        self._KeyId = None
        self._ProductId = None
        self._ResourceId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ProductId = params.get("ProductId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudResourceResponse(AbstractModel):
    """BindCloudResource response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CancelKeyArchiveRequest(AbstractModel):
    """CancelKeyArchive request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyArchiveResponse(AbstractModel):
    """CancelKeyArchive response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique ID of the CMK for which to cancel schedule deletion
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique ID of the CMK for which the schedule deletion is canceled
        :type KeyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey request structure.

    """

    def __init__(self):
        r"""
        :param _Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1-60 letters, digits, `-`, and `_`, and must begin with a letter or digit. The `kms-` prefix is used for Tencent Cloud products.
        :type Alias: str
        :param _Description: CMK description of up to 1,024 bytes in length
        :type Description: str
        :param _KeyUsage: Defines the purpose of the key. The valid values are as follows: `ENCRYPT_DECRYPT` (default): creates a symmetric encryption/decryption key; `ASYMMETRIC_DECRYPT_RSA_2048`: creates an asymmetric encryption/decryption 2048-bit RSA key; `ASYMMETRIC_DECRYPT_SM2`: creates an asymmetric encryption/decryption SM2 key; `ASYMMETRIC_SIGN_VERIFY_SM2`: creates an asymmetric SM2 key for signature verification; `ASYMMETRIC_SIGN_VERIFY_ECC`: creates an asymmetric 2048-bit RSA key for signature verification; `ASYMMETRIC_SIGN_VERIFY_ECDSA384`: creates an asymmetric ECDSA384 key for signature verification. You can get a full list of supported key purposes and algorithms using the ListAlgorithms API.
        :type KeyUsage: str
        :param _Type: Specifies the key type. Default value: 1. Valid value: 1 - default type, indicating that the CMK is created by KMS; 2 - EXTERNAL type, indicating that you need to import key material. For more information, please see the `GetParametersForImport` and `ImportKeyMaterial` API documents.
        :type Type: int
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _HsmClusterId: ID of the HSM cluster. This field is only valid for Exclusive and Managed KMS instances.
        :type HsmClusterId: str
        """
        self._Alias = None
        self._Description = None
        self._KeyUsage = None
        self._Type = None
        self._Tags = None
        self._HsmClusterId = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Description = params.get("Description")
        self._KeyUsage = params.get("KeyUsage")
        self._Type = params.get("Type")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyResponse(AbstractModel):
    """CreateKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        :param _Alias: Alias that makes a key more recognizable and understandable
        :type Alias: str
        :param _CreateTime: Key creation time in UNIX timestamp format
        :type CreateTime: int
        :param _Description: CMK description
        :type Description: str
        :param _KeyState: CMK status
        :type KeyState: str
        :param _KeyUsage: CMK usage
        :type KeyUsage: str
        :param _TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error
        :type TagCode: int
        :param _TagMsg: Tag operation return information
        :type TagMsg: str
        :param _HsmClusterId: ID of the HSM cluster. This field is only valid for Exclusive and Managed KMS instances.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HsmClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._Alias = None
        self._CreateTime = None
        self._Description = None
        self._KeyState = None
        self._KeyUsage = None
        self._TagCode = None
        self._TagMsg = None
        self._HsmClusterId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def TagCode(self):
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._KeyState = params.get("KeyState")
        self._KeyUsage = params.get("KeyUsage")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._HsmClusterId = params.get("HsmClusterId")
        self._RequestId = params.get("RequestId")


class CreateWhiteBoxKeyRequest(AbstractModel):
    """CreateWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param _Alias: Unique alias that makes a key more recognizable and understandable. This parameter should be 1 to 60 letters, digits, `-`, and `_`; it must begin with a letter or digit and cannot be left empty.
        :type Alias: str
        :param _Algorithm: All algorithm types for creating keys. Valid values: AES_256, SM4
        :type Algorithm: str
        :param _Description: Key description of up to 1024 bytes
        :type Description: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        """
        self._Alias = None
        self._Algorithm = None
        self._Description = None
        self._Tags = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Algorithm = params.get("Algorithm")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhiteBoxKeyResponse(AbstractModel):
    """CreateWhiteBoxKey response structure.

    """

    def __init__(self):
        r"""
        :param _EncryptKey: Base64-encoded encryption key
        :type EncryptKey: str
        :param _DecryptKey: Base64-encoded decryption key
        :type DecryptKey: str
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param _TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error
        :type TagCode: int
        :param _TagMsg: Tag operation return message
        :type TagMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EncryptKey = None
        self._DecryptKey = None
        self._KeyId = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def EncryptKey(self):
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def TagCode(self):
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptKey = params.get("EncryptKey")
        self._DecryptKey = params.get("DecryptKey")
        self._KeyId = params.get("KeyId")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt request structure.

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: The ciphertext data to be decrypted.
        :type CiphertextBlob: str
        :param _EncryptionContext: JSON string of key-value pair. If this parameter is specified for `Encrypt`, the same parameter needs to be provided when the `Decrypt` API is called. The maximum length is 1,024 bytes.
        :type EncryptionContext: str
        :param _EncryptionPublicKey: PEM-encoded public key (2048-bit RSA/SM2 key), which can be used to encrypt the `Plaintext` returned. If this field is left empty, the `Plaintext` will not be encrypted.
        :type EncryptionPublicKey: str
        :param _EncryptionAlgorithm: Asymmetric encryption algorithm. Valid values: `SM2` (C1C3C2 ciphertext is returned), `SM2_C1C3C2_ASN1` (C1C3C2 ASN1 ciphertext is returned), `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256`. This field is used in combination with `EncryptionPublicKey` for encryption. If it is left empty, an SM2 public key will be used by default.
        :type EncryptionAlgorithm: str
        """
        self._CiphertextBlob = None
        self._EncryptionContext = None
        self._EncryptionPublicKey = None
        self._EncryptionAlgorithm = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext

    @property
    def EncryptionPublicKey(self):
        return self._EncryptionPublicKey

    @EncryptionPublicKey.setter
    def EncryptionPublicKey(self, EncryptionPublicKey):
        self._EncryptionPublicKey = EncryptionPublicKey

    @property
    def EncryptionAlgorithm(self):
        return self._EncryptionAlgorithm

    @EncryptionAlgorithm.setter
    def EncryptionAlgorithm(self, EncryptionAlgorithm):
        self._EncryptionAlgorithm = EncryptionAlgorithm


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._EncryptionContext = params.get("EncryptionContext")
        self._EncryptionPublicKey = params.get("EncryptionPublicKey")
        self._EncryptionAlgorithm = params.get("EncryptionAlgorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecryptResponse(AbstractModel):
    """Decrypt response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        :param _Plaintext: If `EncryptionPublicKey` is left empty, a Base64-encoded ciphertext will be returned. To get the plaintext, you need to decode the ciphertext first.
If `EncryptionPublicKey` is specified, this field will return the Base64-encoded ciphertext encrypted with the specified public key. To get the plaintext, you need to decode the ciphertext and upload the corresponding private key.
        :type Plaintext: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Specifies the EXTERNAL CMK for which to delete the key material.
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhiteBoxKeyResponse(AbstractModel):
    """DeleteWhiteBoxKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyResponse(AbstractModel):
    """DescribeKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyMetadata: Key attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyMetadata = None
        self._RequestId = None

    @property
    def KeyMetadata(self):
        return self._KeyMetadata

    @KeyMetadata.setter
    def KeyMetadata(self, KeyMetadata):
        self._KeyMetadata = KeyMetadata

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self._KeyMetadata = KeyMetadata()
            self._KeyMetadata._deserialize(params.get("KeyMetadata"))
        self._RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of IDs of the CMKs to be queried in batches. Up to 100 `KeyId` values are supported in one query.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys response structure.

    """

    def __init__(self):
        r"""
        :param _KeyMetadatas: List of returned attribute information
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyMetadatas = None
        self._RequestId = None

    @property
    def KeyMetadatas(self):
        return self._KeyMetadatas

    @KeyMetadatas.setter
    def KeyMetadatas(self, KeyMetadatas):
        self._KeyMetadatas = KeyMetadatas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self._KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self._KeyMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxDecryptKeyRequest(AbstractModel):
    """DescribeWhiteBoxDecryptKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDecryptKeyResponse(AbstractModel):
    """DescribeWhiteBoxDecryptKey response structure.

    """

    def __init__(self):
        r"""
        :param _DecryptKey: Base64-encoded white-box decryption key
        :type DecryptKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DecryptKey = None
        self._RequestId = None

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DecryptKey = params.get("DecryptKey")
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: White-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints response structure.

    """

    def __init__(self):
        r"""
        :param _DeviceFingerprints: Device fingerprint list
        :type DeviceFingerprints: list of DeviceFingerprint
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeviceFingerprints = None
        self._RequestId = None

    @property
    def DeviceFingerprints(self):
        return self._DeviceFingerprints

    @DeviceFingerprints.setter
    def DeviceFingerprints(self, DeviceFingerprints):
        self._DeviceFingerprints = DeviceFingerprints

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceFingerprints") is not None:
            self._DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self._DeviceFingerprints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyDetailsRequest(AbstractModel):
    """DescribeWhiteBoxKeyDetails request structure.

    """

    def __init__(self):
        r"""
        :param _KeyStatus: Filter: key status. 0: disabled, 1: enabled
        :type KeyStatus: int
        :param _Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.
        :type Offset: int
        :param _Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 0, indicating not to paginate.
        :type Limit: int
        :param _TagFilters: Tag filter condition
        :type TagFilters: list of TagFilter
        """
        self._KeyStatus = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def KeyStatus(self):
        return self._KeyStatus

    @KeyStatus.setter
    def KeyStatus(self, KeyStatus):
        self._KeyStatus = KeyStatus

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._KeyStatus = params.get("KeyStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyDetailsResponse(AbstractModel):
    """DescribeWhiteBoxKeyDetails response structure.

    """

    def __init__(self):
        r"""
        :param _KeyInfos: White-box key information list
        :type KeyInfos: list of WhiteboxKeyInfo
        :param _TotalCount: Total white-box keys.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def KeyInfos(self):
        return self._KeyInfos

    @KeyInfos.setter
    def KeyInfos(self, KeyInfos):
        self._KeyInfos = KeyInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyInfos") is not None:
            self._KeyInfos = []
            for item in params.get("KeyInfos"):
                obj = WhiteboxKeyInfo()
                obj._deserialize(item)
                self._KeyInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyRequest(AbstractModel):
    """DescribeWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyResponse(AbstractModel):
    """DescribeWhiteBoxKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyInfo: White-box key information
        :type KeyInfo: :class:`tencentcloud.kms.v20190118.models.WhiteboxKeyInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyInfo = None
        self._RequestId = None

    @property
    def KeyInfo(self):
        return self._KeyInfo

    @KeyInfo.setter
    def KeyInfo(self, KeyInfo):
        self._KeyInfo = KeyInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyInfo") is not None:
            self._KeyInfo = WhiteboxKeyInfo()
            self._KeyInfo._deserialize(params.get("KeyInfo"))
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxServiceStatusRequest(AbstractModel):
    """DescribeWhiteBoxServiceStatus request structure.

    """


class DescribeWhiteBoxServiceStatusResponse(AbstractModel):
    """DescribeWhiteBoxServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: Whether the user's white-box key service is available
        :type ServiceEnabled: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._RequestId = params.get("RequestId")


class DeviceFingerprint(AbstractModel):
    """Device fingerprint

    """

    def __init__(self):
        r"""
        :param _Identity: Fingerprint information collected by device fingerprint collector. Its format must be in the following regular expression: ^[0-9a-f]{8}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{16}$
        :type Identity: str
        :param _Description: Description, such as IP and device name. Length limit: 1,024 bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._Identity = None
        self._Description = None

    @property
    def Identity(self):
        return self._Identity

    @Identity.setter
    def Identity(self, Identity):
        self._Identity = Identity

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Identity = params.get("Identity")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRequest(AbstractModel):
    """DisableKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyResponse(AbstractModel):
    """DisableKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of IDs of the CMKs to be disabled in batches. Up to 100 CMKs are supported at a time
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeysResponse(AbstractModel):
    """DisableKeys response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeyResponse(AbstractModel):
    """DisableWhiteBoxKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeysResponse(AbstractModel):
    """DisableWhiteBoxKeys response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyResponse(AbstractModel):
    """EnableKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _RotateDays: The interval between each key rotation in days. Value range: 7 - 365 (default).
        :type RotateDays: int
        """
        self._KeyId = None
        self._RotateDays = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RotateDays(self):
        return self._RotateDays

    @RotateDays.setter
    def RotateDays(self, RotateDays):
        self._RotateDays = RotateDays


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RotateDays = params.get("RotateDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of IDs of the CMKs to be enabled in batches. Up to 100 CMKs are supported at a time
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeysResponse(AbstractModel):
    """EnableKeys response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeyResponse(AbstractModel):
    """EnableWhiteBoxKey response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys request structure.

    """

    def __init__(self):
        r"""
        :param _KeyIds: List of globally unique white-box key IDs. Note: you should make sure that all provided `KeyId` values are in valid format, unique, and actually exist. Up to 50 ones are allowed.
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeysResponse(AbstractModel):
    """EnableWhiteBoxKeys response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param _PlainText: Base64-encoded text to be encrypted. The size of the original text cannot exceed 4 KB.
        :type PlainText: str
        :param _InitializationVector: Base64-encoded initialization vector of 16 bytes, which will be used by the encryption algorithm. If this parameter is not passed in, the backend service will generate a random one. You should save this value as a parameter for decryption.
        :type InitializationVector: str
        """
        self._KeyId = None
        self._PlainText = None
        self._InitializationVector = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PlainText(self):
        return self._PlainText

    @PlainText.setter
    def PlainText(self, PlainText):
        self._PlainText = PlainText

    @property
    def InitializationVector(self):
        return self._InitializationVector

    @InitializationVector.setter
    def InitializationVector(self, InitializationVector):
        self._InitializationVector = InitializationVector


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PlainText = params.get("PlainText")
        self._InitializationVector = params.get("InitializationVector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptByWhiteBoxResponse(AbstractModel):
    """EncryptByWhiteBox response structure.

    """

    def __init__(self):
        r"""
        :param _InitializationVector: Base64-encoded initialization vector, which will be used by the encryption algorithm. If this parameter is passed in by the caller, it will be returned as-is; otherwise, the backend service will generate a random one and return it.
        :type InitializationVector: str
        :param _CipherText: Base64-encoded ciphertext after encryption
        :type CipherText: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InitializationVector = None
        self._CipherText = None
        self._RequestId = None

    @property
    def InitializationVector(self):
        return self._InitializationVector

    @InitializationVector.setter
    def InitializationVector(self, InitializationVector):
        self._InitializationVector = InitializationVector

    @property
    def CipherText(self):
        return self._CipherText

    @CipherText.setter
    def CipherText(self, CipherText):
        self._CipherText = CipherText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InitializationVector = params.get("InitializationVector")
        self._CipherText = params.get("CipherText")
        self._RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique ID of the CMK generated by calling the `CreateKey` API
        :type KeyId: str
        :param _Plaintext: Encrypted plaintext data. This field must be Base64-encoded. The maximum size of the original data is 4 KB
        :type Plaintext: str
        :param _EncryptionContext: JSON string of key-value pair. If this parameter is specified, the same parameter needs to be provided when the `Decrypt` API is called. It is up to 1,024 characters
        :type EncryptionContext: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._EncryptionContext = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptResponse(AbstractModel):
    """Encrypt response structure.

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: Base64-encoded ciphertext, which is the encrypted information of the ciphertext and key. To get the plaintext, you need to pass in this field to the Decrypt API.
        :type CiphertextBlob: str
        :param _KeyId: Globally unique ID of the CMK used for encryption
        :type KeyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CiphertextBlob = None
        self._KeyId = None
        self._RequestId = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        :param _KeySpec: Specifies the encryption algorithm and size of the `DataKey`. Valid values: AES_128, AES_256. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type KeySpec: str
        :param _NumberOfBytes: Length of the `DataKey`. If both `NumberOfBytes` and `KeySpec` are specified, `NumberOfBytes` will prevail. Minimum value: 1; maximum value: 1024. Either `KeySpec` or `NumberOfBytes` must be specified.
        :type NumberOfBytes: int
        :param _EncryptionContext: JSON string of key-value pair. If this field is used, the same string should be entered when the returned `DataKey` is decrypted.
        :type EncryptionContext: str
        :param _EncryptionPublicKey: PEM-encoded public key (2048-bit RSA/SM2 key), which can be used to encrypt the `Plaintext` returned. If this field is left empty, the `Plaintext` will not be encrypted.
        :type EncryptionPublicKey: str
        :param _EncryptionAlgorithm: Asymmetric encryption algorithm. Valid values: `SM2` (C1C3C2 ciphertext is returned)`, `SM2_C1C3C2_ASN1` (C1C3C2 ASN1 ciphertext is returned), `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256`. This field is used in combination with `EncryptionPublicKey` for encryption. If it is left empty, an SM2 public key will be used by default.
        :type EncryptionAlgorithm: str
        """
        self._KeyId = None
        self._KeySpec = None
        self._NumberOfBytes = None
        self._EncryptionContext = None
        self._EncryptionPublicKey = None
        self._EncryptionAlgorithm = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeySpec(self):
        return self._KeySpec

    @KeySpec.setter
    def KeySpec(self, KeySpec):
        self._KeySpec = KeySpec

    @property
    def NumberOfBytes(self):
        return self._NumberOfBytes

    @NumberOfBytes.setter
    def NumberOfBytes(self, NumberOfBytes):
        self._NumberOfBytes = NumberOfBytes

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext

    @property
    def EncryptionPublicKey(self):
        return self._EncryptionPublicKey

    @EncryptionPublicKey.setter
    def EncryptionPublicKey(self, EncryptionPublicKey):
        self._EncryptionPublicKey = EncryptionPublicKey

    @property
    def EncryptionAlgorithm(self):
        return self._EncryptionAlgorithm

    @EncryptionAlgorithm.setter
    def EncryptionAlgorithm(self, EncryptionAlgorithm):
        self._EncryptionAlgorithm = EncryptionAlgorithm


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeySpec = params.get("KeySpec")
        self._NumberOfBytes = params.get("NumberOfBytes")
        self._EncryptionContext = params.get("EncryptionContext")
        self._EncryptionPublicKey = params.get("EncryptionPublicKey")
        self._EncryptionAlgorithm = params.get("EncryptionAlgorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        :param _Plaintext: If `EncryptionPublicKey` is left empty, a Base64-encoded ciphertext will be returned. To get the plaintext, you need to decode the ciphertext first.
If `EncryptionPublicKey` is specified, this field will return the Base64-encoded ciphertext encrypted with the specified public key. To get the plaintext, you need to decode the ciphertext and upload the corresponding private key.
        :type Plaintext: str
        :param _CiphertextBlob: Ciphertext of the data key, which should be kept by yourself. KMS does not host user data keys. You can call the `Decrypt` API to get the plaintext of the data key from `CiphertextBlob`.
        :type CiphertextBlob: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._CiphertextBlob = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom request structure.

    """

    def __init__(self):
        r"""
        :param _NumberOfBytes: Length of the random number. Minimum value: 1. Maximum value: 1024
        :type NumberOfBytes: int
        """
        self._NumberOfBytes = None

    @property
    def NumberOfBytes(self):
        return self._NumberOfBytes

    @NumberOfBytes.setter
    def NumberOfBytes(self, NumberOfBytes):
        self._NumberOfBytes = NumberOfBytes


    def _deserialize(self, params):
        self._NumberOfBytes = params.get("NumberOfBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom response structure.

    """

    def __init__(self):
        r"""
        :param _Plaintext: Base64-encoded plaintext of the randomly generated number. You need to Base64-decode it to get the plaintext.
        :type Plaintext: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Plaintext = None
        self._RequestId = None

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus response structure.

    """

    def __init__(self):
        r"""
        :param _KeyRotationEnabled: Whether key rotation is enabled
        :type KeyRotationEnabled: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyRotationEnabled = None
        self._RequestId = None

    @property
    def KeyRotationEnabled(self):
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique ID of a CMK. The CMK for which to get the key parameters must be of the `EXTERNAL` type, i.e., Type = 2 when the CMK is created by the `CreateKey` API.
        :type KeyId: str
        :param _WrappingAlgorithm: Specifies the algorithm for key material encryption. Currently, `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1`, and `RSAES_OAEP_SHA_256` are supported.
        :type WrappingAlgorithm: str
        :param _WrappingKeySpec: Specifies the type of wrapping key. Currently, only `RSA_2048` is supported.
        :type WrappingKeySpec: str
        """
        self._KeyId = None
        self._WrappingAlgorithm = None
        self._WrappingKeySpec = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def WrappingAlgorithm(self):
        return self._WrappingAlgorithm

    @WrappingAlgorithm.setter
    def WrappingAlgorithm(self, WrappingAlgorithm):
        self._WrappingAlgorithm = WrappingAlgorithm

    @property
    def WrappingKeySpec(self):
        return self._WrappingKeySpec

    @WrappingKeySpec.setter
    def WrappingKeySpec(self, WrappingKeySpec):
        self._WrappingKeySpec = WrappingKeySpec


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._WrappingAlgorithm = params.get("WrappingAlgorithm")
        self._WrappingKeySpec = params.get("WrappingKeySpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique ID of a CMK, which is used to specify the CMK into which to import key material.
        :type KeyId: str
        :param _ImportToken: The token required for importing key material, which is used as a parameter for `ImportKeyMaterial`.
        :type ImportToken: str
        :param _PublicKey: The Base64-encoded RSA public key used to encrypt key material before importing it with `ImportKeyMaterial`.
        :type PublicKey: str
        :param _ParametersValidTo: Validity period of the token and public key. A token and public key can only be imported when they are valid. If they are expired, you will need to call the `GetParametersForImport` API again to get a new token and public key.
        :type ParametersValidTo: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._ImportToken = None
        self._PublicKey = None
        self._ParametersValidTo = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ImportToken(self):
        return self._ImportToken

    @ImportToken.setter
    def ImportToken(self, ImportToken):
        self._ImportToken = ImportToken

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def ParametersValidTo(self):
        return self._ParametersValidTo

    @ParametersValidTo.setter
    def ParametersValidTo(self, ParametersValidTo):
        self._ParametersValidTo = ParametersValidTo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ImportToken = params.get("ImportToken")
        self._PublicKey = params.get("PublicKey")
        self._ParametersValidTo = params.get("ParametersValidTo")
        self._RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID.
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey response structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID.
        :type KeyId: str
        :param _PublicKey: Base64-encoded public key content.
        :type PublicKey: str
        :param _PublicKeyPem: Public key content in PEM format.
        :type PublicKeyPem: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KeyId = None
        self._PublicKey = None
        self._PublicKeyPem = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PublicKeyPem(self):
        return self._PublicKeyPem

    @PublicKeyPem.setter
    def PublicKeyPem(self, PublicKeyPem):
        self._PublicKeyPem = PublicKeyPem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PublicKey = params.get("PublicKey")
        self._PublicKeyPem = params.get("PublicKeyPem")
        self._RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions request structure.

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Regions: The list of supported regions
Note: this field may return null, indicating that no valid values can be obtained.
        :type Regions: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: Whether the KMS service has been activated. true: activated
        :type ServiceEnabled: bool
        :param _InvalidType: Service unavailability type. 0: not purchased; 1: normal; 2: suspended due to arrears; 3: resource released
        :type InvalidType: int
        :param _UserLevel: 0: Basic Edition, 1: Ultimate Edition
        :type UserLevel: int
        :param _ProExpireTime: Expiration time of the KMS Ultimate edition. It’s represented in a Unix Epoch timestamp.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProExpireTime: int
        :param _ProRenewFlag: Whether to automatically renew Ultimate Edition. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProRenewFlag: int
        :param _ProResourceId: Unique ID of the Ultimate Edition purchase record. If the Ultimate Edition is not activated, the returned value will be null.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProResourceId: str
        :param _ExclusiveVSMEnabled: Whether to activate Managed KMS
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExclusiveVSMEnabled: bool
        :param _ExclusiveHSMEnabled: Whether to activate Exclusive KMS
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExclusiveHSMEnabled: bool
        :param _SubscriptionInfo: KMS subscription information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscriptionInfo: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._InvalidType = None
        self._UserLevel = None
        self._ProExpireTime = None
        self._ProRenewFlag = None
        self._ProResourceId = None
        self._ExclusiveVSMEnabled = None
        self._ExclusiveHSMEnabled = None
        self._SubscriptionInfo = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def InvalidType(self):
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def UserLevel(self):
        return self._UserLevel

    @UserLevel.setter
    def UserLevel(self, UserLevel):
        self._UserLevel = UserLevel

    @property
    def ProExpireTime(self):
        return self._ProExpireTime

    @ProExpireTime.setter
    def ProExpireTime(self, ProExpireTime):
        self._ProExpireTime = ProExpireTime

    @property
    def ProRenewFlag(self):
        return self._ProRenewFlag

    @ProRenewFlag.setter
    def ProRenewFlag(self, ProRenewFlag):
        self._ProRenewFlag = ProRenewFlag

    @property
    def ProResourceId(self):
        return self._ProResourceId

    @ProResourceId.setter
    def ProResourceId(self, ProResourceId):
        self._ProResourceId = ProResourceId

    @property
    def ExclusiveVSMEnabled(self):
        return self._ExclusiveVSMEnabled

    @ExclusiveVSMEnabled.setter
    def ExclusiveVSMEnabled(self, ExclusiveVSMEnabled):
        self._ExclusiveVSMEnabled = ExclusiveVSMEnabled

    @property
    def ExclusiveHSMEnabled(self):
        return self._ExclusiveHSMEnabled

    @ExclusiveHSMEnabled.setter
    def ExclusiveHSMEnabled(self, ExclusiveHSMEnabled):
        self._ExclusiveHSMEnabled = ExclusiveHSMEnabled

    @property
    def SubscriptionInfo(self):
        return self._SubscriptionInfo

    @SubscriptionInfo.setter
    def SubscriptionInfo(self, SubscriptionInfo):
        self._SubscriptionInfo = SubscriptionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._InvalidType = params.get("InvalidType")
        self._UserLevel = params.get("UserLevel")
        self._ProExpireTime = params.get("ProExpireTime")
        self._ProRenewFlag = params.get("ProRenewFlag")
        self._ProResourceId = params.get("ProResourceId")
        self._ExclusiveVSMEnabled = params.get("ExclusiveVSMEnabled")
        self._ExclusiveHSMEnabled = params.get("ExclusiveHSMEnabled")
        self._SubscriptionInfo = params.get("SubscriptionInfo")
        self._RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial request structure.

    """

    def __init__(self):
        r"""
        :param _EncryptedKeyMaterial: Base64-encoded key material that encrypted with the `PublicKey` returned by `GetParametersForImport`. For the KMS of SM-CRYPTO version, the length of the key material should be 128 bits, while for KMS of FIPS-compliant version, the length should be 256 bits.
        :type EncryptedKeyMaterial: str
        :param _ImportToken: Import token obtained by calling `GetParametersForImport`.
        :type ImportToken: str
        :param _KeyId: Specifies the CMK into which to import key material, which must be the same as the one specified by `GetParametersForImport`.
        :type KeyId: str
        :param _ValidTo: Unix timestamp of the key material's expiration time. If this value is empty or 0, the key material will never expire. To specify the expiration time, it should be later than the current time. Maximum value: 2147443200.
        :type ValidTo: int
        """
        self._EncryptedKeyMaterial = None
        self._ImportToken = None
        self._KeyId = None
        self._ValidTo = None

    @property
    def EncryptedKeyMaterial(self):
        return self._EncryptedKeyMaterial

    @EncryptedKeyMaterial.setter
    def EncryptedKeyMaterial(self, EncryptedKeyMaterial):
        self._EncryptedKeyMaterial = EncryptedKeyMaterial

    @property
    def ImportToken(self):
        return self._ImportToken

    @ImportToken.setter
    def ImportToken(self, ImportToken):
        self._ImportToken = ImportToken

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo


    def _deserialize(self, params):
        self._EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self._ImportToken = params.get("ImportToken")
        self._KeyId = params.get("KeyId")
        self._ValidTo = params.get("ValidTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Key(AbstractModel):
    """Returned CMK list information

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID.
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyMetadata(AbstractModel):
    """CMK attribute information

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        :param _Alias: Alias that makes a key more recognizable and understandable
        :type Alias: str
        :param _CreateTime: Key creation time
        :type CreateTime: int
        :param _Description: CMK description
        :type Description: str
        :param _KeyState: CMK status. Valid values: Enabled, Disabled, PendingDelete, PendingImport, Archived.
        :type KeyState: str
        :param _KeyUsage: CMK purpose. Valid values: `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, and `ASYMMETRIC_SIGN_VERIFY_ECC`.
        :type KeyUsage: str
        :param _Type: CMK type. 2: FIPS-compliant; 4: SM-CRYPTO
        :type Type: int
        :param _CreatorUin: Creator
        :type CreatorUin: int
        :param _KeyRotationEnabled: Whether key rotation is enabled
        :type KeyRotationEnabled: bool
        :param _Owner: CMK creator. The value of this parameter is `user` if the CMK is created by the user, or the corresponding service name if it is created automatically by an authorized Tencent Cloud service.
        :type Owner: str
        :param _NextRotateTime: Time of next rotation if key rotation is enabled
        :type NextRotateTime: int
        :param _DeletionDate: Scheduled deletion time
        :type DeletionDate: int
        :param _Origin: CMK key material type. TENCENT_KMS: created by KMS; EXTERNAL: imported by user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: str
        :param _ValidTo: It's valid when `Origin` is `EXTERNAL`, indicating the expiration date of key material. 0 means valid forever.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValidTo: int
        :param _ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`.
        :type ResourceId: str
        :param _HsmClusterId: ID of the HSM cluster. This field is only valid for Exclusive and Managed KMS instances.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HsmClusterId: str
        """
        self._KeyId = None
        self._Alias = None
        self._CreateTime = None
        self._Description = None
        self._KeyState = None
        self._KeyUsage = None
        self._Type = None
        self._CreatorUin = None
        self._KeyRotationEnabled = None
        self._Owner = None
        self._NextRotateTime = None
        self._DeletionDate = None
        self._Origin = None
        self._ValidTo = None
        self._ResourceId = None
        self._HsmClusterId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def KeyRotationEnabled(self):
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def NextRotateTime(self):
        return self._NextRotateTime

    @NextRotateTime.setter
    def NextRotateTime(self, NextRotateTime):
        self._NextRotateTime = NextRotateTime

    @property
    def DeletionDate(self):
        return self._DeletionDate

    @DeletionDate.setter
    def DeletionDate(self, DeletionDate):
        self._DeletionDate = DeletionDate

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._KeyState = params.get("KeyState")
        self._KeyUsage = params.get("KeyUsage")
        self._Type = params.get("Type")
        self._CreatorUin = params.get("CreatorUin")
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._Owner = params.get("Owner")
        self._NextRotateTime = params.get("NextRotateTime")
        self._DeletionDate = params.get("DeletionDate")
        self._Origin = params.get("Origin")
        self._ValidTo = params.get("ValidTo")
        self._ResourceId = params.get("ResourceId")
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _SymmetricAlgorithms: Symmetric encryption algorithms supported in this region
        :type SymmetricAlgorithms: list of AlgorithmInfo
        :param _AsymmetricAlgorithms: Asymmetric encryption algorithms supported in this region
        :type AsymmetricAlgorithms: list of AlgorithmInfo
        :param _AsymmetricSignVerifyAlgorithms: Asymmetric signature verification algorithms supported in the current region
        :type AsymmetricSignVerifyAlgorithms: list of AlgorithmInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SymmetricAlgorithms = None
        self._AsymmetricAlgorithms = None
        self._AsymmetricSignVerifyAlgorithms = None
        self._RequestId = None

    @property
    def SymmetricAlgorithms(self):
        return self._SymmetricAlgorithms

    @SymmetricAlgorithms.setter
    def SymmetricAlgorithms(self, SymmetricAlgorithms):
        self._SymmetricAlgorithms = SymmetricAlgorithms

    @property
    def AsymmetricAlgorithms(self):
        return self._AsymmetricAlgorithms

    @AsymmetricAlgorithms.setter
    def AsymmetricAlgorithms(self, AsymmetricAlgorithms):
        self._AsymmetricAlgorithms = AsymmetricAlgorithms

    @property
    def AsymmetricSignVerifyAlgorithms(self):
        return self._AsymmetricSignVerifyAlgorithms

    @AsymmetricSignVerifyAlgorithms.setter
    def AsymmetricSignVerifyAlgorithms(self, AsymmetricSignVerifyAlgorithms):
        self._AsymmetricSignVerifyAlgorithms = AsymmetricSignVerifyAlgorithms

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self._SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self._AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._AsymmetricAlgorithms.append(obj)
        if params.get("AsymmetricSignVerifyAlgorithms") is not None:
            self._AsymmetricSignVerifyAlgorithms = []
            for item in params.get("AsymmetricSignVerifyAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._AsymmetricSignVerifyAlgorithms.append(obj)
        self._RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0.
        :type Offset: int
        :param _Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200.
        :type Limit: int
        :param _Role: Filters by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service.
        :type Role: int
        :param _OrderType: Sorts by CMK creation time. 0: descending; 1: ascending
        :type OrderType: int
        :param _KeyState: Filters by CMK status. 0: all CMKs; 1: CMKs in `Enabled` status only; 2: CMKs in `Disabled` status only; 3: CMKs in `PendingDelete` status only (i.e., keys with schedule deletion enabled); 4: CMKs in `PendingImport` status only; 5: CMKs in `Archived` status only.
        :type KeyState: int
        :param _SearchKeyAlias: Performs a fuzzy query by `KeyId` or `Alias`
        :type SearchKeyAlias: str
        :param _Origin: Filters by CMK type. "TENCENT_KMS" indicates to filter CMKs whose key materials are created by KMS; "EXTERNAL" indicates to filter CMKs of `EXTERNAL` type whose key materials are imported by users; "ALL" or empty indicates to filter CMKs of both types. This value is case-sensitive.
        :type Origin: str
        :param _KeyUsage: Filters by the `KeyUsage` field value. Valid values: `ALL` (all CMKs), `ENCRYPT_DECRYPT` (used when this field is left empty), `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`, `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, and `ASYMMETRIC_SIGN_VERIFY_ECC`.
        :type KeyUsage: str
        :param _TagFilters: Tag filter condition
        :type TagFilters: list of TagFilter
        :param _HsmClusterId: ID of the HSM cluster. This field is only valid for Exclusive and Managed KMS instances.
        :type HsmClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._Role = None
        self._OrderType = None
        self._KeyState = None
        self._SearchKeyAlias = None
        self._Origin = None
        self._KeyUsage = None
        self._TagFilters = None
        self._HsmClusterId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def SearchKeyAlias(self):
        return self._SearchKeyAlias

    @SearchKeyAlias.setter
    def SearchKeyAlias(self, SearchKeyAlias):
        self._SearchKeyAlias = SearchKeyAlias

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Role = params.get("Role")
        self._OrderType = params.get("OrderType")
        self._KeyState = params.get("KeyState")
        self._SearchKeyAlias = params.get("SearchKeyAlias")
        self._Origin = params.get("Origin")
        self._KeyUsage = params.get("KeyUsage")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of CMKs
        :type TotalCount: int
        :param _KeyMetadatas: List of returned attribute information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyMetadatas: list of KeyMetadata
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyMetadatas = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyMetadatas(self):
        return self._KeyMetadatas

    @KeyMetadatas.setter
    def KeyMetadatas(self, KeyMetadatas):
        self._KeyMetadatas = KeyMetadatas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self._KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self._KeyMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: This parameter has the same meaning of the `Offset` in an SQL query, indicating that this acquisition starts from the "No. Offset value" element of the array arranged in a certain order. The default value is 0
        :type Offset: int
        :param _Limit: This parameter has the same meaning of the `Limit` in an SQL query, indicating that up to `Limit` value elements can be obtained in this request. The default value is 10 and the maximum value is 200
        :type Limit: int
        :param _Role: Filter by creator role. 0 (default value): the CMK is created by the user; 1: the CMK is created automatically by an authorized Tencent Cloud service
        :type Role: int
        :param _HsmClusterId: ID of the HSM cluster. This field is only valid for Exclusive and Managed KMS instances.
        :type HsmClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._Role = None
        self._HsmClusterId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Role = params.get("Role")
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeysResponse(AbstractModel):
    """ListKeys response structure.

    """

    def __init__(self):
        r"""
        :param _Keys: CMK list array
        :type Keys: list of Key
        :param _TotalCount: Total number of CMKs
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Keys = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class OverwriteWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: White-box key ID
        :type KeyId: str
        :param _DeviceFingerprints: Device fingerprint list. If the list is empty, it means to delete all fingerprint information corresponding to the key. There can be up to 200 entries in the list.
        :type DeviceFingerprints: list of DeviceFingerprint
        """
        self._KeyId = None
        self._DeviceFingerprints = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def DeviceFingerprints(self):
        return self._DeviceFingerprints

    @DeviceFingerprints.setter
    def DeviceFingerprints(self, DeviceFingerprints):
        self._DeviceFingerprints = DeviceFingerprints


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        if params.get("DeviceFingerprints") is not None:
            self._DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self._DeviceFingerprints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverwriteWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt request structure.

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: Ciphertext to be re-encrypted
        :type CiphertextBlob: str
        :param _DestinationKeyId: CMK used for re-encryption. If this parameter is empty, the ciphertext will be re-encrypted by using the original CMK (as long as the key is not rotated, the ciphertext will not be refreshed)
        :type DestinationKeyId: str
        :param _SourceEncryptionContext: JSON string of the key-value pair used during ciphertext encryption by `CiphertextBlob`. If not used during encryption, this parameter will be empty
        :type SourceEncryptionContext: str
        :param _DestinationEncryptionContext: JSON string of the key-value pair used during re-encryption. If this field is used, the same string should be entered when the returned new ciphertext is decrypted
        :type DestinationEncryptionContext: str
        """
        self._CiphertextBlob = None
        self._DestinationKeyId = None
        self._SourceEncryptionContext = None
        self._DestinationEncryptionContext = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def DestinationKeyId(self):
        return self._DestinationKeyId

    @DestinationKeyId.setter
    def DestinationKeyId(self, DestinationKeyId):
        self._DestinationKeyId = DestinationKeyId

    @property
    def SourceEncryptionContext(self):
        return self._SourceEncryptionContext

    @SourceEncryptionContext.setter
    def SourceEncryptionContext(self, SourceEncryptionContext):
        self._SourceEncryptionContext = SourceEncryptionContext

    @property
    def DestinationEncryptionContext(self):
        return self._DestinationEncryptionContext

    @DestinationEncryptionContext.setter
    def DestinationEncryptionContext(self, DestinationEncryptionContext):
        self._DestinationEncryptionContext = DestinationEncryptionContext


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._DestinationKeyId = params.get("DestinationKeyId")
        self._SourceEncryptionContext = params.get("SourceEncryptionContext")
        self._DestinationEncryptionContext = params.get("DestinationEncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReEncryptResponse(AbstractModel):
    """ReEncrypt response structure.

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: Re-encrypted ciphertext
        :type CiphertextBlob: str
        :param _KeyId: CMK used for re-encryption
        :type KeyId: str
        :param _SourceKeyId: CMK used by ciphertext before re-encryption
        :type SourceKeyId: str
        :param _ReEncrypted: `true` indicates that the ciphertext has been re-encrypted. When re-encryption is initiated by using the same CMK, as long as the CMK is not rotated, no actual re-encryption will be performed, and the original ciphertext will be returned
        :type ReEncrypted: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CiphertextBlob = None
        self._KeyId = None
        self._SourceKeyId = None
        self._ReEncrypted = None
        self._RequestId = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def SourceKeyId(self):
        return self._SourceKeyId

    @SourceKeyId.setter
    def SourceKeyId(self, SourceKeyId):
        self._SourceKeyId = SourceKeyId

    @property
    def ReEncrypted(self):
        return self._ReEncrypted

    @ReEncrypted.setter
    def ReEncrypted(self, ReEncrypted):
        self._ReEncrypted = ReEncrypted

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._KeyId = params.get("KeyId")
        self._SourceKeyId = params.get("SourceKeyId")
        self._ReEncrypted = params.get("ReEncrypted")
        self._RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique CMK ID
        :type KeyId: str
        :param _PendingWindowInDays: Schedule deletion time range. Value range: [7,30]
        :type PendingWindowInDays: int
        """
        self._KeyId = None
        self._PendingWindowInDays = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PendingWindowInDays(self):
        return self._PendingWindowInDays

    @PendingWindowInDays.setter
    def PendingWindowInDays(self, PendingWindowInDays):
        self._PendingWindowInDays = PendingWindowInDays


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PendingWindowInDays = params.get("PendingWindowInDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion response structure.

    """

    def __init__(self):
        r"""
        :param _DeletionDate: Schedule deletion execution time
        :type DeletionDate: int
        :param _KeyId: Unique ID of the CMK scheduled for deletion
        :type KeyId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeletionDate = None
        self._KeyId = None
        self._RequestId = None

    @property
    def DeletionDate(self):
        return self._DeletionDate

    @DeletionDate.setter
    def DeletionDate(self, DeletionDate):
        self._DeletionDate = DeletionDate

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeletionDate = params.get("DeletionDate")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class SignByAsymmetricKeyRequest(AbstractModel):
    """SignByAsymmetricKey request structure.

    """

    def __init__(self):
        r"""
        :param _Algorithm: Signature algorithm. The valid values include `SM2DSA`, `ECC_P256_R1`, `RSA_PSS_SHA_256`, and `RSA_PKCS1_SHA_256`, etc. You can get a full list of supported algorithms using the ListAlgorithms API.
        :type Algorithm: str
        :param _Message: Full message or message abstract. Before Base64 encoding, an original message can contain up to 4,096 bytes while a message abstract must be 32 bytes.
        :type Message: str
        :param _KeyId: Unique ID of a key
        :type KeyId: str
        :param _MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.
        :type MessageType: str
        """
        self._Algorithm = None
        self._Message = None
        self._KeyId = None
        self._MessageType = None

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType


    def _deserialize(self, params):
        self._Algorithm = params.get("Algorithm")
        self._Message = params.get("Message")
        self._KeyId = params.get("KeyId")
        self._MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignByAsymmetricKeyResponse(AbstractModel):
    """SignByAsymmetricKey response structure.

    """

    def __init__(self):
        r"""
        :param _Signature: Base64-encoded signature
        :type Signature: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Signature = None
        self._RequestId = None

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag key and tag value

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filter

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceRequest(AbstractModel):
    """UnbindCloudResource request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK ID
        :type KeyId: str
        :param _ProductId: Unique ID of a Tencent Cloud service
        :type ProductId: str
        :param _ResourceId: Resource/instance ID, which is stored as a string and defined by the caller based on the Tencent Cloud service’s features.
        :type ResourceId: str
        """
        self._KeyId = None
        self._ProductId = None
        self._ResourceId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ProductId = params.get("ProductId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceResponse(AbstractModel):
    """UnbindCloudResource response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        r"""
        :param _Alias: New alias containing 1-60 characters or digits
        :type Alias: str
        :param _KeyId: Globally unique CMK ID
        :type KeyId: str
        """
        self._Alias = None
        self._KeyId = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription request structure.

    """

    def __init__(self):
        r"""
        :param _Description: New description of up to 1,024 bytes in length
        :type Description: str
        :param _KeyId: ID of the CMK for which to modify the description
        :type KeyId: str
        """
        self._Description = None
        self._KeyId = None

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VerifyByAsymmetricKeyRequest(AbstractModel):
    """VerifyByAsymmetricKey request structure.

    """

    def __init__(self):
        r"""
        :param _KeyId: Unique ID of a key
        :type KeyId: str
        :param _SignatureValue: Signature value, which is generated by calling the KMS signature API.
        :type SignatureValue: str
        :param _Message: Full message or message abstract. Before Base64 encoding, an original message can contain up to 4,096 bytes while a message abstract must be 32 bytes.
        :type Message: str
        :param _Algorithm: Signature algorithm. The valid values include `SM2DSA`, `ECC_P256_R1`, `RSA_PSS_SHA_256`, and `RSA_PKCS1_SHA_256`, etc. You can get a full list of supported algorithms using the ListAlgorithms API.
        :type Algorithm: str
        :param _MessageType: Message type. Valid values: `RAW` (indicating an original message; used by default if the parameter is not passed in) and `DIGEST`.
        :type MessageType: str
        """
        self._KeyId = None
        self._SignatureValue = None
        self._Message = None
        self._Algorithm = None
        self._MessageType = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def SignatureValue(self):
        return self._SignatureValue

    @SignatureValue.setter
    def SignatureValue(self, SignatureValue):
        self._SignatureValue = SignatureValue

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._SignatureValue = params.get("SignatureValue")
        self._Message = params.get("Message")
        self._Algorithm = params.get("Algorithm")
        self._MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyByAsymmetricKeyResponse(AbstractModel):
    """VerifyByAsymmetricKey response structure.

    """

    def __init__(self):
        r"""
        :param _SignatureValid: Whether the signature is valid. `true`: the signature is valid; `false`: the signature is invalid.
        :type SignatureValid: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SignatureValid = None
        self._RequestId = None

    @property
    def SignatureValid(self):
        return self._SignatureValid

    @SignatureValid.setter
    def SignatureValid(self, SignatureValid):
        self._SignatureValid = SignatureValid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignatureValid = params.get("SignatureValid")
        self._RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """White-box key information

    """

    def __init__(self):
        r"""
        :param _KeyId: Globally unique white-box key ID
        :type KeyId: str
        :param _Alias: Unique alias that makes a key more recognizable and understandable. This parameter cannot be empty, can contain 1 to 60 letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type Alias: str
        :param _CreatorUin: Creator
        :type CreatorUin: int
        :param _Description: Key description information
        :type Description: str
        :param _CreateTime: Key creation time in Unix timestamp
        :type CreateTime: int
        :param _Status: White-box key status. Valid values: Enabled, Disabled
        :type Status: str
        :param _OwnerUin: Creator
        :type OwnerUin: int
        :param _Algorithm: Key algorithm type
        :type Algorithm: str
        :param _EncryptKey: Base64-encoded white-box encryption key
        :type EncryptKey: str
        :param _DecryptKey: Base64-encoded white-box decryption key
        :type DecryptKey: str
        :param _ResourceId: Resource ID in the format of `creatorUin/$creatorUin/$keyId`
        :type ResourceId: str
        :param _DeviceFingerprintBind: Whether there is a device fingerprint bound to the current key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeviceFingerprintBind: bool
        """
        self._KeyId = None
        self._Alias = None
        self._CreatorUin = None
        self._Description = None
        self._CreateTime = None
        self._Status = None
        self._OwnerUin = None
        self._Algorithm = None
        self._EncryptKey = None
        self._DecryptKey = None
        self._ResourceId = None
        self._DeviceFingerprintBind = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def EncryptKey(self):
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DeviceFingerprintBind(self):
        return self._DeviceFingerprintBind

    @DeviceFingerprintBind.setter
    def DeviceFingerprintBind(self, DeviceFingerprintBind):
        self._DeviceFingerprintBind = DeviceFingerprintBind


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreatorUin = params.get("CreatorUin")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._Algorithm = params.get("Algorithm")
        self._EncryptKey = params.get("EncryptKey")
        self._DecryptKey = params.get("DecryptKey")
        self._ResourceId = params.get("ResourceId")
        self._DeviceFingerprintBind = params.get("DeviceFingerprintBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        