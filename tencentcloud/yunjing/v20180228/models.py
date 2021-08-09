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
        """
        :param Id: Unique ID.\n        :type Id: int\n        :param Uuid: CWP agent `Uuid`\n        :type Uuid: str\n        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param Username: Account name.\n        :type Username: str\n        :param Groups: Account group.\n        :type Groups: str\n        :param Privilege: Account type.
<li>ORDINARY: ordinary account</li>
<li>SUPPER: super admin account</li>\n        :type Privilege: str\n        :param AccountCreateTime: Account creation time.\n        :type AccountCreateTime: str\n        :param LastLoginTime: Account last login time.\n        :type LastLoginTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.Groups = None
        self.Privilege = None
        self.AccountCreateTime = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.Groups = params.get("Groups")
        self.Privilege = params.get("Privilege")
        self.AccountCreateTime = params.get("AccountCreateTime")
        self.LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountStatistics(AbstractModel):
    """Account statistics.

    """

    def __init__(self):
        """
        :param Username: Username.\n        :type Username: str\n        :param MachineNum: Number of servers.\n        :type MachineNum: int\n        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListRequest(AbstractModel):
    """AddLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Rules: Whitelist rule\n        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`\n        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLoginWhiteListResponse(AbstractModel):
    """AddLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddMachineTagRequest(AbstractModel):
    """AddMachineTag request structure.

    """

    def __init__(self):
        """
        :param Quuid: Server ID\n        :type Quuid: str\n        :param TagId: Tag ID\n        :type TagId: int\n        :param MRegion: Server region\n        :type MRegion: str\n        :param MArea: Server type (`CVM` or `BM`)\n        :type MArea: str\n        """
        self.Quuid = None
        self.TagId = None
        self.MRegion = None
        self.MArea = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.TagId = params.get("TagId")
        self.MRegion = params.get("MRegion")
        self.MArea = params.get("MArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineTagResponse(AbstractModel):
    """AddMachineTag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AgentVul(AbstractModel):
    """Server vulnerability information

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.\n        :type Id: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param VulName: Vulnerability name.\n        :type VulName: str\n        :param VulLevel: Vulnerability severity level.
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
<li>NOTICE: notice</li>\n        :type VulLevel: str\n        :param LastScanTime: Last scanned time.\n        :type LastScanTime: str\n        :param Description: Vulnerability description.\n        :type Description: str\n        :param VulId: Vulnerability category ID.\n        :type VulId: int\n        :param VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>FIXED: fixed</li>\n        :type VulStatus: str\n        """
        self.Id = None
        self.MachineIp = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.Description = None
        self.VulId = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttack(AbstractModel):
    """Brute force attack list

    """

    def __init__(self):
        """
        :param Id: Event ID.\n        :type Id: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param Status: Brute force attack event status
<li>BRUTEATTACK_FAIL_ACCOUNT: brute force attack event - failure (the account exists)</li>
<li>BRUTEATTACK_FAIL_NOACCOUNT: brute force attack event - failure (the account does not exist)</li>
<li>BRUTEATTACK_SUCCESS: brute force attack event - success </li>\n        :type Status: str\n        :param UserName: Username.\n        :type UserName: str\n        :param City: City ID.\n        :type City: int\n        :param Country: Country/Region ID.\n        :type Country: int\n        :param Province: Province/State ID.\n        :type Province: int\n        :param SrcIp: Source IP.\n        :type SrcIp: str\n        :param Count: Number of attempts.\n        :type Count: int\n        :param CreateTime: Occurrence time.\n        :type CreateTime: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param IsProVersion: Whether the server enables CWP Pro.\n        :type IsProVersion: bool\n        :param BanStatus: Whether the server is banned.\n        :type BanStatus: str\n        :param Quuid: Server `UUID`\n        :type Quuid: str\n        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.Count = None
        self.CreateTime = None
        self.MachineName = None
        self.Uuid = None
        self.IsProVersion = None
        self.BanStatus = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.BanStatus = params.get("BanStatus")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion request structure.

    """

    def __init__(self):
        """
        :param Quuid: Server `Uuid`.
`InstanceId` for BM or `Uuid` for CVM\n        :type Quuid: str\n        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """Component list data.

    """

    def __init__(self):
        """
        :param Id: Unique ID.\n        :type Id: int\n        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param ComponentVersion: Component version number.\n        :type ComponentVersion: str\n        :param ComponentType: Component type.
<li>SYSTEM: system component</li>
<li>WEB: web component</li>\n        :type ComponentType: str\n        :param ComponentName: Component name.\n        :type ComponentName: str\n        :param ModifyTime: Component detection update time.\n        :type ModifyTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.ComponentVersion = None
        self.ComponentType = None
        self.ComponentName = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ComponentVersion = params.get("ComponentVersion")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentStatistics(AbstractModel):
    """Component statistics.

    """

    def __init__(self):
        """
        :param Id: Component ID.\n        :type Id: int\n        :param MachineNum: Number of servers.\n        :type MachineNum: int\n        :param ComponentName: Component name.\n        :type ComponentName: str\n        :param ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>\n        :type ComponentType: str\n        :param Description: Component description.\n        :type Description: str\n        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenPortTaskRequest(AbstractModel):
    """CreateOpenPortTask request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenPortTaskResponse(AbstractModel):
    """CreateOpenPortTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuids: CWP agent `UUID` array.\n        :type Uuids: list of str\n        :param Places: Login region information array.\n        :type Places: list of Place\n        """
        self.Uuids = None
        self.Places = None


    def _deserialize(self, params):
        self.Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks request structure.

    """

    def __init__(self):
        """
        :param Ids: Brute force attack event ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Ids: Whitelist ID\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag request structure.

    """

    def __init__(self):
        """
        :param Rid: Associated tag ID\n        :type Rid: int\n        """
        self.Rid = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests request structure.

    """

    def __init__(self):
        """
        :param Ids: Malicious request record ID array. Maximum value: 100 entries.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan record ID array\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Ids: Unusual login location event ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`\n        :type Uuid: str\n        :param CityIds: Added usual login city ID array\n        :type CityIds: list of int non-negative\n        """
        self.Uuid = None
        self.CityIds = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.CityIds = params.get("CityIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Username - String - Required: No - Account username</li>\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account statistics list.\n        :type TotalCount: int\n        :param AccountStatistics: Account statistics list.\n        :type AccountStatistics: list of AccountStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.\n        :type Uuid: str\n        :param Username: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Username` is specified, it indicates to query the information list under the specified username.\n        :type Username: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Username - String - Required: No - Account name</li>
<li>Privilege - String - Required: No - Account name (ORDINARY: ordinary account, SUPPER: super admin account)</li>
<li>MachineIp - String - Required: No - Private IP of server</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.Username = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Username = params.get("Username")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account list.\n        :type TotalCount: int\n        :param Accounts: Account data list.\n        :type Accounts: list of Account\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls request structure.

    """

    def __init__(self):
        """
        :param VulType: Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>\n        :type VulType: str\n        :param Uuid: Agent `UUID`.\n        :type Uuid: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)\n        :type Filters: list of Filter\n        """
        self.VulType = None
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records\n        :type TotalCount: int\n        :param AgentVuls: Server vulnerability information\n        :type AgentVuls: list of AgentVul\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AgentVuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self.AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self.AgentVuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute request structure.

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute response structure.

    """

    def __init__(self):
        """
        :param Offline: CWP deactivation alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>\n        :type Offline: str\n        :param Malware: Trojan discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>\n        :type Malware: str\n        :param NonlocalLogin: Unusual login location discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>\n        :type NonlocalLogin: str\n        :param CrackSuccess: Brute force attack success alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>\n        :type CrackSuccess: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Offline = None
        self.Malware = None
        self.NonlocalLogin = None
        self.CrackSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offline = params.get("Offline")
        self.Malware = params.get("Malware")
        self.NonlocalLogin = params.get("NonlocalLogin")
        self.CrackSuccess = params.get("CrackSuccess")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks request structure.

    """

    def __init__(self):
        """
        :param Uuid: Agent `Uuid`.\n        :type Uuid: str\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Query status (FAILED: brute force attack failed, SUCCESS: brute force attack succeeded)</li>\n        :type Filters: list of Filter\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        """
        self.Uuid = None
        self.Offset = None
        self.Filters = None
        self.Limit = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of events\n        :type TotalCount: int\n        :param BruteAttacks: Brute force attack event list\n        :type BruteAttacks: list of BruteAttack\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.BruteAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo request structure.

    """

    def __init__(self):
        """
        :param ComponentId: Component ID.\n        :type ComponentId: int\n        """
        self.ComponentId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo response structure.

    """

    def __init__(self):
        """
        :param Id: Component ID.\n        :type Id: int\n        :param ComponentName: Component name.\n        :type ComponentName: str\n        :param ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>\n        :type ComponentType: str\n        :param Homepage: Component's official website.\n        :type Homepage: str\n        :param Description: Component description.\n        :type Description: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Id = None
        self.ComponentName = None
        self.ComponentType = None
        self.Homepage = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Homepage = params.get("Homepage")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
ComponentName - String - Required: No - Component name\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in component statistics list.\n        :type TotalCount: int\n        :param ComponentStatistics: Component statistics list data array.\n        :type ComponentStatistics: list of ComponentStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`. Either `Uuid` or `ComponentId` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.\n        :type Uuid: str\n        :param ComponentId: Component ID. Either `Uuid` or `ComponentId` must be specified. If `ComponentId` is specified, it indicates to query the information list under the specified component.\n        :type ComponentId: int\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>ComponentVersion - String - Required: No - Component version number</li>
<li>MachineIp - String - Required: No - Private IP of server</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.ComponentId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ComponentId = params.get("ComponentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in component list.\n        :type TotalCount: int\n        :param Components: Component list data.\n        :type Components: list of Component\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Components = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Username - String - Required: No - Account name</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account change history list.\n        :type TotalCount: int\n        :param HistoryAccounts: Account change history data array.\n        :type HistoryAccounts: list of HistoryAccount\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts request structure.

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID.\n        :type VulId: int\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)</li>\n        :type Filters: list of Filter\n        """
        self.VulId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records\n        :type TotalCount: int\n        :param ImpactedHosts: Affected server list array\n        :type ImpactedHosts: list of ImpactedHost\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ImpactedHosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self.ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self.ImpactedHosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records\n        :type TotalCount: int\n        :param LoginWhiteLists: Login allowlist array\n        :type LoginWhiteLists: list of LoginWhiteLists\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.LoginWhiteLists = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self.LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self.LoginWhiteLists.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo response structure.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param ProtectDays: Days under protection by CWP\n        :type ProtectDays: int\n        :param MachineOs: OS.\n        :type MachineOs: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param MachineStatus: Status.
