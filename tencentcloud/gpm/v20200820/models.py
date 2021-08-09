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


class AttributeMap(AbstractModel):
    """The map key and map value of the player attribute

    """

    def __init__(self):
        """
        :param Key: Map key, supporting [a-zA-Z0-9-\.]*\n        :type Key: str\n        :param Value: Map value\n        :type Value: int\n        """
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
        


class CancelMatchingRequest(AbstractModel):
    """CancelMatching request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param MatchTicketId: The MatchTicket ID of the matchmaking to cancel\n        :type MatchTicketId: str\n        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMatchingResponse(AbstractModel):
    """CancelMatching response structure.

    """

    def __init__(self):
        """
        :param ErrCode: Error code\n        :type ErrCode: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class CreateMatchRequest(AbstractModel):
    """CreateMatch request structure.

    """

    def __init__(self):
        """
        :param MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.\n        :type MatchName: str\n        :param RuleCode: RuleCode\n        :type RuleCode: str\n        :param Timeout: Timeout period in seconds. Value range: 1 600\n        :type Timeout: int\n        :param ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources\n        :type ServerType: int\n        :param MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.\n        :type MatchDesc: str\n        :param NotifyUrl: Only HTTP and HTTPS protocols are supported.\n        :type NotifyUrl: str\n        :param ServerRegion: Region of the game server queue\n        :type ServerRegion: str\n        :param ServerQueue: Game server queue\n        :type ServerQueue: str\n        :param CustomPushData: Custom push data\n        :type CustomPushData: str\n        :param ServerSessionData: Game server session data\n        :type ServerSessionData: str\n        :param GameProperties: Game attribute. It is an array of key-value structure.\n        :type GameProperties: list of StringKV\n        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable\n        :type LogSwitch: int\n        :param Tags: Tag. It is an array of key-value structure.\n        :type Tags: list of StringKV\n        """
        self.MatchName = None
        self.RuleCode = None
        self.Timeout = None
        self.ServerType = None
        self.MatchDesc = None
        self.NotifyUrl = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.Tags = None


    def _deserialize(self, params):
        self.MatchName = params.get("MatchName")
        self.RuleCode = params.get("RuleCode")
        self.Timeout = params.get("Timeout")
        self.ServerType = params.get("ServerType")
        self.MatchDesc = params.get("MatchDesc")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMatchResponse(AbstractModel):
    """CreateMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.\n        :type RuleName: str\n        :param RuleScript: Rule script. Up to 65535 bytes are allowed.\n        :type RuleScript: str\n        :param RuleDesc: Rule description. Up to 1024 bytes are allowed.\n        :type RuleDesc: str\n        :param Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.\n        :type Tags: list of StringKV\n        """
        self.RuleName = None
        self.RuleScript = None
        self.RuleDesc = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.RuleScript = params.get("RuleScript")
        self.RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class DeleteMatchRequest(AbstractModel):
    """DeleteMatch request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMatchResponse(AbstractModel):
    """DeleteMatch response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode\n        :type RuleCode: str\n        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time in seconds\n        :type StartTime: int\n        :param EndTime: End time in seconds\n        :type EndTime: int\n        :param TimeType: Time granularity. Valid values: 1: 1 day, 2: 1 hour, 3: 1 minute, 4: 10 minutes, 5: 30 minutes\n        :type TimeType: int\n        :param MatchCode: MatchCode\n        :type MatchCode: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.TimeType = None
        self.MatchCode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TimeType = params.get("TimeType")
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData response structure.

    """

    def __init__(self):
        """
        :param OverviewData: Matchmaking statistics overview
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`\n        :param TrendData: Trend data of the number of matchmaking requests
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.OverviewData = None
        self.TrendData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OverviewData") is not None:
            self.OverviewData = ReportOverviewData()
            self.OverviewData._deserialize(params.get("OverviewData"))
        if params.get("TrendData") is not None:
            self.TrendData = ReportTrendData()
            self.TrendData._deserialize(params.get("TrendData"))
        self.RequestId = params.get("RequestId")


class DescribeMatchCodesRequest(AbstractModel):
    """DescribeMatchCodes request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset, number of pages.\n        :type Offset: int\n        :param Limit: The number of MatchCodes per page\n        :type Limit: int\n        :param MatchCode: Query by the MatchCode value (a string).\n        :type MatchCode: str\n        """
        self.Offset = None
        self.Limit = None
        self.MatchCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchCodesResponse(AbstractModel):
    """DescribeMatchCodes response structure.

    """

    def __init__(self):
        """
        :param MatchCodes: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchCodes: list of MatchCodeAttr\n        :param TotalCount: The total number of queried MatchCodes
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchCodes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchCodes") is not None:
            self.MatchCodes = []
            for item in params.get("MatchCodes"):
                obj = MatchCodeAttr()
                obj._deserialize(item)
                self.MatchCodes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMatchRequest(AbstractModel):
    """DescribeMatch request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchResponse(AbstractModel):
    """DescribeMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class DescribeMatchesRequest(AbstractModel):
    """DescribeMatches request structure.

    """

    def __init__(self):
        """
        :param PageNumber: The current page number. If this parameter is left empty, all queried matches will be obtained.\n        :type PageNumber: int\n        :param PageSize: Number of matchmaking lists per page. If this parameter is left empty, all queried matches will be obtained.\n        :type PageSize: int\n        :param SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)\n        :type SearchType: str\n        :param Keyword: Keyword. Enter a keyword about SearchType to query.\n        :type Keyword: str\n        :param Tags: Tags. Enter a tag for querying.\n        :type Tags: list of Tag\n        """
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchesResponse(AbstractModel):
    """DescribeMatches response structure.

    """

    def __init__(self):
        """
        :param MatchInfoList: Matchmaking information list
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchInfoList: list of MatchInfo\n        :param TotalCount: Total number of results\n        :type TotalCount: int\n        :param PageNumber: The current page number. The first page will be returned by default if this parameter is left empty.\n        :type PageNumber: int\n        :param PageSize: The number of matches per page. If this parameter is left empty, 30 matches are displayed per page by default. Maximum value: 30\n        :type PageSize: int\n        :param SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)\n        :type SearchType: str\n        :param Keyword: Keyword for querying (optional)\n        :type Keyword: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchInfoList = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfoList") is not None:
            self.MatchInfoList = []
            for item in params.get("MatchInfoList"):
                obj = MatchInfo()
                obj._deserialize(item)
                self.MatchInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        self.RequestId = params.get("RequestId")


class DescribeMatchingProgressRequest(AbstractModel):
    """DescribeMatchingProgress request structure.

    """

    def __init__(self):
        """
        :param MatchTicketIds: List of MatchTicket IDs. It can contain up to 12 IDs.\n        :type MatchTicketIds: list of MTicket\n        """
        self.MatchTicketIds = None


    def _deserialize(self, params):
        if params.get("MatchTicketIds") is not None:
            self.MatchTicketIds = []
            for item in params.get("MatchTicketIds"):
                obj = MTicket()
                obj._deserialize(item)
                self.MatchTicketIds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchingProgressResponse(AbstractModel):
    """DescribeMatchingProgress response structure.

    """

    def __init__(self):
        """
        :param MatchTickets: MatchTicket list
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchTickets: list of MatchTicket\n        :param ErrCode: Error code
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ErrCode: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeRuleRequest(AbstractModel):
    """DescribeRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode\n        :type RuleCode: str\n        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        """
        :param PageNumber: The current page number. The first page will be returned if this parameter is left empty.\n        :type PageNumber: int\n        :param PageSize: The number of rules per page. If this parameter is left empty, 30 rules are displayed per page by default. Maximum value: 30\n        :type PageSize: int\n        :param SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)\n        :type SearchType: str\n        :param Keyword: Keyword. Enter a keyword about SearchType to query.\n        :type Keyword: str\n        :param Tags: Tags. Enter a tag for querying.\n        :type Tags: list of Tag\n        """
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        """
        :param RuleInfoList: Rule information list
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RuleInfoList: list of RuleBriefInfo\n        :param TotalCount: Total number of results\n        :type TotalCount: int\n        :param PageNumber: The current page number\n        :type PageNumber: int\n        :param PageSize: Number of rules per page\n        :type PageSize: int\n        :param SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)\n        :type SearchType: str\n        :param Keyword: Keyword for querying (optional)\n        :type Keyword: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RuleInfoList = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfoList") is not None:
            self.RuleInfoList = []
            for item in params.get("RuleInfoList"):
                obj = RuleBriefInfo()
                obj._deserialize(item)
                self.RuleInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        self.RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    """DescribeToken request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenResponse(AbstractModel):
    """DescribeToken response structure.

    """

    def __init__(self):
        """
        :param MatchToken: The token corresponding to the current MatchCode. If the current MatchCode does not have a token, this parameter may not obtain a valid value.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchToken: str\n        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CompatibleSpan: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param MatchTicketId: MatchTicket ID\n        :type MatchTicketId: str\n        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchAttribute(AbstractModel):
    """Player attributes for matching

    """

    def __init__(self):
        """
        :param Name: Attribute name. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.\n        :type Name: str\n        :param Type: Attribute type. 0: number, 1: string. Default value: 0\n        :type Type: int\n        :param NumberValue: Numeric attribute value. Default value: 0.0\n        :type NumberValue: float\n        :param StringValue: String attribute value. Up to 128 characters are allowed. Default value: ""\n        :type StringValue: str\n        :param ListValue: List attribute value\n        :type ListValue: list of str\n        :param MapValue: Map attribute value\n        :type MapValue: list of AttributeMap\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchCodeAttr(AbstractModel):
    """MatchCode

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchCode: str\n        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchInfo(AbstractModel):
    """Matchmaking information

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param MatchName: Match name\n        :type MatchName: str\n        :param MatchDesc: Matchmaking description
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchDesc: str\n        :param RuleCode: RuleCode\n        :type RuleCode: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param Timeout: Timeout period\n        :type Timeout: int\n        :param NotifyUrl: Receiving notification address\n        :type NotifyUrl: str\n        :param ServerType: Whether to request server resources for the match results. 0: no, 1: request GSE resources\n        :type ServerType: int\n        :param ServerRegion: Region of the server queue
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ServerRegion: str\n        :param ServerQueue: Server queue
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ServerQueue: str\n        :param CustomPushData: Custom push data
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CustomPushData: str\n        :param ServerSessionData: Game server session data
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ServerSessionData: str\n        :param GameProperties: Game attributes
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type GameProperties: list of StringKV\n        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable\n        :type LogSwitch: int\n        :param LogsetId: Logset ID
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LogsetId: str\n        :param LogsetName: Logset name
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LogsetName: str\n        :param LogTopicId: Log topic ID
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LogTopicId: str\n        :param LogTopicName: Log topic name
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LogTopicName: str\n        :param Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Tags: list of StringKV\n        :param Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Region: str\n        :param AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AppId: str\n        :param Uin: User root account UIN
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Uin: str\n        :param CreateUin: Create user account UIN
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CreateUin: str\n        :param RuleName: Rule Name
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RuleName: str\n        :param LogStatus: Log status. 0: normal, 1: the log set does not exist, 2: the log topic does not exist, 3: neither the log set nor the log topic exists.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LogStatus: int\n        """
        self.MatchCode = None
        self.MatchName = None
        self.MatchDesc = None
        self.RuleCode = None
        self.CreateTime = None
        self.Timeout = None
        self.NotifyUrl = None
        self.ServerType = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.LogsetId = None
        self.LogsetName = None
        self.LogTopicId = None
        self.LogTopicName = None
        self.Tags = None
        self.Region = None
        self.AppId = None
        self.Uin = None
        self.CreateUin = None
        self.RuleName = None
        self.LogStatus = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchName = params.get("MatchName")
        self.MatchDesc = params.get("MatchDesc")
        self.RuleCode = params.get("RuleCode")
        self.CreateTime = params.get("CreateTime")
        self.Timeout = params.get("Timeout")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerType = params.get("ServerType")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.LogTopicId = params.get("LogTopicId")
        self.LogTopicName = params.get("LogTopicName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.CreateUin = params.get("CreateUin")
        self.RuleName = params.get("RuleName")
        self.LogStatus = params.get("LogStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchTicket(AbstractModel):
    """MatchTicket information

    """

    def __init__(self):
        """
        :param Id: MatchTicket ID. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.\n        :type Id: str\n        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param MatchResult: Different structure serialized results will be returned according to the MatchType.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchResult: str\n        :param MatchType: Matchmaking type. Valid values: NORMAL, GSE
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchType: str\n        :param Players: Player information list\n        :type Players: list of Player\n        :param Status: Matching status. Valid values: SEARCHING (matching), PLACING (pending match), COMPLETED (match completed), CANCELLED (match cancelled), TIMEDOUT (match timeouts), FAILED (match failed)\n        :type Status: str\n        :param StatusMessage: Matching status descriptions
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type StatusMessage: str\n        :param StatusReason: Reason for the matching status
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type StatusReason: str\n        :param StartTime: The time when the GPM received the matchmaking request, for example "2020-08-17T08:14:38.077Z".\n        :type StartTime: str\n        :param EndTime: The time when the matchmaking request stopped executing due to the completion, failure, timeout, or cancellation, for example "2020-08-17T08:14:38.077Z".
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type EndTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchRequest(AbstractModel):
    """ModifyMatch request structure.

    """

    def __init__(self):
        """
        :param MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.\n        :type MatchName: str\n        :param RuleCode: RuleCode\n        :type RuleCode: str\n        :param Timeout: Timeout period in seconds. Value range: 1 600\n        :type Timeout: int\n        :param ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources\n        :type ServerType: int\n        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.\n        :type MatchDesc: str\n        :param NotifyUrl: Only HTTP and HTTPS protocols are supported.\n        :type NotifyUrl: str\n        :param ServerRegion: Region of the game server queue\n        :type ServerRegion: str\n        :param ServerQueue: Game server queue\n        :type ServerQueue: str\n        :param CustomPushData: Custom push data\n        :type CustomPushData: str\n        :param ServerSessionData: Game server session data\n        :type ServerSessionData: str\n        :param GameProperties: Game attribute. It is an array of key-value structure.\n        :type GameProperties: list of StringKV\n        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable\n        :type LogSwitch: int\n        :param Tags: Tag. It is an array of key-value structure.\n        :type Tags: list of StringKV\n        """
        self.MatchName = None
        self.RuleCode = None
        self.Timeout = None
        self.ServerType = None
        self.MatchCode = None
        self.MatchDesc = None
        self.NotifyUrl = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.Tags = None


    def _deserialize(self, params):
        self.MatchName = params.get("MatchName")
        self.RuleCode = params.get("RuleCode")
        self.Timeout = params.get("Timeout")
        self.ServerType = params.get("ServerType")
        self.MatchCode = params.get("MatchCode")
        self.MatchDesc = params.get("MatchDesc")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchResponse(AbstractModel):
    """ModifyMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode\n        :type RuleCode: str\n        :param RuleName: Rule name. It can only contain numbers, letters, ".", and "-".\n        :type RuleName: str\n        :param RuleDesc: Rule description. Up to 1024 bytes are allowed.\n        :type RuleDesc: str\n        :param Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.\n        :type Tags: list of StringKV\n        """
        self.RuleCode = None
        self.RuleName = None
        self.RuleDesc = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        self.RuleName = params.get("RuleName")
        self.RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class ModifyTokenRequest(AbstractModel):
    """ModifyToken request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced. Value range: 0 - 1800. Within the CompatibleSpan time period, user will receive the current and original token in the event notification.\n        :type CompatibleSpan: int\n        :param MatchToken: Token. It can contain 0 - 64 characters, supporting [a-zA-Z0-9-_.]. If this parameter is left empty, the token will be randomly generated by GPM.\n        :type MatchToken: str\n        """
        self.MatchCode = None
        self.CompatibleSpan = None
        self.MatchToken = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.MatchToken = params.get("MatchToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenResponse(AbstractModel):
    """ModifyToken response structure.

    """

    def __init__(self):
        """
        :param MatchToken: Token that has been set successfully.\n        :type MatchToken: str\n        :param CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CompatibleSpan: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Id: Player ID. It can contain up to 128 characters, supporting [a-zA-Z\d-\._]*.\n        :type Id: str\n        :param Name: Player nickname. Up to 128 characters are allowed.\n        :type Name: str\n        :param MatchAttributes: Player attribute for matching. Up to 10 attributes are supported.\n        :type MatchAttributes: list of MatchAttribute\n        :param Team: Team name. A player can pass in a different team name, which can contain up to 128 characters, and support [a-zA-Z0-9-\.]*.\n        :type Team: str\n        :param CustomPlayerStatus: Custom player status. This parameter will be passed through. Value range: [0, 99999]\n        :type CustomPlayerStatus: int\n        :param CustomProfile: Custom player information. Up to 1024 characters are allowed. This parameter will be passed through.\n        :type CustomProfile: str\n        :param RegionLatencies: Number of delays in each area. Up to 20 delays are supported.\n        :type RegionLatencies: list of RegionLatency\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
ap-tokyo           Asia Pacific (Tokyo)\n        :type Region: str\n        :param Latency: Delay time in ms. Value range: 0 - 999999\n        :type Latency: int\n        """
        self.Region = None
        self.Latency = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportOverviewData(AbstractModel):
    """Matchmaking statistics overview

    """

    def __init__(self):
        """
        :param TotalTimes: Total count\n        :type TotalTimes: str\n        :param SuccessPercent: Success rate\n        :type SuccessPercent: float\n        :param TimeoutPercent: Timeout rate\n        :type TimeoutPercent: float\n        :param FailPercent: Failure rate\n        :type FailPercent: float\n        :param AverageSec: Average matching time\n        :type AverageSec: float\n        """
        self.TotalTimes = None
        self.SuccessPercent = None
        self.TimeoutPercent = None
        self.FailPercent = None
        self.AverageSec = None


    def _deserialize(self, params):
        self.TotalTimes = params.get("TotalTimes")
        self.SuccessPercent = params.get("SuccessPercent")
        self.TimeoutPercent = params.get("TimeoutPercent")
        self.FailPercent = params.get("FailPercent")
        self.AverageSec = params.get("AverageSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTrendData(AbstractModel):
    """Trend data

    """

    def __init__(self):
        """
        :param TotalList: Total count\n        :type TotalList: list of str\n        :param CancelList: Number of requests cancelled\n        :type CancelList: list of str\n        :param SuccessList: Number of successes\n        :type SuccessList: list of str\n        :param FailList: Number of failures\n        :type FailList: list of str\n        :param TimeoutList: Number of request timeout\n        :type TimeoutList: list of str\n        :param TimeList: Time array in seconds\n        :type TimeList: list of str\n        """
        self.TotalList = None
        self.CancelList = None
        self.SuccessList = None
        self.FailList = None
        self.TimeoutList = None
        self.TimeList = None


    def _deserialize(self, params):
        self.TotalList = params.get("TotalList")
        self.CancelList = params.get("CancelList")
        self.SuccessList = params.get("SuccessList")
        self.FailList = params.get("FailList")
        self.TimeoutList = params.get("TimeoutList")
        self.TimeList = params.get("TimeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleBriefInfo(AbstractModel):
    """Brief rule information

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It supports [a-zA-Z\d-\.]*.\n        :type RuleName: str\n        :param MatchCodeList: The associated match\n        :type MatchCodeList: list of StringKV\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param RuleCode: RuleCode\n        :type RuleCode: str\n        """
        self.RuleName = None
        self.MatchCodeList = None
        self.CreateTime = None
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("MatchCodeList") is not None:
            self.MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self.MatchCodeList.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It supports [a-zA-Z0-9-\.]*.\n        :type RuleName: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param RuleDesc: Rule description
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RuleDesc: str\n        :param RuleScript: Rule script\n        :type RuleScript: str\n        :param Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Tags: list of StringKV\n        :param MatchCodeList: The associated match
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MatchCodeList: list of StringKV\n        :param RuleCode: RuleCode\n        :type RuleCode: str\n        :param Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Region: str\n        :param AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type AppId: str\n        :param Uin: User UIN
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Uin: str\n        :param CreateUin: User OwnerUin
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type CreateUin: str\n        """
        self.RuleName = None
        self.CreateTime = None
        self.RuleDesc = None
        self.RuleScript = None
        self.Tags = None
        self.MatchCodeList = None
        self.RuleCode = None
        self.Region = None
        self.AppId = None
        self.Uin = None
        self.CreateUin = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.CreateTime = params.get("CreateTime")
        self.RuleDesc = params.get("RuleDesc")
        self.RuleScript = params.get("RuleScript")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("MatchCodeList") is not None:
            self.MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self.MatchCodeList.append(obj)
        self.RuleCode = params.get("RuleCode")
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.CreateUin = params.get("CreateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillRequest(AbstractModel):
    """StartMatchingBackfill request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param Players: Player information\n        :type Players: list of Player\n        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.\n        :type GameServerSessionId: str\n        :param MatchTicketId: MatchTicket ID, which can contain 1 to 128 characters. This parameter is left empty by default, and in this case, MatchTicket ID will be automatically generated by GPM.\n        :type MatchTicketId: str\n        """
        self.MatchCode = None
        self.Players = None
        self.GameServerSessionId = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillResponse(AbstractModel):
    """StartMatchingBackfill response structure.

    """

    def __init__(self):
        """
        :param MatchTicket: MatchTicket
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MatchTicket = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchTicket") is not None:
            self.MatchTicket = MatchTicket()
            self.MatchTicket._deserialize(params.get("MatchTicket"))
        self.RequestId = params.get("RequestId")


class StartMatchingRequest(AbstractModel):
    """StartMatching request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode\n        :type MatchCode: str\n        :param Players: Player information. Up to 200 entries can be entered.\n        :type Players: list of Player\n        :param MatchTicketId: MatchTicket ID, which can contain up to 128 characters and can only contain numbers, letters, “.”, and “-”. This parameter is left empty by default. When it is empty, the MatchTicket ID will be automatically generated by GPM.\n        :type MatchTicketId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingResponse(AbstractModel):
    """StartMatching response structure.

    """

    def __init__(self):
        """
        :param ErrCode: Error code\n        :type ErrCode: int\n        :param MatchTicketId: MatchTicket ID. Up to 128 characters are allowed.\n        :type MatchTicketId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.MatchTicketId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.MatchTicketId = params.get("MatchTicketId")
        self.RequestId = params.get("RequestId")


class StringKV(AbstractModel):
    """Key-value structure. Both key and value are string types.

    """

    def __init__(self):
        """
        :param Key: Key\n        :type Key: str\n        :param Value: Value\n        :type Value: str\n        """
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
        


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        