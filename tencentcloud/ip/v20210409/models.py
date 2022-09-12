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


class AllocateCustomerCreditRequest(AbstractModel):
    """AllocateCustomerCredit request structure.

    """

    def __init__(self):
        r"""
        :param AddedCredit: Specific value of the credit allocated to the customer
        :type AddedCredit: float
        :param ClientUin: Customer UIN
        :type ClientUin: int
        """
        self.AddedCredit = None
        self.ClientUin = None


    def _deserialize(self, params):
        self.AddedCredit = params.get("AddedCredit")
        self.ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCustomerCreditResponse(AbstractModel):
    """AllocateCustomerCredit response structure.

    """

    def __init__(self):
        r"""
        :param TotalCredit: The updated total credit
        :type TotalCredit: float
        :param RemainingCredit: The updated available credit
        :type RemainingCredit: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCredit = None
        self.RemainingCredit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCredit = params.get("TotalCredit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.RequestId = params.get("RequestId")


class CountryCodeItem(AbstractModel):
    """Country/region code list

    """

    def __init__(self):
        r"""
        :param EnName: Country/region name in English
        :type EnName: str
        :param Name: Country/region name in Chinese
        :type Name: str
        :param IOS2: IOS2 standard country/region code
        :type IOS2: str
        :param IOS3: IOS3 standard country/region code
        :type IOS3: str
        :param Code: Phone code
        :type Code: str
        """
        self.EnName = None
        self.Name = None
        self.IOS2 = None
        self.IOS3 = None
        self.Code = None


    def _deserialize(self, params):
        self.EnName = params.get("EnName")
        self.Name = params.get("Name")
        self.IOS2 = params.get("IOS2")
        self.IOS3 = params.get("IOS3")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param AccountType: Account type of a new customer. Valid value: `business`.
        :type AccountType: str
        :param Mail: Registered email address, which should be valid and correct.
For example, account@qq.com.
        :type Mail: str
        :param Password: Account password
Length limit: 8-20 characters
A password must contain numbers, letters, and special symbols [!@#$%^&*()]. Spaces are not allowed.
        :type Password: str
        :param ConfirmPassword: Confirm the password. It must be the same as the `Password` field.
        :type ConfirmPassword: str
        :param PhoneNum: Customer mobile number, which should be valid and correct.
A global mobile number within 1-32 digits is allowed, such as 18888888888.
        :type PhoneNum: str
        :param CountryCode: Customer’s country/region code, which can be obtained via the `GetCountryCodes` API, such as “852”.
        :type CountryCode: str
        :param Area: Customer’s ISO2 standard country/region code, which can be obtained via the `GetCountryCodes` API. It should correspond to the `CountryCode` field, such as `HK`.
        :type Area: str
        :param Extended: Expanded field, which is left empty by default.
        :type Extended: str
        """
        self.AccountType = None
        self.Mail = None
        self.Password = None
        self.ConfirmPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Area = None
        self.Extended = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Mail = params.get("Mail")
        self.Password = params.get("Password")
        self.ConfirmPassword = params.get("ConfirmPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Area = params.get("Area")
        self.Extended = params.get("Extended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Account UIN
        :type Uin: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetCountryCodesRequest(AbstractModel):
    """GetCountryCodes request structure.

    """


class GetCountryCodesResponse(AbstractModel):
    """GetCountryCodes response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of country/region codes
        :type Data: list of CountryCodeItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CountryCodeItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCreditAllocationHistoryData(AbstractModel):
    """Returned information for querying the credit allocation records of reseller’s customer

    """

    def __init__(self):
        r"""
        :param AllocatedTime: Allocation time
        :type AllocatedTime: str
        :param Operator: Operator
        :type Operator: str
        :param Credit: Allocated credit value
        :type Credit: float
        :param AllocatedCredit: The allocated total credit
        :type AllocatedCredit: float
        """
        self.AllocatedTime = None
        self.Operator = None
        self.Credit = None
        self.AllocatedCredit = None


    def _deserialize(self, params):
        self.AllocatedTime = params.get("AllocatedTime")
        self.Operator = params.get("Operator")
        self.Credit = params.get("Credit")
        self.AllocatedCredit = params.get("AllocatedCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryRequest(AbstractModel):
    """QueryCreditAllocationHistory request structure.

    """

    def __init__(self):
        r"""
        :param ClientUin: Customer UIN
        :type ClientUin: int
        :param Page: Page number
        :type Page: int
        :param PageSize: Number of data entries per page
        :type PageSize: int
        """
        self.ClientUin = None
        self.Page = None
        self.PageSize = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.Page = params.get("Page")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryResponse(AbstractModel):
    """QueryCreditAllocationHistory response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number of records
Note: this field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param History: List of record details
Note: this field may return null, indicating that no valid values can be obtained.
        :type History: list of QueryCreditAllocationHistoryData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.History = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = QueryCreditAllocationHistoryData()
                obj._deserialize(item)
                self.History.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCustomersCreditData(AbstractModel):
    """Complex type of output parameters for querying customer's credit

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param Type: Type
        :type Type: str
        :param Mobile: Phone
        :type Mobile: str
        :param Email: Email
        :type Email: str
        :param Arrears: Overdue payment flag
        :type Arrears: str
        :param AssociationTime: Binding time
        :type AssociationTime: str
        :param RecentExpiry: Expiration time
        :type RecentExpiry: str
        :param ClientUin: The UIN of reseller’s customer
        :type ClientUin: int
        :param Credit: Credit granted to reseller’s customer
        :type Credit: float
        :param RemainingCredit: The remaining credit of reseller’s customer
        :type RemainingCredit: float
        :param IdentifyType: 0: Identity not verified; 1: Individual identity verified; 2: Enterprise identity verified.
        :type IdentifyType: int
        :param Remark: Customer remarks
        :type Remark: str
        :param Force: Forced status
        :type Force: int
        """
        self.Name = None
        self.Type = None
        self.Mobile = None
        self.Email = None
        self.Arrears = None
        self.AssociationTime = None
        self.RecentExpiry = None
        self.ClientUin = None
        self.Credit = None
        self.RemainingCredit = None
        self.IdentifyType = None
        self.Remark = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.Arrears = params.get("Arrears")
        self.AssociationTime = params.get("AssociationTime")
        self.RecentExpiry = params.get("RecentExpiry")
        self.ClientUin = params.get("ClientUin")
        self.Credit = params.get("Credit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.IdentifyType = params.get("IdentifyType")
        self.Remark = params.get("Remark")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditRequest(AbstractModel):
    """QueryCustomersCredit request structure.

    """

    def __init__(self):
        r"""
        :param FilterType: Search condition type. You can only search by UIN, name, or remarks.
        :type FilterType: str
        :param Filter: Search condition
        :type Filter: str
        :param Page: A pagination parameter that specifies the current page number, with a value starting from 1.
        :type Page: int
        :param PageSize: A pagination parameter that specifies the number of entries per page.
        :type PageSize: int
        :param Order: A sort parameter that specifies the sort order. Valid values: `desc` (descending order), or `asc` (ascending order) based on `AssociationTime`. The value will be `desc` if left empty.
        :type Order: str
        """
        self.FilterType = None
        self.Filter = None
        self.Page = None
        self.PageSize = None
        self.Order = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Filter = params.get("Filter")
        self.Page = params.get("Page")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditResponse(AbstractModel):
    """QueryCustomersCredit response structure.

    """

    def __init__(self):
        r"""
        :param Data: Queries the list of customers
Note: this field may return null, indicating that no valid values can be obtained.
        :type Data: list of QueryCustomersCreditData
        :param Total: Number of customers
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryCustomersCreditData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class QueryPartnerCreditRequest(AbstractModel):
    """QueryPartnerCredit request structure.

    """


class QueryPartnerCreditResponse(AbstractModel):
    """QueryPartnerCredit response structure.

    """

    def __init__(self):
        r"""
        :param AllocatedCredit: Allocated credit
        :type AllocatedCredit: float
        :param TotalCredit: Total credit
        :type TotalCredit: float
        :param RemainingCredit: Remaining credit
        :type RemainingCredit: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllocatedCredit = None
        self.TotalCredit = None
        self.RemainingCredit = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllocatedCredit = params.get("AllocatedCredit")
        self.TotalCredit = params.get("TotalCredit")
        self.RemainingCredit = params.get("RemainingCredit")
        self.RequestId = params.get("RequestId")