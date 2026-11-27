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


class AccountFactoryItem(AbstractModel):
    r"""Account Factory baseline items.

    """

    def __init__(self):
        r"""
        :param _Identifier: Unique ID of the Account Factory baseline item, which can contain only English letters, numbers, and symbols (@,._[]-:()+=), and must be 2 to 128 characters in length.
        :type Identifier: str
        :param _Name: Baseline item name, which is unique, supports only the combination of English letters, digits, and symbols (@&_[]-), and is 1 to 25 characters in length.
        :type Name: str
        :param _NameEn: Baseline item English name, which must be unique, can contain only English letters, numbers, spaces, and symbols (@&_[]-), and must be 1 to 64 characters in length.
        :type NameEn: str
        :param _Weight: Baseline item weight. A smaller value indicates a higher priority. Value range: greater than or equal to 0.
        :type Weight: int
        :param _Required: Whether the baseline item is required. Valid values: 1 (yes) and 0 (no).
        :type Required: int
        :param _DependsOn: Baseline item dependencies. The value range of N depends on the number of other baseline items that the current baseline item depends on.
        :type DependsOn: list of DependsOnItem
        :param _Description: Baseline description, which is 2 to 256 English characters in length. The default value is empty.
        :type Description: str
        :param _DescriptionEn: Baseline item English description, which is 2 to 1024 English characters in length. The default value is empty.
        :type DescriptionEn: str
        :param _Classify: Baseline category, which is 2 to 32 English characters in length and cannot be empty.
        :type Classify: str
        :param _ClassifyEn: Baseline English category, which is 2 to 64 English characters in length and cannot be empty.
        :type ClassifyEn: str
        """
        self._Identifier = None
        self._Name = None
        self._NameEn = None
        self._Weight = None
        self._Required = None
        self._DependsOn = None
        self._Description = None
        self._DescriptionEn = None
        self._Classify = None
        self._ClassifyEn = None

    @property
    def Identifier(self):
        r"""Unique ID of the Account Factory baseline item, which can contain only English letters, numbers, and symbols (@,._[]-:()+=), and must be 2 to 128 characters in length.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Name(self):
        r"""Baseline item name, which is unique, supports only the combination of English letters, digits, and symbols (@&_[]-), and is 1 to 25 characters in length.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NameEn(self):
        r"""Baseline item English name, which must be unique, can contain only English letters, numbers, spaces, and symbols (@&_[]-), and must be 1 to 64 characters in length.
        :rtype: str
        """
        return self._NameEn

    @NameEn.setter
    def NameEn(self, NameEn):
        self._NameEn = NameEn

    @property
    def Weight(self):
        r"""Baseline item weight. A smaller value indicates a higher priority. Value range: greater than or equal to 0.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Required(self):
        r"""Whether the baseline item is required. Valid values: 1 (yes) and 0 (no).
        :rtype: int
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DependsOn(self):
        r"""Baseline item dependencies. The value range of N depends on the number of other baseline items that the current baseline item depends on.
        :rtype: list of DependsOnItem
        """
        return self._DependsOn

    @DependsOn.setter
    def DependsOn(self, DependsOn):
        self._DependsOn = DependsOn

    @property
    def Description(self):
        r"""Baseline description, which is 2 to 256 English characters in length. The default value is empty.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptionEn(self):
        r"""Baseline item English description, which is 2 to 1024 English characters in length. The default value is empty.
        :rtype: str
        """
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn

    @property
    def Classify(self):
        r"""Baseline category, which is 2 to 32 English characters in length and cannot be empty.
        :rtype: str
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify

    @property
    def ClassifyEn(self):
        r"""Baseline English category, which is 2 to 64 English characters in length and cannot be empty.
        :rtype: str
        """
        return self._ClassifyEn

    @ClassifyEn.setter
    def ClassifyEn(self, ClassifyEn):
        self._ClassifyEn = ClassifyEn


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Name = params.get("Name")
        self._NameEn = params.get("NameEn")
        self._Weight = params.get("Weight")
        self._Required = params.get("Required")
        if params.get("DependsOn") is not None:
            self._DependsOn = []
            for item in params.get("DependsOn"):
                obj = DependsOnItem()
                obj._deserialize(item)
                self._DependsOn.append(obj)
        self._Description = params.get("Description")
        self._DescriptionEn = params.get("DescriptionEn")
        self._Classify = params.get("Classify")
        self._ClassifyEn = params.get("ClassifyEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineConfigItem(AbstractModel):
    r"""Account Factory baseline configuration item.

    """

    def __init__(self):
        r"""
        :param _Identifier: Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        :param _Configuration: Account factory baseline item configuration. different baseline item configuration parameters.
        :type Configuration: str
        """
        self._Identifier = None
        self._Configuration = None

    @property
    def Identifier(self):
        r"""Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Configuration(self):
        r"""Account factory baseline item configuration. different baseline item configuration parameters.
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Configuration = params.get("Configuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineInfoItem(AbstractModel):
    r"""Account factory baseline information.

    """

    def __init__(self):
        r"""
        :param _Identifier: Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        :param _Configuration: Account factory baseline item configuration. different baseline item configuration parameters.
        :type Configuration: str
        :param _ApplyCount: Specifies the number of accounts for baseline applications.
        :type ApplyCount: int
        """
        self._Identifier = None
        self._Configuration = None
        self._ApplyCount = None

    @property
    def Identifier(self):
        r"""Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Configuration(self):
        r"""Account factory baseline item configuration. different baseline item configuration parameters.
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ApplyCount(self):
        r"""Specifies the number of accounts for baseline applications.
        :rtype: int
        """
        return self._ApplyCount

    @ApplyCount.setter
    def ApplyCount(self, ApplyCount):
        self._ApplyCount = ApplyCount


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Configuration = params.get("Configuration")
        self._ApplyCount = params.get("ApplyCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineStepTaskInfo(AbstractModel):
    r"""Baseline item deployment task information list.

    """

    def __init__(self):
        r"""
        :param _TaskId: Specifies the unique Id of the task, which can only contain english letters and digits, and is a 16-character random string.
        :type TaskId: str
        :param _Identifier: Specifies the unique identifier for the baseline feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        :param _MemberUin: Specifies the member account uin of the applied baseline item.
        :type MemberUin: int
        :param _Status: Baseline item application status. Running means the baseline item is in application. Success means the baseline item application is successful. Failed means the baseline item application failure. Pending means the baseline item is Pending application. Skipped means the baseline item is Skipped.
        :type Status: str
        :param _ErrCode: Error code
        :type ErrCode: str
        :param _ErrMessage: Error message
        :type ErrMessage: str
        :param _Output: Baseline item deployment output.
        :type Output: str
        :param _CreateTime: Creation time, represented in ISO8601 standard format as yyyy-MM-dd hh:MM:ss.
        :type CreateTime: str
        :param _UpdateTime: Specifies the last update time in ISO8601 standard representation with format yyyy-MM-dd hh:MM:ss.
        :type UpdateTime: str
        """
        self._TaskId = None
        self._Identifier = None
        self._MemberUin = None
        self._Status = None
        self._ErrCode = None
        self._ErrMessage = None
        self._Output = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TaskId(self):
        r"""Specifies the unique Id of the task, which can only contain english letters and digits, and is a 16-character random string.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Identifier(self):
        r"""Specifies the unique identifier for the baseline feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def MemberUin(self):
        r"""Specifies the member account uin of the applied baseline item.
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Status(self):
        r"""Baseline item application status. Running means the baseline item is in application. Success means the baseline item application is successful. Failed means the baseline item application failure. Pending means the baseline item is Pending application. Skipped means the baseline item is Skipped.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        r"""Error code
        :rtype: str
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMessage(self):
        r"""Error message
        :rtype: str
        """
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage

    @property
    def Output(self):
        r"""Baseline item deployment output.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def CreateTime(self):
        r"""Creation time, represented in ISO8601 standard format as yyyy-MM-dd hh:MM:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Specifies the last update time in ISO8601 standard representation with format yyyy-MM-dd hh:MM:ss.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Identifier = params.get("Identifier")
        self._MemberUin = params.get("MemberUin")
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMessage = params.get("ErrMessage")
        self._Output = params.get("Output")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesRequest(AbstractModel):
    r"""BatchApplyAccountBaselines request structure.

    """

    def __init__(self):
        r"""
        :param _MemberUinList: Member account UIN, which is also the UIN of the account to which the baseline is applied.
        :type MemberUinList: list of int
        :param _BaselineConfigItems: List of baseline item configuration information.
        :type BaselineConfigItems: list of BaselineConfigItem
        """
        self._MemberUinList = None
        self._BaselineConfigItems = None

    @property
    def MemberUinList(self):
        r"""Member account UIN, which is also the UIN of the account to which the baseline is applied.
        :rtype: list of int
        """
        return self._MemberUinList

    @MemberUinList.setter
    def MemberUinList(self, MemberUinList):
        self._MemberUinList = MemberUinList

    @property
    def BaselineConfigItems(self):
        r"""List of baseline item configuration information.
        :rtype: list of BaselineConfigItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems


    def _deserialize(self, params):
        self._MemberUinList = params.get("MemberUinList")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineConfigItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesResponse(AbstractModel):
    r"""BatchApplyAccountBaselines response structure.

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


class DependsOnItem(AbstractModel):
    r"""Dependency items.

    """

    def __init__(self):
        r"""
        :param _Type: Dependency item type. Valid values: LandingZoneSetUp (Landing Zone dependency) and AccountFactorySetUp (Account Factory dependency).
        :type Type: str
        :param _Identifier: Feature item unique ID, which can contain only English letters, numbers, and symbols (@,._[]-:()+=), and must be 2 to 128 characters in length.
        :type Identifier: str
        """
        self._Type = None
        self._Identifier = None

    @property
    def Type(self):
        r"""Dependency item type. Valid values: LandingZoneSetUp (Landing Zone dependency) and AccountFactorySetUp (Account Factory dependency).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Identifier(self):
        r"""Feature item unique ID, which can contain only English letters, numbers, and symbols (@,._[]-:()+=), and must be 2 to 128 characters in length.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Identifier = params.get("Identifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAccountFactoryBaselineRequest(AbstractModel):
    r"""GetAccountFactoryBaseline request structure.

    """


class GetAccountFactoryBaselineResponse(AbstractModel):
    r"""GetAccountFactoryBaseline response structure.

    """

    def __init__(self):
        r"""
        :param _OwnerUin: Specifies the uin of the main account to which the resource belongs.
        :type OwnerUin: int
        :param _Name: Specifies the baseline item name, which must be unique and can only contain a combination of english letters, digits, chinese characters, and symbols @, &_[]-, with a length of 1-25 chinese or english characters.
        :type Name: str
        :param _BaselineConfigItems: List of baseline item configurations.
        :type BaselineConfigItems: list of BaselineInfoItem
        :param _CreateTime: Creation time, represented in ISO8601 standard format as yyyy-MM-dd hh:MM:ss.
        :type CreateTime: str
        :param _UpdateTime: Specifies the last update time in ISO8601 standard representation with format yyyy-MM-dd hh:MM:ss.
        :type UpdateTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OwnerUin = None
        self._Name = None
        self._BaselineConfigItems = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        r"""Specifies the uin of the main account to which the resource belongs.
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Name(self):
        r"""Specifies the baseline item name, which must be unique and can only contain a combination of english letters, digits, chinese characters, and symbols @, &_[]-, with a length of 1-25 chinese or english characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaselineConfigItems(self):
        r"""List of baseline item configurations.
        :rtype: list of BaselineInfoItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems

    @property
    def CreateTime(self):
        r"""Creation time, represented in ISO8601 standard format as yyyy-MM-dd hh:MM:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Specifies the last update time in ISO8601 standard representation with format yyyy-MM-dd hh:MM:ss.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._OwnerUin = params.get("OwnerUin")
        self._Name = params.get("Name")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineInfoItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ListAccountFactoryBaselineItemsRequest(AbstractModel):
    r"""ListAccountFactoryBaselineItems request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Maximum number of returned records. Value range: 0-200.
        :type Limit: int
        :param _Offset: Offset. Value range: greater than or equal to 0.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""Maximum number of returned records. Value range: 0-200.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Value range: greater than or equal to 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountFactoryBaselineItemsResponse(AbstractModel):
    r"""ListAccountFactoryBaselineItems response structure.

    """

    def __init__(self):
        r"""
        :param _BaselineItems: <p>Account Factory baseline list.<br><strong>1. TCC-AF_ACCOUNT_CONTACT Account contact</strong><br>This baseline item is used to create message recipients (contacts) under a member account.<br>Field    Type    Required    Default value    Valid values and description<br>AccountContacts    Object array    Yes    None    Contact list, up to 50 entries, cannot be empty<br>AccountContacts[].Name    String    Yes    None    Contact name, must be an existing name in the account; cannot be duplicated within the same list; no fixed format restrictions<br>AccountContacts[].CountryCode    String    Yes    None    Phone country code, such as 86; no fixed enumeration<br>AccountContacts[].PhoneNum    String    Yes    None    Phone number, must be verified before this baseline item can be applied; format is determined by the verification process, with no local format restrictions<br>AccountContacts[].Email    String    Yes    None    Email address, must be verified before this baseline item can be applied; format is determined by the verification process, with no local format restrictions<br>AccountContacts[].Remark    String    No    None    Remarks, no length limit specified<br><pre><code>{  &quot;AccountContacts&quot;: [    {      &quot;Name&quot;: &quot;ops-admin&quot;,      &quot;CountryCode&quot;: &quot;86&quot;,      &quot;PhoneNum&quot;: &quot;13800***000&quot;,      &quot;Email&quot;: &quot;ops@ex***le.com&quot;,      &quot;Remark&quot;: &quot;Ops contact&quot;    }  ]}</code></pre><strong>2. TCC-AF_ACCOUNT_NOTIFICATION Message recipient</strong><br>China site:<br>Field    Type    Required    Default value    Valid values and description<br>Subscriptions    Object array    Yes    None    Subscription list, recommended not to exceed 50 entries; if exceeded, process in batches, will not be rejected due to the number of entries<br>Subscriptions[].Name    String    Yes    None    Single sub-user name; enter an existing sub-user name, otherwise the subscription does not take effect<br>Subscriptions[].ProductId    Integer    Yes    None    Product ID, no fixed enumeration, query through DescribeProductIds<br>Subscriptions[].MsgType    Integer    Yes    None    Message type ID, no fixed enumeration, query through DescribeFirstSiteMsgType and DescribeSecondMsgType<br>Subscriptions[].Channel    Integer    Yes    None    Message delivery channel, bitmask, see the table below for values<br>Subscriptions[].Status    String    Yes    None    Only Open or Close; only Open creates a subscription, Close or other values do not take effect</p><p>Channel bitmask:<br>Channel    Value<br>Inbox message    1<br>Email    2<br>SMS    4<br>WeChat    8 (not available on the international site)<br>Voice    16<br>WeCom    32 (not available on the international site)</p><p>Channel combination    Value<br>Inbox message + Email    3<br>Inbox message + SMS    5<br>Email + SMS    6<br>Inbox message + Email + SMS    7</p><p>International site fields:<br>Field    Type    Required    Default value    Valid values and description<br>Subscriptions    Object array    Yes    None    Subscription list, recommended not to exceed 50 entries; if exceeded, process in batches, will not be rejected due to the number of entries<br>Subscriptions[].Name    String array    Yes    None    Sub-user name list; enter existing sub-user names, names will be deduplicated<br>Subscriptions[].MsgType    Integer    Yes    None    Message type ID, no fixed enumeration, query through DescribeFirstSiteMsgType and DescribeSecondMsgType<br>Subscriptions[].Channel    Integer    Yes    None    Message delivery channel, bitmask, values same as the table above</p><p>China site example:<br><pre><code>{  &quot;Subscriptions&quot;: [    {      &quot;Name&quot;: &quot;ops-admin&quot;,      &quot;ProductId&quot;: 1001,      &quot;MsgType&quot;: 2001,      &quot;Channel&quot;: 3,      &quot;Status&quot;: &quot;Open&quot;    }  ]}</code></pre>International site example:<br><pre><code>{  &quot;Subscriptions&quot;: [    {      &quot;Name&quot;: [&quot;ops-admin&quot;, &quot;audit&quot;],      &quot;MsgType&quot;: 2001,      &quot;Channel&quot;: 6    }  ]}</code></pre><strong>3. TCC-AF_CAM_USER_PASSWORD_POLICY CAM password policy</strong><br>Field    Type    Required    Default value    Valid values and description<br>MinimumLength    Integer    Yes    None    Minimum password length, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>MustContain    String    Yes    None    Characters that the password must contain, no fixed enumeration or valid character set specified; whether the value is valid is determined by the CAM password policy<br>ForcePasswordChange    Integer    Yes    None    Forced password change period, no fixed enumeration or unit specified; whether the value is valid is determined by the CAM password policy<br>ReusePasswordLimit    Integer    Yes    None    Password reuse limit, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>RetryPasswordLimit    Integer    Yes    None    Password retry limit, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>OnlyAdminCanResetPassword    Integer    Yes    None    Whether only administrators can reset passwords, no fixed enumeration specified; whether the value is valid is determined by the CAM password policy<br><pre><code>{  &quot;MinimumLength&quot;: 19,  &quot;MustContain&quot;: &quot;A&quot;,  &quot;ForcePasswordChange&quot;: 0,  &quot;ReusePasswordLimit&quot;: 2,  &quot;RetryPasswordLimit&quot;: 1,  &quot;OnlyAdminCanResetPassword&quot;: 0}</code></pre><strong>4. TCC-AF_CAM_USER_SECURITY CAM user security settings</strong><br>Field    Type    Required    Default value    Valid values and description<br>DefaultMFASettings    Object    Yes    None    Login and operation protection settings<br>DefaultMFASettings.LoginStrategy    Integer    Yes    None    1: enforce verification for all users; 2: depend on individual user settings<br>DefaultMFASettings.ActionStrategy    Integer    Yes    None    1: enforce verification for all users; 2: depend on individual user settings; this baseline item must be set to 2<br>DefaultMFASettings.LoginDetail    String array    Yes    None    Valid options: Stoken, Phone, Wechat, U2FToken, Mail; must include Stoken<br>LoginStatusSettings    Object    Yes    None    Session duration settings<br>LoginStatusSettings.SessionTimeout    Integer    No    None    Session timeout in seconds; no fixed upper/lower limit specified; whether the value is valid is determined by CAM<br>LoginStatusSettings.IdleSessionTimeout    Integer    No    None    Idle session timeout in seconds; no fixed upper/lower limit specified; whether the value is valid is determined by CAM<br><pre><code>{  &quot;DefaultMFASettings&quot;: {    &quot;LoginStrategy&quot;: 1,    &quot;ActionStrategy&quot;: 2,    &quot;LoginDetail&quot;: [&quot;Stoken&quot;, &quot;Phone&quot;]  },  &quot;LoginStatusSettings&quot;: {    &quot;SessionTimeout&quot;: 7200,    &quot;IdleSessionTimeout&quot;: 900  }}</code></pre><strong>5. TCC-AF_VPC_SUBNET VPC and subnet</strong><br>Field    Type    Required    Default value    Valid values and description<br>VpcName    String    Yes    None    VPC name, up to 60 bytes<br>CidrBlock    String    Yes    None    VPC CIDR block, only addresses within the three private network segments 10.0.0.0/12, 172.16.0.0/12, and 192.168.0.0/16 are supported<br>RegionName    String    Yes    None    Region, fill in according to "How to fill in regions, AZs, and dynamic values"; the region of this baseline item is specified by this field<br>Subnets    Object array    No    None    Subnet list; if not specified or empty, only the VPC is created, and no subnets are created<br>Subnets[].CidrBlock    String    Yes    None    Subnet CIDR block, must be within the range of CidrBlock, and subnet CIDR blocks within the same VPC cannot overlap<br>Subnets[].SubnetName    String    Yes    None    Subnet name, up to 60 bytes<br>Subnets[].Zone    String    Yes    None    AZ, in the format of ap-guangzhou-2; no fixed enumeration, query through DescribeZones<br><pre><code>{  &quot;VpcName&quot;: &quot;af-vpc&quot;,  &quot;CidrBlock&quot;: &quot;10.0.0.0/16&quot;,  &quot;RegionName&quot;: &quot;ap-guangzhou&quot;,  &quot;Subnets&quot;: [    {      &quot;CidrBlock&quot;: &quot;10.0.1.0/24&quot;,      &quot;SubnetName&quot;: &quot;af-subnet-1&quot;,      &quot;Zone&quot;: &quot;ap-guangzhou-2&quot;    }  ]}</code></pre><strong>6. TCC-AF_SECURITY_GROUP Security group</strong><br>Field    Type    Required    Default value    Valid values and description<br>GroupName    String    Yes    None    Security group name, up to 60 characters<br>GroupDescription    String    No    None    Security group description, up to 100 characters<br>Region    String    Yes    None    Region, fill in according to "How to fill in regions, AZs, and dynamic values"<br>SecurityGroupPolicySet    Object    Yes    None    Security group rule set<br>SecurityGroupPolicySet.Ingress    Object array    No    None    Inbound rule list<br>SecurityGroupPolicySet.Egress    Object array    No    None    Outbound rule list<br>Ingress[].Protocol, Egress[].Protocol    String    Yes    None    TCP, UDP, ICMP, ICMPv6, ALL<br>Ingress[].Port, Egress[].Port    String    Yes    None    all, a single port, or a port range (such as 80 or 80-90); must be set to all when Protocol is ALL<br>Ingress[].Action, Egress[].Action    String    Yes    None    ACCEPT: allow traffic; DROP: drop traffic<br>Ingress[].CidrBlock, Egress[].CidrBlock    String    No    None    IPv4 CIDR block or IP, such as 10.0.0.0/16 or 0.0.0.0/0; mutually exclusive with Ipv6CidrBlock<br>Ingress[].Ipv6CidrBlock, Egress[].Ipv6CidrBlock    String    No    None    Not supported yet, do not fill in<br>Ingress[].SecurityGroupId, Egress[].SecurityGroupId    String    No    None    Referenced security group ID, in the format of sg-ohuuioma; no fixed enumeration, query through the resource list<br>Ingress[].AddressTemplate.AddressId    String    No    None    IP address template ID, in the format of ipm-2uw6ujo6; when using an address template, this field and AddressGroupId must be filled in together<br>Ingress[].AddressTemplate.AddressGroupId    String    No    None    IP address group ID, in the format of ipmg-2uw6ujo6; when using an address template, this field and AddressId must be filled in together<br>Ingress[].PolicyDescription, Egress[].PolicyDescription    String    No    None    Rule description, no length limit specified; whether the value is valid is determined by the cloud product<br><pre><code>{  &quot;GroupName&quot;: &quot;af-sg&quot;,  &quot;GroupDescription&quot;: &quot;account factory baseline&quot;,  &quot;Region&quot;: &quot;ap-guangzhou&quot;,  &quot;SecurityGroupPolicySet&quot;: {    &quot;Ingress&quot;: [      {        &quot;Protocol&quot;: &quot;TCP&quot;,        &quot;Port&quot;: &quot;22&quot;,        &quot;CidrBlock&quot;: &quot;10.0.0.0/16&quot;,        &quot;Action&quot;: &quot;ACCEPT&quot;,        &quot;PolicyDescription&quot;: &quot;ssh&quot;      },      {        &quot;Protocol&quot;: &quot;TCP&quot;,        &quot;Port&quot;: &quot;443&quot;,        &quot;AddressTemplate&quot;: {          &quot;AddressId&quot;: &quot;ipm-2uw6ujo6&quot;,          &quot;AddressGroupId&quot;: &quot;ipmg-2uw6ujo6&quot;        },        &quot;Action&quot;: &quot;ACCEPT&quot;      }    ],    &quot;Egress&quot;: [      {        &quot;Protocol&quot;: &quot;ALL&quot;,        &quot;Port&quot;: &quot;all&quot;,        &quot;CidrBlock&quot;: &quot;0.0.0.0/0&quot;,        &quot;Action&quot;: &quot;ACCEPT&quot;,        &quot;PolicyDescription&quot;: &quot;allow all&quot;      }    ]  }}</code></pre><strong>7. TCC-AF_PRESET_TAG Preset tag</strong><br>Field    Type    Required    Default value    Valid values and description<br>TagValuePairs    Object array    Yes    None    Tag key-value pair list<br>TagValuePairs[].Key    String    Yes    None    Tag key, no fixed length or character restrictions specified; whether the value is valid is determined by the tag service<br>TagValuePairs[].Values    String array    Yes    None    List of tag values corresponding to the key; no fixed length or character restrictions specified; whether the value is valid is determined by the tag service<br>Constraint: the total number of entries in the array cannot exceed 30<br><pre><code>{  &quot;TagValuePairs&quot;: [    { &quot;Key&quot;: &quot;env&quot;, &quot;Values&quot;: [&quot;prod&quot;, &quot;dev&quot;] },    { &quot;Key&quot;: &quot;owner&quot;, &quot;Values&quot;: [&quot;ops&quot;] }  ]}</code></pre><strong>8. TCC-AF_SHARE_IMAGE Shared image</strong><br>Field    Type    Required    Default value    Valid values and description<br>Images    Object array    Yes    None    List of images to be shared, no upper limit specified<br>Images[].Region    String    Yes    None    Region where the image resides, fill in according to "How to fill in regions, AZs, and dynamic values"<br>Images[].ImageId    String    Yes    None    Image ID, in the format of img-gvbnzy6f; no fixed enumeration, query through DescribeImages or the console, the image must be in the available state<br><pre><code>{  &quot;Images&quot;: [    {      &quot;Region&quot;: &quot;ap-guangzhou&quot;,      &quot;ImageId&quot;: &quot;img-gvbnzy6f&quot;    }  ]}</code></pre></p>
        :type BaselineItems: list of AccountFactoryItem
        :param _Total: <p>Total number.</p>
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaselineItems = None
        self._Total = None
        self._RequestId = None

    @property
    def BaselineItems(self):
        r"""<p>Account Factory baseline list.<br><strong>1. TCC-AF_ACCOUNT_CONTACT Account contact</strong><br>This baseline item is used to create message recipients (contacts) under a member account.<br>Field    Type    Required    Default value    Valid values and description<br>AccountContacts    Object array    Yes    None    Contact list, up to 50 entries, cannot be empty<br>AccountContacts[].Name    String    Yes    None    Contact name, must be an existing name in the account; cannot be duplicated within the same list; no fixed format restrictions<br>AccountContacts[].CountryCode    String    Yes    None    Phone country code, such as 86; no fixed enumeration<br>AccountContacts[].PhoneNum    String    Yes    None    Phone number, must be verified before this baseline item can be applied; format is determined by the verification process, with no local format restrictions<br>AccountContacts[].Email    String    Yes    None    Email address, must be verified before this baseline item can be applied; format is determined by the verification process, with no local format restrictions<br>AccountContacts[].Remark    String    No    None    Remarks, no length limit specified<br><pre><code>{  &quot;AccountContacts&quot;: [    {      &quot;Name&quot;: &quot;ops-admin&quot;,      &quot;CountryCode&quot;: &quot;86&quot;,      &quot;PhoneNum&quot;: &quot;13800***000&quot;,      &quot;Email&quot;: &quot;ops@ex***le.com&quot;,      &quot;Remark&quot;: &quot;Ops contact&quot;    }  ]}</code></pre><strong>2. TCC-AF_ACCOUNT_NOTIFICATION Message recipient</strong><br>China site:<br>Field    Type    Required    Default value    Valid values and description<br>Subscriptions    Object array    Yes    None    Subscription list, recommended not to exceed 50 entries; if exceeded, process in batches, will not be rejected due to the number of entries<br>Subscriptions[].Name    String    Yes    None    Single sub-user name; enter an existing sub-user name, otherwise the subscription does not take effect<br>Subscriptions[].ProductId    Integer    Yes    None    Product ID, no fixed enumeration, query through DescribeProductIds<br>Subscriptions[].MsgType    Integer    Yes    None    Message type ID, no fixed enumeration, query through DescribeFirstSiteMsgType and DescribeSecondMsgType<br>Subscriptions[].Channel    Integer    Yes    None    Message delivery channel, bitmask, see the table below for values<br>Subscriptions[].Status    String    Yes    None    Only Open or Close; only Open creates a subscription, Close or other values do not take effect</p><p>Channel bitmask:<br>Channel    Value<br>Inbox message    1<br>Email    2<br>SMS    4<br>WeChat    8 (not available on the international site)<br>Voice    16<br>WeCom    32 (not available on the international site)</p><p>Channel combination    Value<br>Inbox message + Email    3<br>Inbox message + SMS    5<br>Email + SMS    6<br>Inbox message + Email + SMS    7</p><p>International site fields:<br>Field    Type    Required    Default value    Valid values and description<br>Subscriptions    Object array    Yes    None    Subscription list, recommended not to exceed 50 entries; if exceeded, process in batches, will not be rejected due to the number of entries<br>Subscriptions[].Name    String array    Yes    None    Sub-user name list; enter existing sub-user names, names will be deduplicated<br>Subscriptions[].MsgType    Integer    Yes    None    Message type ID, no fixed enumeration, query through DescribeFirstSiteMsgType and DescribeSecondMsgType<br>Subscriptions[].Channel    Integer    Yes    None    Message delivery channel, bitmask, values same as the table above</p><p>China site example:<br><pre><code>{  &quot;Subscriptions&quot;: [    {      &quot;Name&quot;: &quot;ops-admin&quot;,      &quot;ProductId&quot;: 1001,      &quot;MsgType&quot;: 2001,      &quot;Channel&quot;: 3,      &quot;Status&quot;: &quot;Open&quot;    }  ]}</code></pre>International site example:<br><pre><code>{  &quot;Subscriptions&quot;: [    {      &quot;Name&quot;: [&quot;ops-admin&quot;, &quot;audit&quot;],      &quot;MsgType&quot;: 2001,      &quot;Channel&quot;: 6    }  ]}</code></pre><strong>3. TCC-AF_CAM_USER_PASSWORD_POLICY CAM password policy</strong><br>Field    Type    Required    Default value    Valid values and description<br>MinimumLength    Integer    Yes    None    Minimum password length, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>MustContain    String    Yes    None    Characters that the password must contain, no fixed enumeration or valid character set specified; whether the value is valid is determined by the CAM password policy<br>ForcePasswordChange    Integer    Yes    None    Forced password change period, no fixed enumeration or unit specified; whether the value is valid is determined by the CAM password policy<br>ReusePasswordLimit    Integer    Yes    None    Password reuse limit, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>RetryPasswordLimit    Integer    Yes    None    Password retry limit, no fixed enumeration or upper/lower limit specified; whether the value is valid is determined by the CAM password policy<br>OnlyAdminCanResetPassword    Integer    Yes    None    Whether only administrators can reset passwords, no fixed enumeration specified; whether the value is valid is determined by the CAM password policy<br><pre><code>{  &quot;MinimumLength&quot;: 19,  &quot;MustContain&quot;: &quot;A&quot;,  &quot;ForcePasswordChange&quot;: 0,  &quot;ReusePasswordLimit&quot;: 2,  &quot;RetryPasswordLimit&quot;: 1,  &quot;OnlyAdminCanResetPassword&quot;: 0}</code></pre><strong>4. TCC-AF_CAM_USER_SECURITY CAM user security settings</strong><br>Field    Type    Required    Default value    Valid values and description<br>DefaultMFASettings    Object    Yes    None    Login and operation protection settings<br>DefaultMFASettings.LoginStrategy    Integer    Yes    None    1: enforce verification for all users; 2: depend on individual user settings<br>DefaultMFASettings.ActionStrategy    Integer    Yes    None    1: enforce verification for all users; 2: depend on individual user settings; this baseline item must be set to 2<br>DefaultMFASettings.LoginDetail    String array    Yes    None    Valid options: Stoken, Phone, Wechat, U2FToken, Mail; must include Stoken<br>LoginStatusSettings    Object    Yes    None    Session duration settings<br>LoginStatusSettings.SessionTimeout    Integer    No    None    Session timeout in seconds; no fixed upper/lower limit specified; whether the value is valid is determined by CAM<br>LoginStatusSettings.IdleSessionTimeout    Integer    No    None    Idle session timeout in seconds; no fixed upper/lower limit specified; whether the value is valid is determined by CAM<br><pre><code>{  &quot;DefaultMFASettings&quot;: {    &quot;LoginStrategy&quot;: 1,    &quot;ActionStrategy&quot;: 2,    &quot;LoginDetail&quot;: [&quot;Stoken&quot;, &quot;Phone&quot;]  },  &quot;LoginStatusSettings&quot;: {    &quot;SessionTimeout&quot;: 7200,    &quot;IdleSessionTimeout&quot;: 900  }}</code></pre><strong>5. TCC-AF_VPC_SUBNET VPC and subnet</strong><br>Field    Type    Required    Default value    Valid values and description<br>VpcName    String    Yes    None    VPC name, up to 60 bytes<br>CidrBlock    String    Yes    None    VPC CIDR block, only addresses within the three private network segments 10.0.0.0/12, 172.16.0.0/12, and 192.168.0.0/16 are supported<br>RegionName    String    Yes    None    Region, fill in according to "How to fill in regions, AZs, and dynamic values"; the region of this baseline item is specified by this field<br>Subnets    Object array    No    None    Subnet list; if not specified or empty, only the VPC is created, and no subnets are created<br>Subnets[].CidrBlock    String    Yes    None    Subnet CIDR block, must be within the range of CidrBlock, and subnet CIDR blocks within the same VPC cannot overlap<br>Subnets[].SubnetName    String    Yes    None    Subnet name, up to 60 bytes<br>Subnets[].Zone    String    Yes    None    AZ, in the format of ap-guangzhou-2; no fixed enumeration, query through DescribeZones<br><pre><code>{  &quot;VpcName&quot;: &quot;af-vpc&quot;,  &quot;CidrBlock&quot;: &quot;10.0.0.0/16&quot;,  &quot;RegionName&quot;: &quot;ap-guangzhou&quot;,  &quot;Subnets&quot;: [    {      &quot;CidrBlock&quot;: &quot;10.0.1.0/24&quot;,      &quot;SubnetName&quot;: &quot;af-subnet-1&quot;,      &quot;Zone&quot;: &quot;ap-guangzhou-2&quot;    }  ]}</code></pre><strong>6. TCC-AF_SECURITY_GROUP Security group</strong><br>Field    Type    Required    Default value    Valid values and description<br>GroupName    String    Yes    None    Security group name, up to 60 characters<br>GroupDescription    String    No    None    Security group description, up to 100 characters<br>Region    String    Yes    None    Region, fill in according to "How to fill in regions, AZs, and dynamic values"<br>SecurityGroupPolicySet    Object    Yes    None    Security group rule set<br>SecurityGroupPolicySet.Ingress    Object array    No    None    Inbound rule list<br>SecurityGroupPolicySet.Egress    Object array    No    None    Outbound rule list<br>Ingress[].Protocol, Egress[].Protocol    String    Yes    None    TCP, UDP, ICMP, ICMPv6, ALL<br>Ingress[].Port, Egress[].Port    String    Yes    None    all, a single port, or a port range (such as 80 or 80-90); must be set to all when Protocol is ALL<br>Ingress[].Action, Egress[].Action    String    Yes    None    ACCEPT: allow traffic; DROP: drop traffic<br>Ingress[].CidrBlock, Egress[].CidrBlock    String    No    None    IPv4 CIDR block or IP, such as 10.0.0.0/16 or 0.0.0.0/0; mutually exclusive with Ipv6CidrBlock<br>Ingress[].Ipv6CidrBlock, Egress[].Ipv6CidrBlock    String    No    None    Not supported yet, do not fill in<br>Ingress[].SecurityGroupId, Egress[].SecurityGroupId    String    No    None    Referenced security group ID, in the format of sg-ohuuioma; no fixed enumeration, query through the resource list<br>Ingress[].AddressTemplate.AddressId    String    No    None    IP address template ID, in the format of ipm-2uw6ujo6; when using an address template, this field and AddressGroupId must be filled in together<br>Ingress[].AddressTemplate.AddressGroupId    String    No    None    IP address group ID, in the format of ipmg-2uw6ujo6; when using an address template, this field and AddressId must be filled in together<br>Ingress[].PolicyDescription, Egress[].PolicyDescription    String    No    None    Rule description, no length limit specified; whether the value is valid is determined by the cloud product<br><pre><code>{  &quot;GroupName&quot;: &quot;af-sg&quot;,  &quot;GroupDescription&quot;: &quot;account factory baseline&quot;,  &quot;Region&quot;: &quot;ap-guangzhou&quot;,  &quot;SecurityGroupPolicySet&quot;: {    &quot;Ingress&quot;: [      {        &quot;Protocol&quot;: &quot;TCP&quot;,        &quot;Port&quot;: &quot;22&quot;,        &quot;CidrBlock&quot;: &quot;10.0.0.0/16&quot;,        &quot;Action&quot;: &quot;ACCEPT&quot;,        &quot;PolicyDescription&quot;: &quot;ssh&quot;      },      {        &quot;Protocol&quot;: &quot;TCP&quot;,        &quot;Port&quot;: &quot;443&quot;,        &quot;AddressTemplate&quot;: {          &quot;AddressId&quot;: &quot;ipm-2uw6ujo6&quot;,          &quot;AddressGroupId&quot;: &quot;ipmg-2uw6ujo6&quot;        },        &quot;Action&quot;: &quot;ACCEPT&quot;      }    ],    &quot;Egress&quot;: [      {        &quot;Protocol&quot;: &quot;ALL&quot;,        &quot;Port&quot;: &quot;all&quot;,        &quot;CidrBlock&quot;: &quot;0.0.0.0/0&quot;,        &quot;Action&quot;: &quot;ACCEPT&quot;,        &quot;PolicyDescription&quot;: &quot;allow all&quot;      }    ]  }}</code></pre><strong>7. TCC-AF_PRESET_TAG Preset tag</strong><br>Field    Type    Required    Default value    Valid values and description<br>TagValuePairs    Object array    Yes    None    Tag key-value pair list<br>TagValuePairs[].Key    String    Yes    None    Tag key, no fixed length or character restrictions specified; whether the value is valid is determined by the tag service<br>TagValuePairs[].Values    String array    Yes    None    List of tag values corresponding to the key; no fixed length or character restrictions specified; whether the value is valid is determined by the tag service<br>Constraint: the total number of entries in the array cannot exceed 30<br><pre><code>{  &quot;TagValuePairs&quot;: [    { &quot;Key&quot;: &quot;env&quot;, &quot;Values&quot;: [&quot;prod&quot;, &quot;dev&quot;] },    { &quot;Key&quot;: &quot;owner&quot;, &quot;Values&quot;: [&quot;ops&quot;] }  ]}</code></pre><strong>8. TCC-AF_SHARE_IMAGE Shared image</strong><br>Field    Type    Required    Default value    Valid values and description<br>Images    Object array    Yes    None    List of images to be shared, no upper limit specified<br>Images[].Region    String    Yes    None    Region where the image resides, fill in according to "How to fill in regions, AZs, and dynamic values"<br>Images[].ImageId    String    Yes    None    Image ID, in the format of img-gvbnzy6f; no fixed enumeration, query through DescribeImages or the console, the image must be in the available state<br><pre><code>{  &quot;Images&quot;: [    {      &quot;Region&quot;: &quot;ap-guangzhou&quot;,      &quot;ImageId&quot;: &quot;img-gvbnzy6f&quot;    }  ]}</code></pre></p>
        :rtype: list of AccountFactoryItem
        """
        return self._BaselineItems

    @BaselineItems.setter
    def BaselineItems(self, BaselineItems):
        self._BaselineItems = BaselineItems

    @property
    def Total(self):
        r"""<p>Total number.</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("BaselineItems") is not None:
            self._BaselineItems = []
            for item in params.get("BaselineItems"):
                obj = AccountFactoryItem()
                obj._deserialize(item)
                self._BaselineItems.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class ListDeployStepTasksRequest(AbstractModel):
    r"""ListDeployStepTasks request structure.

    """

    def __init__(self):
        r"""
        :param _Identifier: Specifies the unique identifier for the feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        :param _Limit: Maximum number of returned records. value ranges from 0 to 200.
        :type Limit: int
        :param _Offset: Offset. valid values are equal to or greater than 0.
        :type Offset: int
        """
        self._Identifier = None
        self._Limit = None
        self._Offset = None

    @property
    def Identifier(self):
        r"""Specifies the unique identifier for the feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Limit(self):
        r"""Maximum number of returned records. value ranges from 0 to 200.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. valid values are equal to or greater than 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeployStepTasksResponse(AbstractModel):
    r"""ListDeployStepTasks response structure.

    """

    def __init__(self):
        r"""
        :param _BaselineDeployStepTaskList: Account factory baseline function application information list.
        :type BaselineDeployStepTaskList: list of BaselineStepTaskInfo
        :param _Total: Total quantity.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaselineDeployStepTaskList = None
        self._Total = None
        self._RequestId = None

    @property
    def BaselineDeployStepTaskList(self):
        r"""Account factory baseline function application information list.
        :rtype: list of BaselineStepTaskInfo
        """
        return self._BaselineDeployStepTaskList

    @BaselineDeployStepTaskList.setter
    def BaselineDeployStepTaskList(self, BaselineDeployStepTaskList):
        self._BaselineDeployStepTaskList = BaselineDeployStepTaskList

    @property
    def Total(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("BaselineDeployStepTaskList") is not None:
            self._BaselineDeployStepTaskList = []
            for item in params.get("BaselineDeployStepTaskList"):
                obj = BaselineStepTaskInfo()
                obj._deserialize(item)
                self._BaselineDeployStepTaskList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class UpdateAccountFactoryBaselineRequest(AbstractModel):
    r"""UpdateAccountFactoryBaseline request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Specifies the baseline name, which must be unique and can only contain a combination of english letters, digits, chinese characters, and symbols @, &_[]-, with a length of 1-25 chinese or english characters.
        :type Name: str
        :param _BaselineConfigItems: Baseline configuration. overwrite update. can be accessed through controlcenter:GetAccountFactoryBaseline to query existing baseline configuration. can be accessed through controlcenter:ListAccountFactoryBaselineItems to query supported baseline list.
        :type BaselineConfigItems: list of BaselineConfigItem
        """
        self._Name = None
        self._BaselineConfigItems = None

    @property
    def Name(self):
        r"""Specifies the baseline name, which must be unique and can only contain a combination of english letters, digits, chinese characters, and symbols @, &_[]-, with a length of 1-25 chinese or english characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaselineConfigItems(self):
        r"""Baseline configuration. overwrite update. can be accessed through controlcenter:GetAccountFactoryBaseline to query existing baseline configuration. can be accessed through controlcenter:ListAccountFactoryBaselineItems to query supported baseline list.
        :rtype: list of BaselineConfigItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineConfigItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccountFactoryBaselineResponse(AbstractModel):
    r"""UpdateAccountFactoryBaseline response structure.

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