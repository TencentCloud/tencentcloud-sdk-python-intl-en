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
        :param _CertId: Certificate id.
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
        """The instance ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        """The instance name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Domain(self):
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """Certificate id.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Protocol(self):
        """The protocol.
        :rtype: str
        """
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
        :param _InstanceList: API gateway instance details.	
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param _TotalCount: The total number of APIGATEWAY instances in this region.	
        :type TotalCount: int
        :param _Error: Whether to query exceptions.
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """The region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """API gateway instance details.	
        :rtype: list of ApiGatewayInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of APIGATEWAY instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
        :param _DvAuthMethod: Certificate domain validation methods:

DNS_AUTO: Automatically add domain DNS validation. Requires the user's domain to be hosted on 'Cloud DNS' and associated with the same Tencent Cloud account as the certificate application.

DNS: Manually add domain DNS validation. Requires the user to manually add the validation value at their domain's DNS service provider.

FILE: Manually add domain file validation. Requires the user to manually add a specified path file in the root directory of the domain site for file validation. Either HTTP or HTTPS validation will suffice; the domain site must be accessible by overseas CA institutions. The specific access whitelist is: 64.78.193.238, 216.168.247.9, 216.168.249.9, 54.189.196.217.
        :type DvAuthMethod: str
        :param _DomainName: The domain bound to the certificate.
        :type DomainName: str
        :param _ProjectId: The project ID associated with the certificate. Default is 0 (default project)
        :type ProjectId: int
        :param _PackageType: Certificate type, optional, currently only type 83 is supported. 83 = trustasia c1 dv free.
        :type PackageType: str
        :param _ContactEmail: The email associated with the certificate order, By default, it uses the Tencent Cloud account email. If it does not exist, a fixed email address will be used.
        :type ContactEmail: str
        :param _ContactPhone: The mobile phone number associated with the certificate. If it does not exist, a fixed mobile phone number will be used.
        :type ContactPhone: str
        :param _ValidityPeriod: Certificate valid period, 3 months by default, currently only 3 months is supported.
        :type ValidityPeriod: str
        :param _CsrEncryptAlgo: Encryption algorithm, values can be ECC or RSA, default is RSA.
        :type CsrEncryptAlgo: str
        :param _CsrKeyParameter: Key pair parameters. RSA supports only 2048. ECC supports only prime256v1. When the encryption algorithm is set to ECC, this parameter is mandatory.
        :type CsrKeyParameter: str
        :param _CsrKeyPassword: Private key password, currently only used when generating jks, pfx format certificates; private key certificates of other formats are not encrypted.
        :type CsrKeyPassword: str
        :param _Alias: Certificate alias.
        :type Alias: str
        :param _OldCertificateId: Old certificate id, used for certificate renewal (the certificate valid period is within 30 days and not expired), a renewal relationship will be established, which can be hosted; not providing it means applying for a new certificate.
        :type OldCertificateId: str
        :param _PackageId: Benefit package ID, used for free certificate expansion package, the free certificate expansion package has been discontinued.
        :type PackageId: str
        :param _DeleteDnsAutoRecord: Whether to delete the automatic domain name verification record after issuance, which is fasle by default. This parameter can be passed in only for domain names of the DNS_AUTO verification type.
        :type DeleteDnsAutoRecord: bool
        :param _DnsNames: Other domains bound to the certificate, to be opened. This parameter is not currently supported.
        :type DnsNames: list of str
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
        self._DnsNames = None

    @property
    def DvAuthMethod(self):
        """Certificate domain validation methods:

DNS_AUTO: Automatically add domain DNS validation. Requires the user's domain to be hosted on 'Cloud DNS' and associated with the same Tencent Cloud account as the certificate application.

DNS: Manually add domain DNS validation. Requires the user to manually add the validation value at their domain's DNS service provider.

FILE: Manually add domain file validation. Requires the user to manually add a specified path file in the root directory of the domain site for file validation. Either HTTP or HTTPS validation will suffice; the domain site must be accessible by overseas CA institutions. The specific access whitelist is: 64.78.193.238, 216.168.247.9, 216.168.249.9, 54.189.196.217.
        :rtype: str
        """
        return self._DvAuthMethod

    @DvAuthMethod.setter
    def DvAuthMethod(self, DvAuthMethod):
        self._DvAuthMethod = DvAuthMethod

    @property
    def DomainName(self):
        """The domain bound to the certificate.
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ProjectId(self):
        """The project ID associated with the certificate. Default is 0 (default project)
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        """Certificate type, optional, currently only type 83 is supported. 83 = trustasia c1 dv free.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ContactEmail(self):
        """The email associated with the certificate order, By default, it uses the Tencent Cloud account email. If it does not exist, a fixed email address will be used.
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPhone(self):
        """The mobile phone number associated with the certificate. If it does not exist, a fixed mobile phone number will be used.
        :rtype: str
        """
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ValidityPeriod(self):
        """Certificate valid period, 3 months by default, currently only 3 months is supported.
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def CsrEncryptAlgo(self):
        """Encryption algorithm, values can be ECC or RSA, default is RSA.
        :rtype: str
        """
        return self._CsrEncryptAlgo

    @CsrEncryptAlgo.setter
    def CsrEncryptAlgo(self, CsrEncryptAlgo):
        self._CsrEncryptAlgo = CsrEncryptAlgo

    @property
    def CsrKeyParameter(self):
        """Key pair parameters. RSA supports only 2048. ECC supports only prime256v1. When the encryption algorithm is set to ECC, this parameter is mandatory.
        :rtype: str
        """
        return self._CsrKeyParameter

    @CsrKeyParameter.setter
    def CsrKeyParameter(self, CsrKeyParameter):
        self._CsrKeyParameter = CsrKeyParameter

    @property
    def CsrKeyPassword(self):
        """Private key password, currently only used when generating jks, pfx format certificates; private key certificates of other formats are not encrypted.
        :rtype: str
        """
        return self._CsrKeyPassword

    @CsrKeyPassword.setter
    def CsrKeyPassword(self, CsrKeyPassword):
        self._CsrKeyPassword = CsrKeyPassword

    @property
    def Alias(self):
        """Certificate alias.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OldCertificateId(self):
        """Old certificate id, used for certificate renewal (the certificate valid period is within 30 days and not expired), a renewal relationship will be established, which can be hosted; not providing it means applying for a new certificate.
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def PackageId(self):
        """Benefit package ID, used for free certificate expansion package, the free certificate expansion package has been discontinued.
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeleteDnsAutoRecord(self):
        """Whether to delete the automatic domain name verification record after issuance, which is fasle by default. This parameter can be passed in only for domain names of the DNS_AUTO verification type.
        :rtype: bool
        """
        return self._DeleteDnsAutoRecord

    @DeleteDnsAutoRecord.setter
    def DeleteDnsAutoRecord(self, DeleteDnsAutoRecord):
        self._DeleteDnsAutoRecord = DeleteDnsAutoRecord

    @property
    def DnsNames(self):
        """Other domains bound to the certificate, to be opened. This parameter is not currently supported.
        :rtype: list of str
        """
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames


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
        self._DnsNames = params.get("DnsNames")
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
        :param _CertificateId: The newly applied certificate id.
        :type CertificateId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """The newly applied certificate id.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        """The IDs of the CSRs to be deleted, 100 IDs at most.
        :rtype: list of int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """The IDs of the CSRs successfully deleted.
        :rtype: list of int
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

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
        """The region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        """The total number of associated cloud resources.
        :rtype: int
        """
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
        """Supported types: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE).
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def BindResourceRegionResult(self):
        """The region of associated cloud resources.
        :rtype: list of BindResourceRegionResult
        """
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
        


class COSInstanceList(AbstractModel):
    """COS instance details - asynchronous association of cloud resource data structure.

    """

    def __init__(self):
        r"""
        :param _Region: Region.
        :type Region: str
        :param _InstanceList: Instance details.
        :type InstanceList: list of CosInstanceDetail
        :param _TotalCount: Total number under the region.
        :type TotalCount: int
        :param _Error: Error message.
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """Instance details.
        :rtype: list of CosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """Total number under the region.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Error message.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
Note: This field may return `null`, indicating that no valid values can be obtained.
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
        """The CSR ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OwnerUin(self):
        """The account.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        """The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        """The organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        """The department.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        """The email address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        """The province.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """The country or region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Remarks(self):
        """The remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def Status(self):
        """The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """The creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EncryptAlgo(self):
        """The encryption algorithm.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        """The algorithm parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """The certificate ID.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Whether the operation succeeded.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        """Certificate ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """ID of the certificate whose order has been successfully cancelled
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        :param _Status: Domain name status: rejected - the domain name failed the review or its registration has expired/been canceled; processing - deploying; online - started; offline - closed.
        :type Status: str
        :param _HttpsBillingSwitch: Domain billing status, where on indicates enable and off indicates disable.
        :type HttpsBillingSwitch: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._HttpsBillingSwitch = None

    @property
    def Domain(self):
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """The ID of the deployed certificate.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """Domain name status: rejected - the domain name failed the review or its registration has expired/been canceled; processing - deploying; online - started; offline - closed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def HttpsBillingSwitch(self):
        """Domain billing status, where on indicates enable and off indicates disable.
        :rtype: str
        """
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
        :param _InstanceList: CDN domain name details.	
        :type InstanceList: list of CdnInstanceDetail
        :param _Error: Whether to query exceptions.
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """The total number of CDN domains in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """CDN domain name details.	
        :rtype: list of CdnInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """Whether to query exceptions.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertBasicInfo(AbstractModel):
    """Basic information of the certificate

    """

    def __init__(self):
        r"""
        :param _Issuer: Issuer.
        :type Issuer: str
        :param _Subject: Issued to.
        :type Subject: str
        :param _Fingerprint: Certificate fingerprint.
        :type Fingerprint: str
        :param _ValidFrom: Certificate valid period start time.
        :type ValidFrom: str
        :param _ValidTo: Certificate valid period end time.
        :type ValidTo: str
        """
        self._Issuer = None
        self._Subject = None
        self._Fingerprint = None
        self._ValidFrom = None
        self._ValidTo = None

    @property
    def Issuer(self):
        """Issuer.
        :rtype: str
        """
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Subject(self):
        """Issued to.
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Fingerprint(self):
        """Certificate fingerprint.
        :rtype: str
        """
        return self._Fingerprint

    @Fingerprint.setter
    def Fingerprint(self, Fingerprint):
        self._Fingerprint = Fingerprint

    @property
    def ValidFrom(self):
        """Certificate valid period start time.
        :rtype: str
        """
        return self._ValidFrom

    @ValidFrom.setter
    def ValidFrom(self, ValidFrom):
        self._ValidFrom = ValidFrom

    @property
    def ValidTo(self):
        """Certificate valid period end time.
        :rtype: str
        """
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo


    def _deserialize(self, params):
        self._Issuer = params.get("Issuer")
        self._Subject = params.get("Subject")
        self._Fingerprint = params.get("Fingerprint")
        self._ValidFrom = params.get("ValidFrom")
        self._ValidTo = params.get("ValidTo")
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
        """The certificate ID.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def TaskId(self):
        """The async task ID.
        :rtype: str
        """
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
        :param _CertCaId: Root certificate id.
        :type CertCaId: str
        :param _SSLMode: Certificate authentication mode: unidirectional one-way authentication, mutual mutual authentication.
        :type SSLMode: str
        """
        self._CertId = None
        self._DnsNames = None
        self._CertCaId = None
        self._SSLMode = None

    @property
    def CertId(self):
        """The certificate ID.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DnsNames(self):
        """The list of domains bound to the certificate.
        :rtype: list of str
        """
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames

    @property
    def CertCaId(self):
        """Root certificate id.
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def SSLMode(self):
        """Certificate authentication mode: unidirectional one-way authentication, mutual mutual authentication.
        :rtype: str
        """
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
        :param _DomainNumber: Quantity of configurable domain names for the certificate.
        :type DomainNumber: str
        :param _OriginCertificateId: Renew the original certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginCertificateId: str
        :param _ReplacedBy: Original ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedBy: str
        :param _ReplacedFor: Reissue certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedFor: str
        :param _RenewOrder: Renewal certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewOrder: str
        :param _SMCert: Whether it is a China SM certificate.
        :type SMCert: int
        :param _CompanyType: Company type, valid values: 1 (individual); 2 (company).
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
        """Quantity of configurable domain names for the certificate.
        :rtype: str
        """
        return self._DomainNumber

    @DomainNumber.setter
    def DomainNumber(self, DomainNumber):
        self._DomainNumber = DomainNumber

    @property
    def OriginCertificateId(self):
        """Renew the original certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginCertificateId

    @OriginCertificateId.setter
    def OriginCertificateId(self, OriginCertificateId):
        self._OriginCertificateId = OriginCertificateId

    @property
    def ReplacedBy(self):
        """Original ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReplacedBy

    @ReplacedBy.setter
    def ReplacedBy(self, ReplacedBy):
        self._ReplacedBy = ReplacedBy

    @property
    def ReplacedFor(self):
        """Reissue certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReplacedFor

    @ReplacedFor.setter
    def ReplacedFor(self, ReplacedFor):
        self._ReplacedFor = ReplacedFor

    @property
    def RenewOrder(self):
        """Renewal certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RenewOrder

    @RenewOrder.setter
    def RenewOrder(self, RenewOrder):
        self._RenewOrder = RenewOrder

    @property
    def SMCert(self):
        """Whether it is a China SM certificate.
        :rtype: int
        """
        return self._SMCert

    @SMCert.setter
    def SMCert(self, SMCert):
        self._SMCert = SMCert

    @property
    def CompanyType(self):
        """Company type, valid values: 1 (individual); 2 (company).
        :rtype: int
        """
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
        :param _OwnerUin: User uin.
        :type OwnerUin: str
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _From: Certificate source:.
trustasia.
upload.
wosign.
sheca.
        :type From: str
        :param _PackageType: Certificate package type:.
Null: user uploads a certificate (without package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise edition (ev pro),. 
4: securesite enhanced (ev). 
5: securesite enterprise professional edition (ov pro).
6: securesite enterprise (ov). 
7: securesite enterprise (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise (ov) cert. 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain name (ev) ssl certificate.
25: wotrus domain name cert.
26: wotrus domain name multiple domain name cert.
27: wotrus domain name wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi - domain name certificate.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi - domain name certificate.
33: wotrus - national cryptography domain - type certificate.
34: wotrus-national cryptography domain certificate (multiple domain names).
35: wotrus-national cryptography domain certificate (wildcard).
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus - enhanced national cryptography certificate.
41: wotrus - enhanced national cryptography certificate (multiple domain names).
42: trustasia - domain name type certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: DNSPod - enhanced (ev) ssl certificate.
47: DNSPod - enhanced (ev) multiple domain names ssl certificate.
48: DNSPod - domain name-based (dv) ssl certificate.
49: DNSPod - domain name-based (dv) wildcard ssl certificate.
50: DNSPod - domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional edition multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional edition multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise wildcard (ov).
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise pro multiple domain names (ov pro).
93: securesite enterprise multiple domain names (ov).
94: securesite enhanced pro multiple domain names (ev pro).
95: securesite enhanced multiple domain names (ev).
96: securesite ev pro.
97: securesite enterprise professional edition (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise ov ssl certificate for multiple domain names.
100: cfca ov wildcard ssl certificate.
101: cfca enhanced (ev) ssl certificate.
        :type PackageType: str
        :param _CertificateType: Certificate type. ca = client certificate; svr = server certificate.
        :type CertificateType: str
        :param _ProductZhName: Certificate product name.
        :type ProductZhName: str
        :param _Domain: Primary domain name.
        :type Domain: str
        :param _Alias: Remark name.
        :type Alias: str
        :param _Status: Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = dns record added automatically, 5 = enterprise certificate, pending documentation submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending documentation submission, 14 = certificate refunded, 15 = certificate migration in progress.
        :type Status: int
        :param _CertificateExtra: Certificate extended information.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _VulnerabilityStatus: Vulnerability scanning status: INACTIVE = not enabled, ACTIVE = enabled.
        :type VulnerabilityStatus: str
        :param _StatusMsg: Status information.
        :type StatusMsg: str
        :param _VerifyType: Validation type: DNS_AUTO = automatic dns validation, DNS = manual dns validation, FILE = file verification, DNS_PROXY = dns proxy validation, FILE_PROXY = file proxy verification.
        :type VerifyType: str
        :param _CertBeginTime: Certificate validation time.
        :type CertBeginTime: str
        :param _CertEndTime: Certificate expiration time.
        :type CertEndTime: str
        :param _ValidityPeriod: Certificate validity period (month).
        :type ValidityPeriod: str
        :param _InsertTime: Creation time.
        :type InsertTime: str
        :param _CertificateId: Certificate id.
        :type CertificateId: str
        :param _SubjectAltName: Multiple domain names contained in the certificate (including the primary domain name).
        :type SubjectAltName: list of str
        :param _PackageTypeName: Certificate type name.
        :type PackageTypeName: str
        :param _StatusName: Status name.
        :type StatusName: str
        :param _IsVip: Specifies whether the customer is a vip customer. true indicates yes and false indicates no.
        :type IsVip: bool
        :param _IsDv: Specifies whether it is a dv version certificate. true indicates yes and false indicates no.
        :type IsDv: bool
        :param _IsWildcard: Specifies whether it is a wildcard domain name certificate. true indicates yes and false indicates no.
        :type IsWildcard: bool
        :param _IsVulnerability: Whether the vulnerability scanning feature is enabled.
        :type IsVulnerability: bool
        :param _RenewAble: Whether it is renewable.
        :type RenewAble: bool
        :param _ProjectInfo: Project information.
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param _BoundResource: Associated cloud resources are temporarily unavailable.
        :type BoundResource: list of str
        :param _Deployable: Whether it can be deployed.
        :type Deployable: bool
        :param _Tags: Tag list.
        :type Tags: list of Tags
        :param _IsIgnore: Whether expiration notice has been ignored.
        :type IsIgnore: bool
        :param _IsSM: Whether it is a China SM certificate.
        :type IsSM: bool
        :param _EncryptAlgorithm: Certificate algorithm.
        :type EncryptAlgorithm: str
        :param _CAEncryptAlgorithms: Encryption algorithm for upload ca certificate.
        :type CAEncryptAlgorithms: list of str
        :param _CAEndTimes: Expiration time for upload ca certificate.
        :type CAEndTimes: list of str
        :param _CACommonNames: Common name of the upload ca certificate.
        :type CACommonNames: list of str
        :param _PreAuditInfo: Certificate prereview information.
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param _AutoRenewFlag: Whether to auto-renew.
        :type AutoRenewFlag: int
        :param _HostingStatus: Hosting status: 0, hosting; 5, resource replacement; 10, hosting completed; -1, not hosted. 
        :type HostingStatus: int
        :param _HostingCompleteTime: Hosting completion time.
        :type HostingCompleteTime: str
        :param _HostingRenewCertId: Manage the new certificate id.
        :type HostingRenewCertId: str
        :param _HasRenewOrder: Existing renewal certificate id.
        :type HasRenewOrder: str
        :param _ReplaceOriCertIsDelete: Indicates whether the original certificate is deleted during reissue.
        :type ReplaceOriCertIsDelete: bool
        :param _IsExpiring: Indicates whether it is about to expire. a certificate is about to expire if it will expire within 30 days.
        :type IsExpiring: bool
        :param _DVAuthDeadline: Add validation expiration date for DV certificate
        :type DVAuthDeadline: str
        :param _ValidationPassedTime: Domain verification passed time.
        :type ValidationPassedTime: str
        :param _CertSANs: Multiple domain names associated with the certificate.
        :type CertSANs: list of str
        :param _AwaitingValidationMsg: Domain verification rejection information.
        :type AwaitingValidationMsg: str
        :param _AllowDownload: Whether to allow downloading.
        :type AllowDownload: bool
        :param _IsDNSPODResolve: Whether all certificate domain names are managed and resolved by dnspod.
        :type IsDNSPODResolve: bool
        :param _IsPackage: Whether the certificate is purchased with benefit points.
        :type IsPackage: bool
        :param _KeyPasswordCustomFlag: Whether there is a private key password.
        :type KeyPasswordCustomFlag: bool
        :param _SupportDownloadType: Types of web servers supported for download: nginx, apache, iis, tomcat, jks, root, other.
        :type SupportDownloadType: :class:`tencentcloud.ssl.v20191205.models.SupportDownloadType`
        :param _CertRevokedTime: Certificate revocation completion time.
        :type CertRevokedTime: str
        :param _HostingResourceTypes: Hosted resource type list.
        :type HostingResourceTypes: list of str
        :param _HostingConfig: Managed configuration information.
        :type HostingConfig: :class:`tencentcloud.ssl.v20191205.models.HostingConfig`
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
        self._CertRevokedTime = None
        self._HostingResourceTypes = None
        self._HostingConfig = None

    @property
    def OwnerUin(self):
        """User uin.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """Certificate source:.
trustasia.
upload.
wosign.
sheca.
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def PackageType(self):
        """Certificate package type:.
