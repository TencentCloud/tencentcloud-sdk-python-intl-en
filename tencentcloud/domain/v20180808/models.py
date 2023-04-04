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


class AdminContact(AbstractModel):
    """The admin contact.

    """

    def __init__(self):
        r"""
        :param FirstName: The first name.
        :type FirstName: str
        :param LastName: The last name.
        :type LastName: str
        :param Country: The country or region name, such as `CN`.
        :type Country: str
        :param Province: The province or state name.
        :type Province: str
        :param City: The city name.
        :type City: str
        :param AddressLine: The address line 1.
        :type AddressLine: str
        :param ZipCode: The zip code.
        :type ZipCode: str
        :param Email: The email address.
        :type Email: str
        :param Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self.FirstName = None
        self.LastName = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AddressLine = None
        self.ZipCode = None
        self.Email = None
        self.Phone = None
        self.CompanyName = None
        self.JobTitle = None
        self.AddressLineTwo = None
        self.Fax = None


    def _deserialize(self, params):
        self.FirstName = params.get("FirstName")
        self.LastName = params.get("LastName")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AddressLine = params.get("AddressLine")
        self.ZipCode = params.get("ZipCode")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.CompanyName = params.get("CompanyName")
        self.JobTitle = params.get("JobTitle")
        self.AddressLineTwo = params.get("AddressLineTwo")
        self.Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDomainBuyDetails(AbstractModel):
    """The log details of bulk domain purchase

    """

    def __init__(self):
        r"""
        :param Id: The details ID.
        :type Id: int
        :param Action: The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :type Action: str
        :param Domain: The domains.
        :type Domain: str
        :param Status: The status. Valid values: `SUCCESS`, `FAILURE`
        :type Status: str
        :param Reason: The reason for failure.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param CreatedOn: The creation time.
        :type CreatedOn: str
        :param UpdatedOn: The update time.
        :type UpdatedOn: str
        :param TransferDnsResult: Null: The DNS service is not transferred. `false`: The DNS service failed to be transferred. `true`: The DNS service is transferred successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferDnsResult: bool
        :param ReasonZh: The reason for failure, expressed in Chinese.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReasonZh: str
        :param PayStatus: The payment status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayStatus: int
        """
        self.Id = None
        self.Action = None
        self.Domain = None
        self.Status = None
        self.Reason = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.TransferDnsResult = None
        self.ReasonZh = None
        self.PayStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Action = params.get("Action")
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.TransferDnsResult = params.get("TransferDnsResult")
        self.ReasonZh = params.get("ReasonZh")
        self.PayStatus = params.get("PayStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDomainBuyLog(AbstractModel):
    """The log of bulk domain purchase

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param Action: The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :type Action: str
        :param Number: The quantity.
        :type Number: int
        :param Status: The execution status. Valid values: `doing`, `done`
        :type Status: str
        :param CreatedOn: The submission time.
        :type CreatedOn: str
        """
        self.LogId = None
        self.Action = None
        self.Number = None
        self.Status = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.Action = params.get("Action")
        self.Number = params.get("Number")
        self.Status = params.get("Status")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainDNSRequest(AbstractModel):
    """BatchModifyIntlDomainDNS request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The target domains.
        :type Domains: list of str
        :param Dns: The domain DNS array.
        :type Dns: list of str
        :param BatchAction: Valid values: `batch_modify_domain_dns1`, `batch_modify_domain_dns2`, `batch_modify_domain_dns3`
        :type BatchAction: str
        """
        self.Domains = None
        self.Dns = None
        self.BatchAction = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Dns = params.get("Dns")
        self.BatchAction = params.get("BatchAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainDNSResponse(AbstractModel):
    """BatchModifyIntlDomainDNS response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class BatchModifyIntlDomainInfoRequest(AbstractModel):
    """BatchModifyIntlDomainInfo request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The domains whose information is to be modified.
        :type Domains: list of str
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param LockTransfer: Whether to enable the 60-day inter-registrar transfer lock.
        :type LockTransfer: bool
        """
        self.Domains = None
        self.TemplateId = None
        self.LockTransfer = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.TemplateId = params.get("TemplateId")
        self.LockTransfer = params.get("LockTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainInfoResponse(AbstractModel):
    """BatchModifyIntlDomainInfo response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class BillingContact(AbstractModel):
    """The contact person for bills.

    """

    def __init__(self):
        r"""
        :param FirstName: The first name.
        :type FirstName: str
        :param LastName: The last name.
        :type LastName: str
        :param Country: The country or region name, such as `CN`.
        :type Country: str
        :param Province: The province or state name.
        :type Province: str
        :param City: The city name.
        :type City: str
        :param AddressLine: The address line 1.
        :type AddressLine: str
        :param ZipCode: The zip code.
        :type ZipCode: str
        :param Email: The email address.
        :type Email: str
        :param Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self.FirstName = None
        self.LastName = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AddressLine = None
        self.ZipCode = None
        self.Email = None
        self.Phone = None
        self.CompanyName = None
        self.JobTitle = None
        self.AddressLineTwo = None
        self.Fax = None


    def _deserialize(self, params):
        self.FirstName = params.get("FirstName")
        self.LastName = params.get("LastName")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AddressLine = params.get("AddressLine")
        self.ZipCode = params.get("ZipCode")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.CompanyName = params.get("CompanyName")
        self.JobTitle = params.get("JobTitle")
        self.AddressLineTwo = params.get("AddressLineTwo")
        self.Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntlDomainNewRequest(AbstractModel):
    """CheckIntlDomainNew request structure.

    """

    def __init__(self):
        r"""
        :param Domain: The name of the domain to be checked.
        :type Domain: str
        :param Period: Period, in years. If this parameter is left empty, premium domains cannot be queried.
        :type Period: str
        """
        self.Domain = None
        self.Period = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntlDomainNewResponse(AbstractModel):
    """CheckIntlDomainNew response structure.

    """

    def __init__(self):
        r"""
        :param DomainName: The name of the domain checked.
        :type DomainName: str
        :param Available: Whether the domain is available for registration.
        :type Available: bool
        :param Reason: The reason why the domain cannot be registered.
        :type Reason: str
        :param Premium: Whether the domain is a premium one.
        :type Premium: bool
        :param Price: The domain price.
        :type Price: float
        :param BlackWord: Whether the domain name involves restricted words.
        :type BlackWord: bool
        :param Describe: The premium domain description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param FeeRenew: The price for renewing the premium domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeeRenew: float
        :param RealPrice: The real price of the domain. For a premium domain, its price varies depending on the period. For a non-premium domain, the price is the 1-year price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealPrice: float
        :param FeeTransfer: The price for transferring a premium domain in.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeeTransfer: float
        :param FeeRestore: The price for redeeming a premium domain.
        :type FeeRestore: float
        :param Period: The period (in years) of the domain.
        :type Period: int
        :param ReasonZh: The reason why the domain cannot be registered, expressed in Chinese.
        :type ReasonZh: str
        :param ResCode: The internal error code.
        :type ResCode: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainName = None
        self.Available = None
        self.Reason = None
        self.Premium = None
        self.Price = None
        self.BlackWord = None
        self.Describe = None
        self.FeeRenew = None
        self.RealPrice = None
        self.FeeTransfer = None
        self.FeeRestore = None
        self.Period = None
        self.ReasonZh = None
        self.ResCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Available = params.get("Available")
        self.Reason = params.get("Reason")
        self.Premium = params.get("Premium")
        self.Price = params.get("Price")
        self.BlackWord = params.get("BlackWord")
        self.Describe = params.get("Describe")
        self.FeeRenew = params.get("FeeRenew")
        self.RealPrice = params.get("RealPrice")
        self.FeeTransfer = params.get("FeeTransfer")
        self.FeeRestore = params.get("FeeRestore")
        self.Period = params.get("Period")
        self.ReasonZh = params.get("ReasonZh")
        self.ResCode = params.get("ResCode")
        self.RequestId = params.get("RequestId")


class CreateIntlDomainBatchRequest(AbstractModel):
    """CreateIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param Period: The purchase period (years) of the domain. Value range: [1-10]
        :type Period: int
        :param Domains: The domains (maximum 4,000) to purchase.
        :type Domains: list of str
        :param PayMode: The payment method. Valid values: `0` (online payment), `1` (account balance), `2` (package), `3` (offline settlement).
        :type PayMode: int
        :param AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        :param TransferProhibition: Whether to enable the transfer prohibition lock.
        :type TransferProhibition: bool
        :param UpdateProhibition: Whether to enable the update prohibition lock.
        :type UpdateProhibition: bool
        :param CustomDns: The custom DNS servers
        :type CustomDns: list of str
        """
        self.TemplateId = None
        self.Period = None
        self.Domains = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.TransferProhibition = None
        self.UpdateProhibition = None
        self.CustomDns = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Period = params.get("Period")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TransferProhibition = params.get("TransferProhibition")
        self.UpdateProhibition = params.get("UpdateProhibition")
        self.CustomDns = params.get("CustomDns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlDomainBatchResponse(AbstractModel):
    """CreateIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class CreateIntlPhoneEmailRequest(AbstractModel):
    """CreateIntlPhoneEmail request structure.

    """

    def __init__(self):
        r"""
        :param Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param Code: The mobile number or email address.
        :type Code: str
        :param VerifyCode: The verification code.
        :type VerifyCode: str
        """
        self.Type = None
        self.Code = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Code = params.get("Code")
        self.VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlPhoneEmailResponse(AbstractModel):
    """CreateIntlPhoneEmail response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateIntlTemplateRequest(AbstractModel):
    """CreateIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param TemplateType: The profile type. Valid values: `I` (individual, default), `E` (organization).
        :type TemplateType: str
        """
        self.RegistrantContact = None
        self.AdminContact = None
        self.TechnicalContact = None
        self.BillingContact = None
        self.TemplateType = None


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self.RegistrantContact = RegistrantContact()
            self.RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self.AdminContact = AdminContact()
            self.AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self.TechnicalContact = TechnicalContact()
            self.TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self.BillingContact = BillingContact()
            self.BillingContact._deserialize(params.get("BillingContact"))
        self.TemplateType = params.get("TemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlTemplateResponse(AbstractModel):
    """CreateIntlTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class DeleteIntlPhoneEmailRequest(AbstractModel):
    """DeleteIntlPhoneEmail request structure.

    """

    def __init__(self):
        r"""
        :param Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param Code: The mobile number or email address.
        :type Code: str
        """
        self.Type = None
        self.Code = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntlPhoneEmailResponse(AbstractModel):
    """DeleteIntlPhoneEmail response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIntlTemplateRequest(AbstractModel):
    """DeleteIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: The unique ID of the target registrant profile.
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntlTemplateResponse(AbstractModel):
    """DeleteIntlTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeIntlBatchDetailStatusRequest(AbstractModel):
    """DescribeIntlBatchDetailStatus request structure.

    """

    def __init__(self):
        r"""
        :param LogIds: The IDs of the logs to be queried.
        :type LogIds: list of int
        """
        self.LogIds = None


    def _deserialize(self, params):
        self.LogIds = params.get("LogIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlBatchDetailStatusResponse(AbstractModel):
    """DescribeIntlBatchDetailStatus response structure.

    """

    def __init__(self):
        r"""
        :param Details: The details.
        :type Details: list of IntlBatchDetails
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = IntlBatchDetails()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntlBatchOperationLogsRequest(AbstractModel):
    """DescribeIntlBatchOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The offset. Default value: 0
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlBatchOperationLogsResponse(AbstractModel):
    """DescribeIntlBatchOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total count.
        :type TotalCount: int
        :param DomainBatchLogSet: The log list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainBatchLogSet: list of BatchDomainBuyLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DomainBatchLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainBatchLogSet") is not None:
            self.DomainBatchLogSet = []
            for item in params.get("DomainBatchLogSet"):
                obj = BatchDomainBuyLog()
                obj._deserialize(item)
                self.DomainBatchLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntlDomainBatchDetailsRequest(AbstractModel):
    """DescribeIntlDomainBatchDetails request structure.

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param Offset: The offset. Default value: 0
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param OrderByKey: The sort key. Valid values: `Domain`, `UpdateOn`, `Status`
        :type OrderByKey: str
        :param OrderBy: Valid values: `0` (ascending), `1` (descending).
        :type OrderBy: int
        """
        self.LogId = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainBatchDetailsResponse(AbstractModel):
    """DescribeIntlDomainBatchDetails response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The total count.
        :type TotalCount: int
        :param DomainBatchDetailSet: The list of log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainBatchDetailSet: list of BatchDomainBuyDetails
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DomainBatchDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainBatchDetailSet") is not None:
            self.DomainBatchDetailSet = []
            for item in params.get("DomainBatchDetailSet"):
                obj = BatchDomainBuyDetails()
                obj._deserialize(item)
                self.DomainBatchDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntlDomainListRequest(AbstractModel):
    """DescribeIntlDomainList request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The page number in pagination cases.
        :type Offset: int
        :param Limit: The number of records on each page in pagination cases.
        :type Limit: int
        :param KeyWord: The domain keyword for fuzzy search.
        :type KeyWord: str
        :param OrderByRegTime: The registration time sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByRegTime: int
        :param OrderByExpireTime: The expiration time sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByExpireTime: int
        :param Status: The domain status.
`all`: All domains.
`UrgentNeedRenew`: The domains that are in urgent need of renewal.
`RedemptionPending`: The domains that are in urgent need of redemption.
`nosubmit`: The domains with unverified identities.
`tran`: The domains that are being transferred in.
        :type Status: str
        :param DnsStatus: The DNS type. Valid values: `1` (DNSPod), `2` (others).
        :type DnsStatus: int
        :param OrderByDomainName: The domain sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByDomainName: int
        """
        self.Offset = None
        self.Limit = None
        self.KeyWord = None
        self.OrderByRegTime = None
        self.OrderByExpireTime = None
        self.Status = None
        self.DnsStatus = None
        self.OrderByDomainName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.KeyWord = params.get("KeyWord")
        self.OrderByRegTime = params.get("OrderByRegTime")
        self.OrderByExpireTime = params.get("OrderByExpireTime")
        self.Status = params.get("Status")
        self.DnsStatus = params.get("DnsStatus")
        self.OrderByDomainName = params.get("OrderByDomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainListResponse(AbstractModel):
    """DescribeIntlDomainList response structure.

    """

    def __init__(self):
        r"""
        :param DomainSet: The domain information set.
        :type DomainSet: list of IntlDomainInfo
        :param TotalCount: The total number of domains.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = IntlDomainInfo()
                obj._deserialize(item)
                self.DomainSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIntlDomainPriceNewListRequest(AbstractModel):
    """DescribeIntlDomainPriceNewList request structure.

    """

    def __init__(self):
        r"""
        :param TldList: The list of domain suffixes for which you want to query prices. This parameter defaults to all suffixes.
        :type TldList: list of str
        :param Year: The purchase year of the domains for which you want to query prices. This parameter defaults to all years.
        :type Year: list of int
        :param Operation: The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :type Operation: list of str
        """
        self.TldList = None
        self.Year = None
        self.Operation = None


    def _deserialize(self, params):
        self.TldList = params.get("TldList")
        self.Year = params.get("Year")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainPriceNewListResponse(AbstractModel):
    """DescribeIntlDomainPriceNewList response structure.

    """

    def __init__(self):
        r"""
        :param PriceList: The price list of domains.
        :type PriceList: list of PriceInfoNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PriceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PriceList") is not None:
            self.PriceList = []
            for item in params.get("PriceList"):
                obj = PriceInfoNew()
                obj._deserialize(item)
                self.PriceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIntlDomainRequest(AbstractModel):
    """DescribeIntlDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainId: The domain ID.
        :type DomainId: str
        """
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainResponse(AbstractModel):
    """DescribeIntlDomain response structure.

    """

    def __init__(self):
        r"""
        :param DomainInfo: The domain information.
        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.IntlDomainInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = IntlDomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeIntlPhoneEmailListRequest(AbstractModel):
    """DescribeIntlPhoneEmailList request structure.

    """

    def __init__(self):
        r"""
        :param Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param Limit: The number of records on each page in pagination cases.
        :type Limit: int
        :param Offset: The page number in pagination cases.
        :type Offset: int
        """
        self.Type = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlPhoneEmailListResponse(AbstractModel):
    """DescribeIntlPhoneEmailList response structure.

    """

    def __init__(self):
        r"""
        :param PhoneEmailList: The list of verified mobile numbers and email addresses.
        :type PhoneEmailList: list of IntlPhoneEmailLists
        :param TotalCount: The total count.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PhoneEmailList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PhoneEmailList") is not None:
            self.PhoneEmailList = []
            for item in params.get("PhoneEmailList"):
                obj = IntlPhoneEmailLists()
                obj._deserialize(item)
                self.PhoneEmailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIntlTemplateListRequest(AbstractModel):
    """DescribeIntlTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The offset.
        :type Offset: int
        :param Limit: The maximum number of entries.
        :type Limit: int
        :param Keyword: The domain registrant keyword for exact match.
        :type Keyword: str
        :param Type: The type. Valid values: `all` (all types), `I` (individual), `E` (organization).
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlTemplateListResponse(AbstractModel):
    """DescribeIntlTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param TemplateSet: The registrant profile list information.
        :type TemplateSet: list of IntlTemplate
        :param TotalCount: The total count.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateSet") is not None:
            self.TemplateSet = []
            for item in params.get("TemplateSet"):
                obj = IntlTemplate()
                obj._deserialize(item)
                self.TemplateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIntlTemplateRequest(AbstractModel):
    """DescribeIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: The unique ID of a registrant profile.
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlTemplateResponse(AbstractModel):
    """DescribeIntlTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Template: The details of the registrant profile.
        :type Template: :class:`tencentcloud.domain.v20180808.models.IntlTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = IntlTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class IntlBatchDetails(AbstractModel):
    """The details of the bulk task

    """

    def __init__(self):
        r"""
        :param Id: The ID of the bulk task.
        :type Id: int
        :param Status: The task status.
        :type Status: str
        :param Reason: The reason.
        :type Reason: str
        :param ReasonZh: The reason, expressed in Chinese.
        :type ReasonZh: str
        """
        self.Id = None
        self.Status = None
        self.Reason = None
        self.ReasonZh = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.ReasonZh = params.get("ReasonZh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlContactInfo(AbstractModel):
    """The contact information.

    """

    def __init__(self):
        r"""
        :param City: The city name.
        :type City: str
        :param Country: The country or region name.
        :type Country: str
        :param Email: The email address.
        :type Email: str
        :param OrganizationName: The domain registrant.
        :type OrganizationName: str
        :param Province: The province or state name.
        :type Province: str
        :param RegistrantName: The name of the registrant.
        :type RegistrantName: str
        :param RegistrantType: The registrant type. Valid values: `I` (individual), `E` (organization).
        :type RegistrantType: str
        :param Street: The detailed address.
        :type Street: str
        :param Telephone: The mobile number.
        :type Telephone: str
        :param ZipCode: The zip code.
        :type ZipCode: str
        :param FirstName: The first name.
        :type FirstName: str
        :param LastName: The last name.
        :type LastName: str
        :param CompanyName: The company name.
        :type CompanyName: str
        """
        self.City = None
        self.Country = None
        self.Email = None
        self.OrganizationName = None
        self.Province = None
        self.RegistrantName = None
        self.RegistrantType = None
        self.Street = None
        self.Telephone = None
        self.ZipCode = None
        self.FirstName = None
        self.LastName = None
        self.CompanyName = None


    def _deserialize(self, params):
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Email = params.get("Email")
        self.OrganizationName = params.get("OrganizationName")
        self.Province = params.get("Province")
        self.RegistrantName = params.get("RegistrantName")
        self.RegistrantType = params.get("RegistrantType")
        self.Street = params.get("Street")
        self.Telephone = params.get("Telephone")
        self.ZipCode = params.get("ZipCode")
        self.FirstName = params.get("FirstName")
        self.LastName = params.get("LastName")
        self.CompanyName = params.get("CompanyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlDomainInfo(AbstractModel):
    """The domain information set.

    """

    def __init__(self):
        r"""
        :param AutoRenew: The auto-renewal flag. Valid values: `0` (disabled by default), `1` (enabled), `2` (disabled).
        :type AutoRenew: int
        :param CreationDate: The registration time.
        :type CreationDate: str
        :param DomainId: The domain ID.
        :type DomainId: str
        :param DnsStatus: The DNS status. Valid values: `1` (DNSPod), `2` (others), `3` (unknown).
        :type DnsStatus: int
        :param DomainName: The domains.
        :type DomainName: str
        :param DomainStatus: The domain status.
        :type DomainStatus: list of str
        :param Status: The purchase status of the domain. Valid values:
`ok`: Normal.
`RegisterPending`: Pending registration.
`RegisterDoing`: Registration in progress.
`RegisterFailed`: Registration failed.
`RenewPending`: Renewal grace period.
`RenewDoing`: Renewing.
`RedemptionPending`: Redemption period.
`AboutToExpire`: About to expire.
`TransferPending`: Pending transfer.
`TransferTransing`: Transfer in progress.
`TransferFailed`: Transfer failed.
        :type Status: str
        :param ExpirationDate: The expiration date.
        :type ExpirationDate: str
        :param ExpireMessage: The auto-renewal flag. Valid values: `1` (enabled), `2` (disabled), `3` (disabled by default).
        :type ExpireMessage: int
        :param IsPremium: Whether the domain is a premium one.
        :type IsPremium: bool
        :param Dns: The DNS server of the domain.
        :type Dns: list of str
        :param ContactInfo: The contact information.
        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.IntlContactInfo`
        :param CanRenewYears: The number of years available for renewal. The value `0` indicates that the domain has reached its maximum validity period (10 years) and cannot be renewed.
        :type CanRenewYears: int
        :param RegistrarType: The registrar type. If the value is `epp`, the registration time on the page is followed by (UTC). Otherwise, it is followed by (UTC+8).
        :type RegistrarType: str
        :param Uin: The account to which the domain belongs.
        :type Uin: str
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param SupportDnssec: Whether DNSSEC is supported.
        :type SupportDnssec: bool
        :param WhoisPrivacy: WHOIS privacy service status. Valid values: `1` (enabled), `2` (disabled), `3` (enabling), `4` (disabling).
        :type WhoisPrivacy: int
        :param ModifyStatus: Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :type ModifyStatus: str
        :param DnsModifyStatus: Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :type DnsModifyStatus: str
        """
        self.AutoRenew = None
        self.CreationDate = None
        self.DomainId = None
        self.DnsStatus = None
        self.DomainName = None
        self.DomainStatus = None
        self.Status = None
        self.ExpirationDate = None
        self.ExpireMessage = None
        self.IsPremium = None
        self.Dns = None
        self.ContactInfo = None
        self.CanRenewYears = None
        self.RegistrarType = None
        self.Uin = None
        self.TemplateId = None
        self.SupportDnssec = None
        self.WhoisPrivacy = None
        self.ModifyStatus = None
        self.DnsModifyStatus = None


    def _deserialize(self, params):
        self.AutoRenew = params.get("AutoRenew")
        self.CreationDate = params.get("CreationDate")
        self.DomainId = params.get("DomainId")
        self.DnsStatus = params.get("DnsStatus")
        self.DomainName = params.get("DomainName")
        self.DomainStatus = params.get("DomainStatus")
        self.Status = params.get("Status")
        self.ExpirationDate = params.get("ExpirationDate")
        self.ExpireMessage = params.get("ExpireMessage")
        self.IsPremium = params.get("IsPremium")
        self.Dns = params.get("Dns")
        if params.get("ContactInfo") is not None:
            self.ContactInfo = IntlContactInfo()
            self.ContactInfo._deserialize(params.get("ContactInfo"))
        self.CanRenewYears = params.get("CanRenewYears")
        self.RegistrarType = params.get("RegistrarType")
        self.Uin = params.get("Uin")
        self.TemplateId = params.get("TemplateId")
        self.SupportDnssec = params.get("SupportDnssec")
        self.WhoisPrivacy = params.get("WhoisPrivacy")
        self.ModifyStatus = params.get("ModifyStatus")
        self.DnsModifyStatus = params.get("DnsModifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlPhoneEmailLists(AbstractModel):
    """The list of verified mobile numbers and email addresses.

    """

    def __init__(self):
        r"""
        :param Code: The mobile number or email address.
        :type Code: str
        :param Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param CreatedOn: The verification time.
        :type CreatedOn: str
        """
        self.Code = None
        self.Type = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlTemplate(AbstractModel):
    """The details of the registrant profile.

    """

    def __init__(self):
        r"""
        :param RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param CreatedOn: The creation time.
        :type CreatedOn: str
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param IsDefault: Whether the profile is the default one.
        :type IsDefault: int
        :param UpdatedOn: The last update time.
        :type UpdatedOn: str
        """
        self.RegistrantContact = None
        self.AdminContact = None
        self.TechnicalContact = None
        self.BillingContact = None
        self.CreatedOn = None
        self.TemplateId = None
        self.IsDefault = None
        self.UpdatedOn = None


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self.RegistrantContact = RegistrantContact()
            self.RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self.AdminContact = AdminContact()
            self.AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self.TechnicalContact = TechnicalContact()
            self.TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self.BillingContact = BillingContact()
            self.BillingContact._deserialize(params.get("BillingContact"))
        self.CreatedOn = params.get("CreatedOn")
        self.TemplateId = params.get("TemplateId")
        self.IsDefault = params.get("IsDefault")
        self.UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlTemplateInfo(AbstractModel):
    """The registrant profile details.

    """

    def __init__(self):
        r"""
        :param RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param CreatedOn: The creation time.
        :type CreatedOn: str
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param TemplateType: The registrant type. Valid values: `I` (individual), `E` (organization).
        :type TemplateType: str
        :param UpdatedOn: The last updated time.
        :type UpdatedOn: str
        :param Uin: The account ID.
        :type Uin: str
        :param IsDefault: Whether the profile is the default one.
        :type IsDefault: int
        """
        self.RegistrantContact = None
        self.AdminContact = None
        self.TechnicalContact = None
        self.BillingContact = None
        self.CreatedOn = None
        self.TemplateId = None
        self.TemplateType = None
        self.UpdatedOn = None
        self.Uin = None
        self.IsDefault = None


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self.RegistrantContact = RegistrantContact()
            self.RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self.AdminContact = AdminContact()
            self.AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self.TechnicalContact = TechnicalContact()
            self.TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self.BillingContact = BillingContact()
            self.BillingContact._deserialize(params.get("BillingContact"))
        self.CreatedOn = params.get("CreatedOn")
        self.TemplateId = params.get("TemplateId")
        self.TemplateType = params.get("TemplateType")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Uin = params.get("Uin")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnerIntlBatchRequest(AbstractModel):
    """ModifyOwnerIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The domains.
        :type Domains: list of str
        :param ToUin: The user ID.
        :type ToUin: str
        :param DnsTransfer: Whether to transfer the DNS service.
        :type DnsTransfer: bool
        """
        self.Domains = None
        self.ToUin = None
        self.DnsTransfer = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.ToUin = params.get("ToUin")
        self.DnsTransfer = params.get("DnsTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnerIntlBatchResponse(AbstractModel):
    """ModifyOwnerIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The ID of the bulk task.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class PriceInfoNew(AbstractModel):
    """The price information of the domains.

    """

    def __init__(self):
        r"""
        :param Tld: The domain suffix, such as `.com`.
        :type Tld: str
        :param Year: The purchase years. Value range: [1-10]
        :type Year: int
        :param Price: The original price of the domain.
        :type Price: float
        :param RealPrice: The current price of the domain.
        :type RealPrice: float
        :param Operation: The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :type Operation: str
        :param Title: The title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Title: str
        """
        self.Tld = None
        self.Year = None
        self.Price = None
        self.RealPrice = None
        self.Operation = None
        self.Title = None


    def _deserialize(self, params):
        self.Tld = params.get("Tld")
        self.Year = params.get("Year")
        self.Price = params.get("Price")
        self.RealPrice = params.get("RealPrice")
        self.Operation = params.get("Operation")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistrantContact(AbstractModel):
    """The registrant contact.

    """

    def __init__(self):
        r"""
        :param FirstName: The first name.
        :type FirstName: str
        :param LastName: The last name.
        :type LastName: str
        :param Country: The country or region name, such as `CN`.
        :type Country: str
        :param Province: The province or state name.
        :type Province: str
        :param City: The city name.
        :type City: str
        :param AddressLine: The address line 1.
        :type AddressLine: str
        :param ZipCode: The zip code.
        :type ZipCode: str
        :param Email: The email address.
        :type Email: str
        :param Phone: The mobile number, such as `+86.1360000000`.
        :type Phone: str
        :param CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self.FirstName = None
        self.LastName = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AddressLine = None
        self.ZipCode = None
        self.Email = None
        self.Phone = None
        self.CompanyName = None
        self.JobTitle = None
        self.AddressLineTwo = None
        self.Fax = None


    def _deserialize(self, params):
        self.FirstName = params.get("FirstName")
        self.LastName = params.get("LastName")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AddressLine = params.get("AddressLine")
        self.ZipCode = params.get("ZipCode")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.CompanyName = params.get("CompanyName")
        self.JobTitle = params.get("JobTitle")
        self.AddressLineTwo = params.get("AddressLineTwo")
        self.Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewIntlDomainBatchRequest(AbstractModel):
    """RenewIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The domains to check.
        :type Domains: list of str
        :param Period: The period (1 to 10 years). If this parameter is left empty, premium domains cannot be checked.
        :type Period: int
        :param PayMode: Payment method. Valid value: `1` (account balance).
        :type PayMode: int
        :param AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        """
        self.Domains = None
        self.Period = None
        self.PayMode = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Period = params.get("Period")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewIntlDomainBatchResponse(AbstractModel):
    """RenewIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The ID of the bulk task.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class SendIntlPhoneEmailCodeRequest(AbstractModel):
    """SendIntlPhoneEmailCode request structure.

    """

    def __init__(self):
        r"""
        :param Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param Code: The mobile number or email address.
        :type Code: str
        """
        self.Type = None
        self.Code = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendIntlPhoneEmailCodeResponse(AbstractModel):
    """SendIntlPhoneEmailCode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetIntlDomainAutoRenewRequest(AbstractModel):
    """SetIntlDomainAutoRenew request structure.

    """

    def __init__(self):
        r"""
        :param DomainId: The domain ID.
        :type DomainId: str
        :param AutoRenew: Whether to enable auto-renewal. Valid values: `1` (enable), `2` (disable).
        :type AutoRenew: int
        """
        self.DomainId = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetIntlDomainAutoRenewResponse(AbstractModel):
    """SetIntlDomainAutoRenew response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TechnicalContact(AbstractModel):
    """The technical contact.

    """

    def __init__(self):
        r"""
        :param FirstName: The first name.
        :type FirstName: str
        :param LastName: The last name.
        :type LastName: str
        :param Country: The country or region name, such as `CN`.
        :type Country: str
        :param Province: The province or state name.
        :type Province: str
        :param City: The city name.
        :type City: str
        :param AddressLine: The address line 1.
        :type AddressLine: str
        :param ZipCode: The zip code.
        :type ZipCode: str
        :param Email: The email address.
        :type Email: str
        :param Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self.FirstName = None
        self.LastName = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AddressLine = None
        self.ZipCode = None
        self.Email = None
        self.Phone = None
        self.CompanyName = None
        self.JobTitle = None
        self.AddressLineTwo = None
        self.Fax = None


    def _deserialize(self, params):
        self.FirstName = params.get("FirstName")
        self.LastName = params.get("LastName")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AddressLine = params.get("AddressLine")
        self.ZipCode = params.get("ZipCode")
        self.Email = params.get("Email")
        self.Phone = params.get("Phone")
        self.CompanyName = params.get("CompanyName")
        self.JobTitle = params.get("JobTitle")
        self.AddressLineTwo = params.get("AddressLineTwo")
        self.Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInIntlDomainBatchRequest(AbstractModel):
    """TransferInIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: The profile ID.
        :type TemplateId: str
        :param PassWords: The transfer passwords for the domains.
        :type PassWords: list of str
        :param Domains: The domains to be bulk transferred in.
        :type Domains: list of str
        :param PayMode: The payment method. Valid value: `1` (account balance).
        :type PayMode: int
        :param AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        :param TransferProhibition: Whether to enable the transfer prohibition lock.
        :type TransferProhibition: bool
        :param UpdateProhibition: Whether to enable the update prohibition lock.
        :type UpdateProhibition: bool
        :param LockTransfer: Whether to enable the 60-day inter-registrar transfer lock.
        :type LockTransfer: bool
        """
        self.TemplateId = None
        self.PassWords = None
        self.Domains = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.TransferProhibition = None
        self.UpdateProhibition = None
        self.LockTransfer = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.PassWords = params.get("PassWords")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TransferProhibition = params.get("TransferProhibition")
        self.UpdateProhibition = params.get("UpdateProhibition")
        self.LockTransfer = params.get("LockTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInIntlDomainBatchResponse(AbstractModel):
    """TransferInIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class TransferProhibitionIntlBatchRequest(AbstractModel):
    """TransferProhibitionIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The domain array.
        :type Domains: list of str
        :param Status: Whether to enable transfer prohibition. Valid values: `true` (enable), `false` (disable).
        :type Status: bool
        """
        self.Domains = None
        self.Status = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferProhibitionIntlBatchResponse(AbstractModel):
    """TransferProhibitionIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class UpdateProhibitionIntlBatchRequest(AbstractModel):
    """UpdateProhibitionIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param Domains: The domain array.
        :type Domains: list of str
        :param Status: Whether to enable update prohibition. Valid values: `true` (enable), `false` (disable).
        :type Status: bool
        """
        self.Domains = None
        self.Status = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProhibitionIntlBatchResponse(AbstractModel):
    """UpdateProhibitionIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param LogId: The log ID.
        :type LogId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")