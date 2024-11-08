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


class Account(AbstractModel):
    """Account list information.

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID.
        :type Id: int
        :param _Uuid: CWP agent `Uuid`
        :type Uuid: str
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _Username: Account name.
        :type Username: str
        :param _Groups: Account group.
        :type Groups: str
        :param _Privilege: Account type.
<li>ORDINARY: ordinary account</li>
<li>SUPPER: super admin account</li>
        :type Privilege: str
        :param _AccountCreateTime: Account creation time.
        :type AccountCreateTime: str
        :param _LastLoginTime: Account last login time.
        :type LastLoginTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Username = None
        self._Groups = None
        self._Privilege = None
        self._AccountCreateTime = None
        self._LastLoginTime = None

    @property
    def Id(self):
        """Unique ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `Uuid`
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Username(self):
        """Account name.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Groups(self):
        """Account group.
        :rtype: str
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Privilege(self):
        """Account type.
<li>ORDINARY: ordinary account</li>
<li>SUPPER: super admin account</li>
        :rtype: str
        """
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def AccountCreateTime(self):
        """Account creation time.
        :rtype: str
        """
        return self._AccountCreateTime

    @AccountCreateTime.setter
    def AccountCreateTime(self, AccountCreateTime):
        self._AccountCreateTime = AccountCreateTime

    @property
    def LastLoginTime(self):
        """Account last login time.
        :rtype: str
        """
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Username = params.get("Username")
        self._Groups = params.get("Groups")
        self._Privilege = params.get("Privilege")
        self._AccountCreateTime = params.get("AccountCreateTime")
        self._LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountStatistics(AbstractModel):
    """Account statistics.

    """

    def __init__(self):
        r"""
        :param _Username: Username.
        :type Username: str
        :param _MachineNum: Number of servers.
        :type MachineNum: int
        """
        self._Username = None
        self._MachineNum = None

    @property
    def Username(self):
        """Username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def MachineNum(self):
        """Number of servers.
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListRequest(AbstractModel):
    """AddLoginWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Whitelist rule
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self._Rules = None

    @property
    def Rules(self):
        """Whitelist rule
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = LoginWhiteListsRule()
            self._Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListResponse(AbstractModel):
    """AddLoginWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AddMachineTagRequest(AbstractModel):
    """AddMachineTag request structure.

    """

    def __init__(self):
        r"""
        :param _Quuid: Server ID
        :type Quuid: str
        :param _TagId: Tag ID
        :type TagId: int
        :param _MRegion: Server region
        :type MRegion: str
        :param _MArea: Server type (`CVM` or `BM`)
        :type MArea: str
        """
        self._Quuid = None
        self._TagId = None
        self._MRegion = None
        self._MArea = None

    @property
    def Quuid(self):
        """Server ID
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def TagId(self):
        """Tag ID
        :rtype: int
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def MRegion(self):
        """Server region
        :rtype: str
        """
        return self._MRegion

    @MRegion.setter
    def MRegion(self, MRegion):
        self._MRegion = MRegion

    @property
    def MArea(self):
        """Server type (`CVM` or `BM`)
        :rtype: str
        """
        return self._MArea

    @MArea.setter
    def MArea(self, MArea):
        self._MArea = MArea


    def _deserialize(self, params):
        self._Quuid = params.get("Quuid")
        self._TagId = params.get("TagId")
        self._MRegion = params.get("MRegion")
        self._MArea = params.get("MArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineTagResponse(AbstractModel):
    """AddMachineTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AgentVul(AbstractModel):
    """Server vulnerability information

    """

    def __init__(self):
        r"""
        :param _Id: Vulnerability ID.
        :type Id: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _VulName: Vulnerability name.
        :type VulName: str
        :param _VulLevel: Vulnerability severity level.
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
<li>NOTICE: notice</li>
        :type VulLevel: str
        :param _LastScanTime: Last scanned time.
        :type LastScanTime: str
        :param _Description: Vulnerability description.
        :type Description: str
        :param _VulId: Vulnerability category ID.
        :type VulId: int
        :param _VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>FIXED: fixed</li>
        :type VulStatus: str
        """
        self._Id = None
        self._MachineIp = None
        self._VulName = None
        self._VulLevel = None
        self._LastScanTime = None
        self._Description = None
        self._VulId = None
        self._VulStatus = None

    @property
    def Id(self):
        """Vulnerability ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def VulName(self):
        """Vulnerability name.
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        """Vulnerability severity level.
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
<li>NOTICE: notice</li>
        :rtype: str
        """
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def LastScanTime(self):
        """Last scanned time.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Description(self):
        """Vulnerability description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulId(self):
        """Vulnerability category ID.
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulStatus(self):
        """Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>FIXED: fixed</li>
        :rtype: str
        """
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._Description = params.get("Description")
        self._VulId = params.get("VulId")
        self._VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttack(AbstractModel):
    """Brute force attack list

    """

    def __init__(self):
        r"""
        :param _Id: Event ID.
        :type Id: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _Status: Brute force attack event status
<li>BRUTEATTACK_FAIL_ACCOUNT: brute force attack event - failure (the account exists)</li>
<li>BRUTEATTACK_FAIL_NOACCOUNT: brute force attack event - failure (the account does not exist)</li>
<li>BRUTEATTACK_SUCCESS: brute force attack event - success </li>
        :type Status: str
        :param _UserName: Username.
        :type UserName: str
        :param _City: City ID.
        :type City: int
        :param _Country: Country/Region ID.
        :type Country: int
        :param _Province: Province/State ID.
        :type Province: int
        :param _SrcIp: Source IP.
        :type SrcIp: str
        :param _Count: Number of attempts.
        :type Count: int
        :param _CreateTime: Occurrence time.
        :type CreateTime: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _IsProVersion: Whether the server enables CWP Pro.
        :type IsProVersion: bool
        :param _BanStatus: Whether the server is banned.
        :type BanStatus: str
        :param _Quuid: Server `UUID`
        :type Quuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._UserName = None
        self._City = None
        self._Country = None
        self._Province = None
        self._SrcIp = None
        self._Count = None
        self._CreateTime = None
        self._MachineName = None
        self._Uuid = None
        self._IsProVersion = None
        self._BanStatus = None
        self._Quuid = None

    @property
    def Id(self):
        """Event ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        """Brute force attack event status
<li>BRUTEATTACK_FAIL_ACCOUNT: brute force attack event - failure (the account exists)</li>
<li>BRUTEATTACK_FAIL_NOACCOUNT: brute force attack event - failure (the account does not exist)</li>
<li>BRUTEATTACK_SUCCESS: brute force attack event - success </li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        """Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def City(self):
        """City ID.
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """Country/Region ID.
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province/State ID.
        :rtype: int
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def SrcIp(self):
        """Source IP.
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Count(self):
        """Number of attempts.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CreateTime(self):
        """Occurrence time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def IsProVersion(self):
        """Whether the server enables CWP Pro.
        :rtype: bool
        """
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def BanStatus(self):
        """Whether the server is banned.
        :rtype: str
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def Quuid(self):
        """Server `UUID`
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._SrcIp = params.get("SrcIp")
        self._Count = params.get("Count")
        self._CreateTime = params.get("CreateTime")
        self._MachineName = params.get("MachineName")
        self._Uuid = params.get("Uuid")
        self._IsProVersion = params.get("IsProVersion")
        self._BanStatus = params.get("BanStatus")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion request structure.

    """

    def __init__(self):
        r"""
        :param _Quuid: Server `Uuid`.
`InstanceId` for BM or `Uuid` for CVM
        :type Quuid: str
        """
        self._Quuid = None

    @property
    def Quuid(self):
        """Server `Uuid`.
