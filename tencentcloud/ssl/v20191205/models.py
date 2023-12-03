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


class ApiGatewayInstanceDetail(AbstractModel):
    """Details of an APIGATEWAY instance

    """

    def __init__(self):
        r"""
        :param _ServiceId: The instance ID.
        :type ServiceId: str
        :param _ServiceName: The instance name.
        :type ServiceName: str
        :param _Domain: The domain.
        :type Domain: str
        :param _CertId: The certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Protocol: The protocol.
        :type Protocol: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._Domain = None
        self._CertId = None
        self._Protocol = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiGatewayInstanceList(AbstractModel):
    """Details of APIGATEWAY instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
        :type Region: str
        :param _InstanceList: The list of APIGATEWAY instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param _TotalCount: The total number of APIGATEWAY instances in this region.	
        :type TotalCount: int
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _DvAuthMethod: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation
        :type DvAuthMethod: str
        :param _DomainName: Domain name
        :type DomainName: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _PackageType: Certificate type. Currently, the only supported value is 2, which indicates TrustAsia TLS RSA CA.
        :type PackageType: str
        :param _ContactEmail: Email address
        :type ContactEmail: str
        :param _ContactPhone: Mobile number
        :type ContactPhone: str
        :param _ValidityPeriod: Validity period. The default value is 12 months, which is the only supported value currently.
        :type ValidityPeriod: str
        :param _CsrEncryptAlgo: Encryption algorithm. RSA and ECC are supported.
        :type CsrEncryptAlgo: str
        :param _CsrKeyParameter: Key pair parameters. RSA supports only 2048. ECC supports only prime256v1. When the encryption algorithm is set to ECC, this parameter is mandatory.
        :type CsrKeyParameter: str
        :param _CsrKeyPassword: CSR encryption password
        :type CsrKeyPassword: str
        :param _Alias: Alias
        :type Alias: str
        :param _OldCertificateId: Original certificate ID, which is used to apply for a new certificate.
        :type OldCertificateId: str
        :param _PackageId: Benefit package ID, which is used to expand the free certificate package
        :type PackageId: str
        :param _DeleteDnsAutoRecord: Whether to delete the automatic domain name verification record after issuance, which is no by default. This parameter can be passed in only for domain names of the DNS_AUTO verification type.
        :type DeleteDnsAutoRecord: bool
        """
        self._DvAuthMethod = None
        self._DomainName = None
        self._ProjectId = None
        self._PackageType = None
        self._ContactEmail = None
        self._ContactPhone = None
        self._ValidityPeriod = None
        self._CsrEncryptAlgo = None
        self._CsrKeyParameter = None
        self._CsrKeyPassword = None
        self._Alias = None
        self._OldCertificateId = None
        self._PackageId = None
        self._DeleteDnsAutoRecord = None

    @property
    def DvAuthMethod(self):
        return self._DvAuthMethod

    @DvAuthMethod.setter
    def DvAuthMethod(self, DvAuthMethod):
        self._DvAuthMethod = DvAuthMethod

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPhone(self):
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def CsrEncryptAlgo(self):
        return self._CsrEncryptAlgo

    @CsrEncryptAlgo.setter
    def CsrEncryptAlgo(self, CsrEncryptAlgo):
        self._CsrEncryptAlgo = CsrEncryptAlgo

    @property
    def CsrKeyParameter(self):
        return self._CsrKeyParameter

    @CsrKeyParameter.setter
    def CsrKeyParameter(self, CsrKeyParameter):
        self._CsrKeyParameter = CsrKeyParameter

    @property
    def CsrKeyPassword(self):
        return self._CsrKeyPassword

    @CsrKeyPassword.setter
    def CsrKeyPassword(self, CsrKeyPassword):
        self._CsrKeyPassword = CsrKeyPassword

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeleteDnsAutoRecord(self):
        return self._DeleteDnsAutoRecord

    @DeleteDnsAutoRecord.setter
    def DeleteDnsAutoRecord(self, DeleteDnsAutoRecord):
        self._DeleteDnsAutoRecord = DeleteDnsAutoRecord


    def _deserialize(self, params):
        self._DvAuthMethod = params.get("DvAuthMethod")
        self._DomainName = params.get("DomainName")
        self._ProjectId = params.get("ProjectId")
        self._PackageType = params.get("PackageType")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPhone = params.get("ContactPhone")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self._CsrKeyParameter = params.get("CsrKeyParameter")
        self._CsrKeyPassword = params.get("CsrKeyPassword")
        self._Alias = params.get("Alias")
        self._OldCertificateId = params.get("OldCertificateId")
        self._PackageId = params.get("PackageId")
        self._DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class BatchDeleteCSRRequest(AbstractModel):
    """BatchDeleteCSR request structure.

    """

    def __init__(self):
        r"""
        :param _CSRIds: The IDs of the CSRs to be deleted, 100 IDs at most.
        :type CSRIds: list of int
        """
        self._CSRIds = None

    @property
    def CSRIds(self):
        return self._CSRIds

    @CSRIds.setter
    def CSRIds(self, CSRIds):
        self._CSRIds = CSRIds


    def _deserialize(self, params):
        self._CSRIds = params.get("CSRIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteCSRResponse(AbstractModel):
    """BatchDeleteCSR response structure.

    """

    def __init__(self):
        r"""
        :param _Success: The IDs of the CSRs successfully deleted.
        :type Success: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Success = params.get("Success")
        self._RequestId = params.get("RequestId")


