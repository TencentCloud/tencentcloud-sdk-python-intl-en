# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """Account list information.

    """

    def __init__(self):
        """
        :param Id: Unique ID.
        :type Id: int
        :param Uuid: CWP agent `Uuid`
        :type Uuid: str
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param Username: Account name.
        :type Username: str
        :param Groups: Account group.
        :type Groups: str
        :param Privilege: Account type.
<li>ORDINARY: ordinary account</li>
<li>SUPPER: super admin account</li>
        :type Privilege: str
        :param AccountCreateTime: Account creation time.
        :type AccountCreateTime: str
        :param LastLoginTime: Account last login time.
        :type LastLoginTime: str
        """
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


class AccountStatistics(AbstractModel):
    """Account statistics.

    """

    def __init__(self):
        """
        :param Username: Username.
        :type Username: str
        :param MachineNum: Number of servers.
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")


class AddLoginWhiteListRequest(AbstractModel):
    """AddLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Rules: Whitelist rule
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))


class AddLoginWhiteListResponse(AbstractModel):
    """AddLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddMachineTagRequest(AbstractModel):
    """AddMachineTag request structure.

    """

    def __init__(self):
        """
        :param Quuid: Server ID
        :type Quuid: str
        :param TagId: Tag ID
        :type TagId: int
        :param MRegion: Server region
        :type MRegion: str
        :param MArea: Server type (`CVM` or `BM`)
        :type MArea: str
        """
        self.Quuid = None
        self.TagId = None
        self.MRegion = None
        self.MArea = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.TagId = params.get("TagId")
        self.MRegion = params.get("MRegion")
        self.MArea = params.get("MArea")


class AddMachineTagResponse(AbstractModel):
    """AddMachineTag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AgentVul(AbstractModel):
    """Server vulnerability information

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.
        :type Id: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param VulName: Vulnerability name.
        :type VulName: str
        :param VulLevel: Vulnerability severity level.
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
<li>NOTICE: notice</li>
        :type VulLevel: str
        :param LastScanTime: Last scanned time.
        :type LastScanTime: str
        :param Description: Vulnerability description.
        :type Description: str
        :param VulId: Vulnerability category ID.
        :type VulId: int
        :param VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>FIXED: fixed</li>
        :type VulStatus: str
        """
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


class BruteAttack(AbstractModel):
    """Brute force attack list

    """

    def __init__(self):
        """
        :param Id: Event ID.
        :type Id: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param Status: Brute force attack event status
<li>BRUTEATTACK_FAIL_ACCOUNT: brute force attack event - failure (the account exists)</li>
<li>BRUTEATTACK_FAIL_NOACCOUNT: brute force attack event - failure (the account does not exist)</li>
<li>BRUTEATTACK_SUCCESS: brute force attack event - success </li>
        :type Status: str
        :param UserName: Username.
        :type UserName: str
        :param City: City ID.
        :type City: int
        :param Country: Country/Region ID.
        :type Country: int
        :param Province: Province/State ID.
        :type Province: int
        :param SrcIp: Source IP.
        :type SrcIp: str
        :param Count: Number of attempts.
        :type Count: int
        :param CreateTime: Occurrence time.
        :type CreateTime: str
        :param MachineName: Server name.
        :type MachineName: str
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param IsProVersion: Whether the server enables CWP Pro.
        :type IsProVersion: bool
        :param BanStatus: Whether the server is banned.
        :type BanStatus: str
        :param Quuid: Server `UUID`
        :type Quuid: str
        """
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


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion request structure.

    """

    def __init__(self):
        """
        :param Quuid: Server `Uuid`.
`InstanceId` for BM or `Uuid` for CVM
        :type Quuid: str
        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """Component list data.

    """

    def __init__(self):
        """
        :param Id: Unique ID.
        :type Id: int
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param ComponentVersion: Component version number.
        :type ComponentVersion: str
        :param ComponentType: Component type.
