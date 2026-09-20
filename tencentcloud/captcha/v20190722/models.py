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


class CreateCaptchaInfoInternationalRequest(AbstractModel):
    r"""CreateCaptchaInfoInternational request structure.

    """

    def __init__(self):
        r"""
        :param _AppName: <p>Captcha name</p>
        :type AppName: str
        :param _ChannelInfo: <p>Client type</p><p>Enumeration values:</p><ul><li>web: For web scenario</li><li>android: For Android client</li><li>ios: For iOS client</li></ul><p>Default value: web</p>
        :type ChannelInfo: str
        :param _VerifyRank: <p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :type VerifyRank: str
        :param _UserSetCapType: <p>Validation type</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must be 2</li><li>2: Slide</li><li>8: Graphical</li><li>9: Voice</li></ul>
        :type UserSetCapType: str
        :param _DefendMode: <p>Interception mode</p><p>Enumeration values:</p><ul><li>block: interception mode</li><li>notify: perception mode</li></ul><p>Default value: notify</p>
        :type DefendMode: str
        :param _Tags: <p>Resource tag, key&amp;value format</p>
        :type Tags: list of str
        :param _DisableInvisibleSwitch: <p>Verification mechanism</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :type DisableInvisibleSwitch: str
        :param _VerifyDomain: <p>web domain name</p><p>Only valid when ChannelInfo is web</p>
        :type VerifyDomain: str
        :param _VerifyBundleId: <p>app BundleId</p><p>Only valid when ChannelInfo is ios</p>
        :type VerifyBundleId: str
        :param _VerifyPackage: <p>app package</p><p>Only valid when ChannelInfo is android</p>
        :type VerifyPackage: str
        :param _CheckAppidSwitch: <p>Whether to enable captcha encryption. 0: Off. 1: On</p>
        :type CheckAppidSwitch: int
        :param _CheckIvSwitch: <p>Whether to enable non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Input 1 is allowed only when CheckAppidSwitch is 1</p>
        :type CheckIvSwitch: int
        :param _CheckBoxStyle: <p>Checkbox display method</p><p>Enumeration values:</p><ul><li>0: simplified version</li><li>1: basic version</li><li>2: invisible version</li></ul>
        :type CheckBoxStyle: str
        """
        self._AppName = None
        self._ChannelInfo = None
        self._VerifyRank = None
        self._UserSetCapType = None
        self._DefendMode = None
        self._Tags = None
        self._DisableInvisibleSwitch = None
        self._VerifyDomain = None
        self._VerifyBundleId = None
        self._VerifyPackage = None
        self._CheckAppidSwitch = None
        self._CheckIvSwitch = None
        self._CheckBoxStyle = None

    @property
    def AppName(self):
        r"""<p>Captcha name</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ChannelInfo(self):
        r"""<p>Client type</p><p>Enumeration values:</p><ul><li>web: For web scenario</li><li>android: For Android client</li><li>ios: For iOS client</li></ul><p>Default value: web</p>
        :rtype: str
        """
        return self._ChannelInfo

    @ChannelInfo.setter
    def ChannelInfo(self, ChannelInfo):
        self._ChannelInfo = ChannelInfo

    @property
    def VerifyRank(self):
        r"""<p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :rtype: str
        """
        return self._VerifyRank

    @VerifyRank.setter
    def VerifyRank(self, VerifyRank):
        self._VerifyRank = VerifyRank

    @property
    def UserSetCapType(self):
        r"""<p>Validation type</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must be 2</li><li>2: Slide</li><li>8: Graphical</li><li>9: Voice</li></ul>
        :rtype: str
        """
        return self._UserSetCapType

    @UserSetCapType.setter
    def UserSetCapType(self, UserSetCapType):
        self._UserSetCapType = UserSetCapType

    @property
    def DefendMode(self):
        r"""<p>Interception mode</p><p>Enumeration values:</p><ul><li>block: interception mode</li><li>notify: perception mode</li></ul><p>Default value: notify</p>
        :rtype: str
        """
        return self._DefendMode

    @DefendMode.setter
    def DefendMode(self, DefendMode):
        self._DefendMode = DefendMode

    @property
    def Tags(self):
        r"""<p>Resource tag, key&amp;value format</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisableInvisibleSwitch(self):
        r"""<p>Verification mechanism</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :rtype: str
        """
        return self._DisableInvisibleSwitch

    @DisableInvisibleSwitch.setter
    def DisableInvisibleSwitch(self, DisableInvisibleSwitch):
        self._DisableInvisibleSwitch = DisableInvisibleSwitch

    @property
    def VerifyDomain(self):
        r"""<p>web domain name</p><p>Only valid when ChannelInfo is web</p>
        :rtype: str
        """
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyBundleId(self):
        r"""<p>app BundleId</p><p>Only valid when ChannelInfo is ios</p>
        :rtype: str
        """
        return self._VerifyBundleId

    @VerifyBundleId.setter
    def VerifyBundleId(self, VerifyBundleId):
        self._VerifyBundleId = VerifyBundleId

    @property
    def VerifyPackage(self):
        r"""<p>app package</p><p>Only valid when ChannelInfo is android</p>
        :rtype: str
        """
        return self._VerifyPackage

    @VerifyPackage.setter
    def VerifyPackage(self, VerifyPackage):
        self._VerifyPackage = VerifyPackage

    @property
    def CheckAppidSwitch(self):
        r"""<p>Whether to enable captcha encryption. 0: Off. 1: On</p>
        :rtype: int
        """
        return self._CheckAppidSwitch

    @CheckAppidSwitch.setter
    def CheckAppidSwitch(self, CheckAppidSwitch):
        self._CheckAppidSwitch = CheckAppidSwitch

    @property
    def CheckIvSwitch(self):
        r"""<p>Whether to enable non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Input 1 is allowed only when CheckAppidSwitch is 1</p>
        :rtype: int
        """
        return self._CheckIvSwitch

    @CheckIvSwitch.setter
    def CheckIvSwitch(self, CheckIvSwitch):
        self._CheckIvSwitch = CheckIvSwitch

    @property
    def CheckBoxStyle(self):
        r"""<p>Checkbox display method</p><p>Enumeration values:</p><ul><li>0: simplified version</li><li>1: basic version</li><li>2: invisible version</li></ul>
        :rtype: str
        """
        return self._CheckBoxStyle

    @CheckBoxStyle.setter
    def CheckBoxStyle(self, CheckBoxStyle):
        self._CheckBoxStyle = CheckBoxStyle


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._ChannelInfo = params.get("ChannelInfo")
        self._VerifyRank = params.get("VerifyRank")
        self._UserSetCapType = params.get("UserSetCapType")
        self._DefendMode = params.get("DefendMode")
        self._Tags = params.get("Tags")
        self._DisableInvisibleSwitch = params.get("DisableInvisibleSwitch")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyBundleId = params.get("VerifyBundleId")
        self._VerifyPackage = params.get("VerifyPackage")
        self._CheckAppidSwitch = params.get("CheckAppidSwitch")
        self._CheckIvSwitch = params.get("CheckIvSwitch")
        self._CheckBoxStyle = params.get("CheckBoxStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCaptchaInfoInternationalResponse(AbstractModel):
    r"""CreateCaptchaInfoInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data.</p>
        :type Data: int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data.</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class CreateIpWhiteListInternationalRequest(AbstractModel):
    r"""CreateIpWhiteListInternational request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>ip allowlist name</p>
        :type Name: str
        :param _CaptchaAppid: <p>Captcha appid</p>
        :type CaptchaAppid: int
        :param _Ip: <p>ip data</p>
        :type Ip: str
        :param _Comment: <p>Remark information.</p>
        :type Comment: str
        """
        self._Name = None
        self._CaptchaAppid = None
        self._Ip = None
        self._Comment = None

    @property
    def Name(self):
        r"""<p>ip allowlist name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CaptchaAppid(self):
        r"""<p>Captcha appid</p>
        :rtype: int
        """
        return self._CaptchaAppid

    @CaptchaAppid.setter
    def CaptchaAppid(self, CaptchaAppid):
        self._CaptchaAppid = CaptchaAppid

    @property
    def Ip(self):
        r"""<p>ip data</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Comment(self):
        r"""<p>Remark information.</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CaptchaAppid = params.get("CaptchaAppid")
        self._Ip = params.get("Ip")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIpWhiteListInternationalResponse(AbstractModel):
    r"""CreateIpWhiteListInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: int
        :param _IdList: <p>IP allowlist resource id</p>
        :type IdList: list of int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._IdList = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def IdList(self):
        r"""<p>IP allowlist resource id</p>
        :rtype: list of int
        """
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._IdList = params.get("IdList")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DeleteIpWhiteListInternationalRequest(AbstractModel):
    r"""DeleteIpWhiteListInternational request structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaAppid: <p>Captcha appid</p>
        :type CaptchaAppid: int
        :param _Id: <p>Record number</p>
        :type Id: int
        """
        self._CaptchaAppid = None
        self._Id = None

    @property
    def CaptchaAppid(self):
        r"""<p>Captcha appid</p>
        :rtype: int
        """
        return self._CaptchaAppid

    @CaptchaAppid.setter
    def CaptchaAppid(self, CaptchaAppid):
        self._CaptchaAppid = CaptchaAppid

    @property
    def Id(self):
        r"""<p>Record number</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._CaptchaAppid = params.get("CaptchaAppid")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIpWhiteListInternationalResponse(AbstractModel):
    r"""DeleteIpWhiteListInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha info</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha info</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaConsoleDataInternational(AbstractModel):
    r"""Paging query data result obj international

    """

    def __init__(self):
        r"""
        :param _DataList: <p>Paginated data array.</p>
        :type DataList: list of DescribeCaptchaConsoleSubDataInternational
        :param _Total: <p>Total pages</p>
        :type Total: int
        :param _PageIndex: <p>Current page</p>
        :type PageIndex: int
        """
        self._DataList = None
        self._Total = None
        self._PageIndex = None

    @property
    def DataList(self):
        r"""<p>Paginated data array.</p>
        :rtype: list of DescribeCaptchaConsoleSubDataInternational
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def Total(self):
        r"""<p>Total pages</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PageIndex(self):
        r"""<p>Current page</p>
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeCaptchaConsoleSubDataInternational()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._Total = params.get("Total")
        self._PageIndex = params.get("PageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaConsoleSubDataInternational(AbstractModel):
    r"""Verification code console query API v2 international

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: <p>Verification code id</p>
        :type CaptchaAppId: int
        :param _AppName: <p>Verification name</p>
        :type AppName: str
        :param _Domain: <p>Separate domain names with commas</p>
        :type Domain: str
        :param _EncryptKey: <p>Random key</p>
        :type EncryptKey: str
        :param _SceneType: <p>Verification scenario</p><p>Enumeration values:</p><ul><li>1: Account</li><li>2: SMS</li><li>3: Promotion</li><li>4: Comment</li><li>5: Data protection</li><li>6: Other</li></ul>
        :type SceneType: str
        :param _UserSetCapType: <p>Validation type</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must be 2</li><li>2: Sliding puzzle</li><li>8: Graphical point selection</li><li>9: Voice verification</li></ul>
        :type UserSetCapType: int
        :param _NoVerifyRule: <p>Intelligent verification-free</p><p>Enumeration values:</p><ul><li>0: disable</li><li>1: enable</li></ul>
        :type NoVerifyRule: int
        :param _CaptchaLanguage: <p>Language</p><p>Enumeration values:</p><ul><li>1: Self adaptive</li><li>2052: Simplified</li><li>1028: Traditional</li><li>1033: English</li></ul>
        :type CaptchaLanguage: str
        :param _VerifyRank: <p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :type VerifyRank: int
        :param _ChannelInfo: <p>Client type</p><p>Enumeration values:</p><ul><li>web: For web scenario usage</li><li>android: For Android client usage</li><li>ios: For iOS client usage</li></ul>
        :type ChannelInfo: str
        :param _DefendMode: <p>Interception mode</p><p>Enumeration values:</p><ul><li>block: interception mode</li><li>notify: perception mode</li></ul><p>Default value: notify</p>
        :type DefendMode: str
        :param _CreateTime: <p>Creation time.</p>
        :type CreateTime: str
        :param _UpdateTime: <p>Update time.</p>
        :type UpdateTime: str
        :param _CheckAppidSwitch: <p>Whether to enable captchaAppid encryption</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul>
        :type CheckAppidSwitch: int
        :param _Tags: <p>Resource tag.</p>
        :type Tags: list of str
        :param _CheckIvSwitch: <p>Whether to enable non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Disabled</li><li>1: Enabled</li></ul>
        :type CheckIvSwitch: int
        :param _DisableInvisibleSwitch: <p>Verification mechanism</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :type DisableInvisibleSwitch: str
        :param _VerifyDomain: <p>Web domain name</p><p>Valid only when ChannelInfo is web</p>
        :type VerifyDomain: str
        :param _VerifyBundleId: <p>app BundleId</p><p>Valid only when ChannelInfo is ios</p>
        :type VerifyBundleId: str
        :param _VerifyPackage: <p>app package</p><p>Only valid when ChannelInfo is android</p>
        :type VerifyPackage: str
        :param _CheckBoxStyle: <p>Checkbox display method</p><p>Enumeration values:</p><ul><li>0: simplified version</li><li>1: basic version</li><li>2: invisible version</li></ul>
        :type CheckBoxStyle: str
        :param _CustomerType: <p>Customer type</p><p>Enumeration values:</p><ul><li>0: General user</li><li>1: waf</li><li>2: EO</li></ul>
        :type CustomerType: str
        """
        self._CaptchaAppId = None
        self._AppName = None
        self._Domain = None
        self._EncryptKey = None
        self._SceneType = None
        self._UserSetCapType = None
        self._NoVerifyRule = None
        self._CaptchaLanguage = None
        self._VerifyRank = None
        self._ChannelInfo = None
        self._DefendMode = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CheckAppidSwitch = None
        self._Tags = None
        self._CheckIvSwitch = None
        self._DisableInvisibleSwitch = None
        self._VerifyDomain = None
        self._VerifyBundleId = None
        self._VerifyPackage = None
        self._CheckBoxStyle = None
        self._CustomerType = None

    @property
    def CaptchaAppId(self):
        r"""<p>Verification code id</p>
        :rtype: int
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppName(self):
        r"""<p>Verification name</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Domain(self):
        r"""<p>Separate domain names with commas</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def EncryptKey(self):
        r"""<p>Random key</p>
        :rtype: str
        """
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def SceneType(self):
        r"""<p>Verification scenario</p><p>Enumeration values:</p><ul><li>1: Account</li><li>2: SMS</li><li>3: Promotion</li><li>4: Comment</li><li>5: Data protection</li><li>6: Other</li></ul>
        :rtype: str
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def UserSetCapType(self):
        r"""<p>Validation type</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must be 2</li><li>2: Sliding puzzle</li><li>8: Graphical point selection</li><li>9: Voice verification</li></ul>
        :rtype: int
        """
        return self._UserSetCapType

    @UserSetCapType.setter
    def UserSetCapType(self, UserSetCapType):
        self._UserSetCapType = UserSetCapType

    @property
    def NoVerifyRule(self):
        r"""<p>Intelligent verification-free</p><p>Enumeration values:</p><ul><li>0: disable</li><li>1: enable</li></ul>
        :rtype: int
        """
        return self._NoVerifyRule

    @NoVerifyRule.setter
    def NoVerifyRule(self, NoVerifyRule):
        self._NoVerifyRule = NoVerifyRule

    @property
    def CaptchaLanguage(self):
        r"""<p>Language</p><p>Enumeration values:</p><ul><li>1: Self adaptive</li><li>2052: Simplified</li><li>1028: Traditional</li><li>1033: English</li></ul>
        :rtype: str
        """
        return self._CaptchaLanguage

    @CaptchaLanguage.setter
    def CaptchaLanguage(self, CaptchaLanguage):
        self._CaptchaLanguage = CaptchaLanguage

    @property
    def VerifyRank(self):
        r"""<p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :rtype: int
        """
        return self._VerifyRank

    @VerifyRank.setter
    def VerifyRank(self, VerifyRank):
        self._VerifyRank = VerifyRank

    @property
    def ChannelInfo(self):
        r"""<p>Client type</p><p>Enumeration values:</p><ul><li>web: For web scenario usage</li><li>android: For Android client usage</li><li>ios: For iOS client usage</li></ul>
        :rtype: str
        """
        return self._ChannelInfo

    @ChannelInfo.setter
    def ChannelInfo(self, ChannelInfo):
        self._ChannelInfo = ChannelInfo

    @property
    def DefendMode(self):
        r"""<p>Interception mode</p><p>Enumeration values:</p><ul><li>block: interception mode</li><li>notify: perception mode</li></ul><p>Default value: notify</p>
        :rtype: str
        """
        return self._DefendMode

    @DefendMode.setter
    def DefendMode(self, DefendMode):
        self._DefendMode = DefendMode

    @property
    def CreateTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CheckAppidSwitch(self):
        r"""<p>Whether to enable captchaAppid encryption</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul>
        :rtype: int
        """
        return self._CheckAppidSwitch

    @CheckAppidSwitch.setter
    def CheckAppidSwitch(self, CheckAppidSwitch):
        self._CheckAppidSwitch = CheckAppidSwitch

    @property
    def Tags(self):
        r"""<p>Resource tag.</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CheckIvSwitch(self):
        r"""<p>Whether to enable non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Disabled</li><li>1: Enabled</li></ul>
        :rtype: int
        """
        return self._CheckIvSwitch

    @CheckIvSwitch.setter
    def CheckIvSwitch(self, CheckIvSwitch):
        self._CheckIvSwitch = CheckIvSwitch

    @property
    def DisableInvisibleSwitch(self):
        r"""<p>Verification mechanism</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :rtype: str
        """
        return self._DisableInvisibleSwitch

    @DisableInvisibleSwitch.setter
    def DisableInvisibleSwitch(self, DisableInvisibleSwitch):
        self._DisableInvisibleSwitch = DisableInvisibleSwitch

    @property
    def VerifyDomain(self):
        r"""<p>Web domain name</p><p>Valid only when ChannelInfo is web</p>
        :rtype: str
        """
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyBundleId(self):
        r"""<p>app BundleId</p><p>Valid only when ChannelInfo is ios</p>
        :rtype: str
        """
        return self._VerifyBundleId

    @VerifyBundleId.setter
    def VerifyBundleId(self, VerifyBundleId):
        self._VerifyBundleId = VerifyBundleId

    @property
    def VerifyPackage(self):
        r"""<p>app package</p><p>Only valid when ChannelInfo is android</p>
        :rtype: str
        """
        return self._VerifyPackage

    @VerifyPackage.setter
    def VerifyPackage(self, VerifyPackage):
        self._VerifyPackage = VerifyPackage

    @property
    def CheckBoxStyle(self):
        r"""<p>Checkbox display method</p><p>Enumeration values:</p><ul><li>0: simplified version</li><li>1: basic version</li><li>2: invisible version</li></ul>
        :rtype: str
        """
        return self._CheckBoxStyle

    @CheckBoxStyle.setter
    def CheckBoxStyle(self, CheckBoxStyle):
        self._CheckBoxStyle = CheckBoxStyle

    @property
    def CustomerType(self):
        r"""<p>Customer type</p><p>Enumeration values:</p><ul><li>0: General user</li><li>1: waf</li><li>2: EO</li></ul>
        :rtype: str
        """
        return self._CustomerType

    @CustomerType.setter
    def CustomerType(self, CustomerType):
        self._CustomerType = CustomerType


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppName = params.get("AppName")
        self._Domain = params.get("Domain")
        self._EncryptKey = params.get("EncryptKey")
        self._SceneType = params.get("SceneType")
        self._UserSetCapType = params.get("UserSetCapType")
        self._NoVerifyRule = params.get("NoVerifyRule")
        self._CaptchaLanguage = params.get("CaptchaLanguage")
        self._VerifyRank = params.get("VerifyRank")
        self._ChannelInfo = params.get("ChannelInfo")
        self._DefendMode = params.get("DefendMode")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CheckAppidSwitch = params.get("CheckAppidSwitch")
        self._Tags = params.get("Tags")
        self._CheckIvSwitch = params.get("CheckIvSwitch")
        self._DisableInvisibleSwitch = params.get("DisableInvisibleSwitch")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyBundleId = params.get("VerifyBundleId")
        self._VerifyPackage = params.get("VerifyPackage")
        self._CheckBoxStyle = params.get("CheckBoxStyle")
        self._CustomerType = params.get("CustomerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaInfoListInternationalRequest(AbstractModel):
    r"""DescribeCaptchaInfoListInternational request structure.

    """

    def __init__(self):
        r"""
        :param _PageIndex: <p>Pagination parameter - page number</p>
        :type PageIndex: int
        :param _PageSize: <p>Pagination parameters - number of records per page</p>
        :type PageSize: int
        :param _UserSetCapTypeArr: <p>Query parameter - Behavior verification type</p><p>Enumeration values:</p><ul><li>1: Invisible verification</li><li>2: Slide verification</li><li>8: Graphical verification</li><li>9: Voice verification</li></ul>
        :type UserSetCapTypeArr: list of str
        :param _VerifyRankArr: <p>Query parameter - risk control level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul>
        :type VerifyRankArr: list of str
        :param _ChannelInfoArr: <p>Query parameter - client multiple selection</p><p>Enumeration values:</p><ul><li>web:</li><li>ios </li><li>android</li></ul>
        :type ChannelInfoArr: list of str
        :param _CaptchaAppId: <p>Query parameter -Captcha appid</p>
        :type CaptchaAppId: str
        :param _AppName: <p>Query parameter - Captcha name</p>
        :type AppName: str
        :param _OrderBy: <p>Sorting parameter</p><p>Input limits: desc: in descending order by creation time; asc: in ascending order by creation time</p>
        :type OrderBy: :class:`tencentcloud.captcha.v20190722.models.OrderByInternational`
        """
        self._PageIndex = None
        self._PageSize = None
        self._UserSetCapTypeArr = None
        self._VerifyRankArr = None
        self._ChannelInfoArr = None
        self._CaptchaAppId = None
        self._AppName = None
        self._OrderBy = None

    @property
    def PageIndex(self):
        r"""<p>Pagination parameter - page number</p>
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""<p>Pagination parameters - number of records per page</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserSetCapTypeArr(self):
        r"""<p>Query parameter - Behavior verification type</p><p>Enumeration values:</p><ul><li>1: Invisible verification</li><li>2: Slide verification</li><li>8: Graphical verification</li><li>9: Voice verification</li></ul>
        :rtype: list of str
        """
        return self._UserSetCapTypeArr

    @UserSetCapTypeArr.setter
    def UserSetCapTypeArr(self, UserSetCapTypeArr):
        self._UserSetCapTypeArr = UserSetCapTypeArr

    @property
    def VerifyRankArr(self):
        r"""<p>Query parameter - risk control level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul>
        :rtype: list of str
        """
        return self._VerifyRankArr

    @VerifyRankArr.setter
    def VerifyRankArr(self, VerifyRankArr):
        self._VerifyRankArr = VerifyRankArr

    @property
    def ChannelInfoArr(self):
        r"""<p>Query parameter - client multiple selection</p><p>Enumeration values:</p><ul><li>web:</li><li>ios </li><li>android</li></ul>
        :rtype: list of str
        """
        return self._ChannelInfoArr

    @ChannelInfoArr.setter
    def ChannelInfoArr(self, ChannelInfoArr):
        self._ChannelInfoArr = ChannelInfoArr

    @property
    def CaptchaAppId(self):
        r"""<p>Query parameter -Captcha appid</p>
        :rtype: str
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppName(self):
        r"""<p>Query parameter - Captcha name</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def OrderBy(self):
        r"""<p>Sorting parameter</p><p>Input limits: desc: in descending order by creation time; asc: in ascending order by creation time</p>
        :rtype: :class:`tencentcloud.captcha.v20190722.models.OrderByInternational`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        self._UserSetCapTypeArr = params.get("UserSetCapTypeArr")
        self._VerifyRankArr = params.get("VerifyRankArr")
        self._ChannelInfoArr = params.get("ChannelInfoArr")
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppName = params.get("AppName")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderByInternational()
            self._OrderBy._deserialize(params.get("OrderBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaInfoListInternationalResponse(AbstractModel):
    r"""DescribeCaptchaInfoListInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Data block after paging query.</p>
        :type Data: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaConsoleDataInternational`
        :param _CaptchaCode: <p>Captcha response code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Data block after paging query.</p>
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaConsoleDataInternational`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha response code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
            self._Data = DescribeCaptchaConsoleDataInternational()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaIpWhiteListDataNew(AbstractModel):
    r"""Ip allowlist paging query data result

    """

    def __init__(self):
        r"""
        :param _DataList: <p>Data list.</p>
        :type DataList: list of DescribeCaptchaWhiteListItem
        :param _Total: <p>Total number of records</p>
        :type Total: int
        :param _PageIndex: <p>Page number.</p>
        :type PageIndex: int
        """
        self._DataList = None
        self._Total = None
        self._PageIndex = None

    @property
    def DataList(self):
        r"""<p>Data list.</p>
        :rtype: list of DescribeCaptchaWhiteListItem
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def Total(self):
        r"""<p>Total number of records</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PageIndex(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DescribeCaptchaWhiteListItem()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._Total = params.get("Total")
        self._PageIndex = params.get("PageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaptchaResultRequest(AbstractModel):
    r"""DescribeCaptchaResult request structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaType: <p>Fixed value: 9.</p>
        :type CaptchaType: int
        :param _Ticket: <p>User verification ticket returned by the frontend callback function</p>
        :type Ticket: str
        :param _UserIp: <p>Public network IP of the verification</p>
        :type UserIp: str
        :param _Randstr: <p>Random string returned by the frontend callback function</p>
        :type Randstr: str
        :param _CaptchaAppId: <p>Captcha appId. Log in to the <a href="https://console.cloud.tencent.com/captcha/graphical">verification code console</a>. In the [Key] column of the verification list, you can see CaptchaAppId.</p>
        :type CaptchaAppId: int
        :param _AppSecretKey: <p>Captcha application key. Log in to the <a href="https://console.cloud.tencent.com/captcha/graphical">verification code console</a>, and view AppSecretKey in the [Key] column of the verification list. AppSecretKey is a key for server-side verification of verification code tickets. Keep it confidential and do not leak it to third parties.</p>
        :type AppSecretKey: str
        :param _BusinessId: <p>Reserved field</p>
        :type BusinessId: int
        :param _SceneId: <p>Reserved field</p>
        :type SceneId: int
        :param _MacAddress: <p>mac address or unique device identifier</p>
        :type MacAddress: str
        :param _Imei: <p>Mobile device number</p>
        :type Imei: str
        :param _NeedGetCaptchaTime: <p>Whether to return the time when the frontend obtains the verification code. Value: 1: need to return</p>
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
        r"""<p>Fixed value: 9.</p>
        :rtype: int
        """
        return self._CaptchaType

    @CaptchaType.setter
    def CaptchaType(self, CaptchaType):
        self._CaptchaType = CaptchaType

    @property
    def Ticket(self):
        r"""<p>User verification ticket returned by the frontend callback function</p>
        :rtype: str
        """
        return self._Ticket

    @Ticket.setter
    def Ticket(self, Ticket):
        self._Ticket = Ticket

    @property
    def UserIp(self):
        r"""<p>Public network IP of the verification</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Randstr(self):
        r"""<p>Random string returned by the frontend callback function</p>
        :rtype: str
        """
        return self._Randstr

    @Randstr.setter
    def Randstr(self, Randstr):
        self._Randstr = Randstr

    @property
    def CaptchaAppId(self):
        r"""<p>Captcha appId. Log in to the <a href="https://console.cloud.tencent.com/captcha/graphical">verification code console</a>. In the [Key] column of the verification list, you can see CaptchaAppId.</p>
        :rtype: int
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppSecretKey(self):
        r"""<p>Captcha application key. Log in to the <a href="https://console.cloud.tencent.com/captcha/graphical">verification code console</a>, and view AppSecretKey in the [Key] column of the verification list. AppSecretKey is a key for server-side verification of verification code tickets. Keep it confidential and do not leak it to third parties.</p>
        :rtype: str
        """
        return self._AppSecretKey

    @AppSecretKey.setter
    def AppSecretKey(self, AppSecretKey):
        self._AppSecretKey = AppSecretKey

    @property
    def BusinessId(self):
        r"""<p>Reserved field</p>
        :rtype: int
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def SceneId(self):
        r"""<p>Reserved field</p>
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def MacAddress(self):
        r"""<p>mac address or unique device identifier</p>
        :rtype: str
        """
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Imei(self):
        r"""<p>Mobile device number</p>
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def NeedGetCaptchaTime(self):
        r"""<p>Whether to return the time when the frontend obtains the verification code. Value: 1: need to return</p>
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
    r"""DescribeCaptchaResult response structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaCode: <p>1 OK verification passed<br>7 captcha no match The passed-in Randstr is invalid. Please check whether Randstr is consistent with the frontend Randstr.<br>8 ticket expired The passed-in ticket has expired (ticket valid period is 5 minutes). Please generate a new ticket and Randstr for verification.<br>9 ticket reused The passed-in ticket has been reused. Please generate a new ticket and Randstr for verification.<br>15 decrypt fail The passed-in ticket is invalid. Please check whether ticket is consistent with the frontend ticket.<br>16 appid-ticket mismatch The passed-in CaptchaAppId is incorrect. Please check whether CaptchaAppId is consistent with the frontend CaptchaAppId, and ensure that CaptchaAppId is obtained from [Verification Management] -> [Basic Configuration] in the verification code console.<br>21 diff Bill verification exception. Possible reasons: (1) If the ticket contains the trerror prefix, it is generally because the user has a poor network connection, which causes frontend automatic disaster recovery and generates a disaster recovery ticket. The business side can skip or post-process it based on needs. (2) If the ticket does not contain the trerror prefix, it is because the verification code risk control system has detected a security risk in the request. The business side can block it based on needs.<br>100 appid-secretkey-ticket mismatch Parameter validation error. (1) Please check whether CaptchaAppId and AppSecretKey are correct. CaptchaAppId and AppSecretKey need to be obtained from [Verification Management] > [Basic Configuration] in the verification code console. (2) Please check whether the passed-in ticket is generated by the passed-in CaptchaAppId.</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Description and error message</p>
        :type CaptchaMsg: str
        :param _EvilLevel: <p>In non-perception mode, this parameter returns the verification result:<br>EvilLevel=0: The request is not malicious<br>EvilLevel=100: The request is malicious</p>
        :type EvilLevel: int
        :param _GetCaptchaTime: <p>Frontend verification code retrieval time, Timestamp Format</p>
        :type GetCaptchaTime: int
        :param _EvilBitmap: <p>Interception type</p>
        :type EvilBitmap: int
        :param _SubmitCaptchaTime: <p>Time of submitting the verification code</p>
        :type SubmitCaptchaTime: int
        :param _DeviceRiskCategory: <p>Device risk category</p>
        :type DeviceRiskCategory: str
        :param _Score: <p>Verification code score</p><p>Value range: 0-100. Higher scores indicate higher risk</p>
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
        r"""<p>1 OK verification passed<br>7 captcha no match The passed-in Randstr is invalid. Please check whether Randstr is consistent with the frontend Randstr.<br>8 ticket expired The passed-in ticket has expired (ticket valid period is 5 minutes). Please generate a new ticket and Randstr for verification.<br>9 ticket reused The passed-in ticket has been reused. Please generate a new ticket and Randstr for verification.<br>15 decrypt fail The passed-in ticket is invalid. Please check whether ticket is consistent with the frontend ticket.<br>16 appid-ticket mismatch The passed-in CaptchaAppId is incorrect. Please check whether CaptchaAppId is consistent with the frontend CaptchaAppId, and ensure that CaptchaAppId is obtained from [Verification Management] -> [Basic Configuration] in the verification code console.<br>21 diff Bill verification exception. Possible reasons: (1) If the ticket contains the trerror prefix, it is generally because the user has a poor network connection, which causes frontend automatic disaster recovery and generates a disaster recovery ticket. The business side can skip or post-process it based on needs. (2) If the ticket does not contain the trerror prefix, it is because the verification code risk control system has detected a security risk in the request. The business side can block it based on needs.<br>100 appid-secretkey-ticket mismatch Parameter validation error. (1) Please check whether CaptchaAppId and AppSecretKey are correct. CaptchaAppId and AppSecretKey need to be obtained from [Verification Management] > [Basic Configuration] in the verification code console. (2) Please check whether the passed-in ticket is generated by the passed-in CaptchaAppId.</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Description and error message</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

    @property
    def EvilLevel(self):
        r"""<p>In non-perception mode, this parameter returns the verification result:<br>EvilLevel=0: The request is not malicious<br>EvilLevel=100: The request is malicious</p>
        :rtype: int
        """
        return self._EvilLevel

    @EvilLevel.setter
    def EvilLevel(self, EvilLevel):
        self._EvilLevel = EvilLevel

    @property
    def GetCaptchaTime(self):
        r"""<p>Frontend verification code retrieval time, Timestamp Format</p>
        :rtype: int
        """
        return self._GetCaptchaTime

    @GetCaptchaTime.setter
    def GetCaptchaTime(self, GetCaptchaTime):
        self._GetCaptchaTime = GetCaptchaTime

    @property
    def EvilBitmap(self):
        r"""<p>Interception type</p>
        :rtype: int
        """
        return self._EvilBitmap

    @EvilBitmap.setter
    def EvilBitmap(self, EvilBitmap):
        self._EvilBitmap = EvilBitmap

    @property
    def SubmitCaptchaTime(self):
        r"""<p>Time of submitting the verification code</p>
        :rtype: int
        """
        return self._SubmitCaptchaTime

    @SubmitCaptchaTime.setter
    def SubmitCaptchaTime(self, SubmitCaptchaTime):
        self._SubmitCaptchaTime = SubmitCaptchaTime

    @property
    def DeviceRiskCategory(self):
        r"""<p>Device risk category</p>
        :rtype: str
        """
        return self._DeviceRiskCategory

    @DeviceRiskCategory.setter
    def DeviceRiskCategory(self, DeviceRiskCategory):
        self._DeviceRiskCategory = DeviceRiskCategory

    @property
    def Score(self):
        r"""<p>Verification code score</p><p>Value range: 0-100. Higher scores indicate higher risk</p>
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

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
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._EvilLevel = params.get("EvilLevel")
        self._GetCaptchaTime = params.get("GetCaptchaTime")
        self._EvilBitmap = params.get("EvilBitmap")
        self._SubmitCaptchaTime = params.get("SubmitCaptchaTime")
        self._DeviceRiskCategory = params.get("DeviceRiskCategory")
        self._Score = params.get("Score")
        self._RequestId = params.get("RequestId")


class DescribeCaptchaWhiteListItem(AbstractModel):
    r"""ip whitelist data sub-item in the verification code console

    """

    def __init__(self):
        r"""
        :param _Id: <p>No.</p>
        :type Id: int
        :param _Name: <p>Allowlist name</p>
        :type Name: str
        :param _CaptchaAppid: <p>Bind captcha</p>
        :type CaptchaAppid: int
        :param _Ip: <p>ip address</p>
        :type Ip: str
        :param _Status: <p>Status. 0: Ip allowlisted; 1: cancel allowlisting</p>
        :type Status: int
        :param _CreatedTime: <p>Creation time.</p>
        :type CreatedTime: str
        :param _UpdatedTime: <p>Update time.</p>
        :type UpdatedTime: str
        :param _Comment: <p>Remarks.</p>
        :type Comment: str
        """
        self._Id = None
        self._Name = None
        self._CaptchaAppid = None
        self._Ip = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Comment = None

    @property
    def Id(self):
        r"""<p>No.</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>Allowlist name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CaptchaAppid(self):
        r"""<p>Bind captcha</p>
        :rtype: int
        """
        return self._CaptchaAppid

    @CaptchaAppid.setter
    def CaptchaAppid(self, CaptchaAppid):
        self._CaptchaAppid = CaptchaAppid

    @property
    def Ip(self):
        r"""<p>ip address</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        r"""<p>Status. 0: Ip allowlisted; 1: cancel allowlisting</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Comment(self):
        r"""<p>Remarks.</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._CaptchaAppid = params.get("CaptchaAppid")
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpWhiteListInternationalRequest(AbstractModel):
    r"""DescribeIpWhiteListInternational request structure.

    """

    def __init__(self):
        r"""
        :param _PageIndex: <p>Page number.</p>
        :type PageIndex: int
        :param _PageSize: <p>Page length.</p>
        :type PageSize: int
        :param _CaptchaAppid: <p>Captcha appid</p>
        :type CaptchaAppid: int
        :param _Name: <p>Allowlist name</p>
        :type Name: str
        :param _Ip: <p>Ip address</p>
        :type Ip: str
        :param _Status: <p>IP Whitelist Configuration Status</p><p>Enumeration values:</p><ul><li>0: all</li><li>1: allowlisted</li><li>2: allowlisting canceled</li></ul><p>Default value: 0</p>
        :type Status: int
        """
        self._PageIndex = None
        self._PageSize = None
        self._CaptchaAppid = None
        self._Name = None
        self._Ip = None
        self._Status = None

    @property
    def PageIndex(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""<p>Page length.</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def CaptchaAppid(self):
        r"""<p>Captcha appid</p>
        :rtype: int
        """
        return self._CaptchaAppid

    @CaptchaAppid.setter
    def CaptchaAppid(self, CaptchaAppid):
        self._CaptchaAppid = CaptchaAppid

    @property
    def Name(self):
        r"""<p>Allowlist name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ip(self):
        r"""<p>Ip address</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        r"""<p>IP Whitelist Configuration Status</p><p>Enumeration values:</p><ul><li>0: all</li><li>1: allowlisted</li><li>2: allowlisting canceled</li></ul><p>Default value: 0</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        self._CaptchaAppid = params.get("CaptchaAppid")
        self._Name = params.get("Name")
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpWhiteListInternationalResponse(AbstractModel):
    r"""DescribeIpWhiteListInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaIpWhiteListDataNew`
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaIpWhiteListDataNew`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
            self._Data = DescribeCaptchaIpWhiteListDataNew()
            self._Data._deserialize(params.get("Data"))
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class ModifyCaptchaInfoInternationalRequest(AbstractModel):
    r"""ModifyCaptchaInfoInternational request structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: <p>Captcha appid</p>
        :type CaptchaAppId: str
        :param _AppName: <p>Captcha name</p>
        :type AppName: str
        :param _VerifyRank: <p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :type VerifyRank: str
        :param _UserSetCapType: <p>Verification method</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must</li><li>2: Slide verification</li><li>8: Graphical verification</li><li>9: Voice verification</li></ul>
        :type UserSetCapType: str
        :param _DefendMode: <p>Interception mode</p><p>Enumeration values:</p><ul><li>notify: perception mode</li><li>block: interception mode</li></ul>
        :type DefendMode: str
        :param _CheckAppidSwitch: <p>Whether to enable captcha encryption. 0: Off. 1: On</p>
        :type CheckAppidSwitch: int
        :param _CheckIvSwitch: <p>Whether to enable Non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Input 1 is allowed only when CheckAppidSwitch is 1</p>
        :type CheckIvSwitch: int
        :param _DisableInvisibleSwitch: <p>Verification mechanism: '0' One-Click Verification, '1' Always verify, '2' Invisible verification</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :type DisableInvisibleSwitch: str
        :param _VerifyDomain: <p>Web domain name</p><p>Only valid when ChannelInfo is web</p>
        :type VerifyDomain: str
        :param _VerifyBundleId: <p>app BundleId</p><p>Valid only when ChannelInfo is ios</p>
        :type VerifyBundleId: str
        :param _VerifyPackage: <p>app package</p><p>Valid only when ChannelInfo is android</p>
        :type VerifyPackage: str
        :param _Tags: <p>Resource tag, key&amp;value format</p>
        :type Tags: list of str
        :param _CheckBoxStyle: <p>Checkbox display method. '0': minimalist mode, '1': full mode, '2': not set</p>
        :type CheckBoxStyle: str
        """
        self._CaptchaAppId = None
        self._AppName = None
        self._VerifyRank = None
        self._UserSetCapType = None
        self._DefendMode = None
        self._CheckAppidSwitch = None
        self._CheckIvSwitch = None
        self._DisableInvisibleSwitch = None
        self._VerifyDomain = None
        self._VerifyBundleId = None
        self._VerifyPackage = None
        self._Tags = None
        self._CheckBoxStyle = None

    @property
    def CaptchaAppId(self):
        r"""<p>Captcha appid</p>
        :rtype: str
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId

    @property
    def AppName(self):
        r"""<p>Captcha name</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def VerifyRank(self):
        r"""<p>Verification level</p><p>Enumeration values:</p><ul><li>1: Experience-oriented</li><li>2: Balanced</li><li>3: Security-focused</li></ul><p>Default value: 1</p>
        :rtype: str
        """
        return self._VerifyRank

    @VerifyRank.setter
    def VerifyRank(self, VerifyRank):
        self._VerifyRank = VerifyRank

    @property
    def UserSetCapType(self):
        r"""<p>Verification method</p><p>Enumeration values:</p><ul><li>1: Invisible verification. UserSetCapType input 1, DisableInvisibleSwitch must</li><li>2: Slide verification</li><li>8: Graphical verification</li><li>9: Voice verification</li></ul>
        :rtype: str
        """
        return self._UserSetCapType

    @UserSetCapType.setter
    def UserSetCapType(self, UserSetCapType):
        self._UserSetCapType = UserSetCapType

    @property
    def DefendMode(self):
        r"""<p>Interception mode</p><p>Enumeration values:</p><ul><li>notify: perception mode</li><li>block: interception mode</li></ul>
        :rtype: str
        """
        return self._DefendMode

    @DefendMode.setter
    def DefendMode(self, DefendMode):
        self._DefendMode = DefendMode

    @property
    def CheckAppidSwitch(self):
        r"""<p>Whether to enable captcha encryption. 0: Off. 1: On</p>
        :rtype: int
        """
        return self._CheckAppidSwitch

    @CheckAppidSwitch.setter
    def CheckAppidSwitch(self, CheckAppidSwitch):
        self._CheckAppidSwitch = CheckAppidSwitch

    @property
    def CheckIvSwitch(self):
        r"""<p>Whether to enable Non-repeating IV</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Input 1 is allowed only when CheckAppidSwitch is 1</p>
        :rtype: int
        """
        return self._CheckIvSwitch

    @CheckIvSwitch.setter
    def CheckIvSwitch(self, CheckIvSwitch):
        self._CheckIvSwitch = CheckIvSwitch

    @property
    def DisableInvisibleSwitch(self):
        r"""<p>Verification mechanism: '0' One-Click Verification, '1' Always verify, '2' Invisible verification</p><p>Enumeration values:</p><ul><li>0: One-Click Verification</li><li>1: Always verify</li><li>2: Invisible verification. DisableInvisibleSwitch input 2, UserSetCapType must be 1</li></ul>
        :rtype: str
        """
        return self._DisableInvisibleSwitch

    @DisableInvisibleSwitch.setter
    def DisableInvisibleSwitch(self, DisableInvisibleSwitch):
        self._DisableInvisibleSwitch = DisableInvisibleSwitch

    @property
    def VerifyDomain(self):
        r"""<p>Web domain name</p><p>Only valid when ChannelInfo is web</p>
        :rtype: str
        """
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyBundleId(self):
        r"""<p>app BundleId</p><p>Valid only when ChannelInfo is ios</p>
        :rtype: str
        """
        return self._VerifyBundleId

    @VerifyBundleId.setter
    def VerifyBundleId(self, VerifyBundleId):
        self._VerifyBundleId = VerifyBundleId

    @property
    def VerifyPackage(self):
        r"""<p>app package</p><p>Valid only when ChannelInfo is android</p>
        :rtype: str
        """
        return self._VerifyPackage

    @VerifyPackage.setter
    def VerifyPackage(self, VerifyPackage):
        self._VerifyPackage = VerifyPackage

    @property
    def Tags(self):
        r"""<p>Resource tag, key&amp;value format</p>
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CheckBoxStyle(self):
        r"""<p>Checkbox display method. '0': minimalist mode, '1': full mode, '2': not set</p>
        :rtype: str
        """
        return self._CheckBoxStyle

    @CheckBoxStyle.setter
    def CheckBoxStyle(self, CheckBoxStyle):
        self._CheckBoxStyle = CheckBoxStyle


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        self._AppName = params.get("AppName")
        self._VerifyRank = params.get("VerifyRank")
        self._UserSetCapType = params.get("UserSetCapType")
        self._DefendMode = params.get("DefendMode")
        self._CheckAppidSwitch = params.get("CheckAppidSwitch")
        self._CheckIvSwitch = params.get("CheckIvSwitch")
        self._DisableInvisibleSwitch = params.get("DisableInvisibleSwitch")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyBundleId = params.get("VerifyBundleId")
        self._VerifyPackage = params.get("VerifyPackage")
        self._Tags = params.get("Tags")
        self._CheckBoxStyle = params.get("CheckBoxStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCaptchaInfoInternationalResponse(AbstractModel):
    r"""ModifyCaptchaInfoInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class ModifyIpWhiteListInternationalRequest(AbstractModel):
    r"""ModifyIpWhiteListInternational request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>ip allowlist name</p>
        :type Name: str
        :param _Id: <p>Record number</p>
        :type Id: int
        :param _CaptchaAppid: <p>Captcha appid</p>
        :type CaptchaAppid: int
        :param _Status: <p>IP whitelist status</p><p>Enumeration values:</p><ul><li>0: enable</li><li>1: disable</li></ul>
        :type Status: int
        :param _Comment: <p>Remark information.</p>
        :type Comment: str
        """
        self._Name = None
        self._Id = None
        self._CaptchaAppid = None
        self._Status = None
        self._Comment = None

    @property
    def Name(self):
        r"""<p>ip allowlist name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        r"""<p>Record number</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CaptchaAppid(self):
        r"""<p>Captcha appid</p>
        :rtype: int
        """
        return self._CaptchaAppid

    @CaptchaAppid.setter
    def CaptchaAppid(self, CaptchaAppid):
        self._CaptchaAppid = CaptchaAppid

    @property
    def Status(self):
        r"""<p>IP whitelist status</p><p>Enumeration values:</p><ul><li>0: enable</li><li>1: disable</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Comment(self):
        r"""<p>Remark information.</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._CaptchaAppid = params.get("CaptchaAppid")
        self._Status = params.get("Status")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpWhiteListInternationalResponse(AbstractModel):
    r"""ModifyIpWhiteListInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")


class OrderByInternational(AbstractModel):
    r"""General international parameter used for front-end sorting and processing.

    """

    def __init__(self):
        r"""
        :param _CreateTime: Sort by creation time
        :type CreateTime: str
        """
        self._CreateTime = None

    @property
    def CreateTime(self):
        r"""Sort by creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveCaptchaInfoInternationalRequest(AbstractModel):
    r"""RemoveCaptchaInfoInternational request structure.

    """

    def __init__(self):
        r"""
        :param _CaptchaAppId: <p>Captcha AppId</p>
        :type CaptchaAppId: str
        """
        self._CaptchaAppId = None

    @property
    def CaptchaAppId(self):
        r"""<p>Captcha AppId</p>
        :rtype: str
        """
        return self._CaptchaAppId

    @CaptchaAppId.setter
    def CaptchaAppId(self, CaptchaAppId):
        self._CaptchaAppId = CaptchaAppId


    def _deserialize(self, params):
        self._CaptchaAppId = params.get("CaptchaAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveCaptchaInfoInternationalResponse(AbstractModel):
    r"""RemoveCaptchaInfoInternational response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Result data</p>
        :type Data: int
        :param _CaptchaCode: <p>Captcha status code</p>
        :type CaptchaCode: int
        :param _CaptchaMsg: <p>Captcha information</p>
        :type CaptchaMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._CaptchaCode = None
        self._CaptchaMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Result data</p>
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CaptchaCode(self):
        r"""<p>Captcha status code</p>
        :rtype: int
        """
        return self._CaptchaCode

    @CaptchaCode.setter
    def CaptchaCode(self, CaptchaCode):
        self._CaptchaCode = CaptchaCode

    @property
    def CaptchaMsg(self):
        r"""<p>Captcha information</p>
        :rtype: str
        """
        return self._CaptchaMsg

    @CaptchaMsg.setter
    def CaptchaMsg(self, CaptchaMsg):
        self._CaptchaMsg = CaptchaMsg

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
        self._Data = params.get("Data")
        self._CaptchaCode = params.get("CaptchaCode")
        self._CaptchaMsg = params.get("CaptchaMsg")
        self._RequestId = params.get("RequestId")