`InstanceId` for BM or `Uuid` for CVM
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Component(AbstractModel):
    """Component list data.

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID.
        :type Id: int
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _ComponentVersion: Component version number.
        :type ComponentVersion: str
        :param _ComponentType: Component type.
<li>SYSTEM: system component</li>
<li>WEB: web component</li>
        :type ComponentType: str
        :param _ComponentName: Component name.
        :type ComponentName: str
        :param _ModifyTime: Component detection update time.
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._ComponentVersion = None
        self._ComponentType = None
        self._ComponentName = None
        self._ModifyTime = None

    @property
    def Id(self):
        """Unique ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def ComponentVersion(self):
        """Component version number.
        :rtype: str
        """
        return self._ComponentVersion

    @ComponentVersion.setter
    def ComponentVersion(self, ComponentVersion):
        self._ComponentVersion = ComponentVersion

    @property
    def ComponentType(self):
        """Component type.
<li>SYSTEM: system component</li>
<li>WEB: web component</li>
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        """Component name.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ModifyTime(self):
        """Component detection update time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._ComponentVersion = params.get("ComponentVersion")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentStatistics(AbstractModel):
    """Component statistics.

    """

    def __init__(self):
        r"""
        :param _Id: Component ID.
        :type Id: int
        :param _MachineNum: Number of servers.
        :type MachineNum: int
        :param _ComponentName: Component name.
        :type ComponentName: str
        :param _ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :type ComponentType: str
        :param _Description: Component description.
        :type Description: str
        """
        self._Id = None
        self._MachineNum = None
        self._ComponentName = None
        self._ComponentType = None
        self._Description = None

    @property
    def Id(self):
        """Component ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineNum(self):
        """Number of servers.
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum

    @property
    def ComponentName(self):
        """Component name.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentType(self):
        """Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def Description(self):
        """Component description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineNum = params.get("MachineNum")
        self._ComponentName = params.get("ComponentName")
        self._ComponentType = params.get("ComponentType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenPortTaskRequest(AbstractModel):
    """CreateOpenPortTask request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenPortTaskResponse(AbstractModel):
    """CreateOpenPortTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Uuids: CWP agent `UUID` array.
        :type Uuids: list of str
        :param _Places: Login region information array.
        :type Places: list of Place
        """
        self._Uuids = None
        self._Places = None

    @property
    def Uuids(self):
        """CWP agent `UUID` array.
        :rtype: list of str
        """
        return self._Uuids

    @Uuids.setter
    def Uuids(self, Uuids):
        self._Uuids = Uuids

    @property
    def Places(self):
        """Login region information array.
        :rtype: list of Place
        """
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places


    def _deserialize(self, params):
        self._Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Brute force attack event ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Brute force attack event ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Whitelist ID
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Whitelist ID
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag request structure.

    """

    def __init__(self):
        r"""
        :param _Rid: Associated tag ID
        :type Rid: int
        """
        self._Rid = None

    @property
    def Rid(self):
        """Associated tag ID
        :rtype: int
        """
        return self._Rid

    @Rid.setter
    def Rid(self, Rid):
        self._Rid = Rid


    def _deserialize(self, params):
        self._Rid = params.get("Rid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Malicious request record ID array. Maximum value: 100 entries.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Malicious request record ID array. Maximum value: 100 entries.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Trojan record ID array
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Trojan record ID array
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Unusual login location event ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Unusual login location event ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`
        :type Uuid: str
        :param _CityIds: Added usual login city ID array
        :type CityIds: list of int non-negative
        """
        self._Uuid = None
        self._CityIds = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def CityIds(self):
        """Added usual login city ID array
        :rtype: list of int non-negative
        """
        return self._CityIds

    @CityIds.setter
    def CityIds(self, CityIds):
        self._CityIds = CityIds


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._CityIds = params.get("CityIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Username - String - Required: No - Account username</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Username - String - Required: No - Account username</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in account statistics list.
        :type TotalCount: int
        :param _AccountStatistics: Account statistics list.
        :type AccountStatistics: list of AccountStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in account statistics list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountStatistics(self):
        """Account statistics list.
        :rtype: list of AccountStatistics
        """
        return self._AccountStatistics

    @AccountStatistics.setter
    def AccountStatistics(self, AccountStatistics):
        self._AccountStatistics = AccountStatistics

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self._AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self._AccountStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param _Username: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Username` is specified, it indicates to query the information list under the specified username.
        :type Username: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Username - String - Required: No - Account name</li>
<li>Privilege - String - Required: No - Account name (ORDINARY: ordinary account, SUPPER: super admin account)</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Username = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Username(self):
        """CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Username` is specified, it indicates to query the information list under the specified username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Username - String - Required: No - Account name</li>
<li>Privilege - String - Required: No - Account name (ORDINARY: ordinary account, SUPPER: super admin account)</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Username = params.get("Username")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in account list.
        :type TotalCount: int
        :param _Accounts: Account data list.
        :type Accounts: list of Account
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in account list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        """Account data list.
        :rtype: list of Account
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls request structure.

    """

    def __init__(self):
        r"""
        :param _VulType: Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>
        :type VulType: str
        :param _Uuid: Agent `UUID`.
        :type Uuid: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)
        :type Filters: list of Filter
        """
        self._VulType = None
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulType(self):
        """Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>
        :rtype: str
        """
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Uuid(self):
        """Agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulType = params.get("VulType")
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _AgentVuls: Server vulnerability information
        :type AgentVuls: list of AgentVul
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentVuls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentVuls(self):
        """Server vulnerability information
        :rtype: list of AgentVul
        """
        return self._AgentVuls

    @AgentVuls.setter
    def AgentVuls(self, AgentVuls):
        self._AgentVuls = AgentVuls

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self._AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self._AgentVuls.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute request structure.

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _Offline: CWP deactivation alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type Offline: str
        :param _Malware: Trojan discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type Malware: str
        :param _NonlocalLogin: Unusual login location discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type NonlocalLogin: str
        :param _CrackSuccess: Brute force attack success alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type CrackSuccess: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Offline = None
        self._Malware = None
        self._NonlocalLogin = None
        self._CrackSuccess = None
        self._RequestId = None

    @property
    def Offline(self):
        """CWP deactivation alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :rtype: str
        """
        return self._Offline

    @Offline.setter
    def Offline(self, Offline):
        self._Offline = Offline

    @property
    def Malware(self):
        """Trojan discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :rtype: str
        """
        return self._Malware

    @Malware.setter
    def Malware(self, Malware):
        self._Malware = Malware

    @property
    def NonlocalLogin(self):
        """Unusual login location discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :rtype: str
        """
        return self._NonlocalLogin

    @NonlocalLogin.setter
    def NonlocalLogin(self, NonlocalLogin):
        self._NonlocalLogin = NonlocalLogin

    @property
    def CrackSuccess(self):
        """Brute force attack success alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :rtype: str
        """
        return self._CrackSuccess

    @CrackSuccess.setter
    def CrackSuccess(self, CrackSuccess):
        self._CrackSuccess = CrackSuccess

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offline = params.get("Offline")
        self._Malware = params.get("Malware")
        self._NonlocalLogin = params.get("NonlocalLogin")
        self._CrackSuccess = params.get("CrackSuccess")
        self._RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: Agent `Uuid`.
        :type Uuid: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Query status (FAILED: brute force attack failed, SUCCESS: brute force attack succeeded)</li>
        :type Filters: list of Filter
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        """
        self._Uuid = None
        self._Offset = None
        self._Filters = None
        self._Limit = None

    @property
    def Uuid(self):
        """Agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Query status (FAILED: brute force attack failed, SUCCESS: brute force attack succeeded)</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of events
        :type TotalCount: int
        :param _BruteAttacks: Brute force attack event list
        :type BruteAttacks: list of BruteAttack
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BruteAttacks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of events
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BruteAttacks(self):
        """Brute force attack event list
        :rtype: list of BruteAttack
        """
        return self._BruteAttacks

    @BruteAttacks.setter
    def BruteAttacks(self, BruteAttacks):
        self._BruteAttacks = BruteAttacks

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self._BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self._BruteAttacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ComponentId: Component ID.
        :type ComponentId: int
        """
        self._ComponentId = None

    @property
    def ComponentId(self):
        """Component ID.
        :rtype: int
        """
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Component ID.
        :type Id: int
        :param _ComponentName: Component name.
        :type ComponentName: str
        :param _ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :type ComponentType: str
        :param _Homepage: Component's official website.
        :type Homepage: str
        :param _Description: Component description.
        :type Description: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._ComponentName = None
        self._ComponentType = None
        self._Homepage = None
        self._Description = None
        self._RequestId = None

    @property
    def Id(self):
        """Component ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ComponentName(self):
        """Component name.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentType(self):
        """Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def Homepage(self):
        """Component's official website.
        :rtype: str
        """
        return self._Homepage

    @Homepage.setter
    def Homepage(self, Homepage):
        self._Homepage = Homepage

    @property
    def Description(self):
        """Component description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ComponentName = params.get("ComponentName")
        self._ComponentType = params.get("ComponentType")
        self._Homepage = params.get("Homepage")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
ComponentName - String - Required: No - Component name
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
ComponentName - String - Required: No - Component name
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in component statistics list.
        :type TotalCount: int
        :param _ComponentStatistics: Component statistics list data array.
        :type ComponentStatistics: list of ComponentStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ComponentStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in component statistics list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ComponentStatistics(self):
        """Component statistics list data array.
        :rtype: list of ComponentStatistics
        """
        return self._ComponentStatistics

    @ComponentStatistics.setter
    def ComponentStatistics(self, ComponentStatistics):
        self._ComponentStatistics = ComponentStatistics

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self._ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self._ComponentStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`. Either `Uuid` or `ComponentId` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param _ComponentId: Component ID. Either `Uuid` or `ComponentId` must be specified. If `ComponentId` is specified, it indicates to query the information list under the specified component.
        :type ComponentId: int
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>ComponentVersion - String - Required: No - Component version number</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._ComponentId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`. Either `Uuid` or `ComponentId` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ComponentId(self):
        """Component ID. Either `Uuid` or `ComponentId` must be specified. If `ComponentId` is specified, it indicates to query the information list under the specified component.
        :rtype: int
        """
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>ComponentVersion - String - Required: No - Component version number</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._ComponentId = params.get("ComponentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in component list.
        :type TotalCount: int
        :param _Components: Component list data.
        :type Components: list of Component
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Components = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in component list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Components(self):
        """Component list data.
        :rtype: list of Component
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Username - String - Required: No - Account name</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Username - String - Required: No - Account name</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in account change history list.
        :type TotalCount: int
        :param _HistoryAccounts: Account change history data array.
        :type HistoryAccounts: list of HistoryAccount
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._HistoryAccounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in account change history list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistoryAccounts(self):
        """Account change history data array.
        :rtype: list of HistoryAccount
        """
        return self._HistoryAccounts

    @HistoryAccounts.setter
    def HistoryAccounts(self, HistoryAccounts):
        self._HistoryAccounts = HistoryAccounts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self._HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self._HistoryAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts request structure.

    """

    def __init__(self):
        r"""
        :param _VulId: Vulnerability category ID.
        :type VulId: int
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)</li>
        :type Filters: list of Filter
        """
        self._VulId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulId(self):
        """Vulnerability category ID.
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _ImpactedHosts: Affected server list array
        :type ImpactedHosts: list of ImpactedHost
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImpactedHosts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImpactedHosts(self):
        """Affected server list array
        :rtype: list of ImpactedHost
        """
        return self._ImpactedHosts

    @ImpactedHosts.setter
    def ImpactedHosts(self, ImpactedHosts):
        self._ImpactedHosts = ImpactedHosts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self._ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self._ImpactedHosts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Keywords - String - Required: No - Query keywords</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _LoginWhiteLists: Login allowlist array
        :type LoginWhiteLists: list of LoginWhiteLists
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoginWhiteLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoginWhiteLists(self):
        """Login allowlist array
        :rtype: list of LoginWhiteLists
        """
        return self._LoginWhiteLists

    @LoginWhiteLists.setter
    def LoginWhiteLists(self, LoginWhiteLists):
        self._LoginWhiteLists = LoginWhiteLists

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self._LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self._LoginWhiteLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo response structure.

    """

    def __init__(self):
        r"""
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _ProtectDays: Days under protection by CWP
        :type ProtectDays: int
        :param _MachineOs: OS.
        :type MachineOs: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _MachineStatus: Status.
<li>ONLINE: online</li>
<li>OFFLINE: offline</li>
        :type MachineStatus: str
        :param _InstanceId: Unique ID of CVM or BM instance.
        :type InstanceId: str
        :param _MachineWanIp: Public IP of server.
        :type MachineWanIp: str
        :param _Quuid: CVM or BM instance `Uuid`.
        :type Quuid: str
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param _IsProVersion: Whether CWP Pro is activated.
<li>true: yes</li>
<li>false: no</li>
        :type IsProVersion: bool
        :param _ProVersionOpenDate: CWP Pro activation time.
        :type ProVersionOpenDate: str
        :param _MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :type MachineType: str
        :param _MachineRegion: Server region, such as ap-guangzhou or ap-shanghai
        :type MachineRegion: str
        :param _PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :type PayMode: str
        :param _FreeMalwaresLeft: Number of trojans left for free scan.
        :type FreeMalwaresLeft: int
        :param _FreeVulsLeft: Number of vulnerability left for free scan.
        :type FreeVulsLeft: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MachineIp = None
        self._ProtectDays = None
        self._MachineOs = None
        self._MachineName = None
        self._MachineStatus = None
        self._InstanceId = None
        self._MachineWanIp = None
        self._Quuid = None
        self._Uuid = None
        self._IsProVersion = None
        self._ProVersionOpenDate = None
        self._MachineType = None
        self._MachineRegion = None
        self._PayMode = None
        self._FreeMalwaresLeft = None
        self._FreeVulsLeft = None
        self._RequestId = None

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def ProtectDays(self):
        """Days under protection by CWP
        :rtype: int
        """
        return self._ProtectDays

    @ProtectDays.setter
    def ProtectDays(self, ProtectDays):
        self._ProtectDays = ProtectDays

    @property
    def MachineOs(self):
        """OS.
        :rtype: str
        """
        return self._MachineOs

    @MachineOs.setter
    def MachineOs(self, MachineOs):
        self._MachineOs = MachineOs

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineStatus(self):
        """Status.
<li>ONLINE: online</li>
<li>OFFLINE: offline</li>
        :rtype: str
        """
        return self._MachineStatus

    @MachineStatus.setter
    def MachineStatus(self, MachineStatus):
        self._MachineStatus = MachineStatus

    @property
    def InstanceId(self):
        """Unique ID of CVM or BM instance.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MachineWanIp(self):
        """Public IP of server.
        :rtype: str
        """
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def Quuid(self):
        """CVM or BM instance `Uuid`.
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def IsProVersion(self):
        """Whether CWP Pro is activated.
<li>true: yes</li>
<li>false: no</li>
        :rtype: bool
        """
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def ProVersionOpenDate(self):
        """CWP Pro activation time.
        :rtype: str
        """
        return self._ProVersionOpenDate

    @ProVersionOpenDate.setter
    def ProVersionOpenDate(self, ProVersionOpenDate):
        self._ProVersionOpenDate = ProVersionOpenDate

    @property
    def MachineType(self):
        """Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        """Server region, such as ap-guangzhou or ap-shanghai
        :rtype: str
        """
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def PayMode(self):
        """Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def FreeMalwaresLeft(self):
        """Number of trojans left for free scan.
        :rtype: int
        """
        return self._FreeMalwaresLeft

    @FreeMalwaresLeft.setter
    def FreeMalwaresLeft(self, FreeMalwaresLeft):
        self._FreeMalwaresLeft = FreeMalwaresLeft

    @property
    def FreeVulsLeft(self):
        """Number of vulnerability left for free scan.
        :rtype: int
        """
        return self._FreeVulsLeft

    @FreeVulsLeft.setter
    def FreeVulsLeft(self, FreeVulsLeft):
        self._FreeVulsLeft = FreeVulsLeft

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._ProtectDays = params.get("ProtectDays")
        self._MachineOs = params.get("MachineOs")
        self._MachineName = params.get("MachineName")
        self._MachineStatus = params.get("MachineStatus")
        self._InstanceId = params.get("InstanceId")
        self._MachineWanIp = params.get("MachineWanIp")
        self._Quuid = params.get("Quuid")
        self._Uuid = params.get("Uuid")
        self._IsProVersion = params.get("IsProVersion")
        self._ProVersionOpenDate = params.get("ProVersionOpenDate")
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._PayMode = params.get("PayMode")
        self._FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self._FreeVulsLeft = params.get("FreeVulsLeft")
        self._RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines request structure.

    """

    def __init__(self):
        r"""
        :param _MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :type MachineType: str
        :param _MachineRegion: Server region, such as ap-guangzhou or ap-shanghai
        :type MachineRegion: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Keywords - String - Required: no - Query keywords </li>
