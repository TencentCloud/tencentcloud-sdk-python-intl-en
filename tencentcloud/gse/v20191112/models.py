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


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession request structure.

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param AliasId: Alias ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.
        :type AliasId: str
        :param CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.
        :type CreatorId: str
        :param FleetId: Fleet ID. You need to specify an alias ID or fleet ID for each request. If both of them are specified, the fleet ID shall prevail.
        :type FleetId: str
        :param GameProperties: Game attributes. Up to 16 groups of attributes are allowed.
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionData: str
        :param GameServerSessionId: The custom ID of game server session. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionId: str
        :param IdempotencyToken: Idempotency token. Up to 48 ASCII characters are allowed.
        :type IdempotencyToken: str
        :param Name: The name of game server session. Up to 1024 ASCII characters are allowed.
        :type Name: str
        """
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


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession response structure.

    """

    def __init__(self):
        """
        :param GameServerSession: Game server session
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Secret: SSH private key
        :type Secret: str
        :param UserName: Username
        :type UserName: str
        """
        self.Secret = None
        self.UserName = None


    def _deserialize(self, params):
        self.Secret = params.get("Secret")
        self.UserName = params.get("UserName")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails request structure.

    """

    def __init__(self):
        """
        :param AliasId: Alias ID
        :type AliasId: str
        :param FleetId: Fleet ID
        :type FleetId: str
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param Limit: Maximum number of entries in a single query
        :type Limit: int
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type StatusFilter: str
        """
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


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: List of game server session details
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param PlacementId: Unique ID of game server session placement
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param AliasId: Alias ID
        :type AliasId: str
        :param FleetId: Fleet ID
        :type FleetId: str
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param Limit: Maximum number of entries in a single query
        :type Limit: int
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param StatusFilter: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type StatusFilter: str
        """
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


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions response structure.

    """

    def __init__(self):
        """
        :param GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessions: list of GameServerSession
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param Limit: Maximum number of entries in a single query
        :type Limit: int
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param PlayerId: Player ID. It should contain 1 to 1024 ASCII characters.
        :type PlayerId: str
        :param PlayerSessionId: Player session ID. It should contain 1 to 1024 ASCII characters.
        :type PlayerSessionId: str
        :param PlayerSessionStatusFilter: Player session status. Valid values: RESERVED, ACTIVE, COMPLETED, TIMEDOUT
        :type PlayerSessionStatusFilter: str
        """
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


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions response structure.

    """

    def __init__(self):
        """
        :param PlayerSessions: Player session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerSessions: list of PlayerSession
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DesiredPlayerSession(AbstractModel):
    """Player game session information

    """

    def __init__(self):
        """
        :param PlayerId: Unique player ID associated with player session
        :type PlayerId: str
        :param PlayerData: Developer-defined player data
        :type PlayerData: str
        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class GameProperty(AbstractModel):
    """Game attribute details

    """

    def __init__(self):
        """
        :param Key: Attribute name. Up to 32 ASCII characters are allowed.
        :type Key: str
        :param Value: Attribute value. Up to 96 ASCII characters are allowed.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class GameServerSession(AbstractModel):
    """Game session details

    """

    def __init__(self):
        """
        :param CreationTime: Game server session creation time
        :type CreationTime: str
        :param CreatorId: Creator ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreatorId: str
        :param CurrentPlayerSessionCount: The current number of players, which cannot be less than 0.
        :type CurrentPlayerSessionCount: int
        :param DnsName: CVM DNS ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param FleetId: Fleet ID
        :type FleetId: str
        :param GameProperties: Game attributes. Up to 16 groups of attributes are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: The attribute details of game server session. Up to 4096 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameServerSessionData: str
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        :param IpAddress: CVM IP address
        :type IpAddress: str
        :param MatchmakerData: Battle progress details. Up to 400,000 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchmakerData: str
        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param Name: The name of game server session. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Name: str
        :param PlayerSessionCreationPolicy: Player session creation policy. Valid values: ACCEPT_ALL, DENY_ALL
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerSessionCreationPolicy: str
        :param Port: Port number. It should be a value between 1 to 60000.
        :type Port: int
        :param Status: Game server session status. Valid values: ACTIVE, ACTIVATING, TERMINATED, TERMINATING, ERROR
        :type Status: str
        :param StatusReason: Additional information of game server session status
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusReason: str
        :param TerminationTime: Termination time
