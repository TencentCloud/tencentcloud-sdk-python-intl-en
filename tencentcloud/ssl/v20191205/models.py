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
        """
        :param DvAuthMethod: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation\n        :type DvAuthMethod: str\n        :param DomainName: Domain name\n        :type DomainName: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param PackageType: Certificate type. Currently, the only supported value is 2, which indicates TrustAsia TLS RSA CA.\n        :type PackageType: str\n        :param ContactEmail: Email address\n        :type ContactEmail: str\n        :param ContactPhone: Mobile number\n        :type ContactPhone: str\n        :param ValidityPeriod: Validity period. The default value is 12 months, which is the only supported value currently.\n        :type ValidityPeriod: str\n        :param CsrEncryptAlgo: Encryption algorithm. Only RSA is supported.\n        :type CsrEncryptAlgo: str\n        :param CsrKeyParameter: Key pair parameter. Only the 2048-bit key pair is supported.\n        :type CsrKeyParameter: str\n        :param CsrKeyPassword: CSR encryption password\n        :type CsrKeyPassword: str\n        :param Alias: Alias\n        :type Alias: str\n        :param OldCertificateId: Original certificate ID, which is used to apply for a new certificate.\n        :type OldCertificateId: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder request structure.

    """

    def __init__(self):
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param CertificateId: ID of the certificate whose order has been successfully cancelled\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CertificateExtra(AbstractModel):
    """Content of the `CertificateExtra` parameter. `CertificateExtra` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        """
        :param DomainNumber: Number of domain names which can be associated with the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomainNumber: str\n        :param OriginCertificateId: Original certificate ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginCertificateId: str\n        :param ReplacedBy: Original ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReplacedBy: str\n        :param ReplacedFor: New ID of the new certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReplacedFor: str\n        :param RenewOrder: Certificate ID of the new order
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RenewOrder: str\n        """
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
        """
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OwnerUin: str\n        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: str\n        :param From: Certificate source
Note: this field may return null, indicating that no valid values can be obtained.\n        :type From: str\n        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PackageType: str\n        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateType: str\n        :param ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductZhName: str\n        :param Domain: Primary domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Alias: str\n        :param Status: Status value. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: OV/EV certificate, information to be submitted; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param VulnerabilityStatus: Vulnerability scanning status. `INACTIVE`: not activated; `ACTIVE`: activated
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VulnerabilityStatus: str\n        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusMsg: str\n        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VerifyType: str\n        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertBeginTime: str\n        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertEndTime: str\n        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValidityPeriod: str\n        :param InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InsertTime: str\n        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateId: str\n        :param SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubjectAltName: list of str\n        :param PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PackageTypeName: str\n        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusName: str\n        :param IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVip: bool\n        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDv: bool\n        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsWildcard: bool\n        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVulnerability: bool\n        :param RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RenewAble: bool\n        :param ProjectInfo: Project information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`\n        :param BoundResource: Associated Tencent Cloud services. Currently, this parameter is unavailable.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BoundResource: list of str\n        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deployable: bool\n        :param Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tags: list of Tags\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param OrderId: TrustAsia order ID\n        :type OrderId: str\n        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param DeleteResult: Deletion result\n        :type DeleteResult: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail request structure.

    """

    def __init__(self):
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OwnerUin: str\n        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: str\n        :param From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.\n        :type From: str\n        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateType: str\n        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PackageType: str\n        :param ProductZhName: Issuer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductZhName: str\n        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Alias: str\n        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusMsg: str\n        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VerifyType: str\n        :param VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VulnerabilityStatus: str\n        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertBeginTime: str\n        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertEndTime: str\n        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValidityPeriod: str\n        :param InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InsertTime: str\n        :param OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrderId: str\n        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param CertificatePrivateKey: Private key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificatePrivateKey: str\n        :param CertificatePublicKey: Public key of the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificatePublicKey: str\n        :param DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`\n        :param VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VulnerabilityReport: str\n        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateId: str\n        :param TypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TypeName: str\n        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusName: str\n        :param SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubjectAltName: list of str\n        :param IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVip: bool\n        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsWildcard: bool\n        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDv: bool\n        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVulnerability: bool\n        :param SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`\n        :param RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RenewAble: bool\n        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deployable: bool\n        :param Tags: List of associated tags
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tags: list of Tags\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset. The default value is 0.\n        :type Offset: int\n        :param Limit: Number of requested logs. The default value is 20.\n        :type Limit: int\n        :param StartTime: Start time. The default value is 15 days ago.\n        :type StartTime: str\n        :param EndTime: End time. The default value is the current time.\n        :type EndTime: str\n        """
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
        """
        :param AllTotal: Total number of logs that meet query conditions\n        :type AllTotal: int\n        :param TotalCount: Number of logs returned for this request\n        :type TotalCount: int\n        :param OperateLogs: Certificate operation log list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OperateLogs: list of OperationLog\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OwnerUin: str\n        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: str\n        :param From: Certificate source. `trustasia`: TrustAsia; `upload`: certificate uploaded by users
Note: this field may return null, indicating that no valid values can be obtained.\n        :type From: str\n        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateType: str\n        :param PackageType: Certificate plan type. `1`: GeoTrust DV SSL CA - G3; `2`: TrustAsia TLS RSA CA; `3`: SecureSite EV Pro; `4`: SecureSite EV; `5`: SecureSite OV Pro; `6`: SecureSite OV; `7`: SecureSite OV wildcard; `8`: GeoTrust EV; `9`: GeoTrust OV; `10`: GeoTrust OV wildcard; `11`: TrustAsia DV multi-domain; `12`: TrustAsia DV wildcard; `13`: TrustAsia OV wildcard D3; `14`: TrustAsia OV D3; `15`: TrustAsia OV multi-domain D3; `16`: TrustAsia EV D3; `17`: TrustAsia EV multi-domain D3; `18`: GlobalSign OV; `19`: GlobalSign OV wildcard; `20`: GlobalSign EV; `21`: TrustAsia OV wildcard multi-domain D3; `22`: GlobalSign OV multi-domain; `23`: GlobalSign OV wildcard multi-domain; `24`: GlobalSign EV multi-domain
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PackageType: str\n        :param ProductZhName: Name of the certificate issuer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductZhName: str\n        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param Alias: Alias
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Alias: str\n        :param Status: Certificate status. `0`: reviewing; `1`: approved; `2`: unapproved; `3`: expired; `4`: DNS record added; `5`: enterprise-grade certificate, pending submission; `6`: canceling order; `7`: canceled; `8`: information submitted, pending confirmation letter upload; `9`: revoking certificate; `10`: revoked; `11`: reissuing; `12`: pending revocation confirmation letter upload
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param StatusMsg: Status information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusMsg: str\n        :param VerifyType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation; `EMAIL`: email validation
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VerifyType: str\n        :param VulnerabilityStatus: Vulnerability scanning status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VulnerabilityStatus: str\n        :param CertBeginTime: Time when the certificate takes effect
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertBeginTime: str\n        :param CertEndTime: Time when the certificate expires
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertEndTime: str\n        :param ValidityPeriod: Validity period of the certificate, in months
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValidityPeriod: str\n        :param InsertTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InsertTime: str\n        :param OrderId: Order ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrderId: str\n        :param CertificateExtra: Extended information of the certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param DvAuthDetail: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`\n        :param VulnerabilityReport: Vulnerability scanning assessment report
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VulnerabilityReport: str\n        :param CertificateId: Certificate ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateId: str\n        :param PackageTypeName: Certificate type name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PackageTypeName: str\n        :param StatusName: Status description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusName: str\n        :param SubjectAltName: Domain names associated with the certificate (including the primary domain name)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubjectAltName: list of str\n        :param IsVip: Whether the customer is a VIP customer
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVip: bool\n        :param IsWildcard: Whether the certificate is a wildcard certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsWildcard: bool\n        :param IsDv: Whether the certificate is a DV certificate
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDv: bool\n        :param IsVulnerability: Whether the vulnerability scanning feature is enabled
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsVulnerability: bool\n        :param RenewAble: Whether the certificate can be reissued
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RenewAble: bool\n        :param SubmittedData: Submitted data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`\n        :param Deployable: Whether the certificate can be deployed
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Deployable: bool\n        :param Tags: List of tags
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Tags: list of Tags\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Offset: Pagination offset, starting from 0\n        :type Offset: int\n        :param Limit: Number of certificates on each page. The default value is 20.\n        :type Limit: int\n        :param SearchKey: Keyword for search, which can be a certificate ID, alias, or domain name, for example, a8xHcaIs\n        :type SearchKey: str\n        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate\n        :type CertificateType: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param ExpirationSort: Sorting by expiration time. `DESC`: descending; `ASC`: ascending\n        :type ExpirationSort: str\n        :param CertificateStatus: Certificate status\n        :type CertificateStatus: list of int non-negative\n        :param Deployable: Whether the certificate can be deployed. `1`: yes; `0`: no\n        :type Deployable: int\n        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertificateType = None
        self.ProjectId = None
        self.ExpirationSort = None
        self.CertificateStatus = None
        self.Deployable = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertificateType = params.get("CertificateType")
        self.ProjectId = params.get("ProjectId")
        self.ExpirationSort = params.get("ExpirationSort")
        self.CertificateStatus = params.get("CertificateStatus")
        self.Deployable = params.get("Deployable")
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
        """
        :param TotalCount: Total number
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param Certificates: List
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Certificates: list of Certificates\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        """
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
        """
        :param Content: ZIP content encoded by using Base64. After the content is decoded by using Base64, it can be saved as a ZIP file.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Content: str\n        :param ContentType: MIME type. `application/zip`: ZIP file
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContentType: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthKey: str\n        :param DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthValue: str\n        :param DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthDomain: str\n        :param DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthPath: str\n        :param DvAuthKeySubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthKeySubDomain: str\n        :param DvAuths: DV authentication information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuths: list of DvAuths\n        """
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
        """
        :param DvAuthKey: DV authentication key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthKey: str\n        :param DvAuthValue: DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthValue: str\n        :param DvAuthDomain: Domain name of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthDomain: str\n        :param DvAuthPath: Path of the DV authentication value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthPath: str\n        :param DvAuthSubDomain: DV authentication sub-domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthSubDomain: str\n        :param DvAuthVerifyType: DV authentication type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DvAuthVerifyType: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param Alias: Alias\n        :type Alias: str\n        """
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
        """
        :param CertificateId: ID of the successfully modified certificate\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject request structure.

    """

    def __init__(self):
        """
        :param CertificateIdList: ID list of certificates whose projects need to be modified. A maximum of 100 certificate IDs are supported.\n        :type CertificateIdList: list of str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        """
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
        """
        :param SuccessCertificates: List of certificates whose projects were modified successfully
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SuccessCertificates: list of str\n        :param FailCertificates: List of certificates whose projects failed to be modified
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FailCertificates: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Action: Action performed on logs\n        :type Action: str\n        :param CreatedOn: Time when the action is performed\n        :type CreatedOn: str\n        """
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
        


class ProjectInfo(AbstractModel):
    """Content of the `ProjectInfo` parameter. `ProjectInfo` is an element of `Certificates` array which is returned by `DescribeCertificates`.

    """

    def __init__(self):
        """
        :param ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectName: str\n        :param ProjectCreatorUin: UIN of the project creator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectCreatorUin: int\n        :param ProjectCreateTime: Project creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectCreateTime: str\n        :param ProjectResume: Brief project information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectResume: str\n        :param OwnerUin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OwnerUin: int\n        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param ValidType: Validation type. `DNS_AUTO`: automatic DNS validation; `DNS`: manual DNS validation; `FILE`: file validation\n        :type ValidType: str\n        :param CsrType: Type. `original`: original certificate CSR; `upload`: uploaded manually; `online`: generated online. The default value is original.\n        :type CsrType: str\n        :param CsrContent: CSR content\n        :type CsrContent: str\n        :param CsrkeyPassword: Password of the key\n        :type CsrkeyPassword: str\n        :param Reason: Reissue reason\n        :type Reason: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation request structure.

    """

    def __init__(self):
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param CsrType: CSR generation mode. `online`: generated online; `parse`: uploaded manually\n        :type CsrType: str\n        :param CsrContent: Uploaded CSR content\n        :type CsrContent: str\n        :param CertificateDomain: Domain name bound with the certificate\n        :type CertificateDomain: str\n        :param DomainList: Uploaded domain name array (can be uploaded for a multi-domain certificate)\n        :type DomainList: list of str\n        :param KeyPassword: Password of the private key\n        :type KeyPassword: str\n        :param OrganizationName: Organization name\n        :type OrganizationName: str\n        :param OrganizationDivision: Division name\n        :type OrganizationDivision: str\n        :param OrganizationAddress: Detailed address of the organization\n        :type OrganizationAddress: str\n        :param OrganizationCountry: Country where the organization is located, for example, CN (China)\n        :type OrganizationCountry: str\n        :param OrganizationCity: City where the organization is located\n        :type OrganizationCity: str\n        :param OrganizationRegion: Province where the organization is located\n        :type OrganizationRegion: str\n        :param PostalCode: Postal code of the organization\n        :type PostalCode: str\n        :param PhoneAreaCode: Area code of the fixed-line phone number of the organization\n        :type PhoneAreaCode: str\n        :param PhoneNumber: Fixed-line phone number of the organization\n        :type PhoneNumber: str\n        :param VerifyType: Certificate validation method\n        :type VerifyType: str\n        :param AdminFirstName: Last name of the administrator\n        :type AdminFirstName: str\n        :param AdminLastName: First name of the administrator\n        :type AdminLastName: str\n        :param AdminPhoneNum: Mobile number of the administrator\n        :type AdminPhoneNum: str\n        :param AdminEmail: Email of the administrator\n        :type AdminEmail: str\n        :param AdminPosition: Position of the administrator\n        :type AdminPosition: str\n        :param ContactFirstName: Last name of the contact\n        :type ContactFirstName: str\n        :param ContactLastName: First name of the contact\n        :type ContactLastName: str\n        :param ContactEmail: Email of the contact\n        :type ContactEmail: str\n        :param ContactNumber: Mobile number of the contact\n        :type ContactNumber: str\n        :param ContactPosition: Position of the contact\n        :type ContactPosition: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """Content of the `SubmittedData` parameter returned by `DescribeCertificates`

    """

    def __init__(self):
        """
        :param CsrType: CSR type. `online`: CSR generated online; `parse`: CSR pasted
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CsrType: str\n        :param CsrContent: CSR content
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CsrContent: str\n        :param CertificateDomain: Domain name information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertificateDomain: str\n        :param DomainList: DNS information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomainList: list of str\n        :param KeyPassword: Password of the private key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyPassword: str\n        :param OrganizationName: Enterprise or unit name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationName: str\n        :param OrganizationDivision: Division
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationDivision: str\n        :param OrganizationAddress: Address
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationAddress: str\n        :param OrganizationCountry: Country
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationCountry: str\n        :param OrganizationCity: City
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationCity: str\n        :param OrganizationRegion: Province
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrganizationRegion: str\n        :param PostalCode: Postal code
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PostalCode: str\n        :param PhoneAreaCode: Area code of the fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneAreaCode: str\n        :param PhoneNumber: Fixed-line phone number
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneNumber: str\n        :param AdminFirstName: First name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdminFirstName: str\n        :param AdminLastName: Last name of the administrator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdminLastName: str\n        :param AdminPhoneNum: Phone number of the administrator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdminPhoneNum: str\n        :param AdminEmail: Email of the administrator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdminEmail: str\n        :param AdminPosition: Position of the administrator
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AdminPosition: str\n        :param ContactFirstName: First name of the contact
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContactFirstName: str\n        :param ContactLastName: Last name of the contact
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContactLastName: str\n        :param ContactNumber: Phone number of the contact
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContactNumber: str\n        :param ContactEmail: Email of the contact
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContactEmail: str\n        :param ContactPosition: Position of the contact
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ContactPosition: str\n        :param VerifyType: Validation type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VerifyType: str\n        """
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
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate request structure.

    """

    def __init__(self):
        """
        :param CertificatePublicKey: Public key of the certificate\n        :type CertificatePublicKey: str\n        :param CertificatePrivateKey: Private key content. This parameter is required when the certificate type is SVR, and not required when the certificate type is CA.\n        :type CertificatePrivateKey: str\n        :param CertificateType: Certificate type. `CA`: client certificate; `SVR`: server certificate. The default value is SVR.\n        :type CertificateType: str\n        :param Alias: Alias\n        :type Alias: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param CertificateUse: \n        :type CertificateUse: str\n        """
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
        """
        :param CertificateId: Certificate ID\n        :type CertificateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")