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
        """
        :param SecretName: Credential name, which must be unique in the same region. It can contain 128 bytes of letters, digits, hyphens, and underscores and must begin with a letter or digit.\n        :type SecretName: str\n        :param UserNamePrefix: Prefix of the user account name, which is specified by you and can contain up to 8 characters.
Supported character sets include:
Digits: [0, 9].
Lowercase letters: [a, z].
Uppercase letters: [A, Z].
Special symbols: underscore.
The prefix must begin with a letter.\n        :type UserNamePrefix: str\n        :param ProductName: Name of the Tencent Cloud service bound to the credential, such as `Mysql`. The `DescribeSupportedProducts` API can be used to get the names of the supported Tencent Cloud services.\n        :type ProductName: str\n        :param InstanceID: Tencent Cloud service instance ID.\n        :type InstanceID: str\n        :param Domains: Domain name of the account in the form of IP. You can enter `%`.\n        :type Domains: list of str\n        :param PrivilegesList: List of permissions that need to be granted when the credential is bound to a Tencent Cloud service.\n        :type PrivilegesList: list of ProductPrivilegeUnit\n        :param Description: Description, which is used to describe the purpose in detail and can contain up to 2,048 bytes.\n        :type Description: str\n        :param KmsKeyId: Specifies the KMS CMK that encrypts the credential.
If this parameter is left empty, the CMK created by Secrets Manager by default will be used for encryption.
You can also specify a custom KMS CMK created in the same region for encryption.\n        :type KmsKeyId: str\n        :param Tags: List of tags.\n        :type Tags: list of Tag\n        :param RotationBeginTime: User-Defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `True`, this parameter is required.\n        :type RotationBeginTime: str\n        :param EnableRotation: Specifies whether to enable rotation
True - enable
False - do not enable
If this parameter is not specified, `False` will be used by default.\n        :type EnableRotation: bool\n        :param RotationFrequency: Rotation frequency in days. Default value: 1 day.\n        :type RotationFrequency: int\n        """
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
        """
        :param SecretName: Name of the created credential.\n        :type SecretName: str\n        :param TagCode: Tag operation return code. 0: success; 1: internal error; 2: business processing error.
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagCode: int\n        :param TagMsg: Tag operation return message.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagMsg: str\n        :param FlowID: ID of the created Tencent Cloud service credential async task.\n        :type FlowID: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class CreateSecretRequest(AbstractModel):
    """CreateSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Secret name, which must be unique within a region. The name can be up to 128 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.\n        :type SecretName: str\n        :param VersionId: Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit. `SecretName` and `VersionId` are used to query the Secret information.\n        :type VersionId: str\n        :param Description: Description information, such as the detailed use cases. It can be up to 2048 bytes.\n        :type Description: str\n        :param KmsKeyId: KMS CMK used for Secret encryption. If this parameter is left empty, SecretsManager will create a CMK by default. You can also specify a KMS CMK that is created in the same region.\n        :type KmsKeyId: str\n        :param SecretBinary: Base64-encoded plaintext of a binary Secret. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.\n        :type SecretBinary: str\n        :param SecretString: Plaintext of a Secret, in text format. Base64 encoding is not required. Either `SecretBinary` or `SecretString` must be set. A maximum of 4096 bytes is supported.\n        :type SecretString: str\n        :param Tags: List of tags.\n        :type Tags: list of Tag\n        """
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
        """
        :param SecretName: Name of the new Secret.\n        :type SecretName: str\n        :param VersionId: ID of the new Secret version.\n        :type VersionId: str\n        :param TagCode: Return code of tag operation. `0`: success; `1`: internal error; `2`: business processing error
