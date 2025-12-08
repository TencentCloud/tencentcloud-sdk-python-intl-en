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
    r"""Account factory baseline item.

    """

    def __init__(self):
        r"""
        :param _Identifier: Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        :param _Name: Baseline item name. specifies a unique name for the feature item. supports a combination of english letters, numbers, chinese characters, and symbols @, &, _, [, ], -. valid values: 1-25 chinese or english characters.
        :type Name: str
        :param _NameEn: Baseline item english name. specifies a unique name for the baseline item. supports a combination of english letters, digits, spaces, and symbols @, &, _, [], -. valid values: 1-64 english characters.
        :type NameEn: str
        :param _Weight: Baseline item weight. the smaller the value, the higher the weight. value range equal to or greater than 0.
        :type Weight: int
        :param _Required: Specifies whether the baseline item is required (1: required; 0: optional).
        :type Required: int
        :param _DependsOn: Baseline item dependency. value range of N depends on the count of other baseline items it relies on.
        :type DependsOn: list of DependsOnItem
        :param _Description: Baseline description, with a length of 2 to 256 english or chinese characters. it is empty by default.
        :type Description: str
        :param _DescriptionEn: Baseline item english description, with a length of 2 to 1024 english characters. it is empty by default.
        :type DescriptionEn: str
        :param _Classify: Baseline classification. length: 2-32 english or chinese characters. values cannot be empty.
        :type Classify: str
        :param _ClassifyEn: Baseline english classification, with a length of 2-64 english characters. cannot be empty.
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
        r"""Specifies the unique identifier for account factory baseline item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Name(self):
        r"""Baseline item name. specifies a unique name for the feature item. supports a combination of english letters, numbers, chinese characters, and symbols @, &, _, [, ], -. valid values: 1-25 chinese or english characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NameEn(self):
        r"""Baseline item english name. specifies a unique name for the baseline item. supports a combination of english letters, digits, spaces, and symbols @, &, _, [], -. valid values: 1-64 english characters.
        :rtype: str
        """
        return self._NameEn

    @NameEn.setter
    def NameEn(self, NameEn):
        self._NameEn = NameEn

    @property
    def Weight(self):
        r"""Baseline item weight. the smaller the value, the higher the weight. value range equal to or greater than 0.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Required(self):
        r"""Specifies whether the baseline item is required (1: required; 0: optional).
        :rtype: int
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DependsOn(self):
        r"""Baseline item dependency. value range of N depends on the count of other baseline items it relies on.
        :rtype: list of DependsOnItem
        """
        return self._DependsOn

    @DependsOn.setter
    def DependsOn(self, DependsOn):
        self._DependsOn = DependsOn

    @property
    def Description(self):
        r"""Baseline description, with a length of 2 to 256 english or chinese characters. it is empty by default.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptionEn(self):
        r"""Baseline item english description, with a length of 2 to 1024 english characters. it is empty by default.
        :rtype: str
        """
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn

    @property
    def Classify(self):
        r"""Baseline classification. length: 2-32 english or chinese characters. values cannot be empty.
        :rtype: str
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify

    @property
    def ClassifyEn(self):
        r"""Baseline english classification, with a length of 2-64 english characters. cannot be empty.
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
    r"""Dependency.

    """

    def __init__(self):
        r"""
        :param _Type: Dependency type. valid values: LandingZoneSetUp or AccountFactorySetUp. LandingZoneSetUp refers to the dependency of landingZone. AccountFactorySetUp refers to the dependency of account factory.
        :type Type: str
        :param _Identifier: Specifies the unique identifier for the feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
        :type Identifier: str
        """
        self._Type = None
        self._Identifier = None

    @property
    def Type(self):
        r"""Dependency type. valid values: LandingZoneSetUp or AccountFactorySetUp. LandingZoneSetUp refers to the dependency of landingZone. AccountFactorySetUp refers to the dependency of account factory.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Identifier(self):
        r"""Specifies the unique identifier for the feature item, can only contain english letters, digits, and @, ,._[]-:()()[]+=., with a length of 2-128 characters.
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
        :param _Limit: Maximum number of returned records. value ranges from 0 to 200.
        :type Limit: int
        :param _Offset: Offset. valid values are equal to or greater than 0.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

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
        :param _BaselineItems: Account factory baseline list.
        :type BaselineItems: list of AccountFactoryItem
        :param _Total: Total quantity.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaselineItems = None
        self._Total = None
        self._RequestId = None

    @property
    def BaselineItems(self):
        r"""Account factory baseline list.
        :rtype: list of AccountFactoryItem
        """
        return self._BaselineItems

    @BaselineItems.setter
    def BaselineItems(self, BaselineItems):
        self._BaselineItems = BaselineItems

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