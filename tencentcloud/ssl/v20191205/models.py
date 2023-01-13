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
        :param DvAuthMethod: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation
        :type DvAuthMethod: str
        :param DomainName: Domain name
        :type DomainName: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param PackageType: Certificate type. Currently, the only supported value is 2, which indicates TrustAsia TLS RSA CA.
        :type PackageType: str
        :param ContactEmail: Email address
        :type ContactEmail: str
        :param ContactPhone: Mobile number
        :type ContactPhone: str
        :param ValidityPeriod: Validity period. The default value is 12 months, which is the only supported value currently.
        :type ValidityPeriod: str
        :param CsrEncryptAlgo: Encryption algorithm. Only RSA is supported.
        :type CsrEncryptAlgo: str
        :param CsrKeyParameter: Key pair parameter. Only the 2048-bit key pair is supported.
        :type CsrKeyParameter: str
        :param CsrKeyPassword: CSR encryption password
        :type CsrKeyPassword: str
        :param Alias: Alias
        :type Alias: str
        :param OldCertificateId: Original certificate ID, which is used to apply for a new certificate.
        :type OldCertificateId: str
        :param PackageId: Benefit package ID, which is used to expand the free certificate package
        :type PackageId: str
        :param DeleteDnsAutoRecord: Whether to delete the automatic domain name verification record after issuance, which is no by default. This parameter can be passed in only for domain names of the DNS_AUTO verification type.
        :type DeleteDnsAutoRecord: bool
        """
        self.DvAuthMethod = None
        self.DomainName = None
        self.ProjectId = None
        self.PackageType = None
        self.ContactEmail = None
        self.ContactPhone = None
        self.ValidityPeriod = None
        self.CsrEncryptAlgo = None
        self.CsrKeyParameter = None
        self.CsrKeyPassword = None
        self.Alias = None
        self.OldCertificateId = None
        self.PackageId = None
        self.DeleteDnsAutoRecord = None


    def _deserialize(self, params):
        self.DvAuthMethod = params.get("DvAuthMethod")
        self.DomainName = params.get("DomainName")
        self.ProjectId = params.get("ProjectId")
        self.PackageType = params.get("PackageType")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPhone = params.get("ContactPhone")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self.CsrKeyParameter = params.get("CsrKeyParameter")
        self.CsrKeyPassword = params.get("CsrKeyPassword")
        self.Alias = params.get("Alias")
        self.OldCertificateId = params.get("OldCertificateId")
        self.PackageId = params.get("PackageId")
        self.DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: ID of the certificate whose order has been successfully cancelled
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CertificateExtra(AbstractModel):
    """Content of the `CertificateExtra` parameter. `CertificateExtra` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        r"""
        :param DomainNumber: Number of domain names which can be associated with the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainNumber: str
        :param OriginCertificateId: Original certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginCertificateId: str
        :param ReplacedBy: Original ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedBy: str
        :param ReplacedFor: New ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReplacedFor: str
        :param RenewOrder: Certificate ID of the new order
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewOrder: str
        """
        self.DomainNumber = None
        self.OriginCertificateId = None
        self.ReplacedBy = None
        self.ReplacedFor = None
        self.RenewOrder = None


    def _deserialize(self, params):
        self.DomainNumber = params.get("DomainNumber")
        self.OriginCertificateId = params.get("OriginCertificateId")
        self.ReplacedBy = params.get("ReplacedBy")
        self.ReplacedFor = params.get("ReplacedFor")
        self.RenewOrder = params.get("RenewOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificates(AbstractModel):
    """Content of the `Certificates` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param From: Certificate source
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param Domain: Primary domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Status: Status. `0`: Reviewing; `1`: Approved; `2`: Unapproved; `3`: Expired; `4`: DNS record added for domain names of the DNS_AUTO verification type; `5`: Enterprise-grade certificate, pending submission; `6`: Canceling order; `7`: Canceled; `8`: Information submitted, pending confirmation letter upload; `9`: Revoking certificate; `10`: Revoked; `11`: Reissuing; `12`: Pending revocation confirmation letter upload; `13`: Pending information submission for the free certificate; `14`: Refunded.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param VulnerabilityStatus: Vulnerability scanning status. `INACTIVE`: not activated; `ACTIVE`: activated
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageTypeName: str
        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewAble: bool
        :param ProjectInfo: Project information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param BoundResource: Associated Tencent Cloud services. Currently, this parameter is unavailable.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BoundResource: list of str
        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param IsIgnore: Whether the expiration notification was ignored
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsIgnore: bool
        :param IsSM: Whether the certificate is a Chinese SM certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSM: bool
        :param EncryptAlgorithm: Certificate algorithm
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgorithm: str
        :param CAEncryptAlgorithms: Encryption algorithm of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEncryptAlgorithms: list of str
        :param CAEndTimes: Expiration time of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CAEndTimes: list of str
        :param CACommonNames: Generic name of the uploaded CA certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CACommonNames: list of str
        :param PreAuditInfo: Prereview information of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param AutoRenewFlag: Whether auto-renewal is enabled.
Note: This field may return null, indicating that no valid value can be obtained.
        :type AutoRenewFlag: int
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.PackageType = None
        self.CertificateType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.CertificateExtra = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.CertificateId = None
        self.SubjectAltName = None
        self.PackageTypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.ProjectInfo = None
        self.BoundResource = None
        self.Deployable = None
        self.Tags = None
        self.IsIgnore = None
        self.IsSM = None
        self.EncryptAlgorithm = None
        self.CAEncryptAlgorithms = None
        self.CAEndTimes = None
        self.CACommonNames = None
        self.PreAuditInfo = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.PackageType = params.get("PackageType")
        self.CertificateType = params.get("CertificateType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.CertificateId = params.get("CertificateId")
        self.SubjectAltName = params.get("SubjectAltName")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = ProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.BoundResource = params.get("BoundResource")
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.IsIgnore = params.get("IsIgnore")
        self.IsSM = params.get("IsSM")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self.CAEndTimes = params.get("CAEndTimes")
        self.CACommonNames = params.get("CACommonNames")
        if params.get("PreAuditInfo") is not None:
            self.PreAuditInfo = PreAuditInfo()
            self.PreAuditInfo._deserialize(params.get("PreAuditInfo"))
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation response structure.

    """

    def __init__(self):
        r"""
        :param OrderId: TrustAsia order ID
        :type OrderId: str
        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OrderId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate response structure.

    """

    def __init__(self):
        r"""
        :param DeleteResult: Deletion result
        :type DeleteResult: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail response structure.

    """

    def __init__(self):
        r"""
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param CertificatePrivateKey: Private key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePrivateKey: str
        :param CertificatePublicKey: Public key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificatePublicKey: str
        :param DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityReport: str
        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param TypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeName: str
        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param SubjectAltName: Multiple domain names included in the certificate (excluding the primary domain name, which uses the `Domain` field)
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param IsVip: Whether the certificate is a paid one.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param RenewAble: Whether the certificate can be renewed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewAble: bool
        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param Tags: List of associated tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param RootCert: Root certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootCert: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        :param EncryptCert: Chinese SM encryption certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptCert: str
        :param EncryptPrivateKey: Private key of Chinese SM encryption
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptPrivateKey: str
        :param CertFingerprint: SHA1 fingerprint of the signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertFingerprint: str
        :param EncryptCertFingerprint: SHA1 fingerprint of the encryption certificate (for Chinese SM certificates only)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptCertFingerprint: str
        :param EncryptAlgorithm: Certificate algorithm
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptAlgorithm: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.CertificatePrivateKey = None
        self.CertificatePublicKey = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.TypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.SubmittedData = None
        self.RenewAble = None
        self.Deployable = None
        self.Tags = None
        self.RootCert = None
        self.EncryptCert = None
        self.EncryptPrivateKey = None
        self.CertFingerprint = None
        self.EncryptCertFingerprint = None
        self.EncryptAlgorithm = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.RenewAble = params.get("RenewAble")
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("RootCert") is not None:
            self.RootCert = RootCertificates()
            self.RootCert._deserialize(params.get("RootCert"))
        self.EncryptCert = params.get("EncryptCert")
        self.EncryptPrivateKey = params.get("EncryptPrivateKey")
        self.CertFingerprint = params.get("CertFingerprint")
        self.EncryptCertFingerprint = params.get("EncryptCertFingerprint")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset. The default value is 0.
        :type Offset: int
        :param Limit: Number of requested logs. The default value is 20.
        :type Limit: int
        :param StartTime: Start time. The default value is 15 days ago.
        :type StartTime: str
        :param EndTime: End time. The default value is the current time.
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs response structure.

    """

    def __init__(self):
        r"""
        :param AllTotal: Total number of logs that meet query conditions
        :type AllTotal: int
        :param TotalCount: Number of logs returned for this request
        :type TotalCount: int
        :param OperateLogs: Certificate operation log list
Note: this field may return null, indicating that no valid values can be obtained.
        :type OperateLogs: list of OperationLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllTotal = None
        self.TotalCount = None
        self.OperateLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self.OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self.OperateLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate response structure.

    """

    def __init__(self):
        r"""
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: str
        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.
        :type From: str
        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateType: str
        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageType: str
        :param ProductZhName: Name of the certificate issuer
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductZhName: str
        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusMsg: str
        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        :param VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityStatus: str
        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertBeginTime: str
        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertEndTime: str
        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidityPeriod: str
        :param InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderId: str
        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.
        :type VulnerabilityReport: str
        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateId: str
        :param PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PackageTypeName: str
        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusName: str
        :param SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWildcard: bool
        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDv: bool
        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsVulnerability: bool
        :param RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.
        :type RenewAble: bool
        :param SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deployable: bool
        :param Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tags
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.PackageTypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.SubmittedData = None
        self.Deployable = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination offset, starting from 0
        :type Offset: int
        :param Limit: Number of entries per page. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param SearchKey: Keyword for search, which can be a certificate ID, alias, or domain name, for example, a8xHcaIs
        :type SearchKey: str
        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
        :type CertificateType: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ExpirationSort: Sorting by expiration time. `DESC`: descending; `ASC`: ascending
        :type ExpirationSort: str
        :param CertificateStatus: Certificate status. `0`: Reviewing; `1`: Approved; `2`: Unapproved; `3`: Expired; `4`: DNS record added; `5`: Enterprise-grade certificate, pending submission; `6`: Canceling order; `7`: Canceled; `8`: Information submitted, pending confirmation letter upload; `9`: Revoking certificate; `10`: Revoked; `11`: Reissuing; `12`: Pending revocation confirmation letter upload; `13`: Pending information submission for the free certificate.
        :type CertificateStatus: list of int non-negative
        :param Deployable: Whether the certificate can be deployed. `1`: yes; `0`: no
        :type Deployable: int
        :param Upload: Whether to filter uploaded hosted certificates. `1`: Yes; `0`: No.
        :type Upload: int
        :param Renew: Whether to filter renewable certificates. `1`: Yes; `0`: No.
        :type Renew: int
        :param FilterSource: Filter by source. `upload`: Uploaded certificate; `buy`: Tencent Cloud certificate. If this parameter is left empty, all certificates will be queried.
        :type FilterSource: str
        :param IsSM: Whether to filter Chinese SM certificates. `1`: Yes; `0`: No.
        :type IsSM: int
        :param FilterExpiring: Whether to filter expiring certificates. `1`: Yes; `0`: No.
        :type FilterExpiring: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertificateType = None
        self.ProjectId = None
        self.ExpirationSort = None
        self.CertificateStatus = None
        self.Deployable = None
        self.Upload = None
        self.Renew = None
        self.FilterSource = None
        self.IsSM = None
        self.FilterExpiring = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertificateType = params.get("CertificateType")
        self.ProjectId = params.get("ProjectId")
        self.ExpirationSort = params.get("ExpirationSort")
        self.CertificateStatus = params.get("CertificateStatus")
        self.Deployable = params.get("Deployable")
        self.Upload = params.get("Upload")
        self.Renew = params.get("Renew")
        self.FilterSource = params.get("FilterSource")
        self.IsSM = params.get("IsSM")
        self.FilterExpiring = params.get("FilterExpiring")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Certificates: List
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificates: list of Certificates
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Certificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self.Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self.Certificates.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate response structure.

    """

    def __init__(self):
        r"""
        :param Content: ZIP content encoded by using Base64. After the content is decoded by using Base64, it can be saved as a ZIP file.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param ContentType: MIME type. `application/zip`: ZIP file
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContentType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Content = None
        self.ContentType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ContentType = params.get("ContentType")
        self.RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """Content of the `DvAuthDetail` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param DvAuthKeySubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKeySubDomain: str
        :param DvAuths: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuths: list of DvAuths
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthKeySubDomain = None
        self.DvAuths = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self.DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self.DvAuths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DvAuths(AbstractModel):
    """Content of the `DvAuths` parameter

    """

    def __init__(self):
        r"""
        :param DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthKey: str
        :param DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthValue: str
        :param DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthDomain: str
        :param DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthPath: str
        :param DvAuthSubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthSubDomain: str
        :param DvAuthVerifyType: DV authentication type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DvAuthVerifyType: str
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthSubDomain = None
        self.DvAuthVerifyType = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthSubDomain = params.get("DvAuthSubDomain")
        self.DvAuthVerifyType = params.get("DvAuthVerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param Alias: Alias
        :type Alias: str
        """
        self.CertificateId = None
        self.Alias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: ID of the successfully modified certificate
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject request structure.

    """

    def __init__(self):
        r"""
        :param CertificateIdList: ID list of certificates whose projects need to be modified. A maximum of 100 certificate IDs are supported.
        :type CertificateIdList: list of str
        :param ProjectId: Project ID
        :type ProjectId: int
        """
        self.CertificateIdList = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificateIdList = params.get("CertificateIdList")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject response structure.

    """

    def __init__(self):
        r"""
        :param SuccessCertificates: List of certificates whose projects were modified successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :type SuccessCertificates: list of str
        :param FailCertificates: List of certificates whose projects failed to be modified
Note: this field may return null, indicating that no valid values can be obtained.
        :type FailCertificates: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SuccessCertificates = None
        self.FailCertificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCertificates = params.get("SuccessCertificates")
        self.FailCertificates = params.get("FailCertificates")
        self.RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """Certificate operation logs

    """

    def __init__(self):
        r"""
        :param Action: Action performed on logs
        :type Action: str
        :param CreatedOn: Time when the action is performed
        :type CreatedOn: str
        """
        self.Action = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreAuditInfo(AbstractModel):
    """List of prereview information

    """

    def __init__(self):
        r"""
        :param TotalPeriod: Total number of years of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPeriod: int
        :param NowPeriod: Current year of the certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type NowPeriod: int
        :param ManagerId: Certificate prereview manager ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManagerId: str
        """
        self.TotalPeriod = None
        self.NowPeriod = None
        self.ManagerId = None


    def _deserialize(self, params):
        self.TotalPeriod = params.get("TotalPeriod")
        self.NowPeriod = params.get("NowPeriod")
        self.ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """Content of the `ProjectInfo` parameter. `ProjectInfo` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        r"""
        :param ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param ProjectCreatorUin: UIN of the project creator
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectCreatorUin: int
        :param ProjectCreateTime: Project creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectCreateTime: str
        :param ProjectResume: Brief project information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectResume: str
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type OwnerUin: int
        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        """
        self.ProjectName = None
        self.ProjectCreatorUin = None
        self.ProjectCreateTime = None
        self.ProjectResume = None
        self.OwnerUin = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectCreatorUin = params.get("ProjectCreatorUin")
        self.ProjectCreateTime = params.get("ProjectCreateTime")
        self.ProjectResume = params.get("ProjectResume")
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param ValidType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation
        :type ValidType: str
        :param CsrType: Type. `original`: original certificate CSR; `upload`: uploaded manually; `online`: generated online. The default value is original.
        :type CsrType: str
        :param CsrContent: CSR content
        :type CsrContent: str
        :param CsrkeyPassword: Password of the key
        :type CsrkeyPassword: str
        :param Reason: Reissue reason
        :type Reason: str
        """
        self.CertificateId = None
        self.ValidType = None
        self.CsrType = None
        self.CsrContent = None
        self.CsrkeyPassword = None
        self.Reason = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ValidType = params.get("ValidType")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CsrkeyPassword = params.get("CsrkeyPassword")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class RootCertificates(AbstractModel):
    """Root certificate

    """

    def __init__(self):
        r"""
        :param Sign: Chinese SM signature certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Sign: str
        :param Encrypt: Chinese SM encryption certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Encrypt: str
        :param Standard: Standard certificate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Standard: str
        """
        self.Sign = None
        self.Encrypt = None
        self.Standard = None


    def _deserialize(self, params):
        self.Sign = params.get("Sign")
        self.Encrypt = params.get("Encrypt")
        self.Standard = params.get("Standard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation request structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param CsrType: CSR generation mode. `online`: generated online; `parse`: uploaded manually
        :type CsrType: str
        :param CsrContent: Uploaded CSR content
        :type CsrContent: str
        :param CertificateDomain: Domain name bound with the certificate
        :type CertificateDomain: str
        :param DomainList: Uploaded domain name array (can be uploaded for a multi-domain certificate)
        :type DomainList: list of str
        :param KeyPassword: Password of the private key
        :type KeyPassword: str
        :param OrganizationName: Organization name
        :type OrganizationName: str
        :param OrganizationDivision: Division name
        :type OrganizationDivision: str
        :param OrganizationAddress: Detailed address of the organization
        :type OrganizationAddress: str
        :param OrganizationCountry: Country where the organization is located, for example, CN (China)
        :type OrganizationCountry: str
        :param OrganizationCity: City where the organization is located
        :type OrganizationCity: str
        :param OrganizationRegion: Province where the organization is located
        :type OrganizationRegion: str
        :param PostalCode: Postal code of the organization
        :type PostalCode: str
        :param PhoneAreaCode: Area code of the fixed-line phone number of the organization
        :type PhoneAreaCode: str
        :param PhoneNumber: Fixed-line phone number of the organization
        :type PhoneNumber: str
        :param VerifyType: Certificate validation method
        :type VerifyType: str
        :param AdminFirstName: Last name of the administrator
        :type AdminFirstName: str
        :param AdminLastName: First name of the administrator
        :type AdminLastName: str
        :param AdminPhoneNum: Mobile number of the administrator
        :type AdminPhoneNum: str
        :param AdminEmail: Email of the administrator
        :type AdminEmail: str
        :param AdminPosition: Position of the administrator
        :type AdminPosition: str
        :param ContactFirstName: Last name of the contact
        :type ContactFirstName: str
        :param ContactLastName: First name of the contact
        :type ContactLastName: str
        :param ContactEmail: Email of the contact
        :type ContactEmail: str
        :param ContactNumber: Mobile number of the contact
        :type ContactNumber: str
        :param ContactPosition: Position of the contact
        :type ContactPosition: str
        """
        self.CertificateId = None
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.VerifyType = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactEmail = None
        self.ContactNumber = None
        self.ContactPosition = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.VerifyType = params.get("VerifyType")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactPosition = params.get("ContactPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """Content of the `SubmittedData` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        r"""
        :param CsrType: CSR type. `online`: CSR generated online; `parse`: CSR pasted
Note: this field may return null, indicating that no valid values can be obtained.
        :type CsrType: str
        :param CsrContent: CSR content
Note: this field may return null, indicating that no valid values can be obtained.
        :type CsrContent: str
        :param CertificateDomain: Domain name information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertificateDomain: str
        :param DomainList: DNS information
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainList: list of str
        :param KeyPassword: Password of the private key
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyPassword: str
        :param OrganizationName: Enterprise or unit name
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationName: str
        :param OrganizationDivision: Division
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationDivision: str
        :param OrganizationAddress: Address
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationAddress: str
        :param OrganizationCountry: Country
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationCountry: str
        :param OrganizationCity: City
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationCity: str
        :param OrganizationRegion: Province
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrganizationRegion: str
        :param PostalCode: Postal code
Note: this field may return null, indicating that no valid values can be obtained.
        :type PostalCode: str
        :param PhoneAreaCode: Area code of the fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneAreaCode: str
        :param PhoneNumber: Fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneNumber: str
        :param AdminFirstName: First name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminFirstName: str
        :param AdminLastName: Last name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminLastName: str
        :param AdminPhoneNum: Phone number of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminPhoneNum: str
        :param AdminEmail: Email of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminEmail: str
        :param AdminPosition: Position of the administrator
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdminPosition: str
        :param ContactFirstName: First name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactFirstName: str
        :param ContactLastName: Last name of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactLastName: str
        :param ContactNumber: Phone number of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactNumber: str
        :param ContactEmail: Email of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactEmail: str
        :param ContactPosition: Position of the contact
Note: this field may return null, indicating that no valid values can be obtained.
        :type ContactPosition: str
        :param VerifyType: Validation type
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyType: str
        """
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactNumber = None
        self.ContactEmail = None
        self.ContactPosition = None
        self.VerifyType = None


    def _deserialize(self, params):
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPosition = params.get("ContactPosition")
        self.VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """Tag

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
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate request structure.

    """

    def __init__(self):
        r"""
        :param CertificatePublicKey: Public key of the certificate
        :type CertificatePublicKey: str
        :param CertificatePrivateKey: Private key content. This parameter is required when the certificate type is SVR, and not required when the certificate type is CA.
        :type CertificatePrivateKey: str
        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate. The default value is SVR.
        :type CertificateType: str
        :param Alias: Alias
        :type Alias: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CertificateUse: 
        :type CertificateUse: str
        """
        self.CertificatePublicKey = None
        self.CertificatePrivateKey = None
        self.CertificateType = None
        self.Alias = None
        self.ProjectId = None
        self.CertificateUse = None


    def _deserialize(self, params):
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificateType = params.get("CertificateType")
        self.Alias = params.get("Alias")
        self.ProjectId = params.get("ProjectId")
        self.CertificateUse = params.get("CertificateUse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate response structure.

    """

    def __init__(self):
        r"""
        :param CertificateId: Certificate ID
        :type CertificateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")