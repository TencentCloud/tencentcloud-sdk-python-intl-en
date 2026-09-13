# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AddPromotionEvent(AbstractModel):
    r"""AddPromotion event details

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _Coupon: <p>The coupon associated with the promotion</p>
        :type Coupon: :class:`tencentcloud.rce.v20260130.models.Coupon`
        :param _Point: <p>The point associated with the promotion</p>
        :type Point: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        :param _Result: <p>The result of participating the promotion</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131***85678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Coupon = None
        self._Point = None
        self._Result = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Coupon(self):
        r"""<p>The coupon associated with the promotion</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Coupon`
        """
        return self._Coupon

    @Coupon.setter
    def Coupon(self, Coupon):
        self._Coupon = Coupon

    @property
    def Point(self):
        r"""<p>The point associated with the promotion</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._Point

    @Point.setter
    def Point(self, Point):
        self._Point = Point

    @property
    def Result(self):
        r"""<p>The result of participating the promotion</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131***85678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Coupon") is not None:
            self._Coupon = Coupon()
            self._Coupon._deserialize(params.get("Coupon"))
        if params.get("Point") is not None:
            self._Point = CreditPoint()
            self._Point._deserialize(params.get("Point"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Address(AbstractModel):
    r"""Address

    """

    def __init__(self):
        r"""
        :param _Country: <p>Country</p><p>Parameter format: Compliant with the ISO 3166 standard</p>
        :type Country: str
        :param _Region: <p>Province</p>
        :type Region: str
        :param _City: <p>City</p>
        :type City: str
        :param _District: <p>Region</p>
        :type District: str
        :param _Detail: <p>Detailed address</p>
        :type Detail: str
        :param _ZipCode: <p>Postal code</p>
        :type ZipCode: str
        """
        self._Country = None
        self._Region = None
        self._City = None
        self._District = None
        self._Detail = None
        self._ZipCode = None

    @property
    def Country(self):
        r"""<p>Country</p><p>Parameter format: Compliant with the ISO 3166 standard</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Region(self):
        r"""<p>Province</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def City(self):
        r"""<p>City</p>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""<p>Region</p>
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Detail(self):
        r"""<p>Detailed address</p>
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def ZipCode(self):
        r"""<p>Postal code</p>
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._Region = params.get("Region")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Detail = params.get("Detail")
        self._ZipCode = params.get("ZipCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Amount(AbstractModel):
    r"""Amount

    """

    def __init__(self):
        r"""
        :param _Currency: <p>Currency code</p><p>Parameter format: Compliant with the ISO 4217 standard</p>
        :type Currency: str
        :param _OriginalAmount: <p>Original amount in currency</p>
        :type OriginalAmount: float
        :param _ExchangeRateUSD: <p>Current exchange rate of base currency converted to USD</p>
        :type ExchangeRateUSD: float
        :param _ExchangeRateCNY: <p>Current exchange rate of base currency converted to CNY</p>
        :type ExchangeRateCNY: float
        """
        self._Currency = None
        self._OriginalAmount = None
        self._ExchangeRateUSD = None
        self._ExchangeRateCNY = None

    @property
    def Currency(self):
        r"""<p>Currency code</p><p>Parameter format: Compliant with the ISO 4217 standard</p>
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def OriginalAmount(self):
        r"""<p>Original amount in currency</p>
        :rtype: float
        """
        return self._OriginalAmount

    @OriginalAmount.setter
    def OriginalAmount(self, OriginalAmount):
        self._OriginalAmount = OriginalAmount

    @property
    def ExchangeRateUSD(self):
        r"""<p>Current exchange rate of base currency converted to USD</p>
        :rtype: float
        """
        return self._ExchangeRateUSD

    @ExchangeRateUSD.setter
    def ExchangeRateUSD(self, ExchangeRateUSD):
        self._ExchangeRateUSD = ExchangeRateUSD

    @property
    def ExchangeRateCNY(self):
        r"""<p>Current exchange rate of base currency converted to CNY</p>
        :rtype: float
        """
        return self._ExchangeRateCNY

    @ExchangeRateCNY.setter
    def ExchangeRateCNY(self, ExchangeRateCNY):
        self._ExchangeRateCNY = ExchangeRateCNY


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        self._OriginalAmount = params.get("OriginalAmount")
        self._ExchangeRateUSD = params.get("ExchangeRateUSD")
        self._ExchangeRateCNY = params.get("ExchangeRateCNY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class App(AbstractModel):
    r"""The details of the app, os and device

    """

    def __init__(self):
        r"""
        :param _OS: <p>The operating system your application is running on</p>
        :type OS: str
        :param _OSVersion: <p>The operating system version  your application is running on</p>
        :type OSVersion: str
        :param _DeviceManufacturer: <p>The manufacturer of  the device your application is running on</p>
        :type DeviceManufacturer: str
        :param _DeviceModel: <p>The model of the device your application is running on</p>
        :type DeviceModel: str
        :param _DeviceId: <p>The ID of the device your application is running on</p>
        :type DeviceId: str
        :param _AppName: <p>The name of your application</p>
        :type AppName: str
        :param _AppVersion: <p>The version of your application</p>
        :type AppVersion: str
        :param _ClientLanguage: <p>The language of your application</p>
        :type ClientLanguage: str
        """
        self._OS = None
        self._OSVersion = None
        self._DeviceManufacturer = None
        self._DeviceModel = None
        self._DeviceId = None
        self._AppName = None
        self._AppVersion = None
        self._ClientLanguage = None

    @property
    def OS(self):
        r"""<p>The operating system your application is running on</p>
        :rtype: str
        """
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS

    @property
    def OSVersion(self):
        r"""<p>The operating system version  your application is running on</p>
        :rtype: str
        """
        return self._OSVersion

    @OSVersion.setter
    def OSVersion(self, OSVersion):
        self._OSVersion = OSVersion

    @property
    def DeviceManufacturer(self):
        r"""<p>The manufacturer of  the device your application is running on</p>
        :rtype: str
        """
        return self._DeviceManufacturer

    @DeviceManufacturer.setter
    def DeviceManufacturer(self, DeviceManufacturer):
        self._DeviceManufacturer = DeviceManufacturer

    @property
    def DeviceModel(self):
        r"""<p>The model of the device your application is running on</p>
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def DeviceId(self):
        r"""<p>The ID of the device your application is running on</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AppName(self):
        r"""<p>The name of your application</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        r"""<p>The version of your application</p>
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def ClientLanguage(self):
        r"""<p>The language of your application</p>
        :rtype: str
        """
        return self._ClientLanguage

    @ClientLanguage.setter
    def ClientLanguage(self, ClientLanguage):
        self._ClientLanguage = ClientLanguage


    def _deserialize(self, params):
        self._OS = params.get("OS")
        self._OSVersion = params.get("OSVersion")
        self._DeviceManufacturer = params.get("DeviceManufacturer")
        self._DeviceModel = params.get("DeviceModel")
        self._DeviceId = params.get("DeviceId")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._ClientLanguage = params.get("ClientLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskPremiumProRequest(AbstractModel):
    r"""AssessDeviceRiskPremiumPro request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceToken: <p>Device fingerprint token, obtained after integration of the device fingerprint SDK into your website or application</p>
        :type DeviceToken: str
        :param _UserIp: <p>User client IP address (IPv4 or IPv6)</p>
        :type UserIp: str
        """
        self._DeviceToken = None
        self._UserIp = None

    @property
    def DeviceToken(self):
        r"""<p>Device fingerprint token, obtained after integration of the device fingerprint SDK into your website or application</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>User client IP address (IPv4 or IPv6)</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskPremiumProResponse(AbstractModel):
    r"""AssessDeviceRiskPremiumPro response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>The results of AssessDeviceRiskPremiumPro</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumRsp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>The results of AssessDeviceRiskPremiumPro</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskPremiumRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssessDeviceRiskPremiumRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessDeviceRiskPremiumRsp(AbstractModel):
    r"""The results of AssessDeviceRiskPremiumPro

    """

    def __init__(self):
        r"""
        :param _Decision: <p>Decision information</p>
        :type Decision: :class:`tencentcloud.rce.v20260130.models.Decision`
        :param _Score: <p>The risk score information of the device</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Device: <p>The basic information of the device</p>
        :type Device: :class:`tencentcloud.rce.v20260130.models.Device`
        :param _Environment: <p>Basic IP environment information</p>
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Decision = None
        self._Score = None
        self._Device = None
        self._Environment = None

    @property
    def Decision(self):
        r"""<p>Decision information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Decision`
        """
        return self._Decision

    @Decision.setter
    def Decision(self, Decision):
        self._Decision = Decision

    @property
    def Score(self):
        r"""<p>The risk score information of the device</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Device(self):
        r"""<p>The basic information of the device</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Environment(self):
        r"""<p>Basic IP environment information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Decision") is not None:
            self._Decision = Decision()
            self._Decision._deserialize(params.get("Decision"))
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskProRequest(AbstractModel):
    r"""AssessDeviceRiskPro request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceToken: <p>Device fingerprint token, obtained after integration of the device fingerprint SDK into your website or application</p>
        :type DeviceToken: str
        :param _UserIp: <p>User client IP address (IPv4 or IPv6)</p>
        :type UserIp: str
        """
        self._DeviceToken = None
        self._UserIp = None

    @property
    def DeviceToken(self):
        r"""<p>Device fingerprint token, obtained after integration of the device fingerprint SDK into your website or application</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>User client IP address (IPv4 or IPv6)</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessDeviceRiskProResponse(AbstractModel):
    r"""AssessDeviceRiskPro response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>The results of AssessDeviceRiskPro</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskRsp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>The results of AssessDeviceRiskPro</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessDeviceRiskRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssessDeviceRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessDeviceRiskRsp(AbstractModel):
    r"""The results of AssessDeviceRiskPro

    """

    def __init__(self):
        r"""
        :param _Score: <p>The risk score information of the device</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Device: <p>The basic information of the device</p>
        :type Device: :class:`tencentcloud.rce.v20260130.models.Device`
        :param _Environment: <p>Basic IP environment information</p>
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Score = None
        self._Device = None
        self._Environment = None

    @property
    def Score(self):
        r"""<p>The risk score information of the device</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Device(self):
        r"""<p>The basic information of the device</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Environment(self):
        r"""<p>Basic IP environment information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessEnvironmentRiskRequest(AbstractModel):
    r"""AssessEnvironmentRisk request structure.

    """

    def __init__(self):
        r"""
        :param _UserIp: <p>User client IP address(IPv4 or IPv6)</p>
        :type UserIp: str
        """
        self._UserIp = None

    @property
    def UserIp(self):
        r"""<p>User client IP address(IPv4 or IPv6)</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessEnvironmentRiskResponse(AbstractModel):
    r"""AssessEnvironmentRisk response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>The results of AssessEnvironmentRisk</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>The results of AssessEnvironmentRisk</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssessEnvironmentRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessEnvironmentRiskRsp(AbstractModel):
    r"""The results of AssessEnvironmentRisk

    """

    def __init__(self):
        r"""
        :param _Score: <p>The risk score information of the IP environment</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Environment: <p>The basic information of the IP environment</p>
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Score = None
        self._Environment = None

    @property
    def Score(self):
        r"""<p>The risk score information of the IP environment</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Environment(self):
        r"""<p>The basic information of the IP environment</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Billing(AbstractModel):
    r"""Bill information

    """

    def __init__(self):
        r"""
        :param _Address: <p>The billing address associated with this user</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Phone: <p>The phone number associated with the bill</p><p>Parameter format: Complies with the E.164 standard, using the format with "+", region code, and number</p>
        :type Phone: str
        :param _Email: <p>The email associated with the bill</p>
        :type Email: str
        :param _Recipient: <p>The name of the receiver associated with the bill</p>
        :type Recipient: str
        """
        self._Address = None
        self._Phone = None
        self._Email = None
        self._Recipient = None

    @property
    def Address(self):
        r"""<p>The billing address associated with this user</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Phone(self):
        r"""<p>The phone number associated with the bill</p><p>Parameter format: Complies with the E.164 standard, using the format with "+", region code, and number</p>
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""<p>The email associated with the bill</p>
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Recipient(self):
        r"""<p>The name of the receiver associated with the bill</p>
        :rtype: str
        """
        return self._Recipient

    @Recipient.setter
    def Recipient(self, Recipient):
        self._Recipient = Recipient


    def _deserialize(self, params):
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._Recipient = params.get("Recipient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrowseEvent(AbstractModel):
    r"""Browse event details

    """

    def __init__(self):
        r"""
        :param _PageType: <p>Current page type such as home page, search page</p>
        :type PageType: str
        :param _PageUrl: <p>Currently page URL</p>
        :type PageUrl: str
        :param _Duration: <p>Browsing duration</p><p>Measurement unit: ms</p>
        :type Duration: int
        :param _ContentType: <p>The type of the content in current page such as ad, video, article</p>
        :type ContentType: str
        :param _ContentId: <p>The ID of the content in current page</p>
        :type ContentId: str
        :param _ReferPageType: <p>Previous page type such as home page, search page</p>
        :type ReferPageType: str
        :param _ReferPageUrl: <p>Previous page URL</p>
        :type ReferPageUrl: str
        :param _GuestId: <p>The ID of the user as guest</p>
        :type GuestId: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PageType = None
        self._PageUrl = None
        self._Duration = None
        self._ContentType = None
        self._ContentId = None
        self._ReferPageType = None
        self._ReferPageUrl = None
        self._GuestId = None
        self._Cust = None

    @property
    def PageType(self):
        r"""<p>Current page type such as home page, search page</p>
        :rtype: str
        """
        return self._PageType

    @PageType.setter
    def PageType(self, PageType):
        self._PageType = PageType

    @property
    def PageUrl(self):
        r"""<p>Currently page URL</p>
        :rtype: str
        """
        return self._PageUrl

    @PageUrl.setter
    def PageUrl(self, PageUrl):
        self._PageUrl = PageUrl

    @property
    def Duration(self):
        r"""<p>Browsing duration</p><p>Measurement unit: ms</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ContentType(self):
        r"""<p>The type of the content in current page such as ad, video, article</p>
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def ContentId(self):
        r"""<p>The ID of the content in current page</p>
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ReferPageType(self):
        r"""<p>Previous page type such as home page, search page</p>
        :rtype: str
        """
        return self._ReferPageType

    @ReferPageType.setter
    def ReferPageType(self, ReferPageType):
        self._ReferPageType = ReferPageType

    @property
    def ReferPageUrl(self):
        r"""<p>Previous page URL</p>
        :rtype: str
        """
        return self._ReferPageUrl

    @ReferPageUrl.setter
    def ReferPageUrl(self, ReferPageUrl):
        self._ReferPageUrl = ReferPageUrl

    @property
    def GuestId(self):
        r"""<p>The ID of the user as guest</p>
        :rtype: str
        """
        return self._GuestId

    @GuestId.setter
    def GuestId(self, GuestId):
        self._GuestId = GuestId

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PageType = params.get("PageType")
        self._PageUrl = params.get("PageUrl")
        self._Duration = params.get("Duration")
        self._ContentType = params.get("ContentType")
        self._ContentId = params.get("ContentId")
        self._ReferPageType = params.get("ReferPageType")
        self._ReferPageUrl = params.get("ReferPageUrl")
        self._GuestId = params.get("GuestId")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Browser(AbstractModel):
    r"""Browser information

    """

    def __init__(self):
        r"""
        :param _UserAgent: <p>The user agent of the browser that interacts with the website</p>
        :type UserAgent: str
        :param _AcceptLanguage: <p>The language(s) that the client prefers</p><p>Parameter format: Complies with the ISO 3166 standard</p>
        :type AcceptLanguage: str
        :param _ContentLanguage: <p>The language(s) intended for the audience</p><p>Parameter format: Compliant with ISO 3166 standard</p>
        :type ContentLanguage: str
        """
        self._UserAgent = None
        self._AcceptLanguage = None
        self._ContentLanguage = None

    @property
    def UserAgent(self):
        r"""<p>The user agent of the browser that interacts with the website</p>
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def AcceptLanguage(self):
        r"""<p>The language(s) that the client prefers</p><p>Parameter format: Complies with the ISO 3166 standard</p>
        :rtype: str
        """
        return self._AcceptLanguage

    @AcceptLanguage.setter
    def AcceptLanguage(self, AcceptLanguage):
        self._AcceptLanguage = AcceptLanguage

    @property
    def ContentLanguage(self):
        r"""<p>The language(s) intended for the audience</p><p>Parameter format: Compliant with ISO 3166 standard</p>
        :rtype: str
        """
        return self._ContentLanguage

    @ContentLanguage.setter
    def ContentLanguage(self, ContentLanguage):
        self._ContentLanguage = ContentLanguage


    def _deserialize(self, params):
        self._UserAgent = params.get("UserAgent")
        self._AcceptLanguage = params.get("AcceptLanguage")
        self._ContentLanguage = params.get("ContentLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Card(AbstractModel):
    r"""The details of the card

    """

    def __init__(self):
        r"""
        :param _CardBin: <p>Bank identification number.The first six or eight digits of the card number</p><p>Parameter format: Compliant with the ISO 13616-1 standard</p>
        :type CardBin: str
        :param _LastFourDigits: <p>The last four digits of the card number</p><p>Parameter format: Compliant with ISO 13616-1 standard</p>
        :type LastFourDigits: str
        :param _Country: <p>The country where the card issued</p>
        :type Country: str
        :param _Bank: <p>The bank that issued card</p>
        :type Bank: str
        :param _Type: <p>the type of the card</p><p>Enumeration value:</p><ul><li>credit: Credit card</li><li>debit: Debit card</li><li>charge: Charge card</li></ul>
        :type Type: str
        :param _Brand: <p>The brand of the card</p>
        :type Brand: str
        :param _Level: <p>The level of the card that the bank defined</p>
        :type Level: str
        :param _HolderName: <p>The full name of the person who hold the card</p>
        :type HolderName: str
        :param _ExpireTime: <p>The expiration date of the card</p><p>Parameter format: YYYY-MM-DD.</p>
        :type ExpireTime: str
        """
        self._CardBin = None
        self._LastFourDigits = None
        self._Country = None
        self._Bank = None
        self._Type = None
        self._Brand = None
        self._Level = None
        self._HolderName = None
        self._ExpireTime = None

    @property
    def CardBin(self):
        r"""<p>Bank identification number.The first six or eight digits of the card number</p><p>Parameter format: Compliant with the ISO 13616-1 standard</p>
        :rtype: str
        """
        return self._CardBin

    @CardBin.setter
    def CardBin(self, CardBin):
        self._CardBin = CardBin

    @property
    def LastFourDigits(self):
        r"""<p>The last four digits of the card number</p><p>Parameter format: Compliant with ISO 13616-1 standard</p>
        :rtype: str
        """
        return self._LastFourDigits

    @LastFourDigits.setter
    def LastFourDigits(self, LastFourDigits):
        self._LastFourDigits = LastFourDigits

    @property
    def Country(self):
        r"""<p>The country where the card issued</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Bank(self):
        r"""<p>The bank that issued card</p>
        :rtype: str
        """
        return self._Bank

    @Bank.setter
    def Bank(self, Bank):
        self._Bank = Bank

    @property
    def Type(self):
        r"""<p>the type of the card</p><p>Enumeration value:</p><ul><li>credit: Credit card</li><li>debit: Debit card</li><li>charge: Charge card</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        r"""<p>The brand of the card</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Level(self):
        r"""<p>The level of the card that the bank defined</p>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def HolderName(self):
        r"""<p>The full name of the person who hold the card</p>
        :rtype: str
        """
        return self._HolderName

    @HolderName.setter
    def HolderName(self, HolderName):
        self._HolderName = HolderName

    @property
    def ExpireTime(self):
        r"""<p>The expiration date of the card</p><p>Parameter format: YYYY-MM-DD.</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._CardBin = params.get("CardBin")
        self._LastFourDigits = params.get("LastFourDigits")
        self._Country = params.get("Country")
        self._Bank = params.get("Bank")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Level = params.get("Level")
        self._HolderName = params.get("HolderName")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeBackEvent(AbstractModel):
    r"""ChargeBack event details

    """

    def __init__(self):
        r"""
        :param _TransactionId: <p>The ID of the transaction</p>
        :type TransactionId: str
        :param _OrderId: <p>The ID(s) of the order associated with the transaction</p>
        :type OrderId: list of str
        :param _ChargeBackCode: <p>The code of the chargeback defined by the card organization, for example: 10.1, 13.1, 4870, 4871</p>
        :type ChargeBackCode: str
        :param _ChargeBackReason: <p>The reason of the chargeback defined by the card organization, for example: non-receipt of goods, fraud</p>
        :type ChargeBackReason: str
        :param _ChargeBackProcess: <p>The process of the chargeback defined by the card organization</p><p>Enumeration values:</p><ul><li>need_response: Merchant needs to respond</li><li>information_supplied: Merchant has provided information</li><li>chargeback_reversed: Chargeback has been canceled</li><li>chargeback_sustained: Chargeback has been established</li></ul>
        :type ChargeBackProcess: str
        :param _ChargeBackAmount: <p>The amount of the chargeback</p>
        :type ChargeBackAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._TransactionId = None
        self._OrderId = None
        self._ChargeBackCode = None
        self._ChargeBackReason = None
        self._ChargeBackProcess = None
        self._ChargeBackAmount = None
        self._Cust = None

    @property
    def TransactionId(self):
        r"""<p>The ID of the transaction</p>
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def OrderId(self):
        r"""<p>The ID(s) of the order associated with the transaction</p>
        :rtype: list of str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ChargeBackCode(self):
        r"""<p>The code of the chargeback defined by the card organization, for example: 10.1, 13.1, 4870, 4871</p>
        :rtype: str
        """
        return self._ChargeBackCode

    @ChargeBackCode.setter
    def ChargeBackCode(self, ChargeBackCode):
        self._ChargeBackCode = ChargeBackCode

    @property
    def ChargeBackReason(self):
        r"""<p>The reason of the chargeback defined by the card organization, for example: non-receipt of goods, fraud</p>
        :rtype: str
        """
        return self._ChargeBackReason

    @ChargeBackReason.setter
    def ChargeBackReason(self, ChargeBackReason):
        self._ChargeBackReason = ChargeBackReason

    @property
    def ChargeBackProcess(self):
        r"""<p>The process of the chargeback defined by the card organization</p><p>Enumeration values:</p><ul><li>need_response: Merchant needs to respond</li><li>information_supplied: Merchant has provided information</li><li>chargeback_reversed: Chargeback has been canceled</li><li>chargeback_sustained: Chargeback has been established</li></ul>
        :rtype: str
        """
        return self._ChargeBackProcess

    @ChargeBackProcess.setter
    def ChargeBackProcess(self, ChargeBackProcess):
        self._ChargeBackProcess = ChargeBackProcess

    @property
    def ChargeBackAmount(self):
        r"""<p>The amount of the chargeback</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._ChargeBackAmount

    @ChargeBackAmount.setter
    def ChargeBackAmount(self, ChargeBackAmount):
        self._ChargeBackAmount = ChargeBackAmount

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._OrderId = params.get("OrderId")
        self._ChargeBackCode = params.get("ChargeBackCode")
        self._ChargeBackReason = params.get("ChargeBackReason")
        self._ChargeBackProcess = params.get("ChargeBackProcess")
        if params.get("ChargeBackAmount") is not None:
            self._ChargeBackAmount = Amount()
            self._ChargeBackAmount._deserialize(params.get("ChargeBackAmount"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClaimRedPacketEvent(AbstractModel):
    r"""ClaimRedPacket event details

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The Name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _RedPacketId: <p>The ID of the red packet</p>
        :type RedPacketId: str
        :param _RedPacketType: <p>The type of red packet, for example, random amount, passcode, standard</p>
        :type RedPacketType: str
        :param _RedPacketAmount: <p>The amount  in the red packet</p>
        :type RedPacketAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._RedPacketId = None
        self._RedPacketType = None
        self._RedPacketAmount = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The Name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def RedPacketId(self):
        r"""<p>The ID of the red packet</p>
        :rtype: str
        """
        return self._RedPacketId

    @RedPacketId.setter
    def RedPacketId(self, RedPacketId):
        self._RedPacketId = RedPacketId

    @property
    def RedPacketType(self):
        r"""<p>The type of red packet, for example, random amount, passcode, standard</p>
        :rtype: str
        """
        return self._RedPacketType

    @RedPacketType.setter
    def RedPacketType(self, RedPacketType):
        self._RedPacketType = RedPacketType

    @property
    def RedPacketAmount(self):
        r"""<p>The amount  in the red packet</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._RedPacketAmount

    @RedPacketAmount.setter
    def RedPacketAmount(self, RedPacketAmount):
        self._RedPacketAmount = RedPacketAmount

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._RedPacketId = params.get("RedPacketId")
        self._RedPacketType = params.get("RedPacketType")
        if params.get("RedPacketAmount") is not None:
            self._RedPacketAmount = Amount()
            self._RedPacketAmount._deserialize(params.get("RedPacketAmount"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coupon(AbstractModel):
    r"""The details of the coupon

    """

    def __init__(self):
        r"""
        :param _CouponId: <p>The unique ID of each coupon</p>
        :type CouponId: str
        :param _CouponName: <p>The name of the coupon</p>
        :type CouponName: str
        :param _StartTime: <p>The start time of the coupon</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601.</p>
        :type StartTime: str
        :param _ExpireTime: <p>The expiration time of the coupon</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601 standard</p>
        :type ExpireTime: str
        :param _PercentageRate: <p>The percentage rate of the coupon. If discount off is 10%,please send 0.1</p>
        :type PercentageRate: float
        :param _DiscountAmount: <p>The discount amount of the coupon</p>
        :type DiscountAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Threshold: <p>The threshold amount of the coupon</p>
        :type Threshold: float
        """
        self._CouponId = None
        self._CouponName = None
        self._StartTime = None
        self._ExpireTime = None
        self._PercentageRate = None
        self._DiscountAmount = None
        self._Threshold = None

    @property
    def CouponId(self):
        r"""<p>The unique ID of each coupon</p>
        :rtype: str
        """
        return self._CouponId

    @CouponId.setter
    def CouponId(self, CouponId):
        self._CouponId = CouponId

    @property
    def CouponName(self):
        r"""<p>The name of the coupon</p>
        :rtype: str
        """
        return self._CouponName

    @CouponName.setter
    def CouponName(self, CouponName):
        self._CouponName = CouponName

    @property
    def StartTime(self):
        r"""<p>The start time of the coupon</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""<p>The expiration time of the coupon</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601 standard</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PercentageRate(self):
        r"""<p>The percentage rate of the coupon. If discount off is 10%,please send 0.1</p>
        :rtype: float
        """
        return self._PercentageRate

    @PercentageRate.setter
    def PercentageRate(self, PercentageRate):
        self._PercentageRate = PercentageRate

    @property
    def DiscountAmount(self):
        r"""<p>The discount amount of the coupon</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._DiscountAmount

    @DiscountAmount.setter
    def DiscountAmount(self, DiscountAmount):
        self._DiscountAmount = DiscountAmount

    @property
    def Threshold(self):
        r"""<p>The threshold amount of the coupon</p>
        :rtype: float
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._CouponId = params.get("CouponId")
        self._CouponName = params.get("CouponName")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._PercentageRate = params.get("PercentageRate")
        if params.get("DiscountAmount") is not None:
            self._DiscountAmount = Amount()
            self._DiscountAmount._deserialize(params.get("DiscountAmount"))
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderEvent(AbstractModel):
    r"""CreateOrder event details

    """

    def __init__(self):
        r"""
        :param _OrderId: <p>The ID of the order</p>
        :type OrderId: str
        :param _Amount: <p>The amount of the order</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Merchant: <p>The detail information of the merchant associated with the order</p>
        :type Merchant: :class:`tencentcloud.rce.v20260130.models.Merchant`
        :param _Billing: <p>The detail information of the bill associated with the order</p>
        :type Billing: :class:`tencentcloud.rce.v20260130.models.Billing`
        :param _Items: <p>The detail information of the items in the order</p>
        :type Items: list of Item
        :param _Delivery: <p>The detail information of the delivery associated with the order</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        :param _Promotions: <p>The promotion(s) associated with the order</p>
        :type Promotions: list of Promotion
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._OrderId = None
        self._Amount = None
        self._Merchant = None
        self._Billing = None
        self._Items = None
        self._Delivery = None
        self._Promotions = None
        self._Cust = None

    @property
    def OrderId(self):
        r"""<p>The ID of the order</p>
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Amount(self):
        r"""<p>The amount of the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Merchant(self):
        r"""<p>The detail information of the merchant associated with the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Merchant`
        """
        return self._Merchant

    @Merchant.setter
    def Merchant(self, Merchant):
        self._Merchant = Merchant

    @property
    def Billing(self):
        r"""<p>The detail information of the bill associated with the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Billing`
        """
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def Items(self):
        r"""<p>The detail information of the items in the order</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Delivery(self):
        r"""<p>The detail information of the delivery associated with the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery

    @property
    def Promotions(self):
        r"""<p>The promotion(s) associated with the order</p>
        :rtype: list of Promotion
        """
        return self._Promotions

    @Promotions.setter
    def Promotions(self, Promotions):
        self._Promotions = Promotions

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        if params.get("Merchant") is not None:
            self._Merchant = Merchant()
            self._Merchant._deserialize(params.get("Merchant"))
        if params.get("Billing") is not None:
            self._Billing = Billing()
            self._Billing._deserialize(params.get("Billing"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        if params.get("Promotions") is not None:
            self._Promotions = []
            for item in params.get("Promotions"):
                obj = Promotion()
                obj._deserialize(item)
                self._Promotions.append(obj)
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreditPoint(AbstractModel):
    r"""The details of the point

    """

    def __init__(self):
        r"""
        :param _Point: <p>The value of the point</p>
        :type Point: float
        :param _PointType: <p>The type of the point</p>
        :type PointType: str
        """
        self._Point = None
        self._PointType = None

    @property
    def Point(self):
        r"""<p>The value of the point</p>
        :rtype: float
        """
        return self._Point

    @Point.setter
    def Point(self, Point):
        self._Point = Point

    @property
    def PointType(self):
        r"""<p>The type of the point</p>
        :rtype: str
        """
        return self._PointType

    @PointType.setter
    def PointType(self, PointType):
        self._PointType = PointType


    def _deserialize(self, params):
        self._Point = params.get("Point")
        self._PointType = params.get("PointType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cust(AbstractModel):
    r"""Customization parameters agreed with RCE, object array in K:V format

    """

    def __init__(self):
        r"""
        :param _Key: <p>Key</p>
        :type Key: str
        :param _Value: <p>Value</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>Key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustEvent(AbstractModel):
    r"""Custom event

    """

    def __init__(self):
        r"""
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._Cust = None

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataScore(AbstractModel):
    r"""Risk score information

    """

    def __init__(self):
        r"""
        :param _RiskLevel: <p>Risk level</p>
        :type RiskLevel: int
        :param _RiskLabels: <p>Risk label</p>
        :type RiskLabels: list of RiskLabel
        :param _RiskScore: <p>Comprehensive risk score.</p><p>Value ranges from 1 to 1000.</p><p>The larger the value, the larger the risk.</p>
        :type RiskScore: int
        """
        self._RiskLevel = None
        self._RiskLabels = None
        self._RiskScore = None

    @property
    def RiskLevel(self):
        r"""<p>Risk level</p>
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskLabels(self):
        r"""<p>Risk label</p>
        :rtype: list of RiskLabel
        """
        return self._RiskLabels

    @RiskLabels.setter
    def RiskLabels(self, RiskLabels):
        self._RiskLabels = RiskLabels

    @property
    def RiskScore(self):
        r"""<p>Comprehensive risk score.</p><p>Value ranges from 1 to 1000.</p><p>The larger the value, the larger the risk.</p>
        :rtype: int
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore


    def _deserialize(self, params):
        self._RiskLevel = params.get("RiskLevel")
        if params.get("RiskLabels") is not None:
            self._RiskLabels = []
            for item in params.get("RiskLabels"):
                obj = RiskLabel()
                obj._deserialize(item)
                self._RiskLabels.append(obj)
        self._RiskScore = params.get("RiskScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Decision(AbstractModel):
    r"""Decision information

    """

    def __init__(self):
        r"""
        :param _DecisionResult: <p>Decision result</p><ul><li>pass: Pass</li><li>review: Review</li><li>reject: Reject</li></ul>
        :type DecisionResult: str
        :param _Disposition: <p>Decision action when a strategy is matched. Configurable in the console.</p>
        :type Disposition: str
        """
        self._DecisionResult = None
        self._Disposition = None

    @property
    def DecisionResult(self):
        r"""<p>Decision result</p><ul><li>pass: Pass</li><li>review: Review</li><li>reject: Reject</li></ul>
        :rtype: str
        """
        return self._DecisionResult

    @DecisionResult.setter
    def DecisionResult(self, DecisionResult):
        self._DecisionResult = DecisionResult

    @property
    def Disposition(self):
        r"""<p>Decision action when a strategy is matched. Configurable in the console.</p>
        :rtype: str
        """
        return self._Disposition

    @Disposition.setter
    def Disposition(self, Disposition):
        self._Disposition = Disposition


    def _deserialize(self, params):
        self._DecisionResult = params.get("DecisionResult")
        self._Disposition = params.get("Disposition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Delivery(AbstractModel):
    r"""Delivery information

    """

    def __init__(self):
        r"""
        :param _DeliveryMethod: <p>The method of the delivery</p><ul><li>physical</li><li>electronic</li></ul>
        :type DeliveryMethod: str
        :param _DeliveryAmount: <p>The fee of the delivery</p>
        :type DeliveryAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _DeliveryAddress: <p>The address of the delivery</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _ConsigneePhone: <p>Phone number of the consignee</p><p>parameter format: format with "+", region code, and number that complies with the E.164 standard</p>
        :type ConsigneePhone: str
        :param _ConsigneeEmail: <p>Email of the consignee</p>
        :type ConsigneeEmail: str
        :param _ConsigneeName: <p>Full name of the consignee</p>
        :type ConsigneeName: str
        :param _Expedited: <p> Whether is the delivery expedited</p>
        :type Expedited: bool
        :param _DeliveryCarrier: <p>The carrier of the delivery, usually a logistics company</p>
        :type DeliveryCarrier: str
        :param _DeliveryTracking: <p>The number(s) used to track the delivery</p>
        :type DeliveryTracking: str
        """
        self._DeliveryMethod = None
        self._DeliveryAmount = None
        self._DeliveryAddress = None
        self._ConsigneePhone = None
        self._ConsigneeEmail = None
        self._ConsigneeName = None
        self._Expedited = None
        self._DeliveryCarrier = None
        self._DeliveryTracking = None

    @property
    def DeliveryMethod(self):
        r"""<p>The method of the delivery</p><ul><li>physical</li><li>electronic</li></ul>
        :rtype: str
        """
        return self._DeliveryMethod

    @DeliveryMethod.setter
    def DeliveryMethod(self, DeliveryMethod):
        self._DeliveryMethod = DeliveryMethod

    @property
    def DeliveryAmount(self):
        r"""<p>The fee of the delivery</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._DeliveryAmount

    @DeliveryAmount.setter
    def DeliveryAmount(self, DeliveryAmount):
        self._DeliveryAmount = DeliveryAmount

    @property
    def DeliveryAddress(self):
        r"""<p>The address of the delivery</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def ConsigneePhone(self):
        r"""<p>Phone number of the consignee</p><p>parameter format: format with "+", region code, and number that complies with the E.164 standard</p>
        :rtype: str
        """
        return self._ConsigneePhone

    @ConsigneePhone.setter
    def ConsigneePhone(self, ConsigneePhone):
        self._ConsigneePhone = ConsigneePhone

    @property
    def ConsigneeEmail(self):
        r"""<p>Email of the consignee</p>
        :rtype: str
        """
        return self._ConsigneeEmail

    @ConsigneeEmail.setter
    def ConsigneeEmail(self, ConsigneeEmail):
        self._ConsigneeEmail = ConsigneeEmail

    @property
    def ConsigneeName(self):
        r"""<p>Full name of the consignee</p>
        :rtype: str
        """
        return self._ConsigneeName

    @ConsigneeName.setter
    def ConsigneeName(self, ConsigneeName):
        self._ConsigneeName = ConsigneeName

    @property
    def Expedited(self):
        r"""<p> Whether is the delivery expedited</p>
        :rtype: bool
        """
        return self._Expedited

    @Expedited.setter
    def Expedited(self, Expedited):
        self._Expedited = Expedited

    @property
    def DeliveryCarrier(self):
        r"""<p>The carrier of the delivery, usually a logistics company</p>
        :rtype: str
        """
        return self._DeliveryCarrier

    @DeliveryCarrier.setter
    def DeliveryCarrier(self, DeliveryCarrier):
        self._DeliveryCarrier = DeliveryCarrier

    @property
    def DeliveryTracking(self):
        r"""<p>The number(s) used to track the delivery</p>
        :rtype: str
        """
        return self._DeliveryTracking

    @DeliveryTracking.setter
    def DeliveryTracking(self, DeliveryTracking):
        self._DeliveryTracking = DeliveryTracking


    def _deserialize(self, params):
        self._DeliveryMethod = params.get("DeliveryMethod")
        if params.get("DeliveryAmount") is not None:
            self._DeliveryAmount = Amount()
            self._DeliveryAmount._deserialize(params.get("DeliveryAmount"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        self._ConsigneePhone = params.get("ConsigneePhone")
        self._ConsigneeEmail = params.get("ConsigneeEmail")
        self._ConsigneeName = params.get("ConsigneeName")
        self._Expedited = params.get("Expedited")
        self._DeliveryCarrier = params.get("DeliveryCarrier")
        self._DeliveryTracking = params.get("DeliveryTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    r"""The basic infomation of the device

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>The unique id of device returned by RCE</p>
        :type DeviceId: str
        :param _AppVersion: <p>The version of the application</p>
        :type AppVersion: str
        :param _Brand: <p>Device brand</p>
        :type Brand: str
        :param _ClientIp: <p>Client IP address</p>
        :type ClientIp: str
        :param _Model: <p>Device model</p>
        :type Model: str
        :param _NetworkType: <p>Network type of the device</p>
        :type NetworkType: str
        :param _PackageName: <p>The package name of the application</p>
        :type PackageName: str
        :param _Platform: <p>Device platform</p><p>Enumeration value:</p><ul><li>2: Android</li><li>3: IOS</li><li>4: H5</li><li>5: WeChat Mini Program</li></ul>
        :type Platform: str
        :param _SystemVersion: <p>Device system version</p>
        :type SystemVersion: str
        :param _SdkBuildVersion: <p>The build version of SDK</p>
        :type SdkBuildVersion: str
        :param _SignToken: <p>Signature verification token. Please contact us to enable signature verification</p>
        :type SignToken: str
        :param _TokenTime: <p>Token generation timestamp, in milliseconds</p>
        :type TokenTime: str
        """
        self._DeviceId = None
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildVersion = None
        self._SignToken = None
        self._TokenTime = None

    @property
    def DeviceId(self):
        r"""<p>The unique id of device returned by RCE</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def AppVersion(self):
        r"""<p>The version of the application</p>
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        r"""<p>Device brand</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        r"""<p>Client IP address</p>
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        r"""<p>Device model</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        r"""<p>Network type of the device</p>
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        r"""<p>The package name of the application</p>
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        r"""<p>Device platform</p><p>Enumeration value:</p><ul><li>2: Android</li><li>3: IOS</li><li>4: H5</li><li>5: WeChat Mini Program</li></ul>
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        r"""<p>Device system version</p>
        :rtype: str
        """
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildVersion(self):
        r"""<p>The build version of SDK</p>
        :rtype: str
        """
        return self._SdkBuildVersion

    @SdkBuildVersion.setter
    def SdkBuildVersion(self, SdkBuildVersion):
        self._SdkBuildVersion = SdkBuildVersion

    @property
    def SignToken(self):
        r"""<p>Signature verification token. Please contact us to enable signature verification</p>
        :rtype: str
        """
        return self._SignToken

    @SignToken.setter
    def SignToken(self, SignToken):
        self._SignToken = SignToken

    @property
    def TokenTime(self):
        r"""<p>Token generation timestamp, in milliseconds</p>
        :rtype: str
        """
        return self._TokenTime

    @TokenTime.setter
    def TokenTime(self, TokenTime):
        self._TokenTime = TokenTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildVersion = params.get("SdkBuildVersion")
        self._SignToken = params.get("SignToken")
        self._TokenTime = params.get("TokenTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DigitalOrder(AbstractModel):
    r"""The details of the digital order

    """

    def __init__(self):
        r"""
        :param _DigitalAsset: <p>The name of the asset</p>
        :type DigitalAsset: str
        :param _AssetType: <p>The type of the asset</p><p>Enumeration value:</p><ul><li>coin</li><li>commodity</li><li>crypto</li><li>fiat</li><li>token</li><li>stock</li><li>bond</li></ul>
        :type AssetType: str
        :param _OrderType: <p>The type of trade being made</p><p>Enumeration value:</p><ul><li>limit: Limit order</li><li>market: Market order</li><li>stop_limit: Stop-limit order</li><li>stop_loss: Stop-loss order</li><li>take_profit: Take-profit order</li><li>take_profit_limit: Take-profit limit order</li></ul>
        :type OrderType: str
        :param _Volume: <p>The quantity of the digital asset</p>
        :type Volume: float
        """
        self._DigitalAsset = None
        self._AssetType = None
        self._OrderType = None
        self._Volume = None

    @property
    def DigitalAsset(self):
        r"""<p>The name of the asset</p>
        :rtype: str
        """
        return self._DigitalAsset

    @DigitalAsset.setter
    def DigitalAsset(self, DigitalAsset):
        self._DigitalAsset = DigitalAsset

    @property
    def AssetType(self):
        r"""<p>The type of the asset</p><p>Enumeration value:</p><ul><li>coin</li><li>commodity</li><li>crypto</li><li>fiat</li><li>token</li><li>stock</li><li>bond</li></ul>
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def OrderType(self):
        r"""<p>The type of trade being made</p><p>Enumeration value:</p><ul><li>limit: Limit order</li><li>market: Market order</li><li>stop_limit: Stop-limit order</li><li>stop_loss: Stop-loss order</li><li>take_profit: Take-profit order</li><li>take_profit_limit: Take-profit limit order</li></ul>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Volume(self):
        r"""<p>The quantity of the digital asset</p>
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._DigitalAsset = params.get("DigitalAsset")
        self._AssetType = params.get("AssetType")
        self._OrderType = params.get("OrderType")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    r"""The basic information of the IP environment

    """

    def __init__(self):
        r"""
        :param _Location: <p>The geographical location of the IP address</p>
        :type Location: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        :param _Network: <p>The basic IP network information</p>
        :type Network: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        self._Location = None
        self._Network = None

    @property
    def Location(self):
        r"""<p>The geographical location of the IP address</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Network(self):
        r"""<p>The basic IP network information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self._Location = IPLocation()
            self._Location._deserialize(params.get("Location"))
        if params.get("Network") is not None:
            self._Network = IPNetwork()
            self._Network._deserialize(params.get("Network"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventDetail(AbstractModel):
    r"""Event details

    """

    def __init__(self):
        r"""
        :param _Login: <p>Login</p>
        :type Login: :class:`tencentcloud.rce.v20260130.models.LoginEvent`
        :param _Register: <p>Registration</p>
        :type Register: :class:`tencentcloud.rce.v20260130.models.RegisterEvent`
        :param _CreateOrder: <p>Create an order</p>
        :type CreateOrder: :class:`tencentcloud.rce.v20260130.models.CreateOrderEvent`
        :param _Transaction: <p>Transaction</p>
        :type Transaction: :class:`tencentcloud.rce.v20260130.models.TransactionEvent`
        :param _Sms: <p>SMS</p>
        :type Sms: :class:`tencentcloud.rce.v20260130.models.SMSEvent`
        :param _ChargeBack: <p>Chargeback</p>
        :type ChargeBack: :class:`tencentcloud.rce.v20260130.models.ChargeBackEvent`
        :param _Logout: <p>Logout</p>
        :type Logout: :class:`tencentcloud.rce.v20260130.models.LogoutEvent`
        :param _ModifyAccount: <p>Modify account</p>
        :type ModifyAccount: :class:`tencentcloud.rce.v20260130.models.ModifyAccountEvent`
        :param _ModifyPassword: <p>Modify password</p>
        :type ModifyPassword: :class:`tencentcloud.rce.v20260130.models.ModifyPasswordEvent`
        :param _SecurityVerification: <p>Security verification</p>
        :type SecurityVerification: :class:`tencentcloud.rce.v20260130.models.SecurityVerificationEvent`
        :param _AddPromotion: <p>Participate in promotion activities</p>
        :type AddPromotion: :class:`tencentcloud.rce.v20260130.models.AddPromotionEvent`
        :param _Redeem: <p>Redeem a prize</p>
        :type Redeem: :class:`tencentcloud.rce.v20260130.models.RedeemEvent`
        :param _Withdraw: <p>Withdrawal</p>
        :type Withdraw: :class:`tencentcloud.rce.v20260130.models.WithdrawEvent`
        :param _CustEvent: <p>Custom event</p>
        :type CustEvent: :class:`tencentcloud.rce.v20260130.models.CustEvent`
        :param _ScanCode: <p>Scan the QR code</p>
        :type ScanCode: :class:`tencentcloud.rce.v20260130.models.ScanCodeEvent`
        :param _LuckyDraw: <p>Lucky draw</p>
        :type LuckyDraw: :class:`tencentcloud.rce.v20260130.models.LuckyDrawEvent`
        :param _Task: <p>Perform a task</p>
        :type Task: :class:`tencentcloud.rce.v20260130.models.TaskEvent`
        :param _Invitation: <p>Invitation</p>
        :type Invitation: :class:`tencentcloud.rce.v20260130.models.InvitationEvent`
        :param _ClaimRedPacket: <p>Receive a red packet</p>
        :type ClaimRedPacket: :class:`tencentcloud.rce.v20260130.models.ClaimRedPacketEvent`
        :param _Browse: <p>Browse</p>
        :type Browse: :class:`tencentcloud.rce.v20260130.models.BrowseEvent`
        """
        self._Login = None
        self._Register = None
        self._CreateOrder = None
        self._Transaction = None
        self._Sms = None
        self._ChargeBack = None
        self._Logout = None
        self._ModifyAccount = None
        self._ModifyPassword = None
        self._SecurityVerification = None
        self._AddPromotion = None
        self._Redeem = None
        self._Withdraw = None
        self._CustEvent = None
        self._ScanCode = None
        self._LuckyDraw = None
        self._Task = None
        self._Invitation = None
        self._ClaimRedPacket = None
        self._Browse = None

    @property
    def Login(self):
        r"""<p>Login</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LoginEvent`
        """
        return self._Login

    @Login.setter
    def Login(self, Login):
        self._Login = Login

    @property
    def Register(self):
        r"""<p>Registration</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.RegisterEvent`
        """
        return self._Register

    @Register.setter
    def Register(self, Register):
        self._Register = Register

    @property
    def CreateOrder(self):
        r"""<p>Create an order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreateOrderEvent`
        """
        return self._CreateOrder

    @CreateOrder.setter
    def CreateOrder(self, CreateOrder):
        self._CreateOrder = CreateOrder

    @property
    def Transaction(self):
        r"""<p>Transaction</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.TransactionEvent`
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def Sms(self):
        r"""<p>SMS</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.SMSEvent`
        """
        return self._Sms

    @Sms.setter
    def Sms(self, Sms):
        self._Sms = Sms

    @property
    def ChargeBack(self):
        r"""<p>Chargeback</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ChargeBackEvent`
        """
        return self._ChargeBack

    @ChargeBack.setter
    def ChargeBack(self, ChargeBack):
        self._ChargeBack = ChargeBack

    @property
    def Logout(self):
        r"""<p>Logout</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LogoutEvent`
        """
        return self._Logout

    @Logout.setter
    def Logout(self, Logout):
        self._Logout = Logout

    @property
    def ModifyAccount(self):
        r"""<p>Modify account</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ModifyAccountEvent`
        """
        return self._ModifyAccount

    @ModifyAccount.setter
    def ModifyAccount(self, ModifyAccount):
        self._ModifyAccount = ModifyAccount

    @property
    def ModifyPassword(self):
        r"""<p>Modify password</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ModifyPasswordEvent`
        """
        return self._ModifyPassword

    @ModifyPassword.setter
    def ModifyPassword(self, ModifyPassword):
        self._ModifyPassword = ModifyPassword

    @property
    def SecurityVerification(self):
        r"""<p>Security verification</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.SecurityVerificationEvent`
        """
        return self._SecurityVerification

    @SecurityVerification.setter
    def SecurityVerification(self, SecurityVerification):
        self._SecurityVerification = SecurityVerification

    @property
    def AddPromotion(self):
        r"""<p>Participate in promotion activities</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AddPromotionEvent`
        """
        return self._AddPromotion

    @AddPromotion.setter
    def AddPromotion(self, AddPromotion):
        self._AddPromotion = AddPromotion

    @property
    def Redeem(self):
        r"""<p>Redeem a prize</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.RedeemEvent`
        """
        return self._Redeem

    @Redeem.setter
    def Redeem(self, Redeem):
        self._Redeem = Redeem

    @property
    def Withdraw(self):
        r"""<p>Withdrawal</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.WithdrawEvent`
        """
        return self._Withdraw

    @Withdraw.setter
    def Withdraw(self, Withdraw):
        self._Withdraw = Withdraw

    @property
    def CustEvent(self):
        r"""<p>Custom event</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CustEvent`
        """
        return self._CustEvent

    @CustEvent.setter
    def CustEvent(self, CustEvent):
        self._CustEvent = CustEvent

    @property
    def ScanCode(self):
        r"""<p>Scan the QR code</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ScanCodeEvent`
        """
        return self._ScanCode

    @ScanCode.setter
    def ScanCode(self, ScanCode):
        self._ScanCode = ScanCode

    @property
    def LuckyDraw(self):
        r"""<p>Lucky draw</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.LuckyDrawEvent`
        """
        return self._LuckyDraw

    @LuckyDraw.setter
    def LuckyDraw(self, LuckyDraw):
        self._LuckyDraw = LuckyDraw

    @property
    def Task(self):
        r"""<p>Perform a task</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.TaskEvent`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def Invitation(self):
        r"""<p>Invitation</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.InvitationEvent`
        """
        return self._Invitation

    @Invitation.setter
    def Invitation(self, Invitation):
        self._Invitation = Invitation

    @property
    def ClaimRedPacket(self):
        r"""<p>Receive a red packet</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.ClaimRedPacketEvent`
        """
        return self._ClaimRedPacket

    @ClaimRedPacket.setter
    def ClaimRedPacket(self, ClaimRedPacket):
        self._ClaimRedPacket = ClaimRedPacket

    @property
    def Browse(self):
        r"""<p>Browse</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.BrowseEvent`
        """
        return self._Browse

    @Browse.setter
    def Browse(self, Browse):
        self._Browse = Browse


    def _deserialize(self, params):
        if params.get("Login") is not None:
            self._Login = LoginEvent()
            self._Login._deserialize(params.get("Login"))
        if params.get("Register") is not None:
            self._Register = RegisterEvent()
            self._Register._deserialize(params.get("Register"))
        if params.get("CreateOrder") is not None:
            self._CreateOrder = CreateOrderEvent()
            self._CreateOrder._deserialize(params.get("CreateOrder"))
        if params.get("Transaction") is not None:
            self._Transaction = TransactionEvent()
            self._Transaction._deserialize(params.get("Transaction"))
        if params.get("Sms") is not None:
            self._Sms = SMSEvent()
            self._Sms._deserialize(params.get("Sms"))
        if params.get("ChargeBack") is not None:
            self._ChargeBack = ChargeBackEvent()
            self._ChargeBack._deserialize(params.get("ChargeBack"))
        if params.get("Logout") is not None:
            self._Logout = LogoutEvent()
            self._Logout._deserialize(params.get("Logout"))
        if params.get("ModifyAccount") is not None:
            self._ModifyAccount = ModifyAccountEvent()
            self._ModifyAccount._deserialize(params.get("ModifyAccount"))
        if params.get("ModifyPassword") is not None:
            self._ModifyPassword = ModifyPasswordEvent()
            self._ModifyPassword._deserialize(params.get("ModifyPassword"))
        if params.get("SecurityVerification") is not None:
            self._SecurityVerification = SecurityVerificationEvent()
            self._SecurityVerification._deserialize(params.get("SecurityVerification"))
        if params.get("AddPromotion") is not None:
            self._AddPromotion = AddPromotionEvent()
            self._AddPromotion._deserialize(params.get("AddPromotion"))
        if params.get("Redeem") is not None:
            self._Redeem = RedeemEvent()
            self._Redeem._deserialize(params.get("Redeem"))
        if params.get("Withdraw") is not None:
            self._Withdraw = WithdrawEvent()
            self._Withdraw._deserialize(params.get("Withdraw"))
        if params.get("CustEvent") is not None:
            self._CustEvent = CustEvent()
            self._CustEvent._deserialize(params.get("CustEvent"))
        if params.get("ScanCode") is not None:
            self._ScanCode = ScanCodeEvent()
            self._ScanCode._deserialize(params.get("ScanCode"))
        if params.get("LuckyDraw") is not None:
            self._LuckyDraw = LuckyDrawEvent()
            self._LuckyDraw._deserialize(params.get("LuckyDraw"))
        if params.get("Task") is not None:
            self._Task = TaskEvent()
            self._Task._deserialize(params.get("Task"))
        if params.get("Invitation") is not None:
            self._Invitation = InvitationEvent()
            self._Invitation._deserialize(params.get("Invitation"))
        if params.get("ClaimRedPacket") is not None:
            self._ClaimRedPacket = ClaimRedPacketEvent()
            self._ClaimRedPacket._deserialize(params.get("ClaimRedPacket"))
        if params.get("Browse") is not None:
            self._Browse = BrowseEvent()
            self._Browse._deserialize(params.get("Browse"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLocation(AbstractModel):
    r"""The geographical location of the IP address

    """

    def __init__(self):
        r"""
        :param _Country: <p>The country of the IP address</p>
        :type Country: str
        :param _Region: <p>The region of the IP address</p>
        :type Region: str
        :param _City: <p>The city of the IP address</p>
        :type City: str
        :param _District: <p>The district of the IP address</p>
        :type District: str
        :param _Longitude: <p>The longitude of the IP address</p>
        :type Longitude: str
        :param _Latitude: <p>The latitude of the IP address</p>
        :type Latitude: str
        :param _Timezone: <p>The timezone of the IP address</p>
        :type Timezone: str
        :param _ZipCode: <p>The zip code of the IP address</p>
        :type ZipCode: str
        """
        self._Country = None
        self._Region = None
        self._City = None
        self._District = None
        self._Longitude = None
        self._Latitude = None
        self._Timezone = None
        self._ZipCode = None

    @property
    def Country(self):
        r"""<p>The country of the IP address</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Region(self):
        r"""<p>The region of the IP address</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def City(self):
        r"""<p>The city of the IP address</p>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""<p>The district of the IP address</p>
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Longitude(self):
        r"""<p>The longitude of the IP address</p>
        :rtype: str
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""<p>The latitude of the IP address</p>
        :rtype: str
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Timezone(self):
        r"""<p>The timezone of the IP address</p>
        :rtype: str
        """
        return self._Timezone

    @Timezone.setter
    def Timezone(self, Timezone):
        self._Timezone = Timezone

    @property
    def ZipCode(self):
        r"""<p>The zip code of the IP address</p>
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._Region = params.get("Region")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._Timezone = params.get("Timezone")
        self._ZipCode = params.get("ZipCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPNetwork(AbstractModel):
    r"""The basic IP network information

    """

    def __init__(self):
        r"""
        :param _ISP: <p>Internet service provider</p>
        :type ISP: str
        :param _ASN: <p>Autonomous system number</p>
        :type ASN: str
        :param _Organization: <p>IP registration organization name</p>
        :type Organization: str
        :param _IsReserved: <p>Whether it is a reserved IP address</p>
        :type IsReserved: bool
        :param _IsGateway: <p>Whether it is a gateway IP address</p>
        :type IsGateway: bool
        :param _IsAnycast: <p>Whether it belongs to an anycast network</p>
        :type IsAnycast: bool
        :param _IsMobile: <p>Whether it is from a mobile network</p>
        :type IsMobile: bool
        :param _IsDynamic: <p>Whether it is a dynamic IP address</p>
        :type IsDynamic: bool
        :param _IsEgress: <p>Whether it is a network egress</p>
        :type IsEgress: bool
        :param _IsDNS: <p>Whether it is used for domain name resolution</p>
        :type IsDNS: bool
        :param _IsEducation: <p>Whether it is an educational institution</p>
        :type IsEducation: bool
        :param _IsInstitution: <p>Whether it is an organization</p>
        :type IsInstitution: bool
        :param _IsCompany: <p>Whether it is an enterprise dedicated line</p>
        :type IsCompany: bool
        :param _IsResidence: <p>Whether it is a residence broadband connection</p>
        :type IsResidence: bool
        :param _IsCloudService: <p>Whether it is cloud service</p>
        :type IsCloudService: bool
        :param _IsInfrastructure: <p>Whether it is infrastructure</p>
        :type IsInfrastructure: bool
        :param _IsMXServer: <p>Whether it is an mail exchange service</p>
        :type IsMXServer: bool
        """
        self._ISP = None
        self._ASN = None
        self._Organization = None
        self._IsReserved = None
        self._IsGateway = None
        self._IsAnycast = None
        self._IsMobile = None
        self._IsDynamic = None
        self._IsEgress = None
        self._IsDNS = None
        self._IsEducation = None
        self._IsInstitution = None
        self._IsCompany = None
        self._IsResidence = None
        self._IsCloudService = None
        self._IsInfrastructure = None
        self._IsMXServer = None

    @property
    def ISP(self):
        r"""<p>Internet service provider</p>
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def ASN(self):
        r"""<p>Autonomous system number</p>
        :rtype: str
        """
        return self._ASN

    @ASN.setter
    def ASN(self, ASN):
        self._ASN = ASN

    @property
    def Organization(self):
        r"""<p>IP registration organization name</p>
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def IsReserved(self):
        r"""<p>Whether it is a reserved IP address</p>
        :rtype: bool
        """
        return self._IsReserved

    @IsReserved.setter
    def IsReserved(self, IsReserved):
        self._IsReserved = IsReserved

    @property
    def IsGateway(self):
        r"""<p>Whether it is a gateway IP address</p>
        :rtype: bool
        """
        return self._IsGateway

    @IsGateway.setter
    def IsGateway(self, IsGateway):
        self._IsGateway = IsGateway

    @property
    def IsAnycast(self):
        r"""<p>Whether it belongs to an anycast network</p>
        :rtype: bool
        """
        return self._IsAnycast

    @IsAnycast.setter
    def IsAnycast(self, IsAnycast):
        self._IsAnycast = IsAnycast

    @property
    def IsMobile(self):
        r"""<p>Whether it is from a mobile network</p>
        :rtype: bool
        """
        return self._IsMobile

    @IsMobile.setter
    def IsMobile(self, IsMobile):
        self._IsMobile = IsMobile

    @property
    def IsDynamic(self):
        r"""<p>Whether it is a dynamic IP address</p>
        :rtype: bool
        """
        return self._IsDynamic

    @IsDynamic.setter
    def IsDynamic(self, IsDynamic):
        self._IsDynamic = IsDynamic

    @property
    def IsEgress(self):
        r"""<p>Whether it is a network egress</p>
        :rtype: bool
        """
        return self._IsEgress

    @IsEgress.setter
    def IsEgress(self, IsEgress):
        self._IsEgress = IsEgress

    @property
    def IsDNS(self):
        r"""<p>Whether it is used for domain name resolution</p>
        :rtype: bool
        """
        return self._IsDNS

    @IsDNS.setter
    def IsDNS(self, IsDNS):
        self._IsDNS = IsDNS

    @property
    def IsEducation(self):
        r"""<p>Whether it is an educational institution</p>
        :rtype: bool
        """
        return self._IsEducation

    @IsEducation.setter
    def IsEducation(self, IsEducation):
        self._IsEducation = IsEducation

    @property
    def IsInstitution(self):
        r"""<p>Whether it is an organization</p>
        :rtype: bool
        """
        return self._IsInstitution

    @IsInstitution.setter
    def IsInstitution(self, IsInstitution):
        self._IsInstitution = IsInstitution

    @property
    def IsCompany(self):
        r"""<p>Whether it is an enterprise dedicated line</p>
        :rtype: bool
        """
        return self._IsCompany

    @IsCompany.setter
    def IsCompany(self, IsCompany):
        self._IsCompany = IsCompany

    @property
    def IsResidence(self):
        r"""<p>Whether it is a residence broadband connection</p>
        :rtype: bool
        """
        return self._IsResidence

    @IsResidence.setter
    def IsResidence(self, IsResidence):
        self._IsResidence = IsResidence

    @property
    def IsCloudService(self):
        r"""<p>Whether it is cloud service</p>
        :rtype: bool
        """
        return self._IsCloudService

    @IsCloudService.setter
    def IsCloudService(self, IsCloudService):
        self._IsCloudService = IsCloudService

    @property
    def IsInfrastructure(self):
        r"""<p>Whether it is infrastructure</p>
        :rtype: bool
        """
        return self._IsInfrastructure

    @IsInfrastructure.setter
    def IsInfrastructure(self, IsInfrastructure):
        self._IsInfrastructure = IsInfrastructure

    @property
    def IsMXServer(self):
        r"""<p>Whether it is an mail exchange service</p>
        :rtype: bool
        """
        return self._IsMXServer

    @IsMXServer.setter
    def IsMXServer(self, IsMXServer):
        self._IsMXServer = IsMXServer


    def _deserialize(self, params):
        self._ISP = params.get("ISP")
        self._ASN = params.get("ASN")
        self._Organization = params.get("Organization")
        self._IsReserved = params.get("IsReserved")
        self._IsGateway = params.get("IsGateway")
        self._IsAnycast = params.get("IsAnycast")
        self._IsMobile = params.get("IsMobile")
        self._IsDynamic = params.get("IsDynamic")
        self._IsEgress = params.get("IsEgress")
        self._IsDNS = params.get("IsDNS")
        self._IsEducation = params.get("IsEducation")
        self._IsInstitution = params.get("IsInstitution")
        self._IsCompany = params.get("IsCompany")
        self._IsResidence = params.get("IsResidence")
        self._IsCloudService = params.get("IsCloudService")
        self._IsInfrastructure = params.get("IsInfrastructure")
        self._IsMXServer = params.get("IsMXServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvitationEvent(AbstractModel):
    r"""Invitation event details

    """

    def __init__(self):
        r"""
        :param _InviteeUserId: <p>The ID of the invitee</p>
        :type InviteeUserId: str
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviteePhone: <p>The phone number of the invitee</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number.</p>
        :type InviteePhone: str
        :param _InvitationCode: <p>The code that the inviter sent to the user</p>
        :type InvitationCode: str
        :param _InvitationUrl: <p>The url that the inviter sent to the user</p>
        :type InvitationUrl: str
        :param _InvitationChannel: <p>The channel that inviter used to invite the user </p>
        :type InvitationChannel: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._InviteeUserId = None
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviteePhone = None
        self._InvitationCode = None
        self._InvitationUrl = None
        self._InvitationChannel = None
        self._Cust = None

    @property
    def InviteeUserId(self):
        r"""<p>The ID of the invitee</p>
        :rtype: str
        """
        return self._InviteeUserId

    @InviteeUserId.setter
    def InviteeUserId(self, InviteeUserId):
        self._InviteeUserId = InviteeUserId

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviteePhone(self):
        r"""<p>The phone number of the invitee</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number.</p>
        :rtype: str
        """
        return self._InviteePhone

    @InviteePhone.setter
    def InviteePhone(self, InviteePhone):
        self._InviteePhone = InviteePhone

    @property
    def InvitationCode(self):
        r"""<p>The code that the inviter sent to the user</p>
        :rtype: str
        """
        return self._InvitationCode

    @InvitationCode.setter
    def InvitationCode(self, InvitationCode):
        self._InvitationCode = InvitationCode

    @property
    def InvitationUrl(self):
        r"""<p>The url that the inviter sent to the user</p>
        :rtype: str
        """
        return self._InvitationUrl

    @InvitationUrl.setter
    def InvitationUrl(self, InvitationUrl):
        self._InvitationUrl = InvitationUrl

    @property
    def InvitationChannel(self):
        r"""<p>The channel that inviter used to invite the user </p>
        :rtype: str
        """
        return self._InvitationChannel

    @InvitationChannel.setter
    def InvitationChannel(self, InvitationChannel):
        self._InvitationChannel = InvitationChannel

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._InviteeUserId = params.get("InviteeUserId")
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviteePhone = params.get("InviteePhone")
        self._InvitationCode = params.get("InvitationCode")
        self._InvitationUrl = params.get("InvitationUrl")
        self._InvitationChannel = params.get("InvitationChannel")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inviter(AbstractModel):
    r"""Inviter information

    """

    def __init__(self):
        r"""
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _InviterPhone: <p>The phone number of the inviter</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number.</p>
        :type InviterPhone: str
        :param _InviteCode: <p>The code that the inviter sent to the user</p>
        :type InviteCode: str
        :param _InviteChannel: <p>The channel that inviter used to invite the user</p>
        :type InviteChannel: str
        """
        self._InviterUserId = None
        self._InviterPhone = None
        self._InviteCode = None
        self._InviteChannel = None

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def InviterPhone(self):
        r"""<p>The phone number of the inviter</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number.</p>
        :rtype: str
        """
        return self._InviterPhone

    @InviterPhone.setter
    def InviterPhone(self, InviterPhone):
        self._InviterPhone = InviterPhone

    @property
    def InviteCode(self):
        r"""<p>The code that the inviter sent to the user</p>
        :rtype: str
        """
        return self._InviteCode

    @InviteCode.setter
    def InviteCode(self, InviteCode):
        self._InviteCode = InviteCode

    @property
    def InviteChannel(self):
        r"""<p>The channel that inviter used to invite the user</p>
        :rtype: str
        """
        return self._InviteChannel

    @InviteChannel.setter
    def InviteChannel(self, InviteChannel):
        self._InviteChannel = InviteChannel


    def _deserialize(self, params):
        self._InviterUserId = params.get("InviterUserId")
        self._InviterPhone = params.get("InviterPhone")
        self._InviteCode = params.get("InviteCode")
        self._InviteChannel = params.get("InviteChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Item(AbstractModel):
    r"""The details of the item

    """

    def __init__(self):
        r"""
        :param _ItemId: <p>The unique ID of the item</p>
        :type ItemId: str
        :param _ItemName: <p>The name of the item</p>
        :type ItemName: str
        :param _Category: <p>The category of the item</p>
        :type Category: str
        :param _Price: <p>The price of the item</p>
        :type Price: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _UPC: <p>If the item has a UPC (Universal Product Code), please provide it here.</p>
        :type UPC: str
        :param _EAN: <p>If the item has an EAN (European Article Number), please provide it here.</p>
        :type EAN: str
        :param _SKU: <p>If the item has an SKU (Stock Keeping Unit), please provide it here.</p>
        :type SKU: str
        :param _ISBN: <p>If the item has an ISBN (International Standard Book Number), please provide it here.</p>
        :type ISBN: str
        :param _Brand: <p>The brand of the item</p>
        :type Brand: str
        :param _Quantity: <p>The quantity of the item</p>
        :type Quantity: int
        :param _Manufacturer: <p>The manufacture of the item</p>
        :type Manufacturer: str
        :param _Tags: <p>The tags of the item in your system</p>
        :type Tags: str
        """
        self._ItemId = None
        self._ItemName = None
        self._Category = None
        self._Price = None
        self._UPC = None
        self._EAN = None
        self._SKU = None
        self._ISBN = None
        self._Brand = None
        self._Quantity = None
        self._Manufacturer = None
        self._Tags = None

    @property
    def ItemId(self):
        r"""<p>The unique ID of the item</p>
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemName(self):
        r"""<p>The name of the item</p>
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def Category(self):
        r"""<p>The category of the item</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Price(self):
        r"""<p>The price of the item</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def UPC(self):
        r"""<p>If the item has a UPC (Universal Product Code), please provide it here.</p>
        :rtype: str
        """
        return self._UPC

    @UPC.setter
    def UPC(self, UPC):
        self._UPC = UPC

    @property
    def EAN(self):
        r"""<p>If the item has an EAN (European Article Number), please provide it here.</p>
        :rtype: str
        """
        return self._EAN

    @EAN.setter
    def EAN(self, EAN):
        self._EAN = EAN

    @property
    def SKU(self):
        r"""<p>If the item has an SKU (Stock Keeping Unit), please provide it here.</p>
        :rtype: str
        """
        return self._SKU

    @SKU.setter
    def SKU(self, SKU):
        self._SKU = SKU

    @property
    def ISBN(self):
        r"""<p>If the item has an ISBN (International Standard Book Number), please provide it here.</p>
        :rtype: str
        """
        return self._ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @property
    def Brand(self):
        r"""<p>The brand of the item</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Quantity(self):
        r"""<p>The quantity of the item</p>
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Manufacturer(self):
        r"""<p>The manufacture of the item</p>
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def Tags(self):
        r"""<p>The tags of the item in your system</p>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemName = params.get("ItemName")
        self._Category = params.get("Category")
        if params.get("Price") is not None:
            self._Price = Amount()
            self._Price._deserialize(params.get("Price"))
        self._UPC = params.get("UPC")
        self._EAN = params.get("EAN")
        self._SKU = params.get("SKU")
        self._ISBN = params.get("ISBN")
        self._Brand = params.get("Brand")
        self._Quantity = params.get("Quantity")
        self._Manufacturer = params.get("Manufacturer")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginEvent(AbstractModel):
    r"""Login event detail

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>Basic user information</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _UserLoginName: <p>The user name entered when the user logged in</p>
        :type UserLoginName: str
        :param _LoginResult: <p>Login result</p>
        :type LoginResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._UserLoginName = None
        self._LoginResult = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>Basic user information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def UserLoginName(self):
        r"""<p>The user name entered when the user logged in</p>
        :rtype: str
        """
        return self._UserLoginName

    @UserLoginName.setter
    def UserLoginName(self, UserLoginName):
        self._UserLoginName = UserLoginName

    @property
    def LoginResult(self):
        r"""<p>Login result</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._LoginResult

    @LoginResult.setter
    def LoginResult(self, LoginResult):
        self._LoginResult = LoginResult

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._UserLoginName = params.get("UserLoginName")
        if params.get("LoginResult") is not None:
            self._LoginResult = Result()
            self._LoginResult._deserialize(params.get("LoginResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoutEvent(AbstractModel):
    r"""Logout event details

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>The detail information of the user</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _UserLoginName: <p>The user name entered when the user logged in</p>
        :type UserLoginName: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._UserLoginName = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>The detail information of the user</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def UserLoginName(self):
        r"""<p>The user name entered when the user logged in</p>
        :rtype: str
        """
        return self._UserLoginName

    @UserLoginName.setter
    def UserLoginName(self, UserLoginName):
        self._UserLoginName = UserLoginName

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._UserLoginName = params.get("UserLoginName")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LuckyDrawEvent(AbstractModel):
    r"""LuckyDraw event details

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _LuckyDrawCount: <p>Number of lucky draw</p><p>Unit: count</p>
        :type LuckyDrawCount: int
        :param _LuckyDrawType: <p>Type of lucky draw</p>
        :type LuckyDrawType: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._LuckyDrawCount = None
        self._LuckyDrawType = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def LuckyDrawCount(self):
        r"""<p>Number of lucky draw</p><p>Unit: count</p>
        :rtype: int
        """
        return self._LuckyDrawCount

    @LuckyDrawCount.setter
    def LuckyDrawCount(self, LuckyDrawCount):
        self._LuckyDrawCount = LuckyDrawCount

    @property
    def LuckyDrawType(self):
        r"""<p>Type of lucky draw</p>
        :rtype: str
        """
        return self._LuckyDrawType

    @LuckyDrawType.setter
    def LuckyDrawType(self, LuckyDrawType):
        self._LuckyDrawType = LuckyDrawType

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._LuckyDrawCount = params.get("LuckyDrawCount")
        self._LuckyDrawType = params.get("LuckyDrawType")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Merchant(AbstractModel):
    r"""The details of the merchant

    """

    def __init__(self):
        r"""
        :param _MerchantId: <p>The ID of the merchant</p>
        :type MerchantId: str
        :param _Name: <p>The name of the merchant</p>
        :type Name: str
        :param _RegisterTime: <p>Merchant registration time</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601</p>
        :type RegisterTime: str
        :param _Category: <p>Merchant category code</p><p>Parameter format: 4-digit No. compliant with ISO 18245</p>
        :type Category: str
        :param _Phone: <p>The phone number of the merchant</p><p>parameter format: format with "+", region code, and number that complies with the E.164 standard</p>
        :type Phone: str
        :param _Email: <p>The email of the merchant</p>
        :type Email: str
        :param _URL: <p>The url of the merchant shop on the website</p>
        :type URL: str
        :param _Address: <p>The address of the merchant</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Level: <p>The level of the merchant</p>
        :type Level: str
        :param _BusinessType: <p>The type of the merchant</p><p>Enumeration value:</p><ul><li>person: Person</li><li>company: Company</li></ul>
        :type BusinessType: str
        :param _GoodsQuantity: <p>The volume of goods on sale of the merchant</p>
        :type GoodsQuantity: int
        :param _HistoricSalesQuantity: <p>The historical sales volume of the merchant</p>
        :type HistoricSalesQuantity: int
        :param _HistoricSalesAmount: <p>The historical sales amount of the merchant</p>
        :type HistoricSalesAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        self._MerchantId = None
        self._Name = None
        self._RegisterTime = None
        self._Category = None
        self._Phone = None
        self._Email = None
        self._URL = None
        self._Address = None
        self._Level = None
        self._BusinessType = None
        self._GoodsQuantity = None
        self._HistoricSalesQuantity = None
        self._HistoricSalesAmount = None

    @property
    def MerchantId(self):
        r"""<p>The ID of the merchant</p>
        :rtype: str
        """
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def Name(self):
        r"""<p>The name of the merchant</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RegisterTime(self):
        r"""<p>Merchant registration time</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601</p>
        :rtype: str
        """
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def Category(self):
        r"""<p>Merchant category code</p><p>Parameter format: 4-digit No. compliant with ISO 18245</p>
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Phone(self):
        r"""<p>The phone number of the merchant</p><p>parameter format: format with "+", region code, and number that complies with the E.164 standard</p>
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Email(self):
        r"""<p>The email of the merchant</p>
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def URL(self):
        r"""<p>The url of the merchant shop on the website</p>
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Address(self):
        r"""<p>The address of the merchant</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Level(self):
        r"""<p>The level of the merchant</p>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def BusinessType(self):
        r"""<p>The type of the merchant</p><p>Enumeration value:</p><ul><li>person: Person</li><li>company: Company</li></ul>
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def GoodsQuantity(self):
        r"""<p>The volume of goods on sale of the merchant</p>
        :rtype: int
        """
        return self._GoodsQuantity

    @GoodsQuantity.setter
    def GoodsQuantity(self, GoodsQuantity):
        self._GoodsQuantity = GoodsQuantity

    @property
    def HistoricSalesQuantity(self):
        r"""<p>The historical sales volume of the merchant</p>
        :rtype: int
        """
        return self._HistoricSalesQuantity

    @HistoricSalesQuantity.setter
    def HistoricSalesQuantity(self, HistoricSalesQuantity):
        self._HistoricSalesQuantity = HistoricSalesQuantity

    @property
    def HistoricSalesAmount(self):
        r"""<p>The historical sales amount of the merchant</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._HistoricSalesAmount

    @HistoricSalesAmount.setter
    def HistoricSalesAmount(self, HistoricSalesAmount):
        self._HistoricSalesAmount = HistoricSalesAmount


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._Name = params.get("Name")
        self._RegisterTime = params.get("RegisterTime")
        self._Category = params.get("Category")
        self._Phone = params.get("Phone")
        self._Email = params.get("Email")
        self._URL = params.get("URL")
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        self._Level = params.get("Level")
        self._BusinessType = params.get("BusinessType")
        self._GoodsQuantity = params.get("GoodsQuantity")
        self._HistoricSalesQuantity = params.get("HistoricSalesQuantity")
        if params.get("HistoricSalesAmount") is not None:
            self._HistoricSalesAmount = Amount()
            self._HistoricSalesAmount._deserialize(params.get("HistoricSalesAmount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountEvent(AbstractModel):
    r"""ModifyAccount event details

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>The detail information of the user</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _Person: <p>The personal information of the account when registered</p>
        :type Person: :class:`tencentcloud.rce.v20260130.models.Person`
        :param _BillingAddress: <p>The billing address the user provided when registered</p>
        :type BillingAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DeliveryAddress: <p>The delivery address the user provided when registered</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._Person = None
        self._BillingAddress = None
        self._DeliveryAddress = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>The detail information of the user</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Person(self):
        r"""<p>The personal information of the account when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Person`
        """
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def BillingAddress(self):
        r"""<p>The billing address the user provided when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._BillingAddress

    @BillingAddress.setter
    def BillingAddress(self, BillingAddress):
        self._BillingAddress = BillingAddress

    @property
    def DeliveryAddress(self):
        r"""<p>The delivery address the user provided when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Person") is not None:
            self._Person = Person()
            self._Person._deserialize(params.get("Person"))
        if params.get("BillingAddress") is not None:
            self._BillingAddress = Address()
            self._BillingAddress._deserialize(params.get("BillingAddress"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordEvent(AbstractModel):
    r"""ModifyPassword event details

    """

    def __init__(self):
        r"""
        :param _Reason: <p>The reason why the password was updated</p><p>Enumeration value:</p><ul><li>user_modify: User self-initiated modification</li><li>forgot_password: Forget password</li><li>forced_reset: System forcing reset</li></ul>
        :type Reason: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._Reason = None
        self._Cust = None

    @property
    def Reason(self):
        r"""<p>The reason why the password was updated</p><p>Enumeration value:</p><ul><li>user_modify: User self-initiated modification</li><li>forgot_password: Forget password</li><li>forced_reset: System forcing reset</li></ul>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    r"""The details of the order

    """

    def __init__(self):
        r"""
        :param _OrderId: <p>The ID of the order</p>
        :type OrderId: str
        :param _Amount: <p>The amount of the order</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Items: <p>The detail information of the items in the order</p>
        :type Items: list of Item
        :param _Delivery: <p>The detail information of the delivery associated with the order</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        self._OrderId = None
        self._Amount = None
        self._Items = None
        self._Delivery = None

    @property
    def OrderId(self):
        r"""<p>The ID of the order</p>
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Amount(self):
        r"""<p>The amount of the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Items(self):
        r"""<p>The detail information of the items in the order</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Delivery(self):
        r"""<p>The detail information of the delivery associated with the order</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentMethod(AbstractModel):
    r"""Payment method

    """

    def __init__(self):
        r"""
        :param _PaymentType: <p>Payment method</p><p>Enumeration value:</p><ul><li>cash</li><li>check</li><li>credit_card</li><li>debit_card</li><li>crypto_currency</li><li>digital_wallet</li><li>gift_card</li><li>points</li><li>in_app_purchase</li><li>electronic_fund_transfer</li><li>financing</li><li>invoice</li><li>prepaid_card</li><li>sepa_credit</li></ul>
        :type PaymentType: str
        :param _PaymentChannel: <p>The channel of the payment</p>
        :type PaymentChannel: str
        :param _Card: <p>The details of the card.Required while PaymentMethod is "credit_card","debit_card"</p>
        :type Card: :class:`tencentcloud.rce.v20260130.models.Card`
        :param _SEPADirectDebitMandate: <p>SEPA direct debit mandate</p><p>Enumeration value:</p><ul><li>true: Yes</li><li>false: No</li></ul>
        :type SEPADirectDebitMandate: bool
        :param _DigitalWallet: <p>The details of the digital wallet when involved digital trade</p>
        :type DigitalWallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        self._PaymentType = None
        self._PaymentChannel = None
        self._Card = None
        self._SEPADirectDebitMandate = None
        self._DigitalWallet = None

    @property
    def PaymentType(self):
        r"""<p>Payment method</p><p>Enumeration value:</p><ul><li>cash</li><li>check</li><li>credit_card</li><li>debit_card</li><li>crypto_currency</li><li>digital_wallet</li><li>gift_card</li><li>points</li><li>in_app_purchase</li><li>electronic_fund_transfer</li><li>financing</li><li>invoice</li><li>prepaid_card</li><li>sepa_credit</li></ul>
        :rtype: str
        """
        return self._PaymentType

    @PaymentType.setter
    def PaymentType(self, PaymentType):
        self._PaymentType = PaymentType

    @property
    def PaymentChannel(self):
        r"""<p>The channel of the payment</p>
        :rtype: str
        """
        return self._PaymentChannel

    @PaymentChannel.setter
    def PaymentChannel(self, PaymentChannel):
        self._PaymentChannel = PaymentChannel

    @property
    def Card(self):
        r"""<p>The details of the card.Required while PaymentMethod is "credit_card","debit_card"</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Card`
        """
        return self._Card

    @Card.setter
    def Card(self, Card):
        self._Card = Card

    @property
    def SEPADirectDebitMandate(self):
        r"""<p>SEPA direct debit mandate</p><p>Enumeration value:</p><ul><li>true: Yes</li><li>false: No</li></ul>
        :rtype: bool
        """
        return self._SEPADirectDebitMandate

    @SEPADirectDebitMandate.setter
    def SEPADirectDebitMandate(self, SEPADirectDebitMandate):
        self._SEPADirectDebitMandate = SEPADirectDebitMandate

    @property
    def DigitalWallet(self):
        r"""<p>The details of the digital wallet when involved digital trade</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._DigitalWallet

    @DigitalWallet.setter
    def DigitalWallet(self, DigitalWallet):
        self._DigitalWallet = DigitalWallet


    def _deserialize(self, params):
        self._PaymentType = params.get("PaymentType")
        self._PaymentChannel = params.get("PaymentChannel")
        if params.get("Card") is not None:
            self._Card = Card()
            self._Card._deserialize(params.get("Card"))
        self._SEPADirectDebitMandate = params.get("SEPADirectDebitMandate")
        if params.get("DigitalWallet") is not None:
            self._DigitalWallet = Wallet()
            self._DigitalWallet._deserialize(params.get("DigitalWallet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentResult(AbstractModel):
    r"""Payment result

    """

    def __init__(self):
        r"""
        :param _Status: <p>The status of the payment</p><p>Enumeration values: </p><ul><li>success: Success, </li><li>failure: Failure.</li></ul>
        :type Status: str
        :param _FailureReason: <p>The reason why the payment has been declined. e.g.card_declined</p>
        :type FailureReason: str
        :param _ThreeDomainSecure: <p>Whether the 3DS has been used in the payment,  enumeration value:</p><ul><li>Yes: true</li><li>No: false</li></ul>
        :type ThreeDomainSecure: bool
        :param _ECICode: <p>The ECI code returned when 3DS used</p>
        :type ECICode: str
        :param _AVSCode: <p>Response code from the AVS used for address verification</p>
        :type AVSCode: str
        :param _CVCCode: <p>Response code from the CVC used for payment authenticity</p>
        :type CVCCode: str
        """
        self._Status = None
        self._FailureReason = None
        self._ThreeDomainSecure = None
        self._ECICode = None
        self._AVSCode = None
        self._CVCCode = None

    @property
    def Status(self):
        r"""<p>The status of the payment</p><p>Enumeration values: </p><ul><li>success: Success, </li><li>failure: Failure.</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        r"""<p>The reason why the payment has been declined. e.g.card_declined</p>
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def ThreeDomainSecure(self):
        r"""<p>Whether the 3DS has been used in the payment,  enumeration value:</p><ul><li>Yes: true</li><li>No: false</li></ul>
        :rtype: bool
        """
        return self._ThreeDomainSecure

    @ThreeDomainSecure.setter
    def ThreeDomainSecure(self, ThreeDomainSecure):
        self._ThreeDomainSecure = ThreeDomainSecure

    @property
    def ECICode(self):
        r"""<p>The ECI code returned when 3DS used</p>
        :rtype: str
        """
        return self._ECICode

    @ECICode.setter
    def ECICode(self, ECICode):
        self._ECICode = ECICode

    @property
    def AVSCode(self):
        r"""<p>Response code from the AVS used for address verification</p>
        :rtype: str
        """
        return self._AVSCode

    @AVSCode.setter
    def AVSCode(self, AVSCode):
        self._AVSCode = AVSCode

    @property
    def CVCCode(self):
        r"""<p>Response code from the CVC used for payment authenticity</p>
        :rtype: str
        """
        return self._CVCCode

    @CVCCode.setter
    def CVCCode(self, CVCCode):
        self._CVCCode = CVCCode


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        self._ThreeDomainSecure = params.get("ThreeDomainSecure")
        self._ECICode = params.get("ECICode")
        self._AVSCode = params.get("AVSCode")
        self._CVCCode = params.get("CVCCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Person(AbstractModel):
    r"""Personal information

    """

    def __init__(self):
        r"""
        :param _Name: <p>The full name of the user if provided</p>
        :type Name: str
        :param _Gender: <p>The gender of the user if provided</p>
        :type Gender: str
        :param _Birthday: <p>The birthday of the user if provided</p><p>Parameter format: YYYY-MM-DD.</p>
        :type Birthday: str
        :param _Degree: <p>The degree of the user if provided</p>
        :type Degree: str
        :param _Occupation: <p>The occupation of the user if provided</p>
        :type Occupation: str
        """
        self._Name = None
        self._Gender = None
        self._Birthday = None
        self._Degree = None
        self._Occupation = None

    @property
    def Name(self):
        r"""<p>The full name of the user if provided</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Gender(self):
        r"""<p>The gender of the user if provided</p>
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Birthday(self):
        r"""<p>The birthday of the user if provided</p><p>Parameter format: YYYY-MM-DD.</p>
        :rtype: str
        """
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Degree(self):
        r"""<p>The degree of the user if provided</p>
        :rtype: str
        """
        return self._Degree

    @Degree.setter
    def Degree(self, Degree):
        self._Degree = Degree

    @property
    def Occupation(self):
        r"""<p>The occupation of the user if provided</p>
        :rtype: str
        """
        return self._Occupation

    @Occupation.setter
    def Occupation(self, Occupation):
        self._Occupation = Occupation


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Gender = params.get("Gender")
        self._Birthday = params.get("Birthday")
        self._Degree = params.get("Degree")
        self._Occupation = params.get("Occupation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Promotion(AbstractModel):
    r"""The details of the promotion

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _Coupon: <p>The coupon(s) associated with the promotion</p>
        :type Coupon: :class:`tencentcloud.rce.v20260130.models.Coupon`
        :param _CreditPoint: <p>The point(s) associated with the promotion</p>
        :type CreditPoint: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Coupon = None
        self._CreditPoint = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Coupon(self):
        r"""<p>The coupon(s) associated with the promotion</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Coupon`
        """
        return self._Coupon

    @Coupon.setter
    def Coupon(self, Coupon):
        self._Coupon = Coupon

    @property
    def CreditPoint(self):
        r"""<p>The point(s) associated with the promotion</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._CreditPoint

    @CreditPoint.setter
    def CreditPoint(self, CreditPoint):
        self._CreditPoint = CreditPoint


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Coupon") is not None:
            self._Coupon = Coupon()
            self._Coupon._deserialize(params.get("Coupon"))
        if params.get("CreditPoint") is not None:
            self._CreditPoint = CreditPoint()
            self._CreditPoint._deserialize(params.get("CreditPoint"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PromotionCode(AbstractModel):
    r"""The details of the promotion code

    """

    def __init__(self):
        r"""
        :param _Id: <p>The ID of the promotion code</p>
        :type Id: str
        :param _Type: <p>The type of the promotion code, for example: qrcode, barcode, miniprogram code</p>
        :type Type: str
        :param _ImageLink: <p>The url or hyperlink to the image</p>
        :type ImageLink: str
        :param _Address: <p>The address where the promotion code worked</p>
        :type Address: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Items: <p>The item(s) associated with the promotion code</p>
        :type Items: list of Item
        """
        self._Id = None
        self._Type = None
        self._ImageLink = None
        self._Address = None
        self._Items = None

    @property
    def Id(self):
        r"""<p>The ID of the promotion code</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""<p>The type of the promotion code, for example: qrcode, barcode, miniprogram code</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ImageLink(self):
        r"""<p>The url or hyperlink to the image</p>
        :rtype: str
        """
        return self._ImageLink

    @ImageLink.setter
    def ImageLink(self, ImageLink):
        self._ImageLink = ImageLink

    @property
    def Address(self):
        r"""<p>The address where the promotion code worked</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Items(self):
        r"""<p>The item(s) associated with the promotion code</p>
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._ImageLink = params.get("ImageLink")
        if params.get("Address") is not None:
            self._Address = Address()
            self._Address._deserialize(params.get("Address"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeemEvent(AbstractModel):
    r"""Redeem event details

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _Order: <p>Order information associated with the redemption</p>
        :type Order: :class:`tencentcloud.rce.v20260130.models.Order`
        :param _Result: <p>The result of redemption</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Order = None
        self._Result = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Order(self):
        r"""<p>Order information associated with the redemption</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Order`
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Result(self):
        r"""<p>The result of redemption</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Order") is not None:
            self._Order = Order()
            self._Order._deserialize(params.get("Order"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterEvent(AbstractModel):
    r"""Register event details

    """

    def __init__(self):
        r"""
        :param _RegisterResult: <p>The result of the register</p>
        :type RegisterResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _UserInfo: <p>The detail information of the user</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _Person: <p>The personal information of the account when registered</p>
        :type Person: :class:`tencentcloud.rce.v20260130.models.Person`
        :param _BillingAddress: <p>The billing address the user provided when registered</p>
        :type BillingAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DeliveryAddress: <p>The delivery address the user provided when registered</p>
        :type DeliveryAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _Inviter: <p>The detail information of the inviter who invited the user to your business</p>
        :type Inviter: :class:`tencentcloud.rce.v20260130.models.Inviter`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._RegisterResult = None
        self._UserInfo = None
        self._Person = None
        self._BillingAddress = None
        self._DeliveryAddress = None
        self._Inviter = None
        self._Cust = None

    @property
    def RegisterResult(self):
        r"""<p>The result of the register</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._RegisterResult

    @RegisterResult.setter
    def RegisterResult(self, RegisterResult):
        self._RegisterResult = RegisterResult

    @property
    def UserInfo(self):
        r"""<p>The detail information of the user</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Person(self):
        r"""<p>The personal information of the account when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Person`
        """
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def BillingAddress(self):
        r"""<p>The billing address the user provided when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._BillingAddress

    @BillingAddress.setter
    def BillingAddress(self, BillingAddress):
        self._BillingAddress = BillingAddress

    @property
    def DeliveryAddress(self):
        r"""<p>The delivery address the user provided when registered</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._DeliveryAddress

    @DeliveryAddress.setter
    def DeliveryAddress(self, DeliveryAddress):
        self._DeliveryAddress = DeliveryAddress

    @property
    def Inviter(self):
        r"""<p>The detail information of the inviter who invited the user to your business</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Inviter`
        """
        return self._Inviter

    @Inviter.setter
    def Inviter(self, Inviter):
        self._Inviter = Inviter

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("RegisterResult") is not None:
            self._RegisterResult = Result()
            self._RegisterResult._deserialize(params.get("RegisterResult"))
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Person") is not None:
            self._Person = Person()
            self._Person._deserialize(params.get("Person"))
        if params.get("BillingAddress") is not None:
            self._BillingAddress = Address()
            self._BillingAddress._deserialize(params.get("BillingAddress"))
        if params.get("DeliveryAddress") is not None:
            self._DeliveryAddress = Address()
            self._DeliveryAddress._deserialize(params.get("DeliveryAddress"))
        if params.get("Inviter") is not None:
            self._Inviter = Inviter()
            self._Inviter._deserialize(params.get("Inviter"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportEventRequest(AbstractModel):
    r"""ReportEvent request structure.

    """

    def __init__(self):
        r"""
        :param _EventCode: <p>Event code. Used to specify the scenario node for business access.</p><p> Standard events under the account protection product include:</p><ul><li> login: Log in<p></p></li> <li>register: Register </li><li>sms: SMS </li><li>logout: Log out </li><li>modify_account: Modify account </li><li>modify_password: Modify password </li><li>security_verification: Security verification</li></ul><p>Standard events under the payment protection product include:</p><ul><li>create_order: Create an order</li><li>transaction: Transaction</li><li>charge_back: Chargeback</li></ul><p>Standard events under the promotion protection product include:</p><ul><li>add_promotion: Participate in promotions </li><li>redeem: Redeem a prize </li><li>withdraw: Withdraw</li><li>cust_event: Custom event, cust_xxx </li><li>scan_code: Scan a code </li><li>lucky_draw: Lucky draw </li><li>task: Complete a task </li><li>invitation: Invitation </li><li>claim_red_packet: Receive a red packet </li><li>browse: Browse</li></ul><p>Custom events can be evaluated for risk based on an agreement with RCE</p>
        :type EventCode: str
        :param _EventTime: <p>The time when the event occurred</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with the ISO 8601 standard</p>
        :type EventTime: str
        :param _SessionId: <p>The user's current session ID used to associate with the actions before and after logging in. If UserId is not passed, SessionId is required. If missing, an empty string can be filled.</p>
        :type SessionId: str
        :param _DeviceToken: <p>The token provided by the SDK integrated in your web site or application</p>
        :type DeviceToken: str
        :param _UserIp: <p>User client IP address (IPv4 or IPv6)</p>
        :type UserIp: str
        :param _EventDetail: <p>Event details, import corresponding event information based on the event code you input</p>
        :type EventDetail: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        :param _UserId: <p>The user's account ID in your system</p>
        :type UserId: str
        :param _UserEmail: <p>Email of the user</p>
        :type UserEmail: str
        :param _UserPhone: <p>Phone number of the user</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number</p>
        :type UserPhone: str
        :param _Browser: <p>The details of the browser. If you've already integrated our device SDK, this field is not required</p>
        :type Browser: :class:`tencentcloud.rce.v20260130.models.Browser`
        :param _App: <p>The details of the app, os and device.If you've already integrated our device SDK, this field is not required</p>
        :type App: :class:`tencentcloud.rce.v20260130.models.App`
        """
        self._EventCode = None
        self._EventTime = None
        self._SessionId = None
        self._DeviceToken = None
        self._UserIp = None
        self._EventDetail = None
        self._UserId = None
        self._UserEmail = None
        self._UserPhone = None
        self._Browser = None
        self._App = None

    @property
    def EventCode(self):
        r"""<p>Event code. Used to specify the scenario node for business access.</p><p> Standard events under the account protection product include:</p><ul><li> login: Log in<p></p></li> <li>register: Register </li><li>sms: SMS </li><li>logout: Log out </li><li>modify_account: Modify account </li><li>modify_password: Modify password </li><li>security_verification: Security verification</li></ul><p>Standard events under the payment protection product include:</p><ul><li>create_order: Create an order</li><li>transaction: Transaction</li><li>charge_back: Chargeback</li></ul><p>Standard events under the promotion protection product include:</p><ul><li>add_promotion: Participate in promotions </li><li>redeem: Redeem a prize </li><li>withdraw: Withdraw</li><li>cust_event: Custom event, cust_xxx </li><li>scan_code: Scan a code </li><li>lucky_draw: Lucky draw </li><li>task: Complete a task </li><li>invitation: Invitation </li><li>claim_red_packet: Receive a red packet </li><li>browse: Browse</li></ul><p>Custom events can be evaluated for risk based on an agreement with RCE</p>
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventTime(self):
        r"""<p>The time when the event occurred</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with the ISO 8601 standard</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def SessionId(self):
        r"""<p>The user's current session ID used to associate with the actions before and after logging in. If UserId is not passed, SessionId is required. If missing, an empty string can be filled.</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def DeviceToken(self):
        r"""<p>The token provided by the SDK integrated in your web site or application</p>
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def UserIp(self):
        r"""<p>User client IP address (IPv4 or IPv6)</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def EventDetail(self):
        r"""<p>Event details, import corresponding event information based on the event code you input</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.EventDetail`
        """
        return self._EventDetail

    @EventDetail.setter
    def EventDetail(self, EventDetail):
        self._EventDetail = EventDetail

    @property
    def UserId(self):
        r"""<p>The user's account ID in your system</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserEmail(self):
        r"""<p>Email of the user</p>
        :rtype: str
        """
        return self._UserEmail

    @UserEmail.setter
    def UserEmail(self, UserEmail):
        self._UserEmail = UserEmail

    @property
    def UserPhone(self):
        r"""<p>Phone number of the user</p><p>Parameter format: Complies with the E.164 standard format, which includes "+", region code, and number</p>
        :rtype: str
        """
        return self._UserPhone

    @UserPhone.setter
    def UserPhone(self, UserPhone):
        self._UserPhone = UserPhone

    @property
    def Browser(self):
        r"""<p>The details of the browser. If you've already integrated our device SDK, this field is not required</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Browser`
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def App(self):
        r"""<p>The details of the app, os and device.If you've already integrated our device SDK, this field is not required</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.App`
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventTime = params.get("EventTime")
        self._SessionId = params.get("SessionId")
        self._DeviceToken = params.get("DeviceToken")
        self._UserIp = params.get("UserIp")
        if params.get("EventDetail") is not None:
            self._EventDetail = EventDetail()
            self._EventDetail._deserialize(params.get("EventDetail"))
        self._UserId = params.get("UserId")
        self._UserEmail = params.get("UserEmail")
        self._UserPhone = params.get("UserPhone")
        if params.get("Browser") is not None:
            self._Browser = Browser()
            self._Browser._deserialize(params.get("Browser"))
        if params.get("App") is not None:
            self._App = App()
            self._App._deserialize(params.get("App"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportEventResponse(AbstractModel):
    r"""ReportEvent response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Result(AbstractModel):
    r"""Event result

    """

    def __init__(self):
        r"""
        :param _Status: <p>Actual completion status</p><p>Enumeration values:</p><ul><li>success: Success,</li><li>failure: Failure.</li></ul>
        :type Status: str
        :param _FailureReason: <p>Failure reason</p>
        :type FailureReason: str
        """
        self._Status = None
        self._FailureReason = None

    @property
    def Status(self):
        r"""<p>Actual completion status</p><p>Enumeration values:</p><ul><li>success: Success,</li><li>failure: Failure.</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        r"""<p>Failure reason</p>
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskLabel(AbstractModel):
    r"""Risk label

    """

    def __init__(self):
        r"""
        :param _Id: <p>The ID of the label</p>
        :type Id: str
        :param _Reason: <p>The reason of the label</p>
        :type Reason: str
        """
        self._Id = None
        self._Reason = None

    @property
    def Id(self):
        r"""<p>The ID of the label</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Reason(self):
        r"""<p>The reason of the label</p>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SMSEvent(AbstractModel):
    r"""SMS event details

    """

    def __init__(self):
        r"""
        :param _UserInfo: <p>The detail information of the user</p>
        :type UserInfo: :class:`tencentcloud.rce.v20260130.models.User`
        :param _SMSId: <p>The unique ID of the sms</p>
        :type SMSId: str
        :param _ReceivedTime: <p>The time that the user received the sms</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601 standard</p>
        :type ReceivedTime: str
        :param _Action: <p>The action of the user after receiving the sms</p><ul><li>no_action: No action from the user</li><li>safe: User confirmation of the correct person's action</li><li>compromised: Feedback from real users indicates third-party action</li></ul>
        :type Action: str
        :param _SMSResult: <p>The result of the sms</p>
        :type SMSResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._UserInfo = None
        self._SMSId = None
        self._ReceivedTime = None
        self._Action = None
        self._SMSResult = None
        self._Cust = None

    @property
    def UserInfo(self):
        r"""<p>The detail information of the user</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.User`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def SMSId(self):
        r"""<p>The unique ID of the sms</p>
        :rtype: str
        """
        return self._SMSId

    @SMSId.setter
    def SMSId(self, SMSId):
        self._SMSId = SMSId

    @property
    def ReceivedTime(self):
        r"""<p>The time that the user received the sms</p><p>Parameter format: Millisecond-level time with UTC time zone compliant with ISO 8601 standard</p>
        :rtype: str
        """
        return self._ReceivedTime

    @ReceivedTime.setter
    def ReceivedTime(self, ReceivedTime):
        self._ReceivedTime = ReceivedTime

    @property
    def Action(self):
        r"""<p>The action of the user after receiving the sms</p><ul><li>no_action: No action from the user</li><li>safe: User confirmation of the correct person's action</li><li>compromised: Feedback from real users indicates third-party action</li></ul>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def SMSResult(self):
        r"""<p>The result of the sms</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._SMSResult

    @SMSResult.setter
    def SMSResult(self, SMSResult):
        self._SMSResult = SMSResult

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = User()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._SMSId = params.get("SMSId")
        self._ReceivedTime = params.get("ReceivedTime")
        self._Action = params.get("Action")
        if params.get("SMSResult") is not None:
            self._SMSResult = Result()
            self._SMSResult._deserialize(params.get("SMSResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanCodeEvent(AbstractModel):
    r"""ScanCode event details

    """

    def __init__(self):
        r"""
        :param _PromotionCode: <p>Promotion code information</p>
        :type PromotionCode: :class:`tencentcloud.rce.v20260130.models.PromotionCode`
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionCode = None
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._Cust = None

    @property
    def PromotionCode(self):
        r"""<p>Promotion code information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PromotionCode`
        """
        return self._PromotionCode

    @PromotionCode.setter
    def PromotionCode(self, PromotionCode):
        self._PromotionCode = PromotionCode

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("PromotionCode") is not None:
            self._PromotionCode = PromotionCode()
            self._PromotionCode._deserialize(params.get("PromotionCode"))
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityVerificationEvent(AbstractModel):
    r"""SecurityVerification event details

    """

    def __init__(self):
        r"""
        :param _VerificationEvent: <p>The event type being verified</p><p>Enumeration values:</p><ul><li>register</li><li>login</li><li>modify_account</li><li>modify_password</li><li>create_order</li><li>transaction</li><li>modify_order</li><li>withdraw</li><li>add_promotion</li><li>redeem</li></ul>
        :type VerificationEvent: str
        :param _VerificationType: <p>The type of security verification: sms, phone call, email, captcha, shared knowledge, human face, fingerprint, etc</p>
        :type VerificationType: str
        :param _VerificationContent: <p>The content of the security verifcation.This value should be passed when the verification type is set to sms, phone_call, email captcha or shared_knowledge</p>
        :type VerificationContent: str
        :param _VerificationResult: <p>The result of security verification</p>
        :type VerificationResult: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._VerificationEvent = None
        self._VerificationType = None
        self._VerificationContent = None
        self._VerificationResult = None
        self._Cust = None

    @property
    def VerificationEvent(self):
        r"""<p>The event type being verified</p><p>Enumeration values:</p><ul><li>register</li><li>login</li><li>modify_account</li><li>modify_password</li><li>create_order</li><li>transaction</li><li>modify_order</li><li>withdraw</li><li>add_promotion</li><li>redeem</li></ul>
        :rtype: str
        """
        return self._VerificationEvent

    @VerificationEvent.setter
    def VerificationEvent(self, VerificationEvent):
        self._VerificationEvent = VerificationEvent

    @property
    def VerificationType(self):
        r"""<p>The type of security verification: sms, phone call, email, captcha, shared knowledge, human face, fingerprint, etc</p>
        :rtype: str
        """
        return self._VerificationType

    @VerificationType.setter
    def VerificationType(self, VerificationType):
        self._VerificationType = VerificationType

    @property
    def VerificationContent(self):
        r"""<p>The content of the security verifcation.This value should be passed when the verification type is set to sms, phone_call, email captcha or shared_knowledge</p>
        :rtype: str
        """
        return self._VerificationContent

    @VerificationContent.setter
    def VerificationContent(self, VerificationContent):
        self._VerificationContent = VerificationContent

    @property
    def VerificationResult(self):
        r"""<p>The result of security verification</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._VerificationResult

    @VerificationResult.setter
    def VerificationResult(self, VerificationResult):
        self._VerificationResult = VerificationResult

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._VerificationEvent = params.get("VerificationEvent")
        self._VerificationType = params.get("VerificationType")
        self._VerificationContent = params.get("VerificationContent")
        if params.get("VerificationResult") is not None:
            self._VerificationResult = Result()
            self._VerificationResult._deserialize(params.get("VerificationResult"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskEvent(AbstractModel):
    r"""Task event details

    """

    def __init__(self):
        r"""
        :param _PromotionId: <p>The ID of the promotion</p>
        :type PromotionId: str
        :param _PromotionName: <p>The name of the promotion</p>
        :type PromotionName: str
        :param _Description: <p>The description of the promotion</p>
        :type Description: str
        :param _InviterUserId: <p>The ID of the inviter</p>
        :type InviterUserId: str
        :param _TaskId: <p>The ID of the task</p>
        :type TaskId: str
        :param _TaskName: <p>The name of the task</p>
        :type TaskName: str
        :param _TaskType: <p>Task type, such as daily check-in, ad viewing, or step accumulation</p>
        :type TaskType: str
        :param _TaskCostTime: <p>Task completed duration</p><p>Measurement unit: ms</p>
        :type TaskCostTime: int
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._PromotionId = None
        self._PromotionName = None
        self._Description = None
        self._InviterUserId = None
        self._TaskId = None
        self._TaskName = None
        self._TaskType = None
        self._TaskCostTime = None
        self._Cust = None

    @property
    def PromotionId(self):
        r"""<p>The ID of the promotion</p>
        :rtype: str
        """
        return self._PromotionId

    @PromotionId.setter
    def PromotionId(self, PromotionId):
        self._PromotionId = PromotionId

    @property
    def PromotionName(self):
        r"""<p>The name of the promotion</p>
        :rtype: str
        """
        return self._PromotionName

    @PromotionName.setter
    def PromotionName(self, PromotionName):
        self._PromotionName = PromotionName

    @property
    def Description(self):
        r"""<p>The description of the promotion</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InviterUserId(self):
        r"""<p>The ID of the inviter</p>
        :rtype: str
        """
        return self._InviterUserId

    @InviterUserId.setter
    def InviterUserId(self, InviterUserId):
        self._InviterUserId = InviterUserId

    @property
    def TaskId(self):
        r"""<p>The ID of the task</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""<p>The name of the task</p>
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        r"""<p>Task type, such as daily check-in, ad viewing, or step accumulation</p>
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskCostTime(self):
        r"""<p>Task completed duration</p><p>Measurement unit: ms</p>
        :rtype: int
        """
        return self._TaskCostTime

    @TaskCostTime.setter
    def TaskCostTime(self, TaskCostTime):
        self._TaskCostTime = TaskCostTime

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._PromotionId = params.get("PromotionId")
        self._PromotionName = params.get("PromotionName")
        self._Description = params.get("Description")
        self._InviterUserId = params.get("InviterUserId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        self._TaskCostTime = params.get("TaskCostTime")
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionEvent(AbstractModel):
    r"""Transaction event details

    """

    def __init__(self):
        r"""
        :param _TransactionId: <p>The unique ID of the transaction</p>
        :type TransactionId: str
        :param _OrderId: <p>The ID(s) of the order associated with the transaction</p>
        :type OrderId: list of str
        :param _PaymentAmount: <p>The amount of the transaction</p>
        :type PaymentAmount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _PaymentMethod: <p>The detail information of the payment method associated with the transaction</p>
        :type PaymentMethod: :class:`tencentcloud.rce.v20260130.models.PaymentMethod`
        :param _TransactionType: <p>Transaction type</p><p>Enumeration value:</p><ul><li>sale: One-time authorization and deduction (most common)</li><li>authorize: Authorization only (frozen amount)</li><li>capture: Execute deduction (after authorization)</li><li>void: Cancel pending authorization or deduction</li><li>refund: Refund (part or all)</li><li>deposit: Deposit to account</li><li>withdrawal: Withdrawal from account</li><li>transfer: Fund transfer between accounts</li><li>buy: Purchase asset (for example, crypto currency)</li><li>sell: Sell asset</li><li>send: Send fund/asset (for example, cross-wallet transfer)</li><li>receive: Receive fund/asset</li></ul><p>Default value: sale</p>
        :type TransactionType: str
        :param _Billing: <p>Bill information</p>
        :type Billing: :class:`tencentcloud.rce.v20260130.models.Billing`
        :param _Delivery: <p>Delivery information</p>
        :type Delivery: :class:`tencentcloud.rce.v20260130.models.Delivery`
        :param _Merchant: <p>Merchant information</p>
        :type Merchant: :class:`tencentcloud.rce.v20260130.models.Merchant`
        :param _PaymentResult: <p>Payment result</p>
        :type PaymentResult: :class:`tencentcloud.rce.v20260130.models.PaymentResult`
        :param _TransferRecipientUserId: <p>The ID of the recipent in transfer transaction</p>
        :type TransferRecipientUserId: str
        :param _TransferSentAddress: <p>The address of the sender in transfer transaction</p>
        :type TransferSentAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _TransferReceivedAddress: <p>Physical address of the recipient, applicable to the transfer transaction type.</p>
        :type TransferReceivedAddress: :class:`tencentcloud.rce.v20260130.models.Address`
        :param _DigitalOrders: <p>The digital order(s) associated with the transaction</p>
        :type DigitalOrders: list of DigitalOrder
        :param _ReceiverWallet: <p>Wallet to receive crypto currency</p>
        :type ReceiverWallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._TransactionId = None
        self._OrderId = None
        self._PaymentAmount = None
        self._PaymentMethod = None
        self._TransactionType = None
        self._Billing = None
        self._Delivery = None
        self._Merchant = None
        self._PaymentResult = None
        self._TransferRecipientUserId = None
        self._TransferSentAddress = None
        self._TransferReceivedAddress = None
        self._DigitalOrders = None
        self._ReceiverWallet = None
        self._Cust = None

    @property
    def TransactionId(self):
        r"""<p>The unique ID of the transaction</p>
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def OrderId(self):
        r"""<p>The ID(s) of the order associated with the transaction</p>
        :rtype: list of str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PaymentAmount(self):
        r"""<p>The amount of the transaction</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._PaymentAmount

    @PaymentAmount.setter
    def PaymentAmount(self, PaymentAmount):
        self._PaymentAmount = PaymentAmount

    @property
    def PaymentMethod(self):
        r"""<p>The detail information of the payment method associated with the transaction</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PaymentMethod`
        """
        return self._PaymentMethod

    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod):
        self._PaymentMethod = PaymentMethod

    @property
    def TransactionType(self):
        r"""<p>Transaction type</p><p>Enumeration value:</p><ul><li>sale: One-time authorization and deduction (most common)</li><li>authorize: Authorization only (frozen amount)</li><li>capture: Execute deduction (after authorization)</li><li>void: Cancel pending authorization or deduction</li><li>refund: Refund (part or all)</li><li>deposit: Deposit to account</li><li>withdrawal: Withdrawal from account</li><li>transfer: Fund transfer between accounts</li><li>buy: Purchase asset (for example, crypto currency)</li><li>sell: Sell asset</li><li>send: Send fund/asset (for example, cross-wallet transfer)</li><li>receive: Receive fund/asset</li></ul><p>Default value: sale</p>
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def Billing(self):
        r"""<p>Bill information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Billing`
        """
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def Delivery(self):
        r"""<p>Delivery information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Delivery`
        """
        return self._Delivery

    @Delivery.setter
    def Delivery(self, Delivery):
        self._Delivery = Delivery

    @property
    def Merchant(self):
        r"""<p>Merchant information</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Merchant`
        """
        return self._Merchant

    @Merchant.setter
    def Merchant(self, Merchant):
        self._Merchant = Merchant

    @property
    def PaymentResult(self):
        r"""<p>Payment result</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.PaymentResult`
        """
        return self._PaymentResult

    @PaymentResult.setter
    def PaymentResult(self, PaymentResult):
        self._PaymentResult = PaymentResult

    @property
    def TransferRecipientUserId(self):
        r"""<p>The ID of the recipent in transfer transaction</p>
        :rtype: str
        """
        return self._TransferRecipientUserId

    @TransferRecipientUserId.setter
    def TransferRecipientUserId(self, TransferRecipientUserId):
        self._TransferRecipientUserId = TransferRecipientUserId

    @property
    def TransferSentAddress(self):
        r"""<p>The address of the sender in transfer transaction</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._TransferSentAddress

    @TransferSentAddress.setter
    def TransferSentAddress(self, TransferSentAddress):
        self._TransferSentAddress = TransferSentAddress

    @property
    def TransferReceivedAddress(self):
        r"""<p>Physical address of the recipient, applicable to the transfer transaction type.</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Address`
        """
        return self._TransferReceivedAddress

    @TransferReceivedAddress.setter
    def TransferReceivedAddress(self, TransferReceivedAddress):
        self._TransferReceivedAddress = TransferReceivedAddress

    @property
    def DigitalOrders(self):
        r"""<p>The digital order(s) associated with the transaction</p>
        :rtype: list of DigitalOrder
        """
        return self._DigitalOrders

    @DigitalOrders.setter
    def DigitalOrders(self, DigitalOrders):
        self._DigitalOrders = DigitalOrders

    @property
    def ReceiverWallet(self):
        r"""<p>Wallet to receive crypto currency</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._ReceiverWallet

    @ReceiverWallet.setter
    def ReceiverWallet(self, ReceiverWallet):
        self._ReceiverWallet = ReceiverWallet

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._OrderId = params.get("OrderId")
        if params.get("PaymentAmount") is not None:
            self._PaymentAmount = Amount()
            self._PaymentAmount._deserialize(params.get("PaymentAmount"))
        if params.get("PaymentMethod") is not None:
            self._PaymentMethod = PaymentMethod()
            self._PaymentMethod._deserialize(params.get("PaymentMethod"))
        self._TransactionType = params.get("TransactionType")
        if params.get("Billing") is not None:
            self._Billing = Billing()
            self._Billing._deserialize(params.get("Billing"))
        if params.get("Delivery") is not None:
            self._Delivery = Delivery()
            self._Delivery._deserialize(params.get("Delivery"))
        if params.get("Merchant") is not None:
            self._Merchant = Merchant()
            self._Merchant._deserialize(params.get("Merchant"))
        if params.get("PaymentResult") is not None:
            self._PaymentResult = PaymentResult()
            self._PaymentResult._deserialize(params.get("PaymentResult"))
        self._TransferRecipientUserId = params.get("TransferRecipientUserId")
        if params.get("TransferSentAddress") is not None:
            self._TransferSentAddress = Address()
            self._TransferSentAddress._deserialize(params.get("TransferSentAddress"))
        if params.get("TransferReceivedAddress") is not None:
            self._TransferReceivedAddress = Address()
            self._TransferReceivedAddress._deserialize(params.get("TransferReceivedAddress"))
        if params.get("DigitalOrders") is not None:
            self._DigitalOrders = []
            for item in params.get("DigitalOrders"):
                obj = DigitalOrder()
                obj._deserialize(item)
                self._DigitalOrders.append(obj)
        if params.get("ReceiverWallet") is not None:
            self._ReceiverWallet = Wallet()
            self._ReceiverWallet._deserialize(params.get("ReceiverWallet"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    r"""The detail information of the user

    """

    def __init__(self):
        r"""
        :param _UserLevel: <p>The level of the user in your system</p>
        :type UserLevel: str
        :param _UserPoint: <p>The point of the user in your system</p>
        :type UserPoint: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        :param _UserType: <p>The type of the user in your system</p>
        :type UserType: str
        """
        self._UserLevel = None
        self._UserPoint = None
        self._UserType = None

    @property
    def UserLevel(self):
        r"""<p>The level of the user in your system</p>
        :rtype: str
        """
        return self._UserLevel

    @UserLevel.setter
    def UserLevel(self, UserLevel):
        self._UserLevel = UserLevel

    @property
    def UserPoint(self):
        r"""<p>The point of the user in your system</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.CreditPoint`
        """
        return self._UserPoint

    @UserPoint.setter
    def UserPoint(self, UserPoint):
        self._UserPoint = UserPoint

    @property
    def UserType(self):
        r"""<p>The type of the user in your system</p>
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._UserLevel = params.get("UserLevel")
        if params.get("UserPoint") is not None:
            self._UserPoint = CreditPoint()
            self._UserPoint._deserialize(params.get("UserPoint"))
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Wallet(AbstractModel):
    r"""The details of the digital wallet

    """

    def __init__(self):
        r"""
        :param _WalletType: <p>Wallet type</p><p>Enumeration value:</p><ul><li>crypto: Crypto currency</li><li>digital: Digital currency</li><li>fiat: Fiat currency</li></ul>
        :type WalletType: str
        :param _WalletAddress: <p>The address of the wallet.Usually it is the ID of the wallet.</p>
        :type WalletAddress: str
        :param _WalletHolderName: <p>The full name of the person who holds  the wallet</p>
        :type WalletHolderName: str
        :param _WalletProvider: <p>The provider of the wallet, such as wechat, alipay, paypal</p>
        :type WalletProvider: str
        """
        self._WalletType = None
        self._WalletAddress = None
        self._WalletHolderName = None
        self._WalletProvider = None

    @property
    def WalletType(self):
        r"""<p>Wallet type</p><p>Enumeration value:</p><ul><li>crypto: Crypto currency</li><li>digital: Digital currency</li><li>fiat: Fiat currency</li></ul>
        :rtype: str
        """
        return self._WalletType

    @WalletType.setter
    def WalletType(self, WalletType):
        self._WalletType = WalletType

    @property
    def WalletAddress(self):
        r"""<p>The address of the wallet.Usually it is the ID of the wallet.</p>
        :rtype: str
        """
        return self._WalletAddress

    @WalletAddress.setter
    def WalletAddress(self, WalletAddress):
        self._WalletAddress = WalletAddress

    @property
    def WalletHolderName(self):
        r"""<p>The full name of the person who holds  the wallet</p>
        :rtype: str
        """
        return self._WalletHolderName

    @WalletHolderName.setter
    def WalletHolderName(self, WalletHolderName):
        self._WalletHolderName = WalletHolderName

    @property
    def WalletProvider(self):
        r"""<p>The provider of the wallet, such as wechat, alipay, paypal</p>
        :rtype: str
        """
        return self._WalletProvider

    @WalletProvider.setter
    def WalletProvider(self, WalletProvider):
        self._WalletProvider = WalletProvider


    def _deserialize(self, params):
        self._WalletType = params.get("WalletType")
        self._WalletAddress = params.get("WalletAddress")
        self._WalletHolderName = params.get("WalletHolderName")
        self._WalletProvider = params.get("WalletProvider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawEvent(AbstractModel):
    r"""Withdraw event details

    """

    def __init__(self):
        r"""
        :param _Amount: <p>The amount of the withdraw</p>
        :type Amount: :class:`tencentcloud.rce.v20260130.models.Amount`
        :param _Method: <p>The method of the withdraw</p><p>Enumeration value:</p><ul><li>card: bank card</li><li>wallet: digital wallet</li></ul>
        :type Method: str
        :param _Card: <p>The detail information of the card withdrawn to.Required while the withdraw method is card</p>
        :type Card: :class:`tencentcloud.rce.v20260130.models.Card`
        :param _Wallet: <p>The detail information of the wallet withdrawn to.Required while the withdraw method is wallet</p>
        :type Wallet: :class:`tencentcloud.rce.v20260130.models.Wallet`
        :param _Result: <p>Withdraw result</p>
        :type Result: :class:`tencentcloud.rce.v20260130.models.Result`
        :param _Cust: <p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :type Cust: list of Cust
        """
        self._Amount = None
        self._Method = None
        self._Card = None
        self._Wallet = None
        self._Result = None
        self._Cust = None

    @property
    def Amount(self):
        r"""<p>The amount of the withdraw</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Amount`
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Method(self):
        r"""<p>The method of the withdraw</p><p>Enumeration value:</p><ul><li>card: bank card</li><li>wallet: digital wallet</li></ul>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Card(self):
        r"""<p>The detail information of the card withdrawn to.Required while the withdraw method is card</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Card`
        """
        return self._Card

    @Card.setter
    def Card(self, Card):
        self._Card = Card

    @property
    def Wallet(self):
        r"""<p>The detail information of the wallet withdrawn to.Required while the withdraw method is wallet</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Wallet`
        """
        return self._Wallet

    @Wallet.setter
    def Wallet(self, Wallet):
        self._Wallet = Wallet

    @property
    def Result(self):
        r"""<p>Withdraw result</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Result`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Cust(self):
        r"""<p>The custom parameters agreed with RCE. An array of objects in K:V format. e.g.[{"Key": "ApproverName", "Value": "bob"},{"Key":"ApproverPhone","Value": "+86131****5678"}]</p>
        :rtype: list of Cust
        """
        return self._Cust

    @Cust.setter
    def Cust(self, Cust):
        self._Cust = Cust


    def _deserialize(self, params):
        if params.get("Amount") is not None:
            self._Amount = Amount()
            self._Amount._deserialize(params.get("Amount"))
        self._Method = params.get("Method")
        if params.get("Card") is not None:
            self._Card = Card()
            self._Card._deserialize(params.get("Card"))
        if params.get("Wallet") is not None:
            self._Wallet = Wallet()
            self._Wallet._deserialize(params.get("Wallet"))
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        if params.get("Cust") is not None:
            self._Cust = []
            for item in params.get("Cust"):
                obj = Cust()
                obj._deserialize(item)
                self._Cust.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        