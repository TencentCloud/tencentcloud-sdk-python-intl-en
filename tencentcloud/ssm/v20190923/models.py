# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class CreateSecretRequest(AbstractModel):
    """CreateSecret request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret to be deleted.
        :type SecretName: str
        :param RecoveryWindowInDays: Scheduled deletion time, in days. If set to 0, the Secret is deleted immediately. A number in the range of 1 to 30 indicates the number of retention days. The Secret will be deleted after the set value.
        :type RecoveryWindowInDays: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret response structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param Description: Description of the Secret.
        :type Description: str
        :param KmsKeyId: ID of the KMS CMK used for encryption.
        :type KmsKeyId: str
        :param CreateUin: Creator UIN.
        :type CreateUin: int
        :param Status: Secret status, which can be `Enabled`, `Disabled`, or `PendingDelete`.
        :type Status: str
        :param DeleteTime: Deletion time, formatted as a Unix timestamp. For a Secret that is not in `PendingDelete` status, this value is 0.
        :type DeleteTime: int
        :param CreateTime: Creation time.
        :type CreateTime: int
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
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableSecretRequest(AbstractModel):
    """DisableSecret request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableSecretResponse(AbstractModel):
    """DisableSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableSecretRequest(AbstractModel):
    """EnableSecret request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableSecretResponse(AbstractModel):
    """EnableSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetRegionsRequest(AbstractModel):
    """GetRegions request structure.

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret.
        :type SecretName: str
        :param VersionId: ID of the Secret version.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue response structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param VersionId: ID of the Secret version.
        :type VersionId: str
        :param SecretBinary: If the `SecretBinary` field in the request body is specified in the `CreateSecret` call, this field is returned and base64-encoded. The caller needs to perform base64 decoding to obtain the original data. Either `SecretBinary` or `SecretString` will be returned.
        :type SecretBinary: str
        :param SecretString: If the `SecretString` field in the request body is specified in the `CreateSecret` call, this field is returned. Either `SecretBinary` or `SecretString` will be returned.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus request structure.

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus response structure.

    """

    def __init__(self):
        """
        :param ServiceEnabled: `true`: The service is activated; `false`: The service is not activated.
        :type ServiceEnabled: bool
        :param InvalidType: Invalid service type. `0`: not purchased; `1`: normal; `2`: suspended due to arrears; `3`: resource released
        :type InvalidType: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListSecretsRequest(AbstractModel):
    """ListSecrets request structure.

    """

    def __init__(self):
        """
        :param Offset: Starting position of the list, starting at 0. If not specified, 0 is used by default.
        :type Offset: int
        :param Limit: Maximum number of returned Secrets in a query. If not set or set to 0, 20 is used by default.
        :type Limit: int
        :param OrderType: Sorting order according to the creation time. If not set or set to 0, descending order is used; if set to 1, ascending order is used.
        :type OrderType: int
        :param State: Filter according to Secret statuses. `0` (default): all Secrets; `1`: Secrets in `Enabled` status; `2`: Secrets in `Disabled` status; `3`: Secrets in `PendingDelete` status.
        :type State: int
        :param SearchSecretName: Filter according to Secret names. If left empty, this filter is not applied.
        :type SearchSecretName: str
        :param TagFilters: Tag filter condition.
        :type TagFilters: list of TagFilter
        """
        self.Offset = None
        self.Limit = None
        self.OrderType = None
        self.State = None
        self.SearchSecretName = None
        self.TagFilters = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListSecretsResponse(AbstractModel):
    """ListSecrets response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret where the version is added to.
        :type SecretName: str
        :param VersionId: ID of the new Secret version. It can be up to 64 bytes, contain letters, digits, hyphens (-), and underscores (_), and must begin with a letter or digit.
        :type VersionId: str
        :param SecretBinary: Binary Secret information that is base64-encoded. Either `SecretBinary` or `SecretString` must be set.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SecretMetadata(AbstractModel):
    """Basic information of the Secret.

    """

    def __init__(self):
        """
        :param SecretName: Name of the Secret.
        :type SecretName: str
        :param Description: Description of the Secret.
        :type Description: str
        :param KmsKeyId: KMS Key ID used for Secret encryption.
        :type KmsKeyId: str
        :param CreateUin: Creator UIN.
        :type CreateUin: int
        :param Status: Secret status, which can be `Enabled`, `Disabled`, or `PendingDelete`.
        :type Status: str
        :param DeleteTime: Secret deletion time, formatted as a Unix timestamp. This parameter is only applicable for Secrets in `PendingDelete` status.
        :type DeleteTime: int
        :param CreateTime: Secret creation time, formatted as a Unix timestamp.
        :type CreateTime: int
        :param KmsKeyType: Type of KMS CMK used for Secret encryption. `DEFAULT`: default key created by SecretsManager; `CUSTOMER`: user-specified key.
        :type KmsKeyType: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.KmsKeyType = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.KmsKeyType = params.get("KmsKeyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """Tag key and tag value.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagFilter(AbstractModel):
    """Tag filter.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret request structure.

    """

    def __init__(self):
        """
        :param SecretName: Name of a Secret whose content is to be updated.
        :type SecretName: str
        :param VersionId: ID of the Secret version whose content is to be updated.
        :type VersionId: str
        :param SecretBinary: Use this field if the new Secret content is in binary format, and base64-encoded. Either `SecretBinary` or `SecretString` is set.
        :type SecretBinary: str
        :param SecretString: Use this field if the new Secret content is in text format, and base64-encoding is not required. Either `SecretBinary` or `SecretString` is set.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VersionInfo(AbstractModel):
    """List of version ID information.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        