<li>SYSTEM: system component</li>
<li>WEB: web component</li>
        :type ComponentType: str
        :param ComponentName: Component name.
        :type ComponentName: str
        :param ModifyTime: Component detection update time.
        :type ModifyTime: str
        """
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


class ComponentStatistics(AbstractModel):
    """Component statistics.

    """

    def __init__(self):
        """
        :param Id: Component ID.
        :type Id: int
        :param MachineNum: Number of servers.
        :type MachineNum: int
        :param ComponentName: Component name.
        :type ComponentName: str
        :param ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :type ComponentType: str
        :param Description: Component description.
        :type Description: str
        """
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


class CreateOpenPortTaskRequest(AbstractModel):
    """CreateOpenPortTask request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateOpenPortTaskResponse(AbstractModel):
    """CreateOpenPortTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuids: CWP agent `UUID` array.
        :type Uuids: list of str
        :param Places: Login region information array.
        :type Places: list of Place
        """
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


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks request structure.

    """

    def __init__(self):
        """
        :param Ids: Brute force attack event ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Ids: Whitelist ID
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag request structure.

    """

    def __init__(self):
        """
        :param Rid: Associated tag ID
        :type Rid: int
        """
        self.Rid = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests request structure.

    """

    def __init__(self):
        """
        :param Ids: Malicious request record ID array. Maximum value: 100 entries.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan record ID array
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Ids: Unusual login location event ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `Uuid`
        :type Uuid: str
        :param CityIds: Added usual login city ID array
        :type CityIds: list of int non-negative
        """
        self.Uuid = None
        self.CityIds = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.CityIds = params.get("CityIds")


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Username - String - Required: No - Account username</li>
        :type Filters: list of Filter
        """
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


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account statistics list.
        :type TotalCount: int
        :param AccountStatistics: Account statistics list.
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param Username: CWP agent `Uuid`. Either `Username` or `Uuid` must be specified. If `Username` is specified, it indicates to query the information list under the specified username.
        :type Username: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Username - String - Required: No - Account name</li>
<li>Privilege - String - Required: No - Account name (ORDINARY: ordinary account, SUPPER: super admin account)</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
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


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account list.
        :type TotalCount: int
        :param Accounts: Account data list.
        :type Accounts: list of Account
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>BASELINE: security baseline</li>
        :type VulType: str
        :param Uuid: Agent `UUID`.
        :type Uuid: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)
        :type Filters: list of Filter
        """
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


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param AgentVuls: Server vulnerability information
        :type AgentVuls: list of AgentVul
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>CLOSE: alarm disabled</li>
        :type Offline: str
        :param Malware: Trojan discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type Malware: str
        :param NonlocalLogin: Unusual login location discovery alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type NonlocalLogin: str
        :param CrackSuccess: Brute force attack success alarm status:
<li>OPEN: alarm enabled</li>
<li>CLOSE: alarm disabled</li>
        :type CrackSuccess: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: Agent `Uuid`.
        :type Uuid: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Query status (FAILED: brute force attack failed, SUCCESS: brute force attack succeeded)</li>
        :type Filters: list of Filter
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        """
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


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of events
        :type TotalCount: int
        :param BruteAttacks: Brute force attack event list
        :type BruteAttacks: list of BruteAttack
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param ComponentId: Component ID.
        :type ComponentId: int
        """
        self.ComponentId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo response structure.

    """

    def __init__(self):
        """
        :param Id: Component ID.
        :type Id: int
        :param ComponentName: Component name.
        :type ComponentName: str
        :param ComponentType: Component type.
<li>WEB: web component</li>
<li>SYSTEM: system component</li>
        :type ComponentType: str
        :param Homepage: Component's official website.
        :type Homepage: str
        :param Description: Component description.
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
ComponentName - String - Required: No - Component name
        :type Filters: list of Filter
        """
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


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in component statistics list.
        :type TotalCount: int
        :param ComponentStatistics: Component statistics list data array.
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`. Either `Uuid` or `ComponentId` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param ComponentId: Component ID. Either `Uuid` or `ComponentId` must be specified. If `ComponentId` is specified, it indicates to query the information list under the specified component.
        :type ComponentId: int
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>ComponentVersion - String - Required: No - Component version number</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
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


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in component list.
        :type TotalCount: int
        :param Components: Component list data.
        :type Components: list of Component
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Username - String - Required: No - Account name</li>
        :type Filters: list of Filter
        """
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


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in account change history list.
        :type TotalCount: int
        :param HistoryAccounts: Account change history data array.
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param VulId: Vulnerability category ID.
        :type VulId: int
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)</li>
        :type Filters: list of Filter
        """
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


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param ImpactedHosts: Affected server list array
        :type ImpactedHosts: list of ImpactedHost
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
        :type Filters: list of Filter
        """
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


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param LoginWhiteLists: Login whitelist array
        :type LoginWhiteLists: list of LoginWhiteLists
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo response structure.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param ProtectDays: Days under protection by CWP
        :type ProtectDays: int
        :param MachineOs: OS.
        :type MachineOs: str
        :param MachineName: Server name.
        :type MachineName: str
        :param MachineStatus: Status.
