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
        :param _Label: Result of the moderation. <br>`Normal`: normal content; `Porn`: pornographic content; `Abuse`: abusive content; **Ad**: advertising content; `Custom`: custom violating content
        :type Label: str
        :param _Suggestion: Recommended follow-up action. <br>`Block`: block it automatically; `Review`: review the content again in human; **Pass**: pass
Note: This field may return `null`, indicating that no valid value can be found.
        :type Suggestion: str
        :param _Keywords: Returns the information of keywords hit in the text. When no value is returned and `Score` is not empty, it means the `Label` is determined by the semantic-based detection model.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Keywords: list of str
        :param _Score: This field indicates the convincing level of the `Label`, ranging from `0` (lowest) to `100` (highest). 
Note: This field may return `null`, indicating that no valid value can be found.
        :type Score: int
        :param _LibType: It indicates the library type corresponding with the keyword. Valid values: `1` (blocklist/allowlist library) and `2` (custom keyword library). If no custom keyword library is configured, the default value is 1.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibType: int
        :param _LibId: This field is **only valid when `Label` is `Custom`. It returns the custom library ID to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibId: str
        :param _LibName: This field is **only valid when `Label` is `Custom` (custom keyword)`. It returns the custom library name to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :type LibName: str
        :param _SubLabel: The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :type SubLabel: str
        :param _Tags: Returns the keywords, label, sub-label and the score.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._LibType = None
        self._LibId = None
        self._LibName = None
        self._SubLabel = None
        self._Tags = None

    @property
    def Label(self):
        """Result of the moderation. <br>`Normal`: normal content; `Porn`: pornographic content; `Abuse`: abusive content; **Ad**: advertising content; `Custom`: custom violating content
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """Recommended follow-up action. <br>`Block`: block it automatically; `Review`: review the content again in human; **Pass**: pass
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """Returns the information of keywords hit in the text. When no value is returned and `Score` is not empty, it means the `Label` is determined by the semantic-based detection model.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """This field indicates the convincing level of the `Label`, ranging from `0` (lowest) to `100` (highest). 
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LibType(self):
        """It indicates the library type corresponding with the keyword. Valid values: `1` (blocklist/allowlist library) and `2` (custom keyword library). If no custom keyword library is configured, the default value is 1.
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def LibId(self):
        """This field is **only valid when `Label` is `Custom`. It returns the custom library ID to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        """This field is **only valid when `Label` is `Custom` (custom keyword)`. It returns the custom library name to facilitate the library management and configuration.
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def SubLabel(self):
        """The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Tags(self):
        """Returns the keywords, label, sub-label and the score.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        self._LibType = params.get("LibType")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._SubLabel = params.get("SubLabel")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """This field indicates the device information of the service subscriber

    """

    def __init__(self):
        r"""
        :param _IP: This field indicates the IP address of the device used by the service subscriber. <br>
Note: Currently, only IPv4 addresses can be recorded.
        :type IP: str
        :param _Mac: This field indicates the MAC address used by the service subscriber to facilitate device identification and management. Its format and value are consistent with those of the standard MAC address.
        :type Mac: str
        :param _TokenId: * In beta test. Available soon.*
        :type TokenId: str
        :param _DeviceId: * In beta test. Available soon.*
        :type DeviceId: str
        :param _IMEI: This field represents the **IMEI** (International Mobile Equipment Identity) number of the device used by the service subscriber. IMEI can be used to identify each independent mobile communication device, such as a mobile phone, which is convenient for device identification and management. <br>Note: IMEI is formatted with **15 to 17 numbers only**.
        :type IMEI: str
        :param _IDFA: **Dedicated for iOS device**. This field indicates the **IDFA** (Identifier for Advertising) corresponding to the service subscriber. IDFA, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the user.<br>
Note: Since the iOS14 update in 2021, Apple Inc. has allowed users to manually activate or deactivate IDFA, so the validity of the string identifier may be reduced.
        :type IDFA: str
        :param _IDFV: **Dedicated for iOS device**. This field indicates the **IDFV** (Identifier for Vendor) corresponding to the service subscriber. IDFV, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the vendor. IDFV can also be used as a unique device identifier.
        :type IDFV: str
        """
        self._IP = None
        self._Mac = None
        self._TokenId = None
        self._DeviceId = None
        self._IMEI = None
        self._IDFA = None
        self._IDFV = None

    @property
    def IP(self):
        """This field indicates the IP address of the device used by the service subscriber. <br>
Note: Currently, only IPv4 addresses can be recorded.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Mac(self):
        """This field indicates the MAC address used by the service subscriber to facilitate device identification and management. Its format and value are consistent with those of the standard MAC address.
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def TokenId(self):
        """* In beta test. Available soon.*
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def DeviceId(self):
        """* In beta test. Available soon.*
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        """This field represents the **IMEI** (International Mobile Equipment Identity) number of the device used by the service subscriber. IMEI can be used to identify each independent mobile communication device, such as a mobile phone, which is convenient for device identification and management. <br>Note: IMEI is formatted with **15 to 17 numbers only**.
        :rtype: str
        """
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def IDFA(self):
        """**Dedicated for iOS device**. This field indicates the **IDFA** (Identifier for Advertising) corresponding to the service subscriber. IDFA, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the user.<br>
Note: Since the iOS14 update in 2021, Apple Inc. has allowed users to manually activate or deactivate IDFA, so the validity of the string identifier may be reduced.
        :rtype: str
        """
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def IDFV(self):
        """**Dedicated for iOS device**. This field indicates the **IDFV** (Identifier for Vendor) corresponding to the service subscriber. IDFV, a string of hexadecimal 32 characters including numbers and letters, is provided by Apple Inc. to identify the vendor. IDFV can also be used as a unique device identifier.
        :rtype: str
        """
        return self._IDFV

    @IDFV.setter
    def IDFV(self, IDFV):
        self._IDFV = IDFV


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Mac = params.get("Mac")
        self._TokenId = params.get("TokenId")
        self._DeviceId = params.get("DeviceId")
        self._IMEI = params.get("IMEI")
        self._IDFA = params.get("IDFA")
        self._IDFV = params.get("IDFV")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """Account risk detection results

    """

    def __init__(self):
        r"""
        :param _Label: This field returns the risk categories after account information detection. Valid values: **RiskAccount** (the account is at risk), **RiskIP** (the IP address is at risk), and **RiskIMEI** (the mobile device identifier is at risk).
        :type Label: str
        :param _Level: This field returns the risk levels after account information detection. Valid values: **1** (suspected to be at risk) and **2** (malicious risk).
        :type Level: int
        """
        self._Label = None
        self._Level = None

    @property
    def Label(self):
        """This field returns the risk categories after account information detection. Valid values: **RiskAccount** (the account is at risk), **RiskIP** (the IP address is at risk), and **RiskIMEI** (the mobile device identifier is at risk).
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Level(self):
        """This field returns the risk levels after account information detection. Valid values: **1** (suspected to be at risk) and **2** (malicious risk).
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysis(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Label: 
        :type Label: str
        :param _Score: 
        :type Score: int
        :param _Detail: 
        :type Detail: :class:`tencentcloud.tms.v20201229.models.SentimentDetail`
        :param _Code: 
        :type Code: str
        :param _Message: 
        :type Message: str
        """
        self._Label = None
        self._Score = None
        self._Detail = None
        self._Code = None
        self._Message = None

    @property
    def Label(self):
        """
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        """
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Detail(self):
        """
        :rtype: :class:`tencentcloud.tms.v20201229.models.SentimentDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Code(self):
        """
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        if params.get("Detail") is not None:
            self._Detail = SentimentDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentDetail(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Positive: 
        :type Positive: int
        :param _Negative: 
        :type Negative: int
        """
        self._Positive = None
        self._Negative = None

    @property
    def Positive(self):
        """
        :rtype: int
        """
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Negative(self):
        """
        :rtype: int
        """
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative


    def _deserialize(self, params):
        self._Positive = params.get("Positive")
        self._Negative = params.get("Negative")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Returns the keywords, label, sub-label and the score.

    """

    def __init__(self):
        r"""
        :param _Keyword: Returns the hit keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Keyword: str
        :param _SubLabel: Returns the sub-tags.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubLabel: str
        :param _Score: Returns the score for the sub-label
Note: This field may return null, indicating that no valid values can be obtained.
        :type Score: int
        """
        self._Keyword = None
        self._SubLabel = None
        self._Score = None

    @property
    def Keyword(self):
        """Returns the hit keywords.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SubLabel(self):
        """Returns the sub-tags.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        """Returns the score for the sub-label
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration request structure.

    """

    def __init__(self):
        r"""
        :param _Content: This field indicates the text content of the object to be moderated. The text needs to be encoded in utf-8 format and encrypted with Base64. It can contain up to 10,000 characters, calculated by unicode encoding.
        :type Content: str
        :param _BizType: This field indicates the specific policy number, which is used for the API call and can be configured in the CMS console. If it's not entered (left empty), the default moderation policy is adopted. If it's entered, the moderation policies are specified for business scenarios. <br>Note: Biztype contains 3 to 32 characters, including numbers, letters and underscores only. Different Biztypes are associated with different business scenarios and moderation policies. Ensure that you use the Biztype corresponding to the policy you want to apply.
        :type BizType: str
        :param _DataId: This field indicates the data ID you assigned to the object to be moderated, which is convenient for you to identify and manage the file. <br>Value: this field can contain **up to 64 characters**, including uppercase and lowercase letters, numbers and four special symbols (_, -, @, #)
        :type DataId: str
        :param _User: This field indicates the user information related with the object to be moderated, which can be used to identify violating users at risk.
        :type User: :class:`tencentcloud.tms.v20201229.models.User`
        :param _Device: This field indicates the device information related with the object to be moderated, which can be used to identify violating devices at risk.
        :type Device: :class:`tencentcloud.tms.v20201229.models.Device`
        :param _SourceLanguage: This field Indicates the original language of the content.The enumeration values are ("en", "zh", ""), where en means English, zh means Chinese, and an empty string means the default language is Chinese. It is recommended to enter "en" only when the language of the content is clearly "English".
        :type SourceLanguage: str
        """
        self._Content = None
        self._BizType = None
        self._DataId = None
        self._User = None
        self._Device = None
        self._SourceLanguage = None

    @property
    def Content(self):
        """This field indicates the text content of the object to be moderated. The text needs to be encoded in utf-8 format and encrypted with Base64. It can contain up to 10,000 characters, calculated by unicode encoding.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def BizType(self):
        """This field indicates the specific policy number, which is used for the API call and can be configured in the CMS console. If it's not entered (left empty), the default moderation policy is adopted. If it's entered, the moderation policies are specified for business scenarios. <br>Note: Biztype contains 3 to 32 characters, including numbers, letters and underscores only. Different Biztypes are associated with different business scenarios and moderation policies. Ensure that you use the Biztype corresponding to the policy you want to apply.
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        """This field indicates the data ID you assigned to the object to be moderated, which is convenient for you to identify and manage the file. <br>Value: this field can contain **up to 64 characters**, including uppercase and lowercase letters, numbers and four special symbols (_, -, @, #)
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def User(self):
        """This field indicates the user information related with the object to be moderated, which can be used to identify violating users at risk.
        :rtype: :class:`tencentcloud.tms.v20201229.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Device(self):
        """This field indicates the device information related with the object to be moderated, which can be used to identify violating devices at risk.
        :rtype: :class:`tencentcloud.tms.v20201229.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def SourceLanguage(self):
        """This field Indicates the original language of the content.The enumeration values are ("en", "zh", ""), where en means English, zh means Chinese, and an empty string means the default language is Chinese. It is recommended to enter "en" only when the language of the content is clearly "English".
        :rtype: str
        """
        return self._SourceLanguage

    @SourceLanguage.setter
    def SourceLanguage(self, SourceLanguage):
        self._SourceLanguage = SourceLanguage


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._BizType = params.get("BizType")
        self._DataId = params.get("DataId")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._SourceLanguage = params.get("SourceLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration response structure.

    """

    def __init__(self):
        r"""
        :param _BizType: This field returns the BizType of the request parameters
        :type BizType: str
        :param _Label: This field returns the **negative label with the highest priority** in the moderation results (DetailResults), which indicates the moderation result recommended by the model. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Normal**: normal content; **Porn**: pornographic content; **Abuse**: abusive content; **Ad**: advertising content; **Custom**: custom violating content, and others such as objectionable, insecure or inappropriate content.
        :type Label: str
        :param _Suggestion: This field returns the follow-up moderation suggestions. The returned value indicates the recommended operation after obtaining the moderation result. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Block**: block; **Review**: human moderation; **Pass**: pass
        :type Suggestion: str
        :param _Keywords: This field returns the keywords matched with the libraries in the moderated text under the current label to mark the specific violations (for example, *Friend me*). This parameter may have multiple returned values, indicating multiple keywords are matched. If the returned value is empty and the `Score` is not empty, it means that the negative label corresponding to the moderation result is a value returned from the semantic model judgment
Note: This field may return `null`, indicating that no valid value can be found.
        :type Keywords: list of str
        :param _Score: This field returns the confidence level under the current label. Value range: 0 (**the lowest confidence level**) - 100 (**the highest confidence level**). The higher the value, the more likely the text is to belong to the category indicated by the current label. For example, *pornographic 99* indicates that the text is very likely to be pornographic, and *pornographic 0* indicates that the text is not pornographic
        :type Score: int
        :param _DetailResults: This field returns the moderation results based on the text libraries. For details, see `DetailResults` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :type DetailResults: list of DetailResults
        :param _RiskDetails: This field returns the detection results of violating accounts at risk, mainly including violation categories and risk levels. For details, see `RiskDetails` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :type RiskDetails: list of RiskDetails
        :param _Extra: This field returns the extra information configured according to your needs. If it's not configured, the returned value is empty by default. <br>Note: the returned information varies based on different customers or Biztypes. If you need to configure this field, please submit a ticket or contact after-sales manager
Note: This field may return `null`, indicating that no valid value can be found.
        :type Extra: str
        :param _DataId: This field returns the `DataId` in the request parameter corresponding to the moderated object
Note: This field may return `null`, indicating that no valid value can be found.
        :type DataId: str
        :param _SubLabel: The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :type SubLabel: str
        :param _ContextText: Returns the context text.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContextText: str
        :param _SentimentAnalysis: 
        :type SentimentAnalysis: :class:`tencentcloud.tms.v20201229.models.SentimentAnalysis`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BizType = None
        self._Label = None
        self._Suggestion = None
        self._Keywords = None
        self._Score = None
        self._DetailResults = None
        self._RiskDetails = None
        self._Extra = None
        self._DataId = None
        self._SubLabel = None
        self._ContextText = None
        self._SentimentAnalysis = None
        self._RequestId = None

    @property
    def BizType(self):
        """This field returns the BizType of the request parameters
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Label(self):
        """This field returns the **negative label with the highest priority** in the moderation results (DetailResults), which indicates the moderation result recommended by the model. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Normal**: normal content; **Porn**: pornographic content; **Abuse**: abusive content; **Ad**: advertising content; **Custom**: custom violating content, and others such as objectionable, insecure or inappropriate content.
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        """This field returns the follow-up moderation suggestions. The returned value indicates the recommended operation after obtaining the moderation result. It is recommended that you handle different violations with the suggested values according to your business needs. <br>Returned values: **Block**: block; **Review**: human moderation; **Pass**: pass
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        """This field returns the keywords matched with the libraries in the moderated text under the current label to mark the specific violations (for example, *Friend me*). This parameter may have multiple returned values, indicating multiple keywords are matched. If the returned value is empty and the `Score` is not empty, it means that the negative label corresponding to the moderation result is a value returned from the semantic model judgment
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        """This field returns the confidence level under the current label. Value range: 0 (**the lowest confidence level**) - 100 (**the highest confidence level**). The higher the value, the more likely the text is to belong to the category indicated by the current label. For example, *pornographic 99* indicates that the text is very likely to be pornographic, and *pornographic 0* indicates that the text is not pornographic
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def DetailResults(self):
        """This field returns the moderation results based on the text libraries. For details, see `DetailResults` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: list of DetailResults
        """
        return self._DetailResults

    @DetailResults.setter
    def DetailResults(self, DetailResults):
        self._DetailResults = DetailResults

    @property
    def RiskDetails(self):
        """This field returns the detection results of violating accounts at risk, mainly including violation categories and risk levels. For details, see `RiskDetails` in the data structure
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: list of RiskDetails
        """
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Extra(self):
        """This field returns the extra information configured according to your needs. If it's not configured, the returned value is empty by default. <br>Note: the returned information varies based on different customers or Biztypes. If you need to configure this field, please submit a ticket or contact after-sales manager
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def DataId(self):
        """This field returns the `DataId` in the request parameter corresponding to the moderated object
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def SubLabel(self):
        """The field returns the second-level labels under the current label.
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def ContextText(self):
        """Returns the context text.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContextText

    @ContextText.setter
    def ContextText(self, ContextText):
        self._ContextText = ContextText

    @property
    def SentimentAnalysis(self):
        """
        :rtype: :class:`tencentcloud.tms.v20201229.models.SentimentAnalysis`
        """
        return self._SentimentAnalysis

    @SentimentAnalysis.setter
    def SentimentAnalysis(self, SentimentAnalysis):
        self._SentimentAnalysis = SentimentAnalysis

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
        self._BizType = params.get("BizType")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        if params.get("DetailResults") is not None:
            self._DetailResults = []
            for item in params.get("DetailResults"):
                obj = DetailResults()
                obj._deserialize(item)
                self._DetailResults.append(obj)
        if params.get("RiskDetails") is not None:
            self._RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self._RiskDetails.append(obj)
        self._Extra = params.get("Extra")
        self._DataId = params.get("DataId")
        self._SubLabel = params.get("SubLabel")
        self._ContextText = params.get("ContextText")
        if params.get("SentimentAnalysis") is not None:
            self._SentimentAnalysis = SentimentAnalysis()
            self._SentimentAnalysis._deserialize(params.get("SentimentAnalysis"))
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    """This field indicates the account-related information of the service subscriber

    """

    def __init__(self):
        r"""
        :param _UserId: This field indicates the service subscriber ID. This ID can be used to optimize the moderation result judgment based on the account's violation records, which is helpful for auxiliary judgment when there is a risk of suspected violations.
        :type UserId: str
        :param _Nickname: This field indicates the account nickname information of the service subscriber.
        :type Nickname: str
        :param _AccountType: This field indicates the account type corresponding to the service subscriber ID.<br>
Use this field and the account ID (UserId) together to determine a unique account.
        :type AccountType: int
        :param _Gender: This field indicates the gender information of the service subscriber's account.<br>
Values: **0** (default value, indicating the gender is unknown), **1** (male) and **2** (female).
        :type Gender: int
        :param _Age: This field indicates the age information of the service subscriber's account.<br>
Values: Integers between **0** (default value, indicating that the age is unknown) and the number of (**custom maximum age**).
        :type Age: int
        :param _Level: This field indicates the level information of the service subscriber's account.<br>
Values: **0** (default value, indicating that the level is unknown), **1** (lower level), **2** (medium level) and **3** (higher level). Currently, **custom levels are not supported**.
        :type Level: int
        :param _Phone: This field indicates the mobile phone number information of the service subscriber's account. The mobile phone numbers in various regions of the world can be recorded.<br>
Note: Please keep the format of mobile phone number uniform. For example, uniformly use the area code format (086/+86), etc.
        :type Phone: str
        :param _HeadUrl: This field indicates the URL of the service subscriber's profile photos formatted with .png, .jpg, .jpeg, .bmp, .gif and .webp.
Note: Up to 5 MB is supported, and the minimum resolution is 256 x 256. When it takes more than 3 seconds to download, the "download timeout" is returned.
        :type HeadUrl: str
        :param _Desc: This field indicates the profile information of service subscribers. It can contain up to 5,000 characters, including Chinese characters, letters and special symbols.
        :type Desc: str
        :param _RoomId: Room ID of the group chat.
        :type RoomId: str
        :param _ReceiverId: Receiver ID.
        :type ReceiverId: str
        :param _SendTime: Generation time of the message, in ms.
        :type SendTime: int
        """
        self._UserId = None
        self._Nickname = None
        self._AccountType = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None
        self._HeadUrl = None
        self._Desc = None
        self._RoomId = None
        self._ReceiverId = None
        self._SendTime = None

    @property
    def UserId(self):
        """This field indicates the service subscriber ID. This ID can be used to optimize the moderation result judgment based on the account's violation records, which is helpful for auxiliary judgment when there is a risk of suspected violations.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        """This field indicates the account nickname information of the service subscriber.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def AccountType(self):
        """This field indicates the account type corresponding to the service subscriber ID.<br>
Use this field and the account ID (UserId) together to determine a unique account.
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Gender(self):
        """This field indicates the gender information of the service subscriber's account.<br>
Values: **0** (default value, indicating the gender is unknown), **1** (male) and **2** (female).
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        """This field indicates the age information of the service subscriber's account.<br>
Values: Integers between **0** (default value, indicating that the age is unknown) and the number of (**custom maximum age**).
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Level(self):
        """This field indicates the level information of the service subscriber's account.<br>
Values: **0** (default value, indicating that the level is unknown), **1** (lower level), **2** (medium level) and **3** (higher level). Currently, **custom levels are not supported**.
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        """This field indicates the mobile phone number information of the service subscriber's account. The mobile phone numbers in various regions of the world can be recorded.<br>
Note: Please keep the format of mobile phone number uniform. For example, uniformly use the area code format (086/+86), etc.
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def HeadUrl(self):
        """This field indicates the URL of the service subscriber's profile photos formatted with .png, .jpg, .jpeg, .bmp, .gif and .webp.
Note: Up to 5 MB is supported, and the minimum resolution is 256 x 256. When it takes more than 3 seconds to download, the "download timeout" is returned.
        :rtype: str
        """
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl

    @property
    def Desc(self):
        """This field indicates the profile information of service subscribers. It can contain up to 5,000 characters, including Chinese characters, letters and special symbols.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RoomId(self):
        """Room ID of the group chat.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def ReceiverId(self):
        """Receiver ID.
        :rtype: str
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def SendTime(self):
        """Generation time of the message, in ms.
        :rtype: int
        """
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._AccountType = params.get("AccountType")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        self._HeadUrl = params.get("HeadUrl")
        self._Desc = params.get("Desc")
        self._RoomId = params.get("RoomId")
        self._ReceiverId = params.get("ReceiverId")
        self._SendTime = params.get("SendTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        