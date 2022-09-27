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
        :param CaptchaType: It must be `9` here. You can configure the CAPTCHA types in the console.
        :type CaptchaType: int
        :param Ticket: The user verification ticket returned by the frontend callback function
        :type Ticket: str
        :param UserIp: The user public IP obtained from the customer backend server
        :type UserIp: str
        :param Randstr: A random string returned by the frontend callback function
        :type Randstr: str
        :param CaptchaAppId: CAPTCHA's app ID. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the CaptchaAppId in the "Key" column of the CAPTCHA list.
        :type CaptchaAppId: int
        :param AppSecretKey: CAPTCHA's app key. Log in to the [Captcha console](https://console.cloud.tencent.com/captcha/graphical) and you can view the AppSecretKey in the "Key" column of the CAPTCHA list. AppSecretKey is the key for CAPTCHA ticket verification performed by the server. Please keep it confidential and do not disclose it to any third parties.
        :type AppSecretKey: str
        :param BusinessId: Business ID, which is used to differentiate statistical data when this service is used in multiple businesses of a website or an app.
        :type BusinessId: int
        :param SceneId: Scenario ID, which is used to differentiate statistical data when this service is used in multiple scenarios of a website or an app.
        :type SceneId: int
        :param MacAddress: MAC address or unique identifier of a device
        :type MacAddress: str
        :param Imei: Mobile equipment identity number
        :type Imei: str
        :param NeedGetCaptchaTime: Indicates whether to return the time when the frontend obtains the CAPTCHA. Valid values: 1 (return the time) and others.
        :type NeedGetCaptchaTime: int
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.Randstr = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None
        self.NeedGetCaptchaTime = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.Randstr = params.get("Randstr")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")
        self.NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult response structure.

    """

    def __init__(self):
        r"""
        :param CaptchaCode:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
  
 
 
 
 
 
  
 
        :type CaptchaCode: int
        :param CaptchaMsg: Status description and verification error message
Note: This field may return `null`, indicating that no valid value was found.
        :type CaptchaMsg: str
        :param EvilLevel: This parameter returns the result of imperceptible verification. This parameter is not available for Tencent Cloud International yet.
`0`: The request is trusted.
`100`: The request is malicious.
Note: This field may return `null`, indicating that no valid value was found.
        :type EvilLevel: int
        :param GetCaptchaTime: The timestamp when the frontend obtains the CAPTCHA.
Note: This field may return `null`, indicating that no valid value was found.
        :type GetCaptchaTime: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.EvilLevel = None
        self.GetCaptchaTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.EvilLevel = params.get("EvilLevel")
        self.GetCaptchaTime = params.get("GetCaptchaTime")
        self.RequestId = params.get("RequestId")