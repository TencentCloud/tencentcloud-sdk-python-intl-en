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
        :param _CaptchaType: Fill with fixed value: 9.
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
        """Fill with fixed value: 9.
        :rtype: int
        """
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        """The user verification ticket returned by the frontend callback function
        :rtype: str
        """
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        """The user public IP obtained from the customer backend server
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Randstr(self):
        """A random string returned by the frontend callback function
        :rtype: str
        """
        return self._Randstr

    @Randstr.setter
    def Randstr(self, Randstr):
        self._Randstr = Randstr

    @property
    def CaptchaAppId(self):
        """CAPTCHA's app ID. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the CaptchaAppId in the "Key" column of the CAPTCHA list.
        :rtype: int
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        """CAPTCHA's app key. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the AppSecretKey in the "Key" column of the CAPTCHA list. AppSecretKey is the key for CAPTCHA ticket verification performed by the server. Please keep it confidential and do not disclose it to any third parties.
        :rtype: str
        """
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        """Reserved field.
        :rtype: int
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        """Reserved field.
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        """MAC address or unique identifier of a device
        :rtype: str
        """
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        """Mobile equipment identity number
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def NeedGetCaptchaTime(self):
        """Indicates whether to return the time when the frontend obtains the CAPTCHA. Valid values: 1 (return the time) and others.
        :rtype: int
        """
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
        :param _CaptchaCode: OK indicates verification passed.
7 captcha no match. the passed in Randstr is invalid. please check if the Randstr is consistent with the Randstr returned by the frontend.
The passed-in ticket has expired (the valid period of the ticket is 5 minutes). generate the ticket and Randstr again for validation.
The passed-in ticket is reused. generate the ticket and Randstr again for verification.
15 decrypt fail. the passed-in Ticket is invalid. please check if the Ticket is consistent with the Ticket returned by the frontend.
16 appid-ticket mismatch. the passed in CaptchaAppId is incorrect. please check if the CaptchaAppId is consistent with the CaptchaAppId passed in by the frontend, and ensure that the CaptchaAppId is obtained from the verification code console [verification management] -> [basic configuration].
21 diff invoice verification exception. possible reasons: (1) if the Ticket contains the trerror prefix, generally because the user has a poor network connection, resulting in the frontend's automatic disaster recovery and generation of a disaster recovery Ticket. the business side may skip or post-process as needed. (2) if the Ticket does not include the trerror prefix, it is because the security risk of the request was detected by the CAPTCHA-intl risk control system. the business side may intercept as needed.
100 appid-secretkey-ticket mismatch. parameter validation error. (1) please check whether the CaptchaAppId and AppSecretKey are correct. the CaptchaAppId and AppSecretKey need to be obtained from verification code console > verification management > basic configuration. (2) please check whether the passed-in ticket is generated by the passed-in CaptchaAppId.
        :type CaptchaCode: int
        :param _CaptchaMsg: Status description and verification error message.
        :type CaptchaMsg: str
        :param _EvilLevel: In invisible verification mode, this parameter returns the verification result.
EvilLevel=0 indicates that the request is not malicious.
The parameter EvilLevel = 100 indicates that the request is malicious.
        :type EvilLevel: int
        :param _GetCaptchaTime: Frontend retrieval time of the captcha-intl, timestamp format.
        :type GetCaptchaTime: int
        :param _EvilBitmap: Blocking type
Note: This field may return null, indicating that no valid values can be obtained.
        :type EvilBitmap: int
        :param _SubmitCaptchaTime: The time when the CAPTCHA is submitted.
        :type SubmitCaptchaTime: int
        :param _DeviceRiskCategory: Device risk category.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeviceRiskCategory: str
        :param _Score: CAPTCHA-Intl score.
Note:The score ranges from 0 to 100 (e.g., 20, 70, 90).
A higher score indicates a greater probability that the interaction was initiated by a bot or represents a bot attack.
A lower score indicates a greater probability that the interaction was performed by a real human user.
        :type Score: int
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
        self._Score = None
        self._RequestId = None

    @property
    def CaptchaCode(self):
        """OK indicates verification passed.
