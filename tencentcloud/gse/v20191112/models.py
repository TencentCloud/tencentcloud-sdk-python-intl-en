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


class CcnInfo(AbstractModel):
    """CCN information

    """

    def __init__(self):
        """
        :param AccountId: Account of the CCN instance owner\n        :type AccountId: str\n        :param CcnId: CCN ID\n        :type CcnId: str\n        """
        self.AccountId = None
        self.CcnId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetRequest(AbstractModel):
    """CopyFleet request structure.

    """

    def __init__(self):
        """
        :param FleetId: Server fleet ID\n        :type FleetId: str\n        :param CopyNumber: Replica number. It should a value between 1 to the number of the remaining quota. It can be obtained through [Obtaining User Quota](https://intl.cloud.tencent.com/document/product/1165/48732?from_cn_redirect=1).\n        :type CopyNumber: int\n        :param AssetId: Asset package ID\n        :type AssetId: str\n        :param Description: Description. The length is 0-100 characters.\n        :type Description: str\n        :param InboundPermissions: Network configuration\n        :type InboundPermissions: list of InboundPermission\n        :param InstanceType: Server type. It can be obtained through [Obtaining Server Instance Type List](https://intl.cloud.tencent.com/document/product/1165/48732?from_cn_redirect=1).\n        :type InstanceType: str\n        :param FleetType: Server fleet type, which only supports “ON_DEMAND” type now.\n        :type FleetType: str\n        :param Name: Server fleet name. The length is 1-50 characters.\n        :type Name: str\n        :param NewGameServerSessionProtectionPolicy: Protection policy. Valid values: NoProtection·(no protection), FullProtection (full protection), TimeLimitProtection (time-limited protection)\n        :type NewGameServerSessionProtectionPolicy: str\n        :param ResourceCreationLimitPolicy: Limit policy of resource creation\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param RuntimeConfiguration: Progress configuration\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        :param GameServerSessionProtectionTimeLimit: Timeout period of time-limited protection. Value range: 5-1440 minutes. Default value: 60 minutes. This parameter is valid only when NewGameSessionProtectionPolicy is set as TimeLimitProtection.\n        :type GameServerSessionProtectionTimeLimit: int\n        :param SelectedScalingType: Whether to select scaling. Valid values: SCALING_SELECTED, SCALING_UNSELECTED. Default value: SCALING_UNSELECTED.\n        :type SelectedScalingType: str\n        :param SelectedCcnType: Whether to associate the fleet with a CCN instance: CCN_SELECTED_BEFORE_CREATE (associate before creation), CCN_SELECTED_AFTER_CREATE (associated after creation), or CCN_UNSELECTED (do not associate); CCN_UNSELECTED by default\n        :type SelectedCcnType: str\n        :param Tags: Tag list. Up to 50 tags.\n        :type Tags: list of Tag\n        :param SystemDiskInfo: System disk. It can be a SSD (CLOUD_SSD) with 100-500 GB capacity or a Premium Cloud Storage disk (CLOUD_PREMIUM) with 50-500 GB capacity. The increment is 1.\n        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`\n        :param DataDiskInfo: Data disk. It can be SSD disks (CLOUD_SSD) with 100-32000 GB capacity or Premium Cloud Storage disks (CLOUD_PREMIUM) with 10-32000 GB capacity. The increment is 10. \n        :type DataDiskInfo: list of DiskInfo\n        :param SelectedTimerType: Whether to select to replicate the timer policy: TIMER_SELECTED or TIMER_UNSELECTED. The default value is TIMER_UNSELECTED.\n        :type SelectedTimerType: str\n        :param CcnInfos: Information of the CCN instance, including the owner account and the instance ID.\n        :type CcnInfos: list of CcnInfo\n        :param InternetMaxBandwidthOut: Maximum outbound public network bandwidth of the server fleet. Value range: 1 - 200 Mbps. Default value: 100 Mbps.\n        :type InternetMaxBandwidthOut: int\n        """
        self.FleetId = None
        self.CopyNumber = None
        self.AssetId = None
        self.Description = None
        self.InboundPermissions = None
        self.InstanceType = None
        self.FleetType = None
        self.Name = None
        self.NewGameServerSessionProtectionPolicy = None
        self.ResourceCreationLimitPolicy = None
        self.RuntimeConfiguration = None
        self.GameServerSessionProtectionTimeLimit = None
        self.SelectedScalingType = None
        self.SelectedCcnType = None
        self.Tags = None
        self.SystemDiskInfo = None
        self.DataDiskInfo = None
        self.SelectedTimerType = None
        self.CcnInfos = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.CopyNumber = params.get("CopyNumber")
        self.AssetId = params.get("AssetId")
        self.Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self.InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self.InboundPermissions.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.FleetType = params.get("FleetType")
        self.Name = params.get("Name")
        self.NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self.SelectedScalingType = params.get("SelectedScalingType")
        self.SelectedCcnType = params.get("SelectedCcnType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self.SystemDiskInfo = DiskInfo()
            self.SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self.DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDiskInfo.append(obj)
        self.SelectedTimerType = params.get("SelectedTimerType")
        if params.get("CcnInfos") is not None:
            self.CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self.CcnInfos.append(obj)
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetResponse(AbstractModel):
    """CopyFleet response structure.

    """

    def __init__(self):
        """
        :param FleetAttributes: Server fleet attributes
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type FleetAttributes: list of FleetAttributes\n        :param TotalCount: The number of server fleets\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FleetAttributes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self.FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self.FleetAttributes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession request structure.

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.\n        :type MaximumPlayerSessionCount: int\n        :param AliasId: Alias ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.\n        :type AliasId: str\n        :param CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.\n        :type CreatorId: str\n        :param FleetId: Fleet ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.\n        :type FleetId: str\n        :param GameProperties: Game attributes. Up to 16 groups of attributes are allowed.\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.\n        :type GameServerSessionData: str\n        :param GameServerSessionId: The custom ID of game server session. Up to 4096 ASCII characters are allowed.\n        :type GameServerSessionId: str\n        :param IdempotencyToken: Idempotency token. Up to 48 ASCII characters are allowed.\n        :type IdempotencyToken: str\n        :param Name: The name of game server session. Up to 1024 ASCII characters are allowed.\n        :type Name: str\n        """
        self.MaximumPlayerSessionCount = None
        self.AliasId = None
        self.CreatorId = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IdempotencyToken = None
        self.Name = None


    def _deserialize(self, params):
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.AliasId = params.get("AliasId")
        self.CreatorId = params.get("CreatorId")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IdempotencyToken = params.get("IdempotencyToken")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession response structure.

    """

    def __init__(self):
        """
        :param GameServerSession: Game server session
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """Credentials required for instance access

    """

    def __init__(self):
        """
        :param Secret: SSH private key\n        :type Secret: str\n        :param UserName: Username\n        :type UserName: str\n        """
        self.Secret = None
        self.UserName = None


    def _deserialize(self, params):
        self.Secret = params.get("Secret")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyRequest(AbstractModel):
    """DeleteTimerScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param TimerId: Unique ID of the policy\n        :type TimerId: str\n        :param FleetId: ID of the fleet to be bound with the policy\n        :type FleetId: str\n        :param TimerName: Scheduled scaling policy name\n        :type TimerName: str\n        """
        self.TimerId = None
        self.FleetId = None
        self.TimerName = None


    def _deserialize(self, params):
        self.TimerId = params.get("TimerId")
        self.FleetId = params.get("FleetId")
        self.TimerName = params.get("TimerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyResponse(AbstractModel):
    """DeleteTimerScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails request structure.

    """

    def __init__(self):
        """
        :param AliasId: Alias ID\n        :type AliasId: str\n        :param FleetId: Fleet ID\n        :type FleetId: str\n        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.\n        :type GameServerSessionId: str\n        :param Limit: Maximum number of entries in a single query\n        :type Limit: int\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.\n        :type NextToken: str\n        :param StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR\n        :type StatusFilter: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: List of game server session details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessionDetails: list of GameServerSessionDetail\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type NextToken: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessionDetails = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self.GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self.GameServerSessionDetails.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement request structure.

    """

    def __init__(self):
        """
        :param PlacementId: Unique ID of game server session placement\n        :type PlacementId: str\n        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions request structure.

    """

    def __init__(self):
        """
        :param AliasId: Alias ID\n        :type AliasId: str\n        :param FleetId: Fleet ID\n        :type FleetId: str\n        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.\n        :type GameServerSessionId: str\n        :param Limit: Maximum number of entries in a single query\n        :type Limit: int\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.\n        :type NextToken: str\n        :param StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR\n        :type StatusFilter: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions response structure.

    """

    def __init__(self):
        """
        :param GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessions: list of GameServerSession\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type NextToken: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypesRequest(AbstractModel):
    """DescribeInstanceTypes request structure.

    """


class DescribeInstanceTypesResponse(AbstractModel):
    """DescribeInstanceTypes response structure.

    """

    def __init__(self):
        """
        :param InstanceTypeList: List of server types\n        :type InstanceTypeList: list of InstanceTypeInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeList") is not None:
            self.InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = InstanceTypeInfo()
                obj._deserialize(item)
                self.InstanceTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.\n        :type GameServerSessionId: str\n        :param Limit: Maximum number of entries in a single query\n        :type Limit: int\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.\n        :type NextToken: str\n        :param PlayerId: Player ID. It should contain 1 to 1024 ASCII characters.\n        :type PlayerId: str\n        :param PlayerSessionId: Player session ID. It should contain 1 to 1024 ASCII characters.\n        :type PlayerSessionId: str\n        :param PlayerSessionStatusFilter: Player session status. Valid values: RESERVED, ACTIVE, COMPLETED, TIMEDOUT\n        :type PlayerSessionStatusFilter: str\n        """
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.PlayerSessionStatusFilter = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions response structure.

    """

    def __init__(self):
        """
        :param PlayerSessions: Player session list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlayerSessions: list of PlayerSession\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type NextToken: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PlayerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeTimerScalingPoliciesRequest(AbstractModel):
    """DescribeTimerScalingPolicies request structure.

    """

    def __init__(self):
        """
        :param FleetId: ID of the fleet to be bound with the policy\n        :type FleetId: str\n        :param TimerName: Scheduled scaling policy name\n        :type TimerName: str\n        :param BeginTime: Start time of the scheduled scaling policy\n        :type BeginTime: str\n        :param EndTime: End time of the scheduled scaling policy\n        :type EndTime: str\n        :param Offset: Pagination offset\n        :type Offset: int\n        :param Limit: Number of entries per page\n        :type Limit: int\n        """
        self.FleetId = None
        self.TimerName = None
        self.BeginTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.TimerName = params.get("TimerName")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimerScalingPoliciesResponse(AbstractModel):
    """DescribeTimerScalingPolicies response structure.

    """

    def __init__(self):
        """
        :param TimerScalingPolicies: Configuration of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TimerScalingPolicies: list of TimerScalingPolicy\n        :param TotalCount: Total number of scheduled scaling policies
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TimerScalingPolicies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TimerScalingPolicies") is not None:
            self.TimerScalingPolicies = []
            for item in params.get("TimerScalingPolicies"):
                obj = TimerScalingPolicy()
                obj._deserialize(item)
                self.TimerScalingPolicies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """Player game session information

    """

    def __init__(self):
        """
        :param PlayerId: Unique player ID associated with player session\n        :type PlayerId: str\n        :param PlayerData: Developer-defined player data\n        :type PlayerData: str\n        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    """Disk storage information

    """

    def __init__(self):
        """
        :param DiskType: Disk type: Premium Cloud Storage (CLOUD_PREMIUM) or SSD (CLOUD_SSD)\n        :type DiskType: str\n        :param DiskSize: System disk: the available disk capacity is 50-500 GB. Data disk: the available disk capacity is 100-32000 GB, and the value is a multiple of 10. When the disk type is SSD (CLOUD_SSD), the minimum capacity is 100 GB.\n        :type DiskSize: int\n        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessRequest(AbstractModel):
    """EndGameServerSessionAndProcess request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. If a game server session ID is passed in, its corresponding processes, game server sessions, and player sessions will be terminated.\n        :type GameServerSessionId: str\n        :param IpAddress: The public IP of the CVM. You need to pass in `IpAddress` and `Port` at the same time to terminate the matched processes, game server sessions and player sessions (if any exists). It does not take effect in case only the `IpAddress` passed in.\n        :type IpAddress: str\n        :param Port: Port number. Value range: 1025 - 60000. You need to pass in `IpAddress` and `Port` at the same time to terminate the matched processes, game server sessions (if any exists) and player sessions (if any exists). It does not take effect in case only the `IpAddress` passed in.\n        :type Port: int\n        """
        self.GameServerSessionId = None
        self.IpAddress = None
        self.Port = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessResponse(AbstractModel):
    """EndGameServerSessionAndProcess response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FleetAttributes(AbstractModel):
    """Service deployment attributes

    """

    def __init__(self):
        """
        :param AssetId: Asset package ID\n        :type AssetId: str\n        :param CreationTime: Server fleet creation time\n        :type CreationTime: str\n        :param Description: Description
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Description: str\n        :param FleetArn: Description of server fleet resource
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type FleetArn: str\n        :param FleetId: Server fleet ID
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type FleetId: str\n        :param FleetType: Server fleet type, which only supports ON_DEMAND now.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type FleetType: str\n        :param InstanceType: Server type, such as S5.LARGE8
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type InstanceType: str\n        :param Name: Server fleet name\n        :type Name: str\n        :param NewGameServerSessionProtectionPolicy: Game session protection policy
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type NewGameServerSessionProtectionPolicy: str\n        :param OperatingSystem: Operating system type
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type OperatingSystem: str\n        :param ResourceCreationLimitPolicy: Limit policy of resource creation
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param Status: Statuses: “Create”, “Downloading”, “Verifying”, “Generating”, “Activating”, “Active”, “Exception”, “Deleting”, and “End”.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Status: str\n        :param StoppedActions: The status of server fleet when it stopped. If this field is left empty, it means automatic scaling.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type StoppedActions: list of str\n        :param TerminationTime: Server fleet termination time
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TerminationTime: str\n        :param GameServerSessionProtectionTimeLimit: Timeout period of time-limited protection. Value range: 5-1440 minutes. Default value: 60 minutes.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type GameServerSessionProtectionTimeLimit: int\n        :param BillingStatus: Billing status: Unactivated, Activated, Exception, Isolated due to arrears, Terminated, and Unfrozen.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type BillingStatus: str\n        :param Tags: Tag list. Up to 50 tags.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Tags: list of Tag\n        :param DataDiskInfo: Data disk. It can be SSD disks (CLOUD_SSD) with 100-32000 GB capacity or Premium Cloud Storage disks (CLOUD_PREMIUM) with 10-32000 GB capacity. The increment is 10. 
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type DataDiskInfo: list of DiskInfo\n        :param SystemDiskInfo: System disk. It can be a SSD (CLOUD_SSD) with 100-500 GB capacity or a Premium Cloud Storage disk (CLOUD_PREMIUM) with 50-500 GB capacity. The increment is 1.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`\n        :param RelatedCcnInfos: CCN instance information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RelatedCcnInfos: list of RelatedCcnInfo\n        :param InternetMaxBandwidthOut: Maximum outbound public network bandwidth of the server fleet. Value range: 1 - 200 Mbps. Default value: 100 Mbps.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InternetMaxBandwidthOut: int\n        """
        self.AssetId = None
        self.CreationTime = None
        self.Description = None
        self.FleetArn = None
        self.FleetId = None
        self.FleetType = None
        self.InstanceType = None
        self.Name = None
        self.NewGameServerSessionProtectionPolicy = None
        self.OperatingSystem = None
        self.ResourceCreationLimitPolicy = None
        self.Status = None
        self.StoppedActions = None
        self.TerminationTime = None
        self.GameServerSessionProtectionTimeLimit = None
        self.BillingStatus = None
        self.Tags = None
        self.DataDiskInfo = None
        self.SystemDiskInfo = None
        self.RelatedCcnInfos = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.CreationTime = params.get("CreationTime")
        self.Description = params.get("Description")
        self.FleetArn = params.get("FleetArn")
        self.FleetId = params.get("FleetId")
        self.FleetType = params.get("FleetType")
        self.InstanceType = params.get("InstanceType")
        self.Name = params.get("Name")
        self.NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self.OperatingSystem = params.get("OperatingSystem")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self.Status = params.get("Status")
        self.StoppedActions = params.get("StoppedActions")
        self.TerminationTime = params.get("TerminationTime")
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self.BillingStatus = params.get("BillingStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("DataDiskInfo") is not None:
            self.DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDiskInfo.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self.SystemDiskInfo = DiskInfo()
            self.SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("RelatedCcnInfos") is not None:
            self.RelatedCcnInfos = []
            for item in params.get("RelatedCcnInfos"):
                obj = RelatedCcnInfo()
                obj._deserialize(item)
                self.RelatedCcnInfos.append(obj)
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameProperty(AbstractModel):
    """Game attribute details

    """

    def __init__(self):
        """
        :param Key: Attribute name. Up to 32 ASCII characters are allowed.\n        :type Key: str\n        :param Value: Attribute value. Up to 96 ASCII characters are allowed.\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSession(AbstractModel):
    """Game session details

    """

    def __init__(self):
        """
        :param CreationTime: Game server session creation time\n        :type CreationTime: str\n        :param CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CreatorId: str\n        :param CurrentPlayerSessionCount: The current number of players, which cannot be less than 0.\n        :type CurrentPlayerSessionCount: int\n        :param DnsName: CVM DNS ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DnsName: str\n        :param FleetId: Fleet ID\n        :type FleetId: str\n        :param GameProperties: Game attributes. Up to 16 groups of attributes are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type GameServerSessionData: str\n        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.\n        :type GameServerSessionId: str\n        :param IpAddress: CVM IP address\n        :type IpAddress: str\n        :param MatchmakerData: Battle progress details. Up to 400,000 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchmakerData: str\n        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.\n        :type MaximumPlayerSessionCount: int\n        :param Name: The name of game server session. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Name: str\n        :param PlayerSessionCreationPolicy: Player session creation policy. Valid values: ACCEPT_ALL, DENY_ALL
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type PlayerSessionCreationPolicy: str\n        :param Port: Port number. It should be a value between 1 to 60000.\n        :type Port: int\n        :param Status: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR\n        :type Status: str\n        :param StatusReason: Additional information of game server session status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusReason: str\n        :param TerminationTime: Termination time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TerminationTime: str\n        :param InstanceType: Instance type. Up to 128 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type InstanceType: str\n        :param CurrentCustomCount: Current custom count
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CurrentCustomCount: int\n        :param MaxCustomCount: Maximum custom count
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxCustomCount: int\n        :param Weight: Weight
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Weight: int\n        :param AvailabilityStatus: Session availability status, i.e., whether it is blocked. Valid value: Enable, Disable
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AvailabilityStatus: str\n        """
        self.CreationTime = None
        self.CreatorId = None
        self.CurrentPlayerSessionCount = None
        self.DnsName = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.MatchmakerData = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.Port = None
        self.Status = None
        self.StatusReason = None
        self.TerminationTime = None
        self.InstanceType = None
        self.CurrentCustomCount = None
        self.MaxCustomCount = None
        self.Weight = None
        self.AvailabilityStatus = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreatorId = params.get("CreatorId")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.MatchmakerData = params.get("MatchmakerData")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.TerminationTime = params.get("TerminationTime")
        self.InstanceType = params.get("InstanceType")
        self.CurrentCustomCount = params.get("CurrentCustomCount")
        self.MaxCustomCount = params.get("MaxCustomCount")
        self.Weight = params.get("Weight")
        self.AvailabilityStatus = params.get("AvailabilityStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionDetail(AbstractModel):
    """Game server session details (GameServerSessionDetail)

    """

    def __init__(self):
        """
        :param GameServerSession: Game server session\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param ProtectionPolicy: Protection policy. Valid values: NoProtection, FullProtection
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProtectionPolicy: str\n        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionPlacement(AbstractModel):
    """Game session deployment object

    """

    def __init__(self):
        """
        :param PlacementId: Deployment ID\n        :type PlacementId: str\n        :param GameServerSessionQueueName: Service deployment group name\n        :type GameServerSessionQueueName: str\n        :param PlayerLatencies: Player latency
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlayerLatencies: list of PlayerLatency\n        :param Status: Service deployment status\n        :type Status: str\n        :param DnsName: DNS ID assigned to the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DnsName: str\n        :param GameServerSessionId: Game session ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessionId: str\n        :param GameServerSessionName: Game session name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessionName: str\n        :param GameServerSessionRegion: Service deployment region
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessionRegion: str\n        :param GameProperties: Game attributes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameProperties: list of GameProperty\n        :param MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.\n        :type MaximumPlayerSessionCount: int\n        :param GameServerSessionData: Game session data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessionData: str\n        :param IpAddress: IP address of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpAddress: str\n        :param Port: Port number of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Port: int\n        :param MatchmakerData: Game match data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MatchmakerData: str\n        :param PlacedPlayerSessions: Deployed player game data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlacedPlayerSessions: list of PlacedPlayerSession\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.PlayerLatencies = None
        self.Status = None
        self.DnsName = None
        self.GameServerSessionId = None
        self.GameServerSessionName = None
        self.GameServerSessionRegion = None
        self.GameProperties = None
        self.MaximumPlayerSessionCount = None
        self.GameServerSessionData = None
        self.IpAddress = None
        self.Port = None
        self.MatchmakerData = None
        self.PlacedPlayerSessions = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        self.Status = params.get("Status")
        self.DnsName = params.get("DnsName")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.GameServerSessionName = params.get("GameServerSessionName")
        self.GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        self.MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self.PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self.PlacedPlayerSessions.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.\n        :type GameServerSessionId: str\n        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl response structure.

    """

    def __init__(self):
        """
        :param PreSignedUrl: Log download URL. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type PreSignedUrl: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess request structure.

    """

    def __init__(self):
        """
        :param FleetId: Server fleet ID\n        :type FleetId: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        """
        self.FleetId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess response structure.

    """

    def __init__(self):
        """
        :param InstanceAccess: Credentials required for instance login\n        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self.InstanceAccess = InstanceAccess()
            self.InstanceAccess._deserialize(params.get("InstanceAccess"))
        self.RequestId = params.get("RequestId")


class InboundPermission(AbstractModel):
    """Allowed network range.

    """

    def __init__(self):
        """
        :param FromPort: Start port number. Minimum value: 1025.\n        :type FromPort: int\n        :param IpRange: IP range. Valid range of the input IPv4 addresses in CIDR format; for example, 0.0.0.0.0/0.\n        :type IpRange: str\n        :param Protocol: Protocol type: TCP or UDP.\n        :type Protocol: str\n        :param ToPort: End port number. Maximum value: 60000.\n        :type ToPort: int\n        """
        self.FromPort = None
        self.IpRange = None
        self.Protocol = None
        self.ToPort = None


    def _deserialize(self, params):
        self.FromPort = params.get("FromPort")
        self.IpRange = params.get("IpRange")
        self.Protocol = params.get("Protocol")
        self.ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAccess(AbstractModel):
    """Identity credentials for instance access

    """

    def __init__(self):
        """
        :param Credentials: Credentials required for instance access\n        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`\n        :param FleetId: Service deployment ID\n        :type FleetId: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param IpAddress: Public IP of instance\n        :type IpAddress: str\n        :param OperatingSystem: OS\n        :type OperatingSystem: str\n        """
        self.Credentials = None
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.OperatingSystem = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.OperatingSystem = params.get("OperatingSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeInfo(AbstractModel):
    """The server instance type information

    """

    def __init__(self):
        """
        :param TypeName: Name of the server type, such as `Standard SA1`\n        :type TypeName: str\n        :param InstanceType: Specification of the server type, such as `SA1.SMALL1`\n        :type InstanceType: str\n        :param Cpu: CPU, in core\n        :type Cpu: int\n        :param Memory: Memory, in GB\n        :type Memory: int\n        :param NetworkCard: The packet sending and receiving capability, in 10k PPS. \n        :type NetworkCard: int\n        """
        self.TypeName = None
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.NetworkCard = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.NetworkCard = params.get("NetworkCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchRequest(AbstractModel):
    """JoinGameServerSessionBatch request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.\n        :type GameServerSessionId: str\n        :param PlayerIds: Player ID list. At least 1 ID and up to 25 IDs.\n        :type PlayerIds: list of str\n        :param PlayerDataMap: Player custom data\n        :type PlayerDataMap: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`\n        """
        self.GameServerSessionId = None
        self.PlayerIds = None
        self.PlayerDataMap = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerIds = params.get("PlayerIds")
        if params.get("PlayerDataMap") is not None:
            self.PlayerDataMap = PlayerDataMap()
            self.PlayerDataMap._deserialize(params.get("PlayerDataMap"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchResponse(AbstractModel):
    """JoinGameServerSessionBatch response structure.

    """

    def __init__(self):
        """
        :param PlayerSessions: Player session list. Up to 25 sessions.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type PlayerSessions: list of PlayerSession\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PlayerSessions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.RequestId = params.get("RequestId")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.\n        :type GameServerSessionId: str\n        :param PlayerId: Player ID. Up to 1024 ASCII characters are allowed.\n        :type PlayerId: str\n        :param PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.\n        :type PlayerData: str\n        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession response structure.

    """

    def __init__(self):
        """
        :param PlayerSession: Player session
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PlayerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self.PlayerSession = PlayerSession()
            self.PlayerSession._deserialize(params.get("PlayerSession"))
        self.RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """Deployed player game session

    """

    def __init__(self):
        """
        :param PlayerId: Player ID\n        :type PlayerId: str\n        :param PlayerSessionId: Player session ID\n        :type PlayerSessionId: str\n        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerDataMap(AbstractModel):
    """Player custom data

    """

    def __init__(self):
        """
        :param Key: The key of player custom data. It should contain 1 to 1024 ASCII characters.\n        :type Key: str\n        :param Value: The value of player custom data. It should contain 1 to 2048 ASCII characters.\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerLatency(AbstractModel):
    """Player latency information

    """

    def __init__(self):
        """
        :param PlayerId: Player ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PlayerId: str\n        :param RegionIdentifier: Name of region corresponding to latency
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegionIdentifier: str\n        :param LatencyInMilliseconds: Latency in milliseconds\n        :type LatencyInMilliseconds: int\n        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerSession(AbstractModel):
    """Player session details

    """

    def __init__(self):
        """
        :param CreationTime: Player session creation time\n        :type CreationTime: str\n        :param DnsName: ID of the DNS where the game server session is running
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DnsName: str\n        :param FleetId: Fleet ID\n        :type FleetId: str\n        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.\n        :type GameServerSessionId: str\n        :param IpAddress: Address of the CVM instance where the game server session is running\n        :type IpAddress: str\n        :param PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type PlayerData: str\n        :param PlayerId: Player ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type PlayerId: str\n        :param PlayerSessionId: Player session ID\n        :type PlayerSessionId: str\n        :param Port: Port number. It should be a value between 1 to 60000.\n        :type Port: int\n        :param Status: Player session status. Valid values: RESERVED = 1, ACTIVE = 2, COMPLETED =3, TIMEDOUT = 4\n        :type Status: str\n        :param TerminationTime: Player session termination time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TerminationTime: str\n        """
        self.CreationTime = None
        self.DnsName = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.PlayerData = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.Port = None
        self.Status = None
        self.TerminationTime = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.PlayerData = params.get("PlayerData")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.TerminationTime = params.get("TerminationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyRequest(AbstractModel):
    """PutTimerScalingPolicy request structure.

    """

    def __init__(self):
        """
        :param TimerScalingPolicy: Configuration of the scheduled scaling policy\n        :type TimerScalingPolicy: :class:`tencentcloud.gse.v20191112.models.TimerScalingPolicy`\n        """
        self.TimerScalingPolicy = None


    def _deserialize(self, params):
        if params.get("TimerScalingPolicy") is not None:
            self.TimerScalingPolicy = TimerScalingPolicy()
            self.TimerScalingPolicy._deserialize(params.get("TimerScalingPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyResponse(AbstractModel):
    """PutTimerScalingPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RelatedCcnInfo(AbstractModel):
    """Information of the associated CCN instance

    """

    def __init__(self):
        """
        :param AccountId: Account of the CCN instance owner\n        :type AccountId: str\n        :param CcnId: CCN instance ID\n        :type CcnId: str\n        :param AttachType: Status of associated CCN instance\n        :type AttachType: str\n        """
        self.AccountId = None
        self.CcnId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceCreationLimitPolicy(AbstractModel):
    """Resource creation policy

    """

    def __init__(self):
        """
        :param NewGameServerSessionsPerCreator: Creation quantity. Minimum value: 1. Default value: 2.\n        :type NewGameServerSessionsPerCreator: int\n        :param PolicyPeriodInMinutes: Unit time. Minimum value: 1. Default value: 3. Unit: minute.\n        :type PolicyPeriodInMinutes: int\n        """
        self.NewGameServerSessionsPerCreator = None
        self.PolicyPeriodInMinutes = None


    def _deserialize(self, params):
        self.NewGameServerSessionsPerCreator = params.get("NewGameServerSessionsPerCreator")
        self.PolicyPeriodInMinutes = params.get("PolicyPeriodInMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfiguration(AbstractModel):
    """Runtime configuration

    """

    def __init__(self):
        """
        :param GameServerSessionActivationTimeoutSeconds: Game session timeout. Value range: 1-600. Unit: second.\n        :type GameServerSessionActivationTimeoutSeconds: int\n        :param MaxConcurrentGameServerSessionActivations: Maximum number of game sessions. Value range: 1-2,147,483,647.\n        :type MaxConcurrentGameServerSessionActivations: int\n        :param ServerProcesses: Service process configuration. There must be at least one service configuration.\n        :type ServerProcesses: list of ServerProcesse\n        """
        self.GameServerSessionActivationTimeoutSeconds = None
        self.MaxConcurrentGameServerSessionActivations = None
        self.ServerProcesses = None


    def _deserialize(self, params):
        self.GameServerSessionActivationTimeoutSeconds = params.get("GameServerSessionActivationTimeoutSeconds")
        self.MaxConcurrentGameServerSessionActivations = params.get("MaxConcurrentGameServerSessionActivations")
        if params.get("ServerProcesses") is not None:
            self.ServerProcesses = []
            for item in params.get("ServerProcesses"):
                obj = ServerProcesse()
                obj._deserialize(item)
                self.ServerProcesses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions request structure.

    """

    def __init__(self):
        """
        :param AliasId: Alias ID\n        :type AliasId: str\n        :param FleetId: Fleet ID\n        :type FleetId: str\n        :param Limit: Maximum number of entries in a single query\n        :type Limit: int\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.\n        :type NextToken: str\n        :param FilterExpression: Search filter expression. Valid values:
gameServerSessionName: game session name in `String` type
gameServerSessionId: game session ID in `String` type
maximumSessions: maximum number of player sessions in `Number` type
creationTimeMillis: creation time in milliseconds in `Number` type
playerSessionCount: current number of player sessions in `Number` type
hasAvailablePlayerSessions: whether there is available player session in `String` type. Valid values: true, false
gameServerSessionProperties: game session attributes in `String` type

Expressions in `String` type support = and <> for judgment
Expressions in `Number` type support =, <>, >, >=, <, and <= for judgment

Example:
If FilterExpression takes the value:
playerSessionCount>=2 AND hasAvailablePlayerSessions=true"
It means searching for game sessions that have at least two players and have player sessions available.
If FilterExpression takes the value:
gameServerSessionProperties.K1 = 'V1' AND gameServerSessionProperties.K2 = 'V2' OR gameServerSessionProperties.K3 = 'V3'

it means
searching for game sessions that meets the following game server session attributes
{
    "GameProperties":[
        {
            "Key":"K1",
            "Value":"V1"
        },
        {
            "Key":"K2",
            "Value":"V2"
        },
        {
            "Key":"K3",
            "Value":"V3"
        }
    ]
}\n        :type FilterExpression: str\n        :param SortExpression: Sorting keyword
Valid values:
gameServerSessionName: game session name in `String` type
gameServerSessionId: game session ID in `String` type
maximumSessions: maximum number of player sessions in `Number` type
creationTimeMillis: creation time in milliseconds in `Number` type
playerSessionCount: current number of player sessions in `Number` type\n        :type SortExpression: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.Limit = None
        self.NextToken = None
        self.FilterExpression = None
        self.SortExpression = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.FilterExpression = params.get("FilterExpression")
        self.SortExpression = params.get("SortExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions response structure.

    """

    def __init__(self):
        """
        :param GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GameServerSessions: list of GameServerSession\n        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type NextToken: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class ServerProcesse(AbstractModel):
    """Game service process

    """

    def __init__(self):
        """
        :param ConcurrentExecutions: Number of concurrent processes. Value range of total concurrent processes: 1-50.\n        :type ConcurrentExecutions: int\n        :param LaunchPath: Launch Path. Linux: /local/game/ or Windows: C:\game\. The path length is 1-1024.\n        :type LaunchPath: str\n        :param Parameters: Launch parameter. The length is 0-1024.\n        :type Parameters: str\n        """
        self.ConcurrentExecutions = None
        self.LaunchPath = None
        self.Parameters = None


    def _deserialize(self, params):
        self.ConcurrentExecutions = params.get("ConcurrentExecutions")
        self.LaunchPath = params.get("LaunchPath")
        self.Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedRequest(AbstractModel):
    """SetServerReserved request structure.

    """

    def __init__(self):
        """
        :param FleetId: ID of the fleet to be bound with the policy\n        :type FleetId: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ReserveValue: Whether the instance is retained. Valid values: 1 (retained), 0 (not retained). Default value: 0.\n        :type ReserveValue: int\n        """
        self.FleetId = None
        self.InstanceId = None
        self.ReserveValue = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.ReserveValue = params.get("ReserveValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedResponse(AbstractModel):
    """SetServerReserved response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement request structure.

    """

    def __init__(self):
        """
        :param PlacementId: The unique ID of the game server session placement. It should contain up to 48 ASCII characters, supporting [a-zA-Z0-9-]+.\n        :type PlacementId: str\n        :param GameServerSessionQueueName: Game server session queue name\n        :type GameServerSessionQueueName: str\n        :param MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.\n        :type MaximumPlayerSessionCount: int\n        :param DesiredPlayerSessions: Player game session information\n        :type DesiredPlayerSessions: list of DesiredPlayerSession\n        :param GameProperties: Player game session attributes\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: Data of game server sessions. Up to 4096 ASCII characters are allowed.\n        :type GameServerSessionData: str\n        :param GameServerSessionName: Name of game server sessions. Up to 4096 ASCII characters are allowed.\n        :type GameServerSessionName: str\n        :param PlayerLatencies: Player latency\n        :type PlayerLatencies: list of PlayerLatency\n        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.MaximumPlayerSessionCount = None
        self.DesiredPlayerSessions = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionName = None
        self.PlayerLatencies = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self.DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self.DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement request structure.

    """

    def __init__(self):
        """
        :param PlacementId: Unique ID of game server session placement\n        :type PlacementId: str\n        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag structure

    """

    def __init__(self):
        """
        :param Key: Tag key. Up to 127 bytes are allowed.\n        :type Key: str\n        :param Value: Tag value. Up to 255 bytes are allowed.\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetConfiguration(AbstractModel):
    """Configuration of target tracking scaling

    """

    def __init__(self):
        """
        :param TargetValue: Ratio of reserved server session resource 
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TargetValue: int\n        """
        self.TargetValue = None


    def _deserialize(self, params):
        self.TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerConfiguration(AbstractModel):
    """The recurrence pattern of auto-scaling

    """

    def __init__(self):
        """
        :param TimerType: The recurrence pattern of auto-scaling. `0`: undefined, `1`: once, `2`: daily, `3`: monthly, `4`: weekly
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerType: int\n        :param TimerValue: Details of the recurrence pattern of auto-scaling
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerValue: :class:`tencentcloud.gse.v20191112.models.TimerValue`\n        :param BeginTime: Start time of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type BeginTime: str\n        :param EndTime: End time of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type EndTime: str\n        """
        self.TimerType = None
        self.TimerValue = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.TimerType = params.get("TimerType")
        if params.get("TimerValue") is not None:
            self.TimerValue = TimerValue()
            self.TimerValue._deserialize(params.get("TimerValue"))
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerFleetCapacity(AbstractModel):
    """The capacity configurations of the scheduled scaling policy

    """

    def __init__(self):
        """
        :param FleetId: ID of the fleet to be bound with the policy
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type FleetId: str\n        :param DesiredInstances: Desired number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DesiredInstances: int\n        :param MinSize: Minimum number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MinSize: int\n        :param MaxSize: Maximum number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MaxSize: int\n        :param ScalingInterval: Scaling cooldown period, in minutes
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ScalingInterval: int\n        :param ScalingType: Scaling type. `1`: manual, `2`: automatic, `0`: undefined
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ScalingType: int\n        :param TargetConfiguration: Configuration of target tracking scaling
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`\n        """
        self.FleetId = None
        self.DesiredInstances = None
        self.MinSize = None
        self.MaxSize = None
        self.ScalingInterval = None
        self.ScalingType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.DesiredInstances = params.get("DesiredInstances")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.ScalingInterval = params.get("ScalingInterval")
        self.ScalingType = params.get("ScalingType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerScalingPolicy(AbstractModel):
    """Configurations of a scheduled scaling policy

    """

    def __init__(self):
        """
        :param TimerId: Unique ID of the policy. When it’s filled in, the policy will be updated.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerId: str\n        :param TimerName: Scheduled scaling policy name
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerName: str\n        :param TimerStatus: Scheduled scaling policy status. `0`: Undefined, `1`: Not started, 2: Activated, `3`: Stopped, `4`: Expired
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerStatus: int\n        :param TimerFleetCapacity: The capacity configurations of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerFleetCapacity: :class:`tencentcloud.gse.v20191112.models.TimerFleetCapacity`\n        :param TimerConfiguration: The recurrence pattern of auto-scaling
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type TimerConfiguration: :class:`tencentcloud.gse.v20191112.models.TimerConfiguration`\n        """
        self.TimerId = None
        self.TimerName = None
        self.TimerStatus = None
        self.TimerFleetCapacity = None
        self.TimerConfiguration = None


    def _deserialize(self, params):
        self.TimerId = params.get("TimerId")
        self.TimerName = params.get("TimerName")
        self.TimerStatus = params.get("TimerStatus")
        if params.get("TimerFleetCapacity") is not None:
            self.TimerFleetCapacity = TimerFleetCapacity()
            self.TimerFleetCapacity._deserialize(params.get("TimerFleetCapacity"))
        if params.get("TimerConfiguration") is not None:
            self.TimerConfiguration = TimerConfiguration()
            self.TimerConfiguration._deserialize(params.get("TimerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerValue(AbstractModel):
    """Details of the recurrence pattern of the scheduled scaling policy

    """

    def __init__(self):
        """
        :param Day: Execute once every X day(s)
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Day: int\n        :param FromDay: Specify the first day to execute the scaling action in a month (execute once per day)
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type FromDay: int\n        :param ToDay: Specify the last day to execute the scaling action in a month
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ToDay: int\n        :param WeekDays: Specify the week days to repeat the scaling action. Multiple values are supported. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday). 
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type WeekDays: list of int\n        """
        self.Day = None
        self.FromDay = None
        self.ToDay = None
        self.WeekDays = None


    def _deserialize(self, params):
        self.Day = params.get("Day")
        self.FromDay = params.get("FromDay")
        self.ToDay = params.get("ToDay")
        self.WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptRequest(AbstractModel):
    """UpdateBucketAccelerateOpt request structure.

    """

    def __init__(self):
        """
        :param Allowed: `true`: enable global acceleration; `false`: disable global acceleration\n        :type Allowed: bool\n        """
        self.Allowed = None


    def _deserialize(self, params):
        self.Allowed = params.get("Allowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptResponse(AbstractModel):
    """UpdateBucketAccelerateOpt response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateBucketCORSOptRequest(AbstractModel):
    """UpdateBucketCORSOpt request structure.

    """

    def __init__(self):
        """
        :param AllowedOrigins: Allowed access source. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).\n        :type AllowedOrigins: list of str\n        :param AllowedMethods: Allowed HTTP method(s). Multiple methods are allowed, including PUT, GET, POST, and HEAD. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).\n        :type AllowedMethods: list of str\n        :param AllowedHeaders: Specifies the custom HTTP request headers that the browser is allowed to include in a CORS request. Wildcard (*) is supported, indicating allowing all headers (recommended). For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).\n        :type AllowedHeaders: list of str\n        :param MaxAgeSeconds: Sets the validity duration for the CORS configuration (in second). For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).\n        :type MaxAgeSeconds: int\n        :param ExposeHeaders: CORS response header(s) that can be exposed to the browser, case-insensitive. If this parameter is not specified, the browser can access only simple response headers Cache-Control, Content-Type, Expires, and Last-Modified by default. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).\n        :type ExposeHeaders: list of str\n        """
        self.AllowedOrigins = None
        self.AllowedMethods = None
        self.AllowedHeaders = None
        self.MaxAgeSeconds = None
        self.ExposeHeaders = None


    def _deserialize(self, params):
        self.AllowedOrigins = params.get("AllowedOrigins")
        self.AllowedMethods = params.get("AllowedMethods")
        self.AllowedHeaders = params.get("AllowedHeaders")
        self.MaxAgeSeconds = params.get("MaxAgeSeconds")
        self.ExposeHeaders = params.get("ExposeHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketCORSOptResponse(AbstractModel):
    """UpdateBucketCORSOpt response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.\n        :type GameServerSessionId: str\n        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.\n        :type MaximumPlayerSessionCount: int\n        :param Name: Name of the game server session. It should contain 1 to 1024 ASCII characters.\n        :type Name: str\n        :param PlayerSessionCreationPolicy: Player session creation policy, which includes `ACCEPT_ALL` (allow all players) and `DENY_ALL` (reject all players).\n        :type PlayerSessionCreationPolicy: str\n        :param ProtectionPolicy: Protection policy, which includes `NoProtection`·(no protection), `TimeLimitProtection` (time-limited protection) and `FullProtection` (full protection)\n        :type ProtectionPolicy: str\n        """
        self.GameServerSessionId = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession response structure.

    """

    def __init__(self):
        """
        :param GameServerSession: Updated game session\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")