<li>ONLINE: online</li>
<li>OFFLINE: offline</li>
        :type MachineStatus: str
        :param InstanceId: Unique ID of CVM or BM instance.
        :type InstanceId: str
        :param MachineWanIp: Public IP of server.
        :type MachineWanIp: str
        :param Quuid: CVM or BM instance `Uuid`.
        :type Quuid: str
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param IsProVersion: Whether CWP Pro is activated.
<li>true: yes</li>
<li>false: no</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: CWP Pro activation time.
        :type ProVersionOpenDate: str
        :param MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :type MachineType: str
        :param MachineRegion: Server region, such as ap-guangzhou or ap-shanghai
        :type MachineRegion: str
        :param PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :type PayMode: str
        :param FreeMalwaresLeft: Number of trojans left for free scan.
        :type FreeMalwaresLeft: int
        :param FreeVulsLeft: Number of vulnerability left for free scan.
        :type FreeVulsLeft: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>BM: BM</li>
        :type MachineType: str
        :param MachineRegion: Server region, such as ap-guangzhou or ap-shanghai
        :type MachineRegion: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Agent status (OFFLINE: offline, ONLINE: online)</li>
<li>Version - String  Required: No - Current CWP edition (PRO_VERSION: Pro, BASIC_VERSION: Basic)</li>
Each filter supports only one value. Query with multiple values in "OR" relationship is not supported for the time being
        :type Filters: list of Filter
        """
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


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines response structure.

    """

    def __init__(self):
        """
        :param Machines: Server list
        :type Machines: list of Machine
        :param TotalCount: Number of servers
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, TRUSTED: trusted, UN_TRUSTED: untrusted)</li>
<li>Domain - String - Required: No - Malicious request domain name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        """
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


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param MaliciousRequests: Malicious request record array.
        :type MaliciousRequests: list of MaliciousRequest
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: Agent `Uuid`.
        :type Uuid: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Trojan status (UN_OPERATED: not processed, SEGREGATED: isolated, TRUSTED: trusted)</li>