<li>Status - String - Required: no - CWP client status (valid values: OFFLINE, ONLINE, UNINSTALLED)</li>
<li>Version - String - Required: no - Current CWP version (valid values: PRO_VERSION, BASIC_VERSION)</li>
Each filter can have only one value but does not support "OR" queries with multiple values
        :type Filters: list of Filter
        """
        self._MachineType = None
        self._MachineRegion = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def MachineType(self):
        """Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        """Server region, such as ap-guangzhou or ap-shanghai
        :rtype: str
        """
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Keywords - String - Required: no - Query keywords </li>
<li>Status - String - Required: no - CWP client status (valid values: OFFLINE, ONLINE, UNINSTALLED)</li>
<li>Version - String - Required: no - Current CWP version (valid values: PRO_VERSION, BASIC_VERSION)</li>
Each filter can have only one value but does not support "OR" queries with multiple values
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines response structure.

    """

    def __init__(self):
        r"""
        :param _Machines: Server list
        :type Machines: list of Machine
        :param _TotalCount: Number of servers
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Machines = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Machines(self):
        """Server list
        :rtype: list of Machine
        """
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines

    @property
    def TotalCount(self):
        """Number of servers
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self._Machines.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMaliciousRequestsRequest(AbstractModel):
    """DescribeMaliciousRequests request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, TRUSTED: trusted, UN_TRUSTED: untrusted)</li>
<li>Domain - String - Required: No - Malicious request domain name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Uuid = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, TRUSTED: trusted, UN_TRUSTED: untrusted)</li>
<li>Domain - String - Required: No - Malicious request domain name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _MaliciousRequests: Malicious request record array.
        :type MaliciousRequests: list of MaliciousRequest
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._MaliciousRequests = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MaliciousRequests(self):
        """Malicious request record array.
        :rtype: list of MaliciousRequest
        """
        return self._MaliciousRequests

    @MaliciousRequests.setter
    def MaliciousRequests(self, MaliciousRequests):
        self._MaliciousRequests = MaliciousRequests

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MaliciousRequests") is not None:
            self._MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = MaliciousRequest()
                obj._deserialize(item)
                self._MaliciousRequests.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: Agent `Uuid`.
        :type Uuid: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Trojan status (UN_OPERATED: not processed, SEGREGATED: isolated, TRUSTED: trusted)</li>
