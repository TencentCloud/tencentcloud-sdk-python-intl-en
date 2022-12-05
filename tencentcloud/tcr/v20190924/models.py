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


class AccessVpc(AbstractModel):
    """Private network access information

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param Status: Private network access status
        :type Status: str
        :param AccessIp: Private network access IP
        :type AccessIp: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.AccessIp = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.AccessIp = params.get("AccessIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameRequest(AbstractModel):
    """CheckInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param RegistryName: Name of the instance to be created
        :type RegistryName: str
        """
        self.RegistryName = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameResponse(AbstractModel):
    """CheckInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param IsValidated: Verification result. Valid values: true: Valid; false: Invalid.
        :type IsValidated: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsValidated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RequestId = params.get("RequestId")


class CheckInstanceRequest(AbstractModel):
    """CheckInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: ID of the instance to be verified.
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceResponse(AbstractModel):
    """CheckInstance response structure.

    """

    def __init__(self):
        r"""
        :param IsValidated: Verification result. true: valid, false: invalid
        :type IsValidated: bool
        :param RegionId: ID of the region where the instance is located.
        :type RegionId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsValidated = None
        self.RegionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RegionId = params.get("RegionId")
        self.RequestId = params.get("RequestId")


class CreateImageAccelerationServiceRequest(AbstractModel):
    """CreateImageAccelerationService request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param VpcId: ID of the VPC where the CFS file system to be created resides
        :type VpcId: str
        :param SubnetId: ID of the subnet where the CFS file system to be created resides
        :type SubnetId: str
        :param StorageType: Storage class of the CFS file system to be created. Valid values: SD: Standard; HP: High-Performance.
        :type StorageType: str
        :param PGroupId: Permission group ID
        :type PGroupId: str
        :param Zone: AZ name, such as `ap-beijing-1`. For more information, see the list of regions and AZs in Overview.
        :type Zone: str
        :param TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self.RegistryId = None
        self.VpcId = None
        self.SubnetId = None
        self.StorageType = None
        self.PGroupId = None
        self.Zone = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StorageType = params.get("StorageType")
        self.PGroupId = params.get("PGroupId")
        self.Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageAccelerationServiceResponse(AbstractModel):
    """CreateImageAccelerationService response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImmutableTagRulesResponse(AbstractModel):
    """CreateImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceCustomizedDomainRequest(AbstractModel):
    """CreateInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param DomainName: Custom domain name
        :type DomainName: str
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.RegistryId = None
        self.DomainName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DomainName = params.get("DomainName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceCustomizedDomainResponse(AbstractModel):
    """CreateInstanceCustomizedDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryName: Enterprise Edition instance name
        :type RegistryName: str
        :param RegistryType: Enterprise Edition instance type. Valid values: basic: Basic; standard: Standard; premium: Premium.
        :type RegistryType: str
        :param TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param RegistryChargeType: Instance billing mode. Valid values: 0: Pay-as-you-go billing; 1: Prepaid. Default value: 0.
        :type RegistryChargeType: int
        :param SyncTag: Whether to sync TCR cloud tags to the COS bucket
        :type SyncTag: bool
        """
        self.RegistryName = None
        self.RegistryType = None
        self.TagSpecification = None
        self.RegistryChargeType = None
        self.SyncTag = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.RegistryChargeType = params.get("RegistryChargeType")
        self.SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Enterprise Edition instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param TokenType: Access credential type. Values: `longterm` and `temp` (default, valid for one hour)
        :type TokenType: str
        :param Desc: Description of the long-term access credential
        :type Desc: str
        """
        self.RegistryId = None
        self.TokenType = None
        self.Desc = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenType = params.get("TokenType")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param Username: Username
Note: this field may return `null`, indicating that no valid value can be found.
        :type Username: str
        :param Token: Access credential
        :type Token: str
        :param ExpTime: Expiration timestamp of access credential. It is a string of numbers without unit.
        :type ExpTime: int
        :param TokenId: Token ID of long-term access credential. It is not available to temporary access credential.
Note: this field may return `null`, indicating that no valid value can be found.
        :type TokenId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Username = None
        self.Token = None
        self.ExpTime = None
        self.TokenId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Token = params.get("Token")
        self.ExpTime = params.get("ExpTime")
        self.TokenId = params.get("TokenId")
        self.RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultipleSecurityPolicyResponse(AbstractModel):
    """CreateMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name, which can contain 2–30 lowercase letters, digits, and separators (".", "_", and "-") but can neither start or end with a separator nor contain consecutive separators.
        :type NamespaceName: str
        :param IsPublic: Whether to make public. Valid values: true: Yes; false: No.
        :type IsPublic: bool
        :param TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        :param SyncTag: Whether to sync TCR cloud tags to the COS Bucket
        :type SyncTag: bool
        """
        self.RegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None
        self.SyncTag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        self.SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationInstanceResponse(AbstractModel):
    """CreateReplicationInstance response structure.

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: Enterprise Registry Instance ID
        :type ReplicationRegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReplicationRegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Repository name
        :type RepositoryName: str
        :param BriefDescription: Brief repository description
        :type BriefDescription: str
        :param Description: Detailed repository description
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityPoliciesRequest(AbstractModel):
    """CreateSecurityPolicies request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param CidrBlock: 192.168.0.0/24
        :type CidrBlock: str
        :param Description: Description
        :type Description: str
        """
        self.RegistryId = None
        self.CidrBlock = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.CidrBlock = params.get("CidrBlock")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPoliciesResponse(AbstractModel):
    """CreateSecurityPolicies response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param CidrBlock: 192.168.0.0/24
        :type CidrBlock: str
        :param Description: Remarks
        :type Description: str
        """
        self.RegistryId = None
        self.CidrBlock = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.CidrBlock = params.get("CidrBlock")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateSignaturePolicyRequest(AbstractModel):
    """CreateSignaturePolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Name: Policy name
        :type Name: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param KmsId: KMS key
        :type KmsId: str
        :param KmsRegion: Region of the KMS key
        :type KmsRegion: str
        :param Domain: Custom domain name. If this parameter is left empty, the default domain name of the TCR instance will be used to generate the signature.
        :type Domain: str
        :param Disabled: Whether to disable the signing policy. Default value: false.
        :type Disabled: bool
        """
        self.RegistryId = None
        self.Name = None
        self.NamespaceName = None
        self.KmsId = None
        self.KmsRegion = None
        self.Domain = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Name = params.get("Name")
        self.NamespaceName = params.get("NamespaceName")
        self.KmsId = params.get("KmsId")
        self.KmsRegion = params.get("KmsRegion")
        self.Domain = params.get("Domain")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignaturePolicyResponse(AbstractModel):
    """CreateSignaturePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSignatureRequest(AbstractModel):
    """CreateSignature request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Repository name
        :type RepositoryName: str
        :param ImageVersion: Tag name
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignatureResponse(AbstractModel):
    """CreateSignature response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRetentionExecutionRequest(AbstractModel):
    """CreateTagRetentionExecution request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param RetentionId: Tag retention rule ID
        :type RetentionId: int
        :param DryRun: Whether the execution is simulated. Default value: false (not simulated)
        :type DryRun: bool
        """
        self.RegistryId = None
        self.RetentionId = None
        self.DryRun = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionExecutionResponse(AbstractModel):
    """CreateTagRetentionExecution response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRetentionRuleRequest(AbstractModel):
    """CreateTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param NamespaceId: Namespace ID
        :type NamespaceId: int
        :param RetentionRule: Retention policy
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param CronSetting: Execution cycle. Valid values: manual, daily, weekly, monthly.
        :type CronSetting: str
        :param Disabled: Whether to disable the rule. Default value: false.
        :type Disabled: bool
        """
        self.RegistryId = None
        self.NamespaceId = None
        self.RetentionRule = None
        self.CronSetting = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self.RetentionRule = RetentionRule()
            self.RetentionRule._deserialize(params.get("RetentionRule"))
        self.CronSetting = params.get("CronSetting")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionRuleResponse(AbstractModel):
    """CreateTagRetentionRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Trigger: Trigger parameter
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: Namespace
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param Trigger: Newly created trigger
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Trigger = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.RequestId = params.get("RequestId")


class CustomizedDomainInfo(AbstractModel):
    """Custom domain name information

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param CertId: Certificate ID
        :type CertId: str
        :param DomainName: Domain name
        :type DomainName: str
        :param Status: Domain name creation status. Valid values: SUCCESS, FAILURE, CREATING, DELETING.
        :type Status: str
        """
        self.RegistryId = None
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageAccelerateServiceRequest(AbstractModel):
    """DeleteImageAccelerateService request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageAccelerateServiceResponse(AbstractModel):
    """DeleteImageAccelerateService response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RepositoryName: Image repository name
        :type RepositoryName: str
        :param ImageVersion: Image tag
        :type ImageVersion: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param RuleId: Rule ID
        :type RuleId: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImmutableTagRulesResponse(AbstractModel):
    """DeleteImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceCustomizedDomainRequest(AbstractModel):
    """DeleteInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param DomainName: Custom domain name
        :type DomainName: str
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.RegistryId = None
        self.DomainName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DomainName = params.get("DomainName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceCustomizedDomainResponse(AbstractModel):
    """DeleteInstanceCustomizedDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param DeleteBucket: Whether to delete the bucket. Default value: false.
        :type DeleteBucket: bool
        :param DryRun: Whether to enable the `dryRun` mode. Default value: false.
        :type DryRun: bool
        """
        self.RegistryId = None
        self.DeleteBucket = None
        self.DryRun = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DeleteBucket = params.get("DeleteBucket")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param TokenId: Access credential ID
        :type TokenId: str
        """
        self.RegistryId = None
        self.TokenId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenId = params.get("TokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultipleSecurityPolicyResponse(AbstractModel):
    """DeleteMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReplicationInstanceRequest(AbstractModel):
    """DeleteReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param ReplicationRegistryId: Replica instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replica instance
        :type ReplicationRegionId: int
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReplicationInstanceResponse(AbstractModel):
    """DeleteReplicationInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Image repository name
        :type RepositoryName: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryTagsRequest(AbstractModel):
    """DeleteRepositoryTags request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Repository name
        :type RepositoryName: str
        :param Tags: List of tags. Up to 20 tags can be returned for a request.
        :type Tags: list of str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Tags = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryTagsResponse(AbstractModel):
    """DeleteRepositoryTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param PolicyIndex: Allowlist ID
        :type PolicyIndex: int
        :param PolicyVersion: Allowlist version
        :type PolicyVersion: str
        """
        self.RegistryId = None
        self.PolicyIndex = None
        self.PolicyVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.PolicyIndex = params.get("PolicyIndex")
        self.PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteSignaturePolicyRequest(AbstractModel):
    """DeleteSignaturePolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSignaturePolicyResponse(AbstractModel):
    """DeleteSignaturePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRetentionRuleRequest(AbstractModel):
    """DeleteTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param RetentionId: Tag retention rule ID
        :type RetentionId: int
        """
        self.RegistryId = None
        self.RetentionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagRetentionRuleResponse(AbstractModel):
    """DeleteTagRetentionRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Namespace: Namespace
        :type Namespace: str
        :param Id: Trigger ID
        :type Id: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeChartDownloadInfoRequest(AbstractModel):
    """DescribeChartDownloadInfo request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param ChartName: Chart name
        :type ChartName: str
        :param ChartVersion: Chart version
        :type ChartVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.ChartName = None
        self.ChartVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.ChartName = params.get("ChartName")
        self.ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChartDownloadInfoResponse(AbstractModel):
    """DescribeChartDownloadInfo response structure.

    """

    def __init__(self):
        r"""
        :param PreSignedDownloadURL: Presigned URL for download
        :type PreSignedDownloadURL: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PreSignedDownloadURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedDownloadURL = params.get("PreSignedDownloadURL")
        self.RequestId = params.get("RequestId")


class DescribeExternalEndpointStatusRequest(AbstractModel):
    """DescribeExternalEndpointStatus request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalEndpointStatusResponse(AbstractModel):
    """DescribeExternalEndpointStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Public network access status. Valid values: Opening, Opened, Closed.
        :type Status: str
        :param Reason: Reason
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Reason = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.RequestId = params.get("RequestId")


class DescribeGCJobsRequest(AbstractModel):
    """DescribeGCJobs request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGCJobsResponse(AbstractModel):
    """DescribeGCJobs response structure.

    """

    def __init__(self):
        r"""
        :param Jobs: List of GC jobs
        :type Jobs: list of GCJobInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Jobs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = GCJobInfo()
                obj._deserialize(item)
                self.Jobs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageAccelerateServiceRequest(AbstractModel):
    """DescribeImageAccelerateService request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAccelerateServiceResponse(AbstractModel):
    """DescribeImageAccelerateService response structure.

    """

    def __init__(self):
        r"""
        :param Status: Image acceleration status
        :type Status: str
        :param CFSVIP: CFS VIP
        :type CFSVIP: str
        :param IsEnable: Whether to enable
        :type IsEnable: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.CFSVIP = None
        self.IsEnable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.CFSVIP = params.get("CFSVIP")
        self.IsEnable = params.get("IsEnable")
        self.RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Image repository name
        :type RepositoryName: str
        :param ImageVersion: Image tag
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests response structure.

    """

    def __init__(self):
        r"""
        :param Manifest: Image manifest information
        :type Manifest: str
        :param Config: Image configuration information
        :type Config: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Manifest = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Manifest = params.get("Manifest")
        self.Config = params.get("Config")
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Image repository name
        :type RepositoryName: str
        :param ImageVersion: Image tag specified for fuzzy search
        :type ImageVersion: str
        :param Limit: Number of entries per page, which is used for pagination. Default value: 20.
        :type Limit: int
        :param Offset: Page number. Default value: 1.
        :type Offset: int
        :param Digest: Image digest specified for search
        :type Digest: str
        :param ExactMatch: Whether to use exact matching. Valid values: `true` (exact matching), `null` (fuzzy matching).
        :type ExactMatch: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.Limit = None
        self.Offset = None
        self.Digest = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Digest = params.get("Digest")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        r"""
        :param ImageInfoList: List of container images
        :type ImageInfoList: list of TcrImageInfo
        :param TotalCount: Total number of container images
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImmutableTagRulesResponse(AbstractModel):
    """DescribeImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Rule list
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Rules: list of ImmutableTagRule
        :param EmptyNs: Namespace with no rules created
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type EmptyNs: list of str
        :param Total: Total rules
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.EmptyNs = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ImmutableTagRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.EmptyNs = params.get("EmptyNs")
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeInstanceAllNamespacesRequest(AbstractModel):
    """DescribeInstanceAllNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Start position offset
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllNamespacesResponse(AbstractModel):
    """DescribeInstanceAllNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceAllRequest(AbstractModel):
    """DescribeInstanceAll request structure.

    """

    def __init__(self):
        r"""
        :param Registryids: List of instance IDs (if it is empty,
it indicates to get all instances under the current account)
        :type Registryids: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Filters: Filters
        :type Filters: list of Filter
        :param AllRegion: Whether to get the instances in all regions. Default value: False.
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllResponse(AbstractModel):
    """DescribeInstanceAll response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instances
        :type TotalCount: int
        :param Registries: List of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type Registries: list of Registry
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceCustomizedDomainRequest(AbstractModel):
    """DescribeInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param Limit: Pagination limit
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceCustomizedDomainResponse(AbstractModel):
    """DescribeInstanceCustomizedDomain response structure.

    """

    def __init__(self):
        r"""
        :param DomainInfoList: List of domain names
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainInfoList: list of CustomizedDomainInfo
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfoList") is not None:
            self.DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = CustomizedDomainInfo()
                obj._deserialize(item)
                self.DomainInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus request structure.

    """

    def __init__(self):
        r"""
        :param RegistryIds: Array of instance IDs
        :type RegistryIds: list of str
        """
        self.RegistryIds = None


    def _deserialize(self, params):
        self.RegistryIds = params.get("RegistryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus response structure.

    """

    def __init__(self):
        r"""
        :param RegistryStatusSet: List of instance statuses
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistryStatusSet: list of RegistryStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self.RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self.RegistryStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of long-term access credentials
        :type TotalCount: int
        :param Tokens: List of long-term access credentials
        :type Tokens: list of TcrInstanceToken
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tokens = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self.Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self.Tokens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param Registryids: List of instance IDs (if it is empty,
it indicates to get all instances under the current account)
        :type Registryids: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Filters: Filters
        :type Filters: list of Filter
        :param AllRegion: Whether to get the instances in all regions. Default value: False.
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instances
        :type TotalCount: int
        :param Registries: List of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type Registries: list of Registry
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternalEndpointsRequest(AbstractModel):
    """DescribeInternalEndpoints request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointsResponse(AbstractModel):
    """DescribeInternalEndpoints response structure.

    """

    def __init__(self):
        r"""
        :param AccessVpcSet: List of private network access addresses
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessVpcSet: list of AccessVpc
        :param TotalCount: Total number of private network access addresses
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessVpcSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessVpcSet") is not None:
            self.AccessVpcSet = []
            for item in params.get("AccessVpcSet"):
                obj = AccessVpc()
                obj._deserialize(item)
                self.AccessVpcSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Specified namespace. If this parameter is left empty, all namespaces will be queried.
        :type NamespaceName: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Page offset (page number from which to return the results)
        :type Offset: int
        :param All: Whether to list all namespaces
        :type All: bool
        :param Filters: Filters
        :type Filters: list of Filter
        :param KmsSignPolicy: Whether to query only namespaces for which the KMS image signature is enabled
        :type KmsSignPolicy: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None
        self.All = None
        self.Filters = None
        self.KmsSignPolicy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.All = params.get("All")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.KmsSignPolicy = params.get("KmsSignPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param NamespaceList: List of namespaces
        :type NamespaceList: list of TcrNamespaceInfo
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NamespaceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NamespaceList") is not None:
            self.NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self.NamespaceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of returned results
        :type TotalCount: int
        :param Regions: List of regions
        :type Regions: list of Region
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Regions") is not None:
            self.Regions = []
            for item in params.get("Regions"):
                obj = Region()
                obj._deserialize(item)
                self.Regions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks request structure.

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        """
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceCreateTasksResponse(AbstractModel):
    """DescribeReplicationInstanceCreateTasks response structure.

    """

    def __init__(self):
        r"""
        :param TaskDetail: Task details
        :type TaskDetail: list of TaskDetail
        :param Status: Overall task status
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskDetail = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskDetail") is not None:
            self.TaskDetail = []
            for item in params.get("TaskDetail"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.TaskDetail.append(obj)
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceSyncStatusRequest(AbstractModel):
    """DescribeReplicationInstanceSyncStatus request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ShowReplicationLog: Whether to show the synchronization log
        :type ShowReplicationLog: bool
        :param Offset: Page offset for log display. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 5, maximum value: 20.
        :type Limit: int
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ShowReplicationLog = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ShowReplicationLog = params.get("ShowReplicationLog")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus response structure.

    """

    def __init__(self):
        r"""
        :param ReplicationStatus: Synchronization status
        :type ReplicationStatus: str
        :param ReplicationTime: Synchronization completion time
        :type ReplicationTime: str
        :param ReplicationLog: Synchronization log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationLog: :class:`tencentcloud.tcr.v20190924.models.ReplicationLog`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReplicationStatus = None
        self.ReplicationTime = None
        self.ReplicationLog = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationStatus = params.get("ReplicationStatus")
        self.ReplicationTime = params.get("ReplicationTime")
        if params.get("ReplicationLog") is not None:
            self.ReplicationLog = ReplicationLog()
            self.ReplicationLog._deserialize(params.get("ReplicationLog"))
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20, maximum value: 100.
        :type Limit: int
        """
        self.RegistryId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstancesResponse(AbstractModel):
    """DescribeReplicationInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instances
        :type TotalCount: int
        :param ReplicationRegistries: Replication instance list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationRegistries: list of ReplicationRegistry
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReplicationRegistries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReplicationRegistries") is not None:
            self.ReplicationRegistries = []
            for item in params.get("ReplicationRegistries"):
                obj = ReplicationRegistry()
                obj._deserialize(item)
                self.ReplicationRegistries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Specified namespace. If this parameter is left empty, image repositories in all namespaces will be queried.
        :type NamespaceName: str
        :param RepositoryName: Specified image repository. If this parameter is left empty, all image repositories in the specified namespace will be queried.
        :type RepositoryName: str
        :param Offset: Page number, which is used for pagination
        :type Offset: int
        :param Limit: Number of entries per page, which is used for pagination
        :type Limit: int
        :param SortBy: Sort field. Valid values: -creation_time, -name, -update_time.
        :type SortBy: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories response structure.

    """

    def __init__(self):
        r"""
        :param RepositoryList: Repository information list
        :type RepositoryList: list of TcrRepositoryInfo
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RepositoryList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RepositoryList") is not None:
            self.RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self.RepositoryList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    """DescribeSecurityPolicies request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    """DescribeSecurityPolicies response structure.

    """

    def __init__(self):
        r"""
        :param SecurityPolicySet: Instance security policy group
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityPolicySet: list of SecurityPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecurityPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityPolicySet") is not None:
            self.SecurityPolicySet = []
            for item in params.get("SecurityPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionRequest(AbstractModel):
    """DescribeTagRetentionExecution request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param RetentionId: Rule ID
        :type RetentionId: int
        :param Limit: `PageSize` for pagination
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        """
        self.RegistryId = None
        self.RetentionId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionResponse(AbstractModel):
    """DescribeTagRetentionExecution response structure.

    """

    def __init__(self):
        r"""
        :param RetentionExecutionList: List of tag retention execution records
        :type RetentionExecutionList: list of RetentionExecution
        :param TotalCount: Total number of tag retention execution records
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RetentionExecutionList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionExecutionList") is not None:
            self.RetentionExecutionList = []
            for item in params.get("RetentionExecutionList"):
                obj = RetentionExecution()
                obj._deserialize(item)
                self.RetentionExecutionList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionTaskRequest(AbstractModel):
    """DescribeTagRetentionExecutionTask request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param RetentionId: Rule ID
        :type RetentionId: int
        :param ExecutionId: Rule execution ID
        :type ExecutionId: int
        :param Offset: Page offset
        :type Offset: int
        :param Limit: `PageSize` for pagination
        :type Limit: int
        """
        self.RegistryId = None
        self.RetentionId = None
        self.ExecutionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.ExecutionId = params.get("ExecutionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionTaskResponse(AbstractModel):
    """DescribeTagRetentionExecutionTask response structure.

    """

    def __init__(self):
        r"""
        :param RetentionTaskList: List of tag retention execution tasks
        :type RetentionTaskList: list of RetentionTask
        :param TotalCount: Total number of tag retention execution tasks
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RetentionTaskList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionTaskList") is not None:
            self.RetentionTaskList = []
            for item in params.get("RetentionTaskList"):
                obj = RetentionTask()
                obj._deserialize(item)
                self.RetentionTaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionRulesRequest(AbstractModel):
    """DescribeTagRetentionRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param Limit: `PageSize` for pagination
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionRulesResponse(AbstractModel):
    """DescribeTagRetentionRules response structure.

    """

    def __init__(self):
        r"""
        :param RetentionPolicyList: List of tag retention policies
        :type RetentionPolicyList: list of RetentionPolicy
        :param TotalCount: Total number of tag retention policies
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RetentionPolicyList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionPolicyList") is not None:
            self.RetentionPolicyList = []
            for item in params.get("RetentionPolicyList"):
                obj = RetentionPolicy()
                obj._deserialize(item)
                self.RetentionPolicyList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Namespace: Namespace
        :type Namespace: str
        :param Id: Trigger ID
        :type Id: int
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Logs: List of logs
        :type Logs: list of WebhookTriggerLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        :param Namespace: Namespace
        :type Namespace: str
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of triggers
        :type TotalCount: int
        :param Triggers: List of triggers
        :type Triggers: list of WebhookTrigger
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadHelmChartRequest(AbstractModel):
    """DownloadHelmChart request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param ChartName: Helm chart name
        :type ChartName: str
        :param ChartVersion: Helm chart version
        :type ChartVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.ChartName = None
        self.ChartVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.ChartName = params.get("ChartName")
        self.ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadHelmChartResponse(AbstractModel):
    """DownloadHelmChart response structure.

    """

    def __init__(self):
        r"""
        :param TmpToken: Temporary token
        :type TmpToken: str
        :param TmpSecretId: Temporary `secretId`
        :type TmpSecretId: str
        :param TmpSecretKey: Temporary `secretKey`
        :type TmpSecretKey: str
        :param Bucket: Bucket information
        :type Bucket: str
        :param Region: Instance ID
        :type Region: str
        :param Path: Chart information
        :type Path: str
        :param StartTime: Start timestamp
        :type StartTime: int
        :param ExpiredTime: Token expiration timestamp
        :type ExpiredTime: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TmpToken = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TmpToken = params.get("TmpToken")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param Name: Attribute name. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Name: str
        :param Values: Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GCJobInfo(AbstractModel):
    """GC execution information

    """

    def __init__(self):
        r"""
        :param ID: Job ID
        :type ID: int
        :param JobStatus: Job status
        :type JobStatus: str
        :param CreationTime: Creation time
        :type CreationTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Schedule: Scheduling information
        :type Schedule: :class:`tencentcloud.tcr.v20190924.models.Schedule`
        """
        self.ID = None
        self.JobStatus = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Schedule = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.JobStatus = params.get("JobStatus")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Schedule") is not None:
            self.Schedule = Schedule()
            self.Schedule._deserialize(params.get("Schedule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        r"""
        :param Key: Header Key
        :type Key: str
        :param Values: Header Values
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImmutableTagRule(AbstractModel):
    """Tag immutability rule

    """

    def __init__(self):
        r"""
        :param RepositoryPattern: Repository matching rule
        :type RepositoryPattern: str
        :param TagPattern: Tag matching rule
        :type TagPattern: str
        :param RepositoryDecoration: repoMatches or repoExcludes
        :type RepositoryDecoration: str
        :param TagDecoration: matches or excludes
        :type TagDecoration: str
        :param Disabled: Disabling rule
        :type Disabled: bool
        :param RuleId: Rule ID
        :type RuleId: int
        :param NsName: Namespace
        :type NsName: str
        """
        self.RepositoryPattern = None
        self.TagPattern = None
        self.RepositoryDecoration = None
        self.TagDecoration = None
        self.Disabled = None
        self.RuleId = None
        self.NsName = None


    def _deserialize(self, params):
        self.RepositoryPattern = params.get("RepositoryPattern")
        self.TagPattern = params.get("TagPattern")
        self.RepositoryDecoration = params.get("RepositoryDecoration")
        self.TagDecoration = params.get("TagDecoration")
        self.Disabled = params.get("Disabled")
        self.RuleId = params.get("RuleId")
        self.NsName = params.get("NsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueString(AbstractModel):
    """String key-value pair of a common parameter

    """

    def __init__(self):
        r"""
        :param Key: Key
        :type Key: str
        :param Value: Value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointRequest(AbstractModel):
    """ManageExternalEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Operation: Operation. Valid values: Create, Delete.
        :type Operation: str
        """
        self.RegistryId = None
        self.Operation = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointResponse(AbstractModel):
    """ManageExternalEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageInternalEndpointRequest(AbstractModel):
    """ManageInternalEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Operation: Create/Delete
        :type Operation: str
        :param VpcId: ID of the VPC to be connected to
        :type VpcId: str
        :param SubnetId: ID of the subnet to be connected to
        :type SubnetId: str
        :param RegionId: ID of the requested region, which is used as the region of the replica instance
        :type RegionId: int
        :param RegionName: Name of the requested region, which is used as the region of the replica instance
        :type RegionName: str
        """
        self.RegistryId = None
        self.Operation = None
        self.VpcId = None
        self.SubnetId = None
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Operation = params.get("Operation")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageInternalEndpointResponse(AbstractModel):
    """ManageInternalEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageReplicationRequest(AbstractModel):
    """ManageReplication request structure.

    """

    def __init__(self):
        r"""
        :param SourceRegistryId: Source instance ID
        :type SourceRegistryId: str
        :param DestinationRegistryId: Destination instance ID
        :type DestinationRegistryId: str
        :param Rule: Synchronization rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`
        :param Description: Rule description
        :type Description: str
        :param DestinationRegionId: Region ID of the destination instance. For example, `1` represents Guangzhou
        :type DestinationRegionId: int
        :param PeerReplicationOption: Configuration of the synchronization rule
        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`
        """
        self.SourceRegistryId = None
        self.DestinationRegistryId = None
        self.Rule = None
        self.Description = None
        self.DestinationRegionId = None
        self.PeerReplicationOption = None


    def _deserialize(self, params):
        self.SourceRegistryId = params.get("SourceRegistryId")
        self.DestinationRegistryId = params.get("DestinationRegistryId")
        if params.get("Rule") is not None:
            self.Rule = ReplicationRule()
            self.Rule._deserialize(params.get("Rule"))
        self.Description = params.get("Description")
        self.DestinationRegionId = params.get("DestinationRegionId")
        if params.get("PeerReplicationOption") is not None:
            self.PeerReplicationOption = PeerReplicationOption()
            self.PeerReplicationOption._deserialize(params.get("PeerReplicationOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationResponse(AbstractModel):
    """ManageReplication response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace
        :type NamespaceName: str
        :param RuleId: Rule ID
        :type RuleId: int
        :param Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImmutableTagRulesResponse(AbstractModel):
    """ModifyImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RegistryType: Instance specification
        :type RegistryType: str
        """
        self.RegistryId = None
        self.RegistryType = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryType = params.get("RegistryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param TokenId: ID of the long-term access credential of the instance
        :type TokenId: str
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Enable: Whether to enable the long-term access credential of the instance
        :type Enable: bool
        :param Desc: Access credential description
        :type Desc: str
        :param ModifyFlag: Valid values: 1: Modify the description; 2: Enable/Disable. Default value: 2.
        :type ModifyFlag: int
        """
        self.TokenId = None
        self.RegistryId = None
        self.Enable = None
        self.Desc = None
        self.ModifyFlag = None


    def _deserialize(self, params):
        self.TokenId = params.get("TokenId")
        self.RegistryId = params.get("RegistryId")
        self.Enable = params.get("Enable")
        self.Desc = params.get("Desc")
        self.ModifyFlag = params.get("ModifyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param IsPublic: Access level. Valid values: True: Public; False: Private.
        :type IsPublic: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RepositoryName: Image repository name
        :type RepositoryName: str
        :param BriefDescription: Brief repository description
        :type BriefDescription: str
        :param Description: Detailed repository description
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param PolicyIndex: PolicyId
        :type PolicyIndex: int
        :param CidrBlock: Allowed IP, such as `192.168.0.0/24`
        :type CidrBlock: str
        :param Description: Remarks
        :type Description: str
        """
        self.RegistryId = None
        self.PolicyIndex = None
        self.CidrBlock = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.PolicyIndex = params.get("PolicyIndex")
        self.CidrBlock = params.get("CidrBlock")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ModifyTagRetentionRuleRequest(AbstractModel):
    """ModifyTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Primary instance ID
        :type RegistryId: str
        :param NamespaceId: ID of the original namespace
        :type NamespaceId: int
        :param RetentionRule: Retention policy
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param CronSetting: Original execution cycle
        :type CronSetting: str
        :param RetentionId: Rule ID
        :type RetentionId: int
        :param Disabled: Whether to disable the rule
        :type Disabled: bool
        """
        self.RegistryId = None
        self.NamespaceId = None
        self.RetentionRule = None
        self.CronSetting = None
        self.RetentionId = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self.RetentionRule = RetentionRule()
            self.RetentionRule._deserialize(params.get("RetentionRule"))
        self.CronSetting = params.get("CronSetting")
        self.RetentionId = params.get("RetentionId")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagRetentionRuleResponse(AbstractModel):
    """ModifyTagRetentionRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Trigger: Trigger parameter
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: Namespace
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PeerReplicationOption(AbstractModel):
    """Parameters for cross-account synchronization

    """

    def __init__(self):
        r"""
        :param PeerRegistryUin: UIN of the destination instance
        :type PeerRegistryUin: str
        :param PeerRegistryToken: Permanent access Token for the destination instance
        :type PeerRegistryToken: str
        :param EnablePeerReplication: Whether to enable cross-account synchronization
        :type EnablePeerReplication: bool
        """
        self.PeerRegistryUin = None
        self.PeerRegistryToken = None
        self.EnablePeerReplication = None


    def _deserialize(self, params):
        self.PeerRegistryUin = params.get("PeerRegistryUin")
        self.PeerRegistryToken = params.get("PeerRegistryToken")
        self.EnablePeerReplication = params.get("EnablePeerReplication")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param Alias: gz
        :type Alias: str
        :param RegionId: 1
        :type RegionId: int
        :param RegionName: ap-guangzhou
        :type RegionName: str
        :param Status: alluser
        :type Status: str
        :param Remark: remark
        :type Remark: str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        :param UpdatedAt: Update time
        :type UpdatedAt: str
        :param Id: id
        :type Id: int
        """
        self.Alias = None
        self.RegionId = None
        self.RegionName = None
        self.Status = None
        self.Remark = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Id = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Registry(AbstractModel):
    """Instance information structure

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RegistryName: Instance name
        :type RegistryName: str
        :param RegistryType: Instance specification
        :type RegistryType: str
        :param Status: Instance status
        :type Status: str
        :param PublicDomain: Public access URL of the instance
        :type PublicDomain: str
        :param CreatedAt: Instance creation time
        :type CreatedAt: str
        :param RegionName: Region name
        :type RegionName: str
        :param RegionId: Region ID
        :type RegionId: int
        :param EnableAnonymous: Whether to enable anonymity
        :type EnableAnonymous: bool
        :param TokenValidTime: Token validity period
        :type TokenValidTime: int
        :param InternalEndpoint: Internal access address of the instance
        :type InternalEndpoint: str
        :param TagSpecification: Cloud tag of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param ExpiredAt: Instance expiration time (for prepayment)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredAt: str
        :param PayMod: Instance billing mode. Valid values: 0: Postpayment; 1: Prepayment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMod: int
        :param RenewFlag: Prepayment renewal flag. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        """
        self.RegistryId = None
        self.RegistryName = None
        self.RegistryType = None
        self.Status = None
        self.PublicDomain = None
        self.CreatedAt = None
        self.RegionName = None
        self.RegionId = None
        self.EnableAnonymous = None
        self.TokenValidTime = None
        self.InternalEndpoint = None
        self.TagSpecification = None
        self.ExpiredAt = None
        self.PayMod = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        self.Status = params.get("Status")
        self.PublicDomain = params.get("PublicDomain")
        self.CreatedAt = params.get("CreatedAt")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.EnableAnonymous = params.get("EnableAnonymous")
        self.TokenValidTime = params.get("TokenValidTime")
        self.InternalEndpoint = params.get("InternalEndpoint")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.ExpiredAt = params.get("ExpiredAt")
        self.PayMod = params.get("PayMod")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryChargePrepaid(AbstractModel):
    """Instance prepayment mode

    """

    def __init__(self):
        r"""
        :param Period: Instance purchase duration in months
        :type Period: int
        :param RenewFlag: Auto-renewal flag. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
        :type RenewFlag: int
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryCondition(AbstractModel):
    """Instance creation process

    """

    def __init__(self):
        r"""
        :param Type: Instance creation process type
        :type Type: str
        :param Status: Instance creation process status
        :type Status: str
        :param Reason: Reasons for transiting to the process
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self.Type = None
        self.Status = None
        self.Reason = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryStatus(AbstractModel):
    """Instance status

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param Status: Instance status
        :type Status: str
        :param Conditions: Additional status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conditions: list of RegistryCondition
        """
        self.RegistryId = None
        self.Status = None
        self.Conditions = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Instance ID
        :type RegistryId: str
        :param RegistryChargePrepaid: Auto-renewal flag and purchase duration in months for prepayment. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param Flag: Valid values: 0: renewal; 1: change from pay-as-you-go to monthly subscription billing
        :type Flag: int
        """
        self.RegistryId = None
        self.RegistryChargePrepaid = None
        self.Flag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("RegistryChargePrepaid") is not None:
            self.RegistryChargePrepaid = RegistryChargePrepaid()
            self.RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param RegistryId: Enterprise Edition instance ID
        :type RegistryId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ReplicationFilter(AbstractModel):
    """Synchronization rule filter

    """

    def __init__(self):
        r"""
        :param Type: Type (`name`, `tag` and `resource`)
        :type Type: str
        :param Value: It is left blank by default
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationLog(AbstractModel):
    """Synchronization log

    """

    def __init__(self):
        r"""
        :param ResourceType: Resource type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param Source: Path of the source resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Source: str
        :param Destination: Path of the destination resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Destination: str
        :param Status: Synchronization status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param StartTime: Start time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTime: str
        :param EndTime: End time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self.ResourceType = None
        self.Source = None
        self.Destination = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.Source = params.get("Source")
        self.Destination = params.get("Destination")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRegistry(AbstractModel):
    """ID of Enterprise Registry replication instance

    """

    def __init__(self):
        r"""
        :param RegistryId: Master instance ID
        :type RegistryId: str
        :param ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        :param Status: Status of the replication instance
        :type Status: str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None
        self.Status = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRule(AbstractModel):
    """Synchronization rule

    """

    def __init__(self):
        r"""
        :param Name: Name of synchronization rule
        :type Name: str
        :param DestNamespace: Destination namespace
        :type DestNamespace: str
        :param Override: Whether to override
        :type Override: bool
        :param Filters: Synchronization filters
        :type Filters: list of ReplicationFilter
        """
        self.Name = None
        self.DestNamespace = None
        self.Override = None
        self.Filters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DestNamespace = params.get("DestNamespace")
        self.Override = params.get("Override")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ReplicationFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionExecution(AbstractModel):
    """Tag retention rule execution

    """

    def __init__(self):
        r"""
        :param ExecutionId: Execution ID
        :type ExecutionId: int
        :param RetentionId: Rule ID
        :type RetentionId: int
        :param StartTime: Execution start time
        :type StartTime: str
        :param EndTime: Execution end time
        :type EndTime: str
        :param Status: Execution status. Valid values: Failed, Succeed, Stopped, InProgress.
        :type Status: str
        """
        self.ExecutionId = None
        self.RetentionId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.ExecutionId = params.get("ExecutionId")
        self.RetentionId = params.get("RetentionId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionPolicy(AbstractModel):
    """Tag retention policy

    """

    def __init__(self):
        r"""
        :param RetentionId: Tag retention policy ID
        :type RetentionId: int
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param RetentionRuleList: List of rules
        :type RetentionRuleList: list of RetentionRule
        :param CronSetting: Regular execution mode
        :type CronSetting: str
        :param Disabled: Whether to enable the rule
        :type Disabled: bool
        :param NextExecutionTime: The execution time of the next task based on the current time and `cronSetting`, which is for reference only
        :type NextExecutionTime: str
        """
        self.RetentionId = None
        self.NamespaceName = None
        self.RetentionRuleList = None
        self.CronSetting = None
        self.Disabled = None
        self.NextExecutionTime = None


    def _deserialize(self, params):
        self.RetentionId = params.get("RetentionId")
        self.NamespaceName = params.get("NamespaceName")
        if params.get("RetentionRuleList") is not None:
            self.RetentionRuleList = []
            for item in params.get("RetentionRuleList"):
                obj = RetentionRule()
                obj._deserialize(item)
                self.RetentionRuleList.append(obj)
        self.CronSetting = params.get("CronSetting")
        self.Disabled = params.get("Disabled")
        self.NextExecutionTime = params.get("NextExecutionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionRule(AbstractModel):
    """Tag retention rule

    """

    def __init__(self):
        r"""
        :param Key: Supported policy. Valid values: latestPushedK: Retain the latest specified number of pushed tags; nDaysSinceLastPush: Retain the tags pushed in the past specified number of days.
        :type Key: str
        :param Value: Rule value
        :type Value: int
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionTask(AbstractModel):
    """Rule of tag retention task execution

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: int
        :param ExecutionId: Rule execution ID
        :type ExecutionId: int
        :param StartTime: Task start time
        :type StartTime: str
        :param EndTime: Task end time
        :type EndTime: str
        :param Status: Task execution status. Valid values: Failed, Succeed, Stopped, InProgress.
        :type Status: str
        :param Total: Total number of tags
        :type Total: int
        :param Retained: Number of retained tags
        :type Retained: int
        :param Repository: Application repository
        :type Repository: str
        """
        self.TaskId = None
        self.ExecutionId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Total = None
        self.Retained = None
        self.Repository = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ExecutionId = params.get("ExecutionId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Total = params.get("Total")
        self.Retained = params.get("Retained")
        self.Repository = params.get("Repository")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Schedule(AbstractModel):
    """Job scheduling information

    """

    def __init__(self):
        r"""
        :param Type: Type. Valid values: Hourly, Daily, Weekly, Custom, Manual, Dryrun, None.
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """Security policy

    """

    def __init__(self):
        r"""
        :param PolicyIndex: Policy index
        :type PolicyIndex: int
        :param Description: Remarks
        :type Description: str
        :param CidrBlock: The public network IP address of the access source
        :type CidrBlock: str
        :param PolicyVersion: The version of the security policy
        :type PolicyVersion: str
        """
        self.PolicyIndex = None
        self.Description = None
        self.CidrBlock = None
        self.PolicyVersion = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Description = params.get("Description")
        self.CidrBlock = params.get("CidrBlock")
        self.PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Cloud tag

    """

    def __init__(self):
        r"""
        :param Key: Cloud tag key
        :type Key: str
        :param Value: Cloud tag value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """Cloud tag

    """

    def __init__(self):
        r"""
        :param ResourceType: Default value: instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param Tags: Cloud tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
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
        


class TaskDetail(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param TaskName: Task
        :type TaskName: str
        :param TaskUUID: Task UUID
        :type TaskUUID: str
        :param TaskStatus: Task status
        :type TaskStatus: str
        :param TaskMessage: Task details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TaskMessage: str
        :param CreatedTime: Start time of the task
        :type CreatedTime: str
        :param FinishedTime: End time of the task
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FinishedTime: str
        """
        self.TaskName = None
        self.TaskUUID = None
        self.TaskStatus = None
        self.TaskMessage = None
        self.CreatedTime = None
        self.FinishedTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskUUID = params.get("TaskUUID")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskMessage = params.get("TaskMessage")
        self.CreatedTime = params.get("CreatedTime")
        self.FinishedTime = params.get("FinishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrImageInfo(AbstractModel):
    """Image information

    """

    def __init__(self):
        r"""
        :param Digest: Hash value
        :type Digest: str
        :param Size: Image size in bytes
        :type Size: int
        :param ImageVersion: Tag name
        :type ImageVersion: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Kind: Artifact type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kind: str
        :param KmsSignature: KMS signature information
Note: This field may return null, indicating that no valid values can be obtained.
        :type KmsSignature: str
        """
        self.Digest = None
        self.Size = None
        self.ImageVersion = None
        self.UpdateTime = None
        self.Kind = None
        self.KmsSignature = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        self.Size = params.get("Size")
        self.ImageVersion = params.get("ImageVersion")
        self.UpdateTime = params.get("UpdateTime")
        self.Kind = params.get("Kind")
        self.KmsSignature = params.get("KmsSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrInstanceToken(AbstractModel):
    """Instance login token

    """

    def __init__(self):
        r"""
        :param Id: Token ID
        :type Id: str
        :param Desc: Token description
        :type Desc: str
        :param RegistryId: ID of the instance of the token
        :type RegistryId: str
        :param Enabled: Token status
        :type Enabled: bool
        :param CreatedAt: Token creation time
        :type CreatedAt: str
        :param ExpiredAt: Token expiration timestamp
        :type ExpiredAt: int
        """
        self.Id = None
        self.Desc = None
        self.RegistryId = None
        self.Enabled = None
        self.CreatedAt = None
        self.ExpiredAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        self.RegistryId = params.get("RegistryId")
        self.Enabled = params.get("Enabled")
        self.CreatedAt = params.get("CreatedAt")
        self.ExpiredAt = params.get("ExpiredAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrNamespaceInfo(AbstractModel):
    """TCR namespace description

    """

    def __init__(self):
        r"""
        :param Name: Namespace name
        :type Name: str
        :param CreationTime: Creation time
        :type CreationTime: str
        :param Public: Access level
        :type Public: bool
        :param NamespaceId: Namespace ID
        :type NamespaceId: int
        :param TagSpecification: Cloud tag of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param Metadata: Namespace metadata
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metadata: list of KeyValueString
        """
        self.Name = None
        self.CreationTime = None
        self.Public = None
        self.NamespaceId = None
        self.TagSpecification = None
        self.Metadata = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        if params.get("Metadata") is not None:
            self.Metadata = []
            for item in params.get("Metadata"):
                obj = KeyValueString()
                obj._deserialize(item)
                self.Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrRepositoryInfo(AbstractModel):
    """TCR image repository information

    """

    def __init__(self):
        r"""
        :param Name: Repository name
        :type Name: str
        :param Namespace: Namespace name
        :type Namespace: str
        :param CreationTime: Creation time, such as `2006-01-02 15:04:05.999999999 -0700 MST`
        :type CreationTime: str
        :param Public: Whether to make public
        :type Public: bool
        :param Description: Detailed repository description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param BriefDescription: Brief description
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefDescription: str
        :param UpdateTime: Update time, such as `2006-01-02 15:04:05.999999999 -0700 MST`
        :type UpdateTime: str
        """
        self.Name = None
        self.Namespace = None
        self.CreationTime = None
        self.Public = None
        self.Description = None
        self.BriefDescription = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.Description = params.get("Description")
        self.BriefDescription = params.get("BriefDescription")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTarget(AbstractModel):
    """Trigger target

    """

    def __init__(self):
        r"""
        :param Address: Target address
        :type Address: str
        :param Headers: Custom headers
        :type Headers: list of Header
        """
        self.Address = None
        self.Headers = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTrigger(AbstractModel):
    """Webhook trigger

    """

    def __init__(self):
        r"""
        :param Name: Trigger name
        :type Name: str
        :param Targets: Trigger target
        :type Targets: list of WebhookTarget
        :param EventTypes: Action to be triggered
        :type EventTypes: list of str
        :param Condition: Trigger rule
        :type Condition: str
        :param Enabled: Whether to enable the trigger
        :type Enabled: bool
        :param Id: Trigger ID
        :type Id: int
        :param Description: Trigger description
        :type Description: str
        :param NamespaceId: ID of the namespace of the trigger
        :type NamespaceId: int
        """
        self.Name = None
        self.Targets = None
        self.EventTypes = None
        self.Condition = None
        self.Enabled = None
        self.Id = None
        self.Description = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EventTypes = params.get("EventTypes")
        self.Condition = params.get("Condition")
        self.Enabled = params.get("Enabled")
        self.Id = params.get("Id")
        self.Description = params.get("Description")
        self.NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTriggerLog(AbstractModel):
    """Trigger log

    """

    def __init__(self):
        r"""
        :param Id: Log ID
        :type Id: int
        :param TriggerId: Trigger ID
        :type TriggerId: int
        :param EventType: Event type
        :type EventType: str
        :param NotifyType: Notification type
        :type NotifyType: str
        :param Detail: Details
        :type Detail: str
        :param CreationTime: Creation time
        :type CreationTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Status
        :type Status: str
        """
        self.Id = None
        self.TriggerId = None
        self.EventType = None
        self.NotifyType = None
        self.Detail = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TriggerId = params.get("TriggerId")
        self.EventType = params.get("EventType")
        self.NotifyType = params.get("NotifyType")
        self.Detail = params.get("Detail")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        