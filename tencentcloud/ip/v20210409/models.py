# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CountryCodeItem(AbstractModel):
    """Get an element type of the country code interface

    """

    def __init__(self):
        """
        :param EnName: Country English Name
        :type EnName: str
        :param Name: Country Chinese Name
        :type Name: str
        :param IOS2: IOS2 standard country/region code
        :type IOS2: str
        :param IOS3: IOS3 standard country/region code
        :type IOS3: str
        :param Code: Phone Code
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


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        """
        :param AccountType: The account type identification of the newly created customer. The value of this interface is: business
        :type AccountType: str
        :param Mail: Registered email address. The caller needs to ensure the validity and correctness of the email address.
The email format must be met. For example: account@qq.com
        :type Mail: str
        :param Password: Account password.
Length limit: [8,20].
It must also contain numbers, letters and special symbols (!@#$%^&*() and other non-spaces)
        :type Password: str
        :param ConfirmPassword: Reconfirm the password. It must be the same as the Password value
        :type ConfirmPassword: str
        :param PhoneNum: Customer's mobile phone number. The caller is required to ensure the validity and correctness of the mobile phone number.
Length limit: [1,32]. Global mobile phone numbers are supported. For example, 18888888888
        :type PhoneNum: str
        :param CountryCode: The country code of the customer. For the value, please refer to the GetCountryCodes interface GetCountryCodes. Such as 86
        :type CountryCode: str
        :param Area: Customer's IOS2 standard country code. Refer to the GetCountryCodes interface for obtaining country codes. It needs to correspond to the CountryCode value. Such as CN
        :type Area: str
        :param Extended: Extension field, default is empty
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


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        """
        :param Uin: The uin of the account
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
        """
        :param Data: List of Country Codes
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