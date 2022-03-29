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


class DetailResults(AbstractModel):
    """Details of results returned by text moderation

    """

    def __init__(self):
        r"""
        :param Label: Result of the moderation. <br>`Normal`: normal content; `Porn`: pornographic content; `Abuse`: abusive content; **Ad**: advertising content; `Custom`: custom violating content
        :type Label: str
        :param Suggestion: Recommended follow-up action. <br>`Block`: block it automatically; `Review`: review the content again in human; **Pass**: pass
Note: This field may return `null`, indicating that no valid value can be found.
        :type Suggestion: str
        :param Keywords: This field returns the matched keywords. This parameter can include multiple returned values, which means multiple keywords are matched. If no keyword is returned but there is a `Score`, it means that the result of `Label` is determined by a semantic model.
Note: This field may return `null`, indicating that no valid value can be found.
        :type Keywords: list of str
        :param Score: This field indicates the convincing level of the `Label`, ranging from `0` (lowest) to `100` (highest). 
Note: This field may return `null`, indicating that no valid value can be found.
        :type Score: int
        :param LibType: It indicates the library type corresponding with the keyword. Valid values: `1` (blocklist/allowlist library) and `2` (custom keyword library). If no custom keyword library is configured, the default value is 1.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibType: int
        :param LibId: This field is **only valid when `Label` is `Custom`. It returns the custom library ID to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibId: str
        :param LibName: This field is **only valid when `Label` is `Custom` (custom keyword)`. It returns the custom library name to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibName: str
        :param SubLabel: The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :type SubLabel: str
        """
        self.Label = None
        self.Suggestion = None
        self.Keywords = None
        self.Score = None
        self.LibType = None
        self.LibId = None
        self.LibName = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        self.LibType = params.get("LibType")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """This field indicates the device information of the service subscriber

    """

    def __init__(self):
        r"""
        :param IP: This field indicates the IP address of the device used by the service subscriber. <br>
Note: Currently, only IPv4 addresses can be recorded.
        :type IP: str
        :param Mac: This field indicates the MAC address used by the service subscriber to facilitate device identification and management. Its format and value are consistent with those of the standard MAC address.
        :type Mac: str
        :param TokenId: * In beta test. Available soon.*
        :type TokenId: str
        :param DeviceId: * In beta test. Available soon.*
        :type DeviceId: str
        :param IMEI: This field represents the **IMEI** (International Mobile Equipment Identity) number of the device used by the service subscriber. IMEI can be used to identify each independent mobile communication device, such as a mobile phone, which is convenient for device identification and management. <br>Note: IMEI is formatted with **15 to 17 numbers only**.
        :type IMEI: str
        :param IDFA: **Dedicated for iOS device**. This field indicates the **IDFA** (Identifier for Advertising) corresponding to the service subscriber. IDFA, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the user.<br>
Note: Since the iOS14 update in 2021, Apple Inc. has allowed users to manually activate or deactivate IDFA, so the validity of the string identifier may be reduced.
        :type IDFA: str
        :param IDFV: **Dedicated for iOS device**. This field indicates the **IDFV** (Identifier for Vendor) corresponding to the service subscriber. IDFV, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the vendor. IDFV can also be used as a unique device identifier.
        :type IDFV: str
        """
        self.IP = None
        self.Mac = None
        self.TokenId = None
        self.DeviceId = None
        self.IMEI = None
        self.IDFA = None
        self.IDFV = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Mac = params.get("Mac")
        self.TokenId = params.get("TokenId")
        self.DeviceId = params.get("DeviceId")
        self.IMEI = params.get("IMEI")
        self.IDFA = params.get("IDFA")
        self.IDFV = params.get("IDFV")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """Account risk detection results

    """

    def __init__(self):
        r"""
        :param Label: This field returns the risk categories after account information detection. Valid values: **RiskAccount** (the account is at risk), **RiskIP** (the IP address is at risk), and **RiskIMEI** (the mobile device identifier is at risk).
        :type Label: str
        :param Level: This field returns the risk levels after account information detection. Valid values: **1** (suspected to be at risk) and **2** (malicious risk).
        :type Level: int
        """
        self.Label = None
        self.Level = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration request structure.

    """

    def __init__(self):
        r"""
        :param Content: This field indicates the text content of the object to be moderated. The text needs to be encoded in utf-8 format and encrypted with Base64. It can contain up to 10,000 characters, calculated by unicode encoding.
        :type Content: str
        :param BizType: This field indicates the specific policy number, which is used for the API call and can be configured in the CMS console. If it's not entered (left empty), the default moderation policy is adopted. If it's entered, the moderation policies are specified for business scenarios. <br>Note: Biztype contains 3 to 32 characters, including numbers, letters and underscores only. Different Biztypes are associated with different business scenarios and moderation policies. Ensure that you use the Biztype corresponding to the policy you want to apply.
        :type BizType: str
        :param DataId: This field indicates the data ID you assigned to the object to be moderated, which is convenient for you to identify and manage the file. <br>Value: this field can contain **up to 64 characters**, including uppercase and lowercase letters, numbers and four special symbols (_, -, @, #)
        :type DataId: str
        :param User: This field indicates the user information related with the object to be moderated, which can be used to identify violating users at risk.
        :type User: :class:`tencentcloud.tms.v20201229.models.User`
        :param Device: This field indicates the device information related with the object to be moderated, which can be used to identify violating devices at risk.
        :type Device: :class:`tencentcloud.tms.v20201229.models.Device`
        """
        self.Content = None
        self.BizType = None
        self.DataId = None
        self.User = None
        self.Device = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration response structure.

    """

    def __init__(self):
        r"""
        :param BizType: This field returns the BizType of the request parameters
        :type BizType: str
        :param Label: This field returns the **negative label with the highest priority** in the moderation results (DetailResults), which indicates the moderation result recommended by the model. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Normal**: normal content; **Porn**: pornographic content; **Abuse**: abusive content; **Ad**: advertising content; **Custom**: custom violating content, and others such as objectionable, insecure or inappropriate content.
        :type Label: str
        :param Suggestion: This field returns the follow-up moderation suggestions. The returned value indicates the recommended operation after obtaining the moderation result. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Block**: block; **Review**: human moderation; **Pass**: pass
        :type Suggestion: str
        :param Keywords: This field returns the keywords matched with the libraries in the moderated text under the current label to mark the specific violations (for example, *Friend me*). This parameter may have multiple returned values, indicating multiple keywords are matched. If the returned value is empty and the `Score` is not empty, it means that the negative label corresponding to the moderation result is a value returned from the semantic model judgment
Note: This field may return `null`, indicating that no valid value can be found.
        :type Keywords: list of str
        :param Score: This field returns the confidence level under the current label. Value range: 0 (**the lowest confidence level**) - 100 (**the highest confidence level**). The higher the value, the more likely the text is to belong to the category indicated by the current label. For example, *pornographic 99* indicates that the text is very likely to be pornographic, and *pornographic 0* indicates that the text is not pornographic
        :type Score: int
        :param DetailResults: This field returns the moderation results based on the text libraries. For details, see `DetailResults` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :type DetailResults: list of DetailResults
        :param RiskDetails: This field returns the detection results of violating accounts at risk, mainly including violation categories and risk levels. For details, see `RiskDetails` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :type RiskDetails: list of RiskDetails
        :param Extra: This field returns the extra information configured according to your needs. If it's not configured, the returned value is empty by default. <br>Note: the returned information varies based on different customers or Biztypes. If you need to configure this field, please submit a ticket or contact after-sales manager
Note: This field may return `null`, indicating that no valid value can be found.
        :type Extra: str
        :param DataId: This field returns the `DataId` in the request parameter corresponding to the moderated object
Note: This field may return `null`, indicating that no valid value can be found.
        :type DataId: str
        :param SubLabel: The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :type SubLabel: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BizType = None
        self.Label = None
        self.Suggestion = None
        self.Keywords = None
        self.Score = None
        self.DetailResults = None
        self.RiskDetails = None
        self.Extra = None
        self.DataId = None
        self.SubLabel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        if params.get("DetailResults") is not None:
            self.DetailResults = []
            for item in params.get("DetailResults"):
                obj = DetailResults()
                obj._deserialize(item)
                self.DetailResults.append(obj)
        if params.get("RiskDetails") is not None:
            self.RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self.RiskDetails.append(obj)
        self.Extra = params.get("Extra")
        self.DataId = params.get("DataId")
        self.SubLabel = params.get("SubLabel")
        self.RequestId = params.get("RequestId")


class User(AbstractModel):
    """This field indicates the account-related information of the service subscriber

    """

    def __init__(self):
        r"""
        :param UserId: This field indicates the service subscriber ID. This ID can be used to optimize the moderation result judgment based on the account's violation records, which is helpful for auxiliary judgment when there is a risk of suspected violations.
        :type UserId: str
        :param Nickname: This field indicates the account nickname information of the service subscriber.
        :type Nickname: str
        :param AccountType: This field indicates the account type corresponding to the service subscriber ID.<br>
Use this field and the account ID (UserId) together to determine a unique account.
        :type AccountType: int
        :param Gender: This field indicates the gender information of the service subscriber's account.<br>
Values: **0** (default value, indicating the gender is unknown), **1** (male) and **2** (female).
        :type Gender: int
        :param Age: This field indicates the age information of the service subscriber's account.<br>
Values: Integers between **0** (default value, indicating that the age is unknown) and the number of (**custom maximum age**).
        :type Age: int
        :param Level: This field indicates the level information of the service subscriber's account.<br>
Values: **0** (default value, indicating that the level is unknown), **1** (lower level), **2** (medium level) and **3** (higher level). Currently, **custom levels are not supported**.
        :type Level: int
        :param Phone: This field indicates the mobile phone number information of the service subscriber's account. The mobile phone numbers in various regions of the world can be recorded.<br>
Note: Please keep the format of mobile phone number uniform. For example, uniformly use the area code format (086/+86), etc.
        :type Phone: str
        :param HeadUrl: This field indicates the URL of the service subscriber's profile photos formatted with .png, .jpg, .jpeg, .bmp, .gif and .webp.
Note: Up to 5 MB is supported, and the minimum resolution is 256 x 256. When it takes more than 3 seconds to download, the "download timeout" is returned.
        :type HeadUrl: str
        :param Desc: This field indicates the profile information of service subscribers. It can contain up to 5,000 characters, including Chinese characters, letters and special symbols.
        :type Desc: str
        """
        self.UserId = None
        self.Nickname = None
        self.AccountType = None
        self.Gender = None
        self.Age = None
        self.Level = None
        self.Phone = None
        self.HeadUrl = None
        self.Desc = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Nickname = params.get("Nickname")
        self.AccountType = params.get("AccountType")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Level = params.get("Level")
        self.Phone = params.get("Phone")
        self.HeadUrl = params.get("HeadUrl")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        