Note: This field may return `null`, indicating that no valid value was found.\n        :type TagCode: int\n        :param TagMsg: Return message of tag operation.
Note: This field may return `null`, indicating that no valid value was found.\n        :type TagMsg: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Name of the Secret to be deleted.\n        :type SecretName: str\n        :param RecoveryWindowInDays: Scheduled deletion time, in days. If set to 0, the Secret is deleted immediately. A number in the range of 1 to 30 indicates the number of retention days. The Secret will be deleted after the set value.\n        :type RecoveryWindowInDays: int\n        """
        self.SecretName = None
        self.RecoveryWindowInDays = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RecoveryWindowInDays = params.get("RecoveryWindowInDays")
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
        """
        :param SecretName: Name of deleted Secret.\n        :type SecretName: str\n        :param DeleteTime: Secret deletion time, formatted as a Unix timestamp.\n        :type DeleteTime: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param VersionId: ID of the Secret version to be deleted.\n        :type VersionId: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param VersionId: Version ID of the Secret.\n        :type VersionId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param FlowID: Async task ID.\n        :type FlowID: int\n        """
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
        """
        :param TaskStatus: 0: processing, 1: processing succeeded, 2: processing failed\n        :type TaskStatus: int\n        :param Description: Task description.\n        :type Description: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Specifies the name of the credential for which to get the credential rotation details.\n        :type SecretName: str\n        """
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
        """
        :param EnableRotation: Specifies whether to allow rotation. True: yes; False: no.\n        :type EnableRotation: bool\n        :param Frequency: Rotation frequency in days. Default value: 1 day.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Frequency: int\n        :param LatestRotateTime: Last rotation time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LatestRotateTime: str\n        :param NextRotateBeginTime: Next rotation start time, which is an explicitly visible time string in the format of 2006-01-02 15:04:05.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NextRotateBeginTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Specifies the name of the credential for which to get the credential rotation records.\n        :type SecretName: str\n        """
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
        """
        :param VersionIDs: List of version numbers.\n        :type VersionIDs: list of str\n        :param TotalCount: Number of version numbers. The maximum number of version numbers that can be shown to users is 10.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Name of a Secret whose detailed information is to be obtained.\n        :type SecretName: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param Description: Description of the Secret.\n        :type Description: str\n        :param KmsKeyId: ID of the KMS CMK used for encryption.\n        :type KmsKeyId: str\n        :param CreateUin: Creator UIN.\n        :type CreateUin: int\n        :param Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.\n        :type Status: str\n        :param DeleteTime: Deletion time, formatted as a Unix timestamp. For a Secret that is not in `PendingDelete` status, this value is 0.\n        :type DeleteTime: int\n        :param CreateTime: Creation time.\n        :type CreateTime: int\n        :param SecretType: 0: user-defined credential; 1: Tencent Cloud service credential.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SecretType: int\n        :param ProductName: Tencent Cloud service name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductName: str\n        :param ResourceID: Tencent Cloud service instance ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceID: str\n        :param RotationStatus: Whether to enable rotation. True: yes; False: no.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RotationStatus: bool\n        :param RotationFrequency: Rotation frequency in days by default.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RotationFrequency: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeSupportedProductsRequest(AbstractModel):
    """DescribeSupportedProducts request structure.

    """


