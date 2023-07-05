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
        r"""
        :param _AccountId: Account of the CCN instance owner
        :type AccountId: str
        :param _CcnId: CCN ID
        :type CcnId: str
        """
        self._AccountId = None
        self._CcnId = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetRequest(AbstractModel):
    """CopyFleet request structure.

    """

    def __init__(self):
        r"""
        :param _FleetId: Server fleet ID
        :type FleetId: str
        :param _CopyNumber: Replica number. It should a value between 1 to the number of the remaining quota. It can be obtained through [Obtaining User Quota](https://intl.cloud.tencent.com/document/product/1165/48732?from_cn_redirect=1).
        :type CopyNumber: int
        :param _AssetId: Asset package ID
        :type AssetId: str
        :param _Description: Description. The length is 0-100 characters.
        :type Description: str
        :param _InboundPermissions: Network configuration
        :type InboundPermissions: list of InboundPermission
        :param _InstanceType: Server type. It can be obtained through [Obtaining Server Instance Type List](https://intl.cloud.tencent.com/document/product/1165/48732?from_cn_redirect=1).
        :type InstanceType: str
        :param _FleetType: Server fleet type, which only supports “ON_DEMAND” type now.
        :type FleetType: str
        :param _Name: Server fleet name. The length is 1-50 characters.
        :type Name: str
        :param _NewGameServerSessionProtectionPolicy: Protection policy. Valid values: NoProtection·(no protection), FullProtection (full protection), TimeLimitProtection (time-limited protection)
        :type NewGameServerSessionProtectionPolicy: str
        :param _ResourceCreationLimitPolicy: Limit policy of resource creation
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _RuntimeConfiguration: Progress configuration
        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`
        :param _GameServerSessionProtectionTimeLimit: Timeout period of time-limited protection. Value range: 5-1440 minutes. Default value: 60 minutes. This parameter is valid only when NewGameSessionProtectionPolicy is set as TimeLimitProtection.
        :type GameServerSessionProtectionTimeLimit: int
        :param _SelectedScalingType: Whether to select scaling. Valid values: SCALING_SELECTED, SCALING_UNSELECTED. Default value: SCALING_UNSELECTED.
        :type SelectedScalingType: str
        :param _SelectedCcnType: Whether to associate the fleet with a CCN instance: CCN_SELECTED_BEFORE_CREATE (associate before creation), CCN_SELECTED_AFTER_CREATE (associated after creation), or CCN_UNSELECTED (do not associate); CCN_UNSELECTED by default
        :type SelectedCcnType: str
        :param _Tags: Tag list. Up to 50 tags.
        :type Tags: list of Tag
        :param _SystemDiskInfo: System disk. It can be a SSD (CLOUD_SSD) with 100-500 GB capacity or a Premium Cloud Storage disk (CLOUD_PREMIUM) with 50-500 GB capacity. The increment is 1.
        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        :param _DataDiskInfo: Data disk. It can be SSD disks (CLOUD_SSD) with 100-32000 GB capacity or Premium Cloud Storage disks (CLOUD_PREMIUM) with 10-32000 GB capacity. The increment is 10. 
        :type DataDiskInfo: list of DiskInfo
        :param _SelectedTimerType: Whether to select to replicate the timer policy: TIMER_SELECTED or TIMER_UNSELECTED. The default value is TIMER_UNSELECTED.
        :type SelectedTimerType: str
        :param _CcnInfos: Information of the CCN instance, including the owner account and the instance ID.
        :type CcnInfos: list of CcnInfo
        :param _InternetMaxBandwidthOut: Maximum outbound public network bandwidth of the server fleet. Value range: 1 - 200 Mbps. Default value: 100 Mbps.
        :type InternetMaxBandwidthOut: int
        """
        self._FleetId = None
        self._CopyNumber = None
        self._AssetId = None
        self._Description = None
        self._InboundPermissions = None
        self._InstanceType = None
        self._FleetType = None
        self._Name = None
        self._NewGameServerSessionProtectionPolicy = None
        self._ResourceCreationLimitPolicy = None
        self._RuntimeConfiguration = None
        self._GameServerSessionProtectionTimeLimit = None
        self._SelectedScalingType = None
        self._SelectedCcnType = None
        self._Tags = None
        self._SystemDiskInfo = None
        self._DataDiskInfo = None
        self._SelectedTimerType = None
        self._CcnInfos = None
        self._InternetMaxBandwidthOut = None

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def CopyNumber(self):
        return self._CopyNumber

    @CopyNumber.setter
    def CopyNumber(self, CopyNumber):
        self._CopyNumber = CopyNumber

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InboundPermissions(self):
        return self._InboundPermissions

    @InboundPermissions.setter
    def InboundPermissions(self, InboundPermissions):
        self._InboundPermissions = InboundPermissions

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def FleetType(self):
        return self._FleetType

    @FleetType.setter
    def FleetType(self, FleetType):
        self._FleetType = FleetType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameServerSessionProtectionPolicy(self):
        return self._NewGameServerSessionProtectionPolicy

    @NewGameServerSessionProtectionPolicy.setter
    def NewGameServerSessionProtectionPolicy(self, NewGameServerSessionProtectionPolicy):
        self._NewGameServerSessionProtectionPolicy = NewGameServerSessionProtectionPolicy

    @property
    def ResourceCreationLimitPolicy(self):
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def RuntimeConfiguration(self):
        return self._RuntimeConfiguration

    @RuntimeConfiguration.setter
    def RuntimeConfiguration(self, RuntimeConfiguration):
        self._RuntimeConfiguration = RuntimeConfiguration

    @property
    def GameServerSessionProtectionTimeLimit(self):
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit

    @property
    def SelectedScalingType(self):
        return self._SelectedScalingType

    @SelectedScalingType.setter
    def SelectedScalingType(self, SelectedScalingType):
        self._SelectedScalingType = SelectedScalingType

    @property
    def SelectedCcnType(self):
        return self._SelectedCcnType

    @SelectedCcnType.setter
    def SelectedCcnType(self, SelectedCcnType):
        self._SelectedCcnType = SelectedCcnType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SystemDiskInfo(self):
        return self._SystemDiskInfo

    @SystemDiskInfo.setter
    def SystemDiskInfo(self, SystemDiskInfo):
        self._SystemDiskInfo = SystemDiskInfo

    @property
    def DataDiskInfo(self):
        return self._DataDiskInfo

    @DataDiskInfo.setter
    def DataDiskInfo(self, DataDiskInfo):
        self._DataDiskInfo = DataDiskInfo

    @property
    def SelectedTimerType(self):
        return self._SelectedTimerType

    @SelectedTimerType.setter
    def SelectedTimerType(self, SelectedTimerType):
        self._SelectedTimerType = SelectedTimerType

    @property
    def CcnInfos(self):
        return self._CcnInfos

    @CcnInfos.setter
    def CcnInfos(self, CcnInfos):
        self._CcnInfos = CcnInfos

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._CopyNumber = params.get("CopyNumber")
        self._AssetId = params.get("AssetId")
        self._Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self._InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self._InboundPermissions.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._FleetType = params.get("FleetType")
        self._Name = params.get("Name")
        self._NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self._RuntimeConfiguration = RuntimeConfiguration()
            self._RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self._SelectedScalingType = params.get("SelectedScalingType")
        self._SelectedCcnType = params.get("SelectedCcnType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self._SystemDiskInfo = DiskInfo()
            self._SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self._DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDiskInfo.append(obj)
        self._SelectedTimerType = params.get("SelectedTimerType")
        if params.get("CcnInfos") is not None:
            self._CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self._CcnInfos.append(obj)
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetResponse(AbstractModel):
    """CopyFleet response structure.

    """

    def __init__(self):
        r"""
        :param _FleetAttributes: Server fleet attributes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FleetAttributes: list of FleetAttributes
        :param _TotalCount: The number of server fleets
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FleetAttributes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FleetAttributes(self):
        return self._FleetAttributes

    @FleetAttributes.setter
    def FleetAttributes(self, FleetAttributes):
        self._FleetAttributes = FleetAttributes

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self._FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self._FleetAttributes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession request structure.

    """

    def __init__(self):
        r"""
        :param _MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param _AliasId: Alias ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.
        :type AliasId: str
        :param _CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.
        :type CreatorId: str
        :param _FleetId: Fleet ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.
        :type FleetId: str
        :param _GameProperties: Game attributes. Up to 16 groups of attributes are allowed.
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionData: str
        :param _GameServerSessionId: The custom ID of game server session. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionId: str
        :param _IdempotencyToken: Idempotency token. Up to 48 ASCII characters are allowed.
        :type IdempotencyToken: str
        :param _Name: The name of game server session. Up to 1024 ASCII characters are allowed.
        :type Name: str
        """
        self._MaximumPlayerSessionCount = None
        self._AliasId = None
        self._CreatorId = None
        self._FleetId = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionId = None
        self._IdempotencyToken = None
        self._Name = None

    @property
    def MaximumPlayerSessionCount(self):
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def AliasId(self):
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def CreatorId(self):
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IdempotencyToken(self):
        return self._IdempotencyToken

    @IdempotencyToken.setter
    def IdempotencyToken(self, IdempotencyToken):
        self._IdempotencyToken = IdempotencyToken

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._AliasId = params.get("AliasId")
        self._CreatorId = params.get("CreatorId")
        self._FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IdempotencyToken = params.get("IdempotencyToken")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSession: Game server session
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSession = None
        self._RequestId = None

    @property
    def GameServerSession(self):
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """Credentials required for instance access

    """

    def __init__(self):
        r"""
        :param _Secret: SSH private key
        :type Secret: str
        :param _UserName: Username
        :type UserName: str
        """
        self._Secret = None
        self._UserName = None

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._Secret = params.get("Secret")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyRequest(AbstractModel):
    """DeleteTimerScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _TimerId: Unique ID of the policy
        :type TimerId: str
        :param _FleetId: ID of the fleet to be bound with the policy
        :type FleetId: str
        :param _TimerName: Scheduled scaling policy name
        :type TimerName: str
        """
        self._TimerId = None
        self._FleetId = None
        self._TimerName = None

    @property
    def TimerId(self):
        return self._TimerId

    @TimerId.setter
    def TimerId(self, TimerId):
        self._TimerId = TimerId

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def TimerName(self):
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName


    def _deserialize(self, params):
        self._TimerId = params.get("TimerId")
        self._FleetId = params.get("FleetId")
        self._TimerName = params.get("TimerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyResponse(AbstractModel):
    """DeleteTimerScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails request structure.

    """

    def __init__(self):
        r"""
        :param _AliasId: Alias ID
        :type AliasId: str
        :param _FleetId: Fleet ID
        :type FleetId: str
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param _Limit: Maximum number of entries in a single query
        :type Limit: int
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param _StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type StatusFilter: str
        """
        self._AliasId = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._StatusFilter = None

    @property
    def AliasId(self):
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def StatusFilter(self):
        return self._StatusFilter

    @StatusFilter.setter
    def StatusFilter(self, StatusFilter):
        self._StatusFilter = StatusFilter


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionDetails: List of game server session details
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessionDetails = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessionDetails(self):
        return self._GameServerSessionDetails

    @GameServerSessionDetails.setter
    def GameServerSessionDetails(self, GameServerSessionDetails):
        self._GameServerSessionDetails = GameServerSessionDetails

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self._GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self._GameServerSessionDetails.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement request structure.

    """

    def __init__(self):
        r"""
        :param _PlacementId: Unique ID of game server session placement
        :type PlacementId: str
        """
        self._PlacementId = None

    @property
    def PlacementId(self):
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions request structure.

    """

    def __init__(self):
        r"""
        :param _AliasId: Alias ID
        :type AliasId: str
        :param _FleetId: Fleet ID
        :type FleetId: str
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param _Limit: Maximum number of entries in a single query
        :type Limit: int
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param _StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type StatusFilter: str
        """
        self._AliasId = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._StatusFilter = None

    @property
    def AliasId(self):
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def StatusFilter(self):
        return self._StatusFilter

    @StatusFilter.setter
    def StatusFilter(self, StatusFilter):
        self._StatusFilter = StatusFilter


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessions: list of GameServerSession
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessions(self):
        return self._GameServerSessions

    @GameServerSessions.setter
    def GameServerSessions(self, GameServerSessions):
        self._GameServerSessions = GameServerSessions

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self._GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self._GameServerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypesRequest(AbstractModel):
    """DescribeInstanceTypes request structure.

    """


class DescribeInstanceTypesResponse(AbstractModel):
    """DescribeInstanceTypes response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceTypeList: List of server types
        :type InstanceTypeList: list of InstanceTypeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceTypeList = None
        self._RequestId = None

    @property
    def InstanceTypeList(self):
        return self._InstanceTypeList

    @InstanceTypeList.setter
    def InstanceTypeList(self, InstanceTypeList):
        self._InstanceTypeList = InstanceTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeList") is not None:
            self._InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = InstanceTypeInfo()
                obj._deserialize(item)
                self._InstanceTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param _Limit: Maximum number of entries in a single query
        :type Limit: int
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param _PlayerId: Player ID. It should contain 1 to 1024 ASCII characters.
        :type PlayerId: str
        :param _PlayerSessionId: Player session ID. It should contain 1 to 1024 ASCII characters.
        :type PlayerSessionId: str
        :param _PlayerSessionStatusFilter: Player session status. Valid values: RESERVED, ACTIVE, COMPLETED, TIMEDOUT
        :type PlayerSessionStatusFilter: str
        """
        self._GameServerSessionId = None
        self._Limit = None
        self._NextToken = None
        self._PlayerId = None
        self._PlayerSessionId = None
        self._PlayerSessionStatusFilter = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId

    @property
    def PlayerSessionStatusFilter(self):
        return self._PlayerSessionStatusFilter

    @PlayerSessionStatusFilter.setter
    def PlayerSessionStatusFilter(self, PlayerSessionStatusFilter):
        self._PlayerSessionStatusFilter = PlayerSessionStatusFilter


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        self._PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions response structure.

    """

    def __init__(self):
        r"""
        :param _PlayerSessions: Player session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerSessions: list of PlayerSession
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlayerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def PlayerSessions(self):
        return self._PlayerSessions

    @PlayerSessions.setter
    def PlayerSessions(self, PlayerSessions):
        self._PlayerSessions = PlayerSessions

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self._PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self._PlayerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeTimerScalingPoliciesRequest(AbstractModel):
    """DescribeTimerScalingPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _FleetId: ID of the fleet to be bound with the policy
        :type FleetId: str
        :param _TimerName: Scheduled scaling policy name
        :type TimerName: str
        :param _BeginTime: Start time of the scheduled scaling policy
        :type BeginTime: str
        :param _EndTime: End time of the scheduled scaling policy
        :type EndTime: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Number of entries per page
        :type Limit: int
        """
        self._FleetId = None
        self._TimerName = None
        self._BeginTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def TimerName(self):
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._TimerName = params.get("TimerName")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimerScalingPoliciesResponse(AbstractModel):
    """DescribeTimerScalingPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TimerScalingPolicies: Configuration of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TimerScalingPolicies: list of TimerScalingPolicy
        :param _TotalCount: Total number of scheduled scaling policies
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TimerScalingPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TimerScalingPolicies(self):
        return self._TimerScalingPolicies

    @TimerScalingPolicies.setter
    def TimerScalingPolicies(self, TimerScalingPolicies):
        self._TimerScalingPolicies = TimerScalingPolicies

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TimerScalingPolicies") is not None:
            self._TimerScalingPolicies = []
            for item in params.get("TimerScalingPolicies"):
                obj = TimerScalingPolicy()
                obj._deserialize(item)
                self._TimerScalingPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """Player game session information

    """

    def __init__(self):
        r"""
        :param _PlayerId: Unique player ID associated with player session
        :type PlayerId: str
        :param _PlayerData: Developer-defined player data
        :type PlayerData: str
        """
        self._PlayerId = None
        self._PlayerData = None

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerData(self):
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    """Disk storage information

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type: Premium Cloud Storage (CLOUD_PREMIUM) or SSD (CLOUD_SSD)
        :type DiskType: str
        :param _DiskSize: System disk: the available disk capacity is 50-500 GB. Data disk: the available disk capacity is 100-32000 GB, and the value is a multiple of 10. When the disk type is SSD (CLOUD_SSD), the minimum capacity is 100 GB.
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessRequest(AbstractModel):
    """EndGameServerSessionAndProcess request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. If a game server session ID is passed in, its corresponding processes, game server sessions, and player sessions will be terminated.
        :type GameServerSessionId: str
        :param _IpAddress: The public IP of the CVM. You need to pass in `IpAddress` and `Port` at the same time to terminate the matched processes, game server sessions and player sessions (if any exists). It does not take effect in case only the `IpAddress` passed in.
        :type IpAddress: str
        :param _Port: Port number. Value range: 1025 - 60000. You need to pass in `IpAddress` and `Port` at the same time to terminate the matched processes, game server sessions (if any exists) and player sessions (if any exists). It does not take effect in case only the `IpAddress` passed in.
        :type Port: int
        """
        self._GameServerSessionId = None
        self._IpAddress = None
        self._Port = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessResponse(AbstractModel):
    """EndGameServerSessionAndProcess response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FleetAttributes(AbstractModel):
    """Service deployment attributes

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset package ID
        :type AssetId: str
        :param _CreationTime: Server fleet creation time
        :type CreationTime: str
        :param _Description: Description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Description: str
        :param _FleetArn: Description of server fleet resource
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FleetArn: str
        :param _FleetId: Server fleet ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FleetId: str
        :param _FleetType: Server fleet type, which only supports ON_DEMAND now.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FleetType: str
        :param _InstanceType: Server type, such as S5.LARGE8
Note: this field may return `null`, indicating that no valid value is obtained.
        :type InstanceType: str
        :param _Name: Server fleet name
        :type Name: str
        :param _NewGameServerSessionProtectionPolicy: Game session protection policy
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NewGameServerSessionProtectionPolicy: str
        :param _OperatingSystem: Operating system type
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OperatingSystem: str
        :param _ResourceCreationLimitPolicy: Limit policy of resource creation
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`
        :param _Status: Statuses: “Create”, “Downloading”, “Verifying”, “Generating”, “Activating”, “Active”, “Exception”, “Deleting”, and “End”.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Status: str
        :param _StoppedActions: The status of server fleet when it stopped. If this field is left empty, it means automatic scaling.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StoppedActions: list of str
        :param _TerminationTime: Server fleet termination time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TerminationTime: str
        :param _GameServerSessionProtectionTimeLimit: Timeout period of time-limited protection. Value range: 5-1440 minutes. Default value: 60 minutes.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameServerSessionProtectionTimeLimit: int
        :param _BillingStatus: Billing status: Unactivated, Activated, Exception, Isolated due to arrears, Terminated, and Unfrozen.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type BillingStatus: str
        :param _Tags: Tag list. Up to 50 tags.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Tags: list of Tag
        :param _DataDiskInfo: Data disk. It can be SSD disks (CLOUD_SSD) with 100-32000 GB capacity or Premium Cloud Storage disks (CLOUD_PREMIUM) with 10-32000 GB capacity. The increment is 10. 
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DataDiskInfo: list of DiskInfo
        :param _SystemDiskInfo: System disk. It can be a SSD (CLOUD_SSD) with 100-500 GB capacity or a Premium Cloud Storage disk (CLOUD_PREMIUM) with 50-500 GB capacity. The increment is 1.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`
        :param _RelatedCcnInfos: CCN instance information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RelatedCcnInfos: list of RelatedCcnInfo
        :param _InternetMaxBandwidthOut: Maximum outbound public network bandwidth of the server fleet. Value range: 1 - 200 Mbps. Default value: 100 Mbps.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InternetMaxBandwidthOut: int
        """
        self._AssetId = None
        self._CreationTime = None
        self._Description = None
        self._FleetArn = None
        self._FleetId = None
        self._FleetType = None
        self._InstanceType = None
        self._Name = None
        self._NewGameServerSessionProtectionPolicy = None
        self._OperatingSystem = None
        self._ResourceCreationLimitPolicy = None
        self._Status = None
        self._StoppedActions = None
        self._TerminationTime = None
        self._GameServerSessionProtectionTimeLimit = None
        self._BillingStatus = None
        self._Tags = None
        self._DataDiskInfo = None
        self._SystemDiskInfo = None
        self._RelatedCcnInfos = None
        self._InternetMaxBandwidthOut = None

    @property
    def AssetId(self):
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FleetArn(self):
        return self._FleetArn

    @FleetArn.setter
    def FleetArn(self, FleetArn):
        self._FleetArn = FleetArn

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def FleetType(self):
        return self._FleetType

    @FleetType.setter
    def FleetType(self, FleetType):
        self._FleetType = FleetType

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NewGameServerSessionProtectionPolicy(self):
        return self._NewGameServerSessionProtectionPolicy

    @NewGameServerSessionProtectionPolicy.setter
    def NewGameServerSessionProtectionPolicy(self, NewGameServerSessionProtectionPolicy):
        self._NewGameServerSessionProtectionPolicy = NewGameServerSessionProtectionPolicy

    @property
    def OperatingSystem(self):
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem

    @property
    def ResourceCreationLimitPolicy(self):
        return self._ResourceCreationLimitPolicy

    @ResourceCreationLimitPolicy.setter
    def ResourceCreationLimitPolicy(self, ResourceCreationLimitPolicy):
        self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StoppedActions(self):
        return self._StoppedActions

    @StoppedActions.setter
    def StoppedActions(self, StoppedActions):
        self._StoppedActions = StoppedActions

    @property
    def TerminationTime(self):
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime

    @property
    def GameServerSessionProtectionTimeLimit(self):
        return self._GameServerSessionProtectionTimeLimit

    @GameServerSessionProtectionTimeLimit.setter
    def GameServerSessionProtectionTimeLimit(self, GameServerSessionProtectionTimeLimit):
        self._GameServerSessionProtectionTimeLimit = GameServerSessionProtectionTimeLimit

    @property
    def BillingStatus(self):
        return self._BillingStatus

    @BillingStatus.setter
    def BillingStatus(self, BillingStatus):
        self._BillingStatus = BillingStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataDiskInfo(self):
        return self._DataDiskInfo

    @DataDiskInfo.setter
    def DataDiskInfo(self, DataDiskInfo):
        self._DataDiskInfo = DataDiskInfo

    @property
    def SystemDiskInfo(self):
        return self._SystemDiskInfo

    @SystemDiskInfo.setter
    def SystemDiskInfo(self, SystemDiskInfo):
        self._SystemDiskInfo = SystemDiskInfo

    @property
    def RelatedCcnInfos(self):
        return self._RelatedCcnInfos

    @RelatedCcnInfos.setter
    def RelatedCcnInfos(self, RelatedCcnInfos):
        self._RelatedCcnInfos = RelatedCcnInfos

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._CreationTime = params.get("CreationTime")
        self._Description = params.get("Description")
        self._FleetArn = params.get("FleetArn")
        self._FleetId = params.get("FleetId")
        self._FleetType = params.get("FleetType")
        self._InstanceType = params.get("InstanceType")
        self._Name = params.get("Name")
        self._NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self._OperatingSystem = params.get("OperatingSystem")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self._ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self._ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self._Status = params.get("Status")
        self._StoppedActions = params.get("StoppedActions")
        self._TerminationTime = params.get("TerminationTime")
        self._GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self._BillingStatus = params.get("BillingStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataDiskInfo") is not None:
            self._DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDiskInfo.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self._SystemDiskInfo = DiskInfo()
            self._SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("RelatedCcnInfos") is not None:
            self._RelatedCcnInfos = []
            for item in params.get("RelatedCcnInfos"):
                obj = RelatedCcnInfo()
                obj._deserialize(item)
                self._RelatedCcnInfos.append(obj)
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameProperty(AbstractModel):
    """Game attribute details

    """

    def __init__(self):
        r"""
        :param _Key: Attribute name. Up to 32 ASCII characters are allowed.
        :type Key: str
        :param _Value: Attribute value. Up to 96 ASCII characters are allowed.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSession(AbstractModel):
    """Game session details

    """

    def __init__(self):
        r"""
        :param _CreationTime: Game server session creation time
        :type CreationTime: str
        :param _CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreatorId: str
        :param _CurrentPlayerSessionCount: The current number of players, which cannot be less than 0.
        :type CurrentPlayerSessionCount: int
        :param _DnsName: CVM DNS ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param _FleetId: Fleet ID
        :type FleetId: str
        :param _GameProperties: Game attributes. Up to 16 groups of attributes are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameServerSessionData: str
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param _IpAddress: CVM IP address
        :type IpAddress: str
        :param _MatchmakerData: Battle progress details. Up to 400,000 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchmakerData: str
        :param _MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param _Name: The name of game server session. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Name: str
        :param _PlayerSessionCreationPolicy: Player session creation policy. Valid values: ACCEPT_ALL, DENY_ALL
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerSessionCreationPolicy: str
        :param _Port: Port number. It should be a value between 1 to 60000.
        :type Port: int
        :param _Status: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type Status: str
        :param _StatusReason: Additional information of game server session status
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusReason: str
        :param _TerminationTime: Termination time
Note: this field may return null, indicating that no valid values can be obtained.
        :type TerminationTime: str
        :param _InstanceType: Instance type. Up to 128 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type InstanceType: str
        :param _CurrentCustomCount: Current custom count
Note: this field may return null, indicating that no valid values can be obtained.
        :type CurrentCustomCount: int
        :param _MaxCustomCount: Maximum custom count
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxCustomCount: int
        :param _Weight: Weight
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _AvailabilityStatus: Session availability status, i.e., whether it is blocked. Valid value: Enable, Disable
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AvailabilityStatus: str
        """
        self._CreationTime = None
        self._CreatorId = None
        self._CurrentPlayerSessionCount = None
        self._DnsName = None
        self._FleetId = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionId = None
        self._IpAddress = None
        self._MatchmakerData = None
        self._MaximumPlayerSessionCount = None
        self._Name = None
        self._PlayerSessionCreationPolicy = None
        self._Port = None
        self._Status = None
        self._StatusReason = None
        self._TerminationTime = None
        self._InstanceType = None
        self._CurrentCustomCount = None
        self._MaxCustomCount = None
        self._Weight = None
        self._AvailabilityStatus = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def CreatorId(self):
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CurrentPlayerSessionCount(self):
        return self._CurrentPlayerSessionCount

    @CurrentPlayerSessionCount.setter
    def CurrentPlayerSessionCount(self, CurrentPlayerSessionCount):
        self._CurrentPlayerSessionCount = CurrentPlayerSessionCount

    @property
    def DnsName(self):
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def MatchmakerData(self):
        return self._MatchmakerData

    @MatchmakerData.setter
    def MatchmakerData(self, MatchmakerData):
        self._MatchmakerData = MatchmakerData

    @property
    def MaximumPlayerSessionCount(self):
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PlayerSessionCreationPolicy(self):
        return self._PlayerSessionCreationPolicy

    @PlayerSessionCreationPolicy.setter
    def PlayerSessionCreationPolicy(self, PlayerSessionCreationPolicy):
        self._PlayerSessionCreationPolicy = PlayerSessionCreationPolicy

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def TerminationTime(self):
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CurrentCustomCount(self):
        return self._CurrentCustomCount

    @CurrentCustomCount.setter
    def CurrentCustomCount(self, CurrentCustomCount):
        self._CurrentCustomCount = CurrentCustomCount

    @property
    def MaxCustomCount(self):
        return self._MaxCustomCount

    @MaxCustomCount.setter
    def MaxCustomCount(self, MaxCustomCount):
        self._MaxCustomCount = MaxCustomCount

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def AvailabilityStatus(self):
        return self._AvailabilityStatus

    @AvailabilityStatus.setter
    def AvailabilityStatus(self, AvailabilityStatus):
        self._AvailabilityStatus = AvailabilityStatus


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._CreatorId = params.get("CreatorId")
        self._CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self._DnsName = params.get("DnsName")
        self._FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._MatchmakerData = params.get("MatchmakerData")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._Name = params.get("Name")
        self._PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._TerminationTime = params.get("TerminationTime")
        self._InstanceType = params.get("InstanceType")
        self._CurrentCustomCount = params.get("CurrentCustomCount")
        self._MaxCustomCount = params.get("MaxCustomCount")
        self._Weight = params.get("Weight")
        self._AvailabilityStatus = params.get("AvailabilityStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionDetail(AbstractModel):
    """Game server session details (GameServerSessionDetail)

    """

    def __init__(self):
        r"""
        :param _GameServerSession: Game server session
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _ProtectionPolicy: Protection policy. Valid values: NoProtection, FullProtection
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProtectionPolicy: str
        """
        self._GameServerSession = None
        self._ProtectionPolicy = None

    @property
    def GameServerSession(self):
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def ProtectionPolicy(self):
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionPlacement(AbstractModel):
    """Game session deployment object

    """

    def __init__(self):
        r"""
        :param _PlacementId: Deployment ID
        :type PlacementId: str
        :param _GameServerSessionQueueName: Service deployment group name
        :type GameServerSessionQueueName: str
        :param _PlayerLatencies: Player latency
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerLatencies: list of PlayerLatency
        :param _Status: Service deployment status
        :type Status: str
        :param _DnsName: DNS ID assigned to the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param _GameServerSessionId: Game session ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionId: str
        :param _GameServerSessionName: Game session name
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionName: str
        :param _GameServerSessionRegion: Service deployment region
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionRegion: str
        :param _GameProperties: Game attributes
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameProperties: list of GameProperty
        :param _MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.
        :type MaximumPlayerSessionCount: int
        :param _GameServerSessionData: Game session data
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionData: str
        :param _IpAddress: IP address of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpAddress: str
        :param _Port: Port number of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _MatchmakerData: Game match data
Note: this field may return null, indicating that no valid values can be obtained.
        :type MatchmakerData: str
        :param _PlacedPlayerSessions: Deployed player game data
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self._PlacementId = None
        self._GameServerSessionQueueName = None
        self._PlayerLatencies = None
        self._Status = None
        self._DnsName = None
        self._GameServerSessionId = None
        self._GameServerSessionName = None
        self._GameServerSessionRegion = None
        self._GameProperties = None
        self._MaximumPlayerSessionCount = None
        self._GameServerSessionData = None
        self._IpAddress = None
        self._Port = None
        self._MatchmakerData = None
        self._PlacedPlayerSessions = None
        self._StartTime = None
        self._EndTime = None

    @property
    def PlacementId(self):
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId

    @property
    def GameServerSessionQueueName(self):
        return self._GameServerSessionQueueName

    @GameServerSessionQueueName.setter
    def GameServerSessionQueueName(self, GameServerSessionQueueName):
        self._GameServerSessionQueueName = GameServerSessionQueueName

    @property
    def PlayerLatencies(self):
        return self._PlayerLatencies

    @PlayerLatencies.setter
    def PlayerLatencies(self, PlayerLatencies):
        self._PlayerLatencies = PlayerLatencies

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsName(self):
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def GameServerSessionName(self):
        return self._GameServerSessionName

    @GameServerSessionName.setter
    def GameServerSessionName(self, GameServerSessionName):
        self._GameServerSessionName = GameServerSessionName

    @property
    def GameServerSessionRegion(self):
        return self._GameServerSessionRegion

    @GameServerSessionRegion.setter
    def GameServerSessionRegion(self, GameServerSessionRegion):
        self._GameServerSessionRegion = GameServerSessionRegion

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def MaximumPlayerSessionCount(self):
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def GameServerSessionData(self):
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MatchmakerData(self):
        return self._MatchmakerData

    @MatchmakerData.setter
    def MatchmakerData(self, MatchmakerData):
        self._MatchmakerData = MatchmakerData

    @property
    def PlacedPlayerSessions(self):
        return self._PlacedPlayerSessions

    @PlacedPlayerSessions.setter
    def PlacedPlayerSessions(self, PlacedPlayerSessions):
        self._PlacedPlayerSessions = PlacedPlayerSessions

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        self._GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self._PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self._PlayerLatencies.append(obj)
        self._Status = params.get("Status")
        self._DnsName = params.get("DnsName")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._GameServerSessionName = params.get("GameServerSessionName")
        self._GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._IpAddress = params.get("IpAddress")
        self._Port = params.get("Port")
        self._MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self._PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self._PlacedPlayerSessions.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        """
        self._GameServerSessionId = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl response structure.

    """

    def __init__(self):
        r"""
        :param _PreSignedUrl: Log download URL. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PreSignedUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PreSignedUrl = None
        self._RequestId = None

    @property
    def PreSignedUrl(self):
        return self._PreSignedUrl

    @PreSignedUrl.setter
    def PreSignedUrl(self, PreSignedUrl):
        self._PreSignedUrl = PreSignedUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreSignedUrl = params.get("PreSignedUrl")
        self._RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess request structure.

    """

    def __init__(self):
        r"""
        :param _FleetId: Server fleet ID
        :type FleetId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._FleetId = None
        self._InstanceId = None

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceAccess: Credentials required for instance login
        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceAccess = None
        self._RequestId = None

    @property
    def InstanceAccess(self):
        return self._InstanceAccess

    @InstanceAccess.setter
    def InstanceAccess(self, InstanceAccess):
        self._InstanceAccess = InstanceAccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self._InstanceAccess = InstanceAccess()
            self._InstanceAccess._deserialize(params.get("InstanceAccess"))
        self._RequestId = params.get("RequestId")


class InboundPermission(AbstractModel):
    """Allowed network range.

    """

    def __init__(self):
        r"""
        :param _FromPort: Start port number. Minimum value: 1025.
        :type FromPort: int
        :param _IpRange: IP range. Valid range of the input IPv4 addresses in CIDR format; for example, 0.0.0.0.0/0.
        :type IpRange: str
        :param _Protocol: Protocol type: TCP or UDP.
        :type Protocol: str
        :param _ToPort: End port number. Maximum value: 60000.
        :type ToPort: int
        """
        self._FromPort = None
        self._IpRange = None
        self._Protocol = None
        self._ToPort = None

    @property
    def FromPort(self):
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def IpRange(self):
        return self._IpRange

    @IpRange.setter
    def IpRange(self, IpRange):
        self._IpRange = IpRange

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ToPort(self):
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._IpRange = params.get("IpRange")
        self._Protocol = params.get("Protocol")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAccess(AbstractModel):
    """Identity credentials for instance access

    """

    def __init__(self):
        r"""
        :param _Credentials: Credentials required for instance access
        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`
        :param _FleetId: Service deployment ID
        :type FleetId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IpAddress: Public IP of instance
        :type IpAddress: str
        :param _OperatingSystem: OS
        :type OperatingSystem: str
        """
        self._Credentials = None
        self._FleetId = None
        self._InstanceId = None
        self._IpAddress = None
        self._OperatingSystem = None

    @property
    def Credentials(self):
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def OperatingSystem(self):
        return self._OperatingSystem

    @OperatingSystem.setter
    def OperatingSystem(self, OperatingSystem):
        self._OperatingSystem = OperatingSystem


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._IpAddress = params.get("IpAddress")
        self._OperatingSystem = params.get("OperatingSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeInfo(AbstractModel):
    """The server instance type information

    """

    def __init__(self):
        r"""
        :param _TypeName: Name of the server type, such as `Standard SA1`
        :type TypeName: str
        :param _InstanceType: Specification of the server type, such as `SA1.SMALL1`
        :type InstanceType: str
        :param _Cpu: CPU, in core
        :type Cpu: int
        :param _Memory: Memory, in GB
        :type Memory: int
        :param _NetworkCard: The packet sending and receiving capability, in 10k PPS. 
        :type NetworkCard: int
        """
        self._TypeName = None
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._NetworkCard = None

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._NetworkCard = params.get("NetworkCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchRequest(AbstractModel):
    """JoinGameServerSessionBatch request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param _PlayerIds: Player ID list. At least 1 ID and up to 25 IDs.
        :type PlayerIds: list of str
        :param _PlayerDataMap: Player custom data
        :type PlayerDataMap: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`
        """
        self._GameServerSessionId = None
        self._PlayerIds = None
        self._PlayerDataMap = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def PlayerIds(self):
        return self._PlayerIds

    @PlayerIds.setter
    def PlayerIds(self, PlayerIds):
        self._PlayerIds = PlayerIds

    @property
    def PlayerDataMap(self):
        return self._PlayerDataMap

    @PlayerDataMap.setter
    def PlayerDataMap(self, PlayerDataMap):
        self._PlayerDataMap = PlayerDataMap


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._PlayerIds = params.get("PlayerIds")
        if params.get("PlayerDataMap") is not None:
            self._PlayerDataMap = PlayerDataMap()
            self._PlayerDataMap._deserialize(params.get("PlayerDataMap"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchResponse(AbstractModel):
    """JoinGameServerSessionBatch response structure.

    """

    def __init__(self):
        r"""
        :param _PlayerSessions: Player session list. Up to 25 sessions.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerSessions: list of PlayerSession
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlayerSessions = None
        self._RequestId = None

    @property
    def PlayerSessions(self):
        return self._PlayerSessions

    @PlayerSessions.setter
    def PlayerSessions(self, PlayerSessions):
        self._PlayerSessions = PlayerSessions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self._PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self._PlayerSessions.append(obj)
        self._RequestId = params.get("RequestId")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param _PlayerId: Player ID. Up to 1024 ASCII characters are allowed.
        :type PlayerId: str
        :param _PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.
        :type PlayerData: str
        """
        self._GameServerSessionId = None
        self._PlayerId = None
        self._PlayerData = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerData(self):
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._PlayerId = params.get("PlayerId")
        self._PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession response structure.

    """

    def __init__(self):
        r"""
        :param _PlayerSession: Player session
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlayerSession = None
        self._RequestId = None

    @property
    def PlayerSession(self):
        return self._PlayerSession

    @PlayerSession.setter
    def PlayerSession(self, PlayerSession):
        self._PlayerSession = PlayerSession

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self._PlayerSession = PlayerSession()
            self._PlayerSession._deserialize(params.get("PlayerSession"))
        self._RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """Deployed player game session

    """

    def __init__(self):
        r"""
        :param _PlayerId: Player ID
        :type PlayerId: str
        :param _PlayerSessionId: Player session ID
        :type PlayerSessionId: str
        """
        self._PlayerId = None
        self._PlayerSessionId = None

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerDataMap(AbstractModel):
    """Player custom data

    """

    def __init__(self):
        r"""
        :param _Key: The key of player custom data. It should contain 1 to 1024 ASCII characters.
        :type Key: str
        :param _Value: The value of player custom data. It should contain 1 to 2048 ASCII characters.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerLatency(AbstractModel):
    """Player latency information

    """

    def __init__(self):
        r"""
        :param _PlayerId: Player ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerId: str
        :param _RegionIdentifier: Name of region corresponding to latency
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionIdentifier: str
        :param _LatencyInMilliseconds: Latency in milliseconds
        :type LatencyInMilliseconds: int
        """
        self._PlayerId = None
        self._RegionIdentifier = None
        self._LatencyInMilliseconds = None

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def RegionIdentifier(self):
        return self._RegionIdentifier

    @RegionIdentifier.setter
    def RegionIdentifier(self, RegionIdentifier):
        self._RegionIdentifier = RegionIdentifier

    @property
    def LatencyInMilliseconds(self):
        return self._LatencyInMilliseconds

    @LatencyInMilliseconds.setter
    def LatencyInMilliseconds(self, LatencyInMilliseconds):
        self._LatencyInMilliseconds = LatencyInMilliseconds


    def _deserialize(self, params):
        self._PlayerId = params.get("PlayerId")
        self._RegionIdentifier = params.get("RegionIdentifier")
        self._LatencyInMilliseconds = params.get("LatencyInMilliseconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerSession(AbstractModel):
    """Player session details

    """

    def __init__(self):
        r"""
        :param _CreationTime: Player session creation time
        :type CreationTime: str
        :param _DnsName: ID of the DNS where the game server session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param _FleetId: Fleet ID
        :type FleetId: str
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param _IpAddress: Address of the CVM instance where the game server session is running
        :type IpAddress: str
        :param _PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerData: str
        :param _PlayerId: Player ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerId: str
        :param _PlayerSessionId: Player session ID
        :type PlayerSessionId: str
        :param _Port: Port number. It should be a value between 1 to 60000.
        :type Port: int
        :param _Status: Player session status. Valid values: RESERVED = 1, ACTIVE = 2, COMPLETED =3, TIMEDOUT = 4
        :type Status: str
        :param _TerminationTime: Player session termination time
Note: this field may return null, indicating that no valid values can be obtained.
        :type TerminationTime: str
        """
        self._CreationTime = None
        self._DnsName = None
        self._FleetId = None
        self._GameServerSessionId = None
        self._IpAddress = None
        self._PlayerData = None
        self._PlayerId = None
        self._PlayerSessionId = None
        self._Port = None
        self._Status = None
        self._TerminationTime = None

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def DnsName(self):
        return self._DnsName

    @DnsName.setter
    def DnsName(self, DnsName):
        self._DnsName = DnsName

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def PlayerData(self):
        return self._PlayerData

    @PlayerData.setter
    def PlayerData(self, PlayerData):
        self._PlayerData = PlayerData

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def PlayerSessionId(self):
        return self._PlayerSessionId

    @PlayerSessionId.setter
    def PlayerSessionId(self, PlayerSessionId):
        self._PlayerSessionId = PlayerSessionId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TerminationTime(self):
        return self._TerminationTime

    @TerminationTime.setter
    def TerminationTime(self, TerminationTime):
        self._TerminationTime = TerminationTime


    def _deserialize(self, params):
        self._CreationTime = params.get("CreationTime")
        self._DnsName = params.get("DnsName")
        self._FleetId = params.get("FleetId")
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._IpAddress = params.get("IpAddress")
        self._PlayerData = params.get("PlayerData")
        self._PlayerId = params.get("PlayerId")
        self._PlayerSessionId = params.get("PlayerSessionId")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._TerminationTime = params.get("TerminationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyRequest(AbstractModel):
    """PutTimerScalingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _TimerScalingPolicy: Configuration of the scheduled scaling policy
        :type TimerScalingPolicy: :class:`tencentcloud.gse.v20191112.models.TimerScalingPolicy`
        """
        self._TimerScalingPolicy = None

    @property
    def TimerScalingPolicy(self):
        return self._TimerScalingPolicy

    @TimerScalingPolicy.setter
    def TimerScalingPolicy(self, TimerScalingPolicy):
        self._TimerScalingPolicy = TimerScalingPolicy


    def _deserialize(self, params):
        if params.get("TimerScalingPolicy") is not None:
            self._TimerScalingPolicy = TimerScalingPolicy()
            self._TimerScalingPolicy._deserialize(params.get("TimerScalingPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyResponse(AbstractModel):
    """PutTimerScalingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RelatedCcnInfo(AbstractModel):
    """Information of the associated CCN instance

    """

    def __init__(self):
        r"""
        :param _AccountId: Account of the CCN instance owner
        :type AccountId: str
        :param _CcnId: CCN instance ID
        :type CcnId: str
        :param _AttachType: Status of associated CCN instance
        :type AttachType: str
        """
        self._AccountId = None
        self._CcnId = None
        self._AttachType = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def CcnId(self):
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def AttachType(self):
        return self._AttachType

    @AttachType.setter
    def AttachType(self, AttachType):
        self._AttachType = AttachType


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._CcnId = params.get("CcnId")
        self._AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceCreationLimitPolicy(AbstractModel):
    """Resource creation policy

    """

    def __init__(self):
        r"""
        :param _NewGameServerSessionsPerCreator: Creation quantity. Minimum value: 1. Default value: 2.
        :type NewGameServerSessionsPerCreator: int
        :param _PolicyPeriodInMinutes: Unit time. Minimum value: 1. Default value: 3. Unit: minute.
        :type PolicyPeriodInMinutes: int
        """
        self._NewGameServerSessionsPerCreator = None
        self._PolicyPeriodInMinutes = None

    @property
    def NewGameServerSessionsPerCreator(self):
        return self._NewGameServerSessionsPerCreator

    @NewGameServerSessionsPerCreator.setter
    def NewGameServerSessionsPerCreator(self, NewGameServerSessionsPerCreator):
        self._NewGameServerSessionsPerCreator = NewGameServerSessionsPerCreator

    @property
    def PolicyPeriodInMinutes(self):
        return self._PolicyPeriodInMinutes

    @PolicyPeriodInMinutes.setter
    def PolicyPeriodInMinutes(self, PolicyPeriodInMinutes):
        self._PolicyPeriodInMinutes = PolicyPeriodInMinutes


    def _deserialize(self, params):
        self._NewGameServerSessionsPerCreator = params.get("NewGameServerSessionsPerCreator")
        self._PolicyPeriodInMinutes = params.get("PolicyPeriodInMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfiguration(AbstractModel):
    """Runtime configuration

    """

    def __init__(self):
        r"""
        :param _GameServerSessionActivationTimeoutSeconds: Game session timeout. Value range: 1-600. Unit: second.
        :type GameServerSessionActivationTimeoutSeconds: int
        :param _MaxConcurrentGameServerSessionActivations: Maximum number of game sessions. Value range: 1-2,147,483,647.
        :type MaxConcurrentGameServerSessionActivations: int
        :param _ServerProcesses: Service process configuration. There must be at least one service configuration.
        :type ServerProcesses: list of ServerProcesse
        """
        self._GameServerSessionActivationTimeoutSeconds = None
        self._MaxConcurrentGameServerSessionActivations = None
        self._ServerProcesses = None

    @property
    def GameServerSessionActivationTimeoutSeconds(self):
        return self._GameServerSessionActivationTimeoutSeconds

    @GameServerSessionActivationTimeoutSeconds.setter
    def GameServerSessionActivationTimeoutSeconds(self, GameServerSessionActivationTimeoutSeconds):
        self._GameServerSessionActivationTimeoutSeconds = GameServerSessionActivationTimeoutSeconds

    @property
    def MaxConcurrentGameServerSessionActivations(self):
        return self._MaxConcurrentGameServerSessionActivations

    @MaxConcurrentGameServerSessionActivations.setter
    def MaxConcurrentGameServerSessionActivations(self, MaxConcurrentGameServerSessionActivations):
        self._MaxConcurrentGameServerSessionActivations = MaxConcurrentGameServerSessionActivations

    @property
    def ServerProcesses(self):
        return self._ServerProcesses

    @ServerProcesses.setter
    def ServerProcesses(self, ServerProcesses):
        self._ServerProcesses = ServerProcesses


    def _deserialize(self, params):
        self._GameServerSessionActivationTimeoutSeconds = params.get("GameServerSessionActivationTimeoutSeconds")
        self._MaxConcurrentGameServerSessionActivations = params.get("MaxConcurrentGameServerSessionActivations")
        if params.get("ServerProcesses") is not None:
            self._ServerProcesses = []
            for item in params.get("ServerProcesses"):
                obj = ServerProcesse()
                obj._deserialize(item)
                self._ServerProcesses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions request structure.

    """

    def __init__(self):
        r"""
        :param _AliasId: Alias ID
        :type AliasId: str
        :param _FleetId: Fleet ID
        :type FleetId: str
        :param _Limit: Maximum number of entries in a single query
        :type Limit: int
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param _FilterExpression: Search filter expression. Valid values:
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
}
        :type FilterExpression: str
        :param _SortExpression: Sorting keyword
Valid values:
gameServerSessionName: game session name in `String` type
gameServerSessionId: game session ID in `String` type
maximumSessions: maximum number of player sessions in `Number` type
creationTimeMillis: creation time in milliseconds in `Number` type
playerSessionCount: current number of player sessions in `Number` type
        :type SortExpression: str
        """
        self._AliasId = None
        self._FleetId = None
        self._Limit = None
        self._NextToken = None
        self._FilterExpression = None
        self._SortExpression = None

    @property
    def AliasId(self):
        return self._AliasId

    @AliasId.setter
    def AliasId(self, AliasId):
        self._AliasId = AliasId

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def FilterExpression(self):
        return self._FilterExpression

    @FilterExpression.setter
    def FilterExpression(self, FilterExpression):
        self._FilterExpression = FilterExpression

    @property
    def SortExpression(self):
        return self._SortExpression

    @SortExpression.setter
    def SortExpression(self, SortExpression):
        self._SortExpression = SortExpression


    def _deserialize(self, params):
        self._AliasId = params.get("AliasId")
        self._FleetId = params.get("FleetId")
        self._Limit = params.get("Limit")
        self._NextToken = params.get("NextToken")
        self._FilterExpression = params.get("FilterExpression")
        self._SortExpression = params.get("SortExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessions: list of GameServerSession
        :param _NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessions = None
        self._NextToken = None
        self._RequestId = None

    @property
    def GameServerSessions(self):
        return self._GameServerSessions

    @GameServerSessions.setter
    def GameServerSessions(self, GameServerSessions):
        self._GameServerSessions = GameServerSessions

    @property
    def NextToken(self):
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self._GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self._GameServerSessions.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ServerProcesse(AbstractModel):
    """Game service process

    """

    def __init__(self):
        r"""
        :param _ConcurrentExecutions: Number of concurrent processes. Value range of total concurrent processes: 1-50.
        :type ConcurrentExecutions: int
        :param _LaunchPath: Launch Path. Linux: /local/game/ or Windows: C:\game\. The path length is 1-1024.
        :type LaunchPath: str
        :param _Parameters: Launch parameter. The length is 0-1024.
        :type Parameters: str
        """
        self._ConcurrentExecutions = None
        self._LaunchPath = None
        self._Parameters = None

    @property
    def ConcurrentExecutions(self):
        return self._ConcurrentExecutions

    @ConcurrentExecutions.setter
    def ConcurrentExecutions(self, ConcurrentExecutions):
        self._ConcurrentExecutions = ConcurrentExecutions

    @property
    def LaunchPath(self):
        return self._LaunchPath

    @LaunchPath.setter
    def LaunchPath(self, LaunchPath):
        self._LaunchPath = LaunchPath

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._ConcurrentExecutions = params.get("ConcurrentExecutions")
        self._LaunchPath = params.get("LaunchPath")
        self._Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedRequest(AbstractModel):
    """SetServerReserved request structure.

    """

    def __init__(self):
        r"""
        :param _FleetId: ID of the fleet to be bound with the policy
        :type FleetId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ReserveValue: Whether the instance is retained. Valid values: 1 (retained), 0 (not retained). Default value: 0.
        :type ReserveValue: int
        """
        self._FleetId = None
        self._InstanceId = None
        self._ReserveValue = None

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReserveValue(self):
        return self._ReserveValue

    @ReserveValue.setter
    def ReserveValue(self, ReserveValue):
        self._ReserveValue = ReserveValue


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._InstanceId = params.get("InstanceId")
        self._ReserveValue = params.get("ReserveValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedResponse(AbstractModel):
    """SetServerReserved response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement request structure.

    """

    def __init__(self):
        r"""
        :param _PlacementId: The unique ID of the game server session placement. It should contain up to 48 ASCII characters, supporting [a-zA-Z0-9-]+.
        :type PlacementId: str
        :param _GameServerSessionQueueName: Game server session queue name
        :type GameServerSessionQueueName: str
        :param _MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.
        :type MaximumPlayerSessionCount: int
        :param _DesiredPlayerSessions: Player game session information
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param _GameProperties: Player game session attributes
        :type GameProperties: list of GameProperty
        :param _GameServerSessionData: Data of game server sessions. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionData: str
        :param _GameServerSessionName: Name of game server sessions. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionName: str
        :param _PlayerLatencies: Player latency
        :type PlayerLatencies: list of PlayerLatency
        """
        self._PlacementId = None
        self._GameServerSessionQueueName = None
        self._MaximumPlayerSessionCount = None
        self._DesiredPlayerSessions = None
        self._GameProperties = None
        self._GameServerSessionData = None
        self._GameServerSessionName = None
        self._PlayerLatencies = None

    @property
    def PlacementId(self):
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId

    @property
    def GameServerSessionQueueName(self):
        return self._GameServerSessionQueueName

    @GameServerSessionQueueName.setter
    def GameServerSessionQueueName(self, GameServerSessionQueueName):
        self._GameServerSessionQueueName = GameServerSessionQueueName

    @property
    def MaximumPlayerSessionCount(self):
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def DesiredPlayerSessions(self):
        return self._DesiredPlayerSessions

    @DesiredPlayerSessions.setter
    def DesiredPlayerSessions(self, DesiredPlayerSessions):
        self._DesiredPlayerSessions = DesiredPlayerSessions

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def GameServerSessionData(self):
        return self._GameServerSessionData

    @GameServerSessionData.setter
    def GameServerSessionData(self, GameServerSessionData):
        self._GameServerSessionData = GameServerSessionData

    @property
    def GameServerSessionName(self):
        return self._GameServerSessionName

    @GameServerSessionName.setter
    def GameServerSessionName(self, GameServerSessionName):
        self._GameServerSessionName = GameServerSessionName

    @property
    def PlayerLatencies(self):
        return self._PlayerLatencies

    @PlayerLatencies.setter
    def PlayerLatencies(self, PlayerLatencies):
        self._PlayerLatencies = PlayerLatencies


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        self._GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self._DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self._DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._GameServerSessionData = params.get("GameServerSessionData")
        self._GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self._PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self._PlayerLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement request structure.

    """

    def __init__(self):
        r"""
        :param _PlacementId: Unique ID of game server session placement
        :type PlacementId: str
        """
        self._PlacementId = None

    @property
    def PlacementId(self):
        return self._PlacementId

    @PlacementId.setter
    def PlacementId(self, PlacementId):
        self._PlacementId = PlacementId


    def _deserialize(self, params):
        self._PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSessionPlacement = None
        self._RequestId = None

    @property
    def GameServerSessionPlacement(self):
        return self._GameServerSessionPlacement

    @GameServerSessionPlacement.setter
    def GameServerSessionPlacement(self, GameServerSessionPlacement):
        self._GameServerSessionPlacement = GameServerSessionPlacement

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self._GameServerSessionPlacement = GameServerSessionPlacement()
            self._GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag structure

    """

    def __init__(self):
        r"""
        :param _Key: Tag key. Up to 127 bytes are allowed.
        :type Key: str
        :param _Value: Tag value. Up to 255 bytes are allowed.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetConfiguration(AbstractModel):
    """Configuration of target tracking scaling

    """

    def __init__(self):
        r"""
        :param _TargetValue: Ratio of reserved server session resource 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetValue: int
        """
        self._TargetValue = None

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue


    def _deserialize(self, params):
        self._TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerConfiguration(AbstractModel):
    """The recurrence pattern of auto-scaling

    """

    def __init__(self):
        r"""
        :param _TimerType: The recurrence pattern of auto-scaling. `0`: undefined, `1`: once, `2`: daily, `3`: monthly, `4`: weekly
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerType: int
        :param _TimerValue: Details of the recurrence pattern of auto-scaling
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerValue: :class:`tencentcloud.gse.v20191112.models.TimerValue`
        :param _BeginTime: Start time of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BeginTime: str
        :param _EndTime: End time of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self._TimerType = None
        self._TimerValue = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def TimerType(self):
        return self._TimerType

    @TimerType.setter
    def TimerType(self, TimerType):
        self._TimerType = TimerType

    @property
    def TimerValue(self):
        return self._TimerValue

    @TimerValue.setter
    def TimerValue(self, TimerValue):
        self._TimerValue = TimerValue

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._TimerType = params.get("TimerType")
        if params.get("TimerValue") is not None:
            self._TimerValue = TimerValue()
            self._TimerValue._deserialize(params.get("TimerValue"))
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerFleetCapacity(AbstractModel):
    """The capacity configurations of the scheduled scaling policy

    """

    def __init__(self):
        r"""
        :param _FleetId: ID of the fleet to be bound with the policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FleetId: str
        :param _DesiredInstances: Desired number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DesiredInstances: int
        :param _MinSize: Minimum number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MinSize: int
        :param _MaxSize: Maximum number of instances
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxSize: int
        :param _ScalingInterval: Scaling cooldown period, in minutes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ScalingInterval: int
        :param _ScalingType: Scaling type. `1`: manual, `2`: automatic, `0`: undefined
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ScalingType: int
        :param _TargetConfiguration: Configuration of target tracking scaling
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self._FleetId = None
        self._DesiredInstances = None
        self._MinSize = None
        self._MaxSize = None
        self._ScalingInterval = None
        self._ScalingType = None
        self._TargetConfiguration = None

    @property
    def FleetId(self):
        return self._FleetId

    @FleetId.setter
    def FleetId(self, FleetId):
        self._FleetId = FleetId

    @property
    def DesiredInstances(self):
        return self._DesiredInstances

    @DesiredInstances.setter
    def DesiredInstances(self, DesiredInstances):
        self._DesiredInstances = DesiredInstances

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def ScalingInterval(self):
        return self._ScalingInterval

    @ScalingInterval.setter
    def ScalingInterval(self, ScalingInterval):
        self._ScalingInterval = ScalingInterval

    @property
    def ScalingType(self):
        return self._ScalingType

    @ScalingType.setter
    def ScalingType(self, ScalingType):
        self._ScalingType = ScalingType

    @property
    def TargetConfiguration(self):
        return self._TargetConfiguration

    @TargetConfiguration.setter
    def TargetConfiguration(self, TargetConfiguration):
        self._TargetConfiguration = TargetConfiguration


    def _deserialize(self, params):
        self._FleetId = params.get("FleetId")
        self._DesiredInstances = params.get("DesiredInstances")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._ScalingInterval = params.get("ScalingInterval")
        self._ScalingType = params.get("ScalingType")
        if params.get("TargetConfiguration") is not None:
            self._TargetConfiguration = TargetConfiguration()
            self._TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerScalingPolicy(AbstractModel):
    """Configurations of a scheduled scaling policy

    """

    def __init__(self):
        r"""
        :param _TimerId: Unique ID of the policy. When it’s filled in, the policy will be updated.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerId: str
        :param _TimerName: Scheduled scaling policy name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerName: str
        :param _TimerStatus: Scheduled scaling policy status. `0`: Undefined, `1`: Not started, 2: Activated, `3`: Stopped, `4`: Expired
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerStatus: int
        :param _TimerFleetCapacity: The capacity configurations of the scheduled scaling policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerFleetCapacity: :class:`tencentcloud.gse.v20191112.models.TimerFleetCapacity`
        :param _TimerConfiguration: The recurrence pattern of auto-scaling
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimerConfiguration: :class:`tencentcloud.gse.v20191112.models.TimerConfiguration`
        """
        self._TimerId = None
        self._TimerName = None
        self._TimerStatus = None
        self._TimerFleetCapacity = None
        self._TimerConfiguration = None

    @property
    def TimerId(self):
        return self._TimerId

    @TimerId.setter
    def TimerId(self, TimerId):
        self._TimerId = TimerId

    @property
    def TimerName(self):
        return self._TimerName

    @TimerName.setter
    def TimerName(self, TimerName):
        self._TimerName = TimerName

    @property
    def TimerStatus(self):
        return self._TimerStatus

    @TimerStatus.setter
    def TimerStatus(self, TimerStatus):
        self._TimerStatus = TimerStatus

    @property
    def TimerFleetCapacity(self):
        return self._TimerFleetCapacity

    @TimerFleetCapacity.setter
    def TimerFleetCapacity(self, TimerFleetCapacity):
        self._TimerFleetCapacity = TimerFleetCapacity

    @property
    def TimerConfiguration(self):
        return self._TimerConfiguration

    @TimerConfiguration.setter
    def TimerConfiguration(self, TimerConfiguration):
        self._TimerConfiguration = TimerConfiguration


    def _deserialize(self, params):
        self._TimerId = params.get("TimerId")
        self._TimerName = params.get("TimerName")
        self._TimerStatus = params.get("TimerStatus")
        if params.get("TimerFleetCapacity") is not None:
            self._TimerFleetCapacity = TimerFleetCapacity()
            self._TimerFleetCapacity._deserialize(params.get("TimerFleetCapacity"))
        if params.get("TimerConfiguration") is not None:
            self._TimerConfiguration = TimerConfiguration()
            self._TimerConfiguration._deserialize(params.get("TimerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerValue(AbstractModel):
    """Details of the recurrence pattern of the scheduled scaling policy

    """

    def __init__(self):
        r"""
        :param _Day: Execute once every X day(s)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Day: int
        :param _FromDay: Specify the first day to execute the scaling action in a month (execute once per day)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FromDay: int
        :param _ToDay: Specify the last day to execute the scaling action in a month
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ToDay: int
        :param _WeekDays: Specify the week days to repeat the scaling action. Multiple values are supported. Valid values: `1` (Monday), `2` (Tuesday), `3` (Wednesday), `4` (Thursday), `5` (Friday), `6` (Saturday), `7` (Sunday). 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WeekDays: list of int
        """
        self._Day = None
        self._FromDay = None
        self._ToDay = None
        self._WeekDays = None

    @property
    def Day(self):
        return self._Day

    @Day.setter
    def Day(self, Day):
        self._Day = Day

    @property
    def FromDay(self):
        return self._FromDay

    @FromDay.setter
    def FromDay(self, FromDay):
        self._FromDay = FromDay

    @property
    def ToDay(self):
        return self._ToDay

    @ToDay.setter
    def ToDay(self, ToDay):
        self._ToDay = ToDay

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays


    def _deserialize(self, params):
        self._Day = params.get("Day")
        self._FromDay = params.get("FromDay")
        self._ToDay = params.get("ToDay")
        self._WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptRequest(AbstractModel):
    """UpdateBucketAccelerateOpt request structure.

    """

    def __init__(self):
        r"""
        :param _Allowed: `true`: enable global acceleration; `false`: disable global acceleration
        :type Allowed: bool
        """
        self._Allowed = None

    @property
    def Allowed(self):
        return self._Allowed

    @Allowed.setter
    def Allowed(self, Allowed):
        self._Allowed = Allowed


    def _deserialize(self, params):
        self._Allowed = params.get("Allowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptResponse(AbstractModel):
    """UpdateBucketAccelerateOpt response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateBucketCORSOptRequest(AbstractModel):
    """UpdateBucketCORSOpt request structure.

    """

    def __init__(self):
        r"""
        :param _AllowedOrigins: Allowed access source. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).
        :type AllowedOrigins: list of str
        :param _AllowedMethods: Allowed HTTP method(s). Multiple methods are allowed, including PUT, GET, POST, and HEAD. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).
        :type AllowedMethods: list of str
        :param _AllowedHeaders: Specifies the custom HTTP request headers that the browser is allowed to include in a CORS request. Wildcard (*) is supported, indicating allowing all headers (recommended). For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).
        :type AllowedHeaders: list of str
        :param _MaxAgeSeconds: Sets the validity duration for the CORS configuration (in second). For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).
        :type MaxAgeSeconds: int
        :param _ExposeHeaders: CORS response header(s) that can be exposed to the browser, case-insensitive. If this parameter is not specified, the browser can access only simple response headers Cache-Control, Content-Type, Expires, and Last-Modified by default. For details, see [COS Documentation](https://intl.cloud.tencent.com/document/product/436/8279?from_cn_redirect=1).
        :type ExposeHeaders: list of str
        """
        self._AllowedOrigins = None
        self._AllowedMethods = None
        self._AllowedHeaders = None
        self._MaxAgeSeconds = None
        self._ExposeHeaders = None

    @property
    def AllowedOrigins(self):
        return self._AllowedOrigins

    @AllowedOrigins.setter
    def AllowedOrigins(self, AllowedOrigins):
        self._AllowedOrigins = AllowedOrigins

    @property
    def AllowedMethods(self):
        return self._AllowedMethods

    @AllowedMethods.setter
    def AllowedMethods(self, AllowedMethods):
        self._AllowedMethods = AllowedMethods

    @property
    def AllowedHeaders(self):
        return self._AllowedHeaders

    @AllowedHeaders.setter
    def AllowedHeaders(self, AllowedHeaders):
        self._AllowedHeaders = AllowedHeaders

    @property
    def MaxAgeSeconds(self):
        return self._MaxAgeSeconds

    @MaxAgeSeconds.setter
    def MaxAgeSeconds(self, MaxAgeSeconds):
        self._MaxAgeSeconds = MaxAgeSeconds

    @property
    def ExposeHeaders(self):
        return self._ExposeHeaders

    @ExposeHeaders.setter
    def ExposeHeaders(self, ExposeHeaders):
        self._ExposeHeaders = ExposeHeaders


    def _deserialize(self, params):
        self._AllowedOrigins = params.get("AllowedOrigins")
        self._AllowedMethods = params.get("AllowedMethods")
        self._AllowedHeaders = params.get("AllowedHeaders")
        self._MaxAgeSeconds = params.get("MaxAgeSeconds")
        self._ExposeHeaders = params.get("ExposeHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketCORSOptResponse(AbstractModel):
    """UpdateBucketCORSOpt response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession request structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param _MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param _Name: Name of the game server session. It should contain 1 to 1024 ASCII characters.
        :type Name: str
        :param _PlayerSessionCreationPolicy: Player session creation policy, which includes `ACCEPT_ALL` (allow all players) and `DENY_ALL` (reject all players).
        :type PlayerSessionCreationPolicy: str
        :param _ProtectionPolicy: Protection policy, which includes `NoProtection`·(no protection), `TimeLimitProtection` (time-limited protection) and `FullProtection` (full protection)
        :type ProtectionPolicy: str
        """
        self._GameServerSessionId = None
        self._MaximumPlayerSessionCount = None
        self._Name = None
        self._PlayerSessionCreationPolicy = None
        self._ProtectionPolicy = None

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def MaximumPlayerSessionCount(self):
        return self._MaximumPlayerSessionCount

    @MaximumPlayerSessionCount.setter
    def MaximumPlayerSessionCount(self, MaximumPlayerSessionCount):
        self._MaximumPlayerSessionCount = MaximumPlayerSessionCount

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PlayerSessionCreationPolicy(self):
        return self._PlayerSessionCreationPolicy

    @PlayerSessionCreationPolicy.setter
    def PlayerSessionCreationPolicy(self, PlayerSessionCreationPolicy):
        self._PlayerSessionCreationPolicy = PlayerSessionCreationPolicy

    @property
    def ProtectionPolicy(self):
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy


    def _deserialize(self, params):
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self._Name = params.get("Name")
        self._PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self._ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession response structure.

    """

    def __init__(self):
        r"""
        :param _GameServerSession: Updated game session
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GameServerSession = None
        self._RequestId = None

    @property
    def GameServerSession(self):
        return self._GameServerSession

    @GameServerSession.setter
    def GameServerSession(self, GameServerSession):
        self._GameServerSession = GameServerSession

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self._GameServerSession = GameServerSession()
            self._GameServerSession._deserialize(params.get("GameServerSession"))
        self._RequestId = params.get("RequestId")