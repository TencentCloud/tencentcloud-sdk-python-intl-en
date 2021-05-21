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

import warnings

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMatchRequest(AbstractModel):
    """CreateMatch request structure.

    """

    def __init__(self):
        """
        :param MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type MatchName: str
        :param RuleCode: RuleCode
        :type RuleCode: str
        :param Timeout: Timeout period in seconds. Value range: 1 600
        :type Timeout: int
        :param ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.
        :type MatchDesc: str
        :param NotifyUrl: Only HTTP and HTTPS protocols are supported.
        :type NotifyUrl: str
        :param ServerRegion: Region of the game server queue
        :type ServerRegion: str
        :param ServerQueue: Game server queue
        :type ServerQueue: str
        :param CustomPushData: Custom push data
        :type CustomPushData: str
        :param ServerSessionData: Game server session data
        :type ServerSessionData: str
        :param GameProperties: Game attribute. It is an array of key-value structure.
        :type GameProperties: list of StringKV
        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param Tags: Tag. It is an array of key-value structure.
        :type Tags: list of StringKV
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMatchResponse(AbstractModel):
    """CreateMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type RuleName: str
        :param RuleScript: Rule script. Up to 65535 bytes are allowed.
        :type RuleScript: str
        :param RuleDesc: Rule description. Up to 1024 bytes are allowed.
        :type RuleDesc: str
        :param Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.
        :type Tags: list of StringKV
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMatchRequest(AbstractModel):
    """DeleteMatch request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMatchResponse(AbstractModel):
    """DeleteMatch response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode
        :type RuleCode: str
        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDataRequest(AbstractModel):
    """DescribeData request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time in seconds
        :type StartTime: int
        :param EndTime: End time in seconds
        :type EndTime: int
        :param TimeType: Time granularity. Valid values: 1: 1 day, 2: 1 hour, 3: 1 minute, 4: 10 minutes, 5: 30 minutes
        :type TimeType: int
        :param MatchCode: MatchCode
        :type MatchCode: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDataResponse(AbstractModel):
    """DescribeData response structure.

    """

    def __init__(self):
        """
        :param OverviewData: Matchmaking statistics overview
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`
        :param TrendData: Trend data of the number of matchmaking requests
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchCodesRequest(AbstractModel):
    """DescribeMatchCodes request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset, number of pages.
        :type Offset: int
        :param Limit: The number of MatchCodes per page
        :type Limit: int
        :param MatchCode: Query by the MatchCode value (a string).
        :type MatchCode: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchCodesResponse(AbstractModel):
    """DescribeMatchCodes response structure.

    """

    def __init__(self):
        """
        :param MatchCodes: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCodes: list of MatchCodeAttr
        :param TotalCount: The total number of queried MatchCodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchRequest(AbstractModel):
    """DescribeMatch request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchResponse(AbstractModel):
    """DescribeMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchesRequest(AbstractModel):
    """DescribeMatches request structure.

    """

    def __init__(self):
        """
        :param PageNumber: The current page number. If this parameter is left empty, all queried matches will be obtained.
        :type PageNumber: int
        :param PageSize: Number of matchmaking lists per page. If this parameter is left empty, all queried matches will be obtained.
        :type PageSize: int
        :param SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)
        :type SearchType: str
        :param Keyword: Keyword. Enter a keyword about SearchType to query.
        :type Keyword: str
        :param Tags: Tags. Enter a tag for querying.
        :type Tags: list of Tag
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMatchesResponse(AbstractModel):
    """DescribeMatches response structure.

    """

    def __init__(self):
        """
        :param MatchInfoList: Matchmaking information list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchInfoList: list of MatchInfo
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param PageNumber: The current page number. The first page will be returned by default if this parameter is left empty.
        :type PageNumber: int
        :param PageSize: The number of matches per page. If this parameter is left empty, 30 matches are displayed per page by default. Maximum value: 30
        :type PageSize: int
        :param SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)
        :type SearchType: str
        :param Keyword: Keyword for querying (optional)
        :type Keyword: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRuleRequest(AbstractModel):
    """DescribeRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode
        :type RuleCode: str
        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        """
        :param PageNumber: The current page number. The first page will be returned if this parameter is left empty.
        :type PageNumber: int
        :param PageSize: The number of rules per page. If this parameter is left empty, 30 rules are displayed per page by default. Maximum value: 30
        :type PageSize: int
        :param SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)
        :type SearchType: str
        :param Keyword: Keyword. Enter a keyword about SearchType to query.
        :type Keyword: str
        :param Tags: Tags. Enter a tag for querying.
        :type Tags: list of Tag
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        """
        :param RuleInfoList: Rule information list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleInfoList: list of RuleBriefInfo
        :param TotalCount: Total number of results
        :type TotalCount: int
        :param PageNumber: The current page number
        :type PageNumber: int
        :param PageSize: Number of rules per page
        :type PageSize: int
        :param SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)
        :type SearchType: str
        :param Keyword: Keyword for querying (optional)
        :type Keyword: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MatchCodeAttr(AbstractModel):
    """MatchCode

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MatchInfo(AbstractModel):
    """Matchmaking information

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param MatchName: Match name
        :type MatchName: str
        :param MatchDesc: Matchmaking description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchDesc: str
        :param RuleCode: RuleCode
        :type RuleCode: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Timeout: Timeout period
        :type Timeout: int
        :param NotifyUrl: Receiving notification address
        :type NotifyUrl: str
        :param ServerType: Whether to request server resources for the match results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param ServerRegion: Region of the server queue
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerRegion: str
        :param ServerQueue: Server queue
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerQueue: str
        :param CustomPushData: Custom push data
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CustomPushData: str
        :param ServerSessionData: Game server session data
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerSessionData: str
        :param GameProperties: Game attributes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameProperties: list of StringKV
        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param LogsetId: Logset ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogsetId: str
        :param LogsetName: Logset name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogsetName: str
        :param LogTopicId: Log topic ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogTopicId: str
        :param LogTopicName: Log topic name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogTopicName: str
        :param Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Tags: list of StringKV
        :param Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Region: str
        :param AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AppId: str
        :param Uin: User root account UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Uin: str
        :param CreateUin: Create user account UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateUin: str
        :param RuleName: Rule Name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleName: str
        :param LogStatus: Log status. 0: normal, 1: the log set does not exist, 2: the log topic does not exist, 3: neither the log set nor the log topic exists.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogStatus: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMatchRequest(AbstractModel):
    """ModifyMatch request structure.

    """

    def __init__(self):
        """
        :param MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type MatchName: str
        :param RuleCode: RuleCode
        :type RuleCode: str
        :param Timeout: Timeout period in seconds. Value range: 1 600
        :type Timeout: int
        :param ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.
        :type MatchDesc: str
        :param NotifyUrl: Only HTTP and HTTPS protocols are supported.
        :type NotifyUrl: str
        :param ServerRegion: Region of the game server queue
        :type ServerRegion: str
        :param ServerQueue: Game server queue
        :type ServerQueue: str
        :param CustomPushData: Custom push data
        :type CustomPushData: str
        :param ServerSessionData: Game server session data
        :type ServerSessionData: str
        :param GameProperties: Game attribute. It is an array of key-value structure.
        :type GameProperties: list of StringKV
        :param LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param Tags: Tag. It is an array of key-value structure.
        :type Tags: list of StringKV
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMatchResponse(AbstractModel):
    """ModifyMatch response structure.

    """

    def __init__(self):
        """
        :param MatchInfo: Matchmaking information
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        """
        :param RuleCode: RuleCode
        :type RuleCode: str
        :param RuleName: Rule name. It can only contain numbers, letters, ".", and "-".
        :type RuleName: str
        :param RuleDesc: Rule description. Up to 1024 bytes are allowed.
        :type RuleDesc: str
        :param Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.
        :type Tags: list of StringKV
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        """
        :param RuleInfo: Rule information
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReportOverviewData(AbstractModel):
    """Matchmaking statistics overview

    """

    def __init__(self):
        """
        :param TotalTimes: Total count
        :type TotalTimes: str
        :param SuccessPercent: Success rate
        :type SuccessPercent: float
        :param TimeoutPercent: Timeout rate
        :type TimeoutPercent: float
        :param FailPercent: Failure rate
        :type FailPercent: float
        :param AverageSec: Average matching time
        :type AverageSec: float
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReportTrendData(AbstractModel):
    """Trend data

    """

    def __init__(self):
        """
        :param TotalList: Total count
        :type TotalList: list of str
        :param CancelList: Number of requests cancelled
        :type CancelList: list of str
        :param SuccessList: Number of successes
        :type SuccessList: list of str
        :param FailList: Number of failures
        :type FailList: list of str
        :param TimeoutList: Number of request timeout
        :type TimeoutList: list of str
        :param TimeList: Time array in seconds
        :type TimeList: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleBriefInfo(AbstractModel):
    """Brief rule information

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It supports [a-zA-Z\d-\.]*.
        :type RuleName: str
        :param MatchCodeList: The associated match
        :type MatchCodeList: list of StringKV
        :param CreateTime: Creation time
        :type CreateTime: str
        :param RuleCode: RuleCode
        :type RuleCode: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        """
        :param RuleName: Rule name. It supports [a-zA-Z0-9-\.]*.
        :type RuleName: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param RuleDesc: Rule description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleDesc: str
        :param RuleScript: Rule script
        :type RuleScript: str
        :param Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Tags: list of StringKV
        :param MatchCodeList: The associated match
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCodeList: list of StringKV
        :param RuleCode: RuleCode
        :type RuleCode: str
        :param Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Region: str
        :param AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AppId: str
        :param Uin: User UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Uin: str
        :param CreateUin: User OwnerUin
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateUin: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartMatchingBackfillRequest(AbstractModel):
    """StartMatchingBackfill request structure.

    """

    def __init__(self):
        """
        :param MatchCode: MatchCode
        :type MatchCode: str
        :param Players: Player information
        :type Players: list of Player
        :param GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param MatchTicketId: MatchTicket ID, which can contain 1 to 128 characters. This parameter is left empty by default, and in this case, MatchTicket ID will be automatically generated by GPM.
        :type MatchTicketId: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartMatchingBackfillResponse(AbstractModel):
    """StartMatchingBackfill response structure.

    """

    def __init__(self):
        """
        :param MatchTicket: MatchTicket
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MatchTicket = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchTicket") is not None:
            self.MatchTicket = MatchTicket()
            self.MatchTicket._deserialize(params.get("MatchTicket"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StringKV(AbstractModel):
    """Key-value structure. Both key and value are string types.

    """

    def __init__(self):
        """
        :param Key: Key
        :type Key: str
        :param Value: Value
        :type Value: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        """
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        