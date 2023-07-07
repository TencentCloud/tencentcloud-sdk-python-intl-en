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
        :param _CsrKeyParameter: Key pair parameter. RSA supports only the 2048-bit key and ECC supports only prime256v1.
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
        """
        self._DomainNumber = None
        self._OriginCertificateId = None
        self._ReplacedBy = None
        self._ReplacedFor = None
        self._RenewOrder = None
        self._SMCert = None

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


    def _deserialize(self, params):
        self._DomainNumber = params.get("DomainNumber")
        self._OriginCertificateId = params.get("OriginCertificateId")
        self._ReplacedBy = params.get("ReplacedBy")
        self._ReplacedFor = params.get("ReplacedFor")
        self._RenewOrder = params.get("RenewOrder")
        self._SMCert = params.get("SMCert")
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
        :param _RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.
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
        """
        self._CertificateId = None
        self._ValidType = None
        self._CsrType = None
        self._CsrContent = None
        self._CsrkeyPassword = None
        self._Reason = None

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


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ValidType = params.get("ValidType")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CsrkeyPassword = params.get("CsrkeyPassword")
        self._Reason = params.get("Reason")
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
        :param _Repeatable: Whether a certificate can be repeatedly uploaded.
        :type Repeatable: bool
        """
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._CertificateType = None
        self._Alias = None
        self._ProjectId = None
        self._CertificateUse = None
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