Each filter supports only one value. Query with multiple values in "OR" relationship is not supported for the time being.
        :type Filters: list of Filter
        """
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


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of trojans.
        :type TotalCount: int
        :param Malwares: Malware array.
        :type Malwares: list of Malware
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: Agent `Uuid`.
        :type Uuid: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Keywords - String - Required: No - Query keywords</li>
<li>Status - String - Required: No - Login status (NON_LOCAL_LOGIN: unusual login location, NORMAL_LOGIN: intended login)</li>
        :type Filters: list of Filter
        """
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


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param NonLocalLoginPlaces: Unusual login location information array.
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>
        :type Filters: list of Filter
        """
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


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in port statistics list
        :type TotalCount: int
        :param OpenPortStatistics: Port statistics list
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeOpenPortTaskStatusResponse(AbstractModel):
    """DescribeOpenPortTaskStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeOpenPorts` API to get the list of real-time processes) </li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting port</li>
<li>FAILED: failed to get processes</li>
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`. Either `Port` or `Uuid` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param Port: Open port number. Either `Port` or `Uuid` must be specified. If `Port` is specified, it indicates to query the information list under the specified port.
        :type Port: int
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Port - Uint64 - Required: No - Port number</li>
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
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


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in port list.
        :type TotalCount: int
        :param OpenPorts: Port list.
        :type OpenPorts: list of OpenPort
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param OnlineMachineNum: Number of online servers.
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: Number of servers activated CWP Pro.
        :type ProVersionMachineNum: int
        :param MalwareNum: Number of trojan files.
        :type MalwareNum: int
        :param NonlocalLoginNum: Number of unusual login locations.
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: Number of successful brute force attacks.
        :type BruteAttackSuccessNum: int
        :param VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param BaseLineNum: Security baseline number
        :type BaseLineNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param PostPayCost: Fee on yesterday (pay-as-you-go)
        :type PostPayCost: int
        :param IsAutoOpenProVersion: Whether CWP Pro is activated for new servers
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: Number of servers on CWP Pro
        :type ProVersionNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>
        :type Filters: list of Filter
        """
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


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in process statistics list.
        :type TotalCount: int
        :param ProcessStatistics: Process statistics list array.
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Task status.
<li>COMPLETE: completed (at this point, you can call the `DescribeProcesses` API to get the list of real-time processes)</li>
<li>AGENT_OFFLINE: CWP agent is offline</li>
<li>COLLECTING: getting process</li>
<li>FAILED: failed to get processes</li>
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `Uuid`. Either `Uuid` or `ProcessName` must be specified. If `Uuid` is specified, it indicates to query the information list under the specified server.
        :type Uuid: str
        :param ProcessName: Process name. Either `Uuid` or `ProcessName` must be specified. If `ProcessName` is specified, it indicates to query the information list under the specified process.
        :type ProcessName: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>ProcessName - String - Required: No - Process name</li>
<li>MachineIp - String - Required: No - Private IP of server</li>
        :type Filters: list of Filter
        """
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


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of records in process list.
        :type TotalCount: int
        :param Processes: Process list data array.
        :type Processes: list of Process
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics response structure.

    """

    def __init__(self):
        """
        :param SecurityDynamics: Security event message array.
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Start time.
        :type BeginDate: str
        :param EndDate: End time.
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends response structure.

    """

    def __init__(self):
        """
        :param Malwares: Trojan event statistics array.
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: Unusual login location event statistics array.
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: Brute force attack event statistics array.
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: Vulnerability statistics array.
        :type Vuls: list of SecurityTrend
        :param BaseLines: Baseline statistics array.
        :type BaseLines: list of SecurityTrend
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
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
        self.RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines request structure.

    """

    def __init__(self):
        """
        :param Id: Tag ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines response structure.

    """

    def __init__(self):
        """
        :param List: List data
        :type List: list of TagMachine
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeTagsResponse(AbstractModel):
    """DescribeTags response structure.

    """

    def __init__(self):
        """
        :param List: List information
        :type List: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Uuid: CWP agent `UUID`
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: Usual login location array
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param VulId: Vulnerability category ID.
        :type VulId: int
        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo response structure.

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID.
        :type VulId: int
        :param VulName: Vulnerability name.
        :type VulName: str
        :param VulLevel: Vulnerability level.
        :type VulLevel: str
        :param VulType: Vulnerability type.
        :type VulType: str
        :param Description: Vulnerability description.
        :type Description: str
        :param RepairPlan: Repair plan.
        :type RepairPlan: str
        :param CveId: Vulnerability CVE.
        :type CveId: str
        :param Reference: Reference link.
        :type Reference: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param ProVersionNum: Number of servers activated CWP Pro
        :type ProVersionNum: int
        :param ImpactedHostNum: Number of affected activated CWP Pro.
        :type ImpactedHostNum: int
        :param HostNum: Total number of servers.
        :type HostNum: int
        :param BasicVersionNum: Number of servers on CWP Basic.
        :type BasicVersionNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>BASELINE: security baseline</li>
        :type VulType: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Filters: Filter.
<li>Status - String - Required: No - Filter by status (UN_OPERATED: to be processed, FIXED: fixed)

Only one value is allowed for the `Status` filter, and "OR" logic is not supported.
        :type Filters: list of Filter
        """
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


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of vulnerabilities.
        :type TotalCount: int
        :param Vuls: Vulnerability list array.
        :type Vuls: list of Vul
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportBruteAttacks: Brute force attack array in weekly CWP Pro report.
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        """
        self.BeginDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo response structure.

    """

    def __init__(self):
        """
        :param CompanyName: Account owner name.
        :type CompanyName: str
        :param MachineNum: Total number of servers.
        :type MachineNum: int
        :param OnlineMachineNum: Number of online CWP agents
        :type OnlineMachineNum: int
        :param OfflineMachineNum: Number of offline CWP agents.
        :type OfflineMachineNum: int
        :param ProVersionMachineNum: Number of servers on CWP Pro.
        :type ProVersionMachineNum: int
        :param BeginDate: Weekly report start time
        :type BeginDate: str
        :param EndDate: Weekly report end time
        :type EndDate: str
        :param Level: Security level
<li>HIGH: high</li>
<li>MIDDLE: medium</li>
<li>LOW: low</li>
        :type Level: str
        :param MalwareNum: Number of trojan records.
        :type MalwareNum: int
        :param NonlocalLoginNum: Number of unusual login locations.
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: Number of successful brute force attacks.
        :type BruteAttackSuccessNum: int
        :param VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportMalwares: Trojan data in weekly CWP Pro report.
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportNonlocalLoginPlaces: Unusual login location data in weekly CWP Pro report
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param BeginDate: Weekly CWP Pro report start time.
        :type BeginDate: str
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls response structure.

    """

    def __init__(self):
        """
        :param WeeklyReportVuls: Vulnerability data array in weekly CWP Pro report.
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Number of results to be returned. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports response structure.

    """

    def __init__(self):
        """
        :param WeeklyReports: Weekly CWP Pro report list array.
        :type WeeklyReports: list of WeeklyReport
        :param TotalCount: Total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Name: Tag name
        :type Name: str
        :param Id: Tag ID
        :type Id: int
        :param Quuids: CVM instance ID
        :type Quuids: list of str
        """
        self.Name = None
        self.Id = None
        self.Quuids = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Quuids = params.get("Quuids")