Note: this field may return null, indicating that no valid values can be obtained.
        :type TerminationTime: str
        :param InstanceType: Instance type. Up to 128 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type InstanceType: str
        :param CurrentCustomCount: Current custom count
Note: this field may return null, indicating that no valid values can be obtained.
        :type CurrentCustomCount: int
        :param MaxCustomCount: Maximum custom count
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxCustomCount: int
        :param Weight: Weight
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param AvailabilityStatus: Session availability status, i.e., whether it is blocked. Valid value: Enable, Disable
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AvailabilityStatus: str
        """
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


class GameServerSessionDetail(AbstractModel):
    """Game server session details (GameServerSessionDetail)

    """

    def __init__(self):
        """
        :param GameServerSession: Game server session
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param ProtectionPolicy: Protection policy. Valid values: NoProtection, FullProtection
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProtectionPolicy: str
        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class GameServerSessionPlacement(AbstractModel):
    """Game session deployment object

    """

    def __init__(self):
        """
        :param PlacementId: Deployment ID
        :type PlacementId: str
        :param GameServerSessionQueueName: Service deployment group name
        :type GameServerSessionQueueName: str
        :param PlayerLatencies: Player latency
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerLatencies: list of PlayerLatency
        :param Status: Service deployment status
        :type Status: str
        :param DnsName: DNS ID assigned to the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param GameServerSessionId: Game session ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionId: str
        :param GameServerSessionName: Game session name
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionName: str
        :param GameServerSessionRegion: Service deployment region
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionRegion: str
        :param GameProperties: Game attributes
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameProperties: list of GameProperty
        :param MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.
        :type MaximumPlayerSessionCount: int
        :param GameServerSessionData: Game session data
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessionData: str
        :param IpAddress: IP address of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpAddress: str
        :param Port: Port number of the instance where the game session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param MatchmakerData: Game match data
Note: this field may return null, indicating that no valid values can be obtained.
        :type MatchmakerData: str
        :param PlacedPlayerSessions: Deployed player game data
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        """
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


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 48 ASCII characters.
        :type GameServerSessionId: str
        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl response structure.

    """

    def __init__(self):
        """
        :param PreSignedUrl: Log download URL. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PreSignedUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FleetId: Server fleet ID
        :type FleetId: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.FleetId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess response structure.

    """

    def __init__(self):
        """
        :param InstanceAccess: Credentials required for instance login
        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self.InstanceAccess = InstanceAccess()
            self.InstanceAccess._deserialize(params.get("InstanceAccess"))
        self.RequestId = params.get("RequestId")


class InstanceAccess(AbstractModel):
    """Identity credentials for instance access

    """

    def __init__(self):
        """
        :param Credentials: Credentials required for instance access
        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`
        :param FleetId: Service deployment ID
        :type FleetId: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param IpAddress: Public IP of instance
        :type IpAddress: str
        :param OperatingSystem: OS
        :type OperatingSystem: str
        """
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


class JoinGameServerSessionBatchRequest(AbstractModel):
    """JoinGameServerSessionBatch request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param PlayerIds: Player ID list. At least 1 ID and up to 25 IDs.
        :type PlayerIds: list of str
        :param PlayerDataMap: Player custom data
        :type PlayerDataMap: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`
        """
        self.GameServerSessionId = None
        self.PlayerIds = None
        self.PlayerDataMap = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerIds = params.get("PlayerIds")
        if params.get("PlayerDataMap") is not None:
            self.PlayerDataMap = PlayerDataMap()
            self.PlayerDataMap._deserialize(params.get("PlayerDataMap"))


class JoinGameServerSessionBatchResponse(AbstractModel):
    """JoinGameServerSessionBatch response structure.

    """

    def __init__(self):
        """
        :param PlayerSessions: Player session list. Up to 25 sessions.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerSessions: list of PlayerSession
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param PlayerId: Player ID. Up to 1024 ASCII characters are allowed.
        :type PlayerId: str
        :param PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.
        :type PlayerData: str
        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession response structure.

    """

    def __init__(self):
        """
        :param PlayerSession: Player session
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param PlayerId: Player ID
        :type PlayerId: str
        :param PlayerSessionId: Player session ID
        :type PlayerSessionId: str
        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")


class PlayerDataMap(AbstractModel):
    """Player custom data

    """

    def __init__(self):
        """
        :param Key: The key of player custom data. It should contain 1 to 1024 ASCII characters.
        :type Key: str
        :param Value: The value of player custom data. It should contain 1 to 2048 ASCII characters.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class PlayerLatency(AbstractModel):
    """Player latency information

    """

    def __init__(self):
        """
        :param PlayerId: Player ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type PlayerId: str
        :param RegionIdentifier: Name of region corresponding to latency
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionIdentifier: str
        :param LatencyInMilliseconds: Latency in milliseconds
        :type LatencyInMilliseconds: int
        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")


class PlayerSession(AbstractModel):
    """Player session details

    """

    def __init__(self):
        """
        :param CreationTime: Player session creation time
        :type CreationTime: str
        :param DnsName: ID of the DNS where the game server session is running
