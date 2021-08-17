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
        :param CountryCode: Country code, which can be obtained via the `GetCountryCodes` API, such as `86`.
        :type CountryCode: str
        :param Area: ISO2 standard country code, which can be obtained via the `GetCountryCodes` API. It should correspond to the `CountryCode` field.
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