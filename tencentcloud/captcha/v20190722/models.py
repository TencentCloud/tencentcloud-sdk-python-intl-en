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


class DescribeCaptchaResultRequest(AbstractModel):
    """DescribeCaptchaResult request structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaType: It must be `9` here.
        :type CaptchaType: int
        :param _Ticket: The user verification ticket returned by the frontend callback function
        :type Ticket: str
        :param _UserIp: The user public IP obtained from the customer backend server
        :type UserIp: str
        :param _Randstr: A random string returned by the frontend callback function
        :type Randstr: str
        :param _CaptchaAppId: CAPTCHA's app ID. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the CaptchaAppId in the "Key" column of the CAPTCHA list.
        :type CaptchaAppId: int
        :param _AppSecretKey: CAPTCHA's app key. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the AppSecretKey in the "Key" column of the CAPTCHA list. AppSecretKey is the key for CAPTCHA ticket verification performed by the server. Please keep it confidential and do not disclose it to any third parties.
        :type AppSecretKey: str
        :param _BusinessId: Reserved field.
        :type BusinessId: int
        :param _SceneId: Reserved field.
        :type SceneId: int
        :param _MacAddress: MAC address or unique identifier of a device
        :type MacAddress: str
        :param _Imei: Mobile equipment identity number
        :type Imei: str
        :param _NeedGetCaptchaTime: Indicates whether to return the time when the frontend obtains the CAPTCHA. Valid values: 1 (return the time) and others.
        :type NeedGetCaptchaTime: int
        """
        self._CaptchaType = None
        self._Ticket = None
        self._UserIp = None
        self._Randstr = None
        self._CaptchaAppId = None
        self._AppSecretKey = None
        self._BusinessId = None
        self._SceneId = None
        self._MacAddress = None
        self._Imei = None
        self._NeedGetCaptchaTime = None

    @property
    def CaptchaType(self):
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Randstr(self):
        return self._Randstr

    @Randstr.setter
    def Randstr(self, Randstr):
        self._Randstr = Randstr

    @property
    def CaptchaAppId(self):
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def NeedGetCaptchaTime(self):
        return self._NeedGetCaptchaTime

    @NeedGetCaptchaTime.setter
    def NeedGetCaptchaTime(self, NeedGetCaptchaTime):
        self._NeedGetCaptchaTime = NeedGetCaptchaTime


    def _deserialize(self, params):
        self._CaptchaType = params.get("CaptchaType")
        self._Ticket = params.get("Ticket")
        self._UserIp = params.get("UserIp")
        self._Randstr = params.get("Randstr")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppSecretKey = params.get("AppSecretKey")
        self._BusinessId = params.get("BusinessId")
        self._SceneId = params.get("SceneId")
        self._MacAddress = params.get("MacAddress")
        self._Imei = params.get("Imei")
        self._NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult response structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: `1 OK`: Verification passed
`7 captcha no match`: The passed in `Randstr` is invalid. Make sure it is the same as the `Randstr` returned from the frontend.
`8 ticket expired`: The `Ticket` has expired. A ticket is valid for five minutes. Please generate a new `Ticket` and `Randstr`.
`9 ticket reused`: The specified `Ticket` has been used. Please generate a new `Ticket` and `Randstr`.
`15 decrypt fail`: The specified `Ticket` is invalid. Make sure it's the same as the Ticket returned from the frontend. 
`16 appid-ticket mismatch`: The specified `CaptchaAppId` is invalid. Make sure it's the same as the `CaptchaAppId` returned from the frontend. You can obtain it from the CAPTCHA console in **Verification management** > **Basic configuration**.
`21 diff`. Ticket verification error. Possible reasons: 1) If the ticket contains the `terror` prefix, it's usually the case that a disaster recovery ticket is generated due to the network connection problems of the user. You can choose to ignore it or verify again. 2) If the ticket does not include the `terror` prefix, Captcha detects security risk on this request . You can choose to block it or not.
`100 appid-secretkey-ticket mismatch`: Parameter error. 1) Make sure `CaptchaAppId` and `AppSecretKey` are correct. `CaptchaAppId` and `AppSecretKey` in the CAPTACHA console under **Verification management** > **Basic configuration**. 2) Make sure the passed-in `Ticket` is generated by using the passed-in `CaptchaAppId`.
        :type CaptchaCode: int
        :param _CaptchaMsg: Status description and verification error message
Note: This field may return `null`, indicating that no valid value was found.
        :type CaptchaMsg: str
        :param _EvilLevel: This parameter returns the result of imperceptible verification. This parameter is not available for Tencent Cloud International yet.
`0`: The request is trusted.
`100`: The request is malicious.
Note: This field may return `null`, indicating that no valid value was found.
        :type EvilLevel: int
        :param _GetCaptchaTime: The timestamp when the frontend obtains the CAPTCHA.
Note: This field may return `null`, indicating that no valid value was found.
        :type GetCaptchaTime: int
        :param _EvilBitmap: Blocking type
Note: This field may return null, indicating that no valid values can be obtained.
        :type EvilBitmap: int
        :param _SubmitCaptchaTime: The time when the CAPTCHA is submitted.
        :type SubmitCaptchaTime: int
        :param _DeviceRiskCategory: Device Risk Category
        :type DeviceRiskCategory: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._EvilLevel = None
        self._GetCaptchaTime = None
        self._EvilBitmap = None
        self._SubmitCaptchaTime = None
        self._DeviceRiskCategory = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def EvilLevel(self):
        return self._EvilLevel

    @EvilLevel.setter
    def EvilLevel(self, EvilLevel):
        self._EvilLevel = EvilLevel

    @property
    def GetCaptchaTime(self):
        return self._GetCaptchaTime

    @GetCaptchaTime.setter
    def GetCaptchaTime(self, GetCaptchaTime):
        self._GetCaptchaTime = GetCaptchaTime

    @property
    def EvilBitmap(self):
        return self._EvilBitmap

    @EvilBitmap.setter
    def EvilBitmap(self, EvilBitmap):
        self._EvilBitmap = EvilBitmap

    @property
    def SubmitCaptchaTime(self):
        return self._SubmitCaptchaTime

    @SubmitCaptchaTime.setter
    def SubmitCaptchaTime(self, SubmitCaptchaTime):
        self._SubmitCaptchaTime = SubmitCaptchaTime

    @property
    def DeviceRiskCategory(self):
        return self._DeviceRiskCategory

    @DeviceRiskCategory.setter
    def DeviceRiskCategory(self, DeviceRiskCategory):
        self._DeviceRiskCategory = DeviceRiskCategory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._EvilLevel = params.get("EvilLevel")
        self._GetCaptchaTime = params.get("GetCaptchaTime")
        self._EvilBitmap = params.get("EvilBitmap")
        self._SubmitCaptchaTime = params.get("SubmitCaptchaTime")
        self._DeviceRiskCategory = params.get("DeviceRiskCategory")
        self._RequestId = params.get("RequestId")