Null: user uploads a certificate (without package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise edition (ev pro),. 
4: securesite enhanced (ev). 
5: securesite enterprise professional edition (ov pro).
6: securesite enterprise (ov). 
7: securesite enterprise (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise (ov) cert. 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain name (ev) ssl certificate.
25: wotrus domain name cert.
26: wotrus domain name multiple domain name cert.
27: wotrus domain name wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi - domain name certificate.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi - domain name certificate.
33: wotrus - national cryptography domain - type certificate.
34: wotrus-national cryptography domain certificate (multiple domain names).
35: wotrus-national cryptography domain certificate (wildcard).
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus - enhanced national cryptography certificate.
41: wotrus - enhanced national cryptography certificate (multiple domain names).
42: trustasia - domain name type certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: DNSPod - enhanced (ev) ssl certificate.
47: DNSPod - enhanced (ev) multiple domain names ssl certificate.
48: DNSPod - domain name-based (dv) ssl certificate.
49: DNSPod - domain name-based (dv) wildcard ssl certificate.
50: DNSPod - domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional edition multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional edition multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise wildcard (ov).
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise pro multiple domain names (ov pro).
93: securesite enterprise multiple domain names (ov).
94: securesite enhanced pro multiple domain names (ev pro).
95: securesite enhanced multiple domain names (ev).
96: securesite ev pro.
97: securesite enterprise professional edition (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise ov ssl certificate for multiple domain names.
100: cfca ov wildcard ssl certificate.
101: cfca enhanced (ev) ssl certificate.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def CertificateType(self):
        """Certificate type. ca = client certificate; svr = server certificate.
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProductZhName(self):
        """Certificate product name.
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """Primary domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """Remark name.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = dns record added automatically, 5 = enterprise certificate, pending documentation submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending documentation submission, 14 = certificate refunded, 15 = certificate migration in progress.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateExtra(self):
        """Certificate extended information.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def VulnerabilityStatus(self):
        """Vulnerability scanning status: INACTIVE = not enabled, ACTIVE = enabled.
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def StatusMsg(self):
        """Status information.
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """Validation type: DNS_AUTO = automatic dns validation, DNS = manual dns validation, FILE = file verification, DNS_PROXY = dns proxy validation, FILE_PROXY = file proxy verification.
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CertBeginTime(self):
        """Certificate validation time.
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """Certificate expiration time.
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """Certificate validity period (month).
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """Creation time.
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def CertificateId(self):
        """Certificate id.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def SubjectAltName(self):
        """Multiple domain names contained in the certificate (including the primary domain name).
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def PackageTypeName(self):
        """Certificate type name.
        :rtype: str
        """
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        """Status name.
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def IsVip(self):
        """Specifies whether the customer is a vip customer. true indicates yes and false indicates no.
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsDv(self):
        """Specifies whether it is a dv version certificate. true indicates yes and false indicates no.
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsWildcard(self):
        """Specifies whether it is a wildcard domain name certificate. true indicates yes and false indicates no.
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsVulnerability(self):
        """Whether the vulnerability scanning feature is enabled.
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        """Whether it is renewable.
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def ProjectInfo(self):
        """Project information.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        """
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def BoundResource(self):
        """Associated cloud resources are temporarily unavailable.
        :rtype: list of str
        """
        return self._BoundResource

    @BoundResource.setter
    def BoundResource(self, BoundResource):
        self._BoundResource = BoundResource

    @property
    def Deployable(self):
        """Whether it can be deployed.
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """Tag list.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsIgnore(self):
        """Whether expiration notice has been ignored.
        :rtype: bool
        """
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def IsSM(self):
        """Whether it is a China SM certificate.
        :rtype: bool
        """
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def EncryptAlgorithm(self):
        """Certificate algorithm.
        :rtype: str
        """
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def CAEncryptAlgorithms(self):
        """Encryption algorithm for upload ca certificate.
        :rtype: list of str
        """
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CAEndTimes(self):
        """Expiration time for upload ca certificate.
        :rtype: list of str
        """
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def CACommonNames(self):
        """Common name of the upload ca certificate.
        :rtype: list of str
        """
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def PreAuditInfo(self):
        """Certificate prereview information.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        """
        return self._PreAuditInfo

    @PreAuditInfo.setter
    def PreAuditInfo(self, PreAuditInfo):
        self._PreAuditInfo = PreAuditInfo

    @property
    def AutoRenewFlag(self):
        """Whether to auto-renew.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def HostingStatus(self):
        """Hosting status: 0, hosting; 5, resource replacement; 10, hosting completed; -1, not hosted. 
        :rtype: int
        """
        return self._HostingStatus

    @HostingStatus.setter
    def HostingStatus(self, HostingStatus):
        self._HostingStatus = HostingStatus

    @property
    def HostingCompleteTime(self):
        """Hosting completion time.
        :rtype: str
        """
        return self._HostingCompleteTime

    @HostingCompleteTime.setter
    def HostingCompleteTime(self, HostingCompleteTime):
        self._HostingCompleteTime = HostingCompleteTime

    @property
    def HostingRenewCertId(self):
        """Manage the new certificate id.
        :rtype: str
        """
        return self._HostingRenewCertId

    @HostingRenewCertId.setter
    def HostingRenewCertId(self, HostingRenewCertId):
        self._HostingRenewCertId = HostingRenewCertId

    @property
    def HasRenewOrder(self):
        """Existing renewal certificate id.
        :rtype: str
        """
        return self._HasRenewOrder

    @HasRenewOrder.setter
    def HasRenewOrder(self, HasRenewOrder):
        self._HasRenewOrder = HasRenewOrder

    @property
    def ReplaceOriCertIsDelete(self):
        """Indicates whether the original certificate is deleted during reissue.
        :rtype: bool
        """
        return self._ReplaceOriCertIsDelete

    @ReplaceOriCertIsDelete.setter
    def ReplaceOriCertIsDelete(self, ReplaceOriCertIsDelete):
        self._ReplaceOriCertIsDelete = ReplaceOriCertIsDelete

    @property
    def IsExpiring(self):
        """Indicates whether it is about to expire. a certificate is about to expire if it will expire within 30 days.
        :rtype: bool
        """
        return self._IsExpiring

    @IsExpiring.setter
    def IsExpiring(self, IsExpiring):
        self._IsExpiring = IsExpiring

    @property
    def DVAuthDeadline(self):
        """Add validation expiration date for DV certificate
        :rtype: str
        """
        return self._DVAuthDeadline

    @DVAuthDeadline.setter
    def DVAuthDeadline(self, DVAuthDeadline):
        self._DVAuthDeadline = DVAuthDeadline

    @property
    def ValidationPassedTime(self):
        """Domain verification passed time.
        :rtype: str
        """
        return self._ValidationPassedTime

    @ValidationPassedTime.setter
    def ValidationPassedTime(self, ValidationPassedTime):
        self._ValidationPassedTime = ValidationPassedTime

    @property
    def CertSANs(self):
        """Multiple domain names associated with the certificate.
        :rtype: list of str
        """
        return self._CertSANs

    @CertSANs.setter
    def CertSANs(self, CertSANs):
        self._CertSANs = CertSANs

    @property
    def AwaitingValidationMsg(self):
        """Domain verification rejection information.
        :rtype: str
        """
        return self._AwaitingValidationMsg

    @AwaitingValidationMsg.setter
    def AwaitingValidationMsg(self, AwaitingValidationMsg):
        self._AwaitingValidationMsg = AwaitingValidationMsg

    @property
    def AllowDownload(self):
        """Whether to allow downloading.
        :rtype: bool
        """
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def IsDNSPODResolve(self):
        """Whether all certificate domain names are managed and resolved by dnspod.
        :rtype: bool
        """
        return self._IsDNSPODResolve

    @IsDNSPODResolve.setter
    def IsDNSPODResolve(self, IsDNSPODResolve):
        self._IsDNSPODResolve = IsDNSPODResolve

    @property
    def IsPackage(self):
        """Whether the certificate is purchased with benefit points.
        :rtype: bool
        """
        return self._IsPackage

    @IsPackage.setter
    def IsPackage(self, IsPackage):
        self._IsPackage = IsPackage

    @property
    def KeyPasswordCustomFlag(self):
        """Whether there is a private key password.
        :rtype: bool
        """
        return self._KeyPasswordCustomFlag

    @KeyPasswordCustomFlag.setter
    def KeyPasswordCustomFlag(self, KeyPasswordCustomFlag):
        self._KeyPasswordCustomFlag = KeyPasswordCustomFlag

    @property
    def SupportDownloadType(self):
        """Types of web servers supported for download: nginx, apache, iis, tomcat, jks, root, other.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SupportDownloadType`
        """
        return self._SupportDownloadType

    @SupportDownloadType.setter
    def SupportDownloadType(self, SupportDownloadType):
        self._SupportDownloadType = SupportDownloadType

    @property
    def CertRevokedTime(self):
        """Certificate revocation completion time.
        :rtype: str
        """
        return self._CertRevokedTime

    @CertRevokedTime.setter
    def CertRevokedTime(self, CertRevokedTime):
        self._CertRevokedTime = CertRevokedTime

    @property
    def HostingResourceTypes(self):
        """Hosted resource type list.
        :rtype: list of str
        """
        return self._HostingResourceTypes

    @HostingResourceTypes.setter
    def HostingResourceTypes(self, HostingResourceTypes):
        self._HostingResourceTypes = HostingResourceTypes

    @property
    def HostingConfig(self):
        """Managed configuration information.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.HostingConfig`
        """
        return self._HostingConfig

    @HostingConfig.setter
    def HostingConfig(self, HostingConfig):
        self._HostingConfig = HostingConfig


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
        self._CertRevokedTime = params.get("CertRevokedTime")
        self._HostingResourceTypes = params.get("HostingResourceTypes")
        if params.get("HostingConfig") is not None:
            self._HostingConfig = HostingConfig()
            self._HostingConfig._deserialize(params.get("HostingConfig"))
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
        :param _Listeners: CLB listener list.
        :type Listeners: list of ClbListener
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        """The CLB instance ID.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """The CLB instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        """CLB listener list.
        :rtype: list of ClbListener
        """
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
        :param _InstanceList: CLB instance details.
        :type InstanceList: list of ClbInstanceDetail
        :param _TotalCount: The total number of CLB instances in this region.
        :type TotalCount: int
        :param _Error: Whether to query exceptions.
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """The region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """CLB instance details.
        :rtype: list of ClbInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of CLB instances in this region.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
        :param _Certificate: Data of certificate bound to the listener.
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _Rules: List of listener rules.
        :type Rules: list of ClbListenerRule
        :param _NoMatchDomains: Domain list not matched.
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
        """The listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """The listener name.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        """Whether to enable SNI. Valid values: `1` (enable) and `0` (disable).
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Protocol(self):
        """The listener protocol type. Valid values: `HTTPS` and `TCP_SSL`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Certificate(self):
        """Data of certificate bound to the listener.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Rules(self):
        """List of listener rules.
        :rtype: list of ClbListenerRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def NoMatchDomains(self):
        """Domain list not matched.
        :rtype: list of str
        """
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
        :param _Certificate: Certificate data bound to the rule.
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _NoMatchDomains: Domain list not matched.
        :type NoMatchDomains: list of str
        :param _Url: Rule binding path.
        :type Url: str
        """
        self._LocationId = None
        self._Domain = None
        self._IsMatch = None
        self._Certificate = None
        self._NoMatchDomains = None
        self._Url = None

    @property
    def LocationId(self):
        """The rule ID.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        """The domains bound.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IsMatch(self):
        """Whether the rule matches the domains to be associated with a certificate.
        :rtype: bool
        """
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def Certificate(self):
        """Certificate data bound to the rule.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def NoMatchDomains(self):
        """Domain list not matched.
        :rtype: list of str
        """
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains

    @property
    def Url(self):
        """Rule binding path.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._IsMatch = params.get("IsMatch")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        self._NoMatchDomains = params.get("NoMatchDomains")
        self._Url = params.get("Url")
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
        :param _CertificateId: Paid certificate id of materials to be submitted.	
        :type CertificateId: str
        :param _VerifyType: Certificate domain name verification method:.
DNS_AUTO: automatically adds domain dns verification, requiring user domain name resolution to be hosted on [cloud dns](https://console.cloud.tencent.com/cns) and under the same tencent cloud account as the certificate application.
DNS: manually add domain dns verification, which requires users to manually add verification values to the domain resolution service provider.
FILE: manual addition of domain name file verification. requires the user to manually add a specified path file in the root directory of the domain site for file verification, and either http or https passing is acceptable; the domain site needs to be accessible by overseas ca institutions, with the specific access allowlist being: 64.78.193.238, 216.168.247.9, 216.168.249.9, 54.189.196.217.
        :type VerifyType: str
        """
        self._CertificateId = None
        self._VerifyType = None

    @property
    def CertificateId(self):
        """Paid certificate id of materials to be submitted.	
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def VerifyType(self):
        """Certificate domain name verification method:.
DNS_AUTO: automatically adds domain dns verification, requiring user domain name resolution to be hosted on [cloud dns](https://console.cloud.tencent.com/cns) and under the same tencent cloud account as the certificate application.
DNS: manually add domain dns verification, which requires users to manually add verification values to the domain resolution service provider.
FILE: manual addition of domain name file verification. requires the user to manually add a specified path file in the root directory of the domain site for file verification, and either http or https passing is acceptable; the domain site needs to be accessible by overseas ca institutions, with the specific access allowlist being: 64.78.193.238, 216.168.247.9, 216.168.249.9, 54.189.196.217.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OrderId = None
        self._Status = None
        self._RequestId = None

    @property
    def OrderId(self):
        """TrustAsia order ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        """Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CosInstanceDetail(AbstractModel):
    """COS instance description.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name.
        :type Domain: str
        :param _CertId: Bound certificate id.
        :type CertId: str
        :param _Status: ENABLED: domain name online status.
DISABLED: domain name offline status.
        :type Status: str
        :param _Bucket: bucket name.
        :type Bucket: str
        :param _Region: bucket region.
        :type Region: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._Bucket = None
        self._Region = None

    @property
    def Domain(self):
        """Domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """Bound certificate id.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """ENABLED: domain name online status.
DISABLED: domain name offline status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bucket(self):
        """bucket name.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """bucket region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _Tags: 
        :type Tags: list of Tags
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
        self._Tags = None

    @property
    def Domain(self):
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        """The organization name.
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        """The department.
        :rtype: str
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        """The email address.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        """The province.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """The country or region code that complies with ISO 3166, such as CN and US.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        """The encryption algorithm. RSA and ECC are supported.	
        :rtype: str
        """
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        """The key pair parameter. For RSA, only the 2048-bit and 4096-bit key pairs are supported. For ECC, only prime256v1 is supported.
        :rtype: str
        """
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Generate(self):
        """Whether to generate the CSR content. Once the CSR content is generated, the CSR record cannot be modified.
        :rtype: bool
        """
        return self._Generate

    @Generate.setter
    def Generate(self, Generate):
        self._Generate = Generate

    @property
    def KeyPassword(self):
        """The password of the private key.
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def Remark(self):
        """The remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Tags(self):
        """
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """The CSR ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        """The list of certificate IDs, 100 IDs at most.
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def IsCache(self):
        """Whether to use the cached results. Valid values: `1` (default) for yes and `0` for no. If any task completed within last 30 minutes exists under the current certificate ID, and the cache is used, the query result of the last task completed within 30 minutes will be read.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertTaskIds = None
        self._RequestId = None

    @property
    def CertTaskIds(self):
        """The IDs of async tasks for querying cloud resources associated with a certificate.
        :rtype: list of CertTaskId
        """
        return self._CertTaskIds

    @CertTaskIds.setter
    def CertTaskIds(self, CertTaskIds):
        self._CertTaskIds = CertTaskIds

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
        :param _ProductId: Certificate product id. `3`: securesite ev pro; `4`: securesite ev; `5`: securesite ov pro; `6`: securesite ov; `7`: securesite ov wildcard; `8`: geotrust ev; `9`: geotrust ov; `10`: geotrust ov wildcard; `11`: trustasia dv multi-domain; `12`: trustasia dv wildcard; `13`: trustasia ov wildcard d3; `14`: trustasia ov d3; `15`: trustasia ov multi-domain d3; `16`: trustasia ev d3; `17`: trustasia ev multi-domain d3; `18`: globalsign ov; `19`: globalsign ov wildcard; `20`: globalsign ev; `21`: trustasia ov wildcard multi-domain d3; `22`: globalsign ov multi-domain; `23`: globalsign ov wildcard multi-domain; `24`: globalsign ev multi-domain; `25`: wotrus dv; `26`: wotrus dv multi-domain; `27`: wotrus dv wildcard; `28`: wotrus ov; `29`: wotrus ov multi-domain; `30`: wotrus ov wildcard; `31`: wotrus ev; `32`: wotrus ev multi-domain; `33`: DNSPod sm2 dv; `34`: DNSPod sm2 dv multi-domain; `35`: DNSPod sm2 dv wildcard; `37`: DNSPod sm2 ov; `38`: DNSPod sm2 ov multi-domain; `39`: DNSPod sm2 ov wildcard; `40`: DNSPod sm2 ev; `41`: DNSPod sm2 ev multi-domain; `42`: trustasia dv wildcard multi-domain; `43`: dnspod-ov ssl certificate; `44`: dnspod-ov wildcard ssl certificate; `45`: dnspod-ov multi-domain ssl certificate; `46`: dnspod-ev ssl certificate; `47`: dnspod-ev multi-domain ssl certificate; `48`: dnspod-dv ssl certificate; `49`: dnspod-dv wildcard ssl certificate; `50`: dnspod-dv multi-domain ssl certificate; `51`: DNSPod (sm2)-ov ssl certificate; `52`: DNSPod (sm2)-ov wildcard ssl certificate; `53`: DNSPod (sm2)-ov multi-domain ssl certificate; `54`: DNSPod (sm2)-dv ssl certificate; `55`: DNSPod (sm2)-dv wildcard ssl certificate; `56`: DNSPod (sm2)-dv multi-domain ssl certificate; `57`: securesite ov pro multi-domain; `58`: securesite ov multi-domain; `59`: securesite ev pro multi-domain; `60`: securesite ev multi-domain; `61`: geotrust ev multi-domain.
        :type ProductId: int
        :param _DomainNum: Number of domains associated with the certificate
        :type DomainNum: int
        :param _TimeSpan: Certificate validity period.
        :type TimeSpan: int
        :param _AutoVoucher: Whether to automatically use vouchers: 1 for yes, 0 for no; the default is 1.
        :type AutoVoucher: int
        :param _Tags: Tag, generate tags for certificates.
        :type Tags: list of Tags
        """
        self._ProductId = None
        self._DomainNum = None
        self._TimeSpan = None
        self._AutoVoucher = None
        self._Tags = None

    @property
    def ProductId(self):
        """Certificate product id. `3`: securesite ev pro; `4`: securesite ev; `5`: securesite ov pro; `6`: securesite ov; `7`: securesite ov wildcard; `8`: geotrust ev; `9`: geotrust ov; `10`: geotrust ov wildcard; `11`: trustasia dv multi-domain; `12`: trustasia dv wildcard; `13`: trustasia ov wildcard d3; `14`: trustasia ov d3; `15`: trustasia ov multi-domain d3; `16`: trustasia ev d3; `17`: trustasia ev multi-domain d3; `18`: globalsign ov; `19`: globalsign ov wildcard; `20`: globalsign ev; `21`: trustasia ov wildcard multi-domain d3; `22`: globalsign ov multi-domain; `23`: globalsign ov wildcard multi-domain; `24`: globalsign ev multi-domain; `25`: wotrus dv; `26`: wotrus dv multi-domain; `27`: wotrus dv wildcard; `28`: wotrus ov; `29`: wotrus ov multi-domain; `30`: wotrus ov wildcard; `31`: wotrus ev; `32`: wotrus ev multi-domain; `33`: DNSPod sm2 dv; `34`: DNSPod sm2 dv multi-domain; `35`: DNSPod sm2 dv wildcard; `37`: DNSPod sm2 ov; `38`: DNSPod sm2 ov multi-domain; `39`: DNSPod sm2 ov wildcard; `40`: DNSPod sm2 ev; `41`: DNSPod sm2 ev multi-domain; `42`: trustasia dv wildcard multi-domain; `43`: dnspod-ov ssl certificate; `44`: dnspod-ov wildcard ssl certificate; `45`: dnspod-ov multi-domain ssl certificate; `46`: dnspod-ev ssl certificate; `47`: dnspod-ev multi-domain ssl certificate; `48`: dnspod-dv ssl certificate; `49`: dnspod-dv wildcard ssl certificate; `50`: dnspod-dv multi-domain ssl certificate; `51`: DNSPod (sm2)-ov ssl certificate; `52`: DNSPod (sm2)-ov wildcard ssl certificate; `53`: DNSPod (sm2)-ov multi-domain ssl certificate; `54`: DNSPod (sm2)-dv ssl certificate; `55`: DNSPod (sm2)-dv wildcard ssl certificate; `56`: DNSPod (sm2)-dv multi-domain ssl certificate; `57`: securesite ov pro multi-domain; `58`: securesite ov multi-domain; `59`: securesite ev pro multi-domain; `60`: securesite ev multi-domain; `61`: geotrust ev multi-domain.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DomainNum(self):
        """Number of domains associated with the certificate
        :rtype: int
        """
        return self._DomainNum

    @DomainNum.setter
    def DomainNum(self, DomainNum):
        self._DomainNum = DomainNum

    @property
    def TimeSpan(self):
        """Certificate validity period.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def AutoVoucher(self):
        """Whether to automatically use vouchers: 1 for yes, 0 for no; the default is 1.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Tags(self):
        """Tag, generate tags for certificates.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DomainNum = params.get("DomainNum")
        self._TimeSpan = params.get("TimeSpan")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateIds = None
        self._DealIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        """List of certificate IDs
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def DealIds(self):
        """List of order IDs
        :rtype: list of str
        """
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

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
        :param _CertId: Certificate id.
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
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        """The instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Protocol(self):
        """The protocol type.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CertId(self):
        """Certificate id.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def VirtualPort(self):
        """The forwarding port.
        :rtype: str
        """
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
        :param _InstanceList: DDOS instance details.	
        :type InstanceList: list of DdosInstanceDetail
        :param _Error: Whether to query exceptions.
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """The total number of DDOS instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """DDOS instance details.	
        :rtype: list of DdosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """Whether to query exceptions.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
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
        :param _IsCheckResource: When deleting, check whether the certificate is associated with cloud resources. By default, no check is performed. if you choose to check (the authorization service role SSL_QCSLinkedRoleInReplaceLoadCertificate is required), the deletion will become asynchronous, and the API will return an asynchronous task id. you need to use the DescribeDeleteCertificatesTaskResult API to check whether the deletion is successful.
        :type IsCheckResource: bool
        """
        self._CertificateId = None
        self._IsCheckResource = None

    @property
    def CertificateId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCheckResource(self):
        """When deleting, check whether the certificate is associated with cloud resources. By default, no check is performed. if you choose to check (the authorization service role SSL_QCSLinkedRoleInReplaceLoadCertificate is required), the deletion will become asynchronous, and the API will return an asynchronous task id. you need to use the DescribeDeleteCertificatesTaskResult API to check whether the deletion is successful.
        :rtype: bool
        """
        return self._IsCheckResource

    @IsCheckResource.setter
    def IsCheckResource(self, IsCheckResource):
        self._IsCheckResource = IsCheckResource


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCheckResource = params.get("IsCheckResource")
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
        :param _TaskId: Asynchronous deletion task id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeleteResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        """Deletion result
        :rtype: bool
        """
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def TaskId(self):
        """Asynchronous deletion task id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._DeleteResult = params.get("DeleteResult")
        self._TaskId = params.get("TaskId")
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
        """The CSR ID.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """The CSR ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OwnerUin(self):
        """The account.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        """The organization name.
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        """The department.
        :rtype: str
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        """The email address.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        """The province.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """The country or region.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        """The key algorithm.
        :rtype: str
        """
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        """The algorithm parameter.
        :rtype: str
        """
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Remarks(self):
        """The remarks.
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def Status(self):
        """The status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def KeyPassword(self):
        """The password of the private key.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def CreateTime(self):
        """The creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CSR(self):
        """The CSR content.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CSR

    @CSR.setter
    def CSR(self, CSR):
        self._CSR = CSR

    @property
    def PrivateKey(self):
        """The content of the private key.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

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
        :param _Domain: The domain for CSR filtering
        :type Domain: str
        :param _EncryptAlgo: The encryption algorithm for CSR filtering
        :type EncryptAlgo: str
        """
        self._Limit = None
        self._Offset = None
        self._Domain = None
        self._EncryptAlgo = None

    @property
    def Limit(self):
        """The number of CSRs on each page. The default value is 10, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """The pagination offset, starting from 0.	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Domain(self):
        """The domain for CSR filtering
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def EncryptAlgo(self):
        """The encryption algorithm for CSR filtering
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Set = None
        self._RequestId = None

    @property
    def Total(self):
        """The total number of CSRs.	
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Set(self):
        """The list of CSRs.
        :rtype: list of CSRItem
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

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
        :param _TaskId: Task id, which can be used to query the result of binding cloud resources according to the task id obtained from createcertificatebindresourcesynctask.
        :type TaskId: str
        :param _Limit: The number of cloud resources displayed on each page. The default value is 10, and the maximum value is 100.
        :type Limit: str
        :param _Offset: Current offset, default is 0.
        :type Offset: str
        :param _ResourceTypes: Result detail of queried resource type. if not provided, all will be queried. valid values include:.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :type ResourceTypes: list of str
        :param _Regions: Data of querying region list. clb, tke, waf, api gateway, tcb, cos, and tse support region query, while other resource types do not support.
        :type Regions: list of str
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._ResourceTypes = None
        self._Regions = None

    @property
    def TaskId(self):
        """Task id, which can be used to query the result of binding cloud resources according to the task id obtained from createcertificatebindresourcesynctask.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """The number of cloud resources displayed on each page. The default value is 10, and the maximum value is 100.
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Current offset, default is 0.
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ResourceTypes(self):
        """Result detail of queried resource type. if not provided, all will be queried. valid values include:.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        """Data of querying region list. clb, tke, waf, api gateway, tcb, cos, and tse support region query, while other resource types do not support.
        :rtype: list of str
        """
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
        :param _Status: The status of the async task. Valid values: `0` for querying, `1` for successful, and `2` for abnormal. If the status is `1`, check the result of `BindResourceResult` ; if the status is `2`, check the `error` .
        :type Status: int
        :param _CacheTime: The cache time of the current result.
        :type CacheTime: str
        :param _TSE: Associated TSE resource details
Note: This field may return null, indicating that no valid value can be obtained.
        :type TSE: list of TSEInstanceList
        :param _COS: Information of associated cos resource.
Note: this field may return null, indicating that no valid values can be obtained.
        :type COS: list of COSInstanceList
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        self._COS = None
        self._RequestId = None

    @property
    def CLB(self):
        """The details of associated CLB resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ClbInstanceList
        """
        return self._CLB

    @CLB.setter
    def CLB(self, CLB):
        self._CLB = CLB

    @property
    def CDN(self):
        """The details of associated CDN resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CdnInstanceList
        """
        return self._CDN

    @CDN.setter
    def CDN(self, CDN):
        self._CDN = CDN

    @property
    def WAF(self):
        """The details of associated WAF resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of WafInstanceList
        """
        return self._WAF

    @WAF.setter
    def WAF(self, WAF):
        self._WAF = WAF

    @property
    def DDOS(self):
        """The details of associated Anti-DDS resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DdosInstanceList
        """
        return self._DDOS

    @DDOS.setter
    def DDOS(self, DDOS):
        self._DDOS = DDOS

    @property
    def LIVE(self):
        """The details of associated LIVE resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LiveInstanceList
        """
        return self._LIVE

    @LIVE.setter
    def LIVE(self, LIVE):
        self._LIVE = LIVE

    @property
    def VOD(self):
        """The details of associated VOD resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of VODInstanceList
        """
        return self._VOD

    @VOD.setter
    def VOD(self, VOD):
        self._VOD = VOD

    @property
    def TKE(self):
        """The details of associated TKE resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TkeInstanceList
        """
        return self._TKE

    @TKE.setter
    def TKE(self, TKE):
        self._TKE = TKE

    @property
    def APIGATEWAY(self):
        """The details of associated APIGATEWAY resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApiGatewayInstanceList
        """
        return self._APIGATEWAY

    @APIGATEWAY.setter
    def APIGATEWAY(self, APIGATEWAY):
        self._APIGATEWAY = APIGATEWAY

    @property
    def TCB(self):
        """The details of associated TCB resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TCBInstanceList
        """
        return self._TCB

    @TCB.setter
    def TCB(self, TCB):
        self._TCB = TCB

    @property
    def TEO(self):
        """The details of associated TEO resources.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TeoInstanceList
        """
        return self._TEO

    @TEO.setter
    def TEO(self, TEO):
        self._TEO = TEO

    @property
    def Status(self):
        """The status of the async task. Valid values: `0` for querying, `1` for successful, and `2` for abnormal. If the status is `1`, check the result of `BindResourceResult` ; if the status is `2`, check the `error` .
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CacheTime(self):
        """The cache time of the current result.
        :rtype: str
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def TSE(self):
        """Associated TSE resource details
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of TSEInstanceList
        """
        return self._TSE

    @TSE.setter
    def TSE(self, TSE):
        self._TSE = TSE

    @property
    def COS(self):
        """Information of associated cos resource.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of COSInstanceList
        """
        return self._COS

    @COS.setter
    def COS(self, COS):
        self._COS = COS

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
        if params.get("COS") is not None:
            self._COS = []
            for item in params.get("COS"):
                obj = COSInstanceList()
                obj._deserialize(item)
                self._COS.append(obj)
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
        """The task IDs, which are used to query the results of associated cloud resources, 100 IDs at most.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SyncTaskBindResourceResult = None
        self._RequestId = None

    @property
    def SyncTaskBindResourceResult(self):
        """The results of the async tasks for querying associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SyncTaskBindResourceResult
        """
        return self._SyncTaskBindResourceResult

    @SyncTaskBindResourceResult.setter
    def SyncTaskBindResourceResult(self, SyncTaskBindResourceResult):
        self._SyncTaskBindResourceResult = SyncTaskBindResourceResult

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
        """Certificate ID
        :rtype: str
        """
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
        :param _OwnerUin: Certificate belonging to user main account uin.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _From: Certificate source:.
trustAsia.
upload.
wosign.
sheca.
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param _PackageType: Certificate package type:.
null: user uploads a certificate (no package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise version (ev pro),. 
4: securesite enhanced (ev),. 
5: securesite enterprise pro (ov pro).
6: securesite enterprise (ov). 
7: securesite enterprise (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise (ov). 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain names (ev) ssl certificate.
25: wotrus domain cert.
26: wotrus multi-domain cert.
27: wotrus wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi-domain cert.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi-domain name certificate.
33: wotrus-national cryptography domain name certificate.
34: wotrus-national cryptography domain name certificate (multiple domain names).
35: wotrus-national cryptography wildcard certificate.
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus-national cryptography enhanced certificate.
41: wotrus - national cryptography enhanced certificate (multiple domain names).
42: trustasia - domain name certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: dnspod-enhanced (ev) ssl certificate.
47: dnspod-enhanced (ev) multiple domain names ssl certificate.
48: dnspod-domain name-based (dv) ssl certificate.
49: dnspod-domain name-based (dv) wildcard ssl certificate.
50: dnspod-domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional version multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional version multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise (ov) wildcard.
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise ov pro for multiple domain names.
93: securesite enterprise for multiple domain names (ov).
94: securesite ev pro for multiple domain names.
95: securesite ev for multiple domain names.
96: securesite ev pro.
97: securesite enterprise professional edition (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise multiple domain names (ov) ssl certificate.
100: cfca enterprise wildcard (ov) ssl certificate.
101: cfca enhanced (ev) ssl certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _ProductZhName: Certificate product name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param _Domain: Certificate binds to a common name domain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Status: Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = automatically added dns records, 5 = enterprise certificate, pending document submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending document submission, 14 = certificate has been refunded, 15 = certificate migration in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StatusMsg: Status information. valid values:.
//Common status information.
PRE-REVIEWING: in prereview.
LEGAL-REVIEWING: in legal review.
CA-REVIEWING: in ca review.
PENDING-DCV: in domain verification.
WAIT-ISSUE: waiting for issue (domain verification passed).
Certificate review failure status information.
1. order review failed.
2. ca review failed, and the domain name did not pass the security review.
3. domain name verification timed out, and the order was automatically closed. please reapply for the certificate.
4. the certificate information did not pass the review of the certificate ca agency. the reviewer will call the contact information reserved for the certificate. please pay attention to the incoming call. subsequently, you can resubmit the information through "modify information".
To be continuously improved.
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
        :param _InsertTime: Certificate application time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param _OrderId: CA order id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param _CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _CertificatePrivateKey: Private key certificate; for Chinese SM certificates, it refers to the private key certificate in the signature certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePrivateKey: str
        :param _CertificatePublicKey: Public key certificate; for Chinese SM certificate, it refers to the public key certificate in the signature certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePublicKey: str
        :param _DvAuthDetail: Certificate domain name verification information.
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
        :param _SubmittedData: Profile information submitted for paid certificates.
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
        :param _EncryptCert: Chinese SM certificate public key, only has value for national cryptography certificates.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EncryptCert: str
        :param _EncryptPrivateKey: Chinese SM certificate private key certificate, only has value for national cryptography certificates.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EncryptPrivateKey: str
        :param _CertFingerprint: SHA1 fingerprint of the signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertFingerprint: str
        :param _EncryptCertFingerprint: SHA1 fingerprint of the encryption certificate (for Chinese SM certificates only)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptCertFingerprint: str
        :param _EncryptAlgorithm: Certificate encryption algorithm (or Chinese SM certificates only).
Note: this field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgorithm: str
        :param _DvRevokeAuthDetail: The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DvRevokeAuthDetail: list of DvAuths
        :param _CertChainInfo: Certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertChainInfo: list of CertBasicInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        self._CertChainInfo = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        """Certificate belonging to user main account uin.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """Certificate source:.
trustAsia.
upload.
wosign.
sheca.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        """Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        """Certificate package type:.
null: user uploads a certificate (no package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise version (ev pro),. 
4: securesite enhanced (ev),. 
5: securesite enterprise pro (ov pro).
6: securesite enterprise (ov). 
7: securesite enterprise (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise (ov). 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain names (ev) ssl certificate.
25: wotrus domain cert.
26: wotrus multi-domain cert.
27: wotrus wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi-domain cert.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi-domain name certificate.
33: wotrus-national cryptography domain name certificate.
34: wotrus-national cryptography domain name certificate (multiple domain names).
35: wotrus-national cryptography wildcard certificate.
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus-national cryptography enhanced certificate.
41: wotrus - national cryptography enhanced certificate (multiple domain names).
42: trustasia - domain name certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: dnspod-enhanced (ev) ssl certificate.
47: dnspod-enhanced (ev) multiple domain names ssl certificate.
48: dnspod-domain name-based (dv) ssl certificate.
49: dnspod-domain name-based (dv) wildcard ssl certificate.
50: dnspod-domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional version multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional version multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise (ov) wildcard.
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise ov pro for multiple domain names.
93: securesite enterprise for multiple domain names (ov).
94: securesite ev pro for multiple domain names.
95: securesite ev for multiple domain names.
96: securesite ev pro.
97: securesite enterprise professional edition (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise multiple domain names (ov) ssl certificate.
100: cfca enterprise wildcard (ov) ssl certificate.
101: cfca enhanced (ev) ssl certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        """Certificate product name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """Certificate binds to a common name domain.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = automatically added dns records, 5 = enterprise certificate, pending document submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending document submission, 14 = certificate has been refunded, 15 = certificate migration in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        """Status information. valid values:.
//Common status information.
PRE-REVIEWING: in prereview.
LEGAL-REVIEWING: in legal review.
CA-REVIEWING: in ca review.
PENDING-DCV: in domain verification.
WAIT-ISSUE: waiting for issue (domain verification passed).
Certificate review failure status information.
1. order review failed.
2. ca review failed, and the domain name did not pass the security review.
3. domain name verification timed out, and the order was automatically closed. please reapply for the certificate.
4. the certificate information did not pass the review of the certificate ca agency. the reviewer will call the contact information reserved for the certificate. please pay attention to the incoming call. subsequently, you can resubmit the information through "modify information".
To be continuously improved.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        """Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        """Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """Certificate application time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        """CA order id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        """Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def CertificatePrivateKey(self):
        """Private key certificate; for Chinese SM certificates, it refers to the private key certificate in the signature certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificatePublicKey(self):
        """Public key certificate; for Chinese SM certificate, it refers to the public key certificate in the signature certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def DvAuthDetail(self):
        """Certificate domain name verification information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        """
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        """Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        """Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def TypeName(self):
        """Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StatusName(self):
        """Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        """Multiple domain names included in the certificate (excluding the primary domain name, which uses the `Domain` field)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        """Whether the certificate is a paid one.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        """Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        """Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        """Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def SubmittedData(self):
        """Profile information submitted for paid certificates.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        """
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def RenewAble(self):
        """Whether the certificate can be renewed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def Deployable(self):
        """Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """List of associated tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RootCert(self):
        """Root certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        """
        return self._RootCert

    @RootCert.setter
    def RootCert(self, RootCert):
        self._RootCert = RootCert

    @property
    def EncryptCert(self):
        """Chinese SM certificate public key, only has value for national cryptography certificates.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptCert

    @EncryptCert.setter
    def EncryptCert(self, EncryptCert):
        self._EncryptCert = EncryptCert

    @property
    def EncryptPrivateKey(self):
        """Chinese SM certificate private key certificate, only has value for national cryptography certificates.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptPrivateKey

    @EncryptPrivateKey.setter
    def EncryptPrivateKey(self, EncryptPrivateKey):
        self._EncryptPrivateKey = EncryptPrivateKey

    @property
    def CertFingerprint(self):
        """SHA1 fingerprint of the signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertFingerprint

    @CertFingerprint.setter
    def CertFingerprint(self, CertFingerprint):
        self._CertFingerprint = CertFingerprint

    @property
    def EncryptCertFingerprint(self):
        """SHA1 fingerprint of the encryption certificate (for Chinese SM certificates only)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptCertFingerprint

    @EncryptCertFingerprint.setter
    def EncryptCertFingerprint(self, EncryptCertFingerprint):
        self._EncryptCertFingerprint = EncryptCertFingerprint

    @property
    def EncryptAlgorithm(self):
        """Certificate encryption algorithm (or Chinese SM certificates only).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def DvRevokeAuthDetail(self):
        """The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DvAuths
        """
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def CertChainInfo(self):
        """Certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of CertBasicInfo
        """
        return self._CertChainInfo

    @CertChainInfo.setter
    def CertChainInfo(self, CertChainInfo):
        self._CertChainInfo = CertChainInfo

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
        if params.get("CertChainInfo") is not None:
            self._CertChainInfo = []
            for item in params.get("CertChainInfo"):
                obj = CertBasicInfo()
                obj._deserialize(item)
                self._CertChainInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. The default value is 0.
        :type Offset: int
        :param _Limit: Number of requested logs, 20 by default, with a maximum value of 1000. if it exceeds 1000, it will be treated as 1000.
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
        """Offset. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of requested logs, 20 by default, with a maximum value of 1000. if it exceeds 1000, it will be treated as 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """Start time. The default value is 15 days ago.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time. The default value is the current time.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllTotal = None
        self._TotalCount = None
        self._OperateLogs = None
        self._RequestId = None

    @property
    def AllTotal(self):
        """Total number of logs that meet query conditions
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def TotalCount(self):
        """Number of logs returned for this request
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OperateLogs(self):
        """Certificate operation log list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of OperationLog
        """
        return self._OperateLogs

    @OperateLogs.setter
    def OperateLogs(self, OperateLogs):
        self._OperateLogs = OperateLogs

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
        """Certificate ID
        :rtype: str
        """
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
        :param _From: Certificate source:
trustAsia.
upload.
wosign.
sheca.
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param _PackageType: Certificate package type:.
Null: user uploads a certificate (without package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise edition (ev pro),. 
4: securesite enhanced (ev),. 
5: securesite enterprise professional edition (ov pro).
6: securesite enterprise edition (ov). 
7: securesite enterprise edition (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise edition (ov). 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain names (ev) ssl certificate.
25: wotrus domain cert.
26: wotrus multi - domain name cert.
27: wotrus wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi - domain name cert.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi - domain name certificate.
33: wotrus - national cryptography domain - name certificate.
34: wotrus - national cryptography domain - name certificate (multiple domain names).
35: wotrus-national cryptography wildcard domain certificate.
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus-national cryptography enhanced certificate.
41: wotrus - national cryptography enhanced certificate (multiple domain names).
42: trustasia - domain name certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: dnspod-enhanced (ev) ssl certificate.
47: dnspod-enhanced (ev) multiple domain names ssl certificate.
48: dnspod-domain name-based (dv) ssl certificate.
49: dnspod-domain name-based (dv) wildcard ssl certificate.
50: dnspod-domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional version multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional version multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise (ov) wildcard.
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise ov pro for multiple domain names.
93: securesite enterprise for multiple domain names (ov).
94: securesite ev pro for multiple domain names.
95: securesite ev for multiple domain names.
96: securesite ev pro.
97: securesite enterprise professional version (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise multiple domain names (ov) ssl certificate.
100: cfca enterprise wildcard (ov) ssl certificate.
101: cfca enhanced (ev) ssl certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param _ProductZhName: Certificate product name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param _Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Status: Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = dns records added automatically, 5 = enterprise certificate, pending documentation submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending document submission, 14 = certificate has been refunded, 15 = certificate migration in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StatusMsg: Status information. valid values:.
//Common status information.
1. pre-reviewing: prereviewing.
2. legal-reviewing: under legal review.
3. ca-reviewing: under ca review.
4. pending-dcv: under domain verification.
5. wait-issue: waiting for issuance (domain verification passed).
//Certificate review failure status information.
Order review failed.
CA review failed; the domain name did not pass the security review.
Domain verification timed out, and the order was automatically closed. please reapply for the certificate.
The certificate information did not pass the review by the certificate authority. the reviewer will call the contact information reserved for the certificate. please pay attention to the incoming call. subsequently, you can resubmit the information through "modify information".
To be continuously improved.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param _VerifyType: Validation type: DNS_AUTO = automatic dns validation, DNS = manual dns validation, FILE = file verification, DNS_PROXY = dns proxy validation, FILE_PROXY = file proxy validation.
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
        :param _CAEncryptAlgorithms: All encryption methods of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CAEncryptAlgorithms: list of str
        :param _CACommonNames: All common names of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CACommonNames: list of str
        :param _CAEndTimes: All expiration times of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CAEndTimes: list of str
        :param _DvRevokeAuthDetail: The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """Certificate source:
trustAsia.
upload.
wosign.
sheca.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        """Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        """Certificate package type:.
Null: user uploads a certificate (without package type),.
2: trustasia tls rsa ca,. 
3: securesite enhanced enterprise edition (ev pro),. 
4: securesite enhanced (ev),. 
5: securesite enterprise professional edition (ov pro).
6: securesite enterprise edition (ov). 
7: securesite enterprise edition (ov) wildcard. 
8: geotrust enhanced (ev). 
9: geotrust enterprise edition (ov). 
10: geotrust enterprise (ov) wildcard cert. 
11: trustasia domain name-based multiple domain names ssl certificate. 
12: trustasia domain name-based (dv) wildcard cert. 
13: trustasia enterprise wildcard (ov) ssl certificate (d3). 
14: trustasia enterprise (ov) ssl certificate (d3). 
15: trustasia enterprise multiple domain names (ov) ssl certificate (d3). 
16: trustasia enhanced (ev) ssl certificate (d3). 
17: trustasia enhanced multiple domain names (ev) ssl certificate (d3). 
18: globalsign enterprise (ov) ssl certificate. 
19: globalsign enterprise wildcard (ov) ssl certificate. 
20: globalsign enhanced (ev) ssl certificate. 
21: trustasia enterprise wildcard multiple domain names (ov) ssl certificate (d3). 
22: globalsign enterprise multiple domain names (ov) ssl certificate. 
23: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
24: globalsign enhanced multiple domain names (ev) ssl certificate.
25: wotrus domain cert.
26: wotrus multi - domain name cert.
27: wotrus wildcard cert.
28: wotrus enterprise cert.
29: wotrus enterprise multi - domain name cert.
30: wotrus enterprise wildcard certificate.
31: wotrus enhanced certificate.
32: wotrus enhanced multi - domain name certificate.
33: wotrus - national cryptography domain - name certificate.
34: wotrus - national cryptography domain - name certificate (multiple domain names).
35: wotrus-national cryptography wildcard domain certificate.
37: wotrus-national cryptography enterprise certificate.
38: wotrus-national cryptography enterprise certificate (multiple domain names).
39: wotrus-national cryptography enterprise certificate (wildcard).
40: wotrus-national cryptography enhanced certificate.
41: wotrus - national cryptography enhanced certificate (multiple domain names).
42: trustasia - domain name certificate (wildcard multiple domain names).
43: DNSPod - enterprise (ov) ssl certificate.
44: DNSPod - enterprise (ov) wildcard ssl certificate.
45: DNSPod - enterprise (ov) multiple domain names ssl certificate.
46: dnspod-enhanced (ev) ssl certificate.
47: dnspod-enhanced (ev) multiple domain names ssl certificate.
48: dnspod-domain name-based (dv) ssl certificate.
49: dnspod-domain name-based (dv) wildcard ssl certificate.
50: dnspod-domain name-based (dv) multiple domain names ssl certificate.
51: DNSPod (national cryptography) - enterprise (ov) ssl certificate.
52: DNSPod (national cryptography) - enterprise (ov) wildcard ssl certificate.
53: DNSPod (national cryptography) - enterprise (ov) multiple domain names ssl certificate.
54: DNSPod (national cryptography) - domain name-based (dv) ssl certificate.
55: DNSPod (national cryptography) - domain name-based (dv) wildcard ssl certificate.
56: DNSPod (national cryptography) - domain name-based (dv) multiple domain names ssl certificate.
57: securesite enterprise professional version multiple domain names (ov pro).
58: securesite enterprise multiple domain names (ov).
59: securesite enhanced professional version multiple domain names (ev pro).
60: securesite enhanced multiple domain names (ev).
61: geotrust enhanced multiple domain names (ev).
75: securesite enterprise (ov).
76: securesite enterprise (ov) wildcard.
77: securesite enhanced (ev).
78: geotrust enterprise (ov).
79: geotrust enterprise (ov) wildcard.
80: geotrust enhanced (ev).
81: globalsign enterprise (ov) ssl certificate.
82: globalsign enterprise wildcard (ov) ssl certificate.
83: trustasia c1 dv free.
85: globalsign enhanced (ev) ssl certificate.
88: globalsign enterprise wildcard multiple domain names (ov) ssl certificate.
89: globalsign enterprise multiple domain names (ov) ssl certificate.
90: globalsign enhanced multiple domain names (ev) ssl certificate.
91: geotrust enhanced multiple domain names (ev).
92: securesite enterprise ov pro for multiple domain names.
93: securesite enterprise for multiple domain names (ov).
94: securesite ev pro for multiple domain names.
95: securesite ev for multiple domain names.
96: securesite ev pro.
97: securesite enterprise professional version (ov pro).
98: cfca enterprise (ov) ssl certificate.
99: cfca enterprise multiple domain names (ov) ssl certificate.
100: cfca enterprise wildcard (ov) ssl certificate.
101: cfca enhanced (ev) ssl certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        """Certificate product name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """Certificate status: 0 = under review, 1 = approved, 2 = review failed, 3 = expired, 4 = dns records added automatically, 5 = enterprise certificate, pending documentation submission, 6 = order cancellation in progress, 7 = canceled, 8 = documents submitted, pending upload of confirmation letter, 9 = certificate revocation in progress, 10 = revoked, 11 = reissue in progress, 12 = pending upload of revocation confirmation letter, 13 = free certificate pending document submission, 14 = certificate has been refunded, 15 = certificate migration in progress.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        """Status information. valid values:.
//Common status information.
1. pre-reviewing: prereviewing.
2. legal-reviewing: under legal review.
3. ca-reviewing: under ca review.
4. pending-dcv: under domain verification.
5. wait-issue: waiting for issuance (domain verification passed).
//Certificate review failure status information.
Order review failed.
CA review failed; the domain name did not pass the security review.
Domain verification timed out, and the order was automatically closed. please reapply for the certificate.
The certificate information did not pass the review by the certificate authority. the reviewer will call the contact information reserved for the certificate. please pay attention to the incoming call. subsequently, you can resubmit the information through "modify information".
To be continuously improved.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """Validation type: DNS_AUTO = automatic dns validation, DNS = manual dns validation, FILE = file verification, DNS_PROXY = dns proxy validation, FILE_PROXY = file proxy validation.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        """Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        """Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        """Order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        """Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def DvAuthDetail(self):
        """DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        """
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        """Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        """Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PackageTypeName(self):
        """Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        """Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        """Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        """Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        """Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        """Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        """Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        """Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def SubmittedData(self):
        """Submitted data
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        """
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def Deployable(self):
        """Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CAEncryptAlgorithms(self):
        """All encryption methods of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CACommonNames(self):
        """All common names of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def CAEndTimes(self):
        """All expiration times of the ca certificate. only valid when the certificate type CertificateType is ca.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def DvRevokeAuthDetail(self):
        """The authentication value for DV certificate revocation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DvAuths
        """
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

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
        :param _Offset: Pagination offset, starting from 0. default is 0.
        :type Offset: int
        :param _Limit: Number of items per page. default is 10. maximum value is 1000; values exceeding 1000 will be treated as 1000.
        :type Limit: int
        :param _SearchKey: Search keywords, supporting fuzzy match by certificate id, remark name, and certificate domain name.
        :type SearchKey: str
        :param _CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
        :type CertificateType: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ExpirationSort: Default sorting is by certificate application time in descending order. Sort by expiration date if the following values are passed: DESC for descending order of certificate expiration time, ASC for ascending order.
        :type ExpirationSort: str
        :param _CertificateStatus: Certificate status: 0=under review, 1=approved, 2=review failed, 3=expired, 4=dns record added, 5=enterprise certificate, pending submission, 6=order cancellation in progress, 7=canceled, 8=documents submitted, pending upload of confirmation letter, 9=certificate revocation in progress, 10=revoked, 11=reissue in progress, 12=pending upload of revocation confirmation letter, 13=free certificate pending document submission, 14=refunded, 15=certificate migration in progress.
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
        :param _Tags: Filter certificates with specified tags.
        :type Tags: list of Tags
        :param _IsPendingIssue: Whether to filter certificates pending issue: 1 for filtering, 0 and null for no filtering.
        :type IsPendingIssue: int
        :param _CertIds: Filter certificates by the specified certificate id, only supports certificate ids with permission.
        :type CertIds: list of str
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
        self._Tags = None
        self._IsPendingIssue = None
        self._CertIds = None

    @property
    def Offset(self):
        """Pagination offset, starting from 0. default is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of items per page. default is 10. maximum value is 1000; values exceeding 1000 will be treated as 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        """Search keywords, supporting fuzzy match by certificate id, remark name, and certificate domain name.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CertificateType(self):
        """Certificate type. `CA`: client certificate; `SVR`: server certificate
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ExpirationSort(self):
        """Default sorting is by certificate application time in descending order. Sort by expiration date if the following values are passed: DESC for descending order of certificate expiration time, ASC for ascending order.
        :rtype: str
        """
        return self._ExpirationSort

    @ExpirationSort.setter
    def ExpirationSort(self, ExpirationSort):
        self._ExpirationSort = ExpirationSort

    @property
    def CertificateStatus(self):
        """Certificate status: 0=under review, 1=approved, 2=review failed, 3=expired, 4=dns record added, 5=enterprise certificate, pending submission, 6=order cancellation in progress, 7=canceled, 8=documents submitted, pending upload of confirmation letter, 9=certificate revocation in progress, 10=revoked, 11=reissue in progress, 12=pending upload of revocation confirmation letter, 13=free certificate pending document submission, 14=refunded, 15=certificate migration in progress.
        :rtype: list of int non-negative
        """
        return self._CertificateStatus

    @CertificateStatus.setter
    def CertificateStatus(self, CertificateStatus):
        self._CertificateStatus = CertificateStatus

    @property
    def Deployable(self):
        """Whether the certificate can be deployed. `1`: yes; `0`: no
        :rtype: int
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Upload(self):
        """Whether to filter uploaded hosted certificates. `1`: Yes; `0`: No.
        :rtype: int
        """
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Renew(self):
        """Whether to filter renewable certificates. `1`: Yes; `0`: No.
        :rtype: int
        """
        return self._Renew

    @Renew.setter
    def Renew(self, Renew):
        self._Renew = Renew

    @property
    def FilterSource(self):
        """Filter by source. `upload`: Uploaded certificate; `buy`: Tencent Cloud certificate. If this parameter is left empty, all certificates will be queried.
        :rtype: str
        """
        return self._FilterSource

    @FilterSource.setter
    def FilterSource(self, FilterSource):
        self._FilterSource = FilterSource

    @property
    def IsSM(self):
        """Whether to filter Chinese SM certificates. `1`: Yes; `0`: No.
        :rtype: int
        """
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def FilterExpiring(self):
        """Whether to filter expiring certificates. `1`: Yes; `0`: No.
        :rtype: int
        """
        return self._FilterExpiring

    @FilterExpiring.setter
    def FilterExpiring(self, FilterExpiring):
        self._FilterExpiring = FilterExpiring

    @property
    def Hostable(self):
        """Whether the certificate can be hosted. Valid values: `1` for yes and `0` for no.
        :rtype: int
        """
        return self._Hostable

    @Hostable.setter
    def Hostable(self, Hostable):
        self._Hostable = Hostable

    @property
    def Tags(self):
        """Filter certificates with specified tags.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsPendingIssue(self):
        """Whether to filter certificates pending issue: 1 for filtering, 0 and null for no filtering.
        :rtype: int
        """
        return self._IsPendingIssue

    @IsPendingIssue.setter
    def IsPendingIssue(self, IsPendingIssue):
        self._IsPendingIssue = IsPendingIssue

    @property
    def CertIds(self):
        """Filter certificates by the specified certificate id, only supports certificate ids with permission.
        :rtype: list of str
        """
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsPendingIssue = params.get("IsPendingIssue")
        self._CertIds = params.get("CertIds")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Certificates = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Certificates(self):
        """List
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Certificates
        """
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

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
        :param _Offset: Paging offset. default value: 0.
        :type Offset: int
        :param _Limit: Number of items per page. default: 10. maximum value: 200.	
        :type Limit: int
        :param _AsyncCache: Asynchronous or not. 1 means yes, 0 means no. default: 0.
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
        """The ID of the certificate to be deployed.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """The type of resource for certificate deployment.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        """Whether to query the cached results. Valid values: `1` (yes) and `0` (no). By default, the cached results within 30 minutes are queried.
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """The list of filter parameters. FilterKey: domainMatch (query the list of instances with matching or non-matching domains). FilterValue: `1` (default; query the list of instances with matching domains) or `0` (query the list of instances with non-matching domains).
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        """The ID of the deployed certificate.
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Offset(self):
        """Paging offset. default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of items per page. default: 10. maximum value: 200.	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AsyncCache(self):
        """Asynchronous or not. 1 means yes, 0 means no. default: 0.
        :rtype: int
        """
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
        :param _InstanceList: Teo instance list. if no value is obtained, an empty array is returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """Teo instance list. if no value is obtained, an empty array is returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of TeoInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total count.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        :param _DeployRecordId: Deployment record id, which is the record id returned by calling the UpdateCertificateInstance api, or the record id returned by calling the UpdateCertificateRecordRollback rollback api.
        :type DeployRecordId: str
        :param _Limit: Number of items per page. the default is 10. the maximum value is 200.
        :type Limit: str
        :param _Offset: Pagination offset, starting from 0. default is 0.
        :type Offset: str
        """
        self._DeployRecordId = None
        self._Limit = None
        self._Offset = None

    @property
    def DeployRecordId(self):
        """Deployment record id, which is the record id returned by calling the UpdateCertificateInstance api, or the record id returned by calling the UpdateCertificateRecordRollback rollback api.
        :rtype: str
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def Limit(self):
        """Number of items per page. the default is 10. the maximum value is 200.
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Pagination offset, starting from 0. default is 0.
        :rtype: str
        """
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
        :param _TotalCount: If the total number cannot be obtained, return 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RecordDetailList: Certificate deployment record list; returns an empty array if no value is obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecordDetailList: list of UpdateRecordDetails
        :param _SuccessTotalCount: Total number of successes; returns 0 if unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SuccessTotalCount: int
        :param _FailedTotalCount: Total number of failures. if it cannot be obtained, return 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailedTotalCount: int
        :param _RunningTotalCount: Total number of deployments in progress; returns 0 if unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RunningTotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """If the total number cannot be obtained, return 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordDetailList(self):
        """Certificate deployment record list; returns an empty array if no value is obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of UpdateRecordDetails
        """
        return self._RecordDetailList

    @RecordDetailList.setter
    def RecordDetailList(self, RecordDetailList):
        self._RecordDetailList = RecordDetailList

    @property
    def SuccessTotalCount(self):
        """Total number of successes; returns 0 if unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        """Total number of failures. if it cannot be obtained, return 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        """Total number of deployments in progress; returns 0 if unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

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
        """Paging offset, starting from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number per page, 10 by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CertificateId(self):
        """New certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def OldCertificateId(self):
        """Old certificate ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total count
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        """Certificate deployment record list
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of UpdateRecordInfo
        """
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

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
        """Certificate ID
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._ContentType = None
        self._RequestId = None

    @property
    def Content(self):
        """ZIP content encoded by using Base64. After the content is decoded by using Base64, it can be saved as a ZIP file.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        """MIME type. `application/zip`: ZIP file
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

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
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        self._RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """Content of the `DvAuthDetail` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: Certificate domain name verification record key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param _DvAuthValue: Certificate domain name verification record value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param _DvAuthDomain: Certificate domain name verification domain value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param _DvAuthPath: Certificate domain name verification file path, used only for file and file_proxy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param _DvAuthKeySubDomain: Certificate domain name verification subdomain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKeySubDomain: str
        :param _DvAuths: Certificate domain verification information; multiple domain verifications use this field.
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
        """Certificate domain name verification record key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        """Certificate domain name verification record value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        """Certificate domain name verification domain value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        """Certificate domain name verification file path, used only for file and file_proxy.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthKeySubDomain(self):
        """Certificate domain name verification subdomain.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthKeySubDomain

    @DvAuthKeySubDomain.setter
    def DvAuthKeySubDomain(self, DvAuthKeySubDomain):
        self._DvAuthKeySubDomain = DvAuthKeySubDomain

    @property
    def DvAuths(self):
        """Certificate domain verification information; multiple domain verifications use this field.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DvAuths
        """
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
        :param _DvAuthKey: Certificate domain name verification record key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param _DvAuthValue: Certificate domain name verification record value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param _DvAuthDomain: Certificate domain name verification domain value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param _DvAuthPath: Certificate domain name verification file path, used only for file and file_proxy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param _DvAuthSubDomain: Certificate domain name verification subdomain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthSubDomain: str
        :param _DvAuthVerifyType: Certificate domain verification type, valid values:.
TXT: add txt record for dns domain verification.
FILE: domain file verification.
CNAME: add cname record for dns domain verification.
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
        """Certificate domain name verification record key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        """Certificate domain name verification record value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        """Certificate domain name verification domain value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        """Certificate domain name verification file path, used only for file and file_proxy.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthSubDomain(self):
        """Certificate domain name verification subdomain.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DvAuthSubDomain

    @DvAuthSubDomain.setter
    def DvAuthSubDomain(self, DvAuthSubDomain):
        self._DvAuthSubDomain = DvAuthSubDomain

    @property
    def DvAuthVerifyType(self):
        """Certificate domain verification type, valid values:.
TXT: add txt record for dns domain verification.
FILE: domain file verification.
CNAME: add cname record for dns domain verification.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """The error code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """The error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        :param _FilterValue: The value of the filter parameter.
        :type FilterValue: str
        """
        self._FilterKey = None
        self._FilterValue = None

    @property
    def FilterKey(self):
        """The key of the filter parameter.
        :rtype: str
        """
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def FilterValue(self):
        """The value of the filter parameter.
        :rtype: str
        """
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
        """Gateway certificate ID
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Gateway certificate information
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BindDomains(self):
        """Bound domain name
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def CertSource(self):
        """Certificate source
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource

    @property
    def CertId(self):
        """SSL certificate ID that is currently bound
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
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
        


class HostingConfig(AbstractModel):
    """Managed configuration.

    """

    def __init__(self):
        r"""
        :param _ReplaceTime: Hosted resource replacement time, defaults to 30 days before the certificate expiration if there is a renewal certificate, then replace.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplaceTime: int
        :param _MessageTypes: Hosted send message type: 0, reminder message before hosted starts (you will receive this reminder message even if there is no renewal certificate); 1, reminder message when hosted starts (you will receive the message reminder only if there is a renewal certificate); 2, reminder message when hosted resource replacement fails; 3 reminder message when hosted resource replacement succeeds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageTypes: list of int
        :param _ReplaceStartTime: Resource replacement start time.
        :type ReplaceStartTime: str
        :param _ReplaceEndTime: Resource replacement end time.
        :type ReplaceEndTime: str
        """
        self._ReplaceTime = None
        self._MessageTypes = None
        self._ReplaceStartTime = None
        self._ReplaceEndTime = None

    @property
    def ReplaceTime(self):
        """Hosted resource replacement time, defaults to 30 days before the certificate expiration if there is a renewal certificate, then replace.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReplaceTime

    @ReplaceTime.setter
    def ReplaceTime(self, ReplaceTime):
        self._ReplaceTime = ReplaceTime

    @property
    def MessageTypes(self):
        """Hosted send message type: 0, reminder message before hosted starts (you will receive this reminder message even if there is no renewal certificate); 1, reminder message when hosted starts (you will receive the message reminder only if there is a renewal certificate); 2, reminder message when hosted resource replacement fails; 3 reminder message when hosted resource replacement succeeds.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._MessageTypes

    @MessageTypes.setter
    def MessageTypes(self, MessageTypes):
        self._MessageTypes = MessageTypes

    @property
    def ReplaceStartTime(self):
        """Resource replacement start time.
        :rtype: str
        """
        return self._ReplaceStartTime

    @ReplaceStartTime.setter
    def ReplaceStartTime(self, ReplaceStartTime):
        self._ReplaceStartTime = ReplaceStartTime

    @property
    def ReplaceEndTime(self):
        """Resource replacement end time.
        :rtype: str
        """
        return self._ReplaceEndTime

    @ReplaceEndTime.setter
    def ReplaceEndTime(self, ReplaceEndTime):
        self._ReplaceEndTime = ReplaceEndTime


    def _deserialize(self, params):
        self._ReplaceTime = params.get("ReplaceTime")
        self._MessageTypes = params.get("MessageTypes")
        self._ReplaceStartTime = params.get("ReplaceStartTime")
        self._ReplaceEndTime = params.get("ReplaceEndTime")
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
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """The status. Valid values: `-1`: No certificate is associated with the domain.
`1`: HTTPS is enabled for the domain.
`0`: HTTPS is disabled for the domain.
        :rtype: int
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """The total number of LIVE instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """The list of LIVE instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LiveInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
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
        """The CSR ID.	
        :rtype: int
        """
        return self._CSRId

    @CSRId.setter
    def CSRId(self, CSRId):
        self._CSRId = CSRId

    @property
    def Generate(self):
        """Whether to generate the CSR content. Once the CSR content is generated, the CSR record cannot be modified.
        :rtype: bool
        """
        return self._Generate

    @Generate.setter
    def Generate(self, Generate):
        self._Generate = Generate

    @property
    def Domain(self):
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Organization(self):
        """The organization name.
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Department(self):
        """The department.
        :rtype: str
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Email(self):
        """The email address.
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Province(self):
        """The province.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """The country or region.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def EncryptAlgo(self):
        """The encryption algorithm. RSA and ECC are supported.	
        :rtype: str
        """
        return self._EncryptAlgo

    @EncryptAlgo.setter
    def EncryptAlgo(self, EncryptAlgo):
        self._EncryptAlgo = EncryptAlgo

    @property
    def KeyParameter(self):
        """The key pair parameter. For RSA, only the 2048-bit and 4096-bit key pairs are supported. For ECC, only prime256v1 is supported.
        :rtype: str
        """
        return self._KeyParameter

    @KeyParameter.setter
    def KeyParameter(self, KeyParameter):
        self._KeyParameter = KeyParameter

    @property
    def Remark(self):
        """The remarks.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def KeyPassword(self):
        """The password of the private key.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """The CSR ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Alias(self):
        """Alias
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """ID of the successfully modified certificate
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        """ID list of certificates whose projects need to be modified. A maximum of 100 certificate IDs are supported.
        :rtype: list of str
        """
        return self._CertificateIdList

    @CertificateIdList.setter
    def CertificateIdList(self, CertificateIdList):
        self._CertificateIdList = CertificateIdList

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessCertificates = None
        self._FailCertificates = None
        self._RequestId = None

    @property
    def SuccessCertificates(self):
        """List of certificates whose projects were modified successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SuccessCertificates

    @SuccessCertificates.setter
    def SuccessCertificates(self, SuccessCertificates):
        self._SuccessCertificates = SuccessCertificates

    @property
    def FailCertificates(self):
        """List of certificates whose projects failed to be modified
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FailCertificates

    @FailCertificates.setter
    def FailCertificates(self, FailCertificates):
        self._FailCertificates = FailCertificates

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
        """The certificate ID.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """The certificate ID.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        :param _Uin: Root account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _SubAccountUin: Sub-Account.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubAccountUin: str
        :param _CertId: Certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Type: Each operation type corresponds to a specific operation description. the following is a textual explanation of each operation type and its description:.
1. apply: indicates applying for a free cert.
2. delete: indicates a deletion.
3. download - represents the download operation.
4. upload: indicates an upload operation.
5. revoke: indicates revoking a cert.
6. cancelRevoke - indicates canceling the revocation operation.
7. updateAlias - indicates updating the remark information.
8. changeProject - indicates assigning the certificate to a certain project.
9. uploadConfirmLetter - indicates uploading the confirmation letter.
10. cancel - indicates canceling the order operation.
11. replace - specifies reissuing a certificate.
12. downloadConfirmLetter - specifies downloading a certificate revocation confirmation letter.
13. editRevokeLetter - specifies uploading a certificate revocation confirmation letter.
14. renewVIP - specifies renewing a paid certificate.
15. applyVIP - specifies applying for a paid certificate.
16. submitInfo - specifies submitting documentation.
17. downloadConfirmLetter - specifies downloading the confirmation letter template.
18. uploadFromYunAPI - indicates uploading via the cloud api.
19. transferIn - indicates the certificate transfer to operation.
20. transferOut - indicates the certificate transfer operation.
21. refund - indicates applying for a refund.
22. multiYearsRenew - indicates multi-year auto-renewal.
23. modifyDownloadLimit - indicates modifying the download limit switch.
24. issued - indicates certificate issuance.
25. domainValidationPassed - indicates domain verification completed.
26. Resubmit - indicates reapplying for a certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: str
        """
        self._Action = None
        self._CreatedOn = None
        self._Uin = None
        self._SubAccountUin = None
        self._CertId = None
        self._Type = None

    @property
    def Action(self):
        """Action performed on logs
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CreatedOn(self):
        """Time when the action is performed
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def Uin(self):
        """Root account.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        """Sub-Account.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def CertId(self):
        """Certificate id.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Type(self):
        """Each operation type corresponds to a specific operation description. the following is a textual explanation of each operation type and its description:.
1. apply: indicates applying for a free cert.
2. delete: indicates a deletion.
3. download - represents the download operation.
4. upload: indicates an upload operation.
5. revoke: indicates revoking a cert.
6. cancelRevoke - indicates canceling the revocation operation.
7. updateAlias - indicates updating the remark information.
8. changeProject - indicates assigning the certificate to a certain project.
9. uploadConfirmLetter - indicates uploading the confirmation letter.
10. cancel - indicates canceling the order operation.
11. replace - specifies reissuing a certificate.
12. downloadConfirmLetter - specifies downloading a certificate revocation confirmation letter.
13. editRevokeLetter - specifies uploading a certificate revocation confirmation letter.
14. renewVIP - specifies renewing a paid certificate.
15. applyVIP - specifies applying for a paid certificate.
16. submitInfo - specifies submitting documentation.
17. downloadConfirmLetter - specifies downloading the confirmation letter template.
18. uploadFromYunAPI - indicates uploading via the cloud api.
19. transferIn - indicates the certificate transfer to operation.
20. transferOut - indicates the certificate transfer operation.
21. refund - indicates applying for a refund.
22. multiYearsRenew - indicates multi-year auto-renewal.
23. modifyDownloadLimit - indicates modifying the download limit switch.
24. issued - indicates certificate issuance.
25. domainValidationPassed - indicates domain verification completed.
26. Resubmit - indicates reapplying for a certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CreatedOn = params.get("CreatedOn")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._CertId = params.get("CertId")
        self._Type = params.get("Type")
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
        """Total number of years of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPeriod

    @TotalPeriod.setter
    def TotalPeriod(self, TotalPeriod):
        self._TotalPeriod = TotalPeriod

    @property
    def NowPeriod(self):
        """Current year of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NowPeriod

    @NowPeriod.setter
    def NowPeriod(self, NowPeriod):
        self._NowPeriod = NowPeriod

    @property
    def ManagerId(self):
        """Certificate prereview manager ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Project name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectCreatorUin(self):
        """UIN of the project creator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectCreatorUin

    @ProjectCreatorUin.setter
    def ProjectCreatorUin(self, ProjectCreatorUin):
        self._ProjectCreatorUin = ProjectCreatorUin

    @property
    def ProjectCreateTime(self):
        """Project creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectCreateTime

    @ProjectCreateTime.setter
    def ProjectCreateTime(self, ProjectCreateTime):
        self._ProjectCreateTime = ProjectCreateTime

    @property
    def ProjectResume(self):
        """Brief project information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectResume

    @ProjectResume.setter
    def ProjectResume(self, ProjectResume):
        self._ProjectResume = ProjectResume

    @property
    def OwnerUin(self):
        """User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        :param _CsrType: Type. `Original`: original certificate CSR; `Upload`: uploaded manually; `Online`: generated online. The default value is original.
        :type CsrType: str
        :param _CsrContent: CSR content, required when uploading manually.
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
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ValidType(self):
        """Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation
        :rtype: str
        """
        return self._ValidType

    @ValidType.setter
    def ValidType(self, ValidType):
        self._ValidType = ValidType

    @property
    def CsrType(self):
        """Type. `Original`: original certificate CSR; `Upload`: uploaded manually; `Online`: generated online. The default value is original.
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """CSR content, required when uploading manually.
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CsrkeyPassword(self):
        """Password of the key
        :rtype: str
        """
        return self._CsrkeyPassword

    @CsrkeyPassword.setter
    def CsrkeyPassword(self, CsrkeyPassword):
        self._CsrkeyPassword = CsrkeyPassword

    @property
    def Reason(self):
        """Reissue reason
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def CertCSREncryptAlgo(self):
        """The CSR encryption algorithm. Valid values: `RSA` (default), `ECC1`, and `SM2`.
This parameter is available for selection only when the value of `CsrType` is `Online`.
        :rtype: str
        """
        return self._CertCSREncryptAlgo

    @CertCSREncryptAlgo.setter
    def CertCSREncryptAlgo(self, CertCSREncryptAlgo):
        self._CertCSREncryptAlgo = CertCSREncryptAlgo

    @property
    def CertCSRKeyParameter(self):
        """The CSR encryption parameters. When `CsrEncryptAlgo` is set to `RSA`, `2048` (default) and `4096` are available for selection; and when`CsrEncryptAlgo` is set to `ECC`, `prime256v1` (default) and `secp384r1` are available for selection. 
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ResourceTypeRegions(AbstractModel):
    """Cloud resource region list

    """

    def __init__(self):
        r"""
        :param _ResourceType: Cloud resource types, which support clb, waf, api gateway, cos, tke, tse, and tcb.
        :type ResourceType: str
        :param _Regions: Region list
        :type Regions: list of str
        """
        self._ResourceType = None
        self._Regions = None

    @property
    def ResourceType(self):
        """Cloud resource types, which support clb, waf, api gateway, cos, tke, tse, and tcb.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Regions(self):
        """Region list
        :rtype: list of str
        """
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
        """Chinese SM signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Encrypt(self):
        """Chinese SM encryption certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Standard(self):
        """Standard certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        :param _CertificateId: Paid certificate id of materials to be submitted.
        :type CertificateId: str
        :param _CsrType: This field is required. Generation method of CSR, valid values are:
online: tencent cloud generates the CSR and private key based on the submitted parameter information and stores them encryptedly.
parse: generate the CSR and private key by itself, and apply for a certificate by uploading the CSR.
        :type CsrType: str
        :param _CsrContent: The content of the uploaded csr.
If CsrType is parse, this field is required.
        :type CsrContent: str
        :param _CertificateDomain: The common name bound to the certificate. if a CSR is uploaded, the domain name must be consistent with the common name resolved from the CSR.
        :type CertificateDomain: str
        :param _DomainList: Other domain names bound to the certificate. not required for single domain and wildcard domain certificates. required for multiple domain names and multiple wildcard domain names.
        :type DomainList: list of str
        :param _KeyPassword: Private key password, which is currently only used for the password when generating jks and pfx format certificates; other formats of private key certificates are not encrypted.	
        :type KeyPassword: str
        :param _OrganizationName: This field is required. Company name.
        :type OrganizationName: str
        :param _OrganizationDivision: This field is required.  Department name.
        :type OrganizationDivision: str
        :param _OrganizationAddress: This field is required. Company's detailed address.
        :type OrganizationAddress: str
        :param _OrganizationCountry: This field is required.Country name such as CN.
        :type OrganizationCountry: str
        :param _OrganizationCity: This field is required, which specifies the city where the company is located.
        :type OrganizationCity: str
        :param _OrganizationRegion: This field is required, specifying the province where the company is located.
        :type OrganizationRegion: str
        :param _PostalCode: Postal code of the organization
        :type PostalCode: str
        :param _PhoneAreaCode: This field is required, the company's fixed-line phone area code.
        :type PhoneAreaCode: str
        :param _PhoneNumber: This field is required, the company's landline number.
        :type PhoneNumber: str
        :param _VerifyType: Certificate validation method. Validation types: DNS_AUTO = Automatic DNS validation (only supported for domains resolved by Tencent Cloud DNS with a normal resolution status), DNS = Manual DNS validation, FILE = File validation.
        :type VerifyType: str
        :param _AdminFirstName: This field is required, manager name.
        :type AdminFirstName: str
        :param _AdminLastName: This field is required, the manager's surname.
        :type AdminLastName: str
        :param _AdminPhoneNum: This field is required, the manager's mobile phone number.
        :type AdminPhoneNum: str
        :param _AdminEmail: This field is required, the manager's email address.
        :type AdminEmail: str
        :param _AdminPosition: This field is required, the manager position.
        :type AdminPosition: str
        :param _ContactFirstName: This field is required, the contact person name.
        :type ContactFirstName: str
        :param _ContactLastName: This field is required, the contact person's surname.
        :type ContactLastName: str
        :param _ContactEmail: This field is required, the contact person's email address.
        :type ContactEmail: str
        :param _ContactNumber: This field is required, the contact person's mobile phone number.
        :type ContactNumber: str
        :param _ContactPosition: This field is required, the contact person position.
        :type ContactPosition: str
        :param _IsDV: Indicates whether it is a dv certificate. default value is false.
        :type IsDV: bool
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
        self._IsDV = None

    @property
    def CertificateId(self):
        """Paid certificate id of materials to be submitted.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CsrType(self):
        """This field is required. Generation method of CSR, valid values are:
online: tencent cloud generates the CSR and private key based on the submitted parameter information and stores them encryptedly.
parse: generate the CSR and private key by itself, and apply for a certificate by uploading the CSR.
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """The content of the uploaded csr.
If CsrType is parse, this field is required.
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        """The common name bound to the certificate. if a CSR is uploaded, the domain name must be consistent with the common name resolved from the CSR.
        :rtype: str
        """
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        """Other domain names bound to the certificate. not required for single domain and wildcard domain certificates. required for multiple domain names and multiple wildcard domain names.
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        """Private key password, which is currently only used for the password when generating jks and pfx format certificates; other formats of private key certificates are not encrypted.	
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        """This field is required. Company name.
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        """This field is required.  Department name.
        :rtype: str
        """
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        """This field is required. Company's detailed address.
        :rtype: str
        """
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        """This field is required.Country name such as CN.
        :rtype: str
        """
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        """This field is required, which specifies the city where the company is located.
        :rtype: str
        """
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        """This field is required, specifying the province where the company is located.
        :rtype: str
        """
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        """Postal code of the organization
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        """This field is required, the company's fixed-line phone area code.
        :rtype: str
        """
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        """This field is required, the company's landline number.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def VerifyType(self):
        """Certificate validation method. Validation types: DNS_AUTO = Automatic DNS validation (only supported for domains resolved by Tencent Cloud DNS with a normal resolution status), DNS = Manual DNS validation, FILE = File validation.
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def AdminFirstName(self):
        """This field is required, manager name.
        :rtype: str
        """
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        """This field is required, the manager's surname.
        :rtype: str
        """
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        """This field is required, the manager's mobile phone number.
        :rtype: str
        """
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        """This field is required, the manager's email address.
        :rtype: str
        """
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        """This field is required, the manager position.
        :rtype: str
        """
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        """This field is required, the contact person name.
        :rtype: str
        """
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        """This field is required, the contact person's surname.
        :rtype: str
        """
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactEmail(self):
        """This field is required, the contact person's email address.
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactNumber(self):
        """This field is required, the contact person's mobile phone number.
        :rtype: str
        """
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactPosition(self):
        """This field is required, the contact person position.
        :rtype: str
        """
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def IsDV(self):
        """Indicates whether it is a dv certificate. default value is false.
        :rtype: bool
        """
        return self._IsDV

    @IsDV.setter
    def IsDV(self, IsDV):
        self._IsDV = IsDV


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
        self._IsDV = params.get("IsDV")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        """CSR type. `online`: CSR generated online; `parse`: CSR pasted
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """CSR content
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        """Domain name information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        """DNS information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        """Password of the private key
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        """Enterprise or unit name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        """Division
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        """Address
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        """Country
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        """City
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        """Province
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        """Postal code
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        """Area code of the fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        """Fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AdminFirstName(self):
        """First name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        """Last name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        """Phone number of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        """Email of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        """Position of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        """First name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        """Last name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactNumber(self):
        """Phone number of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactEmail(self):
        """Email of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPosition(self):
        """Position of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def VerifyType(self):
        """Validation type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
    """Supported types for download.

    """

    def __init__(self):
        r"""
        :param _NGINX: Whether the available format of nginx can be downloaded.
        :type NGINX: bool
        :param _APACHE: Whether the available format of apache can be downloaded.
        :type APACHE: bool
        :param _TOMCAT: Whether the available format of tomcat can be downloaded.
        :type TOMCAT: bool
        :param _IIS: Whether the available format of iis can be downloaded.
        :type IIS: bool
        :param _JKS: Indicates whether the jks format can be downloaded.
        :type JKS: bool
        :param _OTHER: Indicates whether other formats can be downloaded.
        :type OTHER: bool
        :param _ROOT: Indicates whether the root certificate can be downloaded.
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
        """Whether the available format of nginx can be downloaded.
        :rtype: bool
        """
        return self._NGINX

    @NGINX.setter
    def NGINX(self, NGINX):
        self._NGINX = NGINX

    @property
    def APACHE(self):
        """Whether the available format of apache can be downloaded.
        :rtype: bool
        """
        return self._APACHE

    @APACHE.setter
    def APACHE(self, APACHE):
        self._APACHE = APACHE

    @property
    def TOMCAT(self):
        """Whether the available format of tomcat can be downloaded.
        :rtype: bool
        """
        return self._TOMCAT

    @TOMCAT.setter
    def TOMCAT(self, TOMCAT):
        self._TOMCAT = TOMCAT

    @property
    def IIS(self):
        """Whether the available format of iis can be downloaded.
        :rtype: bool
        """
        return self._IIS

    @IIS.setter
    def IIS(self, IIS):
        self._IIS = IIS

    @property
    def JKS(self):
        """Indicates whether the jks format can be downloaded.
        :rtype: bool
        """
        return self._JKS

    @JKS.setter
    def JKS(self, JKS):
        self._JKS = JKS

    @property
    def OTHER(self):
        """Indicates whether other formats can be downloaded.
        :rtype: bool
        """
        return self._OTHER

    @OTHER.setter
    def OTHER(self, OTHER):
        self._OTHER = OTHER

    @property
    def ROOT(self):
        """Indicates whether the root certificate can be downloaded.
        :rtype: bool
        """
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
        """The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BindResourceResult(self):
        """The associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BindResourceResult
        """
        return self._BindResourceResult

    @BindResourceResult.setter
    def BindResourceResult(self, BindResourceResult):
        self._BindResourceResult = BindResourceResult

    @property
    def Status(self):
        """The status of the async task. Valid values: `0` for querying, `1` for successful, and `2` for abnormal. If the status is `1`, the result of `BindResourceResult` will be displayed; if the status is `2`, the error causes will be displayed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Error(self):
        """The error occurred when querying the associated cloud resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Error`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def CacheTime(self):
        """The cache time of the current result.
        :rtype: str
        """
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
        """The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnionStatus(self):
        """The unified domain status.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UnionStatus

    @UnionStatus.setter
    def UnionStatus(self, UnionStatus):
        self._UnionStatus = UnionStatus

    @property
    def IsPreempted(self):
        """Whether the domain is preempted. A preempted domain is one that is already associated with another environment. It must be disassociated or re-associated first.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsPreempted

    @IsPreempted.setter
    def IsPreempted(self, IsPreempted):
        self._IsPreempted = IsPreempted

    @property
    def ICPStatus(self):
        """Whether the domain is added to the ICP blocklist. Valid values: `0` for no and `1` for yes.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ICPStatus

    @ICPStatus.setter
    def ICPStatus(self, ICPStatus):
        self._ICPStatus = ICPStatus

    @property
    def OldCertificateId(self):
        """The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """The list of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TCBAccessInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The instance count.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        """The unique ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Source(self):
        """The source.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        """The name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """The TCB environment.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBEnvironment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AccessService(self):
        """The access service.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBAccessService`
        """
        return self._AccessService

    @AccessService.setter
    def AccessService(self, AccessService):
        self._AccessService = AccessService

    @property
    def HostService(self):
        """Whether static hosting is used.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBHostService`
        """
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
        """The domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """The status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DNSStatus(self):
        """The resolution status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DNSStatus

    @DNSStatus.setter
    def DNSStatus(self, DNSStatus):
        self._DNSStatus = DNSStatus

    @property
    def OldCertificateId(self):
        """The ID of the associated certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """The list of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TCBHostInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The instance count.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._Region = None
        self._Environments = None
        self._Error = None

    @property
    def Region(self):
        """The region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Environments(self):
        """The list of TCB environments.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TCBEnvironments
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = TCBEnvironments()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._Error = params.get("Error")
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
        """Gateway ID
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        """Gateway name
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def CertificateList(self):
        """Gateway certificate list
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of GatewayCertificate
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Region = None
        self._Error = None

    @property
    def InstanceList(self):
        """TSE instance details
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of TSEInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """Total TSE instances in this region	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Region(self):
        """Region	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TSEInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Region = params.get("Region")
        self._Error = params.get("Error")
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
        :param _Status: Domain status.
`Deployed`: deployed;.
`Processing`: deploying;.
`Applying`: applying;.
`Failed`: application failed;.
`Issued`: binding failed.
        :type Status: str
        """
        self._Host = None
        self._CertId = None
        self._ZoneId = None
        self._Status = None

    @property
    def Host(self):
        """The domain.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def CertId(self):
        """The certificate ID.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ZoneId(self):
        """The AZ ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        """Domain status.
`Deployed`: deployed;.
`Processing`: deploying;.
`Applying`: applying;.
`Failed`: application failed;.
`Issued`: binding failed.
        :rtype: str
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def InstanceList(self):
        """The list of EDGEONE instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TeoInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of EDGEONE instances.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
        """The Ingress name.
        :rtype: str
        """
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def TlsDomains(self):
        """The list of TLS domains.
        :rtype: list of str
        """
        return self._TlsDomains

    @TlsDomains.setter
    def TlsDomains(self, TlsDomains):
        self._TlsDomains = TlsDomains

    @property
    def Domains(self):
        """The list of Ingress domains.
        :rtype: list of str
        """
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
        """The cluster ID.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """The cluster name.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NamespaceList(self):
        """The list of cluster namespaces.
        :rtype: list of TkeNameSpaceDetail
        """
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def ClusterType(self):
        """The cluster type.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterVersion(self):
        """The cluster version.
        :rtype: str
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """The region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """The list of TKE instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TkeInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of TKE instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
        """The namespace name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecretList(self):
        """The secret list.
        :rtype: list of TkeSecretDetail
        """
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
        """The secret name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CertId(self):
        """The certificate ID.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def IngressList(self):
        """The Ingress list.
        :rtype: list of TkeIngressDetail
        """
        return self._IngressList

    @IngressList.setter
    def IngressList(self, IngressList):
        self._IngressList = IngressList

    @property
    def NoMatchDomains(self):
        """The list of domains that do not match the new certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
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
        :param _OldCertificateId: The old certificate id for one-click update. by querying the cloud resources bound to this certificate id, and then updating these cloud resources with the new certificate.
        :type OldCertificateId: str
        :param _ResourceTypes: Resource types that need to be deployed, with optional parameter values (lowercase): clb, cdn, waf, live, ddos, teo, apigateway, vod, tke, tcb, tse, cos.
        :type ResourceTypes: list of str
        :param _CertificateId: New certificate id for one-click update. if this parameter is not provided, the public key certificate and private key certificate must be provided.
        :type CertificateId: str
        :param _Regions: List of regions that need to be deployed (deprecated)
        :type Regions: list of str
        :param _ResourceTypesRegions: List of regions where cloud resources need to be deployed. the cloud resource type of the supported region must be passed. valid values: clb, tke, apigateway, waf, tcb, tse, cos.
        :type ResourceTypesRegions: list of ResourceTypeRegions
        :param _CertificatePublicKey: If a public key certificate is uploaded, the private key certificate must also be uploaded, and the CertificateId does not need to be transmitted.
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: If a private key certificate is uploaded, then a public key certificate must be uploaded; CertificateId is not required.
        :type CertificatePrivateKey: str
        :param _ExpiringNotificationSwitch: Whether to ignore expiration reminder for old certificate  0: do not ignore the notification. 1: ignore the notification, ignore the expiration reminder of OldCertificateId.
        :type ExpiringNotificationSwitch: int
        :param _Repeatable: It specifies whether the same certificate is allowed to be uploaded repeatedly. If the public key and private key certificates are selected for upload, this parameter can be configured. If there are duplicate certificates, the update task will fail.
        :type Repeatable: bool
        :param _AllowDownload: Whether to allow downloading. If you choose to upload a public/private key certificate, this parameter can be configured.
        :type AllowDownload: bool
        :param _Tags: Tag list. If you choose to upload a public/private key certificate, you can configure this parameter.
        :type Tags: list of Tags
        :param _ProjectId: Project id. If you choose to upload a public/private key certificate, you can configure this parameter.
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
        """The old certificate id for one-click update. by querying the cloud resources bound to this certificate id, and then updating these cloud resources with the new certificate.
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def ResourceTypes(self):
        """Resource types that need to be deployed, with optional parameter values (lowercase): clb, cdn, waf, live, ddos, teo, apigateway, vod, tke, tcb, tse, cos.
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def CertificateId(self):
        """New certificate id for one-click update. if this parameter is not provided, the public key certificate and private key certificate must be provided.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Regions(self):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        """List of regions that need to be deployed (deprecated)
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        self._Regions = Regions

    @property
    def ResourceTypesRegions(self):
        """List of regions where cloud resources need to be deployed. the cloud resource type of the supported region must be passed. valid values: clb, tke, apigateway, waf, tcb, tse, cos.
        :rtype: list of ResourceTypeRegions
        """
        return self._ResourceTypesRegions

    @ResourceTypesRegions.setter
    def ResourceTypesRegions(self, ResourceTypesRegions):
        self._ResourceTypesRegions = ResourceTypesRegions

    @property
    def CertificatePublicKey(self):
        """If a public key certificate is uploaded, the private key certificate must also be uploaded, and the CertificateId does not need to be transmitted.
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        """If a private key certificate is uploaded, then a public key certificate must be uploaded; CertificateId is not required.
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def ExpiringNotificationSwitch(self):
        """Whether to ignore expiration reminder for old certificate  0: do not ignore the notification. 1: ignore the notification, ignore the expiration reminder of OldCertificateId.
        :rtype: int
        """
        return self._ExpiringNotificationSwitch

    @ExpiringNotificationSwitch.setter
    def ExpiringNotificationSwitch(self, ExpiringNotificationSwitch):
        self._ExpiringNotificationSwitch = ExpiringNotificationSwitch

    @property
    def Repeatable(self):
        """It specifies whether the same certificate is allowed to be uploaded repeatedly. If the public key and private key certificates are selected for upload, this parameter can be configured. If there are duplicate certificates, the update task will fail.
        :rtype: bool
        """
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable

    @property
    def AllowDownload(self):
        """Whether to allow downloading. If you choose to upload a public/private key certificate, this parameter can be configured.
        :rtype: bool
        """
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def Tags(self):
        """Tag list. If you choose to upload a public/private key certificate, you can configure this parameter.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProjectId(self):
        """Project id. If you choose to upload a public/private key certificate, you can configure this parameter.
        :rtype: int
        """
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
        :param _DeployRecordId: Task id, DeployRecordId of 0 indicates that the task is in progress. repeatedly requesting this api, when DeployRecordId returned is greater than 0, it indicates that the task is created successfully. if not created successfully, an exception will be thrown.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployRecordId: int
        :param _DeployStatus: Status of the task; 1 indicates successful creation; 0 indicates that there is a task being updated currently, and no new update task has been created; the returned value DeployRecordId is the task id being updated.
        :type DeployStatus: int
        :param _UpdateSyncProgress: Task Progress Details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateSyncProgress: list of UpdateSyncProgress
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._UpdateSyncProgress = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """Task id, DeployRecordId of 0 indicates that the task is in progress. repeatedly requesting this api, when DeployRecordId returned is greater than 0, it indicates that the task is created successfully. if not created successfully, an exception will be thrown.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        """Status of the task; 1 indicates successful creation; 0 indicates that there is a task being updated currently, and no new update task has been created; the returned value DeployRecordId is the task id being updated.
        :rtype: int
        """
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def UpdateSyncProgress(self):
        """Task Progress Details.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of UpdateSyncProgress
        """
        return self._UpdateSyncProgress

    @UpdateSyncProgress.setter
    def UpdateSyncProgress(self, UpdateSyncProgress):
        self._UpdateSyncProgress = UpdateSyncProgress

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
        :param _DeployRecordId: Record ID for pending retry deployment, which can be obtained through UpdateCertificateInstance. if this parameter is not provided, DeployRecordDetailId must be provided.
        :type DeployRecordId: int
        :param _DeployRecordDetailId: Detail ID for pending retry deployment record, which can be obtained through the DescribeHostUpdateRecordDetail api. if this parameter is not provided, DeployRecordId must be provided.
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        """Record ID for pending retry deployment, which can be obtained through UpdateCertificateInstance. if this parameter is not provided, DeployRecordDetailId must be provided.
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        """Detail ID for pending retry deployment record, which can be obtained through the DescribeHostUpdateRecordDetail api. if this parameter is not provided, DeployRecordId must be provided.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        """To-be-redeployed record ID
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """Rollback deployment record ID
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

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
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class UpdateRecordDetail(AbstractModel):
    """Update record details

    """

    def __init__(self):
        r"""
        :param _Id: Update detail record id.
        :type Id: int
        :param _CertId: New and old certificate update - new certificate id.
        :type CertId: str
        :param _OldCertId: Old and new certificate update - old certificate id.
        :type OldCertId: str
        :param _Domains: Deployment domain name list
Note: This field may return null, indicating that no valid value can be obtained.
        :type Domains: list of str
        :param _ResourceType: Type of cloud resource for updating old and new certs.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :type ResourceType: str
        :param _Region: Deployment region
Note: This field may return null, indicating that no valid value can be obtained.
        :type Region: str
        :param _Status: Deployment status. valid values:.
0: To be deployed.
1: Deployment successful.
2: Deployment failed.
3: Deploying.
4: Rollback succeeded.
5: Rollback failure.
6: No resource, no need for deployment.
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
        :param _Url: Listener url (only for CLB).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
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
        self._Url = None

    @property
    def Id(self):
        """Update detail record id.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """New and old certificate update - new certificate id.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        """Old and new certificate update - old certificate id.
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def Domains(self):
        """Deployment domain name list
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ResourceType(self):
        """Type of cloud resource for updating old and new certs.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        """Deployment region
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """Deployment status. valid values:.
0: To be deployed.
1: Deployment successful.
2: Deployment failed.
3: Deploying.
4: Rollback succeeded.
5: Rollback failure.
6: No resource, no need for deployment.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        """Deployment error message
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        """Deployment time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Last update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InstanceId(self):
        """Deployment instance ID
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Deployment instance name
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        """Deployment listener ID (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """Deployment listener name (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        """Protocol
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SniSwitch(self):
        """Whether SNI is enabled (only for CLB)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        """Bucket name (only for COS)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Port(self):
        """Port
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Namespace(self):
        """Namespace (only for TKE)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        """Secret name (only for TKE)
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnvId(self):
        """Environment ID
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TCBType(self):
        """TCB deployment type
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._TCBType

    @TCBType.setter
    def TCBType(self, TCBType):
        self._TCBType = TCBType

    @property
    def Url(self):
        """Listener url (only for CLB).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


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
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordDetails(AbstractModel):
    """Details of update records.

    """

    def __init__(self):
        r"""
        :param _ResourceType: Type of cloud resource for updating old and new certs.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :type ResourceType: str
        :param _List: The update details of the cloud resource.
        :type List: list of UpdateRecordDetail
        :param _TotalCount: The update of the total number of cloud resources.
        :type TotalCount: int
        """
        self._ResourceType = None
        self._List = None
        self._TotalCount = None

    @property
    def ResourceType(self):
        """Type of cloud resource for updating old and new certs.
- clb.
- cdn.
- ddos.
- live.
- vod.
- waf.
- apigateway.
- teo.
- tke.
- cos.
- tse.
- tcb.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def List(self):
        """The update details of the cloud resource.
        :rtype: list of UpdateRecordDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        """The update of the total number of cloud resources.
        :rtype: int
        """
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
        """Record ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """New certificate ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        """Old certificate ID
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def ResourceTypes(self):
        """Deployment resource type list
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        """Deployment region list
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Status(self):
        """Deployment status
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """Deployment time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Last update time
        :rtype: str
        """
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
    """Update the progress of asynchronous task.

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceType: str
        :param _UpdateSyncProgressRegions: Region result list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateSyncProgressRegions: list of UpdateSyncProgressRegion
        :param _Status: Asynchronous update progress status: 0, pending, 1 processed, 3 processing.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._ResourceType = None
        self._UpdateSyncProgressRegions = None
        self._Status = None

    @property
    def ResourceType(self):
        """Resource type.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def UpdateSyncProgressRegions(self):
        """Region result list.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of UpdateSyncProgressRegion
        """
        return self._UpdateSyncProgressRegions

    @UpdateSyncProgressRegions.setter
    def UpdateSyncProgressRegions(self, UpdateSyncProgressRegions):
        self._UpdateSyncProgressRegions = UpdateSyncProgressRegions

    @property
    def Status(self):
        """Asynchronous update progress status: 0, pending, 1 processed, 3 processing.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
    """Update the progress of asynchronous task.

    """

    def __init__(self):
        r"""
        :param _Region: Resource type.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _TotalCount: Total number
.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _OffsetCount: Quantity of executions completed.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OffsetCount: int
        :param _Status: Asynchronous update progress status: 0, pending, 1 processed, 3 processing.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._Region = None
        self._TotalCount = None
        self._OffsetCount = None
        self._Status = None

    @property
    def Region(self):
        """Resource type.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        """Total number
.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OffsetCount(self):
        """Quantity of executions completed.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OffsetCount

    @OffsetCount.setter
    def OffsetCount(self, OffsetCount):
        self._OffsetCount = OffsetCount

    @property
    def Status(self):
        """Asynchronous update progress status: 0, pending, 1 processed, 3 processing.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        :param _CertificateUse: Certificate Usage/Source, such as CLB, CDN, WAF, LIVE, DDOS.
        :type CertificateUse: str
        :param _Tags: The list of tags.
        :type Tags: list of Tags
        :param _Repeatable: Whether to allow duplicate upload of the same certificate, true: allow uploading certificates with the same fingerprint; false: do not allow uploading certificates with the same fingerprint. default value: true.
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
        """Public key of the certificate
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        """Private key content. This parameter is required when the certificate type is SVR, and not required when the certificate type is CA.
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificateType(self):
        """Certificate type. Valid values: `CA` (CA certificate) and `SVR` (server certificate). Default value: `SVR`
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def Alias(self):
        """Alias
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CertificateUse(self):
        """Certificate Usage/Source, such as CLB, CDN, WAF, LIVE, DDOS.
        :rtype: str
        """
        return self._CertificateUse

    @CertificateUse.setter
    def CertificateUse(self, CertificateUse):
        self._CertificateUse = CertificateUse

    @property
    def Tags(self):
        """The list of tags.
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Repeatable(self):
        """Whether to allow duplicate upload of the same certificate, true: allow uploading certificates with the same fingerprint; false: do not allow uploading certificates with the same fingerprint. default value: true.
        :rtype: bool
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._RepeatCertId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RepeatCertId(self):
        """The ID of the repeatedly uploaded certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RepeatCertId

    @RepeatCertId.setter
    def RepeatCertId(self, RepeatCertId):
        self._RepeatCertId = RepeatCertId

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
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ConfirmLetter(self):
        """Base64-encoded confirmation letter file, which must be a JPG, JPEG, PNG, or PDF file of 1 KB to 1.4 MB
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """Certificate ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        """Whether the operation is successful
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def InstanceList(self):
        """The list of VOD instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of VodInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of VOD instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
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
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """The certificate ID.
        :rtype: str
        """
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
        """The domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """The certificate ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Keepalive(self):
        """Whether to keep the persistent connection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        :param _Error: Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """The region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """The list of WAF instances.	
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of WafInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """The total number of WAF instances in this region.	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """Whether to query exceptions.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = WafInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        