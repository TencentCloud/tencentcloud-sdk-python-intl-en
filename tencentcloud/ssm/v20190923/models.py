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
        :param SecretName: Credential name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens, and underscores and must begin with a letter or digit.
        :type SecretName: str
        :param UserNamePrefix: Prefix of the user account name, which is specified by you and can contain up to 8 characters.
Supported character sets include:
Digits: [0, 9].
Lowercase letters: [a, z].
Uppercase letters: [A, Z].
Special symbols: underscore.
The prefix must begin with a letter.
        :type UserNamePrefix: str
        :param ProductName: Name of the Tencent Cloud service bound to the credential, such as `Mysql`. The `DescribeSupportedProducts` API can be used to get the names of the supported Tencent Cloud services.
        :type ProductName: str
        :param InstanceID: Tencent Cloud service instance ID.
        :type InstanceID: str
        :param Domains: Domain name of the account in the form of IP. You can enter `%`.
        :type Domains: list of str
        :param PrivilegesList: List of permissions that need to be granted when the credential is bound to a Tencent Cloud service.
        :type PrivilegesList: list of ProductPrivilegeUnit
        :param Description: Description, which is used to describe the purpose in detail and can contain up to 2,048 bytes.
        :type Description: str
        :param KmsKeyId: Specifies the KMS CMK that encrypts the credential.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :type KmsKeyId: str
        :param Tags: List of tags.
        :type Tags: list of Tag
        :param RotationBeginTime: User-Defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `True`, this parameter is required.
        :type RotationBeginTime: str
        :param EnableRotation: Specifies whether to enable rotation
True - enable
False - do not enable
If this parameter is not specified, `False` will be used by default.
        :type EnableRotation: bool
        :param RotationFrequency: Rotation frequency in days. Default value: 1 day.
        :type RotationFrequency: int
        """
        self.SecretName = None
        self.UserNamePrefix = None
        self.ProductName = None
        self.InstanceID = None
        self.Domains = None
        self.PrivilegesList = None
        self.Description = None
        self.KmsKeyId = None
        self.Tags = None
        self.RotationBeginTime = None
        self.EnableRotation = None
        self.RotationFrequency = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.UserNamePrefix = params.get("UserNamePrefix")
        self.ProductName = params.get("ProductName")
        self.InstanceID = params.get("InstanceID")
        self.Domains = params.get("Domains")
        if params.get("PrivilegesList") is not None:
            self.PrivilegesList = []
            for item in params.get("PrivilegesList"):
                obj = ProductPrivilegeUnit()
                obj._deserialize(item)
                self.PrivilegesList.append(obj)
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RotationBeginTime = params.get("RotationBeginTime")
        self.EnableRotation = params.get("EnableRotation")
        self.RotationFrequency = params.get("RotationFrequency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductSecretResponse(AbstractModel):
    """CreateProductSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the created credential.
        :type SecretName: str
        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagCode: int
        :param TagMsg: Tag operation return message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagMsg: str
        :param FlowID: ID of the created Tencent Cloud service credential async task.
        :type FlowID: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.TagCode = None
        self.TagMsg = None
        self.FlowID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.FlowID = params.get("FlowID")
        self.RequestId = params.get("RequestId")