Each filter supports only one value. Query with multiple values in "OR" relationship is not supported for the time being.
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """Agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Trojan status (UN_OPERATED: not processed, SEGREGATED: isolated, TRUSTED: trusted)</li>
Each filter supports only one value. Query with multiple values in "OR" relationship is not supported for the time being.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of trojans.
        :type TotalCount: int
        :param _Malwares: Malware array.
        :type Malwares: list of Malware
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Malwares = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of trojans.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Malwares(self):
        """Malware array.
        :rtype: list of Malware
        """
        return self._Malwares

    @Malwares.setter
    def Malwares(self, Malwares):
        self._Malwares = Malwares

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self._Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self._Malwares.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: Agent `Uuid`.
        :type Uuid: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Login status (NON_LOCAL_LOGIN: unusual login location, NORMAL_LOGIN: intended login)</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """Agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Login status (NON_LOCAL_LOGIN: unusual login location, NORMAL_LOGIN: intended login)</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _NonLocalLoginPlaces: Unusual login location information array.
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NonLocalLoginPlaces = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NonLocalLoginPlaces(self):
        """Unusual login location information array.
        :rtype: list of NonLocalLoginPlace
        """
        return self._NonLocalLoginPlaces

    @NonLocalLoginPlaces.setter
    def NonLocalLoginPlaces(self, NonLocalLoginPlaces):
        self._NonLocalLoginPlaces = NonLocalLoginPlaces

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self._NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self._NonLocalLoginPlaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Port - Uint64 - Required: No - Port number</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in port statistics list
        :type TotalCount: int
        :param _OpenPortStatistics: Port statistics list
        :type OpenPortStatistics: list of OpenPortStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._OpenPortStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in port statistics list
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OpenPortStatistics(self):
        """Port statistics list
        :rtype: list of OpenPortStatistics
        """
        return self._OpenPortStatistics

    @OpenPortStatistics.setter
    def OpenPortStatistics(self, OpenPortStatistics):
        self._OpenPortStatistics = OpenPortStatistics

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self._OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self._OpenPortStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOpenPortTaskStatusRequest(AbstractModel):
    """DescribeOpenPortTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortTaskStatusResponse(AbstractModel):
    """DescribeOpenPortTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeOpenPorts` API to get the list of real-time processes) </li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting port</li>
<li>FAILED: failed to get processes</li>
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeOpenPorts` API to get the list of real-time processes) </li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting port</li>
<li>FAILED: failed to get processes</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`. Either `Port` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param _Port: Open port number. Either `Port` or `Uuid` must be specified. If `Port` is specified, it indicates to query the information list under the specified port.
        :type Port: int
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._Port = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`. Either `Port` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Port(self):
        """Open port number. Either `Port` or `Uuid` must be specified. If `Port` is specified, it indicates to query the information list under the specified port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Port - Uint64 - Required: No - Port number</li>
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Port = params.get("Port")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in port list.
        :type TotalCount: int
        :param _OpenPorts: Port list.
        :type OpenPorts: list of OpenPort
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._OpenPorts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in port list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OpenPorts(self):
        """Port list.
        :rtype: list of OpenPort
        """
        return self._OpenPorts

    @OpenPorts.setter
    def OpenPorts(self, OpenPorts):
        self._OpenPorts = OpenPorts

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self._OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self._OpenPorts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics request structure.

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _OnlineMachineNum: Number of online servers.
        :type OnlineMachineNum: int
        :param _ProVersionMachineNum: Number of servers activated CWP Pro.
        :type ProVersionMachineNum: int
        :param _MalwareNum: Number of trojan files.
        :type MalwareNum: int
        :param _NonlocalLoginNum: Number of unusual login locations.
        :type NonlocalLoginNum: int
        :param _BruteAttackSuccessNum: Number of successful brute force attacks.
        :type BruteAttackSuccessNum: int
        :param _VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param _BaseLineNum: Security baseline number
        :type BaseLineNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OnlineMachineNum = None
        self._ProVersionMachineNum = None
        self._MalwareNum = None
        self._NonlocalLoginNum = None
        self._BruteAttackSuccessNum = None
        self._VulNum = None
        self._BaseLineNum = None
        self._RequestId = None

    @property
    def OnlineMachineNum(self):
        """Number of online servers.
        :rtype: int
        """
        return self._OnlineMachineNum

    @OnlineMachineNum.setter
    def OnlineMachineNum(self, OnlineMachineNum):
        self._OnlineMachineNum = OnlineMachineNum

    @property
    def ProVersionMachineNum(self):
        """Number of servers activated CWP Pro.
        :rtype: int
        """
        return self._ProVersionMachineNum

    @ProVersionMachineNum.setter
    def ProVersionMachineNum(self, ProVersionMachineNum):
        self._ProVersionMachineNum = ProVersionMachineNum

    @property
    def MalwareNum(self):
        """Number of trojan files.
        :rtype: int
        """
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def NonlocalLoginNum(self):
        """Number of unusual login locations.
        :rtype: int
        """
        return self._NonlocalLoginNum

    @NonlocalLoginNum.setter
    def NonlocalLoginNum(self, NonlocalLoginNum):
        self._NonlocalLoginNum = NonlocalLoginNum

    @property
    def BruteAttackSuccessNum(self):
        """Number of successful brute force attacks.
        :rtype: int
        """
        return self._BruteAttackSuccessNum

    @BruteAttackSuccessNum.setter
    def BruteAttackSuccessNum(self, BruteAttackSuccessNum):
        self._BruteAttackSuccessNum = BruteAttackSuccessNum

    @property
    def VulNum(self):
        """Number of vulnerabilities.
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def BaseLineNum(self):
        """Security baseline number
        :rtype: int
        """
        return self._BaseLineNum

    @BaseLineNum.setter
    def BaseLineNum(self, BaseLineNum):
        self._BaseLineNum = BaseLineNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OnlineMachineNum = params.get("OnlineMachineNum")
        self._ProVersionMachineNum = params.get("ProVersionMachineNum")
        self._MalwareNum = params.get("MalwareNum")
        self._NonlocalLoginNum = params.get("NonlocalLoginNum")
        self._BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self._VulNum = params.get("VulNum")
        self._BaseLineNum = params.get("BaseLineNum")
        self._RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo request structure.

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo response structure.

    """

    def __init__(self):
        r"""
        :param _PostPayCost: Fee on yesterday (pay-as-you-go)
        :type PostPayCost: int
        :param _IsAutoOpenProVersion: Whether CWP Pro is activated for new servers
        :type IsAutoOpenProVersion: bool
        :param _ProVersionNum: Number of servers on CWP Pro
        :type ProVersionNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PostPayCost = None
        self._IsAutoOpenProVersion = None
        self._ProVersionNum = None
        self._RequestId = None

    @property
    def PostPayCost(self):
        """Fee on yesterday (pay-as-you-go)
        :rtype: int
        """
        return self._PostPayCost

    @PostPayCost.setter
    def PostPayCost(self, PostPayCost):
        self._PostPayCost = PostPayCost

    @property
    def IsAutoOpenProVersion(self):
        """Whether CWP Pro is activated for new servers
        :rtype: bool
        """
        return self._IsAutoOpenProVersion

    @IsAutoOpenProVersion.setter
    def IsAutoOpenProVersion(self, IsAutoOpenProVersion):
        self._IsAutoOpenProVersion = IsAutoOpenProVersion

    @property
    def ProVersionNum(self):
        """Number of servers on CWP Pro
        :rtype: int
        """
        return self._ProVersionNum

    @ProVersionNum.setter
    def ProVersionNum(self, ProVersionNum):
        self._ProVersionNum = ProVersionNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PostPayCost = params.get("PostPayCost")
        self._IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self._ProVersionNum = params.get("ProVersionNum")
        self._RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>ProcessName - String - Required: No - Process name</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in process statistics list.
        :type TotalCount: int
        :param _ProcessStatistics: Process statistics list array.
        :type ProcessStatistics: list of ProcessStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProcessStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in process statistics list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProcessStatistics(self):
        """Process statistics list array.
        :rtype: list of ProcessStatistics
        """
        return self._ProcessStatistics

    @ProcessStatistics.setter
    def ProcessStatistics(self, ProcessStatistics):
        self._ProcessStatistics = ProcessStatistics

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self._ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self._ProcessStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeProcesses` API to get the list of real-time processes)</li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting process</li>
<li>FAILED: failed to get processes</li>
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeProcesses` API to get the list of real-time processes)</li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting process</li>
<li>FAILED: failed to get processes</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `Uuid`. Either `Uuid` or `ProcessName` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param _ProcessName: Process name. Either `Uuid` or `ProcessName` must be specified. If `ProcessName` is specified, it indicates to query the information list under the specified process.
        :type ProcessName: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
        self._Uuid = None
        self._ProcessName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Uuid(self):
        """CWP agent `Uuid`. Either `Uuid` or `ProcessName` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def ProcessName(self):
        """Process name. Either `Uuid` or `ProcessName` must be specified. If `ProcessName` is specified, it indicates to query the information list under the specified process.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._ProcessName = params.get("ProcessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records in process list.
        :type TotalCount: int
        :param _Processes: Process list data array.
        :type Processes: list of Process
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Processes = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records in process list.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Processes(self):
        """Process list data array.
        :rtype: list of Process
        """
        return self._Processes

    @Processes.setter
    def Processes(self, Processes):
        self._Processes = Processes

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self._Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self._Processes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
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
        


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityDynamics: Security event message array.
        :type SecurityDynamics: list of SecurityDynamic
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityDynamics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SecurityDynamics(self):
        """Security event message array.
        :rtype: list of SecurityDynamic
        """
        return self._SecurityDynamics

    @SecurityDynamics.setter
    def SecurityDynamics(self, SecurityDynamics):
        self._SecurityDynamics = SecurityDynamics

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self._SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self._SecurityDynamics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Start time.
        :type BeginDate: str
        :param _EndDate: End time.
        :type EndDate: str
        """
        self._BeginDate = None
        self._EndDate = None

    @property
    def BeginDate(self):
        """Start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """End time.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends response structure.

    """

    def __init__(self):
        r"""
        :param _Malwares: Trojan event statistics array.
        :type Malwares: list of SecurityTrend
        :param _NonLocalLoginPlaces: Unusual login location event statistics array.
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param _BruteAttacks: Brute force attack event statistics array.
        :type BruteAttacks: list of SecurityTrend
        :param _Vuls: Vulnerability statistics array.
        :type Vuls: list of SecurityTrend
        :param _BaseLines: Baseline statistics array.
        :type BaseLines: list of SecurityTrend
        :param _MaliciousRequests: Statistics array of malicious requests.
        :type MaliciousRequests: list of SecurityTrend
        :param _HighRiskBashs: Statistics array of high-risk commands.
        :type HighRiskBashs: list of SecurityTrend
        :param _ReverseShells: Statistics array of reverse shells.
        :type ReverseShells: list of SecurityTrend
        :param _PrivilegeEscalations: Statistics array of local privilege escalations.
        :type PrivilegeEscalations: list of SecurityTrend
        :param _CyberAttacks: Statistics array of network attacks.
        :type CyberAttacks: list of SecurityTrend
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Malwares = None
        self._NonLocalLoginPlaces = None
        self._BruteAttacks = None
        self._Vuls = None
        self._BaseLines = None
        self._MaliciousRequests = None
        self._HighRiskBashs = None
        self._ReverseShells = None
        self._PrivilegeEscalations = None
        self._CyberAttacks = None
        self._RequestId = None

    @property
    def Malwares(self):
        """Trojan event statistics array.
        :rtype: list of SecurityTrend
        """
        return self._Malwares

    @Malwares.setter
    def Malwares(self, Malwares):
        self._Malwares = Malwares

    @property
    def NonLocalLoginPlaces(self):
        """Unusual login location event statistics array.
        :rtype: list of SecurityTrend
        """
        return self._NonLocalLoginPlaces

    @NonLocalLoginPlaces.setter
    def NonLocalLoginPlaces(self, NonLocalLoginPlaces):
        self._NonLocalLoginPlaces = NonLocalLoginPlaces

    @property
    def BruteAttacks(self):
        """Brute force attack event statistics array.
        :rtype: list of SecurityTrend
        """
        return self._BruteAttacks

    @BruteAttacks.setter
    def BruteAttacks(self, BruteAttacks):
        self._BruteAttacks = BruteAttacks

    @property
    def Vuls(self):
        """Vulnerability statistics array.
        :rtype: list of SecurityTrend
        """
        return self._Vuls

    @Vuls.setter
    def Vuls(self, Vuls):
        self._Vuls = Vuls

    @property
    def BaseLines(self):
        """Baseline statistics array.
        :rtype: list of SecurityTrend
        """
        return self._BaseLines

    @BaseLines.setter
    def BaseLines(self, BaseLines):
        self._BaseLines = BaseLines

    @property
    def MaliciousRequests(self):
        """Statistics array of malicious requests.
        :rtype: list of SecurityTrend
        """
        return self._MaliciousRequests

    @MaliciousRequests.setter
    def MaliciousRequests(self, MaliciousRequests):
        self._MaliciousRequests = MaliciousRequests

    @property
    def HighRiskBashs(self):
        """Statistics array of high-risk commands.
        :rtype: list of SecurityTrend
        """
        return self._HighRiskBashs

    @HighRiskBashs.setter
    def HighRiskBashs(self, HighRiskBashs):
        self._HighRiskBashs = HighRiskBashs

    @property
    def ReverseShells(self):
        """Statistics array of reverse shells.
        :rtype: list of SecurityTrend
        """
        return self._ReverseShells

    @ReverseShells.setter
    def ReverseShells(self, ReverseShells):
        self._ReverseShells = ReverseShells

    @property
    def PrivilegeEscalations(self):
        """Statistics array of local privilege escalations.
        :rtype: list of SecurityTrend
        """
        return self._PrivilegeEscalations

    @PrivilegeEscalations.setter
    def PrivilegeEscalations(self, PrivilegeEscalations):
        self._PrivilegeEscalations = PrivilegeEscalations

    @property
    def CyberAttacks(self):
        """Statistics array of network attacks.
        :rtype: list of SecurityTrend
        """
        return self._CyberAttacks

    @CyberAttacks.setter
    def CyberAttacks(self, CyberAttacks):
        self._CyberAttacks = CyberAttacks

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self._Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self._NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self._BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self._Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self._BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self._MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self._HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self._ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self._PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self._CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self._CyberAttacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Tag ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """Tag ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines response structure.

    """

    def __init__(self):
        r"""
        :param _List: List data
        :type List: list of TagMachine
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """List data
        :rtype: list of TagMachine
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags request structure.

    """

    def __init__(self):
        r"""
        :param _MachineType: CVM instance type.
<li>CVM: CVM</li>
<li>BM: CPM</li>
        :type MachineType: str
        :param _MachineRegion: Server region, such as `ap-guangzhou` and `ap-shanghai`
        :type MachineRegion: str
        """
        self._MachineType = None
        self._MachineRegion = None

    @property
    def MachineType(self):
        """CVM instance type.
<li>CVM: CVM</li>
<li>BM: CPM</li>
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        """Server region, such as `ap-guangzhou` and `ap-shanghai`
        :rtype: str
        """
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags response structure.

    """

    def __init__(self):
        r"""
        :param _List: List information
        :type List: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """List information
        :rtype: list of Tag
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `UUID`
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """CWP agent `UUID`
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _UsualLoginPlaces: Usual login location array
        :type UsualLoginPlaces: list of UsualPlace
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsualLoginPlaces = None
        self._RequestId = None

    @property
    def UsualLoginPlaces(self):
        """Usual login location array
        :rtype: list of UsualPlace
        """
        return self._UsualLoginPlaces

    @UsualLoginPlaces.setter
    def UsualLoginPlaces(self, UsualLoginPlaces):
        self._UsualLoginPlaces = UsualLoginPlaces

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self._UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self._UsualLoginPlaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo request structure.

    """

    def __init__(self):
        r"""
        :param _VulId: Vulnerability category ID.
        :type VulId: int
        """
        self._VulId = None

    @property
    def VulId(self):
        """Vulnerability category ID.
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo response structure.

    """

    def __init__(self):
        r"""
        :param _VulId: Vulnerability category ID.
        :type VulId: int
        :param _VulName: Vulnerability name.
        :type VulName: str
        :param _VulLevel: Vulnerability level.
        :type VulLevel: str
        :param _VulType: Vulnerability type.
        :type VulType: str
        :param _Description: Vulnerability description.
        :type Description: str
        :param _RepairPlan: Repair plan.
        :type RepairPlan: str
        :param _CveId: Vulnerability CVE.
        :type CveId: str
        :param _Reference: Reference link.
        :type Reference: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VulId = None
        self._VulName = None
        self._VulLevel = None
        self._VulType = None
        self._Description = None
        self._RepairPlan = None
        self._CveId = None
        self._Reference = None
        self._RequestId = None

    @property
    def VulId(self):
        """Vulnerability category ID.
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulName(self):
        """Vulnerability name.
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        """Vulnerability level.
        :rtype: str
        """
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def VulType(self):
        """Vulnerability type.
        :rtype: str
        """
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Description(self):
        """Vulnerability description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RepairPlan(self):
        """Repair plan.
        :rtype: str
        """
        return self._RepairPlan

    @RepairPlan.setter
    def RepairPlan(self, RepairPlan):
        self._RepairPlan = RepairPlan

    @property
    def CveId(self):
        """Vulnerability CVE.
        :rtype: str
        """
        return self._CveId

    @CveId.setter
    def CveId(self, CveId):
        self._CveId = CveId

    @property
    def Reference(self):
        """Reference link.
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._VulType = params.get("VulType")
        self._Description = params.get("Description")
        self._RepairPlan = params.get("RepairPlan")
        self._CveId = params.get("CveId")
        self._Reference = params.get("Reference")
        self._RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult request structure.

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult response structure.

    """

    def __init__(self):
        r"""
        :param _VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param _ProVersionNum: Number of servers activated CWP Pro
        :type ProVersionNum: int
        :param _ImpactedHostNum: Number of affected activated CWP Pro.
        :type ImpactedHostNum: int
        :param _HostNum: Total number of servers.
        :type HostNum: int
        :param _BasicVersionNum: Number of servers on CWP Basic.
        :type BasicVersionNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VulNum = None
        self._ProVersionNum = None
        self._ImpactedHostNum = None
        self._HostNum = None
        self._BasicVersionNum = None
        self._RequestId = None

    @property
    def VulNum(self):
        """Number of vulnerabilities.
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def ProVersionNum(self):
        """Number of servers activated CWP Pro
        :rtype: int
        """
        return self._ProVersionNum

    @ProVersionNum.setter
    def ProVersionNum(self, ProVersionNum):
        self._ProVersionNum = ProVersionNum

    @property
    def ImpactedHostNum(self):
        """Number of affected activated CWP Pro.
        :rtype: int
        """
        return self._ImpactedHostNum

    @ImpactedHostNum.setter
    def ImpactedHostNum(self, ImpactedHostNum):
        self._ImpactedHostNum = ImpactedHostNum

    @property
    def HostNum(self):
        """Total number of servers.
        :rtype: int
        """
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def BasicVersionNum(self):
        """Number of servers on CWP Basic.
        :rtype: int
        """
        return self._BasicVersionNum

    @BasicVersionNum.setter
    def BasicVersionNum(self, BasicVersionNum):
        self._BasicVersionNum = BasicVersionNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VulNum = params.get("VulNum")
        self._ProVersionNum = params.get("ProVersionNum")
        self._ImpactedHostNum = params.get("ImpactedHostNum")
        self._HostNum = params.get("HostNum")
        self._BasicVersionNum = params.get("BasicVersionNum")
        self._RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls request structure.

    """

    def __init__(self):
        r"""
        :param _VulType: Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>
        :type VulType: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)

