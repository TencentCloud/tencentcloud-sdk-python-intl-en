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
        :param _AddedCredit: Specific value of the credit allocated to the customer
        :type AddedCredit: float
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        """
        self._AddedCredit = None
        self._ClientUin = None

    @property
    def AddedCredit(self):
        return self._AddedCredit

    @AddedCredit.setter
    def AddedCredit(self, AddedCredit):
        self._AddedCredit = AddedCredit

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin


    def _deserialize(self, params):
        self._AddedCredit = params.get("AddedCredit")
        self._ClientUin = params.get("ClientUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateCustomerCreditResponse(AbstractModel):
    """AllocateCustomerCredit response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCredit: The updated total credit
        :type TotalCredit: float
        :param _RemainingCredit: The updated available credit
        :type RemainingCredit: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCredit = None
        self._RemainingCredit = None
        self._RequestId = None

    @property
    def TotalCredit(self):
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._RequestId = params.get("RequestId")


class CountryCodeItem(AbstractModel):
    """Country/region code list

    """

    def __init__(self):
        r"""
        :param _EnName: Country/region name in English
        :type EnName: str
        :param _Name: Country/region name in Chinese
        :type Name: str
        :param _IOS2: IOS2 standard country/region code
        :type IOS2: str
        :param _IOS3: IOS3 standard country/region code
        :type IOS3: str
        :param _Code: Phone code
        :type Code: str
        """
        self._EnName = None
        self._Name = None
        self._IOS2 = None
        self._IOS3 = None
        self._Code = None

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IOS2(self):
        return self._IOS2

    @IOS2.setter
    def IOS2(self, IOS2):
        self._IOS2 = IOS2

    @property
    def IOS3(self):
        return self._IOS3

    @IOS3.setter
    def IOS3(self, IOS3):
        self._IOS3 = IOS3

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._EnName = params.get("EnName")
        self._Name = params.get("Name")
        self._IOS2 = params.get("IOS2")
        self._IOS3 = params.get("IOS3")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        r"""
        :param _AccountType: Account type of a new customer. Valid values: `personal`, `company`.
        :type AccountType: str
        :param _Mail: Registered email address, which should be valid and correct.
For example, account@qq.com.
        :type Mail: str
        :param _Password: Account password
Length limit: 8-20 characters
A password must contain numbers, letters, and special symbols [!@#$%^&*()]. Spaces are not allowed.
        :type Password: str
        :param _ConfirmPassword: Confirm the password. It must be the same as the `Password` field.
        :type ConfirmPassword: str
        :param _PhoneNum: Customer mobile number, which should be valid and correct.
A global mobile number within 1-32 digits is allowed, such as 18888888888.
        :type PhoneNum: str
        :param _CountryCode: Customer’s country/region code, which can be obtained via the `GetCountryCodes` API, such as “852”.
        :type CountryCode: str
        :param _Area: Customer’s ISO2 standard country/region code, which can be obtained via the `GetCountryCodes` API. It should correspond to the `CountryCode` field, such as `HK`.
        :type Area: str
        :param _Extended: Expanded field, which is left empty by default.
        :type Extended: str
        """
        self._AccountType = None
        self._Mail = None
        self._Password = None
        self._ConfirmPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Area = None
        self._Extended = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ConfirmPassword(self):
        return self._ConfirmPassword

    @ConfirmPassword.setter
    def ConfirmPassword(self, ConfirmPassword):
        self._ConfirmPassword = ConfirmPassword

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Extended(self):
        return self._Extended

    @Extended.setter
    def Extended(self, Extended):
        self._Extended = Extended


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Mail = params.get("Mail")
        self._Password = params.get("Password")
        self._ConfirmPassword = params.get("ConfirmPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Area = params.get("Area")
        self._Extended = params.get("Extended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Account UIN
        :type Uin: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class GetCountryCodesRequest(AbstractModel):
    """GetCountryCodes request structure.

    """


class GetCountryCodesResponse(AbstractModel):
    """GetCountryCodes response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of country/region codes
        :type Data: list of CountryCodeItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CountryCodeItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCreditAllocationHistoryData(AbstractModel):
    """Returned information for querying the credit allocation records of reseller’s customer

    """

    def __init__(self):
        r"""
        :param _AllocatedTime: Allocation time
        :type AllocatedTime: str
        :param _Operator: Operator
        :type Operator: str
        :param _Credit: Allocated credit value
        :type Credit: float
        :param _AllocatedCredit: The allocated total credit
        :type AllocatedCredit: float
        """
        self._AllocatedTime = None
        self._Operator = None
        self._Credit = None
        self._AllocatedCredit = None

    @property
    def AllocatedTime(self):
        return self._AllocatedTime

    @AllocatedTime.setter
    def AllocatedTime(self, AllocatedTime):
        self._AllocatedTime = AllocatedTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Credit(self):
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def AllocatedCredit(self):
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit


    def _deserialize(self, params):
        self._AllocatedTime = params.get("AllocatedTime")
        self._Operator = params.get("Operator")
        self._Credit = params.get("Credit")
        self._AllocatedCredit = params.get("AllocatedCredit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryRequest(AbstractModel):
    """QueryCreditAllocationHistory request structure.

    """

    def __init__(self):
        r"""
        :param _ClientUin: Customer UIN
        :type ClientUin: int
        :param _Page: Page number
        :type Page: int
        :param _PageSize: Number of data entries per page
        :type PageSize: int
        """
        self._ClientUin = None
        self._Page = None
        self._PageSize = None

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ClientUin = params.get("ClientUin")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCreditAllocationHistoryResponse(AbstractModel):
    """QueryCreditAllocationHistory response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of records
Note: this field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _History: List of record details
Note: this field may return null, indicating that no valid values can be obtained.
        :type History: list of QueryCreditAllocationHistoryData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._History = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def History(self):
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("History") is not None:
            self._History = []
            for item in params.get("History"):
                obj = QueryCreditAllocationHistoryData()
                obj._deserialize(item)
                self._History.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCustomersCreditData(AbstractModel):
    """Complex type of output parameters for querying customer's credit

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Type: Type
        :type Type: str
        :param _Mobile: Phone
        :type Mobile: str
        :param _Email: Email
        :type Email: str
        :param _Arrears: Overdue payment flag
        :type Arrears: str
        :param _AssociationTime: Binding time
        :type AssociationTime: str
        :param _RecentExpiry: Expiration time
        :type RecentExpiry: str
        :param _ClientUin: The UIN of reseller’s customer
        :type ClientUin: int
        :param _Credit: Credit granted to reseller’s customer
        :type Credit: float
        :param _RemainingCredit: The remaining credit of reseller’s customer
        :type RemainingCredit: float
        :param _IdentifyType: 0: Identity not verified; 1: Individual identity verified; 2: Enterprise identity verified.
        :type IdentifyType: int
        :param _Remark: Customer remarks
        :type Remark: str
        :param _Force: Forced status
        :type Force: int
        """
        self._Name = None
        self._Type = None
        self._Mobile = None
        self._Email = None
        self._Arrears = None
        self._AssociationTime = None
        self._RecentExpiry = None
        self._ClientUin = None
        self._Credit = None
        self._RemainingCredit = None
        self._IdentifyType = None
        self._Remark = None
        self._Force = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Arrears(self):
        return self._Arrears

    @Arrears.setter
    def Arrears(self, Arrears):
        self._Arrears = Arrears

    @property
    def AssociationTime(self):
        return self._AssociationTime

    @AssociationTime.setter
    def AssociationTime(self, AssociationTime):
        self._AssociationTime = AssociationTime

    @property
    def RecentExpiry(self):
        return self._RecentExpiry

    @RecentExpiry.setter
    def RecentExpiry(self, RecentExpiry):
        self._RecentExpiry = RecentExpiry

    @property
    def ClientUin(self):
        return self._ClientUin

    @ClientUin.setter
    def ClientUin(self, ClientUin):
        self._ClientUin = ClientUin

    @property
    def Credit(self):
        return self._Credit

    @Credit.setter
    def Credit(self, Credit):
        self._Credit = Credit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def IdentifyType(self):
        return self._IdentifyType

    @IdentifyType.setter
    def IdentifyType(self, IdentifyType):
        self._IdentifyType = IdentifyType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._Arrears = params.get("Arrears")
        self._AssociationTime = params.get("AssociationTime")
        self._RecentExpiry = params.get("RecentExpiry")
        self._ClientUin = params.get("ClientUin")
        self._Credit = params.get("Credit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._IdentifyType = params.get("IdentifyType")
        self._Remark = params.get("Remark")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditRequest(AbstractModel):
    """QueryCustomersCredit request structure.

    """

    def __init__(self):
        r"""
        :param _FilterType: Search condition type. You can only search by UIN, name, or remarks.
        :type FilterType: str
        :param _Filter: Search condition
        :type Filter: str
        :param _Page: A pagination parameter that specifies the current page number, with a value starting from 1.
        :type Page: int
        :param _PageSize: A pagination parameter that specifies the number of entries per page.
        :type PageSize: int
        :param _Order: A sort parameter that specifies the sort order. Valid values: `desc` (descending order), or `asc` (ascending order) based on `AssociationTime`. The value will be `desc` if left empty.
        :type Order: str
        """
        self._FilterType = None
        self._Filter = None
        self._Page = None
        self._PageSize = None
        self._Order = None

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Filter = params.get("Filter")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomersCreditResponse(AbstractModel):
    """QueryCustomersCredit response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Queries the list of customers
Note: this field may return null, indicating that no valid values can be obtained.
        :type Data: list of QueryCustomersCreditData
        :param _Total: Number of customers
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QueryCustomersCreditData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class QueryPartnerCreditRequest(AbstractModel):
    """QueryPartnerCredit request structure.

    """


class QueryPartnerCreditResponse(AbstractModel):
    """QueryPartnerCredit response structure.

    """

    def __init__(self):
        r"""
        :param _AllocatedCredit: Allocated credit
        :type AllocatedCredit: float
        :param _TotalCredit: Total credit
        :type TotalCredit: float
        :param _RemainingCredit: Remaining credit
        :type RemainingCredit: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllocatedCredit = None
        self._TotalCredit = None
        self._RemainingCredit = None
        self._RequestId = None

    @property
    def AllocatedCredit(self):
        return self._AllocatedCredit

    @AllocatedCredit.setter
    def AllocatedCredit(self, AllocatedCredit):
        self._AllocatedCredit = AllocatedCredit

    @property
    def TotalCredit(self):
        return self._TotalCredit

    @TotalCredit.setter
    def TotalCredit(self, TotalCredit):
        self._TotalCredit = TotalCredit

    @property
    def RemainingCredit(self):
        return self._RemainingCredit

    @RemainingCredit.setter
    def RemainingCredit(self, RemainingCredit):
        self._RemainingCredit = RemainingCredit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllocatedCredit = params.get("AllocatedCredit")
        self._TotalCredit = params.get("TotalCredit")
        self._RemainingCredit = params.get("RemainingCredit")
        self._RequestId = params.get("RequestId")