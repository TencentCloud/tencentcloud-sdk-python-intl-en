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


class CreateProductSecretRequest(AbstractModel):
    """CreateProductSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Credential name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens, and underscores and must begin with a letter or digit.
        :type SecretName: str
        :param _UserNamePrefix: Prefix of the user account name, which is specified by you and can contain up to 8 characters.
Supported character sets include:
Digits: [0, 9].
Lowercase letters: [a, z].
Uppercase letters: [A, Z].
Special symbols: underscore.
The prefix must begin with a letter.
        :type UserNamePrefix: str
        :param _ProductName: Name of the Tencent Cloud service bound to the credential, such as `Mysql`. The `DescribeSupportedProducts` API can be used to get the names of the supported Tencent Cloud services.
        :type ProductName: str
        :param _InstanceID: Tencent Cloud service instance ID.
        :type InstanceID: str
        :param _Domains: Domain name of the account in the form of IP. You can enter `%`.
        :type Domains: list of str
        :param _PrivilegesList: List of permissions that need to be granted when the credential is bound to a Tencent Cloud service.
        :type PrivilegesList: list of ProductPrivilegeUnit
        :param _Description: Description, which is used to describe the purpose in detail and can contain up to 2,048 bytes.
        :type Description: str
        :param _KmsKeyId: Specifies the KMS CMK that encrypts the credential.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :type KmsKeyId: str
        :param _Tags: List of tags.
        :type Tags: list of Tag
        :param _RotationBeginTime: User-Defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `True`, this parameter is required.
        :type RotationBeginTime: str
        :param _EnableRotation: Specifies whether to enable rotation
True - enable
False - do not enable
If this parameter is not specified, `False` will be used by default.
        :type EnableRotation: bool
        :param _RotationFrequency: Rotation frequency in days. Default value: 1 day.
        :type RotationFrequency: int
        """
        self._SecretName = None
        self._UserNamePrefix = None
        self._ProductName = None
        self._InstanceID = None
        self._Domains = None
        self._PrivilegesList = None
        self._Description = None
        self._KmsKeyId = None
        self._Tags = None
        self._RotationBeginTime = None
        self._EnableRotation = None
        self._RotationFrequency = None

    @property
    def SecretName(self):
        """Credential name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens, and underscores and must begin with a letter or digit.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def UserNamePrefix(self):
        """Prefix of the user account name, which is specified by you and can contain up to 8 characters.