Only one value is allowed for the `Status` filter, and "OR" logic is not supported.
        :type Filters: list of Filter
        """
        self._VulType = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def VulType(self):
        """Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>
        :rtype: str
        """
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)

Only one value is allowed for the `Status` filter, and "OR" logic is not supported.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._VulType = params.get("VulType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of vulnerabilities.
        :type TotalCount: int
        :param _Vuls: Vulnerability list array.
        :type Vuls: list of Vul
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Vuls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of vulnerabilities.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Vuls(self):
        """Vulnerability list array.
        :rtype: list of Vul
        """
        return self._Vuls

    @Vuls.setter
    def Vuls(self, Vuls):
        self._Vuls = Vuls

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self._Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self._Vuls.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        """Weekly CWP Pro report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks response structure.

    """

    def __init__(self):
        r"""
        :param _WeeklyReportBruteAttacks: Brute force attack array in weekly CWP Pro report.
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WeeklyReportBruteAttacks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportBruteAttacks(self):
        """Brute force attack array in weekly CWP Pro report.
        :rtype: list of WeeklyReportBruteAttack
        """
        return self._WeeklyReportBruteAttacks

    @WeeklyReportBruteAttacks.setter
    def WeeklyReportBruteAttacks(self, WeeklyReportBruteAttacks):
        self._WeeklyReportBruteAttacks = WeeklyReportBruteAttacks

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WeeklyReportBruteAttacks") is not None:
            self._WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self._WeeklyReportBruteAttacks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        """
        self._BeginDate = None

    @property
    def BeginDate(self):
        """Weekly CWP Pro report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo response structure.

    """

    def __init__(self):
        r"""
        :param _CompanyName: Account owner name.
        :type CompanyName: str
        :param _MachineNum: Total number of servers.
        :type MachineNum: int
        :param _OnlineMachineNum: Number of online CWP agents
        :type OnlineMachineNum: int
        :param _OfflineMachineNum: Number of offline CWP agents.
        :type OfflineMachineNum: int
        :param _ProVersionMachineNum: Number of servers on CWP Pro.
        :type ProVersionMachineNum: int
        :param _BeginDate: Weekly report start time
        :type BeginDate: str
        :param _EndDate: Weekly report end time
        :type EndDate: str
        :param _Level: Security level
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
        :type Level: str
        :param _MalwareNum: Number of trojan records.
        :type MalwareNum: int
        :param _NonlocalLoginNum: Number of unusual login locations.
        :type NonlocalLoginNum: int
        :param _BruteAttackSuccessNum: Number of successful brute force attacks.
        :type BruteAttackSuccessNum: int
        :param _VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param _DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CompanyName = None
        self._MachineNum = None
        self._OnlineMachineNum = None
        self._OfflineMachineNum = None
        self._ProVersionMachineNum = None
        self._BeginDate = None
        self._EndDate = None
        self._Level = None
        self._MalwareNum = None
        self._NonlocalLoginNum = None
        self._BruteAttackSuccessNum = None
        self._VulNum = None
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def CompanyName(self):
        """Account owner name.
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def MachineNum(self):
        """Total number of servers.
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum

    @property
    def OnlineMachineNum(self):
        """Number of online CWP agents
        :rtype: int
        """
        return self._OnlineMachineNum

    @OnlineMachineNum.setter
    def OnlineMachineNum(self, OnlineMachineNum):
        self._OnlineMachineNum = OnlineMachineNum

    @property
    def OfflineMachineNum(self):
        """Number of offline CWP agents.
        :rtype: int
        """
        return self._OfflineMachineNum

    @OfflineMachineNum.setter
    def OfflineMachineNum(self, OfflineMachineNum):
        self._OfflineMachineNum = OfflineMachineNum

    @property
    def ProVersionMachineNum(self):
        """Number of servers on CWP Pro.
        :rtype: int
        """
        return self._ProVersionMachineNum

    @ProVersionMachineNum.setter
    def ProVersionMachineNum(self, ProVersionMachineNum):
        self._ProVersionMachineNum = ProVersionMachineNum

    @property
    def BeginDate(self):
        """Weekly report start time
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """Weekly report end time
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Level(self):
        """Security level
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def MalwareNum(self):
        """Number of trojan records.
        :rtype: int
        """
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def NonlocalLoginNum(self):
        """Number of unusual login locations.
        :rtype: int
        """
        return self._NonlocalLoginNum

    @NonlocalLoginNum.setter
    def NonlocalLoginNum(self, NonlocalLoginNum):
        self._NonlocalLoginNum = NonlocalLoginNum

    @property
    def BruteAttackSuccessNum(self):
        """Number of successful brute force attacks.
        :rtype: int
        """
        return self._BruteAttackSuccessNum

    @BruteAttackSuccessNum.setter
    def BruteAttackSuccessNum(self, BruteAttackSuccessNum):
        self._BruteAttackSuccessNum = BruteAttackSuccessNum

    @property
    def VulNum(self):
        """Number of vulnerabilities.
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def DownloadUrl(self):
        """Download address for exported file.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._MachineNum = params.get("MachineNum")
        self._OnlineMachineNum = params.get("OnlineMachineNum")
        self._OfflineMachineNum = params.get("OfflineMachineNum")
        self._ProVersionMachineNum = params.get("ProVersionMachineNum")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._Level = params.get("Level")
        self._MalwareNum = params.get("MalwareNum")
        self._NonlocalLoginNum = params.get("NonlocalLoginNum")
        self._BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self._VulNum = params.get("VulNum")
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        """Weekly CWP Pro report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _WeeklyReportMalwares: Trojan data in weekly CWP Pro report.
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WeeklyReportMalwares = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportMalwares(self):
        """Trojan data in weekly CWP Pro report.
        :rtype: list of WeeklyReportMalware
        """
        return self._WeeklyReportMalwares

    @WeeklyReportMalwares.setter
    def WeeklyReportMalwares(self, WeeklyReportMalwares):
        self._WeeklyReportMalwares = WeeklyReportMalwares

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WeeklyReportMalwares") is not None:
            self._WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self._WeeklyReportMalwares.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        """Weekly CWP Pro report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _WeeklyReportNonlocalLoginPlaces: Unusual login location data in weekly CWP Pro report
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WeeklyReportNonlocalLoginPlaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportNonlocalLoginPlaces(self):
        """Unusual login location data in weekly CWP Pro report
        :rtype: list of WeeklyReportNonlocalLoginPlace
        """
        return self._WeeklyReportNonlocalLoginPlaces

    @WeeklyReportNonlocalLoginPlaces.setter
    def WeeklyReportNonlocalLoginPlaces(self, WeeklyReportNonlocalLoginPlaces):
        self._WeeklyReportNonlocalLoginPlaces = WeeklyReportNonlocalLoginPlaces

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self._WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self._WeeklyReportNonlocalLoginPlaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls request structure.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._BeginDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginDate(self):
        """Weekly CWP Pro report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls response structure.

    """

    def __init__(self):
        r"""
        :param _WeeklyReportVuls: Vulnerability data array in weekly CWP Pro report.
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WeeklyReportVuls = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReportVuls(self):
        """Vulnerability data array in weekly CWP Pro report.
        :rtype: list of WeeklyReportVul
        """
        return self._WeeklyReportVuls

    @WeeklyReportVuls.setter
    def WeeklyReportVuls(self, WeeklyReportVuls):
        self._WeeklyReportVuls = WeeklyReportVuls

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WeeklyReportVuls") is not None:
            self._WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self._WeeklyReportVuls.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """Number of results to be returned. Default value: 10. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
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
        


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports response structure.

    """

    def __init__(self):
        r"""
        :param _WeeklyReports: Weekly CWP Pro report list array.
        :type WeeklyReports: list of WeeklyReport
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WeeklyReports = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WeeklyReports(self):
        """Weekly CWP Pro report list array.
        :rtype: list of WeeklyReport
        """
        return self._WeeklyReports

    @WeeklyReports.setter
    def WeeklyReports(self, WeeklyReports):
        self._WeeklyReports = WeeklyReports

    @property
    def TotalCount(self):
        """Total number of records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WeeklyReports") is not None:
            self._WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self._WeeklyReports.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class EditTagsRequest(AbstractModel):
    """EditTags request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Tag name
        :type Name: str
        :param _Id: Tag ID
        :type Id: int
        :param _Quuids: CVM instance ID
        :type Quuids: list of str
        """
        self._Name = None
        self._Id = None
        self._Quuids = None

    @property
    def Name(self):
        """Tag name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        """Tag ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Quuids(self):
        """CVM instance ID
        :rtype: list of str
        """
        return self._Quuids

    @Quuids.setter
    def Quuids(self, Quuids):
        self._Quuids = Quuids


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditTagsResponse(AbstractModel):
    """EditTags response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks request structure.

    """


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Download address for exported file.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests request structure.

    """


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Download address for exported file.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares request structure.

    """


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Download address for exported file.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces request structure.

    """


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param _TaskId: Export task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._TaskId = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        """Download address for exported file.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def TaskId(self):
        """Export task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.

    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values is `OR`.

    * There can be up to 5 filters
    * There can be up to 5 `Values` in the same `Filter`.

    """

    def __init__(self):
        r"""
        :param _Name: Filter key name.
        :type Name: str
        :param _Values: One or more filter values.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Filter key name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """One or more filter values.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistoryAccount(AbstractModel):
    """Account change history data.

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID.
        :type Id: int
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _Username: Account name.
        :type Username: str
        :param _ModifyType: Account change type.
<li>CREATE: creates account</li>
<li>MODIFY: modifies account</li>
<li>DELETE: deletes account</li>
        :type ModifyType: str
        :param _ModifyTime: Change time.
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Username = None
        self._ModifyType = None
        self._ModifyTime = None

    @property
    def Id(self):
        """Unique ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Username(self):
        """Account name.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ModifyType(self):
        """Account change type.
<li>CREATE: creates account</li>
<li>MODIFY: modifies account</li>
<li>DELETE: deletes account</li>
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ModifyTime(self):
        """Change time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Username = params.get("Username")
        self._ModifyType = params.get("ModifyType")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Vulnerability ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Vulnerability ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """Affected server information

    """

    def __init__(self):
        r"""
        :param _Id: Vulnerability ID.
        :type Id: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _LastScanTime: Last detection time.
        :type LastScanTime: str
        :param _VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>SCANING: scanning</li>
<li>FIXED: fixed</li>
        :type VulStatus: str
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _Description: Vulnerability description.
        :type Description: str
        :param _VulId: Vulnerability category ID.
        :type VulId: int
        :param _IsProVersion: Whether it is the CWP Pro.
        :type IsProVersion: bool
        """
        self._Id = None
        self._MachineIp = None
        self._MachineName = None
        self._LastScanTime = None
        self._VulStatus = None
        self._Uuid = None
        self._Description = None
        self._VulId = None
        self._IsProVersion = None

    @property
    def Id(self):
        """Vulnerability ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def LastScanTime(self):
        """Last detection time.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def VulStatus(self):
        """Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>SCANING: scanning</li>
<li>FIXED: fixed</li>
        :rtype: str
        """
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Description(self):
        """Vulnerability description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulId(self):
        """Vulnerability category ID.
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def IsProVersion(self):
        """Whether it is the CWP Pro.
        :rtype: bool
        """
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._LastScanTime = params.get("LastScanTime")
        self._VulStatus = params.get("VulStatus")
        self._Uuid = params.get("Uuid")
        self._Description = params.get("Description")
        self._VulId = params.get("VulId")
        self._IsProVersion = params.get("IsProVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteLists(AbstractModel):
    """Login allowlist

    """

    def __init__(self):
        r"""
        :param _Id: Record ID
        :type Id: int
        :param _Uuid: CWP agent ID
        :type Uuid: str
        :param _Places: Whitelisted location
        :type Places: list of Place
        :param _UserName: Whitelisted users (separated by commas)
        :type UserName: str
        :param _SrcIp: Whitelisted IPs (separated by commas)
        :type SrcIp: str
        :param _IsGlobal: Whether this rule is applied to all servers under the current account
        :type IsGlobal: bool
        :param _CreateTime: Whitelist creation time
        :type CreateTime: str
        :param _ModifyTime: Whitelist modification time
        :type ModifyTime: str
        :param _MachineName: Server name
        :type MachineName: str
        :param _HostIp: Server IP
        :type HostIp: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._Id = None
        self._Uuid = None
        self._Places = None
        self._UserName = None
        self._SrcIp = None
        self._IsGlobal = None
        self._CreateTime = None
        self._ModifyTime = None
        self._MachineName = None
        self._HostIp = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Id(self):
        """Record ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent ID
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Places(self):
        """Whitelisted location
        :rtype: list of Place
        """
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places

    @property
    def UserName(self):
        """Whitelisted users (separated by commas)
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def SrcIp(self):
        """Whitelisted IPs (separated by commas)
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def IsGlobal(self):
        """Whether this rule is applied to all servers under the current account
        :rtype: bool
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def CreateTime(self):
        """Whitelist creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """Whitelist modification time
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def MachineName(self):
        """Server name
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def HostIp(self):
        """Server IP
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        self._UserName = params.get("UserName")
        self._SrcIp = params.get("SrcIp")
        self._IsGlobal = params.get("IsGlobal")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._MachineName = params.get("MachineName")
        self._HostIp = params.get("HostIp")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteListsRule(AbstractModel):
    """Whitelist rule

    """

    def __init__(self):
        r"""
        :param _Places: Whitelisted location
        :type Places: list of Place
        :param _SrcIp: Whitelisted IPs (separated by commas). This parameter can be an IP range.
        :type SrcIp: str
        :param _UserName: Whitelisted usernames (separated by commas)
        :type UserName: str
        :param _IsGlobal: Whether this rule is applied to all servers under the current account
        :type IsGlobal: bool
        :param _HostIp: Server for which the allowlist takes effect
        :type HostIp: str
        :param _Id: Rule ID, used for rule updating
        :type Id: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        """
        self._Places = None
        self._SrcIp = None
        self._UserName = None
        self._IsGlobal = None
        self._HostIp = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Places(self):
        """Whitelisted location
        :rtype: list of Place
        """
        return self._Places

    @Places.setter
    def Places(self, Places):
        self._Places = Places

    @property
    def SrcIp(self):
        """Whitelisted IPs (separated by commas). This parameter can be an IP range.
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def UserName(self):
        """Whitelisted usernames (separated by commas)
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def IsGlobal(self):
        """Whether this rule is applied to all servers under the current account
        :rtype: bool
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal

    @property
    def HostIp(self):
        """Server for which the allowlist takes effect
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def Id(self):
        """Rule ID, used for rule updating
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Places") is not None:
            self._Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self._Places.append(obj)
        self._SrcIp = params.get("SrcIp")
        self._UserName = params.get("UserName")
        self._IsGlobal = params.get("IsGlobal")
        self._HostIp = params.get("HostIp")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Machine(AbstractModel):
    """Server list

    """

    def __init__(self):
        r"""
        :param _MachineName: Server name.
        :type MachineName: str
        :param _MachineOs: Server OS.
        :type MachineOs: str
        :param _MachineStatus: Server status.