class DescribeSupportedProductsResponse(AbstractModel):
    """DescribeSupportedProducts response structure.

    """

    def __init__(self):
        """
        :param Products: List of supported services.\n        :type Products: list of str\n        :param TotalCount: Number of supported services\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Name of the Secret to be disabled.\n        :type SecretName: str\n        """
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
        """
        :param SecretName: Name of the disabled Secret.\n        :type SecretName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret to be enabled.\n        :type SecretName: str\n        """
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
        """
        :param SecretName: Name of the enabled Secret.\n        :type SecretName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Regions: List of regions.\n        :type Regions: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret.\n        :type SecretName: str\n        :param VersionId: Specifies the version number of the corresponding credential.
For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.\n        :type VersionId: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param VersionId: ID of the Secret version.\n        :type VersionId: str\n        :param SecretBinary: When creating a credential (CreateSecret), if you specify binary data, this field will be the Base64-encoded returned result. The application needs to Base64-decode the result to get the original data.
Either `SecretBinary` or `SecretString` cannot be empty.\n        :type SecretBinary: str\n        :param SecretString: When creating a credential (CreateSecret), if you specify general text data, this field will be the returned result.
Either `SecretBinary` or `SecretString` cannot be empty.\n        :type SecretString: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param ServiceEnabled: `true`: The service is activated; `false`: The service is not activated.\n        :type ServiceEnabled: bool\n        :param InvalidType: Invalid service type. `0`: not purchased; `1`: normal; `2`: suspended due to arrears; `3`: resource released\n        :type InvalidType: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.RequestId = params.get("RequestId")


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param Versions: `VersionId` list.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Versions: list of VersionInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Offset: Starting position of the list, starting at 0. If not specified, 0 is used by default.\n        :type Offset: int\n        :param Limit: Maximum number of returned Secrets in a query. If not set or set to 0, 20 is used by default.\n        :type Limit: int\n        :param OrderType: Sorting order according to the creation time. If not set or set to 0, descending order is used; if set to 1, ascending order is used.\n        :type OrderType: int\n        :param State: Filter based on credential status.
The default value is 0, indicating to query all.
1: query the list of credentials in `Enabled` status.
2: query the list of credentials in `Disabled` status.
3: query the list of credentials in `PendingDelete` status.
4: query the list of credentials in `PendingCreate` status.
5: query the list of credentials in `CreateFailed` status.
The `PendingCreate` and `CreateFailed` status only take effect when `SecretType` is Tencent Cloud service credential\n        :type State: int\n        :param SearchSecretName: Filter according to Secret names. If left empty, this filter is not applied.\n        :type SearchSecretName: str\n        :param TagFilters: Tag filter.\n        :type TagFilters: list of TagFilter\n        :param SecretType: 0: user-defined credential (default value).
1: Tencent Cloud service credential.
Either 1 or 0 can be selected for this parameter.\n        :type SecretType: int\n        """
        self.Offset = None
        self.Limit = None
        self.OrderType = None
        self.State = None
        self.SearchSecretName = None
        self.TagFilters = None
        self.SecretType = None


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
        """
        :param TotalCount: Number of filtered Secrets according to `State` and `SearchSecretName`.\n        :type TotalCount: int\n        :param SecretMetadatas: List of Secret information.\n        :type SecretMetadatas: list of SecretMetadata\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param PrivilegeName: Permission name. Valid values:
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

When the permission is `DatabasePrivileges`, the database name must be specified by the `Database` parameter;

When the permission is `TablePrivileges`, the database name and the table name in the database must be specified by the `Database` and `TableName` parameters;

When the permission is `ColumnPrivileges`, the database name, table name in the database, and column name in the table must be specified by the `Database`, `TableName`, and `ColumnName` parameters.\n        :type PrivilegeName: str\n        :param Privileges: Permission list.
For the `Mysql` service, optional permission values are:

1. Valid values of `GlobalPrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

2. Valid values of `DatabasePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

3. Valid values of `TablePrivileges`: "SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER".
Note: if this parameter is not passed in, it means to clear the permission.

4. Valid values of `ColumnPrivileges`: "SELECT","INSERT","UPDATE","REFERENCES".
Note: if this parameter is not passed in, it means to clear the permission.\n        :type Privileges: list of str\n        :param Database: This value takes effect only when `PrivilegeName` is `DatabasePrivileges`.\n        :type Database: str\n        :param TableName: This value takes effect only when `PrivilegeName` is `TablePrivileges`, and the `Database` parameter is required in this case to explicitly indicate the database instance.\n        :type TableName: str\n        :param ColumnName: This value takes effect only when `PrivilegeName` is `ColumnPrivileges`, and the following parameters are required in this case:
Database: explicitly indicate the database instance.
TableName: explicitly indicate the table\n        :type ColumnName: str\n        """
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
        """
        :param SecretName: Name of a Secret where the version is added to.\n        :type SecretName: str\n        :param VersionId: ID of the new Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.\n        :type VersionId: str\n        :param SecretBinary: Base64-encoded binary credential information.
Either `SecretBinary` or `SecretString` must be set.\n        :type SecretBinary: str\n        :param SecretString: Secret information plaintext in text format, base64 encoding is not needed. Either `SecretBinary` or `SecretString` must be set.\n        :type SecretString: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param VersionId: Version ID that is newly added.\n        :type VersionId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SecretName: Name of the Secret to be restored.\n        :type SecretName: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class RotateProductSecretRequest(AbstractModel):
    """RotateProductSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the credential to be rotated.\n        :type SecretName: str\n        """
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
        """
        :param FlowID: Async rotation task ID.\n        :type FlowID: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowID = params.get("FlowID")
        self.RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """Basic information of the Secret.

    """

    def __init__(self):
        """
        :param SecretName: Credential name\n        :type SecretName: str\n        :param Description: Credential description\n        :type Description: str\n        :param KmsKeyId: KMS `KeyId` used to encrypt the credential\n        :type KmsKeyId: str\n        :param CreateUin: Creator UIN\n        :type CreateUin: int\n        :param Status: Credential status: Enabled, Disabled, PendingDelete, Creating, Failed.\n        :type Status: str\n        :param DeleteTime: Credential deletion date, which takes effect for credentials in `PendingDelete` status and is in UNIX timestamp format\n        :type DeleteTime: int\n        :param CreateTime: Credential creation time in UNIX timestamp format\n        :type CreateTime: int\n        :param KmsKeyType: Type of the KMS CMK used to encrypt the credential. `DEFAULT` represents the default key created by Secrets Manager, and `CUSTOMER` represents the user-specified key\n        :type KmsKeyType: str\n        :param RotationStatus: 1: enable rotation; 0: disable rotation
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RotationStatus: int\n        :param NextRotationTime: Start time of the next rotation in UNIX timestamp format
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NextRotationTime: int\n        :param SecretType: 0: user-defined credential; 1: Tencent Cloud service credential.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SecretType: int\n        :param ProductName: Tencent Cloud service name, which takes effect only when `SecretType` is 1 (Tencent Cloud service credential)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductName: str\n        """
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
    """Tag filter.

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
        


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret whose description is to be updated.\n        :type SecretName: str\n        :param Description: New description information, which can be up to 2048 bytes.\n        :type Description: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class UpdateRotationStatusRequest(AbstractModel):
    """UpdateRotationStatus request structure.

    """

    def __init__(self):
        """
        :param SecretName: Tencent Cloud service credential name.\n        :type SecretName: str\n        :param EnableRotation: Specifies whether to enable rotation.