<li>ONLINE: online</li>
<li>OFFLINE: offline</li>\n        :type MachineStatus: str\n        :param InstanceId: Unique ID of CVM or BM instance.\n        :type InstanceId: str\n        :param MachineWanIp: Public IP of server.\n        :type MachineWanIp: str\n        :param Quuid: CVM or BM instance `Uuid`.\n        :type Quuid: str\n        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        :param IsProVersion: Whether CWP Pro is activated.
<li>true: yes</li>
<li>false: no</li>\n        :type IsProVersion: bool\n        :param ProVersionOpenDate: CWP Pro activation time.\n        :type ProVersionOpenDate: str\n        :param MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>\n        :type MachineType: str\n        :param MachineRegion: Server region, such as ap-guangzhou or ap-shanghai\n        :type MachineRegion: str\n        :param PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>\n        :type PayMode: str\n        :param FreeMalwaresLeft: Number of trojans left for free scan.\n        :type FreeMalwaresLeft: int\n        :param FreeVulsLeft: Number of vulnerability left for free scan.\n        :type FreeVulsLeft: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.FreeMalwaresLeft = None
        self.FreeVulsLeft = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self.FreeVulsLeft = params.get("FreeVulsLeft")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines request structure.

    """

    def __init__(self):
        """
        :param MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>\n        :type MachineType: str\n        :param MachineRegion: Server region, such as ap-guangzhou or ap-shanghai\n        :type MachineRegion: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Keywords - String - Required: no - Query keywords </li>