Supported character sets include:
Digits: [0, 9].
Lowercase letters: [a, z].
Uppercase letters: [A, Z].
Special symbols: underscore.
The prefix must begin with a letter.
        :rtype: str
        """
        return self._UserNamePrefix

    @UserNamePrefix.setter
    def UserNamePrefix(self, UserNamePrefix):
        self._UserNamePrefix = UserNamePrefix

    @property
    def ProductName(self):
        """Name of the Tencent Cloud service bound to the credential, such as `Mysql`. The `DescribeSupportedProducts` API can be used to get the names of the supported Tencent Cloud services.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def InstanceID(self):
        """Tencent Cloud service instance ID.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Domains(self):
        """Domain name of the account in the form of IP. You can enter `%`.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def PrivilegesList(self):
        """List of permissions that need to be granted when the credential is bound to a Tencent Cloud service.
        :rtype: list of ProductPrivilegeUnit
        """
        return self._PrivilegesList

    @PrivilegesList.setter
    def PrivilegesList(self, PrivilegesList):
        self._PrivilegesList = PrivilegesList

    @property
    def Description(self):
        """Description, which is used to describe the purpose in detail and can contain up to 2,048 bytes.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """Specifies the KMS CMK that encrypts the credential.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def Tags(self):
        """List of tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RotationBeginTime(self):
        """User-Defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `True`, this parameter is required.
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime

    @property
    def EnableRotation(self):
        """Specifies whether to enable rotation
True - enable
False - do not enable
If this parameter is not specified, `False` will be used by default.
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def RotationFrequency(self):
        """Rotation frequency in days. Default value: 1 day.
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._UserNamePrefix = params.get("UserNamePrefix")
        self._ProductName = params.get("ProductName")
        self._InstanceID = params.get("InstanceID")
        self._Domains = params.get("Domains")
        if params.get("PrivilegesList") is not None:
            self._PrivilegesList = []
            for item in params.get("PrivilegesList"):
                obj = ProductPrivilegeUnit()
                obj._deserialize(item)
                self._PrivilegesList.append(obj)
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RotationBeginTime = params.get("RotationBeginTime")
        self._EnableRotation = params.get("EnableRotation")
        self._RotationFrequency = params.get("RotationFrequency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductSecretResponse(AbstractModel):
    """CreateProductSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the created credential.
        :type SecretName: str
        :param _TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagCode: int
        :param _TagMsg: Tag operation return message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagMsg: str
        :param _FlowID: ID of the created Tencent Cloud service credential async task.
        :type FlowID: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._TagCode = None
        self._TagMsg = None
        self._FlowID = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the created credential.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def TagCode(self):
        """Tag operation return code. 0: success; 1: internal error; 2: business processing error.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """Tag operation return message.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def FlowID(self):
        """ID of the created Tencent Cloud service credential async task.
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._FlowID = params.get("FlowID")
        self._RequestId = params.get("RequestId")


class CreateSSHKeyPairSecretRequest(AbstractModel):
    """CreateSSHKeyPairSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Secret name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens and underscores and must begin with a letter or digit.
        :type SecretName: str
        :param _ProjectId: ID of the project to which the created SSH key belongs.
        :type ProjectId: int
        :param _Description: Description, such as what it is used for. It contains up to 2,048 bytes.
        :type Description: str
        :param _KmsKeyId: Specifies a KMS CMK to encrypt the secret.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :type KmsKeyId: str
        :param _Tags: List of tags.
        :type Tags: list of Tag
        :param _SSHKeyName: Name of the SSH key pair, which only contains digits, letters and underscores and must start with a digit or letter. The maximum length is 25 characters.
        :type SSHKeyName: str
        """
        self._SecretName = None
        self._ProjectId = None
        self._Description = None
        self._KmsKeyId = None
        self._Tags = None
        self._SSHKeyName = None

    @property
    def SecretName(self):
        """Secret name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens and underscores and must begin with a letter or digit.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def ProjectId(self):
        """ID of the project to which the created SSH key belongs.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """Description, such as what it is used for. It contains up to 2,048 bytes.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """Specifies a KMS CMK to encrypt the secret.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def Tags(self):
        """List of tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SSHKeyName(self):
        """Name of the SSH key pair, which only contains digits, letters and underscores and must start with a digit or letter. The maximum length is 25 characters.
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SSHKeyName = params.get("SSHKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSHKeyPairSecretResponse(AbstractModel):
    """CreateSSHKeyPairSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the created secret.
        :type SecretName: str
        :param _SSHKeyID: ID of the created SSH key.
        :type SSHKeyID: str
        :param _SSHKeyName: Name of the created SSH key.
        :type SSHKeyName: str
        :param _TagCode: Tag return code. `0`: success; `1`: internal error; `2`: business processing error.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagCode: int
        :param _TagMsg: Tag return message.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._SSHKeyID = None
        self._SSHKeyName = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the created secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SSHKeyID(self):
        """ID of the created SSH key.
        :rtype: str
        """
        return self._SSHKeyID

    @SSHKeyID.setter
    def SSHKeyID(self, SSHKeyID):
        self._SSHKeyID = SSHKeyID

    @property
    def SSHKeyName(self):
        """Name of the created SSH key.
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName

    @property
    def TagCode(self):
        """Tag return code. `0`: success; `1`: internal error; `2`: business processing error.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """Tag return message.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._SSHKeyID = params.get("SSHKeyID")
        self._SSHKeyName = params.get("SSHKeyName")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class CreateSecretRequest(AbstractModel):
    """CreateSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Secret name, which must be unique in the same region. It can contain 128 bytes ([a-z], [A-Z], [0-9], [-_]). It must begin with a letter or digit. Note that it cannot be modified once created. 
        :type SecretName: str
        :param _VersionId: Secret version. It can contain up to 64 bytes ([a-z], [A-Z], [0-9], [-_.]). It must begin with a letter or digit. `SecretName` and `VersionId` are used to query the Secret information. If it is left empty, the initial Secret version number is used by default.
        :type VersionId: str
        :param _Description: Description information, such as the detailed use cases. It can be up to 2048 bytes.
        :type Description: str
        :param _KmsKeyId: KMS CMK used for Secret encryption. If this parameter is left empty, SecretsManager will create a CMK by default. You can also specify a KMS CMK that is created in the same region.
        :type KmsKeyId: str
        :param _SecretType: Secret type. It defaults to `custom`.
        :type SecretType: int
        :param _SecretBinary: Base64-encoded plaintext of a binary Secret. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :type SecretBinary: str
        :param _SecretString: Plaintext of a Secret, in text format. Base64 encoding is not required. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :type SecretString: str
        :param _AdditionalConfig: Additional configuration of the Secret in JSON format
        :type AdditionalConfig: str
        :param _Tags: List of tags.
        :type Tags: list of Tag
        """
        self._SecretName = None
        self._VersionId = None
        self._Description = None
        self._KmsKeyId = None
        self._SecretType = None
        self._SecretBinary = None
        self._SecretString = None
        self._AdditionalConfig = None
        self._Tags = None

    @property
    def SecretName(self):
        """Secret name, which must be unique in the same region. It can contain 128 bytes ([a-z], [A-Z], [0-9], [-_]). It must begin with a letter or digit. Note that it cannot be modified once created. 
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """Secret version. It can contain up to 64 bytes ([a-z], [A-Z], [0-9], [-_.]). It must begin with a letter or digit. `SecretName` and `VersionId` are used to query the Secret information. If it is left empty, the initial Secret version number is used by default.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Description(self):
        """Description information, such as the detailed use cases. It can be up to 2048 bytes.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """KMS CMK used for Secret encryption. If this parameter is left empty, SecretsManager will create a CMK by default. You can also specify a KMS CMK that is created in the same region.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def SecretType(self):
        """Secret type. It defaults to `custom`.
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def SecretBinary(self):
        """Base64-encoded plaintext of a binary Secret. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """Plaintext of a Secret, in text format. Base64 encoding is not required. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString

    @property
    def AdditionalConfig(self):
        """Additional configuration of the Secret in JSON format
        :rtype: str
        """
        return self._AdditionalConfig

    @AdditionalConfig.setter
    def AdditionalConfig(self, AdditionalConfig):
        self._AdditionalConfig = AdditionalConfig

    @property
    def Tags(self):
        """List of tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._SecretType = params.get("SecretType")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        self._AdditionalConfig = params.get("AdditionalConfig")
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
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the new Secret.
        :type SecretName: str
        :param _VersionId: ID of the new Secret version.
        :type VersionId: str
        :param _TagCode: Return code of tag operation. `0`: success; `1`: internal error; `2`: business processing error
Note: This field may return `null`, indicating that no valid value was found.
        :type TagCode: int
        :param _TagMsg: Return message of tag operation.
Note: This field may return `null`, indicating that no valid value was found.
        :type TagMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the new Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """ID of the new Secret version.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def TagCode(self):
        """Return code of tag operation. `0`: success; `1`: internal error; `2`: business processing error
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """Return message of tag operation.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret to be deleted.
        :type SecretName: str
        :param _RecoveryWindowInDays: Scheduled deletion time (in days), indicating the number of retention days for the secret. Value range: 0-30. If it is `0`, the secret is deleted immediately.
For an SSH key secret, this field can only be `0`.
        :type RecoveryWindowInDays: int
        :param _CleanSSHKey: Specifies whether to delete the SSH key from both the secret and the SSH key list in the CVM console. This field is only valid for SSH key secrets. Valid values:
`True`: deletes SSH key from both the secret and SSH key list in the CVM console. Note that the deletion will fail if the SSH key is already bound to a CVM instance.
`False`: only deletes the SSH key information in the secret.
        :type CleanSSHKey: bool
        """
        self._SecretName = None
        self._RecoveryWindowInDays = None
        self._CleanSSHKey = None

    @property
    def SecretName(self):
        """Name of the Secret to be deleted.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RecoveryWindowInDays(self):
        """Scheduled deletion time (in days), indicating the number of retention days for the secret. Value range: 0-30. If it is `0`, the secret is deleted immediately.
For an SSH key secret, this field can only be `0`.
        :rtype: int
        """
        return self._RecoveryWindowInDays

    @RecoveryWindowInDays.setter
    def RecoveryWindowInDays(self, RecoveryWindowInDays):
        self._RecoveryWindowInDays = RecoveryWindowInDays

    @property
    def CleanSSHKey(self):
        """Specifies whether to delete the SSH key from both the secret and the SSH key list in the CVM console. This field is only valid for SSH key secrets. Valid values:
`True`: deletes SSH key from both the secret and SSH key list in the CVM console. Note that the deletion will fail if the SSH key is already bound to a CVM instance.
`False`: only deletes the SSH key information in the secret.
        :rtype: bool
        """
        return self._CleanSSHKey

    @CleanSSHKey.setter
    def CleanSSHKey(self, CleanSSHKey):
        self._CleanSSHKey = CleanSSHKey


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RecoveryWindowInDays = params.get("RecoveryWindowInDays")
        self._CleanSSHKey = params.get("CleanSSHKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of deleted Secret.
        :type SecretName: str
        :param _DeleteTime: Secret deletion time, formatted as a Unix timestamp.
        :type DeleteTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._DeleteTime = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of deleted Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def DeleteTime(self):
        """Secret deletion time, formatted as a Unix timestamp.
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._DeleteTime = params.get("DeleteTime")
        self._RequestId = params.get("RequestId")


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _VersionId: ID of the Secret version to be deleted.
        :type VersionId: str
        """
        self._SecretName = None
        self._VersionId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """ID of the Secret version to be deleted.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _VersionId: Version ID of the Secret.
        :type VersionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """Version ID of the Secret.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowID: Async task ID.
        :type FlowID: int
        """
        self._FlowID = None

    @property
    def FlowID(self):
        """Async task ID.
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID


    def _deserialize(self, params):
        self._FlowID = params.get("FlowID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 0: processing, 1: processing succeeded, 2: processing failed
        :type TaskStatus: int
        :param _Description: Task description.
        :type Description: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskStatus = None
        self._Description = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        """0: processing, 1: processing succeeded, 2: processing failed
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Description(self):
        """Task description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskStatus = params.get("TaskStatus")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeRotationDetailRequest(AbstractModel):
    """DescribeRotationDetail request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Specifies the name of the credential for which to get the credential rotation details.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Specifies the name of the credential for which to get the credential rotation details.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationDetailResponse(AbstractModel):
    """DescribeRotationDetail response structure.

    """

    def __init__(self):
        r"""
        :param _EnableRotation: Whether to enable rotation. `true`: enabled; `false`: disabled.
        :type EnableRotation: bool
        :param _Frequency: Rotation frequency in days. Default value: 1 day.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Frequency: int
        :param _LatestRotateTime: Last rotation time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestRotateTime: str
        :param _NextRotateBeginTime: Next rotation start time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NextRotateBeginTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnableRotation = None
        self._Frequency = None
        self._LatestRotateTime = None
        self._NextRotateBeginTime = None
        self._RequestId = None

    @property
    def EnableRotation(self):
        """Whether to enable rotation. `true`: enabled; `false`: disabled.
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def Frequency(self):
        """Rotation frequency in days. Default value: 1 day.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def LatestRotateTime(self):
        """Last rotation time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LatestRotateTime

    @LatestRotateTime.setter
    def LatestRotateTime(self, LatestRotateTime):
        self._LatestRotateTime = LatestRotateTime

    @property
    def NextRotateBeginTime(self):
        """Next rotation start time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NextRotateBeginTime

    @NextRotateBeginTime.setter
    def NextRotateBeginTime(self, NextRotateBeginTime):
        self._NextRotateBeginTime = NextRotateBeginTime

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnableRotation = params.get("EnableRotation")
        self._Frequency = params.get("Frequency")
        self._LatestRotateTime = params.get("LatestRotateTime")
        self._NextRotateBeginTime = params.get("NextRotateBeginTime")
        self._RequestId = params.get("RequestId")


class DescribeRotationHistoryRequest(AbstractModel):
    """DescribeRotationHistory request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Specifies the name of the credential for which to get the credential rotation records.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Specifies the name of the credential for which to get the credential rotation records.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationHistoryResponse(AbstractModel):
    """DescribeRotationHistory response structure.

    """

    def __init__(self):
        r"""
        :param _VersionIDs: List of version numbers.
        :type VersionIDs: list of str
        :param _TotalCount: Number of version numbers. The maximum number of version numbers that can be shown to users is 10.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VersionIDs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VersionIDs(self):
        """List of version numbers.
        :rtype: list of str
        """
        return self._VersionIDs

    @VersionIDs.setter
    def VersionIDs(self, VersionIDs):
        self._VersionIDs = VersionIDs

    @property
    def TotalCount(self):
        """Number of version numbers. The maximum number of version numbers that can be shown to users is 10.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionIDs = params.get("VersionIDs")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of a Secret whose detailed information is to be obtained.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of a Secret whose detailed information is to be obtained.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _Description: Description of the Secret.
        :type Description: str
        :param _KmsKeyId: ID of the KMS CMK used for encryption.
        :type KmsKeyId: str
        :param _CreateUin: Creator UIN.
        :type CreateUin: int
        :param _Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :type Status: str
        :param _DeleteTime: Deletion time, formatted as a Unix timestamp. For a Secret that is not in `PendingDelete` status, this value is 0.
        :type DeleteTime: int
        :param _CreateTime: Creation time.
        :type CreateTime: int
        :param _SecretType: `0`: user-defined secret; `1`: database credential; `2`: SSH key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretType: int
        :param _ProductName: Tencent Cloud service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param _ResourceID: Tencent Cloud service instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceID: str
        :param _RotationStatus: Whether to enable rotation. `True`: enable rotation; `False`: disable rotation.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RotationStatus: bool
        :param _RotationFrequency: Rotation frequency in days by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RotationFrequency: int
        :param _ResourceName: Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param _ProjectID: Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectID: int
        :param _AssociatedInstanceIDs: ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedInstanceIDs: list of str
        :param _TargetUin: UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetUin: int
        :param _AdditionalConfig: Additional configuration of the Secret
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdditionalConfig: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._Description = None
        self._KmsKeyId = None
        self._CreateUin = None
        self._Status = None
        self._DeleteTime = None
        self._CreateTime = None
        self._SecretType = None
        self._ProductName = None
        self._ResourceID = None
        self._RotationStatus = None
        self._RotationFrequency = None
        self._ResourceName = None
        self._ProjectID = None
        self._AssociatedInstanceIDs = None
        self._TargetUin = None
        self._AdditionalConfig = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """Description of the Secret.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """ID of the KMS CMK used for encryption.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def CreateUin(self):
        """Creator UIN.
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Status(self):
        """Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeleteTime(self):
        """Deletion time, formatted as a Unix timestamp. For a Secret that is not in `PendingDelete` status, this value is 0.
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecretType(self):
        """`0`: user-defined secret; `1`: database credential; `2`: SSH key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """Tencent Cloud service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceID(self):
        """Tencent Cloud service instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def RotationStatus(self):
        """Whether to enable rotation. `True`: enable rotation; `False`: disable rotation.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RotationStatus

    @RotationStatus.setter
    def RotationStatus(self, RotationStatus):
        self._RotationStatus = RotationStatus

    @property
    def RotationFrequency(self):
        """Rotation frequency in days by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency

    @property
    def ResourceName(self):
        """Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ProjectID(self):
        """Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def AssociatedInstanceIDs(self):
        """ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssociatedInstanceIDs

    @AssociatedInstanceIDs.setter
    def AssociatedInstanceIDs(self, AssociatedInstanceIDs):
        self._AssociatedInstanceIDs = AssociatedInstanceIDs

    @property
    def TargetUin(self):
        """UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def AdditionalConfig(self):
        """Additional configuration of the Secret
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdditionalConfig

    @AdditionalConfig.setter
    def AdditionalConfig(self, AdditionalConfig):
        self._AdditionalConfig = AdditionalConfig

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._CreateUin = params.get("CreateUin")
        self._Status = params.get("Status")
        self._DeleteTime = params.get("DeleteTime")
        self._CreateTime = params.get("CreateTime")
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        self._ResourceID = params.get("ResourceID")
        self._RotationStatus = params.get("RotationStatus")
        self._RotationFrequency = params.get("RotationFrequency")
        self._ResourceName = params.get("ResourceName")
        self._ProjectID = params.get("ProjectID")
        self._AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self._TargetUin = params.get("TargetUin")
        self._AdditionalConfig = params.get("AdditionalConfig")
        self._RequestId = params.get("RequestId")


class DescribeSupportedProductsRequest(AbstractModel):
    """DescribeSupportedProducts request structure.

    """


class DescribeSupportedProductsResponse(AbstractModel):
    """DescribeSupportedProducts response structure.

    """

    def __init__(self):
        r"""
        :param _Products: List of supported services.
        :type Products: list of str
        :param _TotalCount: Number of supported services
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Products = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Products(self):
        """List of supported services.
        :rtype: list of str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TotalCount(self):
        """Number of supported services
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Products = params.get("Products")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DisableSecretRequest(AbstractModel):
    """DisableSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret to be disabled.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of the Secret to be disabled.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableSecretResponse(AbstractModel):
    """DisableSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the disabled Secret.
        :type SecretName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the disabled Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret to be enabled.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of the Secret to be enabled.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSecretResponse(AbstractModel):
    """EnableSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the enabled Secret.
        :type SecretName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the enabled Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions request structure.

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Regions: List of regions.
        :type Regions: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        """List of regions.
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class GetSSHKeyPairValueRequest(AbstractModel):
    """GetSSHKeyPairValue request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Secret name. This field is only valid for SSH key secrets.
        :type SecretName: str
        :param _SSHKeyId: ID of the key pair, which is the unique identifier of the key pair in the CVM.
        :type SSHKeyId: str
        """
        self._SecretName = None
        self._SSHKeyId = None

    @property
    def SecretName(self):
        """Secret name. This field is only valid for SSH key secrets.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SSHKeyId(self):
        """ID of the key pair, which is the unique identifier of the key pair in the CVM.
        :rtype: str
        """
        return self._SSHKeyId

    @SSHKeyId.setter
    def SSHKeyId(self, SSHKeyId):
        self._SSHKeyId = SSHKeyId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._SSHKeyId = params.get("SSHKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSSHKeyPairValueResponse(AbstractModel):
    """GetSSHKeyPairValue response structure.

    """

    def __init__(self):
        r"""
        :param _SSHKeyID: ID of the SSH key.
        :type SSHKeyID: str
        :param _PublicKey: Plaintext value of the Base64-encoded public key.
        :type PublicKey: str
        :param _PrivateKey: Plaintext value of the Base64-encoded private key.
        :type PrivateKey: str
        :param _ProjectID: ID of the project to which the SSH key belongs.
        :type ProjectID: int
        :param _SSHKeyDescription: Description of the SSH key.
The description can be modified in the CVM console.
        :type SSHKeyDescription: str
        :param _SSHKeyName: Name of the SSH key.
The name can be modified in the CVM console.
        :type SSHKeyName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SSHKeyID = None
        self._PublicKey = None
        self._PrivateKey = None
        self._ProjectID = None
        self._SSHKeyDescription = None
        self._SSHKeyName = None
        self._RequestId = None

    @property
    def SSHKeyID(self):
        """ID of the SSH key.
        :rtype: str
        """
        return self._SSHKeyID

    @SSHKeyID.setter
    def SSHKeyID(self, SSHKeyID):
        self._SSHKeyID = SSHKeyID

    @property
    def PublicKey(self):
        """Plaintext value of the Base64-encoded public key.
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        """Plaintext value of the Base64-encoded private key.
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ProjectID(self):
        """ID of the project to which the SSH key belongs.
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def SSHKeyDescription(self):
        """Description of the SSH key.
The description can be modified in the CVM console.
        :rtype: str
        """
        return self._SSHKeyDescription

    @SSHKeyDescription.setter
    def SSHKeyDescription(self, SSHKeyDescription):
        self._SSHKeyDescription = SSHKeyDescription

    @property
    def SSHKeyName(self):
        """Name of the SSH key.
The name can be modified in the CVM console.
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SSHKeyID = params.get("SSHKeyID")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._ProjectID = params.get("ProjectID")
        self._SSHKeyDescription = params.get("SSHKeyDescription")
        self._SSHKeyName = params.get("SSHKeyName")
        self._RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of a Secret.
        :type SecretName: str
        :param _VersionId: Specifies the version number of the corresponding credential.
For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.
        :type VersionId: str
        """
        self._SecretName = None
        self._VersionId = None

    @property
    def SecretName(self):
        """Name of a Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """Specifies the version number of the corresponding credential.
For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _VersionId: ID of the Secret version.
        :type VersionId: str
        :param _SecretBinary: When creating a credential (CreateSecret), if you specify binary data, this field will be the Base64-encoded returned result. The application needs to Base64-decode the result to get the original data.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretBinary: str
        :param _SecretString: When creating a credential (CreateSecret), if you specify general text data, this field will be the returned result.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretString: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """ID of the Secret version.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """When creating a credential (CreateSecret), if you specify binary data, this field will be the Base64-encoded returned result. The application needs to Base64-decode the result to get the original data.
Either `SecretBinary` or `SecretString` cannot be empty.
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """When creating a credential (CreateSecret), if you specify general text data, this field will be the returned result.
Either `SecretBinary` or `SecretString` cannot be empty.
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        self._RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: `true`: The service is activated; `false`: The service is not activated.
        :type ServiceEnabled: bool
        :param _InvalidType: Invalid service type. `0`: not purchased; `1`: normal; `2`: suspended due to arrears; `3`: resource released
        :type InvalidType: int
        :param _AccessKeyEscrowEnabled: `true`: Allow SSM to manage Tencent Cloud API key secrets.
`false`: Forbid SSM to manage Tencent Cloud API key secrets.
        :type AccessKeyEscrowEnabled: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._InvalidType = None
        self._AccessKeyEscrowEnabled = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        """`true`: The service is activated; `false`: The service is not activated.
        :rtype: bool
        """
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def InvalidType(self):
        """Invalid service type. `0`: not purchased; `1`: normal; `2`: suspended due to arrears; `3`: resource released
        :rtype: int
        """
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def AccessKeyEscrowEnabled(self):
        """`true`: Allow SSM to manage Tencent Cloud API key secrets.
`false`: Forbid SSM to manage Tencent Cloud API key secrets.
        :rtype: bool
        """
        return self._AccessKeyEscrowEnabled

    @AccessKeyEscrowEnabled.setter
    def AccessKeyEscrowEnabled(self, AccessKeyEscrowEnabled):
        self._AccessKeyEscrowEnabled = AccessKeyEscrowEnabled

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._InvalidType = params.get("InvalidType")
        self._AccessKeyEscrowEnabled = params.get("AccessKeyEscrowEnabled")
        self._RequestId = params.get("RequestId")


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _Versions: `VersionId` list.
Note: This field may return `null`, indicating that no valid value was found.
        :type Versions: list of VersionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._Versions = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Versions(self):
        """`VersionId` list.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of VersionInfo
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class ListSecretsRequest(AbstractModel):
    """ListSecrets request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of the list, starting at 0. If not specified, 0 is used by default.
        :type Offset: int
        :param _Limit: Maximum number of returned Secrets in a query. If not set or set to 0, 20 is used by default.
        :type Limit: int
        :param _OrderType: Sorting order according to the creation time. If not set or set to 0, descending order is used; if set to 1, ascending order is used.
        :type OrderType: int
        :param _State: Filter based on credential status.
The default value is 0, indicating to query all.
1: query the list of credentials in `Enabled` status.
2: query the list of credentials in `Disabled` status.
3: query the list of credentials in `PendingDelete` status.
4: query the list of credentials in `PendingCreate` status.
5: query the list of credentials in `CreateFailed` status.
The `PendingCreate` and `CreateFailed` status only take effect when `SecretType` is Tencent Cloud service credential
        :type State: int
        :param _SearchSecretName: Filter according to Secret names. If left empty, this filter is not applied.
        :type SearchSecretName: str
        :param _TagFilters: Tag filter.
        :type TagFilters: list of TagFilter
        :param _SecretType: `0` (default): user-defined secret.
`1`: Tencent Cloud services secret.
`2`: SSH key secret.
`3`: Tencent Cloud API key secret.
        :type SecretType: int
        :param _ProductName: This parameter only takes effect when the value of the SecretType parameter is 1.\nWhen the value of SecretType is `1`:
If the ProductName value is empty, it means querying all types of Tencent Cloud product secrets;If the ProductName value is a specific cloud product value such as MySQL, it means querying MySQL database credential;If the ProductName value is multiple cloud product values, such as: Mysql, Tdsql-mysql, Tdsql_C_Mysql (multiple values are separated by commas in English), it means querying the secrets of three cloud product types;To query the list of supported cloud products, use the interface: `DescribeSupportedProducts`.
        :type ProductName: str
        """
        self._Offset = None
        self._Limit = None
        self._OrderType = None
        self._State = None
        self._SearchSecretName = None
        self._TagFilters = None
        self._SecretType = None
        self._ProductName = None

    @property
    def Offset(self):
        """Starting position of the list, starting at 0. If not specified, 0 is used by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of returned Secrets in a query. If not set or set to 0, 20 is used by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderType(self):
        """Sorting order according to the creation time. If not set or set to 0, descending order is used; if set to 1, ascending order is used.
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def State(self):
        """Filter based on credential status.
The default value is 0, indicating to query all.
1: query the list of credentials in `Enabled` status.
2: query the list of credentials in `Disabled` status.
3: query the list of credentials in `PendingDelete` status.
4: query the list of credentials in `PendingCreate` status.
5: query the list of credentials in `CreateFailed` status.
The `PendingCreate` and `CreateFailed` status only take effect when `SecretType` is Tencent Cloud service credential
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SearchSecretName(self):
        """Filter according to Secret names. If left empty, this filter is not applied.
        :rtype: str
        """
        return self._SearchSecretName

    @SearchSecretName.setter
    def SearchSecretName(self, SearchSecretName):
        self._SearchSecretName = SearchSecretName

    @property
    def TagFilters(self):
        """Tag filter.
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def SecretType(self):
        """`0` (default): user-defined secret.
`1`: Tencent Cloud services secret.
`2`: SSH key secret.
`3`: Tencent Cloud API key secret.
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """This parameter only takes effect when the value of the SecretType parameter is 1.\nWhen the value of SecretType is `1`:
If the ProductName value is empty, it means querying all types of Tencent Cloud product secrets;If the ProductName value is a specific cloud product value such as MySQL, it means querying MySQL database credential;If the ProductName value is multiple cloud product values, such as: Mysql, Tdsql-mysql, Tdsql_C_Mysql (multiple values are separated by commas in English), it means querying the secrets of three cloud product types;To query the list of supported cloud products, use the interface: `DescribeSupportedProducts`.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderType = params.get("OrderType")
        self._State = params.get("State")
        self._SearchSecretName = params.get("SearchSecretName")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretsResponse(AbstractModel):
    """ListSecrets response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of filtered Secrets according to `State` and `SearchSecretName`.
        :type TotalCount: int
        :param _SecretMetadatas: List of Secret information.
        :type SecretMetadatas: list of SecretMetadata
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecretMetadatas = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of filtered Secrets according to `State` and `SearchSecretName`.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecretMetadatas(self):
        """List of Secret information.
        :rtype: list of SecretMetadata
        """
        return self._SecretMetadatas

    @SecretMetadatas.setter
    def SecretMetadatas(self, SecretMetadatas):
        self._SecretMetadatas = SecretMetadatas

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SecretMetadatas") is not None:
            self._SecretMetadatas = []
            for item in params.get("SecretMetadatas"):
                obj = SecretMetadata()
                obj._deserialize(item)
                self._SecretMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class ProductPrivilegeUnit(AbstractModel):
    """Permission granted when the credential is associated with the service

    """

    def __init__(self):
        r"""
        :param _PrivilegeName: Permission name. Valid values:
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

When the permission is `DatabasePrivileges`, the database name must be specified by the `Database` parameter;

When the permission is `TablePrivileges`, the database name and the table name in the database must be specified by the `Database` and `TableName` parameters;

When the permission is `ColumnPrivileges`, the database name, table name in the database, and column name in the table must be specified by the `Database`, `TableName`, and `ColumnName` parameters.
        :type PrivilegeName: str
        :param _Privileges: Permission list.
For the `Mysql` service, optional permission values are:

1. Valid values of `GlobalPrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

2. Valid values of `DatabasePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

3. Valid values of `TablePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

4. Valid values of `ColumnPrivileges`: "SELECT","INSERT","UPDATE","REFERENCES".
Note: if this parameter is not passed in, it means to clear the permission.
        :type Privileges: list of str
        :param _Database: This value takes effect only when `PrivilegeName` is `DatabasePrivileges`.
        :type Database: str
        :param _TableName: This value takes effect only when `PrivilegeName` is `TablePrivileges`, and the `Database` parameter is required in this case to explicitly indicate the database instance.
        :type TableName: str
        :param _ColumnName: This value takes effect only when `PrivilegeName` is `ColumnPrivileges`, and the following parameters are required in this case:
Database: explicitly indicate the database instance.
TableName: explicitly indicate the table
        :type ColumnName: str
        """
        self._PrivilegeName = None
        self._Privileges = None
        self._Database = None
        self._TableName = None
        self._ColumnName = None

    @property
    def PrivilegeName(self):
        """Permission name. Valid values:
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

When the permission is `DatabasePrivileges`, the database name must be specified by the `Database` parameter;

When the permission is `TablePrivileges`, the database name and the table name in the database must be specified by the `Database` and `TableName` parameters;

When the permission is `ColumnPrivileges`, the database name, table name in the database, and column name in the table must be specified by the `Database`, `TableName`, and `ColumnName` parameters.
        :rtype: str
        """
        return self._PrivilegeName

    @PrivilegeName.setter
    def PrivilegeName(self, PrivilegeName):
        self._PrivilegeName = PrivilegeName

    @property
    def Privileges(self):
        """Permission list.
For the `Mysql` service, optional permission values are:

1. Valid values of `GlobalPrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

2. Valid values of `DatabasePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

3. Valid values of `TablePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

4. Valid values of `ColumnPrivileges`: "SELECT","INSERT","UPDATE","REFERENCES".
Note: if this parameter is not passed in, it means to clear the permission.
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        """This value takes effect only when `PrivilegeName` is `DatabasePrivileges`.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def TableName(self):
        """This value takes effect only when `PrivilegeName` is `TablePrivileges`, and the `Database` parameter is required in this case to explicitly indicate the database instance.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def ColumnName(self):
        """This value takes effect only when `PrivilegeName` is `ColumnPrivileges`, and the following parameters are required in this case:
Database: explicitly indicate the database instance.
TableName: explicitly indicate the table
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._PrivilegeName = params.get("PrivilegeName")
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        self._TableName = params.get("TableName")
        self._ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of a Secret where the version is added to.
        :type SecretName: str
        :param _VersionId: ID of the new Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type VersionId: str
        :param _SecretBinary: Base64-encoded binary credential information.
Either `SecretBinary` or `SecretString` must be set.
        :type SecretBinary: str
        :param _SecretString: Secret information plaintext in text format, base64 encoding is not needed. Either `SecretBinary` or `SecretString` must be set.
        :type SecretString: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None

    @property
    def SecretName(self):
        """Name of a Secret where the version is added to.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """ID of the new Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """Base64-encoded binary credential information.
Either `SecretBinary` or `SecretString` must be set.
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """Secret information plaintext in text format, base64 encoding is not needed. Either `SecretBinary` or `SecretString` must be set.
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _VersionId: Version ID that is newly added.
        :type VersionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """Version ID that is newly added.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret to be restored.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of the Secret to be restored.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class RotateProductSecretRequest(AbstractModel):
    """RotateProductSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the credential to be rotated.
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """Name of the credential to be rotated.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RotateProductSecretResponse(AbstractModel):
    """RotateProductSecret response structure.

    """

    def __init__(self):
        r"""
        :param _FlowID: Asynchronous rotation task ID. This field is valid when `SecretType` is `1` (i.e., the secret type is Tencent Cloud services secret, such as MySQL/TDSQL credentials).
        :type FlowID: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowID = None
        self._RequestId = None

    @property
    def FlowID(self):
        """Asynchronous rotation task ID. This field is valid when `SecretType` is `1` (i.e., the secret type is Tencent Cloud services secret, such as MySQL/TDSQL credentials).
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowID = params.get("FlowID")
        self._RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """Basic information of the Secret.

    """

    def __init__(self):
        r"""
        :param _SecretName: Credential name
        :type SecretName: str
        :param _Description: Credential description
        :type Description: str
        :param _KmsKeyId: KMS `KeyId` used to encrypt the credential
        :type KmsKeyId: str
        :param _CreateUin: Creator UIN
        :type CreateUin: int
        :param _Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :type Status: str
        :param _DeleteTime: Credential deletion date, which takes effect for credentials in `PendingDelete` status and is in UNIX timestamp format
        :type DeleteTime: int
        :param _CreateTime: Credential creation time in UNIX timestamp format
        :type CreateTime: int
        :param _KmsKeyType: Type of the KMS CMK used to encrypt the credential. `DEFAULT` represents the default key created by Secrets Manager, and `CUSTOMER` represents the user-specified key
        :type KmsKeyType: str
        :param _RotationStatus: 1: enable rotation; 0: disable rotation
Note: this field may return null, indicating that no valid values can be obtained.
        :type RotationStatus: int
        :param _NextRotationTime: Start time of the next rotation in UNIX timestamp format
Note: this field may return null, indicating that no valid values can be obtained.
        :type NextRotationTime: int
        :param _SecretType: 0: custom secret;1: database credential;2: SSH key secret;3: cloud API key secret;4: Redis secret;Note: This field may return `null`, indicating no valid value can be obtained.
        :type SecretType: int
        :param _ProductName: Tencent Cloud service name, which takes effect only when `SecretType` is 1 (Tencent Cloud service credential)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param _ResourceName: Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param _ProjectID: Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProjectID: int
        :param _AssociatedInstanceIDs: ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AssociatedInstanceIDs: list of str
        :param _TargetUin: UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetUin: int
        :param _RotationFrequency: Rotation frequency in days. It takes effect when the rotation feature is enabled. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type RotationFrequency: int
        :param _ResourceID: ID of Tencent Cloud resource corresponding with the Secret. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceID: str
        :param _RotationBeginTime: The rotation start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RotationBeginTime: str
        """
        self._SecretName = None
        self._Description = None
        self._KmsKeyId = None
        self._CreateUin = None
        self._Status = None
        self._DeleteTime = None
        self._CreateTime = None
        self._KmsKeyType = None
        self._RotationStatus = None
        self._NextRotationTime = None
        self._SecretType = None
        self._ProductName = None
        self._ResourceName = None
        self._ProjectID = None
        self._AssociatedInstanceIDs = None
        self._TargetUin = None
        self._RotationFrequency = None
        self._ResourceID = None
        self._RotationBeginTime = None

    @property
    def SecretName(self):
        """Credential name
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """Credential description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """KMS `KeyId` used to encrypt the credential
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def CreateUin(self):
        """Creator UIN
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Status(self):
        """Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeleteTime(self):
        """Credential deletion date, which takes effect for credentials in `PendingDelete` status and is in UNIX timestamp format
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def CreateTime(self):
        """Credential creation time in UNIX timestamp format
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def KmsKeyType(self):
        """Type of the KMS CMK used to encrypt the credential. `DEFAULT` represents the default key created by Secrets Manager, and `CUSTOMER` represents the user-specified key
        :rtype: str
        """
        return self._KmsKeyType

    @KmsKeyType.setter
    def KmsKeyType(self, KmsKeyType):
        self._KmsKeyType = KmsKeyType

    @property
    def RotationStatus(self):
        """1: enable rotation; 0: disable rotation
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RotationStatus

    @RotationStatus.setter
    def RotationStatus(self, RotationStatus):
        self._RotationStatus = RotationStatus

    @property
    def NextRotationTime(self):
        """Start time of the next rotation in UNIX timestamp format
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NextRotationTime

    @NextRotationTime.setter
    def NextRotationTime(self, NextRotationTime):
        self._NextRotationTime = NextRotationTime

    @property
    def SecretType(self):
        """0: custom secret;1: database credential;2: SSH key secret;3: cloud API key secret;4: Redis secret;Note: This field may return `null`, indicating no valid value can be obtained.
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """Tencent Cloud service name, which takes effect only when `SecretType` is 1 (Tencent Cloud service credential)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceName(self):
        """Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ProjectID(self):
        """Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def AssociatedInstanceIDs(self):
        """ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssociatedInstanceIDs

    @AssociatedInstanceIDs.setter
    def AssociatedInstanceIDs(self, AssociatedInstanceIDs):
        self._AssociatedInstanceIDs = AssociatedInstanceIDs

    @property
    def TargetUin(self):
        """UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def RotationFrequency(self):
        """Rotation frequency in days. It takes effect when the rotation feature is enabled. 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency

    @property
    def ResourceID(self):
        """ID of Tencent Cloud resource corresponding with the Secret. 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def RotationBeginTime(self):
        """The rotation start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._CreateUin = params.get("CreateUin")
        self._Status = params.get("Status")
        self._DeleteTime = params.get("DeleteTime")
        self._CreateTime = params.get("CreateTime")
        self._KmsKeyType = params.get("KmsKeyType")
        self._RotationStatus = params.get("RotationStatus")
        self._NextRotationTime = params.get("NextRotationTime")
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        self._ResourceName = params.get("ResourceName")
        self._ProjectID = params.get("ProjectID")
        self._AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self._TargetUin = params.get("TargetUin")
        self._RotationFrequency = params.get("RotationFrequency")
        self._ResourceID = params.get("ResourceID")
        self._RotationBeginTime = params.get("RotationBeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag key and tag value.

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
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: str
        """
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
    """Tag filter.

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
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: list of str
        """
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
        


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of a Secret whose description is to be updated.
        :type SecretName: str
        :param _Description: New description information, which can be up to 2048 bytes.
        :type Description: str
        """
        self._SecretName = None
        self._Description = None

    @property
    def SecretName(self):
        """Name of a Secret whose description is to be updated.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """New description information, which can be up to 2048 bytes.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class UpdateRotationStatusRequest(AbstractModel):
    """UpdateRotationStatus request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Tencent Cloud service credential name.
        :type SecretName: str
        :param _EnableRotation: Specifies whether to enable rotation.
`true`: enables rotation.
`false`: disables rotation.
        :type EnableRotation: bool
        :param _Frequency: Rotation frequency in days. Value range: 30–365.
        :type Frequency: int
        :param _RotationBeginTime: User-defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `true` and `RotationBeginTime` is left empty, the current time will be entered by default.
        :type RotationBeginTime: str
        """
        self._SecretName = None
        self._EnableRotation = None
        self._Frequency = None
        self._RotationBeginTime = None

    @property
    def SecretName(self):
        """Tencent Cloud service credential name.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnableRotation(self):
        """Specifies whether to enable rotation.
`true`: enables rotation.
`false`: disables rotation.
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def Frequency(self):
        """Rotation frequency in days. Value range: 30–365.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def RotationBeginTime(self):
        """User-defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `true` and `RotationBeginTime` is left empty, the current time will be entered by default.
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._EnableRotation = params.get("EnableRotation")
        self._Frequency = params.get("Frequency")
        self._RotationBeginTime = params.get("RotationBeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRotationStatusResponse(AbstractModel):
    """UpdateRotationStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret request structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of a Secret whose content is to be updated.
        :type SecretName: str
        :param _VersionId: ID of the Secret version whose content is to be updated.
        :type VersionId: str
        :param _SecretBinary: This field should be used and Base64-encoded if the content of the new credential is binary.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretBinary: str
        :param _SecretString: This field should be used without being Base64-encoded if the content of the new credential is text. Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretString: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None

    @property
    def SecretName(self):
        """Name of a Secret whose content is to be updated.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """ID of the Secret version whose content is to be updated.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """This field should be used and Base64-encoded if the content of the new credential is binary.
Either `SecretBinary` or `SecretString` cannot be empty.
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """This field should be used without being Base64-encoded if the content of the new credential is text. Either `SecretBinary` or `SecretString` cannot be empty.
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret response structure.

    """

    def __init__(self):
        r"""
        :param _SecretName: Name of the Secret.
        :type SecretName: str
        :param _VersionId: Version ID of the Secret.
        :type VersionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """Name of the Secret.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """Version ID of the Secret.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """List of version ID information.

    """

    def __init__(self):
        r"""
        :param _VersionId: Version ID.
        :type VersionId: str
        :param _CreateTime: Creation time, formatted as a Unix timestamp.
        :type CreateTime: int
        """
        self._VersionId = None
        self._CreateTime = None

    @property
    def VersionId(self):
        """Version ID.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateTime(self):
        """Creation time, formatted as a Unix timestamp.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        