class EditTagsResponse(AbstractModel):
    """EditTags response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param DownloadUrl: Download address for exported file.
        :type DownloadUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
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
        :param Name: Filter key name.
        :type Name: str
        :param Values: One or more filter values.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HistoryAccount(AbstractModel):
    """Account change history data.

    """

    def __init__(self):
        """
        :param Id: Unique ID.
        :type Id: int
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param Username: Account name.
        :type Username: str
        :param ModifyType: Account change type.
<li>CREATE: creates account</li>
<li>MODIFY: modifies account</li>
<li>DELETE: deletes account</li>
        :type ModifyType: str
        :param ModifyTime: Change time.
        :type ModifyTime: str
        """
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


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts request structure.

    """

    def __init__(self):
        """
        :param Ids: Vulnerability ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """Affected server information

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.
        :type Id: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param LastScanTime: Last detection time.
        :type LastScanTime: str
        :param VulStatus: Vulnerability status.
<li>UN_OPERATED: to be processed</li>
<li>SCANING: scanning</li>
<li>FIXED: fixed</li>
        :type VulStatus: str
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param Description: Vulnerability description.
        :type Description: str
        :param VulId: Vulnerability category ID.
        :type VulId: int
        :param IsProVersion: Whether it is the CWP Pro.
        :type IsProVersion: bool
        """
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


class LoginWhiteLists(AbstractModel):
    """Login whitelist

    """

    def __init__(self):
        """
        :param Id: Record ID
        :type Id: int
        :param Uuid: CWP agent ID
        :type Uuid: str
        :param Places: Whitelisted location
        :type Places: list of Place
        :param UserName: Whitelisted users (separated by commas)
        :type UserName: str
        :param SrcIp: Whitelisted IPs (separated by commas)
        :type SrcIp: str
        :param IsGlobal: Whether this rule is applied to all servers under the current account
        :type IsGlobal: bool
        :param CreateTime: Whitelist creation time
        :type CreateTime: str
        :param ModifyTime: Whitelist modification time
        :type ModifyTime: str
        :param MachineName: Server name
        :type MachineName: str
        :param HostIp: Server IP
        :type HostIp: str
        """
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


class LoginWhiteListsRule(AbstractModel):
    """Whitelist rule

    """

    def __init__(self):
        """
        :param Places: Whitelisted location
        :type Places: list of Place
        :param SrcIp: Whitelisted IPs (separated by commas). This parameter can be an IP range.
        :type SrcIp: str
        :param UserName: Whitelisted usernames (separated by commas)
        :type UserName: str
        :param IsGlobal: Whether this rule is applied to all servers under the current account
        :type IsGlobal: bool
        :param HostIp: Server for which the whitelist takes effect
        :type HostIp: str
        :param Id: Rule ID, used for rule updating
        :type Id: int
        """
        self.Places = None
        self.SrcIp = None
        self.UserName = None
        self.IsGlobal = None
        self.HostIp = None
        self.Id = None


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


class Machine(AbstractModel):
    """Server list

    """

    def __init__(self):
        """
        :param MachineName: Server name.
        :type MachineName: str
        :param MachineOs: Server OS.
        :type MachineOs: str
        :param MachineStatus: Server status.
<li>OFFLINE: offline</li>
<li>ONLINE: online</li>
<li>MACHINE_STOPPED: shut down</li>
        :type MachineStatus: str
        :param Uuid: CWP agent `Uuid`. If the agent is offline for a long time, a null character will be returned.
        :type Uuid: str
        :param Quuid: CVM or BM instance `Uuid`.
        :type Quuid: str
        :param VulNum: Number of vulnerabilities.
        :type VulNum: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param IsProVersion: Whether the server has enabled CWP Pro.