True: enable rotation.
False: disable rotation.\n        :type EnableRotation: bool\n        :param Frequency: Rotation frequency in days. Value range: 30–365.\n        :type Frequency: int\n        :param RotationBeginTime: User-Defined rotation start time in the format of 2006-01-02 15:04:05.
When `EnableRotation` is `True`, if `RotationBeginTime` is left empty, the current time will be entered by default.\n        :type RotationBeginTime: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret whose content is to be updated.\n        :type SecretName: str\n        :param VersionId: ID of the Secret version whose content is to be updated.\n        :type VersionId: str\n        :param SecretBinary: This field should be used and Base64-encoded if the content of the new credential is binary.
Either `SecretBinary` or `SecretString` cannot be empty.\n        :type SecretBinary: str\n        :param SecretString: This field should be used without being Base64-encoded if the content of the new credential is text. Either `SecretBinary` or `SecretString` cannot be empty.\n        :type SecretString: str\n        """
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
        """
        :param SecretName: Name of the Secret.\n        :type SecretName: str\n        :param VersionId: Version ID of the Secret.\n        :type VersionId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param VersionId: Version ID.\n        :type VersionId: str\n        :param CreateTime: Creation time, formatted as a Unix timestamp.\n        :type CreateTime: int\n        """
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
        