<li>Status - String - Required: no - CWP client status (valid values: OFFLINE, ONLINE, UNINSTALLED)</li>
<li>Version - String - Required: no - Current CWP version (valid values: PRO_VERSION, BASIC_VERSION)</li>
Each filter can have only one value but does not support "OR" queries with multiple values\n        :type Filters: list of Filter\n        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines response structure.

    """

    def __init__(self):
        """
        :param Machines: Server list\n        :type Machines: list of Machine\n        :param TotalCount: Number of servers\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMaliciousRequestsRequest(AbstractModel):
    """DescribeMaliciousRequests request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, TRUSTED: trusted, UN_TRUSTED: untrusted)</li>
<li>Domain - String - Required: No - Malicious request domain name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>\n        :type Filters: list of Filter\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param MaliciousRequests: Malicious request record array.\n        :type MaliciousRequests: list of MaliciousRequest\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.MaliciousRequests = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = MaliciousRequest()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares request structure.

    """

    def __init__(self):
        """
        :param Uuid: Agent `Uuid`.\n        :type Uuid: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Trojan status (UN_OPERATED: not processed, SEGREGATED: isolated, TRUSTED: trusted)</li>
Each filter supports only one value. Query with multiple values in "OR" relationship is not supported for the time being.\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of trojans.\n        :type TotalCount: int\n        :param Malwares: Malware array.\n        :type Malwares: list of Malware\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Malwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self.Malwares.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuid: Agent `Uuid`.\n        :type Uuid: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Login status (NON_LOCAL_LOGIN: unusual login location, NORMAL_LOGIN: intended login)</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param NonLocalLoginPlaces: Unusual login location information array.\n        :type NonLocalLoginPlaces: list of NonLocalLoginPlace\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.NonLocalLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in port statistics list\n        :type TotalCount: int\n        :param OpenPortStatistics: Port statistics list\n        :type OpenPortStatistics: list of OpenPortStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortTaskStatusRequest(AbstractModel):
    """DescribeOpenPortTaskStatus request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortTaskStatusResponse(AbstractModel):
    """DescribeOpenPortTaskStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeOpenPorts` API to get the list of real-time processes) </li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting port</li>
<li>FAILED: failed to get processes</li>\n        :type Status: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`. Either `Port` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.\n        :type Uuid: str\n        :param Port: Open port number. Either `Port` or `Uuid` must be specified. If `Port` is specified, it indicates to query the information list under the specified port.\n        :type Port: int\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.Port = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in port list.\n        :type TotalCount: int\n        :param OpenPorts: Port list.\n        :type OpenPorts: list of OpenPort\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.OpenPorts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self.OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self.OpenPorts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics request structure.

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics response structure.

    """

    def __init__(self):
        """
        :param OnlineMachineNum: Number of online servers.\n        :type OnlineMachineNum: int\n        :param ProVersionMachineNum: Number of servers activated CWP Pro.\n        :type ProVersionMachineNum: int\n        :param MalwareNum: Number of trojan files.\n        :type MalwareNum: int\n        :param NonlocalLoginNum: Number of unusual login locations.\n        :type NonlocalLoginNum: int\n        :param BruteAttackSuccessNum: Number of successful brute force attacks.\n        :type BruteAttackSuccessNum: int\n        :param VulNum: Number of vulnerabilities.\n        :type VulNum: int\n        :param BaseLineNum: Security baseline number\n        :type BaseLineNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo request structure.

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo response structure.

    """

    def __init__(self):
        """
        :param PostPayCost: Fee on yesterday (pay-as-you-go)\n        :type PostPayCost: int\n        :param IsAutoOpenProVersion: Whether CWP Pro is activated for new servers\n        :type IsAutoOpenProVersion: bool\n        :param ProVersionNum: Number of servers on CWP Pro\n        :type ProVersionNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>\n        :type Filters: list of Filter\n        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in process statistics list.\n        :type TotalCount: int\n        :param ProcessStatistics: Process statistics list array.\n        :type ProcessStatistics: list of ProcessStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeProcesses` API to get the list of real-time processes)</li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting process</li>
<li>FAILED: failed to get processes</li>\n        :type Status: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`. Either `Uuid` or `ProcessName` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.\n        :type Uuid: str\n        :param ProcessName: Process name. Either `Uuid` or `ProcessName` must be specified. If `ProcessName` is specified, it indicates to query the information list under the specified process.\n        :type ProcessName: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>\n        :type Filters: list of Filter\n        """
        self.Uuid = None
        self.ProcessName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in process list.\n        :type TotalCount: int\n        :param Processes: Process list data array.\n        :type Processes: list of Process\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Processes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self.Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self.Processes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics response structure.

    """

    def __init__(self):
        """
        :param SecurityDynamics: Security event message array.\n        :type SecurityDynamics: list of SecurityDynamic\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Start time.\n        :type BeginDate: str\n        :param EndDate: End time.\n        :type EndDate: str\n        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends response structure.

    """

    def __init__(self):
        """
        :param Malwares: Trojan event statistics array.\n        :type Malwares: list of SecurityTrend\n        :param NonLocalLoginPlaces: Unusual login location event statistics array.\n        :type NonLocalLoginPlaces: list of SecurityTrend\n        :param BruteAttacks: Brute force attack event statistics array.\n        :type BruteAttacks: list of SecurityTrend\n        :param Vuls: Vulnerability statistics array.\n        :type Vuls: list of SecurityTrend\n        :param BaseLines: Baseline statistics array.\n        :type BaseLines: list of SecurityTrend\n        :param MaliciousRequests: Statistics array of malicious requests.\n        :type MaliciousRequests: list of SecurityTrend\n        :param HighRiskBashs: Statistics array of high-risk commands.\n        :type HighRiskBashs: list of SecurityTrend\n        :param ReverseShells: Statistics array of reverse shells.\n        :type ReverseShells: list of SecurityTrend\n        :param PrivilegeEscalations: Statistics array of local privilege escalations.\n        :type PrivilegeEscalations: list of SecurityTrend\n        :param CyberAttacks: Statistics array of network attacks.\n        :type CyberAttacks: list of SecurityTrend\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.MaliciousRequests = None
        self.HighRiskBashs = None
        self.ReverseShells = None
        self.PrivilegeEscalations = None
        self.CyberAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self.HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self.ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self.PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self.CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.CyberAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines request structure.

    """

    def __init__(self):
        """
        :param Id: Tag ID\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines response structure.

    """

    def __init__(self):
        """
        :param List: List data\n        :type List: list of TagMachine\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags request structure.

    """

    def __init__(self):
        """
        :param MachineType: CVM instance type.