Note: this field may return null, indicating that no valid values can be obtained.
        :type DnsName: str
        :param FleetId: Fleet ID
        :type FleetId: str
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param IpAddress: Address of the CVM instance where the game server session is running
        :type IpAddress: str
        :param PlayerData: Player custom data. Up to 2048 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerData: str
        :param PlayerId: Player ID. Up to 1024 ASCII characters are allowed.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type PlayerId: str
        :param PlayerSessionId: Player session ID
        :type PlayerSessionId: str
        :param Port: Port number. It should be a value between 1 to 60000.
        :type Port: int
        :param Status: Player session status. Valid values: RESERVED = 1, ACTIVE = 2, COMPLETED =3, TIMEDOUT = 4
        :type Status: str
        :param TerminationTime: Player session termination time
Note: this field may return null, indicating that no valid values can be obtained.
        :type TerminationTime: str
        """
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


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions request structure.

    """

    def __init__(self):
        """
        :param AliasId: Alias ID
        :type AliasId: str
        :param FleetId: Fleet ID
        :type FleetId: str
        :param Limit: Maximum number of entries in a single query
        :type Limit: int
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
        :type NextToken: str
        :param FilterExpression: Search filter expression. Valid values:
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
        :param SortExpression: Sorting keyword
Valid values:
gameServerSessionName: game session name in `String` type
gameServerSessionId: game session ID in `String` type
maximumSessions: maximum number of player sessions in `Number` type
creationTimeMillis: creation time in milliseconds in `Number` type
playerSessionCount: current number of player sessions in `Number` type
        :type SortExpression: str
        """
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


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions response structure.

    """

    def __init__(self):
        """
        :param GameServerSessions: Game server session list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GameServerSessions: list of GameServerSession
        :param NextToken: Pagination offset, which is used for querying the next page. It should contain 1 to 1024 ASCII characters.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NextToken: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement request structure.

    """

    def __init__(self):
        """
        :param PlacementId: The unique ID of the game server session placement. It should contain up to 48 ASCII characters, supporting [a-zA-Z0-9-]+.
        :type PlacementId: str
        :param GameServerSessionQueueName: Game server session queue name
        :type GameServerSessionQueueName: str
        :param MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session. It should a value between 1 to the maximum number of player sessions.
        :type MaximumPlayerSessionCount: int
        :param DesiredPlayerSessions: Player game session information
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param GameProperties: Player game session attributes
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: Data of game server sessions. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionData: str
        :param GameServerSessionName: Name of game server sessions. Up to 4096 ASCII characters are allowed.
        :type GameServerSessionName: str
        :param PlayerLatencies: Player latency
        :type PlayerLatencies: list of PlayerLatency
        """
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


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param PlacementId: Unique ID of game server session placement
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement response structure.

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: Game server session placement
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession request structure.

    """

    def __init__(self):
        """
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param MaximumPlayerSessionCount: The maximum number of players, which cannot be less than 0.
        :type MaximumPlayerSessionCount: int
        :param Name: Name of the game server session. It should contain 1 to 1024 ASCII characters.
        :type Name: str
        :param PlayerSessionCreationPolicy: Player session creation policy, which includes `ACCEPT_ALL` (allow all players) and `DENY_ALL` (reject all players).
        :type PlayerSessionCreationPolicy: str
        :param ProtectionPolicy: Protection policy, which includes `NoProtection`·(no protection), `TimeLimitProtection` (time-limited protection) and `FullProtection` (full protection)
        :type ProtectionPolicy: str
        """
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


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession response structure.

    """

    def __init__(self):
        """
        :param GameServerSession: Updated game session
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")