<li>OFFLINE: offline</li>
<li>ONLINE: online</li>
<li>MACHINE_STOPPED: shut down</li>
        :type MachineStatus: str
        :param _Uuid: CWP agent `Uuid`. If the agent is offline for a long time, a null character will be returned.
        :type Uuid: str
        :param _Quuid: CVM or BM instance `Uuid`.
        :type Quuid: str
        :param _VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _IsProVersion: Whether the server has enabled CWP Pro.
<li>true: yes</li>
<li>false: no</li>
        :type IsProVersion: bool
        :param _MachineWanIp: Public IP of server.
        :type MachineWanIp: str
        :param _PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :type PayMode: str
        :param _MalwareNum: Number of trojans.
        :type MalwareNum: int
        :param _Tag: Tag information
        :type Tag: list of MachineTag
        :param _BaselineNum: Number of baseline risks.
        :type BaselineNum: int
        :param _CyberAttackNum: Number of network risks.
        :type CyberAttackNum: int
        :param _SecurityStatus: Risk status.
<li>SAFE: safe</li>
<li>RISK: at risk</li>
<li>UNKNOWN: unknown</li>
        :type SecurityStatus: str
        :param _InvasionNum: Number of intrusions
        :type InvasionNum: int
        :param _RegionInfo: Region information
        :type RegionInfo: :class:`tencentcloud.yunjing.v20180228.models.RegionInfo`
        """
        self._MachineName = None
        self._MachineOs = None
        self._MachineStatus = None
        self._Uuid = None
        self._Quuid = None
        self._VulNum = None
        self._MachineIp = None
        self._IsProVersion = None
        self._MachineWanIp = None
        self._PayMode = None
        self._MalwareNum = None
        self._Tag = None
        self._BaselineNum = None
        self._CyberAttackNum = None
        self._SecurityStatus = None
        self._InvasionNum = None
        self._RegionInfo = None

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineOs(self):
        """Server OS.
        :rtype: str
        """
        return self._MachineOs

    @MachineOs.setter
    def MachineOs(self, MachineOs):
        self._MachineOs = MachineOs

    @property
    def MachineStatus(self):
        """Server status.
<li>OFFLINE: offline</li>
<li>ONLINE: online</li>
<li>MACHINE_STOPPED: shut down</li>
        :rtype: str
        """
        return self._MachineStatus

    @MachineStatus.setter
    def MachineStatus(self, MachineStatus):
        self._MachineStatus = MachineStatus

    @property
    def Uuid(self):
        """CWP agent `Uuid`. If the agent is offline for a long time, a null character will be returned.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Quuid(self):
        """CVM or BM instance `Uuid`.
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def VulNum(self):
        """Number of vulnerabilities.
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def IsProVersion(self):
        """Whether the server has enabled CWP Pro.
<li>true: yes</li>
<li>false: no</li>
        :rtype: bool
        """
        return self._IsProVersion

    @IsProVersion.setter
    def IsProVersion(self, IsProVersion):
        self._IsProVersion = IsProVersion

    @property
    def MachineWanIp(self):
        """Public IP of server.
        :rtype: str
        """
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def PayMode(self):
        """Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def MalwareNum(self):
        """Number of trojans.
        :rtype: int
        """
        return self._MalwareNum

    @MalwareNum.setter
    def MalwareNum(self, MalwareNum):
        self._MalwareNum = MalwareNum

    @property
    def Tag(self):
        """Tag information
        :rtype: list of MachineTag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def BaselineNum(self):
        """Number of baseline risks.
        :rtype: int
        """
        return self._BaselineNum

    @BaselineNum.setter
    def BaselineNum(self, BaselineNum):
        self._BaselineNum = BaselineNum

    @property
    def CyberAttackNum(self):
        """Number of network risks.
        :rtype: int
        """
        return self._CyberAttackNum

    @CyberAttackNum.setter
    def CyberAttackNum(self, CyberAttackNum):
        self._CyberAttackNum = CyberAttackNum

    @property
    def SecurityStatus(self):
        """Risk status.
<li>SAFE: safe</li>
<li>RISK: at risk</li>
<li>UNKNOWN: unknown</li>
        :rtype: str
        """
        return self._SecurityStatus

    @SecurityStatus.setter
    def SecurityStatus(self, SecurityStatus):
        self._SecurityStatus = SecurityStatus

    @property
    def InvasionNum(self):
        """Number of intrusions
        :rtype: int
        """
        return self._InvasionNum

    @InvasionNum.setter
    def InvasionNum(self, InvasionNum):
        self._InvasionNum = InvasionNum

    @property
    def RegionInfo(self):
        """Region information
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RegionInfo`
        """
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo


    def _deserialize(self, params):
        self._MachineName = params.get("MachineName")
        self._MachineOs = params.get("MachineOs")
        self._MachineStatus = params.get("MachineStatus")
        self._Uuid = params.get("Uuid")
        self._Quuid = params.get("Quuid")
        self._VulNum = params.get("VulNum")
        self._MachineIp = params.get("MachineIp")
        self._IsProVersion = params.get("IsProVersion")
        self._MachineWanIp = params.get("MachineWanIp")
        self._PayMode = params.get("PayMode")
        self._MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._BaselineNum = params.get("BaselineNum")
        self._CyberAttackNum = params.get("CyberAttackNum")
        self._SecurityStatus = params.get("SecurityStatus")
        self._InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineTag(AbstractModel):
    """Server tag information

    """

    def __init__(self):
        r"""
        :param _Rid: Associated tag ID
        :type Rid: int
        :param _Name: Tag name
        :type Name: str
        :param _TagId: Tag ID
        :type TagId: int
        """
        self._Rid = None
        self._Name = None
        self._TagId = None

    @property
    def Rid(self):
        """Associated tag ID
        :rtype: int
        """
        return self._Rid

    @Rid.setter
    def Rid(self, Rid):
        self._Rid = Rid

    @property
    def Name(self):
        """Tag name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagId(self):
        """Tag ID
        :rtype: int
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._Rid = params.get("Rid")
        self._Name = params.get("Name")
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaliciousRequest(AbstractModel):
    """Malicious request data.

    """

    def __init__(self):
        r"""
        :param _Id: Record ID.
        :type Id: int
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _Domain: Malicious request domain name.
        :type Domain: str
        :param _Count: Number of malicious requests.
        :type Count: int
        :param _ProcessName: Process name.
        :type ProcessName: str
        :param _Status: Record status.
<li>UN_OPERATED: to be processed</li>
<li>TRUSTED: trusted</li>
<li>UN_TRUSTED: untrusted</li>
        :type Status: str
        :param _Description: Malicious request domain name description.
        :type Description: str
        :param _Reference: Reference address.
        :type Reference: str
        :param _CreateTime: Discovery time.
        :type CreateTime: str
        :param _MergeTime: Record merge time.
        :type MergeTime: str
        :param _ProcessMd5: Process MD5
Value.
        :type ProcessMd5: str
        :param _CmdLine: Executed command line.
        :type CmdLine: str
        :param _Pid: Process `PID`.
        :type Pid: int
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Domain = None
        self._Count = None
        self._ProcessName = None
        self._Status = None
        self._Description = None
        self._Reference = None
        self._CreateTime = None
        self._MergeTime = None
        self._ProcessMd5 = None
        self._CmdLine = None
        self._Pid = None

    @property
    def Id(self):
        """Record ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Domain(self):
        """Malicious request domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Count(self):
        """Number of malicious requests.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ProcessName(self):
        """Process name.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Status(self):
        """Record status.
<li>UN_OPERATED: to be processed</li>
<li>TRUSTED: trusted</li>
<li>UN_TRUSTED: untrusted</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        """Malicious request domain name description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Reference(self):
        """Reference address.
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def CreateTime(self):
        """Discovery time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MergeTime(self):
        """Record merge time.
        :rtype: str
        """
        return self._MergeTime

    @MergeTime.setter
    def MergeTime(self, MergeTime):
        self._MergeTime = MergeTime

    @property
    def ProcessMd5(self):
        """Process MD5