class CreateSSHKeyPairSecretRequest(AbstractModel):
    """CreateSSHKeyPairSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Secret name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens and underscores and must begin with a letter or digit.
        :type SecretName: str
        :param ProjectId: ID of the project to which the created SSH key belongs.
        :type ProjectId: int
        :param Description: Description, such as what it is used for. It contains up to 2,048 bytes.
        :type Description: str
        :param KmsKeyId: Specifies a KMS CMK to encrypt the secret.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.
        :type KmsKeyId: str
        :param Tags: List of tags.
        :type Tags: list of Tag
        :param SSHKeyName: Name of the SSH key pair, which only contains digits, letters and underscores and must start with a digit or letter. The maximum length is 25 characters.
        :type SSHKeyName: str
        """
        self.SecretName = None
        self.ProjectId = None
        self.Description = None
        self.KmsKeyId = None
        self.Tags = None
        self.SSHKeyName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SSHKeyName = params.get("SSHKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSHKeyPairSecretResponse(AbstractModel):
    """CreateSSHKeyPairSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the created secret.
        :type SecretName: str
        :param SSHKeyID: ID of the created SSH key.
        :type SSHKeyID: str
        :param SSHKeyName: Name of the created SSH key.
        :type SSHKeyName: str
        :param TagCode: Tag return code. `0`: success; `1`: internal error; `2`: business processing error.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagCode: int
        :param TagMsg: Tag return message.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TagMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.SSHKeyID = None
        self.SSHKeyName = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.SSHKeyID = params.get("SSHKeyID")
        self.SSHKeyName = params.get("SSHKeyName")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class CreateSecretRequest(AbstractModel):
    """CreateSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Secret name, which must be unique within a region. The name can be up to 128 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type SecretName: str
        :param VersionId: Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit. `SecretName` and `VersionId` are used to query the Secret information.
        :type VersionId: str
        :param Description: Description information, such as the detailed use cases. It can be up to 2048 bytes.
        :type Description: str
        :param KmsKeyId: KMS CMK used for Secret encryption. If this parameter is left empty, SecretsManager will create a CMK by default. You can also specify a KMS CMK that is created in the same region.
        :type KmsKeyId: str
        :param SecretBinary: Base64-encoded plaintext of a binary Secret. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :type SecretBinary: str
        :param SecretString: Plaintext of a Secret, in text format. Base64 encoding is not required. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.
        :type SecretString: str
        :param Tags: List of tags.
        :type Tags: list of Tag
        """
        self.SecretName = None
        self.VersionId = None
        self.Description = None
        self.KmsKeyId = None
        self.SecretBinary = None
        self.SecretString = None
        self.Tags = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
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
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the new Secret.
        :type SecretName: str
        :param VersionId: ID of the new Secret version.
        :type VersionId: str
        :param TagCode: Return code of tag operation. `0`: success; `1`: internal error; `2`: business processing error
Note: This field may return `null`, indicating that no valid value was found.
        :type TagCode: int
        :param TagMsg: Return message of tag operation.
Note: This field may return `null`, indicating that no valid value was found.
        :type TagMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret to be deleted.
        :type SecretName: str
        :param RecoveryWindowInDays: Scheduled deletion time (in days), indicating the number of retention days for the secret. Value range: 0-30. If it is `0`, the secret is deleted immediately.
For an SSH key secret, this field can only be `0`.
        :type RecoveryWindowInDays: int
        :param CleanSSHKey: Specifies whether to delete the SSH key from both the secret and the SSH key list in the CVM console. This field is only valid for SSH key secrets. Valid values:
`True`: deletes SSH key from both the secret and SSH key list in the CVM console. Note that the deletion will fail if the SSH key is already bound to a CVM instance.
`False`: only deletes the SSH key information in the secret.
        :type CleanSSHKey: bool
        """
        self.SecretName = None
        self.RecoveryWindowInDays = None
        self.CleanSSHKey = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RecoveryWindowInDays = params.get("RecoveryWindowInDays")
        self.CleanSSHKey = params.get("CleanSSHKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of deleted Secret.
        :type SecretName: str
        :param DeleteTime: Secret deletion time, formatted as a Unix timestamp.
        :type DeleteTime: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.DeleteTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.DeleteTime = params.get("DeleteTime")
        self.RequestId = params.get("RequestId")


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: ID of the Secret version to be deleted.
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: Version ID of the Secret.
        :type VersionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param FlowID: Async task ID.
        :type FlowID: int
        """
        self.FlowID = None


    def _deserialize(self, params):
        self.FlowID = params.get("FlowID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        r"""
        :param TaskStatus: 0: processing, 1: processing succeeded, 2: processing failed
        :type TaskStatus: int
        :param Description: Task description.
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskStatus = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeRotationDetailRequest(AbstractModel):
    """DescribeRotationDetail request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Specifies the name of the credential for which to get the credential rotation details.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationDetailResponse(AbstractModel):
    """DescribeRotationDetail response structure.

    """

    def __init__(self):
        r"""
        :param EnableRotation: Whether to enable rotation. `true`: enabled; `false`: disabled.
        :type EnableRotation: bool
        :param Frequency: Rotation frequency in days. Default value: 1 day.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Frequency: int
        :param LatestRotateTime: Last rotation time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LatestRotateTime: str
        :param NextRotateBeginTime: Next rotation start time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NextRotateBeginTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnableRotation = None
        self.Frequency = None
        self.LatestRotateTime = None
        self.NextRotateBeginTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnableRotation = params.get("EnableRotation")
        self.Frequency = params.get("Frequency")
        self.LatestRotateTime = params.get("LatestRotateTime")
        self.NextRotateBeginTime = params.get("NextRotateBeginTime")
        self.RequestId = params.get("RequestId")


class DescribeRotationHistoryRequest(AbstractModel):
    """DescribeRotationHistory request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Specifies the name of the credential for which to get the credential rotation records.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationHistoryResponse(AbstractModel):
    """DescribeRotationHistory response structure.

    """

    def __init__(self):
        r"""
        :param VersionIDs: List of version numbers.
        :type VersionIDs: list of str
        :param TotalCount: Number of version numbers. The maximum number of version numbers that can be shown to users is 10.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VersionIDs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionIDs = params.get("VersionIDs")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of a Secret whose detailed information is to be obtained.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param Description: Description of the Secret.
        :type Description: str
        :param KmsKeyId: ID of the KMS CMK used for encryption.
        :type KmsKeyId: str
        :param CreateUin: Creator UIN.
        :type CreateUin: int
        :param Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :type Status: str
        :param DeleteTime: Deletion time, formatted as a Unix timestamp. For a Secret that is not in `PendingDelete` status, this value is 0.
        :type DeleteTime: int
        :param CreateTime: Creation time.
        :type CreateTime: int
        :param SecretType: `0`: user-defined secret; `1`: database credential; `2`: SSH key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretType: int
        :param ProductName: Tencent Cloud service name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param ResourceID: Tencent Cloud service instance ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceID: str
        :param RotationStatus: Whether to enable rotation. `True`: enable rotation; `False`: disable rotation.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RotationStatus: bool
        :param RotationFrequency: Rotation frequency in days by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RotationFrequency: int
        :param ResourceName: Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param ProjectID: Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectID: int
        :param AssociatedInstanceIDs: ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return null, indicating that no valid values can be obtained.
        :type AssociatedInstanceIDs: list of str
        :param TargetUin: UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TargetUin: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.SecretType = None
        self.ProductName = None
        self.ResourceID = None
        self.RotationStatus = None
        self.RotationFrequency = None
        self.ResourceName = None
        self.ProjectID = None
        self.AssociatedInstanceIDs = None
        self.TargetUin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.SecretType = params.get("SecretType")
        self.ProductName = params.get("ProductName")
        self.ResourceID = params.get("ResourceID")
        self.RotationStatus = params.get("RotationStatus")
        self.RotationFrequency = params.get("RotationFrequency")
        self.ResourceName = params.get("ResourceName")
        self.ProjectID = params.get("ProjectID")
        self.AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self.TargetUin = params.get("TargetUin")
        self.RequestId = params.get("RequestId")


class DescribeSupportedProductsRequest(AbstractModel):
    """DescribeSupportedProducts request structure.

    """


class DescribeSupportedProductsResponse(AbstractModel):
    """DescribeSupportedProducts response structure.

    """

    def __init__(self):
        r"""
        :param Products: List of supported services.
        :type Products: list of str
        :param TotalCount: Number of supported services
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Products = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Products = params.get("Products")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DisableSecretRequest(AbstractModel):
    """DisableSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret to be disabled.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableSecretResponse(AbstractModel):
    """DisableSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the disabled Secret.
        :type SecretName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret to be enabled.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSecretResponse(AbstractModel):
    """EnableSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the enabled Secret.
        :type SecretName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions request structure.

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions response structure.

    """

    def __init__(self):
        r"""
        :param Regions: List of regions.
        :type Regions: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetSSHKeyPairValueRequest(AbstractModel):
    """GetSSHKeyPairValue request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Secret name. This field is only valid for SSH key secrets.
        :type SecretName: str
        :param SSHKeyId: ID of the key pair, which is the unique identifier of the key pair in the CVM.
        :type SSHKeyId: str
        """
        self.SecretName = None
        self.SSHKeyId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.SSHKeyId = params.get("SSHKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSSHKeyPairValueResponse(AbstractModel):
    """GetSSHKeyPairValue response structure.

    """

    def __init__(self):
        r"""
        :param SSHKeyID: ID of the SSH key.
        :type SSHKeyID: str
        :param PublicKey: Plaintext value of the Base64-encoded public key.
        :type PublicKey: str
        :param PrivateKey: Plaintext value of the Base64-encoded private key.
        :type PrivateKey: str
        :param ProjectID: ID of the project to which the SSH key belongs.
        :type ProjectID: int
        :param SSHKeyDescription: Description of the SSH key.
The description can be modified in the CVM console.
        :type SSHKeyDescription: str
        :param SSHKeyName: Name of the SSH key.
The name can be modified in the CVM console.
        :type SSHKeyName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SSHKeyID = None
        self.PublicKey = None
        self.PrivateKey = None
        self.ProjectID = None
        self.SSHKeyDescription = None
        self.SSHKeyName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SSHKeyID = params.get("SSHKeyID")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.ProjectID = params.get("ProjectID")
        self.SSHKeyDescription = params.get("SSHKeyDescription")
        self.SSHKeyName = params.get("SSHKeyName")
        self.RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of a Secret.
        :type SecretName: str
        :param VersionId: Specifies the version number of the corresponding credential.
For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: ID of the Secret version.
        :type VersionId: str
        :param SecretBinary: When creating a credential (CreateSecret), if you specify binary data, this field will be the Base64-encoded returned result. The application needs to Base64-decode the result to get the original data.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretBinary: str
        :param SecretString: When creating a credential (CreateSecret), if you specify general text data, this field will be the returned result.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretString: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        r"""
        :param ServiceEnabled: `true`: The service is activated; `false`: The service is not activated.
        :type ServiceEnabled: bool
        :param InvalidType: Invalid service type. `0`: not purchased; `1`: normal; `2`: suspended due to arrears; `3`: resource released
        :type InvalidType: int
        :param AccessKeyEscrowEnabled: `true`: Allow SSM to manage Tencent Cloud API key secrets.
`false`: Forbid SSM to manage Tencent Cloud API key secrets.
        :type AccessKeyEscrowEnabled: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.AccessKeyEscrowEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.AccessKeyEscrowEnabled = params.get("AccessKeyEscrowEnabled")
        self.RequestId = params.get("RequestId")


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param Versions: `VersionId` list.
Note: This field may return `null`, indicating that no valid value was found.
        :type Versions: list of VersionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSecretsRequest(AbstractModel):
    """ListSecrets request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Starting position of the list, starting at 0. If not specified, 0 is used by default.
        :type Offset: int
        :param Limit: Maximum number of returned Secrets in a query. If not set or set to 0, 20 is used by default.
        :type Limit: int
        :param OrderType: Sorting order according to the creation time. If not set or set to 0, descending order is used; if set to 1, ascending order is used.
        :type OrderType: int
        :param State: Filter based on credential status.
The default value is 0, indicating to query all.
1: query the list of credentials in `Enabled` status.
2: query the list of credentials in `Disabled` status.
3: query the list of credentials in `PendingDelete` status.
4: query the list of credentials in `PendingCreate` status.
5: query the list of credentials in `CreateFailed` status.
The `PendingCreate` and `CreateFailed` status only take effect when `SecretType` is Tencent Cloud service credential
        :type State: int
        :param SearchSecretName: Filter according to Secret names. If left empty, this filter is not applied.
        :type SearchSecretName: str
        :param TagFilters: Tag filter.
        :type TagFilters: list of TagFilter
        :param SecretType: `0` (default): user-defined secret.
`1`: Tencent Cloud services secret.
`2`: SSH key secret.
`3`: Tencent Cloud API key secret.
        :type SecretType: int
        :param ProductName: This parameter is valid only when SecretType is `1`.
 
An empty value indicates querying all types of Tencent Cloud service secrets.
`Mysql`: queries MySQL database credentials.
`Tdsql-mysql`: queries TDSQL MySQL database credentials.
        :type ProductName: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderType = None
        self.State = None
        self.SearchSecretName = None
        self.TagFilters = None
        self.SecretType = None
        self.ProductName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderType = params.get("OrderType")
        self.State = params.get("State")
        self.SearchSecretName = params.get("SearchSecretName")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.SecretType = params.get("SecretType")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretsResponse(AbstractModel):
    """ListSecrets response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of filtered Secrets according to `State` and `SearchSecretName`.
        :type TotalCount: int
        :param SecretMetadatas: List of Secret information.
        :type SecretMetadatas: list of SecretMetadata
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecretMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecretMetadatas") is not None:
            self.SecretMetadatas = []
            for item in params.get("SecretMetadatas"):
                obj = SecretMetadata()
                obj._deserialize(item)
                self.SecretMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class ProductPrivilegeUnit(AbstractModel):
    """Permission granted when the credential is associated with the service

    """

    def __init__(self):
        r"""
        :param PrivilegeName: Permission name. Valid values:
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

When the permission is `DatabasePrivileges`, the database name must be specified by the `Database` parameter;

When the permission is `TablePrivileges`, the database name and the table name in the database must be specified by the `Database` and `TableName` parameters;

When the permission is `ColumnPrivileges`, the database name, table name in the database, and column name in the table must be specified by the `Database`, `TableName`, and `ColumnName` parameters.
        :type PrivilegeName: str
        :param Privileges: Permission list.
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
        :param Database: This value takes effect only when `PrivilegeName` is `DatabasePrivileges`.
        :type Database: str
        :param TableName: This value takes effect only when `PrivilegeName` is `TablePrivileges`, and the `Database` parameter is required in this case to explicitly indicate the database instance.
        :type TableName: str
        :param ColumnName: This value takes effect only when `PrivilegeName` is `ColumnPrivileges`, and the following parameters are required in this case:
Database: explicitly indicate the database instance.
TableName: explicitly indicate the table
        :type ColumnName: str
        """
        self.PrivilegeName = None
        self.Privileges = None
        self.Database = None
        self.TableName = None
        self.ColumnName = None


    def _deserialize(self, params):
        self.PrivilegeName = params.get("PrivilegeName")
        self.Privileges = params.get("Privileges")
        self.Database = params.get("Database")
        self.TableName = params.get("TableName")
        self.ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of a Secret where the version is added to.
        :type SecretName: str
        :param VersionId: ID of the new Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type VersionId: str
        :param SecretBinary: Base64-encoded binary credential information.
Either `SecretBinary` or `SecretString` must be set.
        :type SecretBinary: str
        :param SecretString: Secret information plaintext in text format, base64 encoding is not needed. Either `SecretBinary` or `SecretString` must be set.
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: Version ID that is newly added.
        :type VersionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret to be restored.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class RotateProductSecretRequest(AbstractModel):
    """RotateProductSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the credential to be rotated.
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RotateProductSecretResponse(AbstractModel):
    """RotateProductSecret response structure.

    """

    def __init__(self):
        r"""
        :param FlowID: Asynchronous rotation task ID. This field is valid when `SecretType` is `1` (i.e., the secret type is Tencent Cloud services secret, such as MySQL/TDSQL credentials).
        :type FlowID: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowID = params.get("FlowID")
        self.RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """Basic information of the Secret.

    """

    def __init__(self):
        r"""
        :param SecretName: Credential name
        :type SecretName: str
        :param Description: Credential description
        :type Description: str
        :param KmsKeyId: KMS `KeyId` used to encrypt the credential
        :type KmsKeyId: str
        :param CreateUin: Creator UIN
        :type CreateUin: int
        :param Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.
        :type Status: str
        :param DeleteTime: Credential deletion date, which takes effect for credentials in `PendingDelete` status and is in UNIX timestamp format
        :type DeleteTime: int
        :param CreateTime: Credential creation time in UNIX timestamp format
        :type CreateTime: int
        :param KmsKeyType: Type of the KMS CMK used to encrypt the credential. `DEFAULT` represents the default key created by Secrets Manager, and `CUSTOMER` represents the user-specified key
        :type KmsKeyType: str
        :param RotationStatus: 1: enable rotation; 0: disable rotation
Note: this field may return null, indicating that no valid values can be obtained.
        :type RotationStatus: int
        :param NextRotationTime: Start time of the next rotation in UNIX timestamp format
Note: this field may return null, indicating that no valid values can be obtained.
        :type NextRotationTime: int
        :param SecretType: `0`: user-defined secret.
`1`: Tencent Cloud services secret.
`2`: SSH key secret.
`3`: Tencent Cloud API key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretType: int
        :param ProductName: Tencent Cloud service name, which takes effect only when `SecretType` is 1 (Tencent Cloud service credential)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductName: str
        :param ResourceName: Secret name. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceName: str
        :param ProjectID: Project ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProjectID: int
        :param AssociatedInstanceIDs: ID of the CVM instance associated with the SSH key. ID. This field is only valid when the `SecretType` is set to `2` (SSH key secret).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AssociatedInstanceIDs: list of str
        :param TargetUin: UIN of the Tencent Cloud API key. This field is valid when the secret type is Tencent Cloud API key secret.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetUin: int
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.KmsKeyType = None
        self.RotationStatus = None
        self.NextRotationTime = None
        self.SecretType = None
        self.ProductName = None
        self.ResourceName = None
        self.ProjectID = None
        self.AssociatedInstanceIDs = None
        self.TargetUin = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.KmsKeyType = params.get("KmsKeyType")
        self.RotationStatus = params.get("RotationStatus")
        self.NextRotationTime = params.get("NextRotationTime")
        self.SecretType = params.get("SecretType")
        self.ProductName = params.get("ProductName")
        self.ResourceName = params.get("ResourceName")
        self.ProjectID = params.get("ProjectID")
        self.AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag key and tag value.

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
    """Tag filter.

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
        


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of a Secret whose description is to be updated.
        :type SecretName: str
        :param Description: New description information, which can be up to 2048 bytes.
        :type Description: str
        """
        self.SecretName = None
        self.Description = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class UpdateRotationStatusRequest(AbstractModel):
    """UpdateRotationStatus request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Tencent Cloud service credential name.
        :type SecretName: str
        :param EnableRotation: Specifies whether to enable rotation.
`true`: enables rotation.
`false`: disables rotation.
        :type EnableRotation: bool
        :param Frequency: Rotation frequency in days. Value range: 30–365.
        :type Frequency: int
        :param RotationBeginTime: User-defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `true` and `RotationBeginTime` is left empty, the current time will be entered by default.
        :type RotationBeginTime: str
        """
        self.SecretName = None
        self.EnableRotation = None
        self.Frequency = None
        self.RotationBeginTime = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.EnableRotation = params.get("EnableRotation")
        self.Frequency = params.get("Frequency")
        self.RotationBeginTime = params.get("RotationBeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRotationStatusResponse(AbstractModel):
    """UpdateRotationStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret request structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of a Secret whose content is to be updated.
        :type SecretName: str
        :param VersionId: ID of the Secret version whose content is to be updated.
        :type VersionId: str
        :param SecretBinary: This field should be used and Base64-encoded if the content of the new credential is binary.
Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretBinary: str
        :param SecretString: This field should be used without being Base64-encoded if the content of the new credential is text. Either `SecretBinary` or `SecretString` cannot be empty.
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret response structure.

    """

    def __init__(self):
        r"""
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: Version ID of the Secret.
        :type VersionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """List of version ID information.

    """

    def __init__(self):
        r"""
        :param VersionId: Version ID.
        :type VersionId: str
        :param CreateTime: Creation time, formatted as a Unix timestamp.
        :type CreateTime: int
        """
        self.VersionId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        