7 captcha no match. the passed in Randstr is invalid. please check if the Randstr is consistent with the Randstr returned by the frontend.
The passed-in ticket has expired (the valid period of the ticket is 5 minutes). generate the ticket and Randstr again for validation.
The passed-in ticket is reused. generate the ticket and Randstr again for verification.
15 decrypt fail. the passed-in Ticket is invalid. please check if the Ticket is consistent with the Ticket returned by the frontend.
16 appid-ticket mismatch. the passed in CaptchaAppId is incorrect. please check if the CaptchaAppId is consistent with the CaptchaAppId passed in by the frontend, and ensure that the CaptchaAppId is obtained from the verification code console [verification management] -> [basic configuration].
21 diff invoice verification exception. possible reasons: (1) if the Ticket contains the trerror prefix, generally because the user has a poor network connection, resulting in the frontend's automatic disaster recovery and generation of a disaster recovery Ticket. the business side may skip or post-process as needed. (2) if the Ticket does not include the trerror prefix, it is because the security risk of the request was detected by the CAPTCHA-intl risk control system. the business side may intercept as needed.
100 appid-secretkey-ticket mismatch. parameter validation error. (1) please check whether the CaptchaAppId and AppSecretKey are correct. the CaptchaAppId and AppSecretKey need to be obtained from verification code console > verification management > basic configuration. (2) please check whether the passed-in ticket is generated by the passed-in CaptchaAppId.
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        """Status description and verification error message.
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def EvilLevel(self):
        """In invisible verification mode, this parameter returns the verification result.
EvilLevel=0 indicates that the request is not malicious.
The parameter EvilLevel = 100 indicates that the request is malicious.
        :rtype: int
        """
        return self._EvilLevel

    @EvilLevel.setter
    def EvilLevel(self, EvilLevel):
        self._EvilLevel = EvilLevel

    @property
    def GetCaptchaTime(self):
        """Frontend retrieval time of the captcha-intl, timestamp format.
        :rtype: int
        """
        return self._GetCaptchaTime

    @GetCaptchaTime.setter
    def GetCaptchaTime(self, GetCaptchaTime):
        self._GetCaptchaTime = GetCaptchaTime

    @property
    def EvilBitmap(self):
        """Blocking type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EvilBitmap

    @EvilBitmap.setter
    def EvilBitmap(self, EvilBitmap):
        self._EvilBitmap = EvilBitmap

    @property
    def SubmitCaptchaTime(self):
        """The time when the CAPTCHA is submitted.
        :rtype: int
        """
        return self._SubmitCaptchaTime

    @SubmitCaptchaTime.setter
    def SubmitCaptchaTime(self, SubmitCaptchaTime):
        self._SubmitCaptchaTime = SubmitCaptchaTime

    @property
    def DeviceRiskCategory(self):
        """Device risk category.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeviceRiskCategory

    @DeviceRiskCategory.setter
    def DeviceRiskCategory(self, DeviceRiskCategory):
        self._DeviceRiskCategory = DeviceRiskCategory

    @property
    def Score(self):
        """CAPTCHA-Intl score.
Note:The score ranges from 0 to 100 (e.g., 20, 70, 90).
A higher score indicates a greater probability that the interaction was initiated by a bot or represents a bot attack.
A lower score indicates a greater probability that the interaction was performed by a real human user.
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

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
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._EvilLevel = params.get("EvilLevel")
        self._GetCaptchaTime = params.get("GetCaptchaTime")
        self._EvilBitmap = params.get("EvilBitmap")
        self._SubmitCaptchaTime = params.get("SubmitCaptchaTime")
        self._DeviceRiskCategory = params.get("DeviceRiskCategory")
        self._Score = params.get("Score")
        self._RequestId = params.get("RequestId")