<li>true: yes</li>
<li>false: no</li>
        :type IsProVersion: bool
        :param MachineWanIp: Public IP of server.
        :type MachineWanIp: str
        :param PayMode: Server status.
<li>POSTPAY: post-paid, i.e., pay-as-you-go </li>
        :type PayMode: str
        :param MalwareNum: Number of trojans.
        :type MalwareNum: int
        :param Tag: Tag information
        :type Tag: list of MachineTag
        """
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


class MachineTag(AbstractModel):
    """Server tag information

    """

    def __init__(self):
        """
        :param Rid: Associated tag ID
        :type Rid: int
        :param Name: Tag name
        :type Name: str
        """
        self.Rid = None
        self.Name = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        self.Name = params.get("Name")


class MaliciousRequest(AbstractModel):
    """Malicious request data.

    """

    def __init__(self):
        """
        :param Id: Record ID.
        :type Id: int
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param Domain: Malicious request domain name.
        :type Domain: str
        :param Count: Number of malicious requests.
        :type Count: int
        :param ProcessName: Process name.
        :type ProcessName: str
        :param Status: Record status.
<li>UN_OPERATED: to be processed</li>
<li>TRUSTED: trusted</li>
<li>UN_TRUSTED: untrusted</li>
        :type Status: str
        :param Description: Malicious request domain name description.
        :type Description: str
        :param Reference: Reference address.
        :type Reference: str
        :param CreateTime: Discovery time.
        :type CreateTime: str
        :param MergeTime: Record merge time.
        :type MergeTime: str
        :param ProcessMd5: Process MD5
Value.
        :type ProcessMd5: str
        :param CmdLine: Executed command line.
        :type CmdLine: str
        :param Pid: Process `PID`.
        :type Pid: int
        """
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


class Malware(AbstractModel):
    """Trojan information

    """

    def __init__(self):
        """
        :param Id: Event ID.
        :type Id: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param Status: Current trojan status.
<li>UN_OPERATED: not processed</li><li>SEGREGATED: isolated</li><li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li><li>RECOVERING: recovering</li>
        :type Status: str
        :param FilePath: Trojan path.
        :type FilePath: str
        :param Description: Trojan description.
        :type Description: str
        :param MachineName: Server name.
        :type MachineName: str
        :param FileCreateTime: Trojan file creation time.
        :type FileCreateTime: str
        :param ModifyTime: Trojan file modification time.
        :type ModifyTime: str
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        """
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


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces request structure.

    """

    def __init__(self):
        """
        :param Ids: Unusual login location event ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>CrackSuccess: brute force attack succeeded</li>
        :type Attribute: str
        :param Value: Alarm item attributes.
<li>CLOSE: disabled</li>
<li>OPEN: enabled</li>
        :type Value: str
        """
        self.Attribute = None
        self.Value = None


    def _deserialize(self, params):
        self.Attribute = params.get("Attribute")
        self.Value = params.get("Value")


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>OPEN: enabled</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoginWhiteListRequest(AbstractModel):
    """ModifyLoginWhiteList request structure.

    """

    def __init__(self):
        """
        :param Rules: Whitelist rule
        :type Rules: :class:`tencentcloud.yunjing.v20180228.models.LoginWhiteListsRule`
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = LoginWhiteListsRule()
            self.Rules._deserialize(params.get("Rules"))


class ModifyLoginWhiteListResponse(AbstractModel):
    """ModifyLoginWhiteList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW: does not notify of expiration or auto-renew</li>
        :type RenewFlag: str
        :param Quuid: Unique server ID, corresponding to `uuid` for CVM or `instanceId` for BM.
        :type Quuid: str
        """
        self.RenewFlag = None
        self.Quuid = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Quuid = params.get("Quuid")


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """Unusual login location

    """

    def __init__(self):
        """
        :param Id: Event ID.
        :type Id: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param Status: Login status
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>NORMAL_LOGIN: intended login</li>
        :type Status: str
        :param UserName: Username.
        :type UserName: str
        :param City: City ID.
        :type City: int
        :param Country: Country/Region ID.
        :type Country: int
        :param Province: Province/State ID.
        :type Province: int
        :param SrcIp: Login IP.
        :type SrcIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param LoginTime: Login time.
        :type LoginTime: str
        :param Uuid: CWP agent `Uuid`.
        :type Uuid: str
        """
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


class OpenPort(AbstractModel):
    """Port list

    """

    def __init__(self):
        """
        :param Id: Unique ID.
        :type Id: int
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param Port: Open port number.
        :type Port: int
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param ProcessName: Process name corresponding to port.
        :type ProcessName: str
        :param Pid: Process `Pid` corresponding to port.
        :type Pid: int
        :param CreateTime: Record creation time.
        :type CreateTime: str
        :param ModifyTime: Record update time.
        :type ModifyTime: str
        """
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


class OpenPortStatistics(AbstractModel):
    """Port statistics list

    """

    def __init__(self):
        """
        :param Port: Port number
        :type Port: int
        :param MachineNum: Number of servers
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion request structure.

    """

    def __init__(self):
        """
        :param MachineType: Server type.
