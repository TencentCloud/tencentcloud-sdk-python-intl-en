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


class AttributeMap(AbstractModel):
    """The map key and map value of the player attribute

    """

    def __init__(self):
        """
        :param Key: Map key, supporting [a-zA-Z0-9-\.]*
        :type Key: str
        :param Value: Map value
        :type Value: int
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class CancelMatchingRequest(AbstractModel):
    """CancelMatching request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param MatchTicketId: The MatchTicket ID of the matchmaking to cancel
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")


class CancelMatchingResponse(AbstractModel):
    """CancelMatching response structure.

    """

    def __init__(self):
        """
        :param ErrCode: Error code
        :type ErrCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class DescribeMatchingProgressRequest(AbstractModel):
    """DescribeMatchingProgress request structure.

    """

    def __init__(self):
        """
        :param MatchTicketIds: List of MatchTicket IDs. It can contain up to 12 IDs.
        :type MatchTicketIds: list of MTicket
        """
        self.MatchTicketIds = None


    def _deserialize(self, params):
        if params.get("MatchTicketIds") is not None:
            self.MatchTicketIds = []
            for item in params.get("MatchTicketIds"):
                obj = MTicket()
                obj._deserialize(item)
                self.MatchTicketIds.append(obj)


class DescribeMatchingProgressResponse(AbstractModel):
    """DescribeMatchingProgress response structure.

    """

    def __init__(self):
        """
        :param MatchTickets: MatchTicket list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchTickets: list of MatchTicket
        :param ErrCode: Error code
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ErrCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchTickets = None
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchTickets") is not None:
            self.MatchTickets = []
            for item in params.get("MatchTickets"):
                obj = MatchTicket()
                obj._deserialize(item)
                self.MatchTickets.append(obj)
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    """DescribeToken request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")


class DescribeTokenResponse(AbstractModel):
    """DescribeToken response structure.

    """

    def __init__(self):
        """
        :param MatchToken: The token corresponding to the current MatchCode. If the current MatchCode does not have a token, this parameter may not obtain a valid value.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchToken: str
        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CompatibleSpan: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchToken = None
        self.CompatibleSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MatchToken = params.get("MatchToken")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.RequestId = params.get("RequestId")


class MTicket(AbstractModel):
    """The combination of MatchCode and MatchTicket ID.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param MatchTicketId: MatchTicket ID
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")


class MatchAttribute(AbstractModel):
    """Player attributes for matching

    """

    def __init__(self):
        """
        :param Name: Attribute name. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.
        :type Name: str
        :param Type: Attribute type. 0: number, 1: string. Default value: 0
        :type Type: int
        :param NumberValue: Numeric attribute value. Default value: 0.0
        :type NumberValue: float
        :param StringValue: String attribute value. Up to 128 characters are allowed. Default value: ""
        :type StringValue: str
        :param ListValue: List attribute value
        :type ListValue: list of str
        :param MapValue: Map attribute value
        :type MapValue: list of AttributeMap
        """
        self.Name = None
        self.Type = None
        self.NumberValue = None
        self.StringValue = None
        self.ListValue = None
        self.MapValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.NumberValue = params.get("NumberValue")
        self.StringValue = params.get("StringValue")
        self.ListValue = params.get("ListValue")
        if params.get("MapValue") is not None:
            self.MapValue = []
            for item in params.get("MapValue"):
                obj = AttributeMap()
                obj._deserialize(item)
                self.MapValue.append(obj)


class MatchTicket(AbstractModel):
    """MatchTicket information

    """

    def __init__(self):
        """
        :param Id: MatchTicket ID. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.
        :type Id: str
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param MatchResult: Different structure serialized results will be returned according to the MatchType.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchResult: str
        :param MatchType: Matchmaking type. Valid values: NORMAL, GSE
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchType: str
        :param Players: Player information list
        :type Players: list of Player
        :param Status: Matching status. Valid values: SEARCHING (matching), PLACING (pending match), COMPLETED (match completed), CANCELLED (match cancelled), TIMEDOUT (match timeouts), FAILED (match failed)
        :type Status: str
        :param StatusMessage: Matching status descriptions
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StatusMessage: str
        :param StatusReason: Reason for the matching status
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StatusReason: str
        :param StartTime: The time when the GPM received the matchmaking request, for example "2020-08-17T08:14:38.077Z".
        :type StartTime: str
        :param EndTime: The time when the matchmaking request stopped executing due to the completion, failure, timeout, or cancellation, for example "2020-08-17T08:14:38.077Z".
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndTime: str
        """
        self.Id = None
        self.MatchCode = None
        self.MatchResult = None
        self.MatchType = None
        self.Players = None
        self.Status = None
        self.StatusMessage = None
        self.StatusReason = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MatchCode = params.get("MatchCode")
        self.MatchResult = params.get("MatchResult")
        self.MatchType = params.get("MatchType")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.Status = params.get("Status")
        self.StatusMessage = params.get("StatusMessage")
        self.StatusReason = params.get("StatusReason")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyTokenRequest(AbstractModel):
    """ModifyToken request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced. Value range: 0 - 1800. Within the CompatibleSpan time period, user will receive the current and original token in the event notification.
        :type CompatibleSpan: int
        :param MatchToken: Token. It can contain 0 - 64 characters, supporting [a-zA-Z0-9-_.]. If this parameter is left empty, the token will be randomly generated by GPM.
        :type MatchToken: str
        """
        self.MatchCode = None
        self.CompatibleSpan = None
        self.MatchToken = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.MatchToken = params.get("MatchToken")


class ModifyTokenResponse(AbstractModel):
    """ModifyToken response structure.

    """

    def __init__(self):
        """
        :param MatchToken: Token that has been set successfully.
        :type MatchToken: str
        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CompatibleSpan: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchToken = None
        self.CompatibleSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MatchToken = params.get("MatchToken")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.RequestId = params.get("RequestId")