class BindResourceRegionResult(AbstractModel):
    """Region of associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _TotalCount: The total number of associated cloud resources.
        :type TotalCount: int
        """
        self._Region = None
        self._TotalCount = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindResourceResult(AbstractModel):
    """Associated cloud resources

    """

    def __init__(self):
        r"""
        :param _ResourceType: Supported types: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE).
        :type ResourceType: str
        :param _BindResourceRegionResult: The region of associated cloud resources.
        :type BindResourceRegionResult: list of BindResourceRegionResult
        """
        self._ResourceType = None
        self._BindResourceRegionResult = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def BindResourceRegionResult(self):
        return self._BindResourceRegionResult

    @BindResourceRegionResult.setter
    def BindResourceRegionResult(self, BindResourceRegionResult):
        self._BindResourceRegionResult = BindResourceRegionResult


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("BindResourceRegionResult") is not None:
            self._BindResourceRegionResult = []
            for item in params.get("BindResourceRegionResult"):
                obj = BindResourceRegionResult()
                obj._deserialize(item)
                self._BindResourceRegionResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CSRItem(AbstractModel):
    """Details of a CSR

    """

    def __init__(self):
        r"""
        :param _Id: The CSR ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _OwnerUin: The account.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _Domain: The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Organization: The organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Organization: str
        :param _Department: The department.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Department: str
        :param _Email: The email address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Email: str
        :param _Province: The province.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Province: str
        :param _City: The city.
Note: This field may return null, indicating that no valid values can be obtained.
        :type City: str
        :param _Country: The country or region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Country: str
        :param _Remarks: The remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remarks: str
        :param _Status: The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _CreateTime: The creation time.
Note: u200dThis field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _EncryptAlgo: The encryption algorithm.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgo: str
        :param _KeyParameter: The algorithm parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyParameter: str
        """
        self._Id = None
        self._OwnerUin = None
        self._Domain = None
        self._Organization = None
        self._Department = None
        self._Email = None
        self._Province = None
        self._City = None
        self._Country = None
        self._Remarks = None
        self._Status = None
        self._CreateTime = None
        self._EncryptAlgo = None
        self._KeyParameter = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Remarks(self):
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EncryptAlgo(self):
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OwnerUin = params.get("OwnerUin")
        self._Domain = params.get("Domain")
        self._Organization = params.get("Organization")
        self._Department = params.get("Department")
        self._Email = params.get("Email")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Remarks = params.get("Remarks")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._EncryptAlgo = params.get("EncryptAlgo")
        self._KeyParameter = params.get("KeyParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuditCertificateRequest(AbstractModel):
    """CancelAuditCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: The certificate ID.
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuditCertificateResponse(AbstractModel):
    """CancelAuditCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the operation succeeded.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: ID of the certificate whose order has been successfully cancelled
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CdnInstanceDetail(AbstractModel):
    """Details of a CDN instance

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _CertId: The ID of the deployed certificate.
        :type CertId: str
        :param _Status: The status of the domain.
        :type Status: str
        :param _HttpsBillingSwitch: The billing status of the domain.
        :type HttpsBillingSwitch: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._HttpsBillingSwitch = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def HttpsBillingSwitch(self):
        return self._HttpsBillingSwitch

    @HttpsBillingSwitch.setter
    def HttpsBillingSwitch(self, HttpsBillingSwitch):
        self._HttpsBillingSwitch = HttpsBillingSwitch


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._HttpsBillingSwitch = params.get("HttpsBillingSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnInstanceList(AbstractModel):
    """Details of CDN instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of CDN domains in this region.	
        :type TotalCount: int
        :param _InstanceList: The list of CDN domains.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of CdnInstanceDetail
        """
        self._TotalCount = None
        self._InstanceList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertTaskId(AbstractModel):
    """Certificate and async task IDs

    """

    def __init__(self):
        r"""
        :param _CertId: The certificate ID.
        :type CertId: str
        :param _TaskId: The async task ID.
        :type TaskId: str
        """
        self._CertId = None
        self._TaskId = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificate(AbstractModel):
    """Details of a CLB certificate

    """

    def __init__(self):
        r"""
        :param _CertId: The certificate ID.
        :type CertId: str
        :param _DnsNames: The list of domains bound to the certificate.
        :type DnsNames: list of str
        :param _CertCaId: The root certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertCaId: str
        :param _SSLMode: The authentication type. Valid values: `UNIDIRECTIONAL` (one-way authentication) and `MUTUAL` (two-way authentication).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SSLMode: str
        """
        self._CertId = None
        self._DnsNames = None
        self._CertCaId = None
        self._SSLMode = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DnsNames(self):
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames

    @property
    def CertCaId(self):
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def SSLMode(self):
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._DnsNames = params.get("DnsNames")
        self._CertCaId = params.get("CertCaId")
        self._SSLMode = params.get("SSLMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateExtra(AbstractModel):
    """Content of the `CertificateExtra` parameter. `CertificateExtra` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        r"""
        :param _DomainNumber: Number of domain names which can be associated with the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainNumber: str
        :param _OriginCertificateId: Original certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginCertificateId: str
        :param _ReplacedBy: Original ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedBy: str
        :param _ReplacedFor: New ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedFor: str
        :param _RenewOrder: Certificate ID of the new order
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewOrder: str
        :param _SMCert: Whether the certificate is a Chinese SM certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SMCert: int
        :param _CompanyType: Company type
Note: This field may return null, indicating that no valid value can be obtained.
        :type CompanyType: int
        """
        self._DomainNumber = None
        self._OriginCertificateId = None
        self._ReplacedBy = None
        self._ReplacedFor = None
        self._RenewOrder = None
        self._SMCert = None
        self._CompanyType = None

    @property
    def DomainNumber(self):
        return self._DomainNumber

    @DomainNumber.setter
    def DomainNumber(self, DomainNumber):
        self._DomainNumber = DomainNumber

    @property
    def OriginCertificateId(self):
        return self._OriginCertificateId

    @OriginCertificateId.setter
    def OriginCertificateId(self, OriginCertificateId):
        self._OriginCertificateId = OriginCertificateId

    @property
    def ReplacedBy(self):
        return self._ReplacedBy

    @ReplacedBy.setter
    def ReplacedBy(self, ReplacedBy):
        self._ReplacedBy = ReplacedBy

    @property
    def ReplacedFor(self):
        return self._ReplacedFor

    @ReplacedFor.setter
    def ReplacedFor(self, ReplacedFor):
        self._ReplacedFor = ReplacedFor

    @property
    def RenewOrder(self):
        return self._RenewOrder

    @RenewOrder.setter
    def RenewOrder(self, RenewOrder):
        self._RenewOrder = RenewOrder

    @property
    def SMCert(self):
        return self._SMCert

    @SMCert.setter
    def SMCert(self, SMCert):
        self._SMCert = SMCert

    @property
    def CompanyType(self):
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType


    def _deserialize(self, params):
        self._DomainNumber = params.get("DomainNumber")
        self._OriginCertificateId = params.get("OriginCertificateId")
        self._ReplacedBy = params.get("ReplacedBy")
        self._ReplacedFor = params.get("ReplacedFor")
        self._RenewOrder = params.get("RenewOrder")
        self._SMCert = params.get("SMCert")
        self._CompanyType = params.get("CompanyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificates(AbstractModel):
    """Content of the `Certificates` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _From: Certificate source
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param _PackageType: The certificate plan type. Valid values:
null: Certificates uploaded by users (no plan type)
`1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param _ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param _Domain: Primary domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Status: Status. `0`: Reviewing; `1`: Approved; `2`: Unapproved; `3`: Expired; `4`: DNS record added for domain names of the DNS_AUTO verification type; `5`: Enterprise-grade certificate, pending submission; `6`: Canceling order; `7`: Canceled; `8`: Information submitted, pending confirmation letter upload; `9`: Revoking certificate; `10`: Revoked; `11`: Reissuing; `12`: Pending revocation confirmation letter upload; `13`: Pending information submission for the free certificate; `14`: Refunded.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _VulnerabilityStatus: Vulnerability scanning status. `INACTIVE`: not activated; `ACTIVE`: activated
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param _StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param _VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param _CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param _CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param _ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param _InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param _CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param _SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param _PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageTypeName: str
        :param _StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param _IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param _IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param _IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param _IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param _RenewAble: Whether it can be renewed 
Note: This field may return null, indicating that no valid value can be obtained.
        :type RenewAble: bool
        :param _ProjectInfo: Project information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param _BoundResource: Associated Tencent Cloud services. Currently, this parameter is unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BoundResource: list of str
        :param _Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param _Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param _IsIgnore: Whether the expiration notification was ignored
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsIgnore: bool
        :param _IsSM: Whether the certificate is a Chinese SM certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSM: bool
        :param _EncryptAlgorithm: Certificate algorithm
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgorithm: str
        :param _CAEncryptAlgorithms: Encryption algorithm of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEncryptAlgorithms: list of str
        :param _CAEndTimes: Expiration time of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEndTimes: list of str
        :param _CACommonNames: Generic name of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CACommonNames: list of str
        :param _PreAuditInfo: Prereview information of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param _AutoRenewFlag: Whether auto-renewal is enabled.
Note: This field may return null, indicating that no valid value can be obtained.
        :type AutoRenewFlag: int
        :param _HostingStatus: The hosting status. Valid values: `0` (hosting), `5` (replacing resources), `10` (hosting completed), and `-1` (not hosted). 
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostingStatus: int
        :param _HostingCompleteTime: The hosting completion time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostingCompleteTime: str
        :param _HostingRenewCertId: The hosted new certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostingRenewCertId: str
        :param _HasRenewOrder: Existing renewed certificate ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type HasRenewOrder: str
        :param _ReplaceOriCertIsDelete: Whether the original certificate is deleted when a certificate is reissued.
Note: This field may return null, indicating that no valid value can be obtained.
        :type ReplaceOriCertIsDelete: bool
        :param _IsExpiring: Whether the certificate is expiring soon. A certificate is considered to be expiring soon when there are 30 days or less left.
Note: This field may return null, indicating that no valid value can be obtained.
        :type IsExpiring: bool
        :param _DVAuthDeadline: Validation expiration time for the addition of the DV certificate
Note: This field may return null, indicating that no valid value can be obtained.
        :type DVAuthDeadline: str
        :param _ValidationPassedTime: Domain name validation pass time
Note: This field may return null, indicating that no valid value can be obtained.
        :type ValidationPassedTime: str
        :param _CertSANs: Multiple domain names with which the certificate is associated
Note: This field may return null, indicating that no valid value can be obtained.
        :type CertSANs: list of str
        :param _AwaitingValidationMsg: Domain name validation rejection information
Note: This field may return null, indicating that no valid value can be obtained.
        :type AwaitingValidationMsg: str
        :param _AllowDownload: Whether downloading is allowed
Note: This field may return null, indicating that no valid value can be obtained.
        :type AllowDownload: bool
        :param _IsDNSPODResolve: 
        :type IsDNSPODResolve: bool
        :param _IsPackage: 
        :type IsPackage: bool
        :param _KeyPasswordCustomFlag: 
        :type KeyPasswordCustomFlag: bool
        :param _SupportDownloadType: 
        :type SupportDownloadType: :class:`tencentcloud.ssl.v20191205.models.SupportDownloadType`
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._PackageType = None
        self._CertificateType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._CertificateExtra = None
        self._VulnerabilityStatus = None
        self._StatusMsg = None
        self._VerifyType = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._CertificateId = None
        self._SubjectAltName = None
        self._PackageTypeName = None
        self._StatusName = None
        self._IsVip = None
        self._IsDv = None
        self._IsWildcard = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._ProjectInfo = None
        self._BoundResource = None
        self._Deployable = None
        self._Tags = None
        self._IsIgnore = None
        self._IsSM = None
        self._EncryptAlgorithm = None
        self._CAEncryptAlgorithms = None
        self._CAEndTimes = None
        self._CACommonNames = None
        self._PreAuditInfo = None
        self._AutoRenewFlag = None
        self._HostingStatus = None
        self._HostingCompleteTime = None
        self._HostingRenewCertId = None
        self._HasRenewOrder = None
        self._ReplaceOriCertIsDelete = None
        self._IsExpiring = None
        self._DVAuthDeadline = None
        self._ValidationPassedTime = None
        self._CertSANs = None
        self._AwaitingValidationMsg = None
        self._AllowDownload = None
        self._IsDNSPODResolve = None
        self._IsPackage = None
        self._KeyPasswordCustomFlag = None
        self._SupportDownloadType = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def PackageTypeName(self):
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def ProjectInfo(self):
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def BoundResource(self):
        return self._BoundResource

    @BoundResource.setter
    def BoundResource(self, BoundResource):
        self._BoundResource = BoundResource

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsIgnore(self):
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def IsSM(self):
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def EncryptAlgorithm(self):
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def CAEncryptAlgorithms(self):
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CAEndTimes(self):
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def CACommonNames(self):
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def PreAuditInfo(self):
        return self._PreAuditInfo

    @PreAuditInfo.setter
    def PreAuditInfo(self, PreAuditInfo):
        self._PreAuditInfo = PreAuditInfo

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def HostingStatus(self):
        return self._HostingStatus

    @HostingStatus.setter
    def HostingStatus(self, HostingStatus):
        self._HostingStatus = HostingStatus

    @property
    def HostingCompleteTime(self):
        return self._HostingCompleteTime

    @HostingCompleteTime.setter
    def HostingCompleteTime(self, HostingCompleteTime):
        self._HostingCompleteTime = HostingCompleteTime

    @property
    def HostingRenewCertId(self):
        return self._HostingRenewCertId

    @HostingRenewCertId.setter
    def HostingRenewCertId(self, HostingRenewCertId):
        self._HostingRenewCertId = HostingRenewCertId

    @property
    def HasRenewOrder(self):
        return self._HasRenewOrder

    @HasRenewOrder.setter
    def HasRenewOrder(self, HasRenewOrder):
        self._HasRenewOrder = HasRenewOrder

    @property
    def ReplaceOriCertIsDelete(self):
        return self._ReplaceOriCertIsDelete

    @ReplaceOriCertIsDelete.setter
    def ReplaceOriCertIsDelete(self, ReplaceOriCertIsDelete):
        self._ReplaceOriCertIsDelete = ReplaceOriCertIsDelete

    @property
    def IsExpiring(self):
        return self._IsExpiring

    @IsExpiring.setter
    def IsExpiring(self, IsExpiring):
        self._IsExpiring = IsExpiring

    @property
    def DVAuthDeadline(self):
        return self._DVAuthDeadline

    @DVAuthDeadline.setter
    def DVAuthDeadline(self, DVAuthDeadline):
        self._DVAuthDeadline = DVAuthDeadline

    @property
    def ValidationPassedTime(self):
        return self._ValidationPassedTime

    @ValidationPassedTime.setter
    def ValidationPassedTime(self, ValidationPassedTime):
        self._ValidationPassedTime = ValidationPassedTime

    @property
    def CertSANs(self):
        return self._CertSANs

    @CertSANs.setter
    def CertSANs(self, CertSANs):
        self._CertSANs = CertSANs

    @property
    def AwaitingValidationMsg(self):
        return self._AwaitingValidationMsg

    @AwaitingValidationMsg.setter
    def AwaitingValidationMsg(self, AwaitingValidationMsg):
        self._AwaitingValidationMsg = AwaitingValidationMsg

    @property
    def AllowDownload(self):
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def IsDNSPODResolve(self):
        return self._IsDNSPODResolve

    @IsDNSPODResolve.setter
    def IsDNSPODResolve(self, IsDNSPODResolve):
        self._IsDNSPODResolve = IsDNSPODResolve

    @property
    def IsPackage(self):
        return self._IsPackage

    @IsPackage.setter
    def IsPackage(self, IsPackage):
        self._IsPackage = IsPackage

    @property
    def KeyPasswordCustomFlag(self):
        return self._KeyPasswordCustomFlag

    @KeyPasswordCustomFlag.setter
    def KeyPasswordCustomFlag(self, KeyPasswordCustomFlag):
        self._KeyPasswordCustomFlag = KeyPasswordCustomFlag

    @property
    def SupportDownloadType(self):
        return self._SupportDownloadType

    @SupportDownloadType.setter
    def SupportDownloadType(self, SupportDownloadType):
        self._SupportDownloadType = SupportDownloadType


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._PackageType = params.get("PackageType")
        self._CertificateType = params.get("CertificateType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._CertificateId = params.get("CertificateId")
        self._SubjectAltName = params.get("SubjectAltName")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._IsVip = params.get("IsVip")
        self._IsDv = params.get("IsDv")
        self._IsWildcard = params.get("IsWildcard")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self._ProjectInfo = ProjectInfo()
            self._ProjectInfo._deserialize(params.get("ProjectInfo"))
        self._BoundResource = params.get("BoundResource")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsIgnore = params.get("IsIgnore")
        self._IsSM = params.get("IsSM")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CAEndTimes = params.get("CAEndTimes")
        self._CACommonNames = params.get("CACommonNames")
        if params.get("PreAuditInfo") is not None:
            self._PreAuditInfo = PreAuditInfo()
            self._PreAuditInfo._deserialize(params.get("PreAuditInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._HostingStatus = params.get("HostingStatus")
        self._HostingCompleteTime = params.get("HostingCompleteTime")
        self._HostingRenewCertId = params.get("HostingRenewCertId")
        self._HasRenewOrder = params.get("HasRenewOrder")
        self._ReplaceOriCertIsDelete = params.get("ReplaceOriCertIsDelete")
        self._IsExpiring = params.get("IsExpiring")
        self._DVAuthDeadline = params.get("DVAuthDeadline")
        self._ValidationPassedTime = params.get("ValidationPassedTime")
        self._CertSANs = params.get("CertSANs")
        self._AwaitingValidationMsg = params.get("AwaitingValidationMsg")
        self._AllowDownload = params.get("AllowDownload")
        self._IsDNSPODResolve = params.get("IsDNSPODResolve")
        self._IsPackage = params.get("IsPackage")
        self._KeyPasswordCustomFlag = params.get("KeyPasswordCustomFlag")
        if params.get("SupportDownloadType") is not None:
            self._SupportDownloadType = SupportDownloadType()
            self._SupportDownloadType._deserialize(params.get("SupportDownloadType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbInstanceDetail(AbstractModel):
    """Details of a CLB instance

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: The CLB instance ID.
        :type LoadBalancerId: str
        :param _LoadBalancerName: The CLB instance name.
        :type LoadBalancerName: str
        :param _Listeners: The list of CLB listeners.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Listeners: list of ClbListener
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ClbListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbInstanceList(AbstractModel):
    """Details of CLB instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
        :type Region: str
        :param _InstanceList: The list of CLB instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of ClbInstanceDetail
        :param _TotalCount: The total number of CLB instances in this region.
        :type TotalCount: int
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListener(AbstractModel):
    """Details of a CLB instance listener

    """

    def __init__(self):
        r"""
        :param _ListenerId: The listener ID.
        :type ListenerId: str
        :param _ListenerName: The listener name.
        :type ListenerName: str
        :param _SniSwitch: Whether to enable SNI. Valid values: `1` (enable) and `0` (disable).
        :type SniSwitch: int
        :param _Protocol: The listener protocol type. Valid values: `HTTPS` and `TCP_SSL`.
        :type Protocol: str
        :param _Certificate: The information of the certificate bound to the listener.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _Rules: The list of the listener rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rules: list of ClbListenerRule
        :param _NoMatchDomains: The list of non-matching domains.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoMatchDomains: list of str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._SniSwitch = None
        self._Protocol = None
        self._Certificate = None
        self._Rules = None
        self._NoMatchDomains = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SniSwitch = params.get("SniSwitch")
        self._Protocol = params.get("Protocol")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ClbListenerRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerRule(AbstractModel):
    """Details of a CLB listener rule

    """

    def __init__(self):
        r"""
        :param _LocationId: The rule ID.
        :type LocationId: str
        :param _Domain: The domains bound.
        :type Domain: str
        :param _IsMatch: Whether the rule matches the domains to be associated with a certificate.
        :type IsMatch: bool
        :param _Certificate: The certificates associated with the rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _NoMatchDomains: The list of non-matching domains.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoMatchDomains: list of str
        """
        self._LocationId = None
        self._Domain = None
        self._IsMatch = None
        self._Certificate = None
        self._NoMatchDomains = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._IsMatch = params.get("IsMatch")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _VerifyType: Domain validation method
        :type VerifyType: str
        """
        self._CertificateId = None
        self._VerifyType = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation response structure.

    """

    def __init__(self):
        r"""
        :param _OrderId: TrustAsia order ID
        :type OrderId: str
        :param _Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderId = None
        self._Status = None
        self._RequestId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

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
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateCSRRequest(AbstractModel):
    """CreateCSR request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _Organization: The organization name.
        :type Organization: str
        :param _Department: The department.
        :type Department: str
        :param _Email: The email address.
        :type Email: str
        :param _Province: The province.
        :type Province: str
        :param _City: The city.
        :type City: str
        :param _Country: The country or region code that complies with ISO 3166, such as CN and US.
        :type Country: str
        :param _EncryptAlgo: The encryption algorithm. RSA and ECC are supported.	
        :type EncryptAlgo: str
        :param _KeyParameter: The key pair parameter. For RSA, only the 2048-bit and 4096-bit key pairs are supported. For ECC, only prime256v1 is supported.
        :type KeyParameter: str
        :param _Generate: Whether to generate the CSR content. Once the CSR content is generated, the CSR record cannot be modified.
        :type Generate: bool
        :param _KeyPassword: The password of the private key.
        :type KeyPassword: str
        :param _Remark: The remarks.
        :type Remark: str
        """
        self._Domain = None
        self._Organization = None
        self._Department = None
        self._Email = None
        self._Province = None
        self._City = None
        self._Country = None
        self._EncryptAlgo = None
        self._KeyParameter = None
        self._Generate = None
        self._KeyPassword = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Generate(self):
        return self._Generate

    @Generate.setter
    def Generate(self, Generate):
        self._Generate = Generate

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Organization = params.get("Organization")
        self._Department = params.get("Department")
        self._Email = params.get("Email")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._EncryptAlgo = params.get("EncryptAlgo")
        self._KeyParameter = params.get("KeyParameter")
        self._Generate = params.get("Generate")
        self._KeyPassword = params.get("KeyPassword")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCSRResponse(AbstractModel):
    """CreateCSR response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The CSR ID.
        :type Id: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateCertificateBindResourceSyncTaskRequest(AbstractModel):
    """CreateCertificateBindResourceSyncTask request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateIds: The list of certificate IDs, 100 IDs at most.
        :type CertificateIds: list of str
        :param _IsCache: Whether to use the cached results. Valid values: `1` (default) for yes and `0` for no. If any task completed within last 30 minutes exists under the current certificate ID, and the cache is used, the query result of the last task completed within 30 minutes will be read.
        :type IsCache: int
        """
        self._CertificateIds = None
        self._IsCache = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._IsCache = params.get("IsCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateBindResourceSyncTaskResponse(AbstractModel):
    """CreateCertificateBindResourceSyncTask response structure.

    """

    def __init__(self):
        r"""
        :param _CertTaskIds: The IDs of async tasks for querying cloud resources associated with a certificate.
        :type CertTaskIds: list of CertTaskId
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertTaskIds = None
        self._RequestId = None

    @property
    def CertTaskIds(self):
        return self._CertTaskIds

    @CertTaskIds.setter
    def CertTaskIds(self, CertTaskIds):
        self._CertTaskIds = CertTaskIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertTaskIds") is not None:
            self._CertTaskIds = []
            for item in params.get("CertTaskIds"):
                obj = CertTaskId()
                obj._deserialize(item)
                self._CertTaskIds.append(obj)
        self._RequestId = params.get("RequestId")


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Certificate product ID. `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain; `25` WoTrus DV; `26`: WoTrus DV multi-domain; `27`: WoTrus DV wildcard; `28`: WoTrus OV; `29`: WoTrus OV multi-domain; `30`: WoTrus OV wildcard; `31`: WoTrus EV; `32`: WoTrus EV multi-domain; `33`: DNSPod SM2 DV; `34`: DNSPod SM2 DV multi-domain; `35`: DNSPod SM2 DV wildcard; `37`: DNSPod SM2 OV; `38`: DNSPod SM2 OV multi-domain; `39`: DNSPod SM2 OV wildcard: `40`: DNSPod SM2 EV; `41`: DNSPod SM2 EV multi-domain; `42`: TrustAsia DV wildcard multi-domain.
        :type ProductId: int
        :param _DomainNum: Number of domains associated with the certificate
        :type DomainNum: int
        :param _TimeSpan: Certificate validity period. Currently, you can only purchase 1-year certificates.
        :type TimeSpan: int
        """
        self._ProductId = None
        self._DomainNum = None
        self._TimeSpan = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DomainNum(self):
        return self._DomainNum

    @DomainNum.setter
    def DomainNum(self, DomainNum):
        self._DomainNum = DomainNum

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DomainNum = params.get("DomainNum")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateIds: List of certificate IDs
        :type CertificateIds: list of str
        :param _DealIds: List of order IDs
        :type DealIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateIds = None
        self._DealIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._DealIds = params.get("DealIds")
        self._RequestId = params.get("RequestId")


class DdosInstanceDetail(AbstractModel):
    """Details of a DDOS instance

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _Protocol: The protocol type.
        :type Protocol: str
        :param _CertId: The certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _VirtualPort: The forwarding port.
        :type VirtualPort: str
        """
        self._Domain = None
        self._InstanceId = None
        self._Protocol = None
        self._CertId = None
        self._VirtualPort = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        self._Protocol = params.get("Protocol")
        self._CertId = params.get("CertId")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosInstanceList(AbstractModel):
    """Details of DDOS instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of DDOS instances in this region.	
        :type TotalCount: int
        :param _InstanceList: The list of DDOS instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of DdosInstanceDetail
        """
        self._TotalCount = None
        self._InstanceList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _DeleteResult: Deletion result
        :type DeleteResult: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeleteResult = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeleteResult = params.get("DeleteResult")
        self._RequestId = params.get("RequestId")


class DescribeCSRRequest(AbstractModel):
    """DescribeCSR request structure.

    """

    def __init__(self):
        r"""
        :param _CSRId: The CSR ID.
        :type CSRId: int
        """
        self._CSRId = None

    @property
    def CSRId(self):
        return self._CSRId

    @CSRId.setter
    def CSRId(self, CSRId):
        self._CSRId = CSRId


    def _deserialize(self, params):
        self._CSRId = params.get("CSRId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCSRResponse(AbstractModel):
    """DescribeCSR response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The CSR ID.
        :type Id: int
        :param _OwnerUin: The account.
        :type OwnerUin: str
        :param _Domain: The domain.
        :type Domain: str
        :param _Organization: The organization name.
        :type Organization: str
        :param _Department: The department.
        :type Department: str
        :param _Email: The email address.
        :type Email: str
        :param _Province: The province.
        :type Province: str
        :param _City: The city.
        :type City: str
        :param _Country: The country or region.
        :type Country: str
        :param _EncryptAlgo: The key algorithm.
        :type EncryptAlgo: str
        :param _KeyParameter: The algorithm parameter.
        :type KeyParameter: str
        :param _Remarks: The remarks.
        :type Remarks: str
        :param _Status: The status.
        :type Status: int
        :param _KeyPassword: The password of the private key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyPassword: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _CSR: The CSR content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CSR: str
        :param _PrivateKey: The content of the private key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._OwnerUin = None
        self._Domain = None
        self._Organization = None
        self._Department = None
        self._Email = None
        self._Province = None
        self._City = None
        self._Country = None
        self._EncryptAlgo = None
        self._KeyParameter = None
        self._Remarks = None
        self._Status = None
        self._KeyPassword = None
        self._CreateTime = None
        self._CSR = None
        self._PrivateKey = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Remarks(self):
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CSR(self):
        return self._CSR

    @CSR.setter
    def CSR(self, CSR):
        self._CSR = CSR

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OwnerUin = params.get("OwnerUin")
        self._Domain = params.get("Domain")
        self._Organization = params.get("Organization")
        self._Department = params.get("Department")
        self._Email = params.get("Email")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._EncryptAlgo = params.get("EncryptAlgo")
        self._KeyParameter = params.get("KeyParameter")
        self._Remarks = params.get("Remarks")
        self._Status = params.get("Status")
        self._KeyPassword = params.get("KeyPassword")
        self._CreateTime = params.get("CreateTime")
        self._CSR = params.get("CSR")
        self._PrivateKey = params.get("PrivateKey")
        self._RequestId = params.get("RequestId")


class DescribeCSRSetRequest(AbstractModel):
    """DescribeCSRSet request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: The number of CSRs on each page. The default value is 10, and the maximum value is 100.
        :type Limit: int
        :param _Offset: The pagination offset, starting from 0.	
        :type Offset: int
        :param _Domain: The domain for CSR filtering.
        :type Domain: str
        :param _EncryptAlgo: The encryption algorithm for CSR filtering.
        :type EncryptAlgo: str
        """
        self._Limit = None
        self._Offset = None
        self._Domain = None
        self._EncryptAlgo = None

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
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def EncryptAlgo(self):
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        self._EncryptAlgo = params.get("EncryptAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCSRSetResponse(AbstractModel):
    """DescribeCSRSet response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The total number of CSRs.	
        :type Total: int
        :param _Set: The list of CSRs.
        :type Set: list of CSRItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Set = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Set(self):
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = CSRItem()
                obj._deserialize(item)
                self._Set.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateBindResourceTaskDetailRequest(AbstractModel):
    """DescribeCertificateBindResourceTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID, which is required to query the result of associated cloud resources.
        :type TaskId: str
        :param _Limit: The number of cloud resources displayed on each page. The default value is 10, and the maximum value is 100.
        :type Limit: str
        :param _Offset: The current offset.
        :type Offset: str
        :param _ResourceTypes: The types of the resources to be queried. If no value is passed in, all types of resources will be queried.
        :type ResourceTypes: list of str
        :param _Regions: The regions of the resources to be queried. Only CLB, TKE, WAF, APIGATEWAY, and TCB resources support the query by region.
        :type Regions: list of str
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._ResourceTypes = None
        self._Regions = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateBindResourceTaskDetailResponse(AbstractModel):
    """DescribeCertificateBindResourceTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _CLB: The details of associated CLB resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type CLB: list of ClbInstanceList
        :param _CDN: The details of associated CDN resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type CDN: list of CdnInstanceList
        :param _WAF: The details of associated WAF resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type WAF: list of WafInstanceList
        :param _DDOS: The details of associated Anti-DDS resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDOS: list of DdosInstanceList
        :param _LIVE: The details of associated LIVE resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type LIVE: list of LiveInstanceList
        :param _VOD: The details of associated VOD resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type VOD: list of VODInstanceList
        :param _TKE: The details of associated TKE resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type TKE: list of TkeInstanceList
        :param _APIGATEWAY: The details of associated APIGATEWAY resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type APIGATEWAY: list of ApiGatewayInstanceList
        :param _TCB: The details of associated TCB resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type TCB: list of TCBInstanceList
        :param _TEO: The details of associated TEO resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type TEO: list of TeoInstanceList
        :param _Status: The status of the async task. Valid values: `0` for querying, `1` for successful, and `2` for abnormal. If the status is `1`, the result of `BindResourceResult` will be displayed; if the status is `2`, the error causes will be displayed.
        :type Status: int
        :param _CacheTime: The cache time of the current result.
        :type CacheTime: str
        :param _TSE: Associated TSE resource details
Note: This field may return null, indicating that no valid value can be obtained.
        :type TSE: list of TSEInstanceList
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CLB = None
        self._CDN = None
        self._WAF = None
        self._DDOS = None
        self._LIVE = None
        self._VOD = None
        self._TKE = None
        self._APIGATEWAY = None
        self._TCB = None
        self._TEO = None
        self._Status = None
        self._CacheTime = None
        self._TSE = None
        self._RequestId = None

    @property
    def CLB(self):
        return self._CLB

    @CLB.setter
    def CLB(self, CLB):
        self._CLB = CLB

    @property
    def CDN(self):
        return self._CDN

    @CDN.setter
    def CDN(self, CDN):
        self._CDN = CDN

    @property
    def WAF(self):
        return self._WAF

    @WAF.setter
    def WAF(self, WAF):
        self._WAF = WAF

    @property
    def DDOS(self):
        return self._DDOS

    @DDOS.setter
    def DDOS(self, DDOS):
        self._DDOS = DDOS

    @property
    def LIVE(self):
        return self._LIVE

    @LIVE.setter
    def LIVE(self, LIVE):
        self._LIVE = LIVE

    @property
    def VOD(self):
        return self._VOD

    @VOD.setter
    def VOD(self, VOD):
        self._VOD = VOD

    @property
    def TKE(self):
        return self._TKE

    @TKE.setter
    def TKE(self, TKE):
        self._TKE = TKE

    @property
    def APIGATEWAY(self):
        return self._APIGATEWAY

    @APIGATEWAY.setter
    def APIGATEWAY(self, APIGATEWAY):
        self._APIGATEWAY = APIGATEWAY

    @property
    def TCB(self):
        return self._TCB

    @TCB.setter
    def TCB(self, TCB):
        self._TCB = TCB

    @property
    def TEO(self):
        return self._TEO

    @TEO.setter
    def TEO(self, TEO):
        self._TEO = TEO

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def TSE(self):
        return self._TSE

    @TSE.setter
    def TSE(self, TSE):
        self._TSE = TSE

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CLB") is not None:
            self._CLB = []
            for item in params.get("CLB"):
                obj = ClbInstanceList()
                obj._deserialize(item)
                self._CLB.append(obj)
        if params.get("CDN") is not None:
            self._CDN = []
            for item in params.get("CDN"):
                obj = CdnInstanceList()
                obj._deserialize(item)
                self._CDN.append(obj)
        if params.get("WAF") is not None:
            self._WAF = []
            for item in params.get("WAF"):
                obj = WafInstanceList()
                obj._deserialize(item)
                self._WAF.append(obj)
        if params.get("DDOS") is not None:
            self._DDOS = []
            for item in params.get("DDOS"):
                obj = DdosInstanceList()
                obj._deserialize(item)
                self._DDOS.append(obj)
        if params.get("LIVE") is not None:
            self._LIVE = []
            for item in params.get("LIVE"):
                obj = LiveInstanceList()
                obj._deserialize(item)
                self._LIVE.append(obj)
        if params.get("VOD") is not None:
            self._VOD = []
            for item in params.get("VOD"):
                obj = VODInstanceList()
                obj._deserialize(item)
                self._VOD.append(obj)
        if params.get("TKE") is not None:
            self._TKE = []
            for item in params.get("TKE"):
                obj = TkeInstanceList()
                obj._deserialize(item)
                self._TKE.append(obj)
        if params.get("APIGATEWAY") is not None:
            self._APIGATEWAY = []
            for item in params.get("APIGATEWAY"):
                obj = ApiGatewayInstanceList()
                obj._deserialize(item)
                self._APIGATEWAY.append(obj)
        if params.get("TCB") is not None:
            self._TCB = []
            for item in params.get("TCB"):
                obj = TCBInstanceList()
                obj._deserialize(item)
                self._TCB.append(obj)
        if params.get("TEO") is not None:
            self._TEO = []
            for item in params.get("TEO"):
                obj = TeoInstanceList()
                obj._deserialize(item)
                self._TEO.append(obj)
        self._Status = params.get("Status")
        self._CacheTime = params.get("CacheTime")
        if params.get("TSE") is not None:
            self._TSE = []
            for item in params.get("TSE"):
                obj = TSEInstanceList()
                obj._deserialize(item)
                self._TSE.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateBindResourceTaskResultRequest(AbstractModel):
    """DescribeCertificateBindResourceTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskIds: The task IDs, which are used to query the results of associated cloud resources, 100 IDs at most.
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateBindResourceTaskResultResponse(AbstractModel):
    """DescribeCertificateBindResourceTaskResult response structure.

    """

    def __init__(self):
        r"""
        :param _SyncTaskBindResourceResult: The results of the async tasks for querying associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SyncTaskBindResourceResult: list of SyncTaskBindResourceResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SyncTaskBindResourceResult = None
        self._RequestId = None

    @property
    def SyncTaskBindResourceResult(self):
        return self._SyncTaskBindResourceResult

    @SyncTaskBindResourceResult.setter
    def SyncTaskBindResourceResult(self, SyncTaskBindResourceResult):
        self._SyncTaskBindResourceResult = SyncTaskBindResourceResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SyncTaskBindResourceResult") is not None:
            self._SyncTaskBindResourceResult = []
            for item in params.get("SyncTaskBindResourceResult"):
                obj = SyncTaskBindResourceResult()
                obj._deserialize(item)
                self._SyncTaskBindResourceResult.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail response structure.

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param _PackageType: Certificate plan type. null: User-uploaded certificate (no plan type); `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain; `25` WoTrus DV; `26`: WoTrus DV multi-domain; `27`: WoTrus DV wildcard; `28`: WoTrus OV; `29`: WoTrus OV multi-domain; `30`: WoTrus OV wildcard; `31`: WoTrus EV; `32`: WoTrus EV multi-domain; `33`: DNSPod SM2 DV; `34`: DNSPod SM2 DV multi-domain; `35`: DNSPod SM2 DV wildcard; `37`: DNSPod SM2 OV; `38`: DNSPod SM2 OV multi-domain; `39`: DNSPod SM2 OV wildcard: `40`: DNSPod SM2 EV; `41`: DNSPod SM2 EV multi-domain; `42`: TrustAsia DV wildcard multi-domain.
        :type PackageType: str
        :param _ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param _Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param _VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param _VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param _CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param _CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param _ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param _InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param _OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param _CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _CertificatePrivateKey: Private key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePrivateKey: str
        :param _CertificatePublicKey: Public key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePublicKey: str
        :param _DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityReport: str
        :param _CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param _TypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeName: str
        :param _StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param _SubjectAltName: Multiple domain names included in the certificate (excluding the primary domain name, which uses the `Domain` field)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param _IsVip: Whether the certificate is a paid one.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param _IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param _IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param _IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param _SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _RenewAble: Whether the certificate can be renewed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewAble: bool
        :param _Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param _Tags: List of associated tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param _RootCert: Root certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootCert: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        :param _EncryptCert: Chinese SM encryption certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptCert: str
        :param _EncryptPrivateKey: Private key of Chinese SM encryption
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptPrivateKey: str
        :param _CertFingerprint: SHA1 fingerprint of the signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertFingerprint: str
        :param _EncryptCertFingerprint: SHA1 fingerprint of the encryption certificate (for Chinese SM certificates only)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptCertFingerprint: str
        :param _EncryptAlgorithm: Certificate algorithm
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgorithm: str
        :param _DvRevokeAuthDetail: The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._CertificatePrivateKey = None
        self._CertificatePublicKey = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._TypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._SubmittedData = None
        self._RenewAble = None
        self._Deployable = None
        self._Tags = None
        self._RootCert = None
        self._EncryptCert = None
        self._EncryptPrivateKey = None
        self._CertFingerprint = None
        self._EncryptCertFingerprint = None
        self._EncryptAlgorithm = None
        self._DvRevokeAuthDetail = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def DvAuthDetail(self):
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def SubmittedData(self):
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RootCert(self):
        return self._RootCert

    @RootCert.setter
    def RootCert(self, RootCert):
        self._RootCert = RootCert

    @property
    def EncryptCert(self):
        return self._EncryptCert

    @EncryptCert.setter
    def EncryptCert(self, EncryptCert):
        self._EncryptCert = EncryptCert

    @property
    def EncryptPrivateKey(self):
        return self._EncryptPrivateKey

    @EncryptPrivateKey.setter
    def EncryptPrivateKey(self, EncryptPrivateKey):
        self._EncryptPrivateKey = EncryptPrivateKey

    @property
    def CertFingerprint(self):
        return self._CertFingerprint

    @CertFingerprint.setter
    def CertFingerprint(self, CertFingerprint):
        self._CertFingerprint = CertFingerprint

    @property
    def EncryptCertFingerprint(self):
        return self._EncryptCertFingerprint

    @EncryptCertFingerprint.setter
    def EncryptCertFingerprint(self, EncryptCertFingerprint):
        self._EncryptCertFingerprint = EncryptCertFingerprint

    @property
    def EncryptAlgorithm(self):
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def DvRevokeAuthDetail(self):
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._TypeName = params.get("TypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._RenewAble = params.get("RenewAble")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("RootCert") is not None:
            self._RootCert = RootCertificates()
            self._RootCert._deserialize(params.get("RootCert"))
        self._EncryptCert = params.get("EncryptCert")
        self._EncryptPrivateKey = params.get("EncryptPrivateKey")
        self._CertFingerprint = params.get("CertFingerprint")
        self._EncryptCertFingerprint = params.get("EncryptCertFingerprint")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Number of requested logs. The default value is 20.
        :type Limit: int
        :param _StartTime: Start time. The default value is 15 days ago.
        :type StartTime: str
        :param _EndTime: End time. The default value is the current time.
        :type EndTime: str
        """
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs response structure.

    """

    def __init__(self):
        r"""
        :param _AllTotal: Total number of logs that meet query conditions
        :type AllTotal: int
        :param _TotalCount: Number of logs returned for this request
        :type TotalCount: int
        :param _OperateLogs: Certificate operation log list
Note: this field may return null, indicating that no valid values can be obtained.
        :type OperateLogs: list of OperationLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllTotal = None
        self._TotalCount = None
        self._OperateLogs = None
        self._RequestId = None

    @property
    def AllTotal(self):
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OperateLogs(self):
        return self._OperateLogs

    @OperateLogs.setter
    def OperateLogs(self, OperateLogs):
        self._OperateLogs = OperateLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllTotal = params.get("AllTotal")
        self._TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self._OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self._OperateLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param _PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _ProductZhName: Name of the certificate issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param _Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param _VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param _VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param _CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param _CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param _ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param _InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param _OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param _CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityReport: str
        :param _CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param _PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageTypeName: str
        :param _StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param _SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param _IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param _IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param _IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param _IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param _RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewAble: bool
        :param _SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param _Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param _CAEncryptAlgorithms: All encryption algorithms of a CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEncryptAlgorithms: list of str
        :param _CACommonNames: All common names of a CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CACommonNames: list of str
        :param _CAEndTimes: All expiration time of a CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEndTimes: list of str
        :param _DvRevokeAuthDetail: The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._PackageTypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._SubmittedData = None
        self._Deployable = None
        self._Tags = None
        self._CAEncryptAlgorithms = None
        self._CACommonNames = None
        self._CAEndTimes = None
        self._DvRevokeAuthDetail = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def DvAuthDetail(self):
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PackageTypeName(self):
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def SubmittedData(self):
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CAEncryptAlgorithms(self):
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CACommonNames(self):
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def CAEndTimes(self):
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def DvRevokeAuthDetail(self):
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CACommonNames = params.get("CACommonNames")
        self._CAEndTimes = params.get("CAEndTimes")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from 0
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param _SearchKey: Keyword for search, which can be a certificate ID, alias, or domain name, for example, a8xHcaIs
        :type SearchKey: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
        :type CertificateType: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ExpirationSort: Sorting by expiration time. `DESC`: descending; `ASC`: ascending
        :type ExpirationSort: str
        :param _CertificateStatus: Certificate status. `0`: Reviewing; `1`: Approved; `2`: Unapproved; `3`: Expired; `4`: DNS record added; `5`: Enterprise-grade certificate, pending submission; `6`: Canceling order; `7`: Canceled; `8`: Information submitted, pending confirmation letter upload; `9`: Revoking certificate; `10`: Revoked; `11`: Reissuing; `12`: Pending revocation confirmation letter upload; `13`: Pending information submission for the free certificate.
        :type CertificateStatus: list of int non-negative
        :param _Deployable: Whether the certificate can be deployed. `1`: yes; `0`: no
        :type Deployable: int
        :param _Upload: Whether to filter uploaded hosted certificates. `1`: Yes; `0`: No.
        :type Upload: int
        :param _Renew: Whether to filter renewable certificates. `1`: Yes; `0`: No.
        :type Renew: int
        :param _FilterSource: Filter by source. `upload`: Uploaded certificate; `buy`: Tencent Cloud certificate. If this parameter is left empty, all certificates will be queried.
        :type FilterSource: str
        :param _IsSM: Whether to filter Chinese SM certificates. `1`: Yes; `0`: No.
        :type IsSM: int
        :param _FilterExpiring: Whether to filter expiring certificates. `1`: Yes; `0`: No.
        :type FilterExpiring: int
        :param _Hostable: Whether the certificate can be hosted. Valid values: `1` for yes and `0` for no.
        :type Hostable: int
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._CertificateType = None
        self._ProjectId = None
        self._ExpirationSort = None
        self._CertificateStatus = None
        self._Deployable = None
        self._Upload = None
        self._Renew = None
        self._FilterSource = None
        self._IsSM = None
        self._FilterExpiring = None
        self._Hostable = None

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ExpirationSort(self):
        return self._ExpirationSort

    @ExpirationSort.setter
    def ExpirationSort(self, ExpirationSort):
        self._ExpirationSort = ExpirationSort

    @property
    def CertificateStatus(self):
        return self._CertificateStatus

    @CertificateStatus.setter
    def CertificateStatus(self, CertificateStatus):
        self._CertificateStatus = CertificateStatus

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Upload(self):
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Renew(self):
        return self._Renew

    @Renew.setter
    def Renew(self, Renew):
        self._Renew = Renew

    @property
    def FilterSource(self):
        return self._FilterSource

    @FilterSource.setter
    def FilterSource(self, FilterSource):
        self._FilterSource = FilterSource

    @property
    def IsSM(self):
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def FilterExpiring(self):
        return self._FilterExpiring

    @FilterExpiring.setter
    def FilterExpiring(self, FilterExpiring):
        self._FilterExpiring = FilterExpiring

    @property
    def Hostable(self):
        return self._Hostable

    @Hostable.setter
    def Hostable(self, Hostable):
        self._Hostable = Hostable


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._CertificateType = params.get("CertificateType")
        self._ProjectId = params.get("ProjectId")
        self._ExpirationSort = params.get("ExpirationSort")
        self._CertificateStatus = params.get("CertificateStatus")
        self._Deployable = params.get("Deployable")
        self._Upload = params.get("Upload")
        self._Renew = params.get("Renew")
        self._FilterSource = params.get("FilterSource")
        self._IsSM = params.get("IsSM")
        self._FilterExpiring = params.get("FilterExpiring")
        self._Hostable = params.get("Hostable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Certificates: List
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificates: list of Certificates
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Certificates = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Certificates(self):
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self._Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self._Certificates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostTeoInstanceListRequest(AbstractModel):
    """DescribeHostTeoInstanceList request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: The ID of the certificate to be deployed.
        :type CertificateId: str
        :param _ResourceType: The type of resource for certificate deployment.
        :type ResourceType: str
        :param _IsCache: Whether to query the cached results. Valid values: `1` (yes) and `0` (no). By default, the cached results within 30 minutes are queried.
        :type IsCache: int
        :param _Filters: The list of filter parameters. FilterKey: domainMatch (query the list of instances with matching or non-matching domains). FilterValue: `1` (default; query the list of instances with matching domains) or `0` (query the list of instances with non-matching domains).
        :type Filters: list of Filter
        :param _OldCertificateId: The ID of the deployed certificate.
        :type OldCertificateId: str
        :param _Offset: The pagination offset, starting from 0.
        :type Offset: int
        :param _Limit: The number of instances on each page. Default value: 10.	
        :type Limit: int
        :param _AsyncCache: Whether the query is asynchronous.
        :type AsyncCache: int
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None
        self._AsyncCache = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

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
    def AsyncCache(self):
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AsyncCache = params.get("AsyncCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTeoInstanceListResponse(AbstractModel):
    """DescribeHostTeoInstanceList response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceList: The list of EDGEONE instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordDetailRequest(AbstractModel):
    """DescribeHostUpdateRecordDetail request structure.

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: One-click update record ID
        :type DeployRecordId: str
        :param _Limit: Number per page, 10 by default.
        :type Limit: str
        :param _Offset: Paging offset, starting from 0
        :type Offset: str
        """
        self._DeployRecordId = None
        self._Limit = None
        self._Offset = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

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
        self._DeployRecordId = params.get("DeployRecordId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordDetailResponse(AbstractModel):
    """DescribeHostUpdateRecordDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count
Note: This field may return null, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RecordDetailList: Certificate deployment record list
Note: This field may return null, indicating that no valid value can be obtained.
        :type RecordDetailList: list of UpdateRecordDetails
        :param _SuccessTotalCount: Total successful deployments
Note: This field may return null, indicating that no valid value can be obtained.
        :type SuccessTotalCount: int
        :param _FailedTotalCount: Total failed deployments
Note: This field may return null, indicating that no valid value can be obtained.
        :type FailedTotalCount: int
        :param _RunningTotalCount: Total running deployments
Note: This field may return null, indicating that no valid value can be obtained.
        :type RunningTotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordDetailList = None
        self._SuccessTotalCount = None
        self._FailedTotalCount = None
        self._RunningTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordDetailList(self):
        return self._RecordDetailList

    @RecordDetailList.setter
    def RecordDetailList(self, RecordDetailList):
        self._RecordDetailList = RecordDetailList

    @property
    def SuccessTotalCount(self):
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordDetailList") is not None:
            self._RecordDetailList = []
            for item in params.get("RecordDetailList"):
                obj = UpdateRecordDetails()
                obj._deserialize(item)
                self._RecordDetailList.append(obj)
        self._SuccessTotalCount = params.get("SuccessTotalCount")
        self._FailedTotalCount = params.get("FailedTotalCount")
        self._RunningTotalCount = params.get("RunningTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordRequest(AbstractModel):
    """DescribeHostUpdateRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Paging offset, starting from 0
        :type Offset: int
        :param _Limit: Number per page, 10 by default.
        :type Limit: int
        :param _CertificateId: New certificate ID
        :type CertificateId: str
        :param _OldCertificateId: Old certificate ID
        :type OldCertificateId: str
        """
        self._Offset = None
        self._Limit = None
        self._CertificateId = None
        self._OldCertificateId = None

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
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CertificateId = params.get("CertificateId")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordResponse(AbstractModel):
    """DescribeHostUpdateRecord response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count
Note: This field may return null, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _DeployRecordList: Certificate deployment record list
Note: This field may return null, indicating that no valid value can be obtained.
        :type DeployRecordList: list of UpdateRecordInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self._DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = UpdateRecordInfo()
                obj._deserialize(item)
                self._DeployRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _Content: ZIP content encoded by using Base64. After the content is decoded by using Base64, it can be saved as a ZIP file.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param _ContentType: MIME type. `application/zip`: ZIP file
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContentType: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._ContentType = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        self._RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """Content of the `DvAuthDetail` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param _DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param _DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param _DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param _DvAuthKeySubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKeySubDomain: str
        :param _DvAuths: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuths: list of DvAuths
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthKeySubDomain = None
        self._DvAuths = None

    @property
    def DvAuthKey(self):
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthKeySubDomain(self):
        return self._DvAuthKeySubDomain

    @DvAuthKeySubDomain.setter
    def DvAuthKeySubDomain(self, DvAuthKeySubDomain):
        self._DvAuthKeySubDomain = DvAuthKeySubDomain

    @property
    def DvAuths(self):
        return self._DvAuths

    @DvAuths.setter
    def DvAuths(self, DvAuths):
        self._DvAuths = DvAuths


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self._DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvAuths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DvAuths(AbstractModel):
    """Content of the `DvAuths` parameter

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param _DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param _DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param _DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param _DvAuthSubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthSubDomain: str
        :param _DvAuthVerifyType: DV authentication type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthVerifyType: str
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthSubDomain = None
        self._DvAuthVerifyType = None

    @property
    def DvAuthKey(self):
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthSubDomain(self):
        return self._DvAuthSubDomain

    @DvAuthSubDomain.setter
    def DvAuthSubDomain(self, DvAuthSubDomain):
        self._DvAuthSubDomain = DvAuthSubDomain

    @property
    def DvAuthVerifyType(self):
        return self._DvAuthVerifyType

    @DvAuthVerifyType.setter
    def DvAuthVerifyType(self, DvAuthVerifyType):
        self._DvAuthVerifyType = DvAuthVerifyType


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthSubDomain = params.get("DvAuthSubDomain")
        self._DvAuthVerifyType = params.get("DvAuthVerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Error(AbstractModel):
    """Errors

    """

    def __init__(self):
        r"""
        :param _Code: The error code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param _Message: The error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """List of filter parameters

    """

    def __init__(self):
        r"""
        :param _FilterKey: The key of the filter parameter.
        :type FilterKey: str
        :param _FilterValue: u200cThe value of the filter parameter.
        :type FilterValue: str
        """
        self._FilterKey = None
        self._FilterValue = None

    @property
    def FilterKey(self):
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def FilterValue(self):
        return self._FilterValue

    @FilterValue.setter
    def FilterValue(self, FilterValue):
        self._FilterValue = FilterValue


    def _deserialize(self, params):
        self._FilterKey = params.get("FilterKey")
        self._FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayCertificate(AbstractModel):
    """Cloud-native gateway certificate information

    """

    def __init__(self):
        r"""
        :param _Id: Gateway certificate ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type Id: str
        :param _Name: Gateway certificate information
Note: This field may return null, indicating that no valid value can be obtained.
        :type Name: str
        :param _BindDomains: Bound domain name
Note: This field may return null, indicating that no valid value can be obtained.
        :type BindDomains: list of str
        :param _CertSource: Certificate source
Note: This field may return null, indicating that no valid value can be obtained.
        :type CertSource: str
        :param _CertId: SSL certificate ID that is currently bound
Note: This field may return null, indicating that no valid value can be obtained.
        :type CertId: str
        """
        self._Id = None
        self._Name = None
        self._BindDomains = None
        self._CertSource = None
        self._CertId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BindDomains(self):
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def CertSource(self):
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BindDomains = params.get("BindDomains")
        self._CertSource = params.get("CertSource")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceDetail(AbstractModel):
    """Details of a LIVE instance

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _CertId: The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Status: The status. Valid values: `-1`: No certificate is associated with the domain.
`1`: HTTPS is enabled for the domain.
`0`: HTTPS is disabled for the domain.
        :type Status: int
        """
        self._Domain = None
        self._CertId = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceList(AbstractModel):
    """Details of LIVE instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of LIVE instances in this region.	
        :type TotalCount: int
        :param _InstanceList: The list of LIVE instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of LiveInstanceDetail
        """
        self._TotalCount = None
        self._InstanceList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCSRRequest(AbstractModel):
    """ModifyCSR request structure.

    """

    def __init__(self):
        r"""
        :param _CSRId: The CSR ID.	
        :type CSRId: int
        :param _Generate: Whether to generate the CSR content. Once the CSR content is generated, the CSR record cannot be modified.
        :type Generate: bool
        :param _Domain: The domain.
        :type Domain: str
        :param _Organization: The organization name.
        :type Organization: str
        :param _Department: The department.
        :type Department: str
        :param _Email: The email address.
        :type Email: str
        :param _Province: The province.
        :type Province: str
        :param _City: The city.
        :type City: str
        :param _Country: The country or region.
        :type Country: str
        :param _EncryptAlgo: The encryption algorithm. RSA and ECC are supported.	
        :type EncryptAlgo: str
        :param _KeyParameter: The key pair parameter. For RSA, only the 2048-bit and 4096-bit key pairs are supported. For ECC, only prime256v1 is supported.
        :type KeyParameter: str
        :param _Remark: The remarks.
        :type Remark: str
        :param _KeyPassword: The password of the private key.
        :type KeyPassword: str
        """
        self._CSRId = None
        self._Generate = None
        self._Domain = None
        self._Organization = None
        self._Department = None
        self._Email = None
        self._Province = None
        self._City = None
        self._Country = None
        self._EncryptAlgo = None
        self._KeyParameter = None
        self._Remark = None
        self._KeyPassword = None

    @property
    def CSRId(self):
        return self._CSRId

    @CSRId.setter
    def CSRId(self, CSRId):
        self._CSRId = CSRId

    @property
    def Generate(self):
        return self._Generate

    @Generate.setter
    def Generate(self, Generate):
        self._Generate = Generate

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword


    def _deserialize(self, params):
        self._CSRId = params.get("CSRId")
        self._Generate = params.get("Generate")
        self._Domain = params.get("Domain")
        self._Organization = params.get("Organization")
        self._Department = params.get("Department")
        self._Email = params.get("Email")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._EncryptAlgo = params.get("EncryptAlgo")
        self._KeyParameter = params.get("KeyParameter")
        self._Remark = params.get("Remark")
        self._KeyPassword = params.get("KeyPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCSRResponse(AbstractModel):
    """ModifyCSR response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The CSR ID.
        :type Id: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _Alias: Alias
        :type Alias: str
        """
        self._CertificateId = None
        self._Alias = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: ID of the successfully modified certificate
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateIdList: ID list of certificates whose projects need to be modified. A maximum of 100 certificate IDs are supported.
        :type CertificateIdList: list of str
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._CertificateIdList = None
        self._ProjectId = None

    @property
    def CertificateIdList(self):
        return self._CertificateIdList

    @CertificateIdList.setter
    def CertificateIdList(self, CertificateIdList):
        self._CertificateIdList = CertificateIdList

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._CertificateIdList = params.get("CertificateIdList")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessCertificates: List of certificates whose projects were modified successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :type SuccessCertificates: list of str
        :param _FailCertificates: List of certificates whose projects failed to be modified
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailCertificates: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessCertificates = None
        self._FailCertificates = None
        self._RequestId = None

    @property
    def SuccessCertificates(self):
        return self._SuccessCertificates

    @SuccessCertificates.setter
    def SuccessCertificates(self, SuccessCertificates):
        self._SuccessCertificates = SuccessCertificates

    @property
    def FailCertificates(self):
        return self._FailCertificates

    @FailCertificates.setter
    def FailCertificates(self, FailCertificates):
        self._FailCertificates = FailCertificates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessCertificates = params.get("SuccessCertificates")
        self._FailCertificates = params.get("FailCertificates")
        self._RequestId = params.get("RequestId")


class ModifyCertificateResubmitRequest(AbstractModel):
    """ModifyCertificateResubmit request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: The certificate ID.
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateResubmitResponse(AbstractModel):
    """ModifyCertificateResubmit response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: The certificate ID.
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """Certificate operation logs

    """

    def __init__(self):
        r"""
        :param _Action: Action performed on logs
        :type Action: str
        :param _CreatedOn: Time when the action is performed
        :type CreatedOn: str
        """
        self._Action = None
        self._CreatedOn = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreAuditInfo(AbstractModel):
    """List of prereview information

    """

    def __init__(self):
        r"""
        :param _TotalPeriod: Total number of years of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPeriod: int
        :param _NowPeriod: Current year of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type NowPeriod: int
        :param _ManagerId: Certificate prereview manager ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManagerId: str
        """
        self._TotalPeriod = None
        self._NowPeriod = None
        self._ManagerId = None

    @property
    def TotalPeriod(self):
        return self._TotalPeriod

    @TotalPeriod.setter
    def TotalPeriod(self, TotalPeriod):
        self._TotalPeriod = TotalPeriod

    @property
    def NowPeriod(self):
        return self._NowPeriod

    @NowPeriod.setter
    def NowPeriod(self, NowPeriod):
        self._NowPeriod = NowPeriod

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._TotalPeriod = params.get("TotalPeriod")
        self._NowPeriod = params.get("NowPeriod")
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """Content of the `ProjectInfo` parameter. `ProjectInfo` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        r"""
        :param _ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _ProjectCreatorUin: UIN of the project creator
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectCreatorUin: int
        :param _ProjectCreateTime: Project creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectCreateTime: str
        :param _ProjectResume: Brief project information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectResume: str
        :param _OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: int
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        """
        self._ProjectName = None
        self._ProjectCreatorUin = None
        self._ProjectCreateTime = None
        self._ProjectResume = None
        self._OwnerUin = None
        self._ProjectId = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectCreatorUin(self):
        return self._ProjectCreatorUin

    @ProjectCreatorUin.setter
    def ProjectCreatorUin(self, ProjectCreatorUin):
        self._ProjectCreatorUin = ProjectCreatorUin

    @property
    def ProjectCreateTime(self):
        return self._ProjectCreateTime

    @ProjectCreateTime.setter
    def ProjectCreateTime(self, ProjectCreateTime):
        self._ProjectCreateTime = ProjectCreateTime

    @property
    def ProjectResume(self):
        return self._ProjectResume

    @ProjectResume.setter
    def ProjectResume(self, ProjectResume):
        self._ProjectResume = ProjectResume

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectCreatorUin = params.get("ProjectCreatorUin")
        self._ProjectCreateTime = params.get("ProjectCreateTime")
        self._ProjectResume = params.get("ProjectResume")
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _ValidType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation
        :type ValidType: str
        :param _CsrType: Type. `original`: original certificate CSR; `upload`: uploaded manually; `online`: generated online. The default value is original.
        :type CsrType: str
        :param _CsrContent: CSR content
        :type CsrContent: str
        :param _CsrkeyPassword: Password of the key
        :type CsrkeyPassword: str
        :param _Reason: Reissue reason
        :type Reason: str
        :param _CertCSREncryptAlgo: The CSR encryption algorithm. Valid values: `RSA` (default), `ECC1`, and `SM2`.
This parameter is available for selection only when the value of `CsrType` is `Online`.
        :type CertCSREncryptAlgo: str
        :param _CertCSRKeyParameter: The CSR encryption parameters. When `CsrEncryptAlgo` is set to `RSA`, `2048` (default) and `4096` are available for selection; and when`CsrEncryptAlgo` is set to `ECC`, `prime256v1` (default) and `secp384r1` are available for selection. 
        :type CertCSRKeyParameter: str
        """
        self._CertificateId = None
        self._ValidType = None
        self._CsrType = None
        self._CsrContent = None
        self._CsrkeyPassword = None
        self._Reason = None
        self._CertCSREncryptAlgo = None
        self._CertCSRKeyParameter = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ValidType(self):
        return self._ValidType

    @ValidType.setter
    def ValidType(self, ValidType):
        self._ValidType = ValidType

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CsrkeyPassword(self):
        return self._CsrkeyPassword

    @CsrkeyPassword.setter
    def CsrkeyPassword(self, CsrkeyPassword):
        self._CsrkeyPassword = CsrkeyPassword

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def CertCSREncryptAlgo(self):
        return self._CertCSREncryptAlgo

    @CertCSREncryptAlgo.setter
    def CertCSREncryptAlgo(self, CertCSREncryptAlgo):
        self._CertCSREncryptAlgo = CertCSREncryptAlgo

    @property
    def CertCSRKeyParameter(self):
        return self._CertCSRKeyParameter

    @CertCSRKeyParameter.setter
    def CertCSRKeyParameter(self, CertCSRKeyParameter):
        self._CertCSRKeyParameter = CertCSRKeyParameter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ValidType = params.get("ValidType")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CsrkeyPassword = params.get("CsrkeyPassword")
        self._Reason = params.get("Reason")
        self._CertCSREncryptAlgo = params.get("CertCSREncryptAlgo")
        self._CertCSRKeyParameter = params.get("CertCSRKeyParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ResourceTypeRegions(AbstractModel):
    """Cloud resource region list

    """

    def __init__(self):
        r"""
        :param _ResourceType: Cloud resource type
        :type ResourceType: str
        :param _Regions: Region list
        :type Regions: list of str
        """
        self._ResourceType = None
        self._Regions = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RootCertificates(AbstractModel):
    """Root certificate

    """

    def __init__(self):
        r"""
        :param _Sign: Chinese SM signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sign: str
        :param _Encrypt: Chinese SM encryption certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: str
        :param _Standard: Standard certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Standard: str
        """
        self._Sign = None
        self._Encrypt = None
        self._Standard = None

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Standard(self):
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._Encrypt = params.get("Encrypt")
        self._Standard = params.get("Standard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _CsrType: CSR generation mode. `online`: generated online; `parse`: uploaded manually
        :type CsrType: str
        :param _CsrContent: Uploaded CSR content
        :type CsrContent: str
        :param _CertificateDomain: Domain name bound with the certificate
        :type CertificateDomain: str
        :param _DomainList: Uploaded domain name array (can be uploaded for a multi-domain certificate)
        :type DomainList: list of str
        :param _KeyPassword: Password of the private key
        :type KeyPassword: str
        :param _OrganizationName: Organization name
        :type OrganizationName: str
        :param _OrganizationDivision: Division name
        :type OrganizationDivision: str
        :param _OrganizationAddress: Detailed address of the organization
        :type OrganizationAddress: str
        :param _OrganizationCountry: Country where the organization is located, for example, CN (China)
        :type OrganizationCountry: str
        :param _OrganizationCity: City where the organization is located
        :type OrganizationCity: str
        :param _OrganizationRegion: Province where the organization is located
        :type OrganizationRegion: str
        :param _PostalCode: Postal code of the organization
        :type PostalCode: str
        :param _PhoneAreaCode: Area code of the fixed-line phone number of the organization
        :type PhoneAreaCode: str
        :param _PhoneNumber: Fixed-line phone number of the organization
        :type PhoneNumber: str
        :param _VerifyType: Certificate validation method
        :type VerifyType: str
        :param _AdminFirstName: Last name of the administrator
        :type AdminFirstName: str
        :param _AdminLastName: First name of the administrator
        :type AdminLastName: str
        :param _AdminPhoneNum: Mobile number of the administrator
        :type AdminPhoneNum: str
        :param _AdminEmail: Email of the administrator
        :type AdminEmail: str
        :param _AdminPosition: Position of the administrator
        :type AdminPosition: str
        :param _ContactFirstName: Last name of the contact
        :type ContactFirstName: str
        :param _ContactLastName: First name of the contact
        :type ContactLastName: str
        :param _ContactEmail: Email of the contact
        :type ContactEmail: str
        :param _ContactNumber: Mobile number of the contact
        :type ContactNumber: str
        :param _ContactPosition: Position of the contact
        :type ContactPosition: str
        """
        self._CertificateId = None
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._VerifyType = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactEmail = None
        self._ContactNumber = None
        self._ContactPosition = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def AdminFirstName(self):
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactPosition(self):
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._VerifyType = params.get("VerifyType")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactPosition = params.get("ContactPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """Content of the `SubmittedData` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param _CsrType: CSR type. `online`: CSR generated online; `parse`: CSR pasted
Note: this field may return null, indicating that no valid values can be obtained.
        :type CsrType: str
        :param _CsrContent: CSR content
Note: this field may return null, indicating that no valid values can be obtained.
        :type CsrContent: str
        :param _CertificateDomain: Domain name information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateDomain: str
        :param _DomainList: DNS information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainList: list of str
        :param _KeyPassword: Password of the private key
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyPassword: str
        :param _OrganizationName: Enterprise or unit name
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationName: str
        :param _OrganizationDivision: Division
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationDivision: str
        :param _OrganizationAddress: Address
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationAddress: str
        :param _OrganizationCountry: Country
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationCountry: str
        :param _OrganizationCity: City
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationCity: str
        :param _OrganizationRegion: Province
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationRegion: str
        :param _PostalCode: Postal code
Note: this field may return null, indicating that no valid values can be obtained.
        :type PostalCode: str
        :param _PhoneAreaCode: Area code of the fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneAreaCode: str
        :param _PhoneNumber: Fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param _AdminFirstName: First name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminFirstName: str
        :param _AdminLastName: Last name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminLastName: str
        :param _AdminPhoneNum: Phone number of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminPhoneNum: str
        :param _AdminEmail: Email of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminEmail: str
        :param _AdminPosition: Position of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminPosition: str
        :param _ContactFirstName: First name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactFirstName: str
        :param _ContactLastName: Last name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactLastName: str
        :param _ContactNumber: Phone number of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactNumber: str
        :param _ContactEmail: Email of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactEmail: str
        :param _ContactPosition: Position of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactPosition: str
        :param _VerifyType: Validation type
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        """
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactNumber = None
        self._ContactEmail = None
        self._ContactPosition = None
        self._VerifyType = None

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AdminFirstName(self):
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPosition(self):
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPosition = params.get("ContactPosition")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportDownloadType(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _NGINX: 
        :type NGINX: bool
        :param _APACHE: 
        :type APACHE: bool
        :param _TOMCAT: 
        :type TOMCAT: bool
        :param _IIS: 
        :type IIS: bool
        :param _JKS: 
        :type JKS: bool
        :param _OTHER: 
        :type OTHER: bool
        :param _ROOT: 
        :type ROOT: bool
        """
        self._NGINX = None
        self._APACHE = None
        self._TOMCAT = None
        self._IIS = None
        self._JKS = None
        self._OTHER = None
        self._ROOT = None

    @property
    def NGINX(self):
        return self._NGINX

    @NGINX.setter
    def NGINX(self, NGINX):
        self._NGINX = NGINX

    @property
    def APACHE(self):
        return self._APACHE

    @APACHE.setter
    def APACHE(self, APACHE):
        self._APACHE = APACHE

    @property
    def TOMCAT(self):
        return self._TOMCAT

    @TOMCAT.setter
    def TOMCAT(self, TOMCAT):
        self._TOMCAT = TOMCAT

    @property
    def IIS(self):
        return self._IIS

    @IIS.setter
    def IIS(self, IIS):
        self._IIS = IIS

    @property
    def JKS(self):
        return self._JKS

    @JKS.setter
    def JKS(self, JKS):
        self._JKS = JKS

    @property
    def OTHER(self):
        return self._OTHER

    @OTHER.setter
    def OTHER(self, OTHER):
        self._OTHER = OTHER

    @property
    def ROOT(self):
        return self._ROOT

    @ROOT.setter
    def ROOT(self, ROOT):
        self._ROOT = ROOT


    def _deserialize(self, params):
        self._NGINX = params.get("NGINX")
        self._APACHE = params.get("APACHE")
        self._TOMCAT = params.get("TOMCAT")
        self._IIS = params.get("IIS")
        self._JKS = params.get("JKS")
        self._OTHER = params.get("OTHER")
        self._ROOT = params.get("ROOT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTaskBindResourceResult(AbstractModel):
    """Result of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _BindResourceResult: The associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BindResourceResult: list of BindResourceResult
        :param _Status: The status of the async task. Valid values: `0` for querying, `1` for successful, and `2` for abnormal. If the status is `1`, the result of `BindResourceResult` will be displayed; if the status is `2`, the error causes will be displayed.
        :type Status: int
        :param _Error: The error occurred when querying the associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Error: :class:`tencentcloud.ssl.v20191205.models.Error`
        :param _CacheTime: The cache time of the current result.
        :type CacheTime: str
        """
        self._TaskId = None
        self._BindResourceResult = None
        self._Status = None
        self._Error = None
        self._CacheTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BindResourceResult(self):
        return self._BindResourceResult

    @BindResourceResult.setter
    def BindResourceResult(self, BindResourceResult):
        self._BindResourceResult = BindResourceResult

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("BindResourceResult") is not None:
            self._BindResourceResult = []
            for item in params.get("BindResourceResult"):
                obj = BindResourceResult()
                obj._deserialize(item)
                self._BindResourceResult.append(obj)
        self._Status = params.get("Status")
        if params.get("Error") is not None:
            self._Error = Error()
            self._Error._deserialize(params.get("Error"))
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBAccessInstance(AbstractModel):
    """TCB access instances

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Status: The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _UnionStatus: The unified domain status.

Note: This field may return null, indicating that no valid values can be obtained.
        :type UnionStatus: int
        :param _IsPreempted: Whether the domain is preempted. A preempted domain is one that is already associated with another environment. It must be disassociated or re-associated first.

Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPreempted: bool
        :param _ICPStatus: Whether the domain is added to the ICP blocklist. Valid values: `0` for no and `1` for yes.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ICPStatus: int
        :param _OldCertificateId: The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OldCertificateId: str
        """
        self._Domain = None
        self._Status = None
        self._UnionStatus = None
        self._IsPreempted = None
        self._ICPStatus = None
        self._OldCertificateId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnionStatus(self):
        return self._UnionStatus

    @UnionStatus.setter
    def UnionStatus(self, UnionStatus):
        self._UnionStatus = UnionStatus

    @property
    def IsPreempted(self):
        return self._IsPreempted

    @IsPreempted.setter
    def IsPreempted(self, IsPreempted):
        self._IsPreempted = IsPreempted

    @property
    def ICPStatus(self):
        return self._ICPStatus

    @ICPStatus.setter
    def ICPStatus(self, ICPStatus):
        self._ICPStatus = ICPStatus

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._UnionStatus = params.get("UnionStatus")
        self._IsPreempted = params.get("IsPreempted")
        self._ICPStatus = params.get("ICPStatus")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBAccessService(AbstractModel):
    """Details of TCB access instances

    """

    def __init__(self):
        r"""
        :param _InstanceList: The list of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TCBAccessInstance
        :param _TotalCount: The instance count.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TCBAccessInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBEnvironment(AbstractModel):
    """Details of TCB environment instance

    """

    def __init__(self):
        r"""
        :param _ID: The unique ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _Source: The source.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Source: str
        :param _Name: The name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Status: The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._ID = None
        self._Source = None
        self._Name = None
        self._Status = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBEnvironments(AbstractModel):
    """Details of TCB instances by environment - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Environment: The TCB environment.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Environment: :class:`tencentcloud.ssl.v20191205.models.TCBEnvironment`
        :param _AccessService: The access service.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessService: :class:`tencentcloud.ssl.v20191205.models.TCBAccessService`
        :param _HostService: Whether static hosting is used.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostService: :class:`tencentcloud.ssl.v20191205.models.TCBHostService`
        """
        self._Environment = None
        self._AccessService = None
        self._HostService = None

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AccessService(self):
        return self._AccessService

    @AccessService.setter
    def AccessService(self, AccessService):
        self._AccessService = AccessService

    @property
    def HostService(self):
        return self._HostService

    @HostService.setter
    def HostService(self, HostService):
        self._HostService = HostService


    def _deserialize(self, params):
        if params.get("Environment") is not None:
            self._Environment = TCBEnvironment()
            self._Environment._deserialize(params.get("Environment"))
        if params.get("AccessService") is not None:
            self._AccessService = TCBAccessService()
            self._AccessService._deserialize(params.get("AccessService"))
        if params.get("HostService") is not None:
            self._HostService = TCBHostService()
            self._HostService._deserialize(params.get("HostService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBHostInstance(AbstractModel):
    """Details of TCB service instances subject to static hosting

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Status: The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _DNSStatus: The resolution status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DNSStatus: str
        :param _OldCertificateId: The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OldCertificateId: str
        """
        self._Domain = None
        self._Status = None
        self._DNSStatus = None
        self._OldCertificateId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DNSStatus(self):
        return self._DNSStatus

    @DNSStatus.setter
    def DNSStatus(self, DNSStatus):
        self._DNSStatus = DNSStatus

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._DNSStatus = params.get("DNSStatus")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBHostService(AbstractModel):
    """List of TCB services subject to static hosting

    """

    def __init__(self):
        r"""
        :param _InstanceList: The list of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TCBHostInstance
        :param _TotalCount: The instance count.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TCBHostInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBInstanceList(AbstractModel):
    """Details of TCB instances by region - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
        :type Region: str
        :param _Environments: The list of TCB environments.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Environments: list of TCBEnvironments
        """
        self._Region = None
        self._Environments = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Environments(self):
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = TCBEnvironments()
                obj._deserialize(item)
                self._Environments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TSEInstanceDetail(AbstractModel):
    """TSE instance details

    """

    def __init__(self):
        r"""
        :param _GatewayId: Gateway ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type GatewayId: str
        :param _GatewayName: Gateway name
Note: This field may return null, indicating that no valid value can be obtained.
        :type GatewayName: str
        :param _CertificateList: Gateway certificate list
Note: This field may return null, indicating that no valid value can be obtained.
        :type CertificateList: list of GatewayCertificate
        """
        self._GatewayId = None
        self._GatewayName = None
        self._CertificateList = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def CertificateList(self):
        return self._CertificateList

    @CertificateList.setter
    def CertificateList(self, CertificateList):
        self._CertificateList = CertificateList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GatewayName = params.get("GatewayName")
        if params.get("CertificateList") is not None:
            self._CertificateList = []
            for item in params.get("CertificateList"):
                obj = GatewayCertificate()
                obj._deserialize(item)
                self._CertificateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TSEInstanceList(AbstractModel):
    """TSE instance details - asynchronously associated cloud resource data structure

    """

    def __init__(self):
        r"""
        :param _InstanceList: TSE instance details
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceList: list of TSEInstanceDetail
        :param _TotalCount: Total TSE instances in this region	
        :type TotalCount: int
        :param _Region: Region	
        :type Region: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Region = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TSEInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """Tag

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
        


class TeoInstanceDetail(AbstractModel):
    """Details of TEO instances

    """

    def __init__(self):
        r"""
        :param _Host: The domain.
        :type Host: str
        :param _CertId: The certificate ID.
        :type CertId: str
        :param _ZoneId: The AZ ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param _Status: The status of the domain.
        :type Status: str
        """
        self._Host = None
        self._CertId = None
        self._ZoneId = None
        self._Status = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._CertId = params.get("CertId")
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeoInstanceList(AbstractModel):
    """Details of the EDGEONE instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _InstanceList: The list of EDGEONE instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: The total number of EDGEONE instances.	
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeIngressDetail(AbstractModel):
    """Details of a TKE Ingress instance

    """

    def __init__(self):
        r"""
        :param _IngressName: The Ingress name.
        :type IngressName: str
        :param _TlsDomains: The list of TLS domains.
        :type TlsDomains: list of str
        :param _Domains: The list of Ingress domains.
        :type Domains: list of str
        """
        self._IngressName = None
        self._TlsDomains = None
        self._Domains = None

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def TlsDomains(self):
        return self._TlsDomains

    @TlsDomains.setter
    def TlsDomains(self, TlsDomains):
        self._TlsDomains = TlsDomains

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._IngressName = params.get("IngressName")
        self._TlsDomains = params.get("TlsDomains")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceDetail(AbstractModel):
    """Details of a TKE instance

    """

    def __init__(self):
        r"""
        :param _ClusterId: The cluster ID.
        :type ClusterId: str
        :param _ClusterName: The cluster name.
        :type ClusterName: str
        :param _NamespaceList: The list of cluster namespaces.
        :type NamespaceList: list of TkeNameSpaceDetail
        :param _ClusterType: The cluster type.
        :type ClusterType: str
        :param _ClusterVersion: The cluster version.
        :type ClusterVersion: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._NamespaceList = None
        self._ClusterType = None
        self._ClusterVersion = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TkeNameSpaceDetail()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        self._ClusterType = params.get("ClusterType")
        self._ClusterVersion = params.get("ClusterVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceList(AbstractModel):
    """Details of TKE instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
        :type Region: str
        :param _InstanceList: The list of TKE instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TkeInstanceDetail
        :param _TotalCount: The total number of TKE instances in this region.	
        :type TotalCount: int
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeNameSpaceDetail(AbstractModel):
    """Details of a TKE namespace

    """

    def __init__(self):
        r"""
        :param _Name: The namespace name.
        :type Name: str
        :param _SecretList: The secret list.
        :type SecretList: list of TkeSecretDetail
        """
        self._Name = None
        self._SecretList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecretList(self):
        return self._SecretList

    @SecretList.setter
    def SecretList(self, SecretList):
        self._SecretList = SecretList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("SecretList") is not None:
            self._SecretList = []
            for item in params.get("SecretList"):
                obj = TkeSecretDetail()
                obj._deserialize(item)
                self._SecretList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeSecretDetail(AbstractModel):
    """Details of a TKE secret

    """

    def __init__(self):
        r"""
        :param _Name: The secret name.
        :type Name: str
        :param _CertId: The certificate ID.
        :type CertId: str
        :param _IngressList: The Ingress list.
        :type IngressList: list of TkeIngressDetail
        :param _NoMatchDomains: The list of domains that do not match the new certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoMatchDomains: list of str
        """
        self._Name = None
        self._CertId = None
        self._IngressList = None
        self._NoMatchDomains = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def IngressList(self):
        return self._IngressList

    @IngressList.setter
    def IngressList(self, IngressList):
        self._IngressList = IngressList

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CertId = params.get("CertId")
        if params.get("IngressList") is not None:
            self._IngressList = []
            for item in params.get("IngressList"):
                obj = TkeIngressDetail()
                obj._deserialize(item)
                self._IngressList.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceRequest(AbstractModel):
    """UpdateCertificateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _OldCertificateId: One-click update old certificate ID
        :type OldCertificateId: str
        :param _ResourceTypes: Type of the resource that needs to be deployed. The following parameter values are optional: clb, cdn, waf, live, ddos, teo, apigateway, vod, tke, and tcb.
        :type ResourceTypes: list of str
        :param _CertificateId: One-click update new certificate ID
        :type CertificateId: str
        :param _Regions: List of regions that need to be deployed (deprecated)
        :type Regions: list of str
        :param _ResourceTypesRegions: List of regions for which cloud resources need to be deployed
        :type ResourceTypesRegions: list of ResourceTypeRegions
        :param _CertificatePublicKey: Public key of the certificate. If the public key of the certificate is uploaded, CertificateId does not need to be uploaded.
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: Private key of the certificate. If the public key of the certificate is uploaded, the private key of the certificate is required.
        :type CertificatePrivateKey: str
        :param _ExpiringNotificationSwitch: Whether an expiration reminder is ignored for the old certificate. 0: The notification is not ignored. 1: The notification is ignored.
        :type ExpiringNotificationSwitch: int
        :param _Repeatable: Whether repeated uploading of the same certificate is allowed. If the public key of the certificate is uploaded, this parameter can be configured.
        :type Repeatable: bool
        :param _AllowDownload: Whether downloading is allowed. If the public key of the certificate is uploaded, this parameter can be configured.
        :type AllowDownload: bool
        :param _Tags: Tag list. If the public key of the certificate is uploaded, this parameter can be configured.
        :type Tags: list of Tags
        :param _ProjectId: Project ID. If the public key of the certificate is uploaded, this parameter can be configured.
        :type ProjectId: int
        """
        self._OldCertificateId = None
        self._ResourceTypes = None
        self._CertificateId = None
        self._Regions = None
        self._ResourceTypesRegions = None
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._ExpiringNotificationSwitch = None
        self._Repeatable = None
        self._AllowDownload = None
        self._Tags = None
        self._ProjectId = None

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Regions(self):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        self._Regions = Regions

    @property
    def ResourceTypesRegions(self):
        return self._ResourceTypesRegions

    @ResourceTypesRegions.setter
    def ResourceTypesRegions(self, ResourceTypesRegions):
        self._ResourceTypesRegions = ResourceTypesRegions

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def ExpiringNotificationSwitch(self):
        return self._ExpiringNotificationSwitch

    @ExpiringNotificationSwitch.setter
    def ExpiringNotificationSwitch(self, ExpiringNotificationSwitch):
        self._ExpiringNotificationSwitch = ExpiringNotificationSwitch

    @property
    def Repeatable(self):
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable

    @property
    def AllowDownload(self):
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._OldCertificateId = params.get("OldCertificateId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._CertificateId = params.get("CertificateId")
        self._Regions = params.get("Regions")
        if params.get("ResourceTypesRegions") is not None:
            self._ResourceTypesRegions = []
            for item in params.get("ResourceTypesRegions"):
                obj = ResourceTypeRegions()
                obj._deserialize(item)
                self._ResourceTypesRegions.append(obj)
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._ExpiringNotificationSwitch = params.get("ExpiringNotificationSwitch")
        self._Repeatable = params.get("Repeatable")
        self._AllowDownload = params.get("AllowDownload")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceResponse(AbstractModel):
    """UpdateCertificateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: Cloud resource deployment task ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type DeployRecordId: int
        :param _DeployStatus: Deployment status. 1 indicates that the deployment succeeded, and 0 indicates that the deployment failed.
        :type DeployStatus: int
        :param _UpdateSyncProgress: 
        :type UpdateSyncProgress: list of UpdateSyncProgress
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._UpdateSyncProgress = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def UpdateSyncProgress(self):
        return self._UpdateSyncProgress

    @UpdateSyncProgress.setter
    def UpdateSyncProgress(self, UpdateSyncProgress):
        self._UpdateSyncProgress = UpdateSyncProgress

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployStatus = params.get("DeployStatus")
        if params.get("UpdateSyncProgress") is not None:
            self._UpdateSyncProgress = []
            for item in params.get("UpdateSyncProgress"):
                obj = UpdateSyncProgress()
                obj._deserialize(item)
                self._UpdateSyncProgress.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateCertificateRecordRetryRequest(AbstractModel):
    """UpdateCertificateRecordRetry request structure.

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: To-be-redeployed record ID
        :type DeployRecordId: int
        :param _DeployRecordDetailId: To-be-redeployed record detail ID
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        return self._DeployRecordDetailId

    @DeployRecordDetailId.setter
    def DeployRecordDetailId(self, DeployRecordDetailId):
        self._DeployRecordDetailId = DeployRecordDetailId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRetryResponse(AbstractModel):
    """UpdateCertificateRecordRetry response structure.

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


class UpdateCertificateRecordRollbackRequest(AbstractModel):
    """UpdateCertificateRecordRollback request structure.

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: To-be-redeployed record ID
        :type DeployRecordId: int
        """
        self._DeployRecordId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRollbackResponse(AbstractModel):
    """UpdateCertificateRecordRollback response structure.

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: Rollback deployment record ID
        :type DeployRecordId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class UpdateRecordDetail(AbstractModel):
    """Update record details

    """

    def __init__(self):
        r"""
        :param _Id: Detail record ID
        :type Id: int
        :param _CertId: New certificate ID
        :type CertId: str
        :param _OldCertId: Old certificate ID
        :type OldCertId: str
        :param _Domains: Deployment domain name list
Note: This field may return null, indicating that no valid value can be obtained.
        :type Domains: list of str
        :param _ResourceType: Deployment resource type
        :type ResourceType: str
        :param _Region: Deployment region
Note: This field may return null, indicating that no valid value can be obtained.
        :type Region: str
        :param _Status: Deployment status
        :type Status: int
        :param _ErrorMsg: Deployment error message
Note: This field may return null, indicating that no valid value can be obtained.
        :type ErrorMsg: str
        :param _CreateTime: Deployment time
        :type CreateTime: str
        :param _UpdateTime: Last update time
        :type UpdateTime: str
        :param _InstanceId: Deployment instance ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceId: str
        :param _InstanceName: Deployment instance name
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceName: str
        :param _ListenerId: Deployment listener ID (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :type ListenerId: str
        :param _ListenerName: Deployment listener name (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :type ListenerName: str
        :param _Protocol: Protocol
Note: This field may return null, indicating that no valid value can be obtained.
        :type Protocol: str
        :param _SniSwitch: Whether SNI is enabled (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :type SniSwitch: int
        :param _Bucket: Bucket name (only for COS)
Note: This field may return null, indicating that no valid value can be obtained.
        :type Bucket: str
        :param _Port: Port
Note: This field may return null, indicating that no valid value can be obtained.
        :type Port: int
        :param _Namespace: Namespace (only for TKE)
Note: This field may return null, indicating that no valid value can be obtained.
        :type Namespace: str
        :param _SecretName: Secret name (only for TKE)
Note: This field may return null, indicating that no valid value can be obtained.
        :type SecretName: str
        :param _EnvId: Environment ID
Note: This field may return null, indicating that no valid value can be obtained.
        :type EnvId: str
        :param _TCBType: TCB deployment type
Note: This field may return null, indicating that no valid value can be obtained.
        :type TCBType: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._Domains = None
        self._ResourceType = None
        self._Region = None
        self._Status = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._InstanceId = None
        self._InstanceName = None
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._SniSwitch = None
        self._Bucket = None
        self._Port = None
        self._Namespace = None
        self._SecretName = None
        self._EnvId = None
        self._TCBType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TCBType(self):
        return self._TCBType

    @TCBType.setter
    def TCBType(self, TCBType):
        self._TCBType = TCBType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._Domains = params.get("Domains")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._SniSwitch = params.get("SniSwitch")
        self._Bucket = params.get("Bucket")
        self._Port = params.get("Port")
        self._Namespace = params.get("Namespace")
        self._SecretName = params.get("SecretName")
        self._EnvId = params.get("EnvId")
        self._TCBType = params.get("TCBType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordDetails(AbstractModel):
    """Update record detail list

    """

    def __init__(self):
        r"""
        :param _ResourceType: Deployment resource type
        :type ResourceType: str
        :param _List: Deployment resource detail list
        :type List: list of UpdateRecordDetail
        :param _TotalCount: Total deployment resource count
        :type TotalCount: int
        """
        self._ResourceType = None
        self._List = None
        self._TotalCount = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UpdateRecordDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordInfo(AbstractModel):
    """Deployment record information

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: int
        :param _CertId: New certificate ID
        :type CertId: str
        :param _OldCertId: Old certificate ID
        :type OldCertId: str
        :param _ResourceTypes: Deployment resource type list
        :type ResourceTypes: list of str
        :param _Regions: Deployment region list
Note: This field may return null, indicating that no valid value can be obtained.
        :type Regions: list of str
        :param _Status: Deployment status
        :type Status: int
        :param _CreateTime: Deployment time
        :type CreateTime: str
        :param _UpdateTime: Last update time
        :type UpdateTime: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._ResourceTypes = None
        self._Regions = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSyncProgress(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _ResourceType: 
        :type ResourceType: str
        :param _UpdateSyncProgressRegions: 
        :type UpdateSyncProgressRegions: list of UpdateSyncProgressRegion
        :param _Status: 
        :type Status: int
        """
        self._ResourceType = None
        self._UpdateSyncProgressRegions = None
        self._Status = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def UpdateSyncProgressRegions(self):
        return self._UpdateSyncProgressRegions

    @UpdateSyncProgressRegions.setter
    def UpdateSyncProgressRegions(self, UpdateSyncProgressRegions):
        self._UpdateSyncProgressRegions = UpdateSyncProgressRegions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("UpdateSyncProgressRegions") is not None:
            self._UpdateSyncProgressRegions = []
            for item in params.get("UpdateSyncProgressRegions"):
                obj = UpdateSyncProgressRegion()
                obj._deserialize(item)
                self._UpdateSyncProgressRegions.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSyncProgressRegion(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Region: 
        :type Region: str
        :param _TotalCount: 
        :type TotalCount: int
        :param _OffsetCount: 
        :type OffsetCount: int
        :param _Status: 
        :type Status: int
        """
        self._Region = None
        self._TotalCount = None
        self._OffsetCount = None
        self._Status = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OffsetCount(self):
        return self._OffsetCount

    @OffsetCount.setter
    def OffsetCount(self, OffsetCount):
        self._OffsetCount = OffsetCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._TotalCount = params.get("TotalCount")
        self._OffsetCount = params.get("OffsetCount")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _CertificatePublicKey: Public key of the certificate
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: Private key content. This parameter is required when the certificate type is SVR, and not required when the certificate type is CA.
        :type CertificatePrivateKey: str
        :param _CertificateType: Certificate type. Valid values: `CA` (CA certificate) and `SVR` (server certificate). Default value: `SVR`
        :type CertificateType: str
        :param _Alias: Alias
        :type Alias: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CertificateUse: 
        :type CertificateUse: str
        :param _Tags: The list of tags.
        :type Tags: list of Tags
        :param _Repeatable: Whether a certificate can be repeatedly uploaded.
        :type Repeatable: bool
        """
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._CertificateType = None
        self._Alias = None
        self._ProjectId = None
        self._CertificateUse = None
        self._Tags = None
        self._Repeatable = None

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CertificateUse(self):
        return self._CertificateUse

    @CertificateUse.setter
    def CertificateUse(self, CertificateUse):
        self._CertificateUse = CertificateUse

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Repeatable(self):
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable


    def _deserialize(self, params):
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificateType = params.get("CertificateType")
        self._Alias = params.get("Alias")
        self._ProjectId = params.get("ProjectId")
        self._CertificateUse = params.get("CertificateUse")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Repeatable = params.get("Repeatable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _RepeatCertId: The ID of the repeatedly uploaded certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RepeatCertId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RepeatCertId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RepeatCertId(self):
        return self._RepeatCertId

    @RepeatCertId.setter
    def RepeatCertId(self, RepeatCertId):
        self._RepeatCertId = RepeatCertId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RepeatCertId = params.get("RepeatCertId")
        self._RequestId = params.get("RequestId")


class UploadConfirmLetterRequest(AbstractModel):
    """UploadConfirmLetter request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _ConfirmLetter: Base64-encoded confirmation letter file, which must be a JPG, JPEG, PNG, or PDF file of 1 KB to 1.4 MB
        :type ConfirmLetter: str
        """
        self._CertificateId = None
        self._ConfirmLetter = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ConfirmLetter(self):
        return self._ConfirmLetter

    @ConfirmLetter.setter
    def ConfirmLetter(self, ConfirmLetter):
        self._ConfirmLetter = ConfirmLetter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ConfirmLetter = params.get("ConfirmLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadConfirmLetterResponse(AbstractModel):
    """UploadConfirmLetter response structure.

    """

    def __init__(self):
        r"""
        :param _CertificateId: Certificate ID
        :type CertificateId: str
        :param _IsSuccess: Whether the operation is successful
        :type IsSuccess: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class VODInstanceList(AbstractModel):
    """Details of VOD instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _InstanceList: The list of VOD instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of VodInstanceDetail
        :param _TotalCount: The total number of VOD instances in this region.	
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodInstanceDetail(AbstractModel):
    """Details of a VOD instance

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _CertId: The certificate ID.
        :type CertId: str
        """
        self._Domain = None
        self._CertId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafInstanceDetail(AbstractModel):
    """Details of a WAF instance

    """

    def __init__(self):
        r"""
        :param _Domain: The domain.
        :type Domain: str
        :param _CertId: The certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Keepalive: Whether to keep the persistent connection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Keepalive: int
        """
        self._Domain = None
        self._CertId = None
        self._Keepalive = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Keepalive(self):
        return self._Keepalive

    @Keepalive.setter
    def Keepalive(self, Keepalive):
        self._Keepalive = Keepalive


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Keepalive = params.get("Keepalive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafInstanceList(AbstractModel):
    """Details of WAF instances - data structure of an async task for querying associated cloud resources

    """

    def __init__(self):
        r"""
        :param _Region: The region.
        :type Region: str
        :param _InstanceList: The list of WAF instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of WafInstanceDetail
        :param _TotalCount: The total number of WAF instances in this region.	
        :type TotalCount: int
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = WafInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        