Value.
        :rtype: str
        """
        return self._ProcessMd5

    @ProcessMd5.setter
    def ProcessMd5(self, ProcessMd5):
        self._ProcessMd5 = ProcessMd5

    @property
    def CmdLine(self):
        """Executed command line.
        :rtype: str
        """
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Pid(self):
        """Process `PID`.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Domain = params.get("Domain")
        self._Count = params.get("Count")
        self._ProcessName = params.get("ProcessName")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Reference = params.get("Reference")
        self._CreateTime = params.get("CreateTime")
        self._MergeTime = params.get("MergeTime")
        self._ProcessMd5 = params.get("ProcessMd5")
        self._CmdLine = params.get("CmdLine")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Malware(AbstractModel):
    """Trojan information

    """

    def __init__(self):
        r"""
        :param _Id: Event ID.
        :type Id: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _Status: Current trojan status.
<li>UN_OPERATED: not processed</li><li>SEGREGATED: isolated</li><li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li><li>RECOVERING: recovering</li>
        :type Status: str
        :param _FilePath: Trojan path.
        :type FilePath: str
        :param _Description: Trojan description.
        :type Description: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _FileCreateTime: Trojan file creation time.
        :type FileCreateTime: str
        :param _ModifyTime: Trojan file modification time.
        :type ModifyTime: str
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._FilePath = None
        self._Description = None
        self._MachineName = None
        self._FileCreateTime = None
        self._ModifyTime = None
        self._Uuid = None

    @property
    def Id(self):
        """Event ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        """Current trojan status.
<li>UN_OPERATED: not processed</li><li>SEGREGATED: isolated</li><li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li><li>RECOVERING: recovering</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FilePath(self):
        """Trojan path.
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Description(self):
        """Trojan description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def FileCreateTime(self):
        """Trojan file creation time.
        :rtype: str
        """
        return self._FileCreateTime

    @FileCreateTime.setter
    def FileCreateTime(self, FileCreateTime):
        self._FileCreateTime = FileCreateTime

    @property
    def ModifyTime(self):
        """Trojan file modification time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._FilePath = params.get("FilePath")
        self._Description = params.get("Description")
        self._MachineName = params.get("MachineName")
        self._FileCreateTime = params.get("FileCreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Unusual login location event ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Unusual login location event ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _Attribute: Alarm item.
<li>Offline: CWP is offline</li>
<li>Malware: trojan event</li>
<li>NonlocalLogin: unusual login location discovered</li>
<li>CrackSuccess: brute force attack succeeded</li>
        :type Attribute: str
        :param _Value: Alarm item attributes.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>
        :type Value: str
        """
        self._Attribute = None
        self._Value = None

    @property
    def Attribute(self):
        """Alarm item.
<li>Offline: CWP is offline</li>
<li>Malware: trojan event</li>
<li>NonlocalLogin: unusual login location discovered</li>
<li>CrackSuccess: brute force attack succeeded</li>
        :rtype: str
        """
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def Value(self):
        """Alarm item attributes.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Attribute = params.get("Attribute")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Auto-Activation status.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        """Auto-Activation status.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoginWhiteListRequest(AbstractModel):
    """ModifyLoginWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Whitelist rule
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self._Rules = None

    @property
    def Rules(self):
        """Whitelist rule
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = LoginWhiteListsRule()
            self._Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoginWhiteListResponse(AbstractModel):
    """ModifyLoginWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _RenewFlag: Auto-renewal flag. Valid values:
<li>NOTIFY_AND_AUTO_RENEW: notifies of expiration and auto-renews</li>
<li>NOTIFY_AND_MANUAL_RENEW: notifies of expiration but does not auto-renew</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW: does not notify of expiration or auto-renew</li>
        :type RenewFlag: str
        :param _Quuid: Unique server ID, corresponding to `uuid` for CVM or `instanceId` for BM.
        :type Quuid: str
        """
        self._RenewFlag = None
        self._Quuid = None

    @property
    def RenewFlag(self):
        """Auto-renewal flag. Valid values:
<li>NOTIFY_AND_AUTO_RENEW: notifies of expiration and auto-renews</li>
<li>NOTIFY_AND_MANUAL_RENEW: notifies of expiration but does not auto-renew</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW: does not notify of expiration or auto-renew</li>
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Quuid(self):
        """Unique server ID, corresponding to `uuid` for CVM or `instanceId` for BM.
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """Unusual login location

    """

    def __init__(self):
        r"""
        :param _Id: Event ID.
        :type Id: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _Status: Login status
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>NORMAL_LOGIN: intended login</li>
        :type Status: str
        :param _UserName: Username.
        :type UserName: str
        :param _City: City ID.
        :type City: int
        :param _Country: Country/Region ID.
        :type Country: int
        :param _Province: Province/State ID.
        :type Province: int
        :param _SrcIp: Login IP.
        :type SrcIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _LoginTime: Login time.
        :type LoginTime: str
        :param _Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self._Id = None
        self._MachineIp = None
        self._Status = None
        self._UserName = None
        self._City = None
        self._Country = None
        self._Province = None
        self._SrcIp = None
        self._MachineName = None
        self._LoginTime = None
        self._Uuid = None

    @property
    def Id(self):
        """Event ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Status(self):
        """Login status
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>NORMAL_LOGIN: intended login</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserName(self):
        """Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def City(self):
        """City ID.
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """Country/Region ID.
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province/State ID.
        :rtype: int
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def SrcIp(self):
        """Login IP.
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def LoginTime(self):
        """Login time.
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Uuid(self):
        """CWP agent `Uuid`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MachineIp = params.get("MachineIp")
        self._Status = params.get("Status")
        self._UserName = params.get("UserName")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._SrcIp = params.get("SrcIp")
        self._MachineName = params.get("MachineName")
        self._LoginTime = params.get("LoginTime")
        self._Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPort(AbstractModel):
    """Port list

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID.
        :type Id: int
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _Port: Open port number.
        :type Port: int
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _ProcessName: Process name corresponding to port.
        :type ProcessName: str
        :param _Pid: Process `Pid` corresponding to port.
        :type Pid: int
        :param _CreateTime: Record creation time.
        :type CreateTime: str
        :param _ModifyTime: Record update time.
        :type ModifyTime: str
        """
        self._Id = None
        self._Uuid = None
        self._Port = None
        self._MachineIp = None
        self._MachineName = None
        self._ProcessName = None
        self._Pid = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def Id(self):
        """Unique ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Port(self):
        """Open port number.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def ProcessName(self):
        """Process name corresponding to port.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Pid(self):
        """Process `Pid` corresponding to port.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def CreateTime(self):
        """Record creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """Record update time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._Port = params.get("Port")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._ProcessName = params.get("ProcessName")
        self._Pid = params.get("Pid")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPortStatistics(AbstractModel):
    """Port statistics list

    """

    def __init__(self):
        r"""
        :param _Port: Port number
        :type Port: int
        :param _MachineNum: Number of servers
        :type MachineNum: int
        """
        self._Port = None
        self._MachineNum = None

    @property
    def Port(self):
        """Port number
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MachineNum(self):
        """Number of servers
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion request structure.

    """

    def __init__(self):
        r"""
        :param _MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :type MachineType: str
        :param _MachineRegion: Server region
Examples: ap-guangzhou, ap-shanghai
        :type MachineRegion: str
        :param _Quuids: Server `Uuid` array.
`InstanceId` for BM or `Uuid` for CVM
        :type Quuids: list of str
        :param _ActivityId: Event ID.
        :type ActivityId: int
        """
        self._MachineType = None
        self._MachineRegion = None
        self._Quuids = None
        self._ActivityId = None

    @property
    def MachineType(self):
        """Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def MachineRegion(self):
        """Server region
Examples: ap-guangzhou, ap-shanghai
        :rtype: str
        """
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def Quuids(self):
        """Server `Uuid` array.
`InstanceId` for BM or `Uuid` for CVM
        :rtype: list of str
        """
        return self._Quuids

    @Quuids.setter
    def Quuids(self, Quuids):
        self._Quuids = Quuids

    @property
    def ActivityId(self):
        """Event ID.
        :rtype: int
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId


    def _deserialize(self, params):
        self._MachineType = params.get("MachineType")
        self._MachineRegion = params.get("MachineRegion")
        self._Quuids = params.get("Quuids")
        self._ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Place(AbstractModel):
    """Login location information

    """

    def __init__(self):
        r"""
        :param _CityId: City ID.
        :type CityId: int
        :param _ProvinceId: Province/State ID.
        :type ProvinceId: int
        :param _CountryId: Country/Region ID. Currently, only `1` (Mainland China) is supported.
        :type CountryId: int
        """
        self._CityId = None
        self._ProvinceId = None
        self._CountryId = None

    @property
    def CityId(self):
        """City ID.
        :rtype: int
        """
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId

    @property
    def ProvinceId(self):
        """Province/State ID.
        :rtype: int
        """
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def CountryId(self):
        """Country/Region ID. Currently, only `1` (Mainland China) is supported.
        :rtype: int
        """
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId


    def _deserialize(self, params):
        self._CityId = params.get("CityId")
        self._ProvinceId = params.get("ProvinceId")
        self._CountryId = params.get("CountryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Process(AbstractModel):
    """Process information.

    """

    def __init__(self):
        r"""
        :param _Id: Unique ID.
        :type Id: int
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _MachineName: Server name.
        :type MachineName: str
        :param _Pid: Process `Pid`.
        :type Pid: int
        :param _Ppid: Process `Ppid`.
        :type Ppid: int
        :param _ProcessName: Process name.
        :type ProcessName: str
        :param _Username: Process username.
        :type Username: str
        :param _Platform: OS.
<li>WIN32: Windows 32-bit</li>
<li>WIN64: Windows 64-bit</li>
<li>LINUX32: Linux 32-bit</li>
<li>LINUX64: Linux 64-bit</li>
        :type Platform: str
        :param _FullPath: Process path.
        :type FullPath: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        """
        self._Id = None
        self._Uuid = None
        self._MachineIp = None
        self._MachineName = None
        self._Pid = None
        self._Ppid = None
        self._ProcessName = None
        self._Username = None
        self._Platform = None
        self._FullPath = None
        self._CreateTime = None

    @property
    def Id(self):
        """Unique ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineName(self):
        """Server name.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def Pid(self):
        """Process `Pid`.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Ppid(self):
        """Process `Ppid`.
        :rtype: int
        """
        return self._Ppid

    @Ppid.setter
    def Ppid(self, Ppid):
        self._Ppid = Ppid

    @property
    def ProcessName(self):
        """Process name.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def Username(self):
        """Process username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Platform(self):
        """OS.
<li>WIN32: Windows 32-bit</li>
<li>WIN64: Windows 64-bit</li>
<li>LINUX32: Linux 32-bit</li>
<li>LINUX64: Linux 64-bit</li>
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def FullPath(self):
        """Process path.
        :rtype: str
        """
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath

    @property
    def CreateTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._MachineIp = params.get("MachineIp")
        self._MachineName = params.get("MachineName")
        self._Pid = params.get("Pid")
        self._Ppid = params.get("Ppid")
        self._ProcessName = params.get("ProcessName")
        self._Username = params.get("Username")
        self._Platform = params.get("Platform")
        self._FullPath = params.get("FullPath")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistics(AbstractModel):
    """Process statistics.

    """

    def __init__(self):
        r"""
        :param _ProcessName: Process name.
        :type ProcessName: str
        :param _MachineNum: Number of servers.
        :type MachineNum: int
        """
        self._ProcessName = None
        self._MachineNum = None

    @property
    def ProcessName(self):
        """Process name.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def MachineNum(self):
        """Number of servers.
        :rtype: int
        """
        return self._MachineNum

    @MachineNum.setter
    def MachineNum(self, MachineNum):
        self._MachineNum = MachineNum


    def _deserialize(self, params):
        self._ProcessName = params.get("ProcessName")
        self._MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Trojan ID array. Up to 200 IDs can be deleted at a time
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Trojan ID array. Up to 200 IDs can be deleted at a time
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessIds: Array of IDs of successfully recovered trojans.
        :type SuccessIds: list of int non-negative
        :param _FailedIds: Array of IDs of trojans failed to be recovered.
        :type FailedIds: list of int non-negative
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessIds = None
        self._FailedIds = None
        self._RequestId = None

    @property
    def SuccessIds(self):
        """Array of IDs of successfully recovered trojans.
        :rtype: list of int non-negative
        """
        return self._SuccessIds

    @SuccessIds.setter
    def SuccessIds(self, SuccessIds):
        self._SuccessIds = SuccessIds

    @property
    def FailedIds(self):
        """Array of IDs of trojans failed to be recovered.
        :rtype: list of int non-negative
        """
        return self._FailedIds

    @FailedIds.setter
    def FailedIds(self, FailedIds):
        self._FailedIds = FailedIds

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessIds = params.get("SuccessIds")
        self._FailedIds = params.get("FailedIds")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _Region: Region, such as `ap-guangzhou`, `ap-shanghai` and `ap-beijing`
        :type Region: str
        :param _RegionName: Region name, such as `South China (Guangzhou)`, `East China (Shanghai)`, and `North China (Beijing)`
        :type RegionName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RegionCode: Region code, such as `gz`, `sh`, and `bj`
        :type RegionCode: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None
        self._RegionCode = None

    @property
    def Region(self):
        """Region, such as `ap-guangzhou`, `ap-shanghai` and `ap-beijing`
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """Region name, such as `South China (Guangzhou)`, `East China (Shanghai)`, and `North China (Beijing)`
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        """Region ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionCode(self):
        """Region code, such as `gz`, `sh`, and `bj`
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._RegionCode = params.get("RegionCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Vulnerability ID.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """Vulnerability ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SecurityDynamic(AbstractModel):
    """Security event message data.

    """

    def __init__(self):
        r"""
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _EventTime: Security event occurrence time.
        :type EventTime: str
        :param _EventType: Security event type.
<li>MALWARE: trojan event</li>
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>BRUTEATTACK_SUCCESS: brute force attack succeeded</li>
<li>VUL: vulnerability</li>
<li>BASELINE: security baseline</li>
        :type EventType: str
        :param _Message: Security event message.
        :type Message: str
        :param _SecurityLevel: Security event level.
<li>RISK: severe</li>
<li>HIGH: high</li>
<li>NORMAL: medium</li>
<li>LOW: low</li>
        :type SecurityLevel: str
        """
        self._Uuid = None
        self._EventTime = None
        self._EventType = None
        self._Message = None
        self._SecurityLevel = None

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def EventTime(self):
        """Security event occurrence time.
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def EventType(self):
        """Security event type.
<li>MALWARE: trojan event</li>
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>BRUTEATTACK_SUCCESS: brute force attack succeeded</li>
<li>VUL: vulnerability</li>
<li>BASELINE: security baseline</li>
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def Message(self):
        """Security event message.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SecurityLevel(self):
        """Security event level.
<li>RISK: severe</li>
<li>HIGH: high</li>
<li>NORMAL: medium</li>
<li>LOW: low</li>
        :rtype: str
        """
        return self._SecurityLevel

    @SecurityLevel.setter
    def SecurityLevel(self, SecurityLevel):
        self._SecurityLevel = SecurityLevel


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._EventTime = params.get("EventTime")
        self._EventType = params.get("EventType")
        self._Message = params.get("Message")
        self._SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTrend(AbstractModel):
    """Security trend statistics.

    """

    def __init__(self):
        r"""
        :param _Date: Event time.
        :type Date: str
        :param _EventNum: Number of events.
        :type EventNum: int
        """
        self._Date = None
        self._EventNum = None

    @property
    def Date(self):
        """Event time.
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def EventNum(self):
        """Number of events.
        :rtype: int
        """
        return self._EventNum

    @EventNum.setter
    def EventNum(self, EventNum):
        self._EventNum = EventNum


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._EventNum = params.get("EventNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Trojan event ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Trojan event ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessIds: Array of IDs of successfully isolated trojans.
        :type SuccessIds: list of int non-negative
        :param _FailedIds: Array of IDs of trojans failed to be isolated.
        :type FailedIds: list of int non-negative
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessIds = None
        self._FailedIds = None
        self._RequestId = None

    @property
    def SuccessIds(self):
        """Array of IDs of successfully isolated trojans.
        :rtype: list of int non-negative
        """
        return self._SuccessIds

    @SuccessIds.setter
    def SuccessIds(self, SuccessIds):
        self._SuccessIds = SuccessIds

    @property
    def FailedIds(self):
        """Array of IDs of trojans failed to be isolated.
        :rtype: list of int non-negative
        """
        return self._FailedIds

    @FailedIds.setter
    def FailedIds(self, FailedIds):
        self._FailedIds = FailedIds

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessIds = params.get("SuccessIds")
        self._FailedIds = params.get("FailedIds")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag information

    """

    def __init__(self):
        r"""
        :param _Id: Tag ID
        :type Id: int
        :param _Name: Tag name
        :type Name: str
        :param _Count: Number of servers
        :type Count: int
        """
        self._Id = None
        self._Name = None
        self._Count = None

    @property
    def Id(self):
        """Tag ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Tag name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        """Number of servers
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagMachine(AbstractModel):
    """Tagged server information

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: str
        :param _Quuid: Server ID
        :type Quuid: str
        :param _MachineName: Server name
        :type MachineName: str
        :param _MachineIp: Private IP of server
        :type MachineIp: str
        :param _MachineWanIp: Public IP of server
        :type MachineWanIp: str
        :param _MachineRegion: Server region
        :type MachineRegion: str
        :param _MachineType: Server region type
        :type MachineType: str
        """
        self._Id = None
        self._Quuid = None
        self._MachineName = None
        self._MachineIp = None
        self._MachineWanIp = None
        self._MachineRegion = None
        self._MachineType = None

    @property
    def Id(self):
        """ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Quuid(self):
        """Server ID
        :rtype: str
        """
        return self._Quuid

    @Quuid.setter
    def Quuid(self, Quuid):
        self._Quuid = Quuid

    @property
    def MachineName(self):
        """Server name
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineIp(self):
        """Private IP of server
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def MachineWanIp(self):
        """Public IP of server
        :rtype: str
        """
        return self._MachineWanIp

    @MachineWanIp.setter
    def MachineWanIp(self, MachineWanIp):
        self._MachineWanIp = MachineWanIp

    @property
    def MachineRegion(self):
        """Server region
        :rtype: str
        """
        return self._MachineRegion

    @MachineRegion.setter
    def MachineRegion(self, MachineRegion):
        self._MachineRegion = MachineRegion

    @property
    def MachineType(self):
        """Server region type
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Quuid = params.get("Quuid")
        self._MachineName = params.get("MachineName")
        self._MachineIp = params.get("MachineIp")
        self._MachineWanIp = params.get("MachineWanIp")
        self._MachineRegion = params.get("MachineRegion")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Malicious request record ID.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """Malicious request record ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Trojan ID array.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Trojan ID array.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Trusted record ID.
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """Trusted record ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Trojan event ID array. Up to 200 IDs can be processed at a time.
        :type Ids: list of int non-negative
        """
        self._Ids = None

    @property
    def Ids(self):
        """Trojan event ID array. Up to 200 IDs can be processed at a time.
        :rtype: list of int non-negative
        """
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """Usual login location

    """

    def __init__(self):
        r"""
        :param _Id: ID.
        :type Id: int
        :param _Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param _CountryId: Country/Region ID.
        :type CountryId: int
        :param _ProvinceId: Province/State ID.
        :type ProvinceId: int
        :param _CityId: City ID.
        :type CityId: int
        """
        self._Id = None
        self._Uuid = None
        self._CountryId = None
        self._ProvinceId = None
        self._CityId = None

    @property
    def Id(self):
        """ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uuid(self):
        """CWP agent `UUID`.
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def CountryId(self):
        """Country/Region ID.
        :rtype: int
        """
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId

    @property
    def ProvinceId(self):
        """Province/State ID.
        :rtype: int
        """
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def CityId(self):
        """City ID.
        :rtype: int
        """
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uuid = params.get("Uuid")
        self._CountryId = params.get("CountryId")
        self._ProvinceId = params.get("ProvinceId")
        self._CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vul(AbstractModel):
    """Vulnerability list data

    """

    def __init__(self):
        r"""
        :param _VulId: Vulnerability category ID
        :type VulId: int
        :param _VulName: Vulnerability name
        :type VulName: str
        :param _VulLevel: Vulnerability severity level:
HIGH: high
MIDDLE: medium
LOW: low
NOTICE: notice
        :type VulLevel: str
        :param _LastScanTime: Last scanned time
        :type LastScanTime: str
        :param _ImpactedHostNum: Number of affected servers
        :type ImpactedHostNum: int
        :param _VulStatus: Vulnerability status
* UN_OPERATED: to be processed
* FIXED: fixed
        :type VulStatus: str
        """
        self._VulId = None
        self._VulName = None
        self._VulLevel = None
        self._LastScanTime = None
        self._ImpactedHostNum = None
        self._VulStatus = None

    @property
    def VulId(self):
        """Vulnerability category ID
        :rtype: int
        """
        return self._VulId

    @VulId.setter
    def VulId(self, VulId):
        self._VulId = VulId

    @property
    def VulName(self):
        """Vulnerability name
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulLevel(self):
        """Vulnerability severity level:
HIGH: high
MIDDLE: medium
LOW: low
NOTICE: notice
        :rtype: str
        """
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def LastScanTime(self):
        """Last scanned time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ImpactedHostNum(self):
        """Number of affected servers
        :rtype: int
        """
        return self._ImpactedHostNum

    @ImpactedHostNum.setter
    def ImpactedHostNum(self, ImpactedHostNum):
        self._ImpactedHostNum = ImpactedHostNum

    @property
    def VulStatus(self):
        """Vulnerability status
* UN_OPERATED: to be processed
* FIXED: fixed
        :rtype: str
        """
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus


    def _deserialize(self, params):
        self._VulId = params.get("VulId")
        self._VulName = params.get("VulName")
        self._VulLevel = params.get("VulLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._ImpactedHostNum = params.get("ImpactedHostNum")
        self._VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReport(AbstractModel):
    """Weekly report list.

    """

    def __init__(self):
        r"""
        :param _BeginDate: Weekly report start time.
        :type BeginDate: str
        :param _EndDate: Weekly report end time.
        :type EndDate: str
        """
        self._BeginDate = None
        self._EndDate = None

    @property
    def BeginDate(self):
        """Weekly report start time.
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """Weekly report end time.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportBruteAttack(AbstractModel):
    """Brute force attack data in weekly CWP Pro report.

    """

    def __init__(self):
        r"""
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _Username: Hacked username.
        :type Username: str
        :param _SrcIp: Source IP.
        :type SrcIp: str
        :param _Count: Number of attempts.
        :type Count: int
        :param _AttackTime: Attack time.
        :type AttackTime: str
        """
        self._MachineIp = None
        self._Username = None
        self._SrcIp = None
        self._Count = None
        self._AttackTime = None

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Username(self):
        """Hacked username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SrcIp(self):
        """Source IP.
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Count(self):
        """Number of attempts.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AttackTime(self):
        """Attack time.
        :rtype: str
        """
        return self._AttackTime

    @AttackTime.setter
    def AttackTime(self, AttackTime):
        self._AttackTime = AttackTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._Username = params.get("Username")
        self._SrcIp = params.get("SrcIp")
        self._Count = params.get("Count")
        self._AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportMalware(AbstractModel):
    """Trojan data in weekly CWP Pro report.

    """

    def __init__(self):
        r"""
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _FilePath: Trojan file path.
        :type FilePath: str
        :param _Md5: Trojan file MD5 value.
        :type Md5: str
        :param _FindTime: Trojan discovery time.
        :type FindTime: str
        :param _Status: Current trojan status.
<li>UN_OPERATED: not processed</li>
<li>SEGREGATED: isolated</li>
<li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li>
<li>RECOVERING: recovering</li>
        :type Status: str
        """
        self._MachineIp = None
        self._FilePath = None
        self._Md5 = None
        self._FindTime = None
        self._Status = None

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def FilePath(self):
        """Trojan file path.
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Md5(self):
        """Trojan file MD5 value.
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def FindTime(self):
        """Trojan discovery time.
        :rtype: str
        """
        return self._FindTime

    @FindTime.setter
    def FindTime(self, FindTime):
        self._FindTime = FindTime

    @property
    def Status(self):
        """Current trojan status.
<li>UN_OPERATED: not processed</li>
<li>SEGREGATED: isolated</li>
<li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li>
<li>RECOVERING: recovering</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._FilePath = params.get("FilePath")
        self._Md5 = params.get("Md5")
        self._FindTime = params.get("FindTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """Unusual login location data in weekly CWP Pro report

    """

    def __init__(self):
        r"""
        :param _MachineIp: Server IP.
        :type MachineIp: str
        :param _Username: Username.
        :type Username: str
        :param _SrcIp: Source IP.
        :type SrcIp: str
        :param _Country: Country/Region ID.
        :type Country: int
        :param _Province: Province/State ID.
        :type Province: int
        :param _City: City ID.
        :type City: int
        :param _LoginTime: Login time.
        :type LoginTime: str
        """
        self._MachineIp = None
        self._Username = None
        self._SrcIp = None
        self._Country = None
        self._Province = None
        self._City = None
        self._LoginTime = None

    @property
    def MachineIp(self):
        """Server IP.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def Username(self):
        """Username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SrcIp(self):
        """Source IP.
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Country(self):
        """Country/Region ID.
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """Province/State ID.
        :rtype: int
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """City ID.
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def LoginTime(self):
        """Login time.
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._Username = params.get("Username")
        self._SrcIp = params.get("SrcIp")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._LoginTime = params.get("LoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportVul(AbstractModel):
    """Vulnerability data in weekly CWP Pro report.

    """

    def __init__(self):
        r"""
        :param _MachineIp: Private IP of server.
        :type MachineIp: str
        :param _VulName: Vulnerability name.
        :type VulName: str
        :param _VulType: Vulnerability type.
<li> WEB: web vulnerability</li>
<li> SYSTEM: system component vulnerability</li>
<li> BASELINE: security baseline</li>
        :type VulType: str
        :param _Description: Vulnerability description.
        :type Description: str
        :param _VulStatus: Vulnerability status.
<li> UN_OPERATED: to be processed</li>
<li> SCANING: scanning</li>
<li> FIXED: fixed</li>
        :type VulStatus: str
        :param _LastScanTime: Last scanned time.
        :type LastScanTime: str
        """
        self._MachineIp = None
        self._VulName = None
        self._VulType = None
        self._Description = None
        self._VulStatus = None
        self._LastScanTime = None

    @property
    def MachineIp(self):
        """Private IP of server.
        :rtype: str
        """
        return self._MachineIp

    @MachineIp.setter
    def MachineIp(self, MachineIp):
        self._MachineIp = MachineIp

    @property
    def VulName(self):
        """Vulnerability name.
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulType(self):
        """Vulnerability type.
<li> WEB: web vulnerability</li>
<li> SYSTEM: system component vulnerability</li>
<li> BASELINE: security baseline</li>
        :rtype: str
        """
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def Description(self):
        """Vulnerability description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VulStatus(self):
        """Vulnerability status.
<li> UN_OPERATED: to be processed</li>
<li> SCANING: scanning</li>
<li> FIXED: fixed</li>
        :rtype: str
        """
        return self._VulStatus

    @VulStatus.setter
    def VulStatus(self, VulStatus):
        self._VulStatus = VulStatus

    @property
    def LastScanTime(self):
        """Last scanned time.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime


    def _deserialize(self, params):
        self._MachineIp = params.get("MachineIp")
        self._VulName = params.get("VulName")
        self._VulType = params.get("VulType")
        self._Description = params.get("Description")
        self._VulStatus = params.get("VulStatus")
        self._LastScanTime = params.get("LastScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        