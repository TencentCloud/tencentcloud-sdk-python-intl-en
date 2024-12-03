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
        :param _FirstName: The first name.
        :type FirstName: str
        :param _LastName: The last name.
        :type LastName: str
        :param _Country: The country or region name, such as `CN`.
        :type Country: str
        :param _Province: The province or state name.
        :type Province: str
        :param _City: The city name.
        :type City: str
        :param _AddressLine: The address line 1.
        :type AddressLine: str
        :param _ZipCode: The zip code.
        :type ZipCode: str
        :param _Email: The email address.
        :type Email: str
        :param _Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param _CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param _JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param _AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param _Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self._FirstName = None
        self._LastName = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._ZipCode = None
        self._Email = None
        self._Phone = None
        self._CompanyName = None
        self._JobTitle = None
        self._AddressLineTwo = None
        self._Fax = None

    @property
    def FirstName(self):
        """The first name.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        """The last name.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Country(self):
        """The country or region name, such as `CN`.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """The province or state name.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city name.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """The address line 1.
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def ZipCode(self):
        """The zip code.
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

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
    def Phone(self):
        """The mobile number, such as `+86.13600000000`.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def CompanyName(self):
        """The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def JobTitle(self):
        """The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobTitle

    @JobTitle.setter
    def JobTitle(self, JobTitle):
        self._JobTitle = JobTitle

    @property
    def AddressLineTwo(self):
        """The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressLineTwo

    @AddressLineTwo.setter
    def AddressLineTwo(self, AddressLineTwo):
        self._AddressLineTwo = AddressLineTwo

    @property
    def Fax(self):
        """The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fax

    @Fax.setter
    def Fax(self, Fax):
        self._Fax = Fax


    def _deserialize(self, params):
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._ZipCode = params.get("ZipCode")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._CompanyName = params.get("CompanyName")
        self._JobTitle = params.get("JobTitle")
        self._AddressLineTwo = params.get("AddressLineTwo")
        self._Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDomainBuyDetails(AbstractModel):
    """The log details of bulk domain purchase

    """

    def __init__(self):
        r"""
        :param _Id: The details ID.
        :type Id: int
        :param _Action: The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :type Action: str
        :param _Domain: The domains.
        :type Domain: str
        :param _Status: The status. Valid values: `SUCCESS`, `FAILURE`
        :type Status: str
        :param _Reason: The reason for failure.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param _CreatedOn: The creation time.
        :type CreatedOn: str
        :param _UpdatedOn: The update time.
        :type UpdatedOn: str
        :param _TransferDnsResult: Null: The DNS service is not transferred. `false`: The DNS service failed to be transferred. `true`: The DNS service is transferred successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransferDnsResult: bool
        :param _ReasonZh: The reason for failure, expressed in Chinese.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReasonZh: str
        :param _PayStatus: The payment status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayStatus: int
        """
        self._Id = None
        self._Action = None
        self._Domain = None
        self._Status = None
        self._Reason = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._TransferDnsResult = None
        self._ReasonZh = None
        self._PayStatus = None

    @property
    def Id(self):
        """The details ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Action(self):
        """The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Domain(self):
        """The domains.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """The status. Valid values: `SUCCESS`, `FAILURE`
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        """The reason for failure.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def CreatedOn(self):
        """The creation time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """The update time.
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def TransferDnsResult(self):
        """Null: The DNS service is not transferred. `false`: The DNS service failed to be transferred. `true`: The DNS service is transferred successfully.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._TransferDnsResult

    @TransferDnsResult.setter
    def TransferDnsResult(self, TransferDnsResult):
        self._TransferDnsResult = TransferDnsResult

    @property
    def ReasonZh(self):
        """The reason for failure, expressed in Chinese.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReasonZh

    @ReasonZh.setter
    def ReasonZh(self, ReasonZh):
        self._ReasonZh = ReasonZh

    @property
    def PayStatus(self):
        """The payment status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayStatus

    @PayStatus.setter
    def PayStatus(self, PayStatus):
        self._PayStatus = PayStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Action = params.get("Action")
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._TransferDnsResult = params.get("TransferDnsResult")
        self._ReasonZh = params.get("ReasonZh")
        self._PayStatus = params.get("PayStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDomainBuyLog(AbstractModel):
    """The log of bulk domain purchase

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _Action: The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :type Action: str
        :param _Number: The quantity.
        :type Number: int
        :param _Status: The execution status. Valid values: `doing`, `done`
        :type Status: str
        :param _CreatedOn: The submission time.
        :type CreatedOn: str
        """
        self._LogId = None
        self._Action = None
        self._Number = None
        self._Status = None
        self._CreatedOn = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def Action(self):
        """The bulk operation type. Valid values: `new` (register domains), `batch_transfer_prohibition_on` (enable transfer prohibition), `batch_transfer_prohibition_off` (disable transfer prohibition), `batch_update_prohibition_on` (enable update prohibition), `batch_update_prohibition_off` (disable update prohibition).
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Number(self):
        """The quantity.
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Status(self):
        """The execution status. Valid values: `doing`, `done`
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedOn(self):
        """The submission time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._Action = params.get("Action")
        self._Number = params.get("Number")
        self._Status = params.get("Status")
        self._CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainDNSRequest(AbstractModel):
    """BatchModifyIntlDomainDNS request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The target domains.
        :type Domains: list of str
        :param _Dns: The domain DNS array.
        :type Dns: list of str
        :param _BatchAction: Valid values: `batch_modify_domain_dns1`, `batch_modify_domain_dns2`, `batch_modify_domain_dns3`
        :type BatchAction: str
        """
        self._Domains = None
        self._Dns = None
        self._BatchAction = None

    @property
    def Domains(self):
        """The target domains.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Dns(self):
        """The domain DNS array.
        :rtype: list of str
        """
        return self._Dns

    @Dns.setter
    def Dns(self, Dns):
        self._Dns = Dns

    @property
    def BatchAction(self):
        """Valid values: `batch_modify_domain_dns1`, `batch_modify_domain_dns2`, `batch_modify_domain_dns3`
        :rtype: str
        """
        return self._BatchAction

    @BatchAction.setter
    def BatchAction(self, BatchAction):
        self._BatchAction = BatchAction


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._Dns = params.get("Dns")
        self._BatchAction = params.get("BatchAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainDNSResponse(AbstractModel):
    """BatchModifyIntlDomainDNS response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class BatchModifyIntlDomainInfoRequest(AbstractModel):
    """BatchModifyIntlDomainInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The domains whose information is to be modified.
        :type Domains: list of str
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _LockTransfer: Whether to enable the 60-day inter-registrar transfer lock.
        :type LockTransfer: bool
        """
        self._Domains = None
        self._TemplateId = None
        self._LockTransfer = None

    @property
    def Domains(self):
        """The domains whose information is to be modified.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def LockTransfer(self):
        """Whether to enable the 60-day inter-registrar transfer lock.
        :rtype: bool
        """
        return self._LockTransfer

    @LockTransfer.setter
    def LockTransfer(self, LockTransfer):
        self._LockTransfer = LockTransfer


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._TemplateId = params.get("TemplateId")
        self._LockTransfer = params.get("LockTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyIntlDomainInfoResponse(AbstractModel):
    """BatchModifyIntlDomainInfo response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class BillingContact(AbstractModel):
    """The contact person for bills.

    """

    def __init__(self):
        r"""
        :param _FirstName: The first name.
        :type FirstName: str
        :param _LastName: The last name.
        :type LastName: str
        :param _Country: The country or region name, such as `CN`.
        :type Country: str
        :param _Province: The province or state name.
        :type Province: str
        :param _City: The city name.
        :type City: str
        :param _AddressLine: The address line 1.
        :type AddressLine: str
        :param _ZipCode: The zip code.
        :type ZipCode: str
        :param _Email: The email address.
        :type Email: str
        :param _Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param _CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param _JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param _AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param _Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self._FirstName = None
        self._LastName = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._ZipCode = None
        self._Email = None
        self._Phone = None
        self._CompanyName = None
        self._JobTitle = None
        self._AddressLineTwo = None
        self._Fax = None

    @property
    def FirstName(self):
        """The first name.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        """The last name.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Country(self):
        """The country or region name, such as `CN`.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """The province or state name.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city name.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """The address line 1.
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def ZipCode(self):
        """The zip code.
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

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
    def Phone(self):
        """The mobile number, such as `+86.13600000000`.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def CompanyName(self):
        """The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def JobTitle(self):
        """The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobTitle

    @JobTitle.setter
    def JobTitle(self, JobTitle):
        self._JobTitle = JobTitle

    @property
    def AddressLineTwo(self):
        """The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressLineTwo

    @AddressLineTwo.setter
    def AddressLineTwo(self, AddressLineTwo):
        self._AddressLineTwo = AddressLineTwo

    @property
    def Fax(self):
        """The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fax

    @Fax.setter
    def Fax(self, Fax):
        self._Fax = Fax


    def _deserialize(self, params):
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._ZipCode = params.get("ZipCode")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._CompanyName = params.get("CompanyName")
        self._JobTitle = params.get("JobTitle")
        self._AddressLineTwo = params.get("AddressLineTwo")
        self._Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntlDomainNewRequest(AbstractModel):
    """CheckIntlDomainNew request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: The name of the domain to be checked.
        :type Domain: str
        :param _Period: Period, in years. If this parameter is left empty, premium domains cannot be queried.
        :type Period: str
        """
        self._Domain = None
        self._Period = None

    @property
    def Domain(self):
        """The name of the domain to be checked.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Period(self):
        """Period, in years. If this parameter is left empty, premium domains cannot be queried.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIntlDomainNewResponse(AbstractModel):
    """CheckIntlDomainNew response structure.

    """

    def __init__(self):
        r"""
        :param _DomainName: The name of the domain checked.
        :type DomainName: str
        :param _Available: Whether the domain is available for registration.
        :type Available: bool
        :param _Reason: The reason why the domain cannot be registered.
        :type Reason: str
        :param _Premium: Whether the domain is a premium one.
        :type Premium: bool
        :param _Price: The domain price.
        :type Price: float
        :param _BlackWord: Whether the domain name involves restricted words.
        :type BlackWord: bool
        :param _Describe: The premium domain description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param _FeeRenew: The price for renewing the premium domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeeRenew: float
        :param _RealPrice: The real price of the domain. For a premium domain, its price varies depending on the period. For a non-premium domain, the price is the 1-year price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealPrice: float
        :param _FeeTransfer: The price for transferring a premium domain in.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FeeTransfer: float
        :param _FeeRestore: The price for redeeming a premium domain.
        :type FeeRestore: float
        :param _Period: The period (in years) of the domain.
        :type Period: int
        :param _ReasonZh: The reason why the domain cannot be registered, expressed in Chinese.
        :type ReasonZh: str
        :param _ResCode: The internal error code.
        :type ResCode: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainName = None
        self._Available = None
        self._Reason = None
        self._Premium = None
        self._Price = None
        self._BlackWord = None
        self._Describe = None
        self._FeeRenew = None
        self._RealPrice = None
        self._FeeTransfer = None
        self._FeeRestore = None
        self._Period = None
        self._ReasonZh = None
        self._ResCode = None
        self._RequestId = None

    @property
    def DomainName(self):
        """The name of the domain checked.
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Available(self):
        """Whether the domain is available for registration.
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Reason(self):
        """The reason why the domain cannot be registered.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Premium(self):
        """Whether the domain is a premium one.
        :rtype: bool
        """
        return self._Premium

    @Premium.setter
    def Premium(self, Premium):
        self._Premium = Premium

    @property
    def Price(self):
        """The domain price.
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def BlackWord(self):
        """Whether the domain name involves restricted words.
        :rtype: bool
        """
        return self._BlackWord

    @BlackWord.setter
    def BlackWord(self, BlackWord):
        self._BlackWord = BlackWord

    @property
    def Describe(self):
        """The premium domain description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def FeeRenew(self):
        """The price for renewing the premium domain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._FeeRenew

    @FeeRenew.setter
    def FeeRenew(self, FeeRenew):
        self._FeeRenew = FeeRenew

    @property
    def RealPrice(self):
        """The real price of the domain. For a premium domain, its price varies depending on the period. For a non-premium domain, the price is the 1-year price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RealPrice

    @RealPrice.setter
    def RealPrice(self, RealPrice):
        self._RealPrice = RealPrice

    @property
    def FeeTransfer(self):
        """The price for transferring a premium domain in.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._FeeTransfer

    @FeeTransfer.setter
    def FeeTransfer(self, FeeTransfer):
        self._FeeTransfer = FeeTransfer

    @property
    def FeeRestore(self):
        """The price for redeeming a premium domain.
        :rtype: float
        """
        return self._FeeRestore

    @FeeRestore.setter
    def FeeRestore(self, FeeRestore):
        self._FeeRestore = FeeRestore

    @property
    def Period(self):
        """The period (in years) of the domain.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReasonZh(self):
        """The reason why the domain cannot be registered, expressed in Chinese.
        :rtype: str
        """
        return self._ReasonZh

    @ReasonZh.setter
    def ReasonZh(self, ReasonZh):
        self._ReasonZh = ReasonZh

    @property
    def ResCode(self):
        """The internal error code.
        :rtype: str
        """
        return self._ResCode

    @ResCode.setter
    def ResCode(self, ResCode):
        self._ResCode = ResCode

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Available = params.get("Available")
        self._Reason = params.get("Reason")
        self._Premium = params.get("Premium")
        self._Price = params.get("Price")
        self._BlackWord = params.get("BlackWord")
        self._Describe = params.get("Describe")
        self._FeeRenew = params.get("FeeRenew")
        self._RealPrice = params.get("RealPrice")
        self._FeeTransfer = params.get("FeeTransfer")
        self._FeeRestore = params.get("FeeRestore")
        self._Period = params.get("Period")
        self._ReasonZh = params.get("ReasonZh")
        self._ResCode = params.get("ResCode")
        self._RequestId = params.get("RequestId")


class CreateIntlDomainBatchRequest(AbstractModel):
    """CreateIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _Period: The purchase period (years) of the domain. Value range: [1-10]
        :type Period: int
        :param _Domains: The domains (maximum 4,000) to purchase.
        :type Domains: list of str
        :param _PayMode: The payment method. Valid values: `0` (online payment), `1` (account balance), `2` (package), `3` (offline settlement).
        :type PayMode: int
        :param _AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        :param _TransferProhibition: Whether to enable the transfer prohibition lock.
        :type TransferProhibition: bool
        :param _UpdateProhibition: Whether to enable the update prohibition lock.
        :type UpdateProhibition: bool
        :param _CustomDns: The custom DNS servers
        :type CustomDns: list of str
        """
        self._TemplateId = None
        self._Period = None
        self._Domains = None
        self._PayMode = None
        self._AutoRenewFlag = None
        self._TransferProhibition = None
        self._UpdateProhibition = None
        self._CustomDns = None

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Period(self):
        """The purchase period (years) of the domain. Value range: [1-10]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Domains(self):
        """The domains (maximum 4,000) to purchase.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def PayMode(self):
        """The payment method. Valid values: `0` (online payment), `1` (account balance), `2` (package), `3` (offline settlement).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        """Whether to enable auto-renewal.
        :rtype: bool
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TransferProhibition(self):
        """Whether to enable the transfer prohibition lock.
        :rtype: bool
        """
        return self._TransferProhibition

    @TransferProhibition.setter
    def TransferProhibition(self, TransferProhibition):
        self._TransferProhibition = TransferProhibition

    @property
    def UpdateProhibition(self):
        """Whether to enable the update prohibition lock.
        :rtype: bool
        """
        return self._UpdateProhibition

    @UpdateProhibition.setter
    def UpdateProhibition(self, UpdateProhibition):
        self._UpdateProhibition = UpdateProhibition

    @property
    def CustomDns(self):
        """The custom DNS servers
        :rtype: list of str
        """
        return self._CustomDns

    @CustomDns.setter
    def CustomDns(self, CustomDns):
        self._CustomDns = CustomDns


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Period = params.get("Period")
        self._Domains = params.get("Domains")
        self._PayMode = params.get("PayMode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TransferProhibition = params.get("TransferProhibition")
        self._UpdateProhibition = params.get("UpdateProhibition")
        self._CustomDns = params.get("CustomDns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlDomainBatchResponse(AbstractModel):
    """CreateIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class CreateIntlPhoneEmailRequest(AbstractModel):
    """CreateIntlPhoneEmail request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param _Code: The mobile number or email address.
        :type Code: str
        :param _VerifyCode: The verification code.
        :type VerifyCode: str
        """
        self._Type = None
        self._Code = None
        self._VerifyCode = None

    @property
    def Type(self):
        """The type. Valid values: `1` (mobile number), `2` (email address).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Code(self):
        """The mobile number or email address.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def VerifyCode(self):
        """The verification code.
        :rtype: str
        """
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Code = params.get("Code")
        self._VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlPhoneEmailResponse(AbstractModel):
    """CreateIntlPhoneEmail response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateIntlTemplateRequest(AbstractModel):
    """CreateIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param _AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param _TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param _BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param _TemplateType: The profile type. Valid values: `I` (individual, default), `E` (organization).
        :type TemplateType: str
        """
        self._RegistrantContact = None
        self._AdminContact = None
        self._TechnicalContact = None
        self._BillingContact = None
        self._TemplateType = None

    @property
    def RegistrantContact(self):
        """The registrant contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        """
        return self._RegistrantContact

    @RegistrantContact.setter
    def RegistrantContact(self, RegistrantContact):
        self._RegistrantContact = RegistrantContact

    @property
    def AdminContact(self):
        """The admin contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        """
        return self._AdminContact

    @AdminContact.setter
    def AdminContact(self, AdminContact):
        self._AdminContact = AdminContact

    @property
    def TechnicalContact(self):
        """The technical contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        """
        return self._TechnicalContact

    @TechnicalContact.setter
    def TechnicalContact(self, TechnicalContact):
        self._TechnicalContact = TechnicalContact

    @property
    def BillingContact(self):
        """The contact person for bills.
        :rtype: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        """
        return self._BillingContact

    @BillingContact.setter
    def BillingContact(self, BillingContact):
        self._BillingContact = BillingContact

    @property
    def TemplateType(self):
        """The profile type. Valid values: `I` (individual, default), `E` (organization).
        :rtype: str
        """
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self._RegistrantContact = RegistrantContact()
            self._RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self._AdminContact = AdminContact()
            self._AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self._TechnicalContact = TechnicalContact()
            self._TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self._BillingContact = BillingContact()
            self._BillingContact._deserialize(params.get("BillingContact"))
        self._TemplateType = params.get("TemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntlTemplateResponse(AbstractModel):
    """CreateIntlTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class DeleteIntlPhoneEmailRequest(AbstractModel):
    """DeleteIntlPhoneEmail request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param _Code: The mobile number or email address.
        :type Code: str
        """
        self._Type = None
        self._Code = None

    @property
    def Type(self):
        """The type. Valid values: `1` (mobile number), `2` (email address).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Code(self):
        """The mobile number or email address.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntlPhoneEmailResponse(AbstractModel):
    """DeleteIntlPhoneEmail response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteIntlTemplateRequest(AbstractModel):
    """DeleteIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The unique ID of the target registrant profile.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """The unique ID of the target registrant profile.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntlTemplateResponse(AbstractModel):
    """DeleteIntlTemplate response structure.

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


class DescribeIntlBatchDetailStatusRequest(AbstractModel):
    """DescribeIntlBatchDetailStatus request structure.

    """

    def __init__(self):
        r"""
        :param _LogIds: The IDs of the logs to be queried.
        :type LogIds: list of int
        """
        self._LogIds = None

    @property
    def LogIds(self):
        """The IDs of the logs to be queried.
        :rtype: list of int
        """
        return self._LogIds

    @LogIds.setter
    def LogIds(self, LogIds):
        self._LogIds = LogIds


    def _deserialize(self, params):
        self._LogIds = params.get("LogIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlBatchDetailStatusResponse(AbstractModel):
    """DescribeIntlBatchDetailStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Details: The details.
        :type Details: list of IntlBatchDetails
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        """The details.
        :rtype: list of IntlBatchDetails
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = IntlBatchDetails()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIntlBatchOperationLogsRequest(AbstractModel):
    """DescribeIntlBatchOperationLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The offset. Default value: 0
        :type Offset: int
        :param _Limit: The number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """The offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlBatchOperationLogsResponse(AbstractModel):
    """DescribeIntlBatchOperationLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _DomainBatchLogSet: The log list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainBatchLogSet: list of BatchDomainBuyLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DomainBatchLogSet = None
        self._RequestId = None

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
    def DomainBatchLogSet(self):
        """The log list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BatchDomainBuyLog
        """
        return self._DomainBatchLogSet

    @DomainBatchLogSet.setter
    def DomainBatchLogSet(self, DomainBatchLogSet):
        self._DomainBatchLogSet = DomainBatchLogSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DomainBatchLogSet") is not None:
            self._DomainBatchLogSet = []
            for item in params.get("DomainBatchLogSet"):
                obj = BatchDomainBuyLog()
                obj._deserialize(item)
                self._DomainBatchLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIntlDomainBatchDetailsRequest(AbstractModel):
    """DescribeIntlDomainBatchDetails request structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _Offset: The offset. Default value: 0
        :type Offset: int
        :param _Limit: The number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _OrderByKey: The sort key. Valid values: `Domain`, `UpdateOn`, `Status`
        :type OrderByKey: str
        :param _OrderBy: Valid values: `0` (ascending), `1` (descending).
        :type OrderBy: int
        """
        self._LogId = None
        self._Offset = None
        self._Limit = None
        self._OrderByKey = None
        self._OrderBy = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def Offset(self):
        """The offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByKey(self):
        """The sort key. Valid values: `Domain`, `UpdateOn`, `Status`
        :rtype: str
        """
        return self._OrderByKey

    @OrderByKey.setter
    def OrderByKey(self, OrderByKey):
        self._OrderByKey = OrderByKey

    @property
    def OrderBy(self):
        """Valid values: `0` (ascending), `1` (descending).
        :rtype: int
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByKey = params.get("OrderByKey")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainBatchDetailsResponse(AbstractModel):
    """DescribeIntlDomainBatchDetails response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _DomainBatchDetailSet: The list of log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainBatchDetailSet: list of BatchDomainBuyDetails
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DomainBatchDetailSet = None
        self._RequestId = None

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
    def DomainBatchDetailSet(self):
        """The list of log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BatchDomainBuyDetails
        """
        return self._DomainBatchDetailSet

    @DomainBatchDetailSet.setter
    def DomainBatchDetailSet(self, DomainBatchDetailSet):
        self._DomainBatchDetailSet = DomainBatchDetailSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DomainBatchDetailSet") is not None:
            self._DomainBatchDetailSet = []
            for item in params.get("DomainBatchDetailSet"):
                obj = BatchDomainBuyDetails()
                obj._deserialize(item)
                self._DomainBatchDetailSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIntlDomainListRequest(AbstractModel):
    """DescribeIntlDomainList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The page number in pagination cases.
        :type Offset: int
        :param _Limit: The number of records on each page in pagination cases.
        :type Limit: int
        :param _KeyWord: The domain keyword for fuzzy search.
        :type KeyWord: str
        :param _OrderByRegTime: The registration time sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByRegTime: int
        :param _OrderByExpireTime: The expiration time sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByExpireTime: int
        :param _Status: The domain status.
`all`: All domains.
`UrgentNeedRenew`: The domains that are in urgent need of renewal.
`RedemptionPending`: The domains that are in urgent need of redemption.
`nosubmit`: The domains with unverified identities.
`tran`: The domains that are being transferred in.
        :type Status: str
        :param _DnsStatus: The DNS type. Valid values: `1` (DNSPod), `2` (others).
        :type DnsStatus: int
        :param _OrderByDomainName: The domain sort order. Valid values: `1` (descending), `2` (ascending).
        :type OrderByDomainName: int
        """
        self._Offset = None
        self._Limit = None
        self._KeyWord = None
        self._OrderByRegTime = None
        self._OrderByExpireTime = None
        self._Status = None
        self._DnsStatus = None
        self._OrderByDomainName = None

    @property
    def Offset(self):
        """The page number in pagination cases.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The number of records on each page in pagination cases.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def KeyWord(self):
        """The domain keyword for fuzzy search.
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def OrderByRegTime(self):
        """The registration time sort order. Valid values: `1` (descending), `2` (ascending).
        :rtype: int
        """
        return self._OrderByRegTime

    @OrderByRegTime.setter
    def OrderByRegTime(self, OrderByRegTime):
        self._OrderByRegTime = OrderByRegTime

    @property
    def OrderByExpireTime(self):
        """The expiration time sort order. Valid values: `1` (descending), `2` (ascending).
        :rtype: int
        """
        return self._OrderByExpireTime

    @OrderByExpireTime.setter
    def OrderByExpireTime(self, OrderByExpireTime):
        self._OrderByExpireTime = OrderByExpireTime

    @property
    def Status(self):
        """The domain status.
`all`: All domains.
`UrgentNeedRenew`: The domains that are in urgent need of renewal.
`RedemptionPending`: The domains that are in urgent need of redemption.
`nosubmit`: The domains with unverified identities.
`tran`: The domains that are being transferred in.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsStatus(self):
        """The DNS type. Valid values: `1` (DNSPod), `2` (others).
        :rtype: int
        """
        return self._DnsStatus

    @DnsStatus.setter
    def DnsStatus(self, DnsStatus):
        self._DnsStatus = DnsStatus

    @property
    def OrderByDomainName(self):
        """The domain sort order. Valid values: `1` (descending), `2` (ascending).
        :rtype: int
        """
        return self._OrderByDomainName

    @OrderByDomainName.setter
    def OrderByDomainName(self, OrderByDomainName):
        self._OrderByDomainName = OrderByDomainName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._KeyWord = params.get("KeyWord")
        self._OrderByRegTime = params.get("OrderByRegTime")
        self._OrderByExpireTime = params.get("OrderByExpireTime")
        self._Status = params.get("Status")
        self._DnsStatus = params.get("DnsStatus")
        self._OrderByDomainName = params.get("OrderByDomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainListResponse(AbstractModel):
    """DescribeIntlDomainList response structure.

    """

    def __init__(self):
        r"""
        :param _DomainSet: The domain information set.
        :type DomainSet: list of IntlDomainInfo
        :param _TotalCount: The total number of domains.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainSet(self):
        """The domain information set.
        :rtype: list of IntlDomainInfo
        """
        return self._DomainSet

    @DomainSet.setter
    def DomainSet(self, DomainSet):
        self._DomainSet = DomainSet

    @property
    def TotalCount(self):
        """The total number of domains.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainSet") is not None:
            self._DomainSet = []
            for item in params.get("DomainSet"):
                obj = IntlDomainInfo()
                obj._deserialize(item)
                self._DomainSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIntlDomainPriceNewListRequest(AbstractModel):
    """DescribeIntlDomainPriceNewList request structure.

    """

    def __init__(self):
        r"""
        :param _TldList: The list of domain suffixes for which you want to query prices. This parameter defaults to all suffixes.
        :type TldList: list of str
        :param _Year: The purchase year of the domains for which you want to query prices. This parameter defaults to all years.
        :type Year: list of int
        :param _Operation: The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :type Operation: list of str
        """
        self._TldList = None
        self._Year = None
        self._Operation = None

    @property
    def TldList(self):
        """The list of domain suffixes for which you want to query prices. This parameter defaults to all suffixes.
        :rtype: list of str
        """
        return self._TldList

    @TldList.setter
    def TldList(self, TldList):
        self._TldList = TldList

    @property
    def Year(self):
        """The purchase year of the domains for which you want to query prices. This parameter defaults to all years.
        :rtype: list of int
        """
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year

    @property
    def Operation(self):
        """The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :rtype: list of str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._TldList = params.get("TldList")
        self._Year = params.get("Year")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainPriceNewListResponse(AbstractModel):
    """DescribeIntlDomainPriceNewList response structure.

    """

    def __init__(self):
        r"""
        :param _PriceList: The price list of domains.
        :type PriceList: list of PriceInfoNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PriceList = None
        self._RequestId = None

    @property
    def PriceList(self):
        """The price list of domains.
        :rtype: list of PriceInfoNew
        """
        return self._PriceList

    @PriceList.setter
    def PriceList(self, PriceList):
        self._PriceList = PriceList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PriceList") is not None:
            self._PriceList = []
            for item in params.get("PriceList"):
                obj = PriceInfoNew()
                obj._deserialize(item)
                self._PriceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIntlDomainRequest(AbstractModel):
    """DescribeIntlDomain request structure.

    """

    def __init__(self):
        r"""
        :param _DomainId: The domain ID.
        :type DomainId: str
        """
        self._DomainId = None

    @property
    def DomainId(self):
        """The domain ID.
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlDomainResponse(AbstractModel):
    """DescribeIntlDomain response structure.

    """

    def __init__(self):
        r"""
        :param _DomainInfo: The domain information.
        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.IntlDomainInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        """The domain information.
        :rtype: :class:`tencentcloud.domain.v20180808.models.IntlDomainInfo`
        """
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = IntlDomainInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class DescribeIntlPhoneEmailListRequest(AbstractModel):
    """DescribeIntlPhoneEmailList request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param _Limit: The number of records on each page in pagination cases.
        :type Limit: int
        :param _Offset: The page number in pagination cases.
        :type Offset: int
        """
        self._Type = None
        self._Limit = None
        self._Offset = None

    @property
    def Type(self):
        """The type. Valid values: `1` (mobile number), `2` (email address).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        """The number of records on each page in pagination cases.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """The page number in pagination cases.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlPhoneEmailListResponse(AbstractModel):
    """DescribeIntlPhoneEmailList response structure.

    """

    def __init__(self):
        r"""
        :param _PhoneEmailList: The list of verified mobile numbers and email addresses.
        :type PhoneEmailList: list of IntlPhoneEmailLists
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PhoneEmailList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PhoneEmailList(self):
        """The list of verified mobile numbers and email addresses.
        :rtype: list of IntlPhoneEmailLists
        """
        return self._PhoneEmailList

    @PhoneEmailList.setter
    def PhoneEmailList(self, PhoneEmailList):
        self._PhoneEmailList = PhoneEmailList

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
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PhoneEmailList") is not None:
            self._PhoneEmailList = []
            for item in params.get("PhoneEmailList"):
                obj = IntlPhoneEmailLists()
                obj._deserialize(item)
                self._PhoneEmailList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIntlTemplateListRequest(AbstractModel):
    """DescribeIntlTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The offset.
        :type Offset: int
        :param _Limit: The maximum number of entries.
        :type Limit: int
        :param _Keyword: The domain registrant keyword for exact match.
        :type Keyword: str
        :param _Type: The type. Valid values: `all` (all types), `I` (individual), `E` (organization).
        :type Type: str
        """
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Type = None

    @property
    def Offset(self):
        """The offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """The maximum number of entries.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        """The domain registrant keyword for exact match.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Type(self):
        """The type. Valid values: `all` (all types), `I` (individual), `E` (organization).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlTemplateListResponse(AbstractModel):
    """DescribeIntlTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateSet: The registrant profile list information.
        :type TemplateSet: list of IntlTemplate
        :param _TotalCount: The total count.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TemplateSet(self):
        """The registrant profile list information.
        :rtype: list of IntlTemplate
        """
        return self._TemplateSet

    @TemplateSet.setter
    def TemplateSet(self, TemplateSet):
        self._TemplateSet = TemplateSet

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
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TemplateSet") is not None:
            self._TemplateSet = []
            for item in params.get("TemplateSet"):
                obj = IntlTemplate()
                obj._deserialize(item)
                self._TemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIntlTemplateRequest(AbstractModel):
    """DescribeIntlTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The unique ID of a registrant profile.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """The unique ID of a registrant profile.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntlTemplateResponse(AbstractModel):
    """DescribeIntlTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Template: The details of the registrant profile.
        :type Template: :class:`tencentcloud.domain.v20180808.models.IntlTemplateInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        """The details of the registrant profile.
        :rtype: :class:`tencentcloud.domain.v20180808.models.IntlTemplateInfo`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = IntlTemplateInfo()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class IntlBatchDetails(AbstractModel):
    """The details of the bulk task

    """

    def __init__(self):
        r"""
        :param _Id: The ID of the bulk task.
        :type Id: int
        :param _Status: The task status.
        :type Status: str
        :param _Reason: The reason.
        :type Reason: str
        :param _ReasonZh: The reason, expressed in Chinese.
        :type ReasonZh: str
        """
        self._Id = None
        self._Status = None
        self._Reason = None
        self._ReasonZh = None

    @property
    def Id(self):
        """The ID of the bulk task.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """The task status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        """The reason.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReasonZh(self):
        """The reason, expressed in Chinese.
        :rtype: str
        """
        return self._ReasonZh

    @ReasonZh.setter
    def ReasonZh(self, ReasonZh):
        self._ReasonZh = ReasonZh


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._ReasonZh = params.get("ReasonZh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlContactInfo(AbstractModel):
    """The contact information.

    """

    def __init__(self):
        r"""
        :param _City: The city name.
        :type City: str
        :param _Country: The country or region name.
        :type Country: str
        :param _Email: The email address.
        :type Email: str
        :param _OrganizationName: The domain registrant.
        :type OrganizationName: str
        :param _Province: The province or state name.
        :type Province: str
        :param _RegistrantName: The name of the registrant.
        :type RegistrantName: str
        :param _RegistrantType: The registrant type. Valid values: `I` (individual), `E` (organization).
        :type RegistrantType: str
        :param _Street: The detailed address.
        :type Street: str
        :param _Telephone: The mobile number.
        :type Telephone: str
        :param _ZipCode: The zip code.
        :type ZipCode: str
        :param _FirstName: The first name.
        :type FirstName: str
        :param _LastName: The last name.
        :type LastName: str
        :param _CompanyName: The company name.
        :type CompanyName: str
        """
        self._City = None
        self._Country = None
        self._Email = None
        self._OrganizationName = None
        self._Province = None
        self._RegistrantName = None
        self._RegistrantType = None
        self._Street = None
        self._Telephone = None
        self._ZipCode = None
        self._FirstName = None
        self._LastName = None
        self._CompanyName = None

    @property
    def City(self):
        """The city name.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """The country or region name.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

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
    def OrganizationName(self):
        """The domain registrant.
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def Province(self):
        """The province or state name.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def RegistrantName(self):
        """The name of the registrant.
        :rtype: str
        """
        return self._RegistrantName

    @RegistrantName.setter
    def RegistrantName(self, RegistrantName):
        self._RegistrantName = RegistrantName

    @property
    def RegistrantType(self):
        """The registrant type. Valid values: `I` (individual), `E` (organization).
        :rtype: str
        """
        return self._RegistrantType

    @RegistrantType.setter
    def RegistrantType(self, RegistrantType):
        self._RegistrantType = RegistrantType

    @property
    def Street(self):
        """The detailed address.
        :rtype: str
        """
        return self._Street

    @Street.setter
    def Street(self, Street):
        self._Street = Street

    @property
    def Telephone(self):
        """The mobile number.
        :rtype: str
        """
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone

    @property
    def ZipCode(self):
        """The zip code.
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

    @property
    def FirstName(self):
        """The first name.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        """The last name.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def CompanyName(self):
        """The company name.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName


    def _deserialize(self, params):
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Email = params.get("Email")
        self._OrganizationName = params.get("OrganizationName")
        self._Province = params.get("Province")
        self._RegistrantName = params.get("RegistrantName")
        self._RegistrantType = params.get("RegistrantType")
        self._Street = params.get("Street")
        self._Telephone = params.get("Telephone")
        self._ZipCode = params.get("ZipCode")
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._CompanyName = params.get("CompanyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlDomainInfo(AbstractModel):
    """The domain information set.

    """

    def __init__(self):
        r"""
        :param _AutoRenew: The auto-renewal flag. Valid values: `0` (disabled by default), `1` (enabled), `2` (disabled).
        :type AutoRenew: int
        :param _CreationDate: The registration time.
        :type CreationDate: str
        :param _DomainId: The domain ID.
        :type DomainId: str
        :param _DnsStatus: The DNS status. Valid values: `1` (DNSPod), `2` (others), `3` (unknown).
        :type DnsStatus: int
        :param _DomainName: The domains.
        :type DomainName: str
        :param _DomainStatus: The domain status.
        :type DomainStatus: list of str
        :param _Status: The purchase status of the domain. Valid values:
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
        :param _ExpirationDate: The expiration date.
        :type ExpirationDate: str
        :param _ExpireMessage: The auto-renewal flag. Valid values: `1` (enabled), `2` (disabled), `3` (disabled by default).
        :type ExpireMessage: int
        :param _IsPremium: Whether the domain is a premium one.
        :type IsPremium: bool
        :param _Dns: The DNS server of the domain.
        :type Dns: list of str
        :param _ContactInfo: The contact information.
        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.IntlContactInfo`
        :param _CanRenewYears: The number of years available for renewal. The value `0` indicates that the domain has reached its maximum validity period (10 years) and cannot be renewed.
        :type CanRenewYears: int
        :param _RegistrarType: The registrar type. If the value is `epp`, the registration time on the page is followed by (UTC). Otherwise, it is followed by (UTC+8).
        :type RegistrarType: str
        :param _Uin: The account to which the domain belongs.
        :type Uin: str
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _SupportDnssec: Whether DNSSEC is supported.
        :type SupportDnssec: bool
        :param _WhoisPrivacy: WHOIS privacy service status. Valid values: `1` (enabled), `2` (disabled), `3` (enabling), `4` (disabling).
        :type WhoisPrivacy: int
        :param _ModifyStatus: Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :type ModifyStatus: str
        :param _DnsModifyStatus: Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :type DnsModifyStatus: str
        """
        self._AutoRenew = None
        self._CreationDate = None
        self._DomainId = None
        self._DnsStatus = None
        self._DomainName = None
        self._DomainStatus = None
        self._Status = None
        self._ExpirationDate = None
        self._ExpireMessage = None
        self._IsPremium = None
        self._Dns = None
        self._ContactInfo = None
        self._CanRenewYears = None
        self._RegistrarType = None
        self._Uin = None
        self._TemplateId = None
        self._SupportDnssec = None
        self._WhoisPrivacy = None
        self._ModifyStatus = None
        self._DnsModifyStatus = None

    @property
    def AutoRenew(self):
        """The auto-renewal flag. Valid values: `0` (disabled by default), `1` (enabled), `2` (disabled).
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def CreationDate(self):
        """The registration time.
        :rtype: str
        """
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate

    @property
    def DomainId(self):
        """The domain ID.
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def DnsStatus(self):
        """The DNS status. Valid values: `1` (DNSPod), `2` (others), `3` (unknown).
        :rtype: int
        """
        return self._DnsStatus

    @DnsStatus.setter
    def DnsStatus(self, DnsStatus):
        self._DnsStatus = DnsStatus

    @property
    def DomainName(self):
        """The domains.
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainStatus(self):
        """The domain status.
        :rtype: list of str
        """
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def Status(self):
        """The purchase status of the domain. Valid values:
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
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpirationDate(self):
        """The expiration date.
        :rtype: str
        """
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def ExpireMessage(self):
        """The auto-renewal flag. Valid values: `1` (enabled), `2` (disabled), `3` (disabled by default).
        :rtype: int
        """
        return self._ExpireMessage

    @ExpireMessage.setter
    def ExpireMessage(self, ExpireMessage):
        self._ExpireMessage = ExpireMessage

    @property
    def IsPremium(self):
        """Whether the domain is a premium one.
        :rtype: bool
        """
        return self._IsPremium

    @IsPremium.setter
    def IsPremium(self, IsPremium):
        self._IsPremium = IsPremium

    @property
    def Dns(self):
        """The DNS server of the domain.
        :rtype: list of str
        """
        return self._Dns

    @Dns.setter
    def Dns(self, Dns):
        self._Dns = Dns

    @property
    def ContactInfo(self):
        """The contact information.
        :rtype: :class:`tencentcloud.domain.v20180808.models.IntlContactInfo`
        """
        return self._ContactInfo

    @ContactInfo.setter
    def ContactInfo(self, ContactInfo):
        self._ContactInfo = ContactInfo

    @property
    def CanRenewYears(self):
        """The number of years available for renewal. The value `0` indicates that the domain has reached its maximum validity period (10 years) and cannot be renewed.
        :rtype: int
        """
        return self._CanRenewYears

    @CanRenewYears.setter
    def CanRenewYears(self, CanRenewYears):
        self._CanRenewYears = CanRenewYears

    @property
    def RegistrarType(self):
        """The registrar type. If the value is `epp`, the registration time on the page is followed by (UTC). Otherwise, it is followed by (UTC+8).
        :rtype: str
        """
        return self._RegistrarType

    @RegistrarType.setter
    def RegistrarType(self, RegistrarType):
        self._RegistrarType = RegistrarType

    @property
    def Uin(self):
        """The account to which the domain belongs.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SupportDnssec(self):
        """Whether DNSSEC is supported.
        :rtype: bool
        """
        return self._SupportDnssec

    @SupportDnssec.setter
    def SupportDnssec(self, SupportDnssec):
        self._SupportDnssec = SupportDnssec

    @property
    def WhoisPrivacy(self):
        """WHOIS privacy service status. Valid values: `1` (enabled), `2` (disabled), `3` (enabling), `4` (disabling).
        :rtype: int
        """
        return self._WhoisPrivacy

    @WhoisPrivacy.setter
    def WhoisPrivacy(self, WhoisPrivacy):
        self._WhoisPrivacy = WhoisPrivacy

    @property
    def ModifyStatus(self):
        """Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :rtype: str
        """
        return self._ModifyStatus

    @ModifyStatus.setter
    def ModifyStatus(self, ModifyStatus):
        self._ModifyStatus = ModifyStatus

    @property
    def DnsModifyStatus(self):
        """Valid values: `NotModify` (not modified), `Modifying`, `Failed` (failed to modify)
        :rtype: str
        """
        return self._DnsModifyStatus

    @DnsModifyStatus.setter
    def DnsModifyStatus(self, DnsModifyStatus):
        self._DnsModifyStatus = DnsModifyStatus


    def _deserialize(self, params):
        self._AutoRenew = params.get("AutoRenew")
        self._CreationDate = params.get("CreationDate")
        self._DomainId = params.get("DomainId")
        self._DnsStatus = params.get("DnsStatus")
        self._DomainName = params.get("DomainName")
        self._DomainStatus = params.get("DomainStatus")
        self._Status = params.get("Status")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ExpireMessage = params.get("ExpireMessage")
        self._IsPremium = params.get("IsPremium")
        self._Dns = params.get("Dns")
        if params.get("ContactInfo") is not None:
            self._ContactInfo = IntlContactInfo()
            self._ContactInfo._deserialize(params.get("ContactInfo"))
        self._CanRenewYears = params.get("CanRenewYears")
        self._RegistrarType = params.get("RegistrarType")
        self._Uin = params.get("Uin")
        self._TemplateId = params.get("TemplateId")
        self._SupportDnssec = params.get("SupportDnssec")
        self._WhoisPrivacy = params.get("WhoisPrivacy")
        self._ModifyStatus = params.get("ModifyStatus")
        self._DnsModifyStatus = params.get("DnsModifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlPhoneEmailLists(AbstractModel):
    """The list of verified mobile numbers and email addresses.

    """

    def __init__(self):
        r"""
        :param _Code: The mobile number or email address.
        :type Code: str
        :param _Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param _CreatedOn: The verification time.
        :type CreatedOn: str
        """
        self._Code = None
        self._Type = None
        self._CreatedOn = None

    @property
    def Code(self):
        """The mobile number or email address.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        """The type. Valid values: `1` (mobile number), `2` (email address).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatedOn(self):
        """The verification time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        self._CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlTemplate(AbstractModel):
    """The details of the registrant profile.

    """

    def __init__(self):
        r"""
        :param _RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param _AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param _TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param _BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param _CreatedOn: The creation time.
        :type CreatedOn: str
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _IsDefault: Whether the profile is the default one.
        :type IsDefault: int
        :param _UpdatedOn: The last update time.
        :type UpdatedOn: str
        """
        self._RegistrantContact = None
        self._AdminContact = None
        self._TechnicalContact = None
        self._BillingContact = None
        self._CreatedOn = None
        self._TemplateId = None
        self._IsDefault = None
        self._UpdatedOn = None

    @property
    def RegistrantContact(self):
        """The registrant contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        """
        return self._RegistrantContact

    @RegistrantContact.setter
    def RegistrantContact(self, RegistrantContact):
        self._RegistrantContact = RegistrantContact

    @property
    def AdminContact(self):
        """The admin contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        """
        return self._AdminContact

    @AdminContact.setter
    def AdminContact(self, AdminContact):
        self._AdminContact = AdminContact

    @property
    def TechnicalContact(self):
        """The technical contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        """
        return self._TechnicalContact

    @TechnicalContact.setter
    def TechnicalContact(self, TechnicalContact):
        self._TechnicalContact = TechnicalContact

    @property
    def BillingContact(self):
        """The contact person for bills.
        :rtype: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        """
        return self._BillingContact

    @BillingContact.setter
    def BillingContact(self, BillingContact):
        self._BillingContact = BillingContact

    @property
    def CreatedOn(self):
        """The creation time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def IsDefault(self):
        """Whether the profile is the default one.
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def UpdatedOn(self):
        """The last update time.
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self._RegistrantContact = RegistrantContact()
            self._RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self._AdminContact = AdminContact()
            self._AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self._TechnicalContact = TechnicalContact()
            self._TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self._BillingContact = BillingContact()
            self._BillingContact._deserialize(params.get("BillingContact"))
        self._CreatedOn = params.get("CreatedOn")
        self._TemplateId = params.get("TemplateId")
        self._IsDefault = params.get("IsDefault")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntlTemplateInfo(AbstractModel):
    """The registrant profile details.

    """

    def __init__(self):
        r"""
        :param _RegistrantContact: The registrant contact.
        :type RegistrantContact: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        :param _AdminContact: The admin contact.
        :type AdminContact: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        :param _TechnicalContact: The technical contact.
        :type TechnicalContact: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        :param _BillingContact: The contact person for bills.
        :type BillingContact: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        :param _CreatedOn: The creation time.
        :type CreatedOn: str
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _TemplateType: The registrant type. Valid values: `I` (individual), `E` (organization).
        :type TemplateType: str
        :param _UpdatedOn: The last updated time.
        :type UpdatedOn: str
        :param _Uin: The account ID.
        :type Uin: str
        :param _IsDefault: Whether the profile is the default one.
        :type IsDefault: int
        """
        self._RegistrantContact = None
        self._AdminContact = None
        self._TechnicalContact = None
        self._BillingContact = None
        self._CreatedOn = None
        self._TemplateId = None
        self._TemplateType = None
        self._UpdatedOn = None
        self._Uin = None
        self._IsDefault = None

    @property
    def RegistrantContact(self):
        """The registrant contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.RegistrantContact`
        """
        return self._RegistrantContact

    @RegistrantContact.setter
    def RegistrantContact(self, RegistrantContact):
        self._RegistrantContact = RegistrantContact

    @property
    def AdminContact(self):
        """The admin contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.AdminContact`
        """
        return self._AdminContact

    @AdminContact.setter
    def AdminContact(self, AdminContact):
        self._AdminContact = AdminContact

    @property
    def TechnicalContact(self):
        """The technical contact.
        :rtype: :class:`tencentcloud.domain.v20180808.models.TechnicalContact`
        """
        return self._TechnicalContact

    @TechnicalContact.setter
    def TechnicalContact(self, TechnicalContact):
        self._TechnicalContact = TechnicalContact

    @property
    def BillingContact(self):
        """The contact person for bills.
        :rtype: :class:`tencentcloud.domain.v20180808.models.BillingContact`
        """
        return self._BillingContact

    @BillingContact.setter
    def BillingContact(self, BillingContact):
        self._BillingContact = BillingContact

    @property
    def CreatedOn(self):
        """The creation time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateType(self):
        """The registrant type. Valid values: `I` (individual), `E` (organization).
        :rtype: str
        """
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def UpdatedOn(self):
        """The last updated time.
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Uin(self):
        """The account ID.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def IsDefault(self):
        """Whether the profile is the default one.
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        if params.get("RegistrantContact") is not None:
            self._RegistrantContact = RegistrantContact()
            self._RegistrantContact._deserialize(params.get("RegistrantContact"))
        if params.get("AdminContact") is not None:
            self._AdminContact = AdminContact()
            self._AdminContact._deserialize(params.get("AdminContact"))
        if params.get("TechnicalContact") is not None:
            self._TechnicalContact = TechnicalContact()
            self._TechnicalContact._deserialize(params.get("TechnicalContact"))
        if params.get("BillingContact") is not None:
            self._BillingContact = BillingContact()
            self._BillingContact._deserialize(params.get("BillingContact"))
        self._CreatedOn = params.get("CreatedOn")
        self._TemplateId = params.get("TemplateId")
        self._TemplateType = params.get("TemplateType")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Uin = params.get("Uin")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnerIntlBatchRequest(AbstractModel):
    """ModifyOwnerIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The domains.
        :type Domains: list of str
        :param _ToUin: The user ID.
        :type ToUin: str
        :param _DnsTransfer: Whether to transfer the DNS service.
        :type DnsTransfer: bool
        """
        self._Domains = None
        self._ToUin = None
        self._DnsTransfer = None

    @property
    def Domains(self):
        """The domains.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ToUin(self):
        """The user ID.
        :rtype: str
        """
        return self._ToUin

    @ToUin.setter
    def ToUin(self, ToUin):
        self._ToUin = ToUin

    @property
    def DnsTransfer(self):
        """Whether to transfer the DNS service.
        :rtype: bool
        """
        return self._DnsTransfer

    @DnsTransfer.setter
    def DnsTransfer(self, DnsTransfer):
        self._DnsTransfer = DnsTransfer


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._ToUin = params.get("ToUin")
        self._DnsTransfer = params.get("DnsTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOwnerIntlBatchResponse(AbstractModel):
    """ModifyOwnerIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The ID of the bulk task.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The ID of the bulk task.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class PriceInfoNew(AbstractModel):
    """The price information of the domains.

    """

    def __init__(self):
        r"""
        :param _Tld: The domain suffix, such as `.com`.
        :type Tld: str
        :param _Year: The purchase years. Value range: [1-10]
        :type Year: int
        :param _Price: The original price of the domain.
        :type Price: float
        :param _RealPrice: The current price of the domain.
        :type RealPrice: float
        :param _Operation: The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :type Operation: str
        :param _Title: The title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Title: str
        """
        self._Tld = None
        self._Year = None
        self._Price = None
        self._RealPrice = None
        self._Operation = None
        self._Title = None

    @property
    def Tld(self):
        """The domain suffix, such as `.com`.
        :rtype: str
        """
        return self._Tld

    @Tld.setter
    def Tld(self, Tld):
        self._Tld = Tld

    @property
    def Year(self):
        """The purchase years. Value range: [1-10]
        :rtype: int
        """
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year

    @property
    def Price(self):
        """The original price of the domain.
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RealPrice(self):
        """The current price of the domain.
        :rtype: float
        """
        return self._RealPrice

    @RealPrice.setter
    def RealPrice(self, RealPrice):
        self._RealPrice = RealPrice

    @property
    def Operation(self):
        """The domain purchase type. Valid values: `new`, `renew`, `redem` (redeem), `tran` (transfer in).
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Title(self):
        """The title.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Tld = params.get("Tld")
        self._Year = params.get("Year")
        self._Price = params.get("Price")
        self._RealPrice = params.get("RealPrice")
        self._Operation = params.get("Operation")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistrantContact(AbstractModel):
    """The registrant contact.

    """

    def __init__(self):
        r"""
        :param _FirstName: The first name.
        :type FirstName: str
        :param _LastName: The last name.
        :type LastName: str
        :param _Country: The country or region name, such as `CN`.
        :type Country: str
        :param _Province: The province or state name.
        :type Province: str
        :param _City: The city name.
        :type City: str
        :param _AddressLine: The address line 1.
        :type AddressLine: str
        :param _ZipCode: The zip code.
        :type ZipCode: str
        :param _Email: The email address.
        :type Email: str
        :param _Phone: The mobile number, such as `+86.1360000000`.
        :type Phone: str
        :param _CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param _JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param _AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param _Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self._FirstName = None
        self._LastName = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._ZipCode = None
        self._Email = None
        self._Phone = None
        self._CompanyName = None
        self._JobTitle = None
        self._AddressLineTwo = None
        self._Fax = None

    @property
    def FirstName(self):
        """The first name.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        """The last name.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Country(self):
        """The country or region name, such as `CN`.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """The province or state name.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city name.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """The address line 1.
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def ZipCode(self):
        """The zip code.
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

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
    def Phone(self):
        """The mobile number, such as `+86.1360000000`.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def CompanyName(self):
        """The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def JobTitle(self):
        """The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobTitle

    @JobTitle.setter
    def JobTitle(self, JobTitle):
        self._JobTitle = JobTitle

    @property
    def AddressLineTwo(self):
        """The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressLineTwo

    @AddressLineTwo.setter
    def AddressLineTwo(self, AddressLineTwo):
        self._AddressLineTwo = AddressLineTwo

    @property
    def Fax(self):
        """The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fax

    @Fax.setter
    def Fax(self, Fax):
        self._Fax = Fax


    def _deserialize(self, params):
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._ZipCode = params.get("ZipCode")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._CompanyName = params.get("CompanyName")
        self._JobTitle = params.get("JobTitle")
        self._AddressLineTwo = params.get("AddressLineTwo")
        self._Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewIntlDomainBatchRequest(AbstractModel):
    """RenewIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The domains to check.
        :type Domains: list of str
        :param _Period: The period (1 to 10 years). If this parameter is left empty, premium domains cannot be checked.
        :type Period: int
        :param _PayMode: Payment method. Valid value: `1` (account balance).
        :type PayMode: int
        :param _AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        """
        self._Domains = None
        self._Period = None
        self._PayMode = None
        self._AutoRenewFlag = None

    @property
    def Domains(self):
        """The domains to check.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Period(self):
        """The period (1 to 10 years). If this parameter is left empty, premium domains cannot be checked.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PayMode(self):
        """Payment method. Valid value: `1` (account balance).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        """Whether to enable auto-renewal.
        :rtype: bool
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._Period = params.get("Period")
        self._PayMode = params.get("PayMode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewIntlDomainBatchResponse(AbstractModel):
    """RenewIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The ID of the bulk task.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The ID of the bulk task.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class SendIntlPhoneEmailCodeRequest(AbstractModel):
    """SendIntlPhoneEmailCode request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The type. Valid values: `1` (mobile number), `2` (email address).
        :type Type: int
        :param _Code: The mobile number or email address.
        :type Code: str
        """
        self._Type = None
        self._Code = None

    @property
    def Type(self):
        """The type. Valid values: `1` (mobile number), `2` (email address).
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Code(self):
        """The mobile number or email address.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendIntlPhoneEmailCodeResponse(AbstractModel):
    """SendIntlPhoneEmailCode response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetIntlDomainAutoRenewRequest(AbstractModel):
    """SetIntlDomainAutoRenew request structure.

    """

    def __init__(self):
        r"""
        :param _DomainId: The domain ID.
        :type DomainId: str
        :param _AutoRenew: Whether to enable auto-renewal. Valid values: `1` (enable), `2` (disable).
        :type AutoRenew: int
        """
        self._DomainId = None
        self._AutoRenew = None

    @property
    def DomainId(self):
        """The domain ID.
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def AutoRenew(self):
        """Whether to enable auto-renewal. Valid values: `1` (enable), `2` (disable).
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetIntlDomainAutoRenewResponse(AbstractModel):
    """SetIntlDomainAutoRenew response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TechnicalContact(AbstractModel):
    """The technical contact.

    """

    def __init__(self):
        r"""
        :param _FirstName: The first name.
        :type FirstName: str
        :param _LastName: The last name.
        :type LastName: str
        :param _Country: The country or region name, such as `CN`.
        :type Country: str
        :param _Province: The province or state name.
        :type Province: str
        :param _City: The city name.
        :type City: str
        :param _AddressLine: The address line 1.
        :type AddressLine: str
        :param _ZipCode: The zip code.
        :type ZipCode: str
        :param _Email: The email address.
        :type Email: str
        :param _Phone: The mobile number, such as `+86.13600000000`.
        :type Phone: str
        :param _CompanyName: The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompanyName: str
        :param _JobTitle: The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobTitle: str
        :param _AddressLineTwo: The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddressLineTwo: str
        :param _Fax: The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fax: str
        """
        self._FirstName = None
        self._LastName = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AddressLine = None
        self._ZipCode = None
        self._Email = None
        self._Phone = None
        self._CompanyName = None
        self._JobTitle = None
        self._AddressLineTwo = None
        self._Fax = None

    @property
    def FirstName(self):
        """The first name.
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        """The last name.
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Country(self):
        """The country or region name, such as `CN`.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """The province or state name.
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """The city name.
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AddressLine(self):
        """The address line 1.
        :rtype: str
        """
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, AddressLine):
        self._AddressLine = AddressLine

    @property
    def ZipCode(self):
        """The zip code.
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

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
    def Phone(self):
        """The mobile number, such as `+86.13600000000`.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def CompanyName(self):
        """The company or organization name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def JobTitle(self):
        """The job title.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobTitle

    @JobTitle.setter
    def JobTitle(self, JobTitle):
        self._JobTitle = JobTitle

    @property
    def AddressLineTwo(self):
        """The address line 2.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressLineTwo

    @AddressLineTwo.setter
    def AddressLineTwo(self, AddressLineTwo):
        self._AddressLineTwo = AddressLineTwo

    @property
    def Fax(self):
        """The fax number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fax

    @Fax.setter
    def Fax(self, Fax):
        self._Fax = Fax


    def _deserialize(self, params):
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AddressLine = params.get("AddressLine")
        self._ZipCode = params.get("ZipCode")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._CompanyName = params.get("CompanyName")
        self._JobTitle = params.get("JobTitle")
        self._AddressLineTwo = params.get("AddressLineTwo")
        self._Fax = params.get("Fax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInIntlDomainBatchRequest(AbstractModel):
    """TransferInIntlDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The profile ID.
        :type TemplateId: str
        :param _PassWords: The transfer passwords for the domains.
        :type PassWords: list of str
        :param _Domains: The domains to be bulk transferred in.
        :type Domains: list of str
        :param _PayMode: The payment method. Valid value: `1` (account balance).
        :type PayMode: int
        :param _AutoRenewFlag: Whether to enable auto-renewal.
        :type AutoRenewFlag: bool
        :param _TransferProhibition: Whether to enable the transfer prohibition lock.
        :type TransferProhibition: bool
        :param _UpdateProhibition: Whether to enable the update prohibition lock.
        :type UpdateProhibition: bool
        :param _LockTransfer: Whether to enable the 60-day inter-registrar transfer lock.
        :type LockTransfer: bool
        """
        self._TemplateId = None
        self._PassWords = None
        self._Domains = None
        self._PayMode = None
        self._AutoRenewFlag = None
        self._TransferProhibition = None
        self._UpdateProhibition = None
        self._LockTransfer = None

    @property
    def TemplateId(self):
        """The profile ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def PassWords(self):
        """The transfer passwords for the domains.
        :rtype: list of str
        """
        return self._PassWords

    @PassWords.setter
    def PassWords(self, PassWords):
        self._PassWords = PassWords

    @property
    def Domains(self):
        """The domains to be bulk transferred in.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def PayMode(self):
        """The payment method. Valid value: `1` (account balance).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AutoRenewFlag(self):
        """Whether to enable auto-renewal.
        :rtype: bool
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TransferProhibition(self):
        """Whether to enable the transfer prohibition lock.
        :rtype: bool
        """
        return self._TransferProhibition

    @TransferProhibition.setter
    def TransferProhibition(self, TransferProhibition):
        self._TransferProhibition = TransferProhibition

    @property
    def UpdateProhibition(self):
        """Whether to enable the update prohibition lock.
        :rtype: bool
        """
        return self._UpdateProhibition

    @UpdateProhibition.setter
    def UpdateProhibition(self, UpdateProhibition):
        self._UpdateProhibition = UpdateProhibition

    @property
    def LockTransfer(self):
        """Whether to enable the 60-day inter-registrar transfer lock.
        :rtype: bool
        """
        return self._LockTransfer

    @LockTransfer.setter
    def LockTransfer(self, LockTransfer):
        self._LockTransfer = LockTransfer


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._PassWords = params.get("PassWords")
        self._Domains = params.get("Domains")
        self._PayMode = params.get("PayMode")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TransferProhibition = params.get("TransferProhibition")
        self._UpdateProhibition = params.get("UpdateProhibition")
        self._LockTransfer = params.get("LockTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInIntlDomainBatchResponse(AbstractModel):
    """TransferInIntlDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The bulk purchase log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class TransferProhibitionIntlBatchRequest(AbstractModel):
    """TransferProhibitionIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The domain array.
        :type Domains: list of str
        :param _Status: Whether to enable transfer prohibition. Valid values: `true` (enable), `false` (disable).
        :type Status: bool
        """
        self._Domains = None
        self._Status = None

    @property
    def Domains(self):
        """The domain array.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Status(self):
        """Whether to enable transfer prohibition. Valid values: `true` (enable), `false` (disable).
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferProhibitionIntlBatchResponse(AbstractModel):
    """TransferProhibitionIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")


class UpdateProhibitionIntlBatchRequest(AbstractModel):
    """UpdateProhibitionIntlBatch request structure.

    """

    def __init__(self):
        r"""
        :param _Domains: The domain array.
        :type Domains: list of str
        :param _Status: Whether to enable update prohibition. Valid values: `true` (enable), `false` (disable).
        :type Status: bool
        """
        self._Domains = None
        self._Status = None

    @property
    def Domains(self):
        """The domain array.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Status(self):
        """Whether to enable update prohibition. Valid values: `true` (enable), `false` (disable).
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProhibitionIntlBatchResponse(AbstractModel):
    """UpdateProhibitionIntlBatch response structure.

    """

    def __init__(self):
        r"""
        :param _LogId: The log ID.
        :type LogId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogId = None
        self._RequestId = None

    @property
    def LogId(self):
        """The log ID.
        :rtype: int
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogId = params.get("LogId")
        self._RequestId = params.get("RequestId")