<li>CVM: CVM</li>
<li>BM: CPM</li>\n        :type MachineType: str\n        :param MachineRegion: Server region, such as `ap-guangzhou` and `ap-shanghai`\n        :type MachineRegion: str\n        """
        self.MachineType = None
        self.MachineRegion = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags response structure.

    """

    def __init__(self):
        """
        :param List: List information\n        :type List: list of Tag\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `UUID`\n        :type Uuid: str\n        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: Usual login location array\n        :type UsualLoginPlaces: list of UsualPlace\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo request structure.

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID.\n        :type VulId: int\n        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo response structure.

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID.\n        :type VulId: int\n        :param VulName: Vulnerability name.\n        :type VulName: str\n        :param VulLevel: Vulnerability level.\n        :type VulLevel: str\n        :param VulType: Vulnerability type.\n        :type VulType: str\n        :param Description: Vulnerability description.\n        :type Description: str\n        :param RepairPlan: Repair plan.\n        :type RepairPlan: str\n        :param CveId: Vulnerability CVE.\n        :type CveId: str\n        :param Reference: Reference link.\n        :type Reference: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.VulType = None
        self.Description = None
        self.RepairPlan = None
        self.CveId = None
        self.Reference = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.RepairPlan = params.get("RepairPlan")
        self.CveId = params.get("CveId")
        self.Reference = params.get("Reference")
        self.RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult request structure.

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult response structure.

    """

    def __init__(self):
        """
        :param VulNum: Number of vulnerabilities.\n        :type VulNum: int\n        :param ProVersionNum: Number of servers activated CWP Pro\n        :type ProVersionNum: int\n        :param ImpactedHostNum: Number of affected activated CWP Pro.\n        :type ImpactedHostNum: int\n        :param HostNum: Total number of servers.\n        :type HostNum: int\n        :param BasicVersionNum: Number of servers on CWP Basic.\n        :type BasicVersionNum: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.VulNum = None
        self.ProVersionNum = None
        self.ImpactedHostNum = None
        self.HostNum = None
        self.BasicVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulNum = params.get("VulNum")
        self.ProVersionNum = params.get("ProVersionNum")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.HostNum = params.get("HostNum")
        self.BasicVersionNum = params.get("BasicVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls request structure.

    """

    def __init__(self):
        """
        :param VulType: Vulnerability type.
<li>WEB: web application vulnerability</li>
<li>SYSTEM: system component vulnerability</li>
<li>BASELINE: security baseline</li>\n        :type VulType: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)

Only one value is allowed for the `Status` filter, and "OR" logic is not supported.\n        :type Filters: list of Filter\n        """
        self.VulType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of vulnerabilities.\n        :type TotalCount: int\n        :param Vuls: Vulnerability list array.\n        :type Vuls: list of Vul\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly CWP Pro report start time.\n        :type BeginDate: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportBruteAttacks: Brute force attack array in weekly CWP Pro report.\n        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WeeklyReportBruteAttacks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportBruteAttacks") is not None:
            self.WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self.WeeklyReportBruteAttacks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly CWP Pro report start time.\n        :type BeginDate: str\n        """
        self.BeginDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo response structure.

    """

    def __init__(self):
        """
        :param CompanyName: Account owner name.\n        :type CompanyName: str\n        :param MachineNum: Total number of servers.\n        :type MachineNum: int\n        :param OnlineMachineNum: Number of online CWP agents\n        :type OnlineMachineNum: int\n        :param OfflineMachineNum: Number of offline CWP agents.\n        :type OfflineMachineNum: int\n        :param ProVersionMachineNum: Number of servers on CWP Pro.\n        :type ProVersionMachineNum: int\n        :param BeginDate: Weekly report start time\n        :type BeginDate: str\n        :param EndDate: Weekly report end time\n        :type EndDate: str\n        :param Level: Security level
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>\n        :type Level: str\n        :param MalwareNum: Number of trojan records.\n        :type MalwareNum: int\n        :param NonlocalLoginNum: Number of unusual login locations.\n        :type NonlocalLoginNum: int\n        :param BruteAttackSuccessNum: Number of successful brute force attacks.\n        :type BruteAttackSuccessNum: int\n        :param VulNum: Number of vulnerabilities.\n        :type VulNum: int\n        :param DownloadUrl: Download address for exported file.\n        :type DownloadUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CompanyName = None
        self.MachineNum = None
        self.OnlineMachineNum = None
        self.OfflineMachineNum = None
        self.ProVersionMachineNum = None
        self.BeginDate = None
        self.EndDate = None
        self.Level = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.MachineNum = params.get("MachineNum")
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.OfflineMachineNum = params.get("OfflineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.Level = params.get("Level")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly CWP Pro report start time.\n        :type BeginDate: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportMalwares: Trojan data in weekly CWP Pro report.\n        :type WeeklyReportMalwares: list of WeeklyReportMalware\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WeeklyReportMalwares = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportMalwares") is not None:
            self.WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self.WeeklyReportMalwares.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly CWP Pro report start time.\n        :type BeginDate: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportNonlocalLoginPlaces: Unusual login location data in weekly CWP Pro report\n        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WeeklyReportNonlocalLoginPlaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self.WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self.WeeklyReportNonlocalLoginPlaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls request structure.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly CWP Pro report start time.\n        :type BeginDate: str\n        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportVuls: Vulnerability data array in weekly CWP Pro report.\n        :type WeeklyReportVuls: list of WeeklyReportVul\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WeeklyReportVuls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportVuls") is not None:
            self.WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self.WeeklyReportVuls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.\n        :type Limit: int\n        :param Offset: Offset. Default value: 0.\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports response structure.

    """

    def __init__(self):
        """
        :param WeeklyReports: Weekly CWP Pro report list array.\n        :type WeeklyReports: list of WeeklyReport\n        :param TotalCount: Total number of records.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WeeklyReports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReports") is not None:
            self.WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self.WeeklyReports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class EditTagsRequest(AbstractModel):
    """EditTags request structure.

    """

    def __init__(self):
        """
        :param Name: Tag name\n        :type Name: str\n        :param Id: Tag ID\n        :type Id: int\n        :param Quuids: CVM instance ID\n        :type Quuids: list of str\n        """
        self.Name = None
        self.Id = None
        self.Quuids = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditTagsResponse(AbstractModel):
    """EditTags response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks request structure.

    """


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param DownloadUrl: Download address for exported file.\n        :type DownloadUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests request structure.

    """


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests response structure.

    """

    def __init__(self):
        """
        :param DownloadUrl: Download address for exported file.\n        :type DownloadUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares request structure.

    """


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares response structure.

    """

    def __init__(self):
        """
        :param DownloadUrl: Download address for exported file.\n        :type DownloadUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces request structure.

    """


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param DownloadUrl: Download address for exported file.\n        :type DownloadUrl: str\n        :param TaskId: Export task ID\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.

    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values is `OR`.

    * There can be up to 5 filters
    * There can be up to 5 `Values` in the same `Filter`.

    """

    def __init__(self):
        """
        :param Name: Filter key name.\n        :type Name: str\n        :param Values: One or more filter values.\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistoryAccount(AbstractModel):
    """Account change history data.

    """

    def __init__(self):
        """
        :param Id: Unique ID.\n        :type Id: int\n        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param Username: Account name.\n        :type Username: str\n        :param ModifyType: Account change type.
<li>CREATE: creates account</li>
<li>MODIFY: modifies account</li>
<li>DELETE: deletes account</li>\n        :type ModifyType: str\n        :param ModifyTime: Change time.\n        :type ModifyTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts request structure.

    """

    def __init__(self):
        """
        :param Ids: Vulnerability ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """Affected server information

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.\n        :type Id: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param LastScanTime: Last detection time.\n        :type LastScanTime: str\n        :param VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>SCANING: scanning</li>
<li>FIXED: fixed</li>\n        :type VulStatus: str\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param Description: Vulnerability description.\n        :type Description: str\n        :param VulId: Vulnerability category ID.\n        :type VulId: int\n        :param IsProVersion: Whether it is the CWP Pro.\n        :type IsProVersion: bool\n        """
        self.Id = None
        self.MachineIp = None
        self.MachineName = None
        self.LastScanTime = None
        self.VulStatus = None
        self.Uuid = None
        self.Description = None
        self.VulId = None
        self.IsProVersion = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.LastScanTime = params.get("LastScanTime")
        self.VulStatus = params.get("VulStatus")
        self.Uuid = params.get("Uuid")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.IsProVersion = params.get("IsProVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteLists(AbstractModel):
    """Login allowlist

    """

    def __init__(self):
        """
        :param Id: Record ID\n        :type Id: int\n        :param Uuid: CWP agent ID\n        :type Uuid: str\n        :param Places: Whitelisted location\n        :type Places: list of Place\n        :param UserName: Whitelisted users (separated by commas)\n        :type UserName: str\n        :param SrcIp: Whitelisted IPs (separated by commas)\n        :type SrcIp: str\n        :param IsGlobal: Whether this rule is applied to all servers under the current account\n        :type IsGlobal: bool\n        :param CreateTime: Whitelist creation time\n        :type CreateTime: str\n        :param ModifyTime: Whitelist modification time\n        :type ModifyTime: str\n        :param MachineName: Server name\n        :type MachineName: str\n        :param HostIp: Server IP\n        :type HostIp: str\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.Places = None
        self.UserName = None
        self.SrcIp = None
        self.IsGlobal = None
        self.CreateTime = None
        self.ModifyTime = None
        self.MachineName = None
        self.HostIp = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.IsGlobal = params.get("IsGlobal")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.MachineName = params.get("MachineName")
        self.HostIp = params.get("HostIp")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteListsRule(AbstractModel):
    """Whitelist rule

    """

    def __init__(self):
        """
        :param Places: Whitelisted location\n        :type Places: list of Place\n        :param SrcIp: Whitelisted IPs (separated by commas). This parameter can be an IP range.\n        :type SrcIp: str\n        :param UserName: Whitelisted usernames (separated by commas)\n        :type UserName: str\n        :param IsGlobal: Whether this rule is applied to all servers under the current account\n        :type IsGlobal: bool\n        :param HostIp: Server for which the allowlist takes effect\n        :type HostIp: str\n        :param Id: Rule ID, used for rule updating\n        :type Id: int\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        """
        self.Places = None
        self.SrcIp = None
        self.UserName = None
        self.IsGlobal = None
        self.HostIp = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.SrcIp = params.get("SrcIp")
        self.UserName = params.get("UserName")
        self.IsGlobal = params.get("IsGlobal")
        self.HostIp = params.get("HostIp")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Machine(AbstractModel):
    """Server list

    """

    def __init__(self):
        """
        :param MachineName: Server name.\n        :type MachineName: str\n        :param MachineOs: Server OS.\n        :type MachineOs: str\n        :param MachineStatus: Server status.
<li>OFFLINE: offline</li>
<li>ONLINE: online</li>
<li>MACHINE_STOPPED: shut down</li>\n        :type MachineStatus: str\n        :param Uuid: CWP agent `Uuid`. If the agent is offline for a long time, a null character will be returned.\n        :type Uuid: str\n        :param Quuid: CVM or BM instance `Uuid`.\n        :type Quuid: str\n        :param VulNum: Number of vulnerabilities.\n        :type VulNum: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param IsProVersion: Whether the server has enabled CWP Pro.
<li>true: yes</li>
<li>false: no</li>\n        :type IsProVersion: bool\n        :param MachineWanIp: Public IP of server.\n        :type MachineWanIp: str\n        :param PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>\n        :type PayMode: str\n        :param MalwareNum: Number of trojans.\n        :type MalwareNum: int\n        :param Tag: Tag information\n        :type Tag: list of MachineTag\n        :param BaselineNum: Number of baseline risks.\n        :type BaselineNum: int\n        :param CyberAttackNum: Number of network risks.\n        :type CyberAttackNum: int\n        :param SecurityStatus: Risk status.
<li>SAFE: safe</li>
<li>RISK: at risk</li>
<li>UNKNOWN: unknown</li>\n        :type SecurityStatus: str\n        :param InvasionNum: Number of intrusions\n        :type InvasionNum: int\n        :param RegionInfo: Region information\n        :type RegionInfo: :class:`tencentcloud.yunjing.v20180228.models.RegionInfo`\n        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None
        self.MalwareNum = None
        self.Tag = None
        self.BaselineNum = None
        self.CyberAttackNum = None
        self.SecurityStatus = None
        self.InvasionNum = None
        self.RegionInfo = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")
        self.MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.BaselineNum = params.get("BaselineNum")
        self.CyberAttackNum = params.get("CyberAttackNum")
        self.SecurityStatus = params.get("SecurityStatus")
        self.InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineTag(AbstractModel):
    """Server tag information

    """

    def __init__(self):
        """
        :param Rid: Associated tag ID\n        :type Rid: int\n        :param Name: Tag name\n        :type Name: str\n        :param TagId: Tag ID\n        :type TagId: int\n        """
        self.Rid = None
        self.Name = None
        self.TagId = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        self.Name = params.get("Name")
        self.TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaliciousRequest(AbstractModel):
    """Malicious request data.

    """

    def __init__(self):
        """
        :param Id: Record ID.\n        :type Id: int\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param Domain: Malicious request domain name.\n        :type Domain: str\n        :param Count: Number of malicious requests.\n        :type Count: int\n        :param ProcessName: Process name.\n        :type ProcessName: str\n        :param Status: Record status.
<li>UN_OPERATED: to be processed</li>
<li>TRUSTED: trusted</li>
<li>UN_TRUSTED: untrusted</li>\n        :type Status: str\n        :param Description: Malicious request domain name description.\n        :type Description: str\n        :param Reference: Reference address.\n        :type Reference: str\n        :param CreateTime: Discovery time.\n        :type CreateTime: str\n        :param MergeTime: Record merge time.\n        :type MergeTime: str\n        :param ProcessMd5: Process MD5
Value.\n        :type ProcessMd5: str\n        :param CmdLine: Executed command line.\n        :type CmdLine: str\n        :param Pid: Process `PID`.\n        :type Pid: int\n        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Domain = None
        self.Count = None
        self.ProcessName = None
        self.Status = None
        self.Description = None
        self.Reference = None
        self.CreateTime = None
        self.MergeTime = None
        self.ProcessMd5 = None
        self.CmdLine = None
        self.Pid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Domain = params.get("Domain")
        self.Count = params.get("Count")
        self.ProcessName = params.get("ProcessName")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Reference = params.get("Reference")
        self.CreateTime = params.get("CreateTime")
        self.MergeTime = params.get("MergeTime")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.CmdLine = params.get("CmdLine")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Malware(AbstractModel):
    """Trojan information

    """

    def __init__(self):
        """
        :param Id: Event ID.\n        :type Id: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param Status: Current trojan status.
<li>UN_OPERATED: not processed</li><li>SEGREGATED: isolated</li><li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li><li>RECOVERING: recovering</li>\n        :type Status: str\n        :param FilePath: Trojan path.\n        :type FilePath: str\n        :param Description: Trojan description.\n        :type Description: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param FileCreateTime: Trojan file creation time.\n        :type FileCreateTime: str\n        :param ModifyTime: Trojan file modification time.\n        :type ModifyTime: str\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.FilePath = None
        self.Description = None
        self.MachineName = None
        self.FileCreateTime = None
        self.ModifyTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.FilePath = params.get("FilePath")
        self.Description = params.get("Description")
        self.MachineName = params.get("MachineName")
        self.FileCreateTime = params.get("FileCreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Ids: Unusual login location event ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute request structure.

    """

    def __init__(self):
        """
        :param Attribute: Alarm item.
<li>Offline: CWP is offline</li>
<li>Malware: trojan event</li>
<li>NonlocalLogin: unusual login location discovered</li>
<li>CrackSuccess: brute force attack succeeded</li>\n        :type Attribute: str\n        :param Value: Alarm item attributes.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>\n        :type Value: str\n        """
        self.Attribute = None
        self.Value = None


    def _deserialize(self, params):
        self.Attribute = params.get("Attribute")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig request structure.

    """

    def __init__(self):
        """
        :param Status: Auto-Activation status.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>\n        :type Status: str\n        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoginWhiteListRequest(AbstractModel):
    """ModifyLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Rules: Whitelist rule\n        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`\n        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoginWhiteListResponse(AbstractModel):
    """ModifyLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag request structure.

    """

    def __init__(self):
        """
        :param RenewFlag: Auto-renewal flag. Valid values:
<li>NOTIFY_AND_AUTO_RENEW: notifies of expiration and auto-renews</li>
<li>NOTIFY_AND_MANUAL_RENEW: notifies of expiration but does not auto-renew</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW: does not notify of expiration or auto-renew</li>\n        :type RenewFlag: str\n        :param Quuid: Unique server ID, corresponding to `uuid` for CVM or `instanceId` for BM.\n        :type Quuid: str\n        """
        self.RenewFlag = None
        self.Quuid = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """Unusual login location

    """

    def __init__(self):
        """
        :param Id: Event ID.\n        :type Id: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param Status: Login status
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>NORMAL_LOGIN: intended login</li>\n        :type Status: str\n        :param UserName: Username.\n        :type UserName: str\n        :param City: City ID.\n        :type City: int\n        :param Country: Country/Region ID.\n        :type Country: int\n        :param Province: Province/State ID.\n        :type Province: int\n        :param SrcIp: Login IP.\n        :type SrcIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param LoginTime: Login time.\n        :type LoginTime: str\n        :param Uuid: CWP agent `Uuid`.\n        :type Uuid: str\n        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.MachineName = None
        self.LoginTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.MachineName = params.get("MachineName")
        self.LoginTime = params.get("LoginTime")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPort(AbstractModel):
    """Port list

    """

    def __init__(self):
        """
        :param Id: Unique ID.\n        :type Id: int\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param Port: Open port number.\n        :type Port: int\n        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param ProcessName: Process name corresponding to port.\n        :type ProcessName: str\n        :param Pid: Process `Pid` corresponding to port.\n        :type Pid: int\n        :param CreateTime: Record creation time.\n        :type CreateTime: str\n        :param ModifyTime: Record update time.\n        :type ModifyTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.Port = None
        self.MachineIp = None
        self.MachineName = None
        self.ProcessName = None
        self.Pid = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ProcessName = params.get("ProcessName")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPortStatistics(AbstractModel):
    """Port statistics list

    """

    def __init__(self):
        """
        :param Port: Port number\n        :type Port: int\n        :param MachineNum: Number of servers\n        :type MachineNum: int\n        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion request structure.

    """

    def __init__(self):
        """
        :param MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>\n        :type MachineType: str\n        :param MachineRegion: Server region
Examples: ap-guangzhou, ap-shanghai\n        :type MachineRegion: str\n        :param Quuids: Server `Uuid` array.
`InstanceId` for BM or `Uuid` for CVM\n        :type Quuids: list of str\n        :param ActivityId: Event ID.\n        :type ActivityId: int\n        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuids = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuids = params.get("Quuids")
        self.ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Place(AbstractModel):
    """Login location information

    """

    def __init__(self):
        """
        :param CityId: City ID.\n        :type CityId: int\n        :param ProvinceId: Province/State ID.\n        :type ProvinceId: int\n        :param CountryId: Country/Region ID. Currently, only `1` (Mainland China) is supported.\n        :type CountryId: int\n        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Process(AbstractModel):
    """Process information.

    """

    def __init__(self):
        """
        :param Id: Unique ID.\n        :type Id: int\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param MachineName: Server name.\n        :type MachineName: str\n        :param Pid: Process `Pid`.\n        :type Pid: int\n        :param Ppid: Process `Ppid`.\n        :type Ppid: int\n        :param ProcessName: Process name.\n        :type ProcessName: str\n        :param Username: Process username.\n        :type Username: str\n        :param Platform: OS.
<li>WIN32: Windows 32-bit</li>
<li>WIN64: Windows 64-bit</li>
<li>LINUX32: Linux 32-bit</li>
<li>LINUX64: Linux 64-bit</li>\n        :type Platform: str\n        :param FullPath: Process path.\n        :type FullPath: str\n        :param CreateTime: Creation time.\n        :type CreateTime: str\n        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Pid = None
        self.Ppid = None
        self.ProcessName = None
        self.Username = None
        self.Platform = None
        self.FullPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Pid = params.get("Pid")
        self.Ppid = params.get("Ppid")
        self.ProcessName = params.get("ProcessName")
        self.Username = params.get("Username")
        self.Platform = params.get("Platform")
        self.FullPath = params.get("FullPath")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistics(AbstractModel):
    """Process statistics.

    """

    def __init__(self):
        """
        :param ProcessName: Process name.\n        :type ProcessName: str\n        :param MachineNum: Number of servers.\n        :type MachineNum: int\n        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan ID array. Up to 200 IDs can be deleted at a time\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares response structure.

    """

    def __init__(self):
        """
        :param SuccessIds: Array of IDs of successfully recovered trojans.\n        :type SuccessIds: list of int non-negative\n        :param FailedIds: Array of IDs of trojans failed to be recovered.\n        :type FailedIds: list of int non-negative\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        """
        :param Region: Region, such as `ap-guangzhou`, `ap-shanghai` and `ap-beijing`\n        :type Region: str\n        :param RegionName: Region name, such as `South China (Guangzhou)`, `East China (Shanghai)`, and `North China (Beijing)`\n        :type RegionName: str\n        :param RegionId: Region ID\n        :type RegionId: int\n        :param RegionCode: Region code, such as `gz`, `sh`, and `bj`\n        :type RegionCode: str\n        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionCode = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionCode = params.get("RegionCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost request structure.

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityDynamic(AbstractModel):
    """Security event message data.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param EventTime: Security event occurrence time.\n        :type EventTime: str\n        :param EventType: Security event type.
<li>MALWARE: trojan event</li>
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>BRUTEATTACK_SUCCESS: brute force attack succeeded</li>
<li>VUL: vulnerability</li>
<li>BASELINE: security baseline</li>\n        :type EventType: str\n        :param Message: Security event message.\n        :type Message: str\n        :param SecurityLevel: Security event level.
<li>RISK: severe</li>
<li>HIGH: high</li>
<li>NORMAL: medium</li>
<li>LOW: low</li>\n        :type SecurityLevel: str\n        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None
        self.SecurityLevel = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")
        self.SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTrend(AbstractModel):
    """Security trend statistics.

    """

    def __init__(self):
        """
        :param Date: Event time.\n        :type Date: str\n        :param EventNum: Number of events.\n        :type EventNum: int\n        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan event ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares response structure.

    """

    def __init__(self):
        """
        :param SuccessIds: Array of IDs of successfully isolated trojans.\n        :type SuccessIds: list of int non-negative\n        :param FailedIds: Array of IDs of trojans failed to be isolated.\n        :type FailedIds: list of int non-negative\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag information

    """

    def __init__(self):
        """
        :param Id: Tag ID\n        :type Id: int\n        :param Name: Tag name\n        :type Name: str\n        :param Count: Number of servers\n        :type Count: int\n        """
        self.Id = None
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagMachine(AbstractModel):
    """Tagged server information

    """

    def __init__(self):
        """
        :param Id: ID\n        :type Id: str\n        :param Quuid: Server ID\n        :type Quuid: str\n        :param MachineName: Server name\n        :type MachineName: str\n        :param MachineIp: Private IP of server\n        :type MachineIp: str\n        :param MachineWanIp: Public IP of server\n        :type MachineWanIp: str\n        :param MachineRegion: Server region\n        :type MachineRegion: str\n        :param MachineType: Server region type\n        :type MachineType: str\n        """
        self.Id = None
        self.Quuid = None
        self.MachineName = None
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineRegion = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.MachineName = params.get("MachineName")
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineRegion = params.get("MachineRegion")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest request structure.

    """

    def __init__(self):
        """
        :param Id: Malicious request record ID.\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan ID array.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest request structure.

    """

    def __init__(self):
        """
        :param Id: Trusted record ID.\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan event ID array. Up to 200 IDs can be processed at a time.\n        :type Ids: list of int non-negative\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """Usual login location

    """

    def __init__(self):
        """
        :param Id: ID.\n        :type Id: int\n        :param Uuid: CWP agent `UUID`.\n        :type Uuid: str\n        :param CountryId: Country/Region ID.\n        :type CountryId: int\n        :param ProvinceId: Province/State ID.\n        :type ProvinceId: int\n        :param CityId: City ID.\n        :type CityId: int\n        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vul(AbstractModel):
    """Vulnerability list data

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID\n        :type VulId: int\n        :param VulName: Vulnerability name\n        :type VulName: str\n        :param VulLevel: Vulnerability severity level:
HIGH: high
MIDDLE: medium
LOW: low
NOTICE: notice\n        :type VulLevel: str\n        :param LastScanTime: Last scanned time\n        :type LastScanTime: str\n        :param ImpactedHostNum: Number of affected servers\n        :type ImpactedHostNum: int\n        :param VulStatus: Vulnerability status
* UN_OPERATED: to be processed
* FIXED: fixed\n        :type VulStatus: str\n        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.ImpactedHostNum = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.VulStatus = params.get("VulStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReport(AbstractModel):
    """Weekly report list.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly report start time.\n        :type BeginDate: str\n        :param EndDate: Weekly report end time.\n        :type EndDate: str\n        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportBruteAttack(AbstractModel):
    """Brute force attack data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param Username: Hacked username.\n        :type Username: str\n        :param SrcIp: Source IP.\n        :type SrcIp: str\n        :param Count: Number of attempts.\n        :type Count: int\n        :param AttackTime: Attack time.\n        :type AttackTime: str\n        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Count = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportMalware(AbstractModel):
    """Trojan data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param FilePath: Trojan file path.\n        :type FilePath: str\n        :param Md5: Trojan file MD5 value.\n        :type Md5: str\n        :param FindTime: Trojan discovery time.\n        :type FindTime: str\n        :param Status: Current trojan status.
<li>UN_OPERATED: not processed</li>
<li>SEGREGATED: isolated</li>
<li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li>
<li>RECOVERING: recovering</li>\n        :type Status: str\n        """
        self.MachineIp = None
        self.FilePath = None
        self.Md5 = None
        self.FindTime = None
        self.Status = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.FilePath = params.get("FilePath")
        self.Md5 = params.get("Md5")
        self.FindTime = params.get("FindTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """Unusual login location data in weekly CWP Pro report

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.\n        :type MachineIp: str\n        :param Username: Username.\n        :type Username: str\n        :param SrcIp: Source IP.\n        :type SrcIp: str\n        :param Country: Country/Region ID.\n        :type Country: int\n        :param Province: Province/State ID.\n        :type Province: int\n        :param City: City ID.\n        :type City: int\n        :param LoginTime: Login time.\n        :type LoginTime: str\n        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Country = None
        self.Province = None
        self.City = None
        self.LoginTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.LoginTime = params.get("LoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyReportVul(AbstractModel):
    """Vulnerability data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Private IP of server.\n        :type MachineIp: str\n        :param VulName: Vulnerability name.\n        :type VulName: str\n        :param VulType: Vulnerability type.
<li> WEB: web vulnerability</li>
<li> SYSTEM: system component vulnerability</li>
<li> BASELINE: security baseline</li>\n        :type VulType: str\n        :param Description: Vulnerability description.\n        :type Description: str\n        :param VulStatus: Vulnerability status.
<li> UN_OPERATED: to be processed</li>
<li> SCANING: scanning</li>
<li> FIXED: fixed</li>\n        :type VulStatus: str\n        :param LastScanTime: Last scanned time.\n        :type LastScanTime: str\n        """
        self.MachineIp = None
        self.VulName = None
        self.VulType = None
        self.Description = None
        self.VulStatus = None
        self.LastScanTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.VulStatus = params.get("VulStatus")
        self.LastScanTime = params.get("LastScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        