<li>CVM: CVM</li>
<li>BM: BM</li>
        :type MachineType: str
        :param MachineRegion: Server region
Examples: ap-guangzhou, ap-shanghai
        :type MachineRegion: str
        :param Quuids: Server `Uuid` array.
`InstanceId` for BM or `Uuid` for CVM
        :type Quuids: list of str
        :param ActivityId: Event ID.
        :type ActivityId: int
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuids = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuids = params.get("Quuids")
        self.ActivityId = params.get("ActivityId")


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Place(AbstractModel):
    """Login location information

    """

    def __init__(self):
        """
        :param CityId: City ID.
        :type CityId: int
        :param ProvinceId: Province/State ID.
        :type ProvinceId: int
        :param CountryId: Country/Region ID. Currently, only `1` (Mainland China) is supported.
        :type CountryId: int
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")


class Process(AbstractModel):
    """Process information.

    """

    def __init__(self):
        """
        :param Id: Unique ID.
        :type Id: int
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param MachineName: Server name.
        :type MachineName: str
        :param Pid: Process `Pid`.
        :type Pid: int
        :param Ppid: Process `Ppid`.
        :type Ppid: int
        :param ProcessName: Process name.
        :type ProcessName: str
        :param Username: Process username.
        :type Username: str
        :param Platform: OS.
<li>WIN32: Windows 32-bit</li>
<li>WIN64: Windows 64-bit</li>
<li>LINUX32: Linux 32-bit</li>
<li>LINUX64: Linux 64-bit</li>
        :type Platform: str
        :param FullPath: Process path.
        :type FullPath: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        """
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


class ProcessStatistics(AbstractModel):
    """Process statistics.

    """

    def __init__(self):
        """
        :param ProcessName: Process name.
        :type ProcessName: str
        :param MachineNum: Number of servers.
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan ID array. Up to 200 IDs can be deleted at a time
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares response structure.

    """

    def __init__(self):
        """
        :param SuccessIds: Array of IDs of successfully recovered trojans.
        :type SuccessIds: list of int non-negative
        :param FailedIds: Array of IDs of trojans failed to be recovered.
        :type FailedIds: list of int non-negative
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost request structure.

    """

    def __init__(self):
        """
        :param Id: Vulnerability ID.
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityDynamic(AbstractModel):
    """Security event message data.

    """

    def __init__(self):
        """
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param EventTime: Security event occurrence time.
        :type EventTime: str
        :param EventType: Security event type.
<li>MALWARE: trojan event</li>
<li>NON_LOCAL_LOGIN: unusual login location</li>
<li>BRUTEATTACK_SUCCESS: brute force attack succeeded</li>
<li>VUL: vulnerability</li>
<li>BASELINE: security baseline</li>
        :type EventType: str
        :param Message: Security event message.
        :type Message: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")


class SecurityTrend(AbstractModel):
    """Security trend statistics.

    """

    def __init__(self):
        """
        :param Date: Event time.
        :type Date: str
        :param EventNum: Number of events.
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan event ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares response structure.

    """

    def __init__(self):
        """
        :param SuccessIds: Array of IDs of successfully isolated trojans.
        :type SuccessIds: list of int non-negative
        :param FailedIds: Array of IDs of trojans failed to be isolated.
        :type FailedIds: list of int non-negative
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Id: Tag ID
        :type Id: int
        :param Name: Tag name
        :type Name: str
        :param Count: Number of servers
        :type Count: int
        """
        self.Id = None
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Count = params.get("Count")


class TagMachine(AbstractModel):
    """Tagged server information

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: str
        :param Quuid: Server ID
        :type Quuid: str
        :param MachineName: Server name
        :type MachineName: str
        :param MachineIp: Private IP of server
        :type MachineIp: str
        :param MachineWanIp: Public IP of server
        :type MachineWanIp: str
        :param MachineRegion: Server region
        :type MachineRegion: str
        :param MachineType: Server region type
        :type MachineType: str
        """
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


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest request structure.

    """

    def __init__(self):
        """
        :param Id: Malicious request record ID.
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan ID array.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest request structure.

    """

    def __init__(self):
        """
        :param Id: Trusted record ID.
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares request structure.

    """

    def __init__(self):
        """
        :param Ids: Trojan event ID array. Up to 200 IDs can be processed at a time.
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """Usual login location

    """

    def __init__(self):
        """
        :param Id: ID.
        :type Id: int
        :param Uuid: CWP agent `UUID`.
        :type Uuid: str
        :param CountryId: Country/Region ID.
        :type CountryId: int
        :param ProvinceId: Province/State ID.
        :type ProvinceId: int
        :param CityId: City ID.
        :type CityId: int
        """
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


class Vul(AbstractModel):
    """Vulnerability list data

    """

    def __init__(self):
        """
        :param VulId: Vulnerability category ID
        :type VulId: int
        :param VulName: Vulnerability name
        :type VulName: str
        :param VulLevel: Vulnerability severity level:
HIGH: high
MIDDLE: medium
LOW: low
NOTICE: notice
        :type VulLevel: str
        :param LastScanTime: Last scanned time
        :type LastScanTime: str
        :param ImpactedHostNum: Number of affected servers
        :type ImpactedHostNum: int
        :param VulStatus: Vulnerability status
* UN_OPERATED: to be processed
* FIXED: fixed
        :type VulStatus: str
        """
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


class WeeklyReport(AbstractModel):
    """Weekly report list.

    """

    def __init__(self):
        """
        :param BeginDate: Weekly report start time.
        :type BeginDate: str
        :param EndDate: Weekly report end time.
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class WeeklyReportBruteAttack(AbstractModel):
    """Brute force attack data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param Username: Hacked username.
        :type Username: str
        :param SrcIp: Source IP.
        :type SrcIp: str
        :param Count: Number of attempts.
        :type Count: int
        :param AttackTime: Attack time.
        :type AttackTime: str
        """
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


class WeeklyReportMalware(AbstractModel):
    """Trojan data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param FilePath: Trojan file path.
        :type FilePath: str
        :param Md5: Trojan file MD5 value.
        :type Md5: str
        :param FindTime: Trojan discovery time.
        :type FindTime: str
        :param Status: Current trojan status.
<li>UN_OPERATED: not processed</li>
<li>SEGREGATED: isolated</li>
<li>TRUSTED: trusted</li>
<li>SEPARATING: isolating</li>
<li>RECOVERING: recovering</li>
        :type Status: str
        """
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


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """Unusual login location data in weekly CWP Pro report

    """

    def __init__(self):
        """
        :param MachineIp: Server IP.
        :type MachineIp: str
        :param Username: Username.
        :type Username: str
        :param SrcIp: Source IP.
        :type SrcIp: str
        :param Country: Country/Region ID.
        :type Country: int
        :param Province: Province/State ID.
        :type Province: int
        :param City: City ID.
        :type City: int
        :param LoginTime: Login time.
        :type LoginTime: str
        """
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


class WeeklyReportVul(AbstractModel):
    """Vulnerability data in weekly CWP Pro report.

    """

    def __init__(self):
        """
        :param MachineIp: Private IP of server.
        :type MachineIp: str
        :param VulName: Vulnerability name.
        :type VulName: str
        :param VulType: Vulnerability type.
<li> WEB: web vulnerability</li>
<li> SYSTEM: system component vulnerability</li>
<li> BASELINE: security baseline</li>
        :type VulType: str
        :param Description: Vulnerability description.
        :type Description: str
        :param VulStatus: Vulnerability status.
<li> UN_OPERATED: to be processed</li>
<li> SCANING: scanning</li>
<li> FIXED: fixed</li>
        :type VulStatus: str
        :param LastScanTime: Last scanned time.
        :type LastScanTime: str
        """
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