class Player(AbstractModel):
    """Player information

    """

    def __init__(self):
        """
        :param Id: Player ID. It can contain up to 128 characters, supporting [a-zA-Z\d-\._]*.
        :type Id: str
        :param Name: Player nickname. Up to 128 characters are allowed.
        :type Name: str
        :param MatchAttributes: Player attribute for matching. Up to 10 attributes are supported.
        :type MatchAttributes: list of MatchAttribute
        :param Team: Team name. A player can pass in a different team name, which can contain up to 128 characters, and support [a-zA-Z0-9-\.]*.
        :type Team: str
        :param CustomPlayerStatus: Custom player status. This parameter will be passed through. Value range: [0, 99999]
        :type CustomPlayerStatus: int
        :param CustomProfile: Custom player information. Up to 1024 characters are allowed. This parameter will be passed through.
        :type CustomProfile: str
        :param RegionLatencies: Number of delays in each area. Up to 20 delays are supported.
        :type RegionLatencies: list of RegionLatency
        """
        self.Id = None
        self.Name = None
        self.MatchAttributes = None
        self.Team = None
        self.CustomPlayerStatus = None
        self.CustomProfile = None
        self.RegionLatencies = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("MatchAttributes") is not None:
            self.MatchAttributes = []
            for item in params.get("MatchAttributes"):
                obj = MatchAttribute()
                obj._deserialize(item)
                self.MatchAttributes.append(obj)
        self.Team = params.get("Team")
        self.CustomPlayerStatus = params.get("CustomPlayerStatus")
        self.CustomProfile = params.get("CustomProfile")
        if params.get("RegionLatencies") is not None:
            self.RegionLatencies = []
            for item in params.get("RegionLatencies"):
                obj = RegionLatency()
                obj._deserialize(item)
                self.RegionLatencies.append(obj)


class RegionLatency(AbstractModel):
    """The network delay time for players to reach different regions.

    """

    def __init__(self):
        """
        :param Region: Region
ap-beijing          North China (Beijing)
ap-chengdu          Southwest China (Chengdu)
ap-guangzhou           South China (Guangzhou)
ap-hongkong           Hong Kong/Macao/Taiwan (Hong Kong, China)
ap-seoul          Asia Pacific (Seoul)
ap-shanghai          East China (Shanghai)
ap-singapore          Southeast Asia (Singapore)
eu-frankfurt          Europe (Frankfurt)
na-siliconvalley          Western US (Silicon Valley)
na-toronto           North America (Toronto)
ap-mumbai           Asia Pacific (Mumbai)
na-ashburn          Eastern US (Virginia)
ap-bangkok           Asia Pacific (Bangkok)
eu-moscow           Europe (Moscow)
ap-tokyo           Asia Pacific (Tokyo)
        :type Region: str
        :param Latency: Delay time in ms. Value range: 0 - 999999
        :type Latency: int
        """
        self.Region = None
        self.Latency = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Latency = params.get("Latency")


class StartMatchingRequest(AbstractModel):
    """StartMatching request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param Players: Player information. Up to 200 entries can be entered.
        :type Players: list of Player
        :param MatchTicketId: MatchTicket ID, which can contain up to 128 characters and can only contain numbers, letters, “.”, and “-”. This parameter is left empty by default. When it is empty, the MatchTicket ID will be automatically generated by GPM.
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.Players = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.MatchTicketId = params.get("MatchTicketId")


class StartMatchingResponse(AbstractModel):
    """StartMatching response structure.

    """

    def __init__(self):
        """
        :param ErrCode: Error code
        :type ErrCode: int
        :param MatchTicketId: MatchTicket ID. Up to 128 characters are allowed.
        :type MatchTicketId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ErrCode = None
        self.MatchTicketId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.MatchTicketId = params.get("MatchTicketId")
        self.RequestId = params.get("RequestId")