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
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Status: Private network access status
        :type Status: str
        :param _AccessIp: Private network access IP
        :type AccessIp: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AccessIp = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccessIp(self):
        return self._AccessIp

    @AccessIp.setter
    def AccessIp(self, AccessIp):
        self._AccessIp = AccessIp


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AccessIp = params.get("AccessIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameRequest(AbstractModel):
    """CheckInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryName: Name of the instance to be created
        :type RegistryName: str
        """
        self._RegistryName = None

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName


    def _deserialize(self, params):
        self._RegistryName = params.get("RegistryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameResponse(AbstractModel):
    """CheckInstanceName response structure.

    """

    def __init__(self):
        r"""
        :param _IsValidated: Verification result. Valid values: true: Valid; false: Invalid.
        :type IsValidated: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsValidated = None
        self._RequestId = None

    @property
    def IsValidated(self):
        return self._IsValidated

    @IsValidated.setter
    def IsValidated(self, IsValidated):
        self._IsValidated = IsValidated

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValidated = params.get("IsValidated")
        self._RequestId = params.get("RequestId")


class CheckInstanceRequest(AbstractModel):
    """CheckInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: ID of the instance to be verified.
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceResponse(AbstractModel):
    """CheckInstance response structure.

    """

    def __init__(self):
        r"""
        :param _IsValidated: Verification result. true: valid, false: invalid
        :type IsValidated: bool
        :param _RegionId: ID of the region where the instance is located.
        :type RegionId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsValidated = None
        self._RegionId = None
        self._RequestId = None

    @property
    def IsValidated(self):
        return self._IsValidated

    @IsValidated.setter
    def IsValidated(self, IsValidated):
        self._IsValidated = IsValidated

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValidated = params.get("IsValidated")
        self._RegionId = params.get("RegionId")
        self._RequestId = params.get("RequestId")


class CreateCustomAccountRequest(AbstractModel):
    """CreateCustomAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Name: Custom account name
        :type Name: str
        :param _Permissions: Policy list
        :type Permissions: list of Permission
        :param _Description: Custom account description
        :type Description: str
        :param _Duration: Validity in days starting from the current day. It takes a higher priority than `ExpiresAt`.
        :type Duration: int
        :param _ExpiresAt: Expiry time of the custom account (timestamp, in milliseconds)
        :type ExpiresAt: int
        :param _Disable: Whether to disable the custom account
        :type Disable: bool
        """
        self._RegistryId = None
        self._Name = None
        self._Permissions = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomAccountResponse(AbstractModel):
    """CreateCustomAccount response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Custom username (the prefix `tcr$` is automatically added)
        :type Name: str
        :param _Password: Custom password, which is displayed only once
        :type Password: str
        :param _ExpiresAt: Custom expiry time (timestamp)
        :type ExpiresAt: int
        :param _CreateTime: Custom account creation time
        :type CreateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Password = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class CreateImageAccelerationServiceRequest(AbstractModel):
    """CreateImageAccelerationService request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _VpcId: ID of the VPC where the CFS file system to be created resides
        :type VpcId: str
        :param _SubnetId: ID of the subnet where the CFS file system to be created resides
        :type SubnetId: str
        :param _StorageType: Storage class of the CFS file system to be created. Valid values: SD: Standard; HP: High-Performance.
        :type StorageType: str
        :param _PGroupId: Permission group ID
        :type PGroupId: str
        :param _Zone: AZ name, such as `ap-beijing-1`. For more information, see the list of regions and AZs in Overview.
        :type Zone: str
        :param _TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self._RegistryId = None
        self._VpcId = None
        self._SubnetId = None
        self._StorageType = None
        self._PGroupId = None
        self._Zone = None
        self._TagSpecification = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def PGroupId(self):
        return self._PGroupId

    @PGroupId.setter
    def PGroupId(self, PGroupId):
        self._PGroupId = PGroupId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._StorageType = params.get("StorageType")
        self._PGroupId = params.get("PGroupId")
        self._Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageAccelerationServiceResponse(AbstractModel):
    """CreateImageAccelerationService response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace
        :type NamespaceName: str
        :param _Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Rule = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        if params.get("Rule") is not None:
            self._Rule = ImmutableTagRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImmutableTagRulesResponse(AbstractModel):
    """CreateImmutableTagRules response structure.

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


class CreateInstanceCustomizedDomainRequest(AbstractModel):
    """CreateInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _DomainName: Custom domain name
        :type DomainName: str
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._RegistryId = None
        self._DomainName = None
        self._CertificateId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DomainName = params.get("DomainName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceCustomizedDomainResponse(AbstractModel):
    """CreateInstanceCustomizedDomain response structure.

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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryName: Enterprise Edition instance name
        :type RegistryName: str
        :param _RegistryType: Enterprise Edition instance type. Valid values: basic: Basic; standard: Standard; premium: Premium.
        :type RegistryType: str
        :param _TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _RegistryChargeType: Instance billing mode. Valid values: 0: Pay-as-you-go billing; 1: Prepaid. Default value: 0.
        :type RegistryChargeType: int
        :param _RegistryChargePrepaid: Auto-renewal setting and purchase period
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param _SyncTag: Whether to sync TCR cloud tags to the COS bucket
        :type SyncTag: bool
        :param _EnableCosMAZ: Whether to enable the COS Multi-AZ feature
        :type EnableCosMAZ: bool
        :param _DeletionProtection: Whether to enable deletion protection
        :type DeletionProtection: bool
        """
        self._RegistryName = None
        self._RegistryType = None
        self._TagSpecification = None
        self._RegistryChargeType = None
        self._RegistryChargePrepaid = None
        self._SyncTag = None
        self._EnableCosMAZ = None
        self._DeletionProtection = None

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def RegistryChargeType(self):
        return self._RegistryChargeType

    @RegistryChargeType.setter
    def RegistryChargeType(self, RegistryChargeType):
        self._RegistryChargeType = RegistryChargeType

    @property
    def RegistryChargePrepaid(self):
        return self._RegistryChargePrepaid

    @RegistryChargePrepaid.setter
    def RegistryChargePrepaid(self, RegistryChargePrepaid):
        self._RegistryChargePrepaid = RegistryChargePrepaid

    @property
    def SyncTag(self):
        return self._SyncTag

    @SyncTag.setter
    def SyncTag(self, SyncTag):
        self._SyncTag = SyncTag

    @property
    def EnableCosMAZ(self):
        return self._EnableCosMAZ

    @EnableCosMAZ.setter
    def EnableCosMAZ(self, EnableCosMAZ):
        self._EnableCosMAZ = EnableCosMAZ

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._RegistryName = params.get("RegistryName")
        self._RegistryType = params.get("RegistryType")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        self._RegistryChargeType = params.get("RegistryChargeType")
        if params.get("RegistryChargePrepaid") is not None:
            self._RegistryChargePrepaid = RegistryChargePrepaid()
            self._RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self._SyncTag = params.get("SyncTag")
        self._EnableCosMAZ = params.get("EnableCosMAZ")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Enterprise Edition instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _TokenType: Access credential type. Values: `longterm` and `temp` (default, valid for one hour)
        :type TokenType: str
        :param _Desc: Description of the long-term access credential
        :type Desc: str
        """
        self._RegistryId = None
        self._TokenType = None
        self._Desc = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def TokenType(self):
        return self._TokenType

    @TokenType.setter
    def TokenType(self, TokenType):
        self._TokenType = TokenType

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._TokenType = params.get("TokenType")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param _Username: Username
Note: this field may return `null`, indicating that no valid value can be found.
        :type Username: str
        :param _Token: Access credential
        :type Token: str
        :param _ExpTime: Expiration timestamp of access credential. It is a string of numbers without unit.
        :type ExpTime: int
        :param _TokenId: Token ID of long-term access credential. It is not available to temporary access credential.
Note: this field may return `null`, indicating that no valid value can be found.
        :type TokenId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Username = None
        self._Token = None
        self._ExpTime = None
        self._TokenId = None
        self._RequestId = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpTime(self):
        return self._ExpTime

    @ExpTime.setter
    def ExpTime(self, ExpTime):
        self._ExpTime = ExpTime

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Token = params.get("Token")
        self._ExpTime = params.get("ExpTime")
        self._TokenId = params.get("TokenId")
        self._RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self._RegistryId = None
        self._SecurityGroupPolicySet = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def SecurityGroupPolicySet(self):
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultipleSecurityPolicyResponse(AbstractModel):
    """CreateMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name, which can contain 2–30 lowercase letters, digits, and separators (".", "_", and "-") but can neither start or end with a separator nor contain consecutive separators.
        :type NamespaceName: str
        :param _IsPublic: Whether to make public. Valid values: true: Yes; false: No.
        :type IsPublic: bool
        :param _TagSpecification: Cloud tag description
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._IsPublic = None
        self._TagSpecification = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._IsPublic = params.get("IsPublic")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

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


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Master instance ID
        :type RegistryId: str
        :param _ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param _ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        :param _SyncTag: Whether to sync TCR cloud tags to the COS Bucket
        :type SyncTag: bool
        """
        self._RegistryId = None
        self._ReplicationRegionId = None
        self._ReplicationRegionName = None
        self._SyncTag = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ReplicationRegionName(self):
        return self._ReplicationRegionName

    @ReplicationRegionName.setter
    def ReplicationRegionName(self, ReplicationRegionName):
        self._ReplicationRegionName = ReplicationRegionName

    @property
    def SyncTag(self):
        return self._SyncTag

    @SyncTag.setter
    def SyncTag(self, SyncTag):
        self._SyncTag = SyncTag


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ReplicationRegionName = params.get("ReplicationRegionName")
        self._SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationInstanceResponse(AbstractModel):
    """CreateReplicationInstance response structure.

    """

    def __init__(self):
        r"""
        :param _ReplicationRegistryId: Enterprise Registry Instance ID
        :type ReplicationRegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReplicationRegistryId = None
        self._RequestId = None

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Repository name
        :type RepositoryName: str
        :param _BriefDescription: Brief repository description
        :type BriefDescription: str
        :param _Description: Detailed repository description
        :type Description: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._BriefDescription = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._BriefDescription = params.get("BriefDescription")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository response structure.

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


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _CidrBlock: 192.168.0.0/24
        :type CidrBlock: str
        :param _Description: Remarks
        :type Description: str
        """
        self._RegistryId = None
        self._CidrBlock = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._CidrBlock = params.get("CidrBlock")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class CreateServiceAccountRequest(AbstractModel):
    """CreateServiceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Name: Service account name
        :type Name: str
        :param _Permissions: Policy list
        :type Permissions: list of Permission
        :param _Description: Service account description
        :type Description: str
        :param _Duration: Validity in days starting from the current day. It takes a higher priority than `ExpiresAt`.
        :type Duration: int
        :param _ExpiresAt: Expiry time (timestamp, in milliseconds)
        :type ExpiresAt: int
        :param _Disable: Whether to disable the service account
        :type Disable: bool
        """
        self._RegistryId = None
        self._Name = None
        self._Permissions = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceAccountResponse(AbstractModel):
    """CreateServiceAccount response structure.

    """

    def __init__(self):
        r"""
        :param _Name: Service account name (the prefix `tcr$` is automatically added)
        :type Name: str
        :param _Password: Service account password, which is displayed only once
        :type Password: str
        :param _ExpiresAt: Expiry time of the service account (timestamp)
        :type ExpiresAt: int
        :param _CreateTime: Creation time of the service account
        :type CreateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Password = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class CreateSignaturePolicyRequest(AbstractModel):
    """CreateSignaturePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Name: Policy name
        :type Name: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _KmsId: KMS key
        :type KmsId: str
        :param _KmsRegion: Region of the KMS key
        :type KmsRegion: str
        :param _Domain: Custom domain name. If this parameter is left empty, the default domain name of the TCR instance will be used to generate the signature.
        :type Domain: str
        :param _Disabled: Whether to disable the signing policy. Default value: false.
        :type Disabled: bool
        """
        self._RegistryId = None
        self._Name = None
        self._NamespaceName = None
        self._KmsId = None
        self._KmsRegion = None
        self._Domain = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def KmsId(self):
        return self._KmsId

    @KmsId.setter
    def KmsId(self, KmsId):
        self._KmsId = KmsId

    @property
    def KmsRegion(self):
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._NamespaceName = params.get("NamespaceName")
        self._KmsId = params.get("KmsId")
        self._KmsRegion = params.get("KmsRegion")
        self._Domain = params.get("Domain")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignaturePolicyResponse(AbstractModel):
    """CreateSignaturePolicy response structure.

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


class CreateSignatureRequest(AbstractModel):
    """CreateSignature request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Repository name
        :type RepositoryName: str
        :param _ImageVersion: Tag name
        :type ImageVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignatureResponse(AbstractModel):
    """CreateSignature response structure.

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


class CreateTagRetentionExecutionRequest(AbstractModel):
    """CreateTagRetentionExecution request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _RetentionId: Tag retention rule ID
        :type RetentionId: int
        :param _DryRun: Whether the execution is simulated. Default value: false (not simulated)
        :type DryRun: bool
        """
        self._RegistryId = None
        self._RetentionId = None
        self._DryRun = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionExecutionResponse(AbstractModel):
    """CreateTagRetentionExecution response structure.

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


class CreateTagRetentionRuleRequest(AbstractModel):
    """CreateTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _NamespaceId: Namespace ID
        :type NamespaceId: int
        :param _RetentionRule: Retention policy
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param _CronSetting: Execution cycle. Valid values: manual, daily, weekly, monthly.
        :type CronSetting: str
        :param _Disabled: Whether to disable the rule. Default value: false.
        :type Disabled: bool
        """
        self._RegistryId = None
        self._NamespaceId = None
        self._RetentionRule = None
        self._CronSetting = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RetentionRule(self):
        return self._RetentionRule

    @RetentionRule.setter
    def RetentionRule(self, RetentionRule):
        self._RetentionRule = RetentionRule

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self._RetentionRule = RetentionRule()
            self._RetentionRule._deserialize(params.get("RetentionRule"))
        self._CronSetting = params.get("CronSetting")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionRuleResponse(AbstractModel):
    """CreateTagRetentionRule response structure.

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


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Trigger: Trigger parameter
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _Namespace: Namespace
        :type Namespace: str
        """
        self._RegistryId = None
        self._Trigger = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param _Trigger: Newly created trigger
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Trigger = None
        self._RequestId = None

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._RequestId = params.get("RequestId")


class CustomAccount(AbstractModel):
    """Custom account

    """

    def __init__(self):
        r"""
        :param _Name: Custom account name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param _Description: Description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _Disable: Whether to disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Disable: bool
        :param _ExpiresAt: Expiry time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExpiresAt: int
        :param _CreateTime: Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Permissions: Policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Permissions: list of Permission
        """
        self._Name = None
        self._Description = None
        self._Disable = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Permissions = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Disable = params.get("Disable")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomizedDomainInfo(AbstractModel):
    """Custom domain name information

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _CertId: Certificate ID
        :type CertId: str
        :param _DomainName: Domain name
        :type DomainName: str
        :param _Status: Domain name creation status. Valid values: SUCCESS, FAILURE, CREATING, DELETING.
        :type Status: str
        """
        self._RegistryId = None
        self._CertId = None
        self._DomainName = None
        self._Status = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._CertId = params.get("CertId")
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomAccountRequest(AbstractModel):
    """DeleteCustomAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID	
        :type RegistryId: str
        :param _Name: Custom account name
        :type Name: str
        """
        self._RegistryId = None
        self._Name = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomAccountResponse(AbstractModel):
    """DeleteCustomAccount response structure.

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


class DeleteImageAccelerateServiceRequest(AbstractModel):
    """DeleteImageAccelerateService request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageAccelerateServiceResponse(AbstractModel):
    """DeleteImageAccelerateService response structure.

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


class DeleteImageRequest(AbstractModel):
    """DeleteImage request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RepositoryName: Image repository name
        :type RepositoryName: str
        :param _ImageVersion: Image tag
        :type ImageVersion: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._RepositoryName = None
        self._ImageVersion = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage response structure.

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


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace
        :type NamespaceName: str
        :param _RuleId: Rule ID
        :type RuleId: int
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RuleId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImmutableTagRulesResponse(AbstractModel):
    """DeleteImmutableTagRules response structure.

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


class DeleteInstanceCustomizedDomainRequest(AbstractModel):
    """DeleteInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _DomainName: Custom domain name
        :type DomainName: str
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._RegistryId = None
        self._DomainName = None
        self._CertificateId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DomainName = params.get("DomainName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceCustomizedDomainResponse(AbstractModel):
    """DeleteInstanceCustomizedDomain response structure.

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


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _DeleteBucket: Whether to delete the bucket. Default value: false.
        :type DeleteBucket: bool
        :param _DryRun: Whether to enable the `dryRun` mode. Default value: false.
        :type DryRun: bool
        """
        self._RegistryId = None
        self._DeleteBucket = None
        self._DryRun = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def DeleteBucket(self):
        return self._DeleteBucket

    @DeleteBucket.setter
    def DeleteBucket(self, DeleteBucket):
        self._DeleteBucket = DeleteBucket

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._DeleteBucket = params.get("DeleteBucket")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

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


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _TokenId: Access credential ID
        :type TokenId: str
        """
        self._RegistryId = None
        self._TokenId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._TokenId = params.get("TokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken response structure.

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


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _SecurityGroupPolicySet: Security group policy
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self._RegistryId = None
        self._SecurityGroupPolicySet = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def SecurityGroupPolicySet(self):
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultipleSecurityPolicyResponse(AbstractModel):
    """DeleteMultipleSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace response structure.

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


class DeleteReplicationInstanceRequest(AbstractModel):
    """DeleteReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _ReplicationRegistryId: Replica instance ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: Region ID of the replica instance
        :type ReplicationRegionId: int
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReplicationInstanceResponse(AbstractModel):
    """DeleteReplicationInstance response structure.

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


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Image repository name
        :type RepositoryName: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository response structure.

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


class DeleteRepositoryTagsRequest(AbstractModel):
    """DeleteRepositoryTags request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Repository name
        :type RepositoryName: str
        :param _Tags: List of tags. Up to 20 tags can be returned for a request.
        :type Tags: list of str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._Tags = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryTagsResponse(AbstractModel):
    """DeleteRepositoryTags response structure.

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


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _PolicyIndex: Allowlist ID
        :type PolicyIndex: int
        :param _PolicyVersion: Allowlist version
        :type PolicyVersion: str
        :param _CidrBlock: IP range or IP address (mutually exclusive).
        :type CidrBlock: str
        """
        self._RegistryId = None
        self._PolicyIndex = None
        self._PolicyVersion = None
        self._CidrBlock = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._PolicyIndex = params.get("PolicyIndex")
        self._PolicyVersion = params.get("PolicyVersion")
        self._CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class DeleteServiceAccountRequest(AbstractModel):
    """DeleteServiceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID	
        :type RegistryId: str
        :param _Name: Service account name
        :type Name: str
        """
        self._RegistryId = None
        self._Name = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceAccountResponse(AbstractModel):
    """DeleteServiceAccount response structure.

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


class DeleteSignaturePolicyRequest(AbstractModel):
    """DeleteSignaturePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        """
        self._RegistryId = None
        self._NamespaceName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSignaturePolicyResponse(AbstractModel):
    """DeleteSignaturePolicy response structure.

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


class DeleteTagRetentionRuleRequest(AbstractModel):
    """DeleteTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _RetentionId: Tag retention rule ID
        :type RetentionId: int
        """
        self._RegistryId = None
        self._RetentionId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagRetentionRuleResponse(AbstractModel):
    """DeleteTagRetentionRule response structure.

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


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Id: Trigger ID
        :type Id: int
        """
        self._RegistryId = None
        self._Namespace = None
        self._Id = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Namespace = params.get("Namespace")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger response structure.

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


class DescribeChartDownloadInfoRequest(AbstractModel):
    """DescribeChartDownloadInfo request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace
        :type NamespaceName: str
        :param _ChartName: Chart name
        :type ChartName: str
        :param _ChartVersion: Chart version
        :type ChartVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._ChartName = None
        self._ChartVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def ChartName(self):
        return self._ChartName

    @ChartName.setter
    def ChartName(self, ChartName):
        self._ChartName = ChartName

    @property
    def ChartVersion(self):
        return self._ChartVersion

    @ChartVersion.setter
    def ChartVersion(self, ChartVersion):
        self._ChartVersion = ChartVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._ChartName = params.get("ChartName")
        self._ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChartDownloadInfoResponse(AbstractModel):
    """DescribeChartDownloadInfo response structure.

    """

    def __init__(self):
        r"""
        :param _PreSignedDownloadURL: Presigned URL for download
        :type PreSignedDownloadURL: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PreSignedDownloadURL = None
        self._RequestId = None

    @property
    def PreSignedDownloadURL(self):
        return self._PreSignedDownloadURL

    @PreSignedDownloadURL.setter
    def PreSignedDownloadURL(self, PreSignedDownloadURL):
        self._PreSignedDownloadURL = PreSignedDownloadURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedDownloadURL = params.get("PreSignedDownloadURL")
        self._RequestId = params.get("RequestId")


class DescribeCustomAccountsRequest(AbstractModel):
    """DescribeCustomAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _All: All custom accounts
        :type All: bool
        :param _EmbedPermission: Whether to enter the policy
        :type EmbedPermission: bool
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: `0`
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: `20`. Maximum value: 100`.
        :type Limit: int
        """
        self._RegistryId = None
        self._All = None
        self._EmbedPermission = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def EmbedPermission(self):
        return self._EmbedPermission

    @EmbedPermission.setter
    def EmbedPermission(self, EmbedPermission):
        self._EmbedPermission = EmbedPermission

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._All = params.get("All")
        self._EmbedPermission = params.get("EmbedPermission")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomAccountsResponse(AbstractModel):
    """DescribeCustomAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _CustomAccounts: List of custom accounts
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CustomAccounts: list of CustomAccount
        :param _TotalCount: Number of custom accounts
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CustomAccounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CustomAccounts(self):
        return self._CustomAccounts

    @CustomAccounts.setter
    def CustomAccounts(self, CustomAccounts):
        self._CustomAccounts = CustomAccounts

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
        if params.get("CustomAccounts") is not None:
            self._CustomAccounts = []
            for item in params.get("CustomAccounts"):
                obj = CustomAccount()
                obj._deserialize(item)
                self._CustomAccounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeExternalEndpointStatusRequest(AbstractModel):
    """DescribeExternalEndpointStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalEndpointStatusResponse(AbstractModel):
    """DescribeExternalEndpointStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Public network access status. Valid values: Opening, Opened, Closed.
        :type Status: str
        :param _Reason: Reason
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Reason = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._RequestId = params.get("RequestId")


class DescribeGCJobsRequest(AbstractModel):
    """DescribeGCJobs request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGCJobsResponse(AbstractModel):
    """DescribeGCJobs response structure.

    """

    def __init__(self):
        r"""
        :param _Jobs: List of GC jobs
        :type Jobs: list of GCJobInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = GCJobInfo()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageAccelerateServiceRequest(AbstractModel):
    """DescribeImageAccelerateService request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAccelerateServiceResponse(AbstractModel):
    """DescribeImageAccelerateService response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Image acceleration status
        :type Status: str
        :param _CFSVIP: CFS VIP
        :type CFSVIP: str
        :param _IsEnable: Whether to enable
        :type IsEnable: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._CFSVIP = None
        self._IsEnable = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CFSVIP(self):
        return self._CFSVIP

    @CFSVIP.setter
    def CFSVIP(self, CFSVIP):
        self._CFSVIP = CFSVIP

    @property
    def IsEnable(self):
        return self._IsEnable

    @IsEnable.setter
    def IsEnable(self, IsEnable):
        self._IsEnable = IsEnable

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CFSVIP = params.get("CFSVIP")
        self._IsEnable = params.get("IsEnable")
        self._RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Image repository name
        :type RepositoryName: str
        :param _ImageVersion: Image tag
        :type ImageVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests response structure.

    """

    def __init__(self):
        r"""
        :param _Manifest: Image manifest information
        :type Manifest: str
        :param _Config: Image configuration information
        :type Config: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Manifest = None
        self._Config = None
        self._RequestId = None

    @property
    def Manifest(self):
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Manifest = params.get("Manifest")
        self._Config = params.get("Config")
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Image repository name
        :type RepositoryName: str
        :param _ImageVersion: Image tag specified for fuzzy search
        :type ImageVersion: str
        :param _Limit: Number of entries per page, which is used for pagination. Default value: 20.
        :type Limit: int
        :param _Offset: Page number. Default value: 1.
        :type Offset: int
        :param _Digest: Image digest specified for search
        :type Digest: str
        :param _ExactMatch: Whether to use exact matching. Valid values: `true` (exact matching), `null` (fuzzy matching).
        :type ExactMatch: bool
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._ImageVersion = None
        self._Limit = None
        self._Offset = None
        self._Digest = None
        self._ExactMatch = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._ImageVersion = params.get("ImageVersion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Digest = params.get("Digest")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        r"""
        :param _ImageInfoList: List of container images
        :type ImageInfoList: list of TcrImageInfo
        :param _TotalCount: Total number of container images
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageInfoList(self):
        return self._ImageInfoList

    @ImageInfoList.setter
    def ImageInfoList(self, ImageInfoList):
        self._ImageInfoList = ImageInfoList

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
        if params.get("ImageInfoList") is not None:
            self._ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self._ImageInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImmutableTagRulesResponse(AbstractModel):
    """DescribeImmutableTagRules response structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Rule list
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Rules: list of ImmutableTagRule
        :param _EmptyNs: Namespace with no rules created
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type EmptyNs: list of str
        :param _Total: Total rules
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Rules = None
        self._EmptyNs = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def EmptyNs(self):
        return self._EmptyNs

    @EmptyNs.setter
    def EmptyNs(self, EmptyNs):
        self._EmptyNs = EmptyNs

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ImmutableTagRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._EmptyNs = params.get("EmptyNs")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeInstanceAllNamespacesRequest(AbstractModel):
    """DescribeInstanceAllNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Start position offset
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllNamespacesResponse(AbstractModel):
    """DescribeInstanceAllNamespaces response structure.

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


class DescribeInstanceCustomizedDomainRequest(AbstractModel):
    """DescribeInstanceCustomizedDomain request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceCustomizedDomainResponse(AbstractModel):
    """DescribeInstanceCustomizedDomain response structure.

    """

    def __init__(self):
        r"""
        :param _DomainInfoList: List of domain names
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainInfoList: list of CustomizedDomainInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainInfoList(self):
        return self._DomainInfoList

    @DomainInfoList.setter
    def DomainInfoList(self, DomainInfoList):
        self._DomainInfoList = DomainInfoList

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
        if params.get("DomainInfoList") is not None:
            self._DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = CustomizedDomainInfo()
                obj._deserialize(item)
                self._DomainInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryIds: Array of instance IDs
        :type RegistryIds: list of str
        """
        self._RegistryIds = None

    @property
    def RegistryIds(self):
        return self._RegistryIds

    @RegistryIds.setter
    def RegistryIds(self, RegistryIds):
        self._RegistryIds = RegistryIds


    def _deserialize(self, params):
        self._RegistryIds = params.get("RegistryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryStatusSet: List of instance statuses
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistryStatusSet: list of RegistryStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryStatusSet = None
        self._RequestId = None

    @property
    def RegistryStatusSet(self):
        return self._RegistryStatusSet

    @RegistryStatusSet.setter
    def RegistryStatusSet(self, RegistryStatusSet):
        self._RegistryStatusSet = RegistryStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self._RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self._RegistryStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of long-term access credentials
        :type TotalCount: int
        :param _Tokens: List of long-term access credentials
        :type Tokens: list of TcrInstanceToken
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tokens = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tokens(self):
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self._Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self._Tokens.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Registryids: List of instance IDs (if it is empty,
it indicates to get all instances under the current account)
        :type Registryids: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _AllRegion: Whether to get the instances in all regions. Default value: False.
        :type AllRegion: bool
        """
        self._Registryids = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._AllRegion = None

    @property
    def Registryids(self):
        return self._Registryids

    @Registryids.setter
    def Registryids(self, Registryids):
        self._Registryids = Registryids

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AllRegion(self):
        return self._AllRegion

    @AllRegion.setter
    def AllRegion(self, AllRegion):
        self._AllRegion = AllRegion


    def _deserialize(self, params):
        self._Registryids = params.get("Registryids")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances
        :type TotalCount: int
        :param _Registries: List of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type Registries: list of Registry
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Registries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Registries(self):
        return self._Registries

    @Registries.setter
    def Registries(self, Registries):
        self._Registries = Registries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self._Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self._Registries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternalEndpointsRequest(AbstractModel):
    """DescribeInternalEndpoints request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointsResponse(AbstractModel):
    """DescribeInternalEndpoints response structure.

    """

    def __init__(self):
        r"""
        :param _AccessVpcSet: List of private network access addresses
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessVpcSet: list of AccessVpc
        :param _TotalCount: Total number of private network access addresses
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessVpcSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccessVpcSet(self):
        return self._AccessVpcSet

    @AccessVpcSet.setter
    def AccessVpcSet(self, AccessVpcSet):
        self._AccessVpcSet = AccessVpcSet

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
        if params.get("AccessVpcSet") is not None:
            self._AccessVpcSet = []
            for item in params.get("AccessVpcSet"):
                obj = AccessVpc()
                obj._deserialize(item)
                self._AccessVpcSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Specified namespace. If this parameter is left empty, all namespaces will be queried.
        :type NamespaceName: str
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Page offset (page number from which to return the results)
        :type Offset: int
        :param _All: Whether to list all namespaces
        :type All: bool
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _KmsSignPolicy: Whether to query only namespaces for which the KMS image signature is enabled
        :type KmsSignPolicy: bool
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Limit = None
        self._Offset = None
        self._All = None
        self._Filters = None
        self._KmsSignPolicy = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def KmsSignPolicy(self):
        return self._KmsSignPolicy

    @KmsSignPolicy.setter
    def KmsSignPolicy(self, KmsSignPolicy):
        self._KmsSignPolicy = KmsSignPolicy


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._All = params.get("All")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._KmsSignPolicy = params.get("KmsSignPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceList: List of namespaces
        :type NamespaceList: list of TcrNamespaceInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NamespaceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

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
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of returned results
        :type TotalCount: int
        :param _Regions: List of regions
        :type Regions: list of Region
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Regions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = Region()
                obj._deserialize(item)
                self._Regions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        """
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId


    def _deserialize(self, params):
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceCreateTasksResponse(AbstractModel):
    """DescribeReplicationInstanceCreateTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TaskDetail: Task details
        :type TaskDetail: list of TaskDetail
        :param _Status: Overall task status
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskDetail = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskDetail(self):
        return self._TaskDetail

    @TaskDetail.setter
    def TaskDetail(self, TaskDetail):
        self._TaskDetail = TaskDetail

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskDetail") is not None:
            self._TaskDetail = []
            for item in params.get("TaskDetail"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._TaskDetail.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstanceSyncStatusRequest(AbstractModel):
    """DescribeReplicationInstanceSyncStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Master instance ID
        :type RegistryId: str
        :param _ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param _ShowReplicationLog: Whether to show the synchronization log
        :type ShowReplicationLog: bool
        :param _Offset: Page offset for log display. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 5, maximum value: 20.
        :type Limit: int
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None
        self._ShowReplicationLog = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ShowReplicationLog(self):
        return self._ShowReplicationLog

    @ShowReplicationLog.setter
    def ShowReplicationLog(self, ShowReplicationLog):
        self._ShowReplicationLog = ShowReplicationLog

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


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ShowReplicationLog = params.get("ShowReplicationLog")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ReplicationStatus: Synchronization status
        :type ReplicationStatus: str
        :param _ReplicationTime: Synchronization completion time
        :type ReplicationTime: str
        :param _ReplicationLog: Synchronization log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationLog: :class:`tencentcloud.tcr.v20190924.models.ReplicationLog`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReplicationStatus = None
        self._ReplicationTime = None
        self._ReplicationLog = None
        self._RequestId = None

    @property
    def ReplicationStatus(self):
        return self._ReplicationStatus

    @ReplicationStatus.setter
    def ReplicationStatus(self, ReplicationStatus):
        self._ReplicationStatus = ReplicationStatus

    @property
    def ReplicationTime(self):
        return self._ReplicationTime

    @ReplicationTime.setter
    def ReplicationTime(self, ReplicationTime):
        self._ReplicationTime = ReplicationTime

    @property
    def ReplicationLog(self):
        return self._ReplicationLog

    @ReplicationLog.setter
    def ReplicationLog(self, ReplicationLog):
        self._ReplicationLog = ReplicationLog

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReplicationStatus = params.get("ReplicationStatus")
        self._ReplicationTime = params.get("ReplicationTime")
        if params.get("ReplicationLog") is not None:
            self._ReplicationLog = ReplicationLog()
            self._ReplicationLog._deserialize(params.get("ReplicationLog"))
        self._RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 20, maximum value: 100.
        :type Limit: int
        """
        self._RegistryId = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

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


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstancesResponse(AbstractModel):
    """DescribeReplicationInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances
        :type TotalCount: int
        :param _ReplicationRegistries: Replication instance list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReplicationRegistries: list of ReplicationRegistry
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicationRegistries = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicationRegistries(self):
        return self._ReplicationRegistries

    @ReplicationRegistries.setter
    def ReplicationRegistries(self, ReplicationRegistries):
        self._ReplicationRegistries = ReplicationRegistries

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReplicationRegistries") is not None:
            self._ReplicationRegistries = []
            for item in params.get("ReplicationRegistries"):
                obj = ReplicationRegistry()
                obj._deserialize(item)
                self._ReplicationRegistries.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Specified namespace. If this parameter is left empty, image repositories in all namespaces will be queried.
        :type NamespaceName: str
        :param _RepositoryName: Specified image repository. If this parameter is left empty, all image repositories in the specified namespace will be queried.
        :type RepositoryName: str
        :param _Offset: Page number, which is used for pagination
        :type Offset: int
        :param _Limit: Number of entries per page, which is used for pagination
        :type Limit: int
        :param _SortBy: Sort field. Valid values: -creation_time, -name, -update_time.
        :type SortBy: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._Offset = None
        self._Limit = None
        self._SortBy = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

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
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories response structure.

    """

    def __init__(self):
        r"""
        :param _RepositoryList: Repository information list
        :type RepositoryList: list of TcrRepositoryInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RepositoryList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RepositoryList(self):
        return self._RepositoryList

    @RepositoryList.setter
    def RepositoryList(self, RepositoryList):
        self._RepositoryList = RepositoryList

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
        if params.get("RepositoryList") is not None:
            self._RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self._RepositoryList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    """DescribeSecurityPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    """DescribeSecurityPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicySet: Instance security policy group
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityPolicySet: list of SecurityPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityPolicySet = None
        self._RequestId = None

    @property
    def SecurityPolicySet(self):
        return self._SecurityPolicySet

    @SecurityPolicySet.setter
    def SecurityPolicySet(self, SecurityPolicySet):
        self._SecurityPolicySet = SecurityPolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityPolicySet") is not None:
            self._SecurityPolicySet = []
            for item in params.get("SecurityPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityPolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceAccountsRequest(AbstractModel):
    """DescribeServiceAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _All: All service accounts
        :type All: bool
        :param _EmbedPermission: Whether to fill in permission information
        :type EmbedPermission: bool
        :param _Filters: Filters
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: `0`
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: `20`. Maximum value: `100`. The maximum value is automatically applied when a value exceeding it is entered.
        :type Limit: int
        """
        self._RegistryId = None
        self._All = None
        self._EmbedPermission = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def All(self):
        return self._All

    @All.setter
    def All(self, All):
        self._All = All

    @property
    def EmbedPermission(self):
        return self._EmbedPermission

    @EmbedPermission.setter
    def EmbedPermission(self, EmbedPermission):
        self._EmbedPermission = EmbedPermission

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._All = params.get("All")
        self._EmbedPermission = params.get("EmbedPermission")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceAccountsResponse(AbstractModel):
    """DescribeServiceAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceAccounts: List of service accounts
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServiceAccounts: list of ServiceAccount
        :param _TotalCount: Number of service accounts
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceAccounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ServiceAccounts(self):
        return self._ServiceAccounts

    @ServiceAccounts.setter
    def ServiceAccounts(self, ServiceAccounts):
        self._ServiceAccounts = ServiceAccounts

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
        if params.get("ServiceAccounts") is not None:
            self._ServiceAccounts = []
            for item in params.get("ServiceAccounts"):
                obj = ServiceAccount()
                obj._deserialize(item)
                self._ServiceAccounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionRequest(AbstractModel):
    """DescribeTagRetentionExecution request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _RetentionId: Rule ID
        :type RetentionId: int
        :param _Limit: `PageSize` for pagination
        :type Limit: int
        :param _Offset: Page offset
        :type Offset: int
        """
        self._RegistryId = None
        self._RetentionId = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionResponse(AbstractModel):
    """DescribeTagRetentionExecution response structure.

    """

    def __init__(self):
        r"""
        :param _RetentionExecutionList: List of tag retention execution records
        :type RetentionExecutionList: list of RetentionExecution
        :param _TotalCount: Total number of tag retention execution records
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RetentionExecutionList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionExecutionList(self):
        return self._RetentionExecutionList

    @RetentionExecutionList.setter
    def RetentionExecutionList(self, RetentionExecutionList):
        self._RetentionExecutionList = RetentionExecutionList

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
        if params.get("RetentionExecutionList") is not None:
            self._RetentionExecutionList = []
            for item in params.get("RetentionExecutionList"):
                obj = RetentionExecution()
                obj._deserialize(item)
                self._RetentionExecutionList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionTaskRequest(AbstractModel):
    """DescribeTagRetentionExecutionTask request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _RetentionId: Rule ID
        :type RetentionId: int
        :param _ExecutionId: Rule execution ID
        :type ExecutionId: int
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: `PageSize` for pagination
        :type Limit: int
        """
        self._RegistryId = None
        self._RetentionId = None
        self._ExecutionId = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

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


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RetentionId = params.get("RetentionId")
        self._ExecutionId = params.get("ExecutionId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionTaskResponse(AbstractModel):
    """DescribeTagRetentionExecutionTask response structure.

    """

    def __init__(self):
        r"""
        :param _RetentionTaskList: List of tag retention execution tasks
        :type RetentionTaskList: list of RetentionTask
        :param _TotalCount: Total number of tag retention execution tasks
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RetentionTaskList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionTaskList(self):
        return self._RetentionTaskList

    @RetentionTaskList.setter
    def RetentionTaskList(self, RetentionTaskList):
        self._RetentionTaskList = RetentionTaskList

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
        if params.get("RetentionTaskList") is not None:
            self._RetentionTaskList = []
            for item in params.get("RetentionTaskList"):
                obj = RetentionTask()
                obj._deserialize(item)
                self._RetentionTaskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTagRetentionRulesRequest(AbstractModel):
    """DescribeTagRetentionRules request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _Limit: `PageSize` for pagination
        :type Limit: int
        :param _Offset: Page offset
        :type Offset: int
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionRulesResponse(AbstractModel):
    """DescribeTagRetentionRules response structure.

    """

    def __init__(self):
        r"""
        :param _RetentionPolicyList: List of tag retention policies
        :type RetentionPolicyList: list of RetentionPolicy
        :param _TotalCount: Total number of tag retention policies
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RetentionPolicyList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RetentionPolicyList(self):
        return self._RetentionPolicyList

    @RetentionPolicyList.setter
    def RetentionPolicyList(self, RetentionPolicyList):
        self._RetentionPolicyList = RetentionPolicyList

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
        if params.get("RetentionPolicyList") is not None:
            self._RetentionPolicyList = []
            for item in params.get("RetentionPolicyList"):
                obj = RetentionPolicy()
                obj._deserialize(item)
                self._RetentionPolicyList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Id: Trigger ID
        :type Id: int
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        """
        self._RegistryId = None
        self._Namespace = None
        self._Id = None
        self._Limit = None
        self._Offset = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Namespace = params.get("Namespace")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Logs: List of logs
        :type Logs: list of WebhookTriggerLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Logs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Logs(self):
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self._Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self._Logs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Namespace: Namespace
        :type Namespace: str
        """
        self._RegistryId = None
        self._Limit = None
        self._Offset = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of triggers
        :type TotalCount: int
        :param _Triggers: List of triggers
        :type Triggers: list of WebhookTrigger
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Triggers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self._Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self._Triggers.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadHelmChartRequest(AbstractModel):
    """DownloadHelmChart request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _ChartName: Helm chart name
        :type ChartName: str
        :param _ChartVersion: Helm chart version
        :type ChartVersion: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._ChartName = None
        self._ChartVersion = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def ChartName(self):
        return self._ChartName

    @ChartName.setter
    def ChartName(self, ChartName):
        self._ChartName = ChartName

    @property
    def ChartVersion(self):
        return self._ChartVersion

    @ChartVersion.setter
    def ChartVersion(self, ChartVersion):
        self._ChartVersion = ChartVersion


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._ChartName = params.get("ChartName")
        self._ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadHelmChartResponse(AbstractModel):
    """DownloadHelmChart response structure.

    """

    def __init__(self):
        r"""
        :param _TmpToken: Temporary token
        :type TmpToken: str
        :param _TmpSecretId: Temporary `secretId`
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary `secretKey`
        :type TmpSecretKey: str
        :param _Bucket: Bucket information
        :type Bucket: str
        :param _Region: Instance ID
        :type Region: str
        :param _Path: Chart information
        :type Path: str
        :param _StartTime: Start timestamp
        :type StartTime: int
        :param _ExpiredTime: Token expiration timestamp
        :type ExpiredTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TmpToken = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Bucket = None
        self._Region = None
        self._Path = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def TmpToken(self):
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TmpToken = params.get("TmpToken")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Path = params.get("Path")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param _Name: Attribute name. If more than one filter exists, the logical relationship between these filters is `AND`.
        :type Name: str
        :param _Values: Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GCJobInfo(AbstractModel):
    """GC execution information

    """

    def __init__(self):
        r"""
        :param _ID: Job ID
        :type ID: int
        :param _JobStatus: Job status
        :type JobStatus: str
        :param _CreationTime: Creation time
        :type CreationTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Schedule: Scheduling information
        :type Schedule: :class:`tencentcloud.tcr.v20190924.models.Schedule`
        """
        self._ID = None
        self._JobStatus = None
        self._CreationTime = None
        self._UpdateTime = None
        self._Schedule = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Schedule(self):
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._JobStatus = params.get("JobStatus")
        self._CreationTime = params.get("CreationTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Schedule") is not None:
            self._Schedule = Schedule()
            self._Schedule._deserialize(params.get("Schedule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        r"""
        :param _Key: Header Key
        :type Key: str
        :param _Values: Header Values
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImmutableTagRule(AbstractModel):
    """Tag immutability rule

    """

    def __init__(self):
        r"""
        :param _RepositoryPattern: Repository matching rule
        :type RepositoryPattern: str
        :param _TagPattern: Tag matching rule
        :type TagPattern: str
        :param _RepositoryDecoration: repoMatches or repoExcludes
        :type RepositoryDecoration: str
        :param _TagDecoration: matches or excludes
        :type TagDecoration: str
        :param _Disabled: Disabling rule
        :type Disabled: bool
        :param _RuleId: Rule ID
        :type RuleId: int
        :param _NsName: Namespace
        :type NsName: str
        """
        self._RepositoryPattern = None
        self._TagPattern = None
        self._RepositoryDecoration = None
        self._TagDecoration = None
        self._Disabled = None
        self._RuleId = None
        self._NsName = None

    @property
    def RepositoryPattern(self):
        return self._RepositoryPattern

    @RepositoryPattern.setter
    def RepositoryPattern(self, RepositoryPattern):
        self._RepositoryPattern = RepositoryPattern

    @property
    def TagPattern(self):
        return self._TagPattern

    @TagPattern.setter
    def TagPattern(self, TagPattern):
        self._TagPattern = TagPattern

    @property
    def RepositoryDecoration(self):
        return self._RepositoryDecoration

    @RepositoryDecoration.setter
    def RepositoryDecoration(self, RepositoryDecoration):
        self._RepositoryDecoration = RepositoryDecoration

    @property
    def TagDecoration(self):
        return self._TagDecoration

    @TagDecoration.setter
    def TagDecoration(self, TagDecoration):
        self._TagDecoration = TagDecoration

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def NsName(self):
        return self._NsName

    @NsName.setter
    def NsName(self, NsName):
        self._NsName = NsName


    def _deserialize(self, params):
        self._RepositoryPattern = params.get("RepositoryPattern")
        self._TagPattern = params.get("TagPattern")
        self._RepositoryDecoration = params.get("RepositoryDecoration")
        self._TagDecoration = params.get("TagDecoration")
        self._Disabled = params.get("Disabled")
        self._RuleId = params.get("RuleId")
        self._NsName = params.get("NsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueString(AbstractModel):
    """String key-value pair of a common parameter

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointRequest(AbstractModel):
    """ManageExternalEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Operation: Operation. Valid values: Create, Delete.
        :type Operation: str
        """
        self._RegistryId = None
        self._Operation = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointResponse(AbstractModel):
    """ManageExternalEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ManageInternalEndpointRequest(AbstractModel):
    """ManageInternalEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Operation: Create/Delete
        :type Operation: str
        :param _VpcId: ID of the VPC to be connected to
        :type VpcId: str
        :param _SubnetId: ID of the subnet to be connected to
        :type SubnetId: str
        :param _RegionId: ID of the requested region, which is used as the region of the replica instance
        :type RegionId: int
        :param _RegionName: Name of the requested region, which is used as the region of the replica instance
        :type RegionName: str
        """
        self._RegistryId = None
        self._Operation = None
        self._VpcId = None
        self._SubnetId = None
        self._RegionId = None
        self._RegionName = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Operation = params.get("Operation")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageInternalEndpointResponse(AbstractModel):
    """ManageInternalEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ManageReplicationRequest(AbstractModel):
    """ManageReplication request structure.

    """

    def __init__(self):
        r"""
        :param _SourceRegistryId: Source instance ID
        :type SourceRegistryId: str
        :param _DestinationRegistryId: Destination instance ID
        :type DestinationRegistryId: str
        :param _Rule: Synchronization rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`
        :param _Description: Rule description
        :type Description: str
        :param _DestinationRegionId: Region ID of the destination instance. For example, `1` represents Guangzhou
        :type DestinationRegionId: int
        :param _PeerReplicationOption: Configuration of the synchronization rule
        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`
        """
        self._SourceRegistryId = None
        self._DestinationRegistryId = None
        self._Rule = None
        self._Description = None
        self._DestinationRegionId = None
        self._PeerReplicationOption = None

    @property
    def SourceRegistryId(self):
        return self._SourceRegistryId

    @SourceRegistryId.setter
    def SourceRegistryId(self, SourceRegistryId):
        self._SourceRegistryId = SourceRegistryId

    @property
    def DestinationRegistryId(self):
        return self._DestinationRegistryId

    @DestinationRegistryId.setter
    def DestinationRegistryId(self, DestinationRegistryId):
        self._DestinationRegistryId = DestinationRegistryId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DestinationRegionId(self):
        return self._DestinationRegionId

    @DestinationRegionId.setter
    def DestinationRegionId(self, DestinationRegionId):
        self._DestinationRegionId = DestinationRegionId

    @property
    def PeerReplicationOption(self):
        return self._PeerReplicationOption

    @PeerReplicationOption.setter
    def PeerReplicationOption(self, PeerReplicationOption):
        self._PeerReplicationOption = PeerReplicationOption


    def _deserialize(self, params):
        self._SourceRegistryId = params.get("SourceRegistryId")
        self._DestinationRegistryId = params.get("DestinationRegistryId")
        if params.get("Rule") is not None:
            self._Rule = ReplicationRule()
            self._Rule._deserialize(params.get("Rule"))
        self._Description = params.get("Description")
        self._DestinationRegionId = params.get("DestinationRegionId")
        if params.get("PeerReplicationOption") is not None:
            self._PeerReplicationOption = PeerReplicationOption()
            self._PeerReplicationOption._deserialize(params.get("PeerReplicationOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationResponse(AbstractModel):
    """ManageReplication response structure.

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


class ModifyCustomAccountRequest(AbstractModel):
    """ModifyCustomAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Name: Custom account name
        :type Name: str
        :param _Description: Custom account description
        :type Description: str
        :param _Duration: Validity in days starting from the current day. It takes a higher priority than `ExpiresAt`.
        :type Duration: int
        :param _ExpiresAt: Expiry time of the custom account (timestamp)
        :type ExpiresAt: int
        :param _Disable: Whether to disable the custom account
        :type Disable: bool
        :param _Permissions: Policy list
        :type Permissions: list of Permission
        """
        self._RegistryId = None
        self._Name = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None
        self._Permissions = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomAccountResponse(AbstractModel):
    """ModifyCustomAccount response structure.

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


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace
        :type NamespaceName: str
        :param _RuleId: Rule ID
        :type RuleId: int
        :param _Rule: Rule
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RuleId = None
        self._Rule = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RuleId = params.get("RuleId")
        if params.get("Rule") is not None:
            self._Rule = ImmutableTagRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImmutableTagRulesResponse(AbstractModel):
    """ModifyImmutableTagRules response structure.

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


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RegistryType: Instance edition
Basic: `basic`
Standard: `standard`
Premium: `premium`
        :type RegistryType: str
        :param _DeletionProtection: Whether to enable deletion protection. It defaults to `false`. 
        :type DeletionProtection: bool
        """
        self._RegistryId = None
        self._RegistryType = None
        self._DeletionProtection = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RegistryType = params.get("RegistryType")
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

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


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken request structure.

    """

    def __init__(self):
        r"""
        :param _TokenId: ID of the long-term access credential of the instance
        :type TokenId: str
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Enable: Whether to enable the long-term access credential of the instance
        :type Enable: bool
        :param _Desc: Access credential description
        :type Desc: str
        :param _ModifyFlag: Valid values: 1: Modify the description; 2: Enable/Disable. Default value: 2.
        :type ModifyFlag: int
        """
        self._TokenId = None
        self._RegistryId = None
        self._Enable = None
        self._Desc = None
        self._ModifyFlag = None

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ModifyFlag(self):
        return self._ModifyFlag

    @ModifyFlag.setter
    def ModifyFlag(self, ModifyFlag):
        self._ModifyFlag = ModifyFlag


    def _deserialize(self, params):
        self._TokenId = params.get("TokenId")
        self._RegistryId = params.get("RegistryId")
        self._Enable = params.get("Enable")
        self._Desc = params.get("Desc")
        self._ModifyFlag = params.get("ModifyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken response structure.

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


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _IsPublic: Access level. Valid values: True: Public; False: Private.
        :type IsPublic: bool
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._IsPublic = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._IsPublic = params.get("IsPublic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace response structure.

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


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RepositoryName: Image repository name
        :type RepositoryName: str
        :param _BriefDescription: Brief repository description
        :type BriefDescription: str
        :param _Description: Detailed repository description
        :type Description: str
        """
        self._RegistryId = None
        self._NamespaceName = None
        self._RepositoryName = None
        self._BriefDescription = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RepositoryName(self):
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceName = params.get("NamespaceName")
        self._RepositoryName = params.get("RepositoryName")
        self._BriefDescription = params.get("BriefDescription")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository response structure.

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


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _PolicyIndex: PolicyId
        :type PolicyIndex: int
        :param _CidrBlock: Allowed IP, such as `192.168.0.0/24`
        :type CidrBlock: str
        :param _Description: Remarks
        :type Description: str
        """
        self._RegistryId = None
        self._PolicyIndex = None
        self._CidrBlock = None
        self._Description = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._PolicyIndex = params.get("PolicyIndex")
        self._CidrBlock = params.get("CidrBlock")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ModifyServiceAccountRequest(AbstractModel):
    """ModifyServiceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Name: Service account name
        :type Name: str
        :param _Description: Service account description
        :type Description: str
        :param _Duration: Validity in days starting from the current day, It takes a higher priority than `ExpiresAt`.
        :type Duration: int
        :param _ExpiresAt: Expiry time (timestamp, in milliseconds)
        :type ExpiresAt: int
        :param _Disable: Whether to disable the service account
        :type Disable: bool
        :param _Permissions: Policy list
        :type Permissions: list of Permission
        """
        self._RegistryId = None
        self._Name = None
        self._Description = None
        self._Duration = None
        self._ExpiresAt = None
        self._Disable = None
        self._Permissions = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Duration = params.get("Duration")
        self._ExpiresAt = params.get("ExpiresAt")
        self._Disable = params.get("Disable")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceAccountResponse(AbstractModel):
    """ModifyServiceAccount response structure.

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


class ModifyTagRetentionRuleRequest(AbstractModel):
    """ModifyTagRetentionRule request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Primary instance ID
        :type RegistryId: str
        :param _NamespaceId: ID of the original namespace
        :type NamespaceId: int
        :param _RetentionRule: Retention policy
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param _CronSetting: Original execution cycle
        :type CronSetting: str
        :param _RetentionId: Rule ID
        :type RetentionId: int
        :param _Disabled: Whether to disable the rule
        :type Disabled: bool
        """
        self._RegistryId = None
        self._NamespaceId = None
        self._RetentionRule = None
        self._CronSetting = None
        self._RetentionId = None
        self._Disabled = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RetentionRule(self):
        return self._RetentionRule

    @RetentionRule.setter
    def RetentionRule(self, RetentionRule):
        self._RetentionRule = RetentionRule

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self._RetentionRule = RetentionRule()
            self._RetentionRule._deserialize(params.get("RetentionRule"))
        self._CronSetting = params.get("CronSetting")
        self._RetentionId = params.get("RetentionId")
        self._Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagRetentionRuleResponse(AbstractModel):
    """ModifyTagRetentionRule response structure.

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


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Trigger: Trigger parameter
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param _Namespace: Namespace
        :type Namespace: str
        """
        self._RegistryId = None
        self._Trigger = None
        self._Namespace = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self._Trigger = WebhookTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger response structure.

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


class PeerReplicationOption(AbstractModel):
    """Parameters for cross-account synchronization

    """

    def __init__(self):
        r"""
        :param _PeerRegistryUin: UIN of the destination instance
        :type PeerRegistryUin: str
        :param _PeerRegistryToken: Permanent access Token for the destination instance
        :type PeerRegistryToken: str
        :param _EnablePeerReplication: Whether to enable cross-account synchronization
        :type EnablePeerReplication: bool
        """
        self._PeerRegistryUin = None
        self._PeerRegistryToken = None
        self._EnablePeerReplication = None

    @property
    def PeerRegistryUin(self):
        return self._PeerRegistryUin

    @PeerRegistryUin.setter
    def PeerRegistryUin(self, PeerRegistryUin):
        self._PeerRegistryUin = PeerRegistryUin

    @property
    def PeerRegistryToken(self):
        return self._PeerRegistryToken

    @PeerRegistryToken.setter
    def PeerRegistryToken(self, PeerRegistryToken):
        self._PeerRegistryToken = PeerRegistryToken

    @property
    def EnablePeerReplication(self):
        return self._EnablePeerReplication

    @EnablePeerReplication.setter
    def EnablePeerReplication(self, EnablePeerReplication):
        self._EnablePeerReplication = EnablePeerReplication


    def _deserialize(self, params):
        self._PeerRegistryUin = params.get("PeerRegistryUin")
        self._PeerRegistryToken = params.get("PeerRegistryToken")
        self._EnablePeerReplication = params.get("EnablePeerReplication")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Permission(AbstractModel):
    """Policy

    """

    def __init__(self):
        r"""
        :param _Resource: Resource path. Valid value: `Namespace`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Resource: str
        :param _Actions: Action. Valid values: `tcr:PushRepository`, `tcr:PullRepository`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Actions: list of str
        """
        self._Resource = None
        self._Actions = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _Alias: gz
        :type Alias: str
        :param _RegionId: 1
        :type RegionId: int
        :param _RegionName: ap-guangzhou
        :type RegionName: str
        :param _Status: alluser
        :type Status: str
        :param _Remark: remark
        :type Remark: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _UpdatedAt: Update time
        :type UpdatedAt: str
        :param _Id: id
        :type Id: int
        """
        self._Alias = None
        self._RegionId = None
        self._RegionName = None
        self._Status = None
        self._Remark = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Id = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Registry(AbstractModel):
    """Instance information structure

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RegistryName: Instance name
        :type RegistryName: str
        :param _RegistryType: Instance specification
        :type RegistryType: str
        :param _Status: Instance status
        :type Status: str
        :param _PublicDomain: Public access URL of the instance
        :type PublicDomain: str
        :param _CreatedAt: Instance creation time
        :type CreatedAt: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _EnableAnonymous: Whether to enable anonymity
        :type EnableAnonymous: bool
        :param _TokenValidTime: Token validity period
        :type TokenValidTime: int
        :param _InternalEndpoint: Internal access address of the instance
        :type InternalEndpoint: str
        :param _TagSpecification: Cloud tag of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _ExpiredAt: Instance expiration time (for prepayment)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredAt: str
        :param _PayMod: Instance billing mode. Valid values: 0: Postpayment; 1: Prepayment.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMod: int
        :param _RenewFlag: Prepayment renewal flag. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        """
        self._RegistryId = None
        self._RegistryName = None
        self._RegistryType = None
        self._Status = None
        self._PublicDomain = None
        self._CreatedAt = None
        self._RegionName = None
        self._RegionId = None
        self._EnableAnonymous = None
        self._TokenValidTime = None
        self._InternalEndpoint = None
        self._TagSpecification = None
        self._ExpiredAt = None
        self._PayMod = None
        self._RenewFlag = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryName(self):
        return self._RegistryName

    @RegistryName.setter
    def RegistryName(self, RegistryName):
        self._RegistryName = RegistryName

    @property
    def RegistryType(self):
        return self._RegistryType

    @RegistryType.setter
    def RegistryType(self, RegistryType):
        self._RegistryType = RegistryType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublicDomain(self):
        return self._PublicDomain

    @PublicDomain.setter
    def PublicDomain(self, PublicDomain):
        self._PublicDomain = PublicDomain

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def EnableAnonymous(self):
        return self._EnableAnonymous

    @EnableAnonymous.setter
    def EnableAnonymous(self, EnableAnonymous):
        self._EnableAnonymous = EnableAnonymous

    @property
    def TokenValidTime(self):
        return self._TokenValidTime

    @TokenValidTime.setter
    def TokenValidTime(self, TokenValidTime):
        self._TokenValidTime = TokenValidTime

    @property
    def InternalEndpoint(self):
        return self._InternalEndpoint

    @InternalEndpoint.setter
    def InternalEndpoint(self, InternalEndpoint):
        self._InternalEndpoint = InternalEndpoint

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def ExpiredAt(self):
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def PayMod(self):
        return self._PayMod

    @PayMod.setter
    def PayMod(self, PayMod):
        self._PayMod = PayMod

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RegistryName = params.get("RegistryName")
        self._RegistryType = params.get("RegistryType")
        self._Status = params.get("Status")
        self._PublicDomain = params.get("PublicDomain")
        self._CreatedAt = params.get("CreatedAt")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._EnableAnonymous = params.get("EnableAnonymous")
        self._TokenValidTime = params.get("TokenValidTime")
        self._InternalEndpoint = params.get("InternalEndpoint")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        self._ExpiredAt = params.get("ExpiredAt")
        self._PayMod = params.get("PayMod")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryChargePrepaid(AbstractModel):
    """Instance prepayment mode

    """

    def __init__(self):
        r"""
        :param _Period: Instance purchase duration in months
        :type Period: int
        :param _RenewFlag: Auto-renewal flag. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
        :type RenewFlag: int
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryCondition(AbstractModel):
    """Instance creation process

    """

    def __init__(self):
        r"""
        :param _Type: Instance creation process type
        :type Type: str
        :param _Status: Instance creation process status
        :type Status: str
        :param _Reason: Reasons for transiting to the process
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self._Type = None
        self._Status = None
        self._Reason = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryStatus(AbstractModel):
    """Instance status

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _Status: Instance status
        :type Status: str
        :param _Conditions: Additional status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conditions: list of RegistryCondition
        """
        self._RegistryId = None
        self._Status = None
        self._Conditions = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Status = params.get("Status")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Instance ID
        :type RegistryId: str
        :param _RegistryChargePrepaid: Auto-renewal flag and purchase duration in months for prepayment. Valid values: 0: Manual renewal; 1: Auto-renewal; 2: No renewal and no notification.
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param _Flag: Valid values: 0: renewal; 1: change from pay-as-you-go to monthly subscription billing
        :type Flag: int
        """
        self._RegistryId = None
        self._RegistryChargePrepaid = None
        self._Flag = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RegistryChargePrepaid(self):
        return self._RegistryChargePrepaid

    @RegistryChargePrepaid.setter
    def RegistryChargePrepaid(self, RegistryChargePrepaid):
        self._RegistryChargePrepaid = RegistryChargePrepaid

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        if params.get("RegistryChargePrepaid") is not None:
            self._RegistryChargePrepaid = RegistryChargePrepaid()
            self._RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RegistryId: Enterprise Edition instance ID
        :type RegistryId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegistryId = None
        self._RequestId = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RequestId = params.get("RequestId")


class ReplicationFilter(AbstractModel):
    """Synchronization rule filter

    """

    def __init__(self):
        r"""
        :param _Type: Type (`name`, `tag` and `resource`)
        :type Type: str
        :param _Value: It is left blank by default
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationLog(AbstractModel):
    """Synchronization log

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _Source: Path of the source resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Source: str
        :param _Destination: Path of the destination resource
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Destination: str
        :param _Status: Synchronization status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        :param _StartTime: Start time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: End time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self._ResourceType = None
        self._Source = None
        self._Destination = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Destination(self):
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._Source = params.get("Source")
        self._Destination = params.get("Destination")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRegistry(AbstractModel):
    """ID of Enterprise Registry replication instance

    """

    def __init__(self):
        r"""
        :param _RegistryId: Master instance ID
        :type RegistryId: str
        :param _ReplicationRegistryId: Replication instance ID
        :type ReplicationRegistryId: str
        :param _ReplicationRegionId: Region ID of the replication instance
        :type ReplicationRegionId: int
        :param _ReplicationRegionName: Region name of the replication instance
        :type ReplicationRegionName: str
        :param _Status: Status of the replication instance
        :type Status: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        """
        self._RegistryId = None
        self._ReplicationRegistryId = None
        self._ReplicationRegionId = None
        self._ReplicationRegionName = None
        self._Status = None
        self._CreatedAt = None

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def ReplicationRegistryId(self):
        return self._ReplicationRegistryId

    @ReplicationRegistryId.setter
    def ReplicationRegistryId(self, ReplicationRegistryId):
        self._ReplicationRegistryId = ReplicationRegistryId

    @property
    def ReplicationRegionId(self):
        return self._ReplicationRegionId

    @ReplicationRegionId.setter
    def ReplicationRegionId(self, ReplicationRegionId):
        self._ReplicationRegionId = ReplicationRegionId

    @property
    def ReplicationRegionName(self):
        return self._ReplicationRegionName

    @ReplicationRegionName.setter
    def ReplicationRegionName(self, ReplicationRegionName):
        self._ReplicationRegionName = ReplicationRegionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._ReplicationRegistryId = params.get("ReplicationRegistryId")
        self._ReplicationRegionId = params.get("ReplicationRegionId")
        self._ReplicationRegionName = params.get("ReplicationRegionName")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRule(AbstractModel):
    """Synchronization rule

    """

    def __init__(self):
        r"""
        :param _Name: Name of synchronization rule
        :type Name: str
        :param _DestNamespace: Destination namespace
        :type DestNamespace: str
        :param _Override: Whether to override
        :type Override: bool
        :param _Filters: Synchronization filters
        :type Filters: list of ReplicationFilter
        """
        self._Name = None
        self._DestNamespace = None
        self._Override = None
        self._Filters = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DestNamespace(self):
        return self._DestNamespace

    @DestNamespace.setter
    def DestNamespace(self, DestNamespace):
        self._DestNamespace = DestNamespace

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DestNamespace = params.get("DestNamespace")
        self._Override = params.get("Override")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ReplicationFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionExecution(AbstractModel):
    """Tag retention rule execution

    """

    def __init__(self):
        r"""
        :param _ExecutionId: Execution ID
        :type ExecutionId: int
        :param _RetentionId: Rule ID
        :type RetentionId: int
        :param _StartTime: Execution start time
        :type StartTime: str
        :param _EndTime: Execution end time
        :type EndTime: str
        :param _Status: Execution status. Valid values: Failed, Succeed, Stopped, InProgress.
        :type Status: str
        """
        self._ExecutionId = None
        self._RetentionId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ExecutionId = params.get("ExecutionId")
        self._RetentionId = params.get("RetentionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionPolicy(AbstractModel):
    """Tag retention policy

    """

    def __init__(self):
        r"""
        :param _RetentionId: Tag retention policy ID
        :type RetentionId: int
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _RetentionRuleList: List of rules
        :type RetentionRuleList: list of RetentionRule
        :param _CronSetting: Regular execution mode
        :type CronSetting: str
        :param _Disabled: Whether to enable the rule
        :type Disabled: bool
        :param _NextExecutionTime: The execution time of the next task based on the current time and `cronSetting`, which is for reference only
        :type NextExecutionTime: str
        """
        self._RetentionId = None
        self._NamespaceName = None
        self._RetentionRuleList = None
        self._CronSetting = None
        self._Disabled = None
        self._NextExecutionTime = None

    @property
    def RetentionId(self):
        return self._RetentionId

    @RetentionId.setter
    def RetentionId(self, RetentionId):
        self._RetentionId = RetentionId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def RetentionRuleList(self):
        return self._RetentionRuleList

    @RetentionRuleList.setter
    def RetentionRuleList(self, RetentionRuleList):
        self._RetentionRuleList = RetentionRuleList

    @property
    def CronSetting(self):
        return self._CronSetting

    @CronSetting.setter
    def CronSetting(self, CronSetting):
        self._CronSetting = CronSetting

    @property
    def Disabled(self):
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def NextExecutionTime(self):
        return self._NextExecutionTime

    @NextExecutionTime.setter
    def NextExecutionTime(self, NextExecutionTime):
        self._NextExecutionTime = NextExecutionTime


    def _deserialize(self, params):
        self._RetentionId = params.get("RetentionId")
        self._NamespaceName = params.get("NamespaceName")
        if params.get("RetentionRuleList") is not None:
            self._RetentionRuleList = []
            for item in params.get("RetentionRuleList"):
                obj = RetentionRule()
                obj._deserialize(item)
                self._RetentionRuleList.append(obj)
        self._CronSetting = params.get("CronSetting")
        self._Disabled = params.get("Disabled")
        self._NextExecutionTime = params.get("NextExecutionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionRule(AbstractModel):
    """Tag retention rule

    """

    def __init__(self):
        r"""
        :param _Key: Supported policy. Valid values: latestPushedK: Retain the latest specified number of pushed tags; nDaysSinceLastPush: Retain the tags pushed in the past specified number of days.
        :type Key: str
        :param _Value: Rule value
        :type Value: int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionTask(AbstractModel):
    """Rule of tag retention task execution

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _ExecutionId: Rule execution ID
        :type ExecutionId: int
        :param _StartTime: Task start time
        :type StartTime: str
        :param _EndTime: Task end time
        :type EndTime: str
        :param _Status: Task execution status. Valid values: Failed, Succeed, Stopped, InProgress.
        :type Status: str
        :param _Total: Total number of tags
        :type Total: int
        :param _Retained: Number of retained tags
        :type Retained: int
        :param _Repository: Application repository
        :type Repository: str
        """
        self._TaskId = None
        self._ExecutionId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Total = None
        self._Retained = None
        self._Repository = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ExecutionId(self):
        return self._ExecutionId

    @ExecutionId.setter
    def ExecutionId(self, ExecutionId):
        self._ExecutionId = ExecutionId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Retained(self):
        return self._Retained

    @Retained.setter
    def Retained(self, Retained):
        self._Retained = Retained

    @property
    def Repository(self):
        return self._Repository

    @Repository.setter
    def Repository(self, Repository):
        self._Repository = Repository


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ExecutionId = params.get("ExecutionId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Total = params.get("Total")
        self._Retained = params.get("Retained")
        self._Repository = params.get("Repository")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Schedule(AbstractModel):
    """Job scheduling information

    """

    def __init__(self):
        r"""
        :param _Type: Type. Valid values: Hourly, Daily, Weekly, Custom, Manual, Dryrun, None.
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """Security policy

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: Policy index
        :type PolicyIndex: int
        :param _Description: Remarks
        :type Description: str
        :param _CidrBlock: The public network IP address of the access source
        :type CidrBlock: str
        :param _PolicyVersion: The version of the security policy
        :type PolicyVersion: str
        """
        self._PolicyIndex = None
        self._Description = None
        self._CidrBlock = None
        self._PolicyVersion = None

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        self._Description = params.get("Description")
        self._CidrBlock = params.get("CidrBlock")
        self._PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAccount(AbstractModel):
    """Service account

    """

    def __init__(self):
        r"""
        :param _Name: Service account name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param _Description: Description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _Disable: Whether to disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Disable: bool
        :param _ExpiresAt: Expiry time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExpiresAt: int
        :param _CreateTime: Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Permissions: Policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Permissions: list of Permission
        """
        self._Name = None
        self._Description = None
        self._Disable = None
        self._ExpiresAt = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Permissions = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ExpiresAt(self):
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Disable = params.get("Disable")
        self._ExpiresAt = params.get("ExpiresAt")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Cloud tag

    """

    def __init__(self):
        r"""
        :param _Key: Cloud tag key
        :type Key: str
        :param _Value: Cloud tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """Cloud tag

    """

    def __init__(self):
        r"""
        :param _ResourceType: Default value: instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _Tags: Cloud tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
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
        


class TaskDetail(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param _TaskName: Task
        :type TaskName: str
        :param _TaskUUID: Task UUID
        :type TaskUUID: str
        :param _TaskStatus: Task status
        :type TaskStatus: str
        :param _TaskMessage: Task details
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TaskMessage: str
        :param _CreatedTime: Start time of the task
        :type CreatedTime: str
        :param _FinishedTime: End time of the task
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FinishedTime: str
        """
        self._TaskName = None
        self._TaskUUID = None
        self._TaskStatus = None
        self._TaskMessage = None
        self._CreatedTime = None
        self._FinishedTime = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskUUID(self):
        return self._TaskUUID

    @TaskUUID.setter
    def TaskUUID(self, TaskUUID):
        self._TaskUUID = TaskUUID

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskUUID = params.get("TaskUUID")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskMessage = params.get("TaskMessage")
        self._CreatedTime = params.get("CreatedTime")
        self._FinishedTime = params.get("FinishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrImageInfo(AbstractModel):
    """Image information

    """

    def __init__(self):
        r"""
        :param _Digest: Hash value
        :type Digest: str
        :param _Size: Image size in bytes
        :type Size: int
        :param _ImageVersion: Tag name
        :type ImageVersion: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Kind: Artifact type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kind: str
        :param _KmsSignature: KMS signature information
Note: This field may return null, indicating that no valid values can be obtained.
        :type KmsSignature: str
        """
        self._Digest = None
        self._Size = None
        self._ImageVersion = None
        self._UpdateTime = None
        self._Kind = None
        self._KmsSignature = None

    @property
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def ImageVersion(self):
        return self._ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, ImageVersion):
        self._ImageVersion = ImageVersion

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def KmsSignature(self):
        return self._KmsSignature

    @KmsSignature.setter
    def KmsSignature(self, KmsSignature):
        self._KmsSignature = KmsSignature


    def _deserialize(self, params):
        self._Digest = params.get("Digest")
        self._Size = params.get("Size")
        self._ImageVersion = params.get("ImageVersion")
        self._UpdateTime = params.get("UpdateTime")
        self._Kind = params.get("Kind")
        self._KmsSignature = params.get("KmsSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrInstanceToken(AbstractModel):
    """Instance login token

    """

    def __init__(self):
        r"""
        :param _Id: Token ID
        :type Id: str
        :param _Desc: Token description
        :type Desc: str
        :param _RegistryId: ID of the instance of the token
        :type RegistryId: str
        :param _Enabled: Token status
        :type Enabled: bool
        :param _CreatedAt: Token creation time
        :type CreatedAt: str
        :param _ExpiredAt: Token expiration timestamp
        :type ExpiredAt: int
        """
        self._Id = None
        self._Desc = None
        self._RegistryId = None
        self._Enabled = None
        self._CreatedAt = None
        self._ExpiredAt = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ExpiredAt(self):
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Desc = params.get("Desc")
        self._RegistryId = params.get("RegistryId")
        self._Enabled = params.get("Enabled")
        self._CreatedAt = params.get("CreatedAt")
        self._ExpiredAt = params.get("ExpiredAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrNamespaceInfo(AbstractModel):
    """TCR namespace description

    """

    def __init__(self):
        r"""
        :param _Name: Namespace name
        :type Name: str
        :param _CreationTime: Creation time
        :type CreationTime: str
        :param _Public: Access level
        :type Public: bool
        :param _NamespaceId: Namespace ID
        :type NamespaceId: int
        :param _TagSpecification: Cloud tag of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param _Metadata: Namespace metadata
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metadata: list of KeyValueString
        """
        self._Name = None
        self._CreationTime = None
        self._Public = None
        self._NamespaceId = None
        self._TagSpecification = None
        self._Metadata = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreationTime = params.get("CreationTime")
        self._Public = params.get("Public")
        self._NamespaceId = params.get("NamespaceId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = KeyValueString()
                obj._deserialize(item)
                self._Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrRepositoryInfo(AbstractModel):
    """TCR image repository information

    """

    def __init__(self):
        r"""
        :param _Name: Repository name
        :type Name: str
        :param _Namespace: Namespace name
        :type Namespace: str
        :param _CreationTime: Creation time, such as `2006-01-02 15:04:05.999999999 -0700 MST`
        :type CreationTime: str
        :param _Public: Whether to make public
        :type Public: bool
        :param _Description: Detailed repository description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _BriefDescription: Brief description
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefDescription: str
        :param _UpdateTime: Update time, such as `2006-01-02 15:04:05.999999999 -0700 MST`
        :type UpdateTime: str
        """
        self._Name = None
        self._Namespace = None
        self._CreationTime = None
        self._Public = None
        self._Description = None
        self._BriefDescription = None
        self._UpdateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Public(self):
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def BriefDescription(self):
        return self._BriefDescription

    @BriefDescription.setter
    def BriefDescription(self, BriefDescription):
        self._BriefDescription = BriefDescription

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._CreationTime = params.get("CreationTime")
        self._Public = params.get("Public")
        self._Description = params.get("Description")
        self._BriefDescription = params.get("BriefDescription")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTarget(AbstractModel):
    """Trigger target

    """

    def __init__(self):
        r"""
        :param _Address: Target address
        :type Address: str
        :param _Headers: Custom headers
        :type Headers: list of Header
        """
        self._Address = None
        self._Headers = None

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Address = params.get("Address")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTrigger(AbstractModel):
    """Webhook trigger

    """

    def __init__(self):
        r"""
        :param _Name: Trigger name
        :type Name: str
        :param _Targets: Trigger target
        :type Targets: list of WebhookTarget
        :param _EventTypes: Action to be triggered
        :type EventTypes: list of str
        :param _Condition: Trigger rule
        :type Condition: str
        :param _Enabled: Whether to enable the trigger
        :type Enabled: bool
        :param _Id: Trigger ID
        :type Id: int
        :param _Description: Trigger description
        :type Description: str
        :param _NamespaceId: ID of the namespace of the trigger
        :type NamespaceId: int
        """
        self._Name = None
        self._Targets = None
        self._EventTypes = None
        self._Condition = None
        self._Enabled = None
        self._Id = None
        self._Description = None
        self._NamespaceId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EventTypes(self):
        return self._EventTypes

    @EventTypes.setter
    def EventTypes(self, EventTypes):
        self._EventTypes = EventTypes

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._EventTypes = params.get("EventTypes")
        self._Condition = params.get("Condition")
        self._Enabled = params.get("Enabled")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTriggerLog(AbstractModel):
    """Trigger log

    """

    def __init__(self):
        r"""
        :param _Id: Log ID
        :type Id: int
        :param _TriggerId: Trigger ID
        :type TriggerId: int
        :param _EventType: Event type
        :type EventType: str
        :param _NotifyType: Notification type
        :type NotifyType: str
        :param _Detail: Details
        :type Detail: str
        :param _CreationTime: Creation time
        :type CreationTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Status: Status
        :type Status: str
        """
        self._Id = None
        self._TriggerId = None
        self._EventType = None
        self._NotifyType = None
        self._Detail = None
        self._CreationTime = None
        self._UpdateTime = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TriggerId(self):
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TriggerId = params.get("TriggerId")
        self._EventType = params.get("EventType")
        self._NotifyType = params.get("NotifyType")
        self._Detail = params.get("Detail")
        self._CreationTime = params.get("CreationTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        