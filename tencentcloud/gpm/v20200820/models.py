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
        r"""
        :param _Key: Map key, supporting [a-zA-Z0-9-\.]*
        :type Key: str
        :param _Value: Map value
        :type Value: int
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
        


class CancelMatchingRequest(AbstractModel):
    """CancelMatching request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _MatchTicketId: The MatchTicket ID of the matchmaking to cancel
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchTicketId(self):
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMatchingResponse(AbstractModel):
    """CancelMatching response structure.

    """

    def __init__(self):
        r"""
        :param _ErrCode: Error code
        :type ErrCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrCode = None
        self._RequestId = None

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrCode = params.get("ErrCode")
        self._RequestId = params.get("RequestId")


class CreateMatchRequest(AbstractModel):
    """CreateMatch request structure.

    """

    def __init__(self):
        r"""
        :param _MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type MatchName: str
        :param _RuleCode: RuleCode
        :type RuleCode: str
        :param _Timeout: Timeout period in seconds. Value range: 1 600
        :type Timeout: int
        :param _ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param _MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.
        :type MatchDesc: str
        :param _NotifyUrl: Only HTTP and HTTPS protocols are supported.
        :type NotifyUrl: str
        :param _ServerRegion: Region of the game server queue
        :type ServerRegion: str
        :param _ServerQueue: Game server queue
        :type ServerQueue: str
        :param _CustomPushData: Custom push data
        :type CustomPushData: str
        :param _ServerSessionData: Game server session data
        :type ServerSessionData: str
        :param _GameProperties: Game attribute. It is an array of key-value structure.
        :type GameProperties: list of StringKV
        :param _LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param _Tags: Tag. It is an array of key-value structure.
        :type Tags: list of StringKV
        """
        self._MatchName = None
        self._RuleCode = None
        self._Timeout = None
        self._ServerType = None
        self._MatchDesc = None
        self._NotifyUrl = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._Tags = None

    @property
    def MatchName(self):
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def MatchDesc(self):
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def NotifyUrl(self):
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerRegion(self):
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MatchName = params.get("MatchName")
        self._RuleCode = params.get("RuleCode")
        self._Timeout = params.get("Timeout")
        self._ServerType = params.get("ServerType")
        self._MatchDesc = params.get("MatchDesc")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMatchResponse(AbstractModel):
    """CreateMatch response structure.

    """

    def __init__(self):
        r"""
        :param _MatchInfo: Matchmaking information
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type RuleName: str
        :param _RuleScript: Rule script. Up to 65535 bytes are allowed.
        :type RuleScript: str
        :param _RuleDesc: Rule description. Up to 1024 bytes are allowed.
        :type RuleDesc: str
        :param _Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.
        :type Tags: list of StringKV
        """
        self._RuleName = None
        self._RuleScript = None
        self._RuleDesc = None
        self._Tags = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleScript(self):
        return self._RuleScript

    @RuleScript.setter
    def RuleScript(self, RuleScript):
        self._RuleScript = RuleScript

    @property
    def RuleDesc(self):
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RuleScript = params.get("RuleScript")
        self._RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleInfo: Rule information
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class DeleteMatchRequest(AbstractModel):
    """DeleteMatch request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMatchResponse(AbstractModel):
    """DeleteMatch response structure.

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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleCode: RuleCode
        :type RuleCode: str
        """
        self._RuleCode = None

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule response structure.

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


class DescribeDataRequest(AbstractModel):
    """DescribeData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time in seconds
        :type StartTime: int
        :param _EndTime: End time in seconds
        :type EndTime: int
        :param _TimeType: Time granularity. Valid values: 1: 1 day, 2: 1 hour, 3: 1 minute, 4: 10 minutes, 5: 30 minutes
        :type TimeType: int
        :param _MatchCode: MatchCode
        :type MatchCode: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TimeType = None
        self._MatchCode = None

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

    @property
    def TimeType(self):
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TimeType = params.get("TimeType")
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData response structure.

    """

    def __init__(self):
        r"""
        :param _OverviewData: Matchmaking statistics overview
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`
        :param _TrendData: Trend data of the number of matchmaking requests
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OverviewData = None
        self._TrendData = None
        self._RequestId = None

    @property
    def OverviewData(self):
        return self._OverviewData

    @OverviewData.setter
    def OverviewData(self, OverviewData):
        self._OverviewData = OverviewData

    @property
    def TrendData(self):
        return self._TrendData

    @TrendData.setter
    def TrendData(self, TrendData):
        self._TrendData = TrendData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OverviewData") is not None:
            self._OverviewData = ReportOverviewData()
            self._OverviewData._deserialize(params.get("OverviewData"))
        if params.get("TrendData") is not None:
            self._TrendData = ReportTrendData()
            self._TrendData._deserialize(params.get("TrendData"))
        self._RequestId = params.get("RequestId")


class DescribeMatchCodesRequest(AbstractModel):
    """DescribeMatchCodes request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, number of pages.
        :type Offset: int
        :param _Limit: The number of MatchCodes per page
        :type Limit: int
        :param _MatchCode: Query by the MatchCode value (a string).
        :type MatchCode: str
        """
        self._Offset = None
        self._Limit = None
        self._MatchCode = None

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

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchCodesResponse(AbstractModel):
    """DescribeMatchCodes response structure.

    """

    def __init__(self):
        r"""
        :param _MatchCodes: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCodes: list of MatchCodeAttr
        :param _TotalCount: The total number of queried MatchCodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchCodes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MatchCodes(self):
        return self._MatchCodes

    @MatchCodes.setter
    def MatchCodes(self, MatchCodes):
        self._MatchCodes = MatchCodes

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
        if params.get("MatchCodes") is not None:
            self._MatchCodes = []
            for item in params.get("MatchCodes"):
                obj = MatchCodeAttr()
                obj._deserialize(item)
                self._MatchCodes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMatchRequest(AbstractModel):
    """DescribeMatch request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchResponse(AbstractModel):
    """DescribeMatch response structure.

    """

    def __init__(self):
        r"""
        :param _MatchInfo: Matchmaking information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class DescribeMatchesRequest(AbstractModel):
    """DescribeMatches request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: The current page number. If this parameter is left empty, all queried matches will be obtained.
        :type PageNumber: int
        :param _PageSize: Number of matchmaking lists per page. If this parameter is left empty, all queried matches will be obtained.
        :type PageSize: int
        :param _SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)
        :type SearchType: str
        :param _Keyword: Keyword. Enter a keyword about SearchType to query.
        :type Keyword: str
        :param _Tags: Tags. Enter a tag for querying.
        :type Tags: list of Tag
        """
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._Tags = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchesResponse(AbstractModel):
    """DescribeMatches response structure.

    """

    def __init__(self):
        r"""
        :param _MatchInfoList: Matchmaking information list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchInfoList: list of MatchInfo
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _PageNumber: The current page number. The first page will be returned by default if this parameter is left empty.
        :type PageNumber: int
        :param _PageSize: The number of matches per page. If this parameter is left empty, 30 matches are displayed per page by default. Maximum value: 30
        :type PageSize: int
        :param _SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)
        :type SearchType: str
        :param _Keyword: Keyword for querying (optional)
        :type Keyword: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchInfoList = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._RequestId = None

    @property
    def MatchInfoList(self):
        return self._MatchInfoList

    @MatchInfoList.setter
    def MatchInfoList(self, MatchInfoList):
        self._MatchInfoList = MatchInfoList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchInfoList") is not None:
            self._MatchInfoList = []
            for item in params.get("MatchInfoList"):
                obj = MatchInfo()
                obj._deserialize(item)
                self._MatchInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        self._RequestId = params.get("RequestId")


class DescribeMatchingProgressRequest(AbstractModel):
    """DescribeMatchingProgress request structure.

    """

    def __init__(self):
        r"""
        :param _MatchTicketIds: List of MatchTicket IDs. It can contain up to 12 IDs.
        :type MatchTicketIds: list of MTicket
        """
        self._MatchTicketIds = None

    @property
    def MatchTicketIds(self):
        return self._MatchTicketIds

    @MatchTicketIds.setter
    def MatchTicketIds(self, MatchTicketIds):
        self._MatchTicketIds = MatchTicketIds


    def _deserialize(self, params):
        if params.get("MatchTicketIds") is not None:
            self._MatchTicketIds = []
            for item in params.get("MatchTicketIds"):
                obj = MTicket()
                obj._deserialize(item)
                self._MatchTicketIds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchingProgressResponse(AbstractModel):
    """DescribeMatchingProgress response structure.

    """

    def __init__(self):
        r"""
        :param _MatchTickets: MatchTicket list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchTickets: list of MatchTicket
        :param _ErrCode: Error code
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ErrCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchTickets = None
        self._ErrCode = None
        self._RequestId = None

    @property
    def MatchTickets(self):
        return self._MatchTickets

    @MatchTickets.setter
    def MatchTickets(self, MatchTickets):
        self._MatchTickets = MatchTickets

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchTickets") is not None:
            self._MatchTickets = []
            for item in params.get("MatchTickets"):
                obj = MatchTicket()
                obj._deserialize(item)
                self._MatchTickets.append(obj)
        self._ErrCode = params.get("ErrCode")
        self._RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleCode: RuleCode
        :type RuleCode: str
        """
        self._RuleCode = None

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleInfo: Rule information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: The current page number. The first page will be returned if this parameter is left empty.
        :type PageNumber: int
        :param _PageSize: The number of rules per page. If this parameter is left empty, 30 rules are displayed per page by default. Maximum value: 30
        :type PageSize: int
        :param _SearchType: Query type (optional). Valid values: match (query by matchCode or matchName), rule (query by ruleCode or ruleName), and other types (not filtered)
        :type SearchType: str
        :param _Keyword: Keyword. Enter a keyword about SearchType to query.
        :type Keyword: str
        :param _Tags: Tags. Enter a tag for querying.
        :type Tags: list of Tag
        """
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._Tags = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param _RuleInfoList: Rule information list
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleInfoList: list of RuleBriefInfo
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _PageNumber: The current page number
        :type PageNumber: int
        :param _PageSize: Number of rules per page
        :type PageSize: int
        :param _SearchType: Query type (optional). Valid values: matchName (query by match name), matchCode (query by matchCode), ruleName (query by rule name), and tag (query by tag key/value)
        :type SearchType: str
        :param _Keyword: Keyword for querying (optional)
        :type Keyword: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleInfoList = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._RequestId = None

    @property
    def RuleInfoList(self):
        return self._RuleInfoList

    @RuleInfoList.setter
    def RuleInfoList(self, RuleInfoList):
        self._RuleInfoList = RuleInfoList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleInfoList") is not None:
            self._RuleInfoList = []
            for item in params.get("RuleInfoList"):
                obj = RuleBriefInfo()
                obj._deserialize(item)
                self._RuleInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        self._RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    """DescribeToken request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenResponse(AbstractModel):
    """DescribeToken response structure.

    """

    def __init__(self):
        r"""
        :param _MatchToken: The token corresponding to the current MatchCode. If the current MatchCode does not have a token, this parameter may not obtain a valid value.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchToken: str
        :param _CompatibleSpan: The time period during which GPM will continuously push the original token in seconds when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CompatibleSpan: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchToken = None
        self._CompatibleSpan = None
        self._RequestId = None

    @property
    def MatchToken(self):
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken

    @property
    def CompatibleSpan(self):
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MatchToken = params.get("MatchToken")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._RequestId = params.get("RequestId")


class MTicket(AbstractModel):
    """The combination of MatchCode and MatchTicket ID.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _MatchTicketId: MatchTicket ID
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchTicketId(self):
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchAttribute(AbstractModel):
    """Player attributes for matching

    """

    def __init__(self):
        r"""
        :param _Name: Attribute name. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.
        :type Name: str
        :param _Type: Attribute type. 0: number, 1: string. Default value: 0
        :type Type: int
        :param _NumberValue: Numeric attribute value. Default value: 0.0
        :type NumberValue: float
        :param _StringValue: String attribute value. Up to 128 characters are allowed. Default value: ""
        :type StringValue: str
        :param _ListValue: List attribute value
        :type ListValue: list of str
        :param _MapValue: Map attribute value
        :type MapValue: list of AttributeMap
        """
        self._Name = None
        self._Type = None
        self._NumberValue = None
        self._StringValue = None
        self._ListValue = None
        self._MapValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NumberValue(self):
        return self._NumberValue

    @NumberValue.setter
    def NumberValue(self, NumberValue):
        self._NumberValue = NumberValue

    @property
    def StringValue(self):
        return self._StringValue

    @StringValue.setter
    def StringValue(self, StringValue):
        self._StringValue = StringValue

    @property
    def ListValue(self):
        return self._ListValue

    @ListValue.setter
    def ListValue(self, ListValue):
        self._ListValue = ListValue

    @property
    def MapValue(self):
        return self._MapValue

    @MapValue.setter
    def MapValue(self, MapValue):
        self._MapValue = MapValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._NumberValue = params.get("NumberValue")
        self._StringValue = params.get("StringValue")
        self._ListValue = params.get("ListValue")
        if params.get("MapValue") is not None:
            self._MapValue = []
            for item in params.get("MapValue"):
                obj = AttributeMap()
                obj._deserialize(item)
                self._MapValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchCodeAttr(AbstractModel):
    """MatchCode

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchInfo(AbstractModel):
    """Matchmaking information

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _MatchName: Match name
        :type MatchName: str
        :param _MatchDesc: Matchmaking description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchDesc: str
        :param _RuleCode: RuleCode
        :type RuleCode: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Timeout: Timeout period
        :type Timeout: int
        :param _NotifyUrl: Receiving notification address
        :type NotifyUrl: str
        :param _ServerType: Whether to request server resources for the match results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param _ServerRegion: Region of the server queue
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerRegion: str
        :param _ServerQueue: Server queue
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerQueue: str
        :param _CustomPushData: Custom push data
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CustomPushData: str
        :param _ServerSessionData: Game server session data
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ServerSessionData: str
        :param _GameProperties: Game attributes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type GameProperties: list of StringKV
        :param _LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param _LogsetId: Logset ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogsetId: str
        :param _LogsetName: Logset name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogsetName: str
        :param _LogTopicId: Log topic ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogTopicId: str
        :param _LogTopicName: Log topic name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogTopicName: str
        :param _Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Tags: list of StringKV
        :param _Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Region: str
        :param _AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AppId: str
        :param _Uin: User root account UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Uin: str
        :param _CreateUin: Create user account UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateUin: str
        :param _RuleName: Rule Name
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleName: str
        :param _LogStatus: Log status. 0: normal, 1: the log set does not exist, 2: the log topic does not exist, 3: neither the log set nor the log topic exists.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogStatus: int
        """
        self._MatchCode = None
        self._MatchName = None
        self._MatchDesc = None
        self._RuleCode = None
        self._CreateTime = None
        self._Timeout = None
        self._NotifyUrl = None
        self._ServerType = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._LogsetId = None
        self._LogsetName = None
        self._LogTopicId = None
        self._LogTopicName = None
        self._Tags = None
        self._Region = None
        self._AppId = None
        self._Uin = None
        self._CreateUin = None
        self._RuleName = None
        self._LogStatus = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchName(self):
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def MatchDesc(self):
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def NotifyUrl(self):
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def ServerRegion(self):
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogTopicName(self):
        return self._LogTopicName

    @LogTopicName.setter
    def LogTopicName(self, LogTopicName):
        self._LogTopicName = LogTopicName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def LogStatus(self):
        return self._LogStatus

    @LogStatus.setter
    def LogStatus(self, LogStatus):
        self._LogStatus = LogStatus


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchName = params.get("MatchName")
        self._MatchDesc = params.get("MatchDesc")
        self._RuleCode = params.get("RuleCode")
        self._CreateTime = params.get("CreateTime")
        self._Timeout = params.get("Timeout")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerType = params.get("ServerType")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._LogTopicId = params.get("LogTopicId")
        self._LogTopicName = params.get("LogTopicName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CreateUin = params.get("CreateUin")
        self._RuleName = params.get("RuleName")
        self._LogStatus = params.get("LogStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchTicket(AbstractModel):
    """MatchTicket information

    """

    def __init__(self):
        r"""
        :param _Id: MatchTicket ID. It can contain up to 128 characters, supporting [a-zA-Z0-9-\.]*.
        :type Id: str
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _MatchResult: Different structure serialized results will be returned according to the MatchType.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchResult: str
        :param _MatchType: Matchmaking type. Valid values: NORMAL, GSE
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchType: str
        :param _Players: Player information list
        :type Players: list of Player
        :param _Status: Matching status. Valid values: SEARCHING (matching), PLACING (pending match), COMPLETED (match completed), CANCELLED (match cancelled), TIMEDOUT (match timeouts), FAILED (match failed)
        :type Status: str
        :param _StatusMessage: Matching status descriptions
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StatusMessage: str
        :param _StatusReason: Reason for the matching status
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StatusReason: str
        :param _StartTime: The time when the GPM received the matchmaking request, for example "2020-08-17T08:14:38.077Z".
        :type StartTime: str
        :param _EndTime: The time when the matchmaking request stopped executing due to the completion, failure, timeout, or cancellation, for example "2020-08-17T08:14:38.077Z".
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndTime: str
        """
        self._Id = None
        self._MatchCode = None
        self._MatchResult = None
        self._MatchType = None
        self._Players = None
        self._Status = None
        self._StatusMessage = None
        self._StatusReason = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchResult(self):
        return self._MatchResult

    @MatchResult.setter
    def MatchResult(self, MatchResult):
        self._MatchResult = MatchResult

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def Players(self):
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMessage(self):
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def StatusReason(self):
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

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
        self._Id = params.get("Id")
        self._MatchCode = params.get("MatchCode")
        self._MatchResult = params.get("MatchResult")
        self._MatchType = params.get("MatchType")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._Status = params.get("Status")
        self._StatusMessage = params.get("StatusMessage")
        self._StatusReason = params.get("StatusReason")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchRequest(AbstractModel):
    """ModifyMatch request structure.

    """

    def __init__(self):
        r"""
        :param _MatchName: Match name. It can contain up to 128 bytes, supporting [a-zA-Z0-9-\.]*.
        :type MatchName: str
        :param _RuleCode: RuleCode
        :type RuleCode: str
        :param _Timeout: Timeout period in seconds. Value range: 1 600
        :type Timeout: int
        :param _ServerType: Whether to request server resources for the matchmaking results. 0: no, 1: request GSE resources
        :type ServerType: int
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _MatchDesc: Matchmaking description. Up to 1024 bytes are allowed.
        :type MatchDesc: str
        :param _NotifyUrl: Only HTTP and HTTPS protocols are supported.
        :type NotifyUrl: str
        :param _ServerRegion: Region of the game server queue
        :type ServerRegion: str
        :param _ServerQueue: Game server queue
        :type ServerQueue: str
        :param _CustomPushData: Custom push data
        :type CustomPushData: str
        :param _ServerSessionData: Game server session data
        :type ServerSessionData: str
        :param _GameProperties: Game attribute. It is an array of key-value structure.
        :type GameProperties: list of StringKV
        :param _LogSwitch: Enable or disable the log. 0: disable, 1: enable
        :type LogSwitch: int
        :param _Tags: Tag. It is an array of key-value structure.
        :type Tags: list of StringKV
        """
        self._MatchName = None
        self._RuleCode = None
        self._Timeout = None
        self._ServerType = None
        self._MatchCode = None
        self._MatchDesc = None
        self._NotifyUrl = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._Tags = None

    @property
    def MatchName(self):
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchDesc(self):
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def NotifyUrl(self):
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerRegion(self):
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MatchName = params.get("MatchName")
        self._RuleCode = params.get("RuleCode")
        self._Timeout = params.get("Timeout")
        self._ServerType = params.get("ServerType")
        self._MatchCode = params.get("MatchCode")
        self._MatchDesc = params.get("MatchDesc")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchResponse(AbstractModel):
    """ModifyMatch response structure.

    """

    def __init__(self):
        r"""
        :param _MatchInfo: Matchmaking information
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleCode: RuleCode
        :type RuleCode: str
        :param _RuleName: Rule name. It can only contain numbers, letters, ".", and "-".
        :type RuleName: str
        :param _RuleDesc: Rule description. Up to 1024 bytes are allowed.
        :type RuleDesc: str
        :param _Tags: Tag. It is an array of key-value structure. Up to 50 tags can be associated.
        :type Tags: list of StringKV
        """
        self._RuleCode = None
        self._RuleName = None
        self._RuleDesc = None
        self._Tags = None

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleDesc(self):
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        self._RuleName = params.get("RuleName")
        self._RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleInfo: Rule information
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class ModifyTokenRequest(AbstractModel):
    """ModifyToken request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced. Value range: 0 - 1800. Within the CompatibleSpan time period, user will receive the current and original token in the event notification.
        :type CompatibleSpan: int
        :param _MatchToken: Token. It can contain 0 - 64 characters, supporting [a-zA-Z0-9-_.]. If this parameter is left empty, the token will be randomly generated by GPM.
        :type MatchToken: str
        """
        self._MatchCode = None
        self._CompatibleSpan = None
        self._MatchToken = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def CompatibleSpan(self):
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

    @property
    def MatchToken(self):
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._MatchToken = params.get("MatchToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenResponse(AbstractModel):
    """ModifyToken response structure.

    """

    def __init__(self):
        r"""
        :param _MatchToken: Token that has been set successfully.
        :type MatchToken: str
        :param _CompatibleSpan: The time period during which GPM will continuously push the original token in seconds to the user when the token is replaced.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CompatibleSpan: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchToken = None
        self._CompatibleSpan = None
        self._RequestId = None

    @property
    def MatchToken(self):
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken

    @property
    def CompatibleSpan(self):
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MatchToken = params.get("MatchToken")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._RequestId = params.get("RequestId")


class Player(AbstractModel):
    """Player information

    """

    def __init__(self):
        r"""
        :param _Id: Player ID. It can contain up to 128 characters, supporting [a-zA-Z\d-\._]*.
        :type Id: str
        :param _Name: Player nickname. Up to 128 characters are allowed.
        :type Name: str
        :param _MatchAttributes: Player attribute for matching. Up to 10 attributes are supported.
        :type MatchAttributes: list of MatchAttribute
        :param _Team: Team name. A player can pass in a different team name, which can contain up to 128 characters, and support [a-zA-Z0-9-\.]*.
        :type Team: str
        :param _CustomPlayerStatus: Custom player status. This parameter will be passed through. Value range: [0, 99999]
        :type CustomPlayerStatus: int
        :param _CustomProfile: Custom player information. Up to 1024 characters are allowed. This parameter will be passed through.
        :type CustomProfile: str
        :param _RegionLatencies: Number of delays in each area. Up to 20 delays are supported.
        :type RegionLatencies: list of RegionLatency
        """
        self._Id = None
        self._Name = None
        self._MatchAttributes = None
        self._Team = None
        self._CustomPlayerStatus = None
        self._CustomProfile = None
        self._RegionLatencies = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MatchAttributes(self):
        return self._MatchAttributes

    @MatchAttributes.setter
    def MatchAttributes(self, MatchAttributes):
        self._MatchAttributes = MatchAttributes

    @property
    def Team(self):
        return self._Team

    @Team.setter
    def Team(self, Team):
        self._Team = Team

    @property
    def CustomPlayerStatus(self):
        return self._CustomPlayerStatus

    @CustomPlayerStatus.setter
    def CustomPlayerStatus(self, CustomPlayerStatus):
        self._CustomPlayerStatus = CustomPlayerStatus

    @property
    def CustomProfile(self):
        return self._CustomProfile

    @CustomProfile.setter
    def CustomProfile(self, CustomProfile):
        self._CustomProfile = CustomProfile

    @property
    def RegionLatencies(self):
        return self._RegionLatencies

    @RegionLatencies.setter
    def RegionLatencies(self, RegionLatencies):
        self._RegionLatencies = RegionLatencies


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("MatchAttributes") is not None:
            self._MatchAttributes = []
            for item in params.get("MatchAttributes"):
                obj = MatchAttribute()
                obj._deserialize(item)
                self._MatchAttributes.append(obj)
        self._Team = params.get("Team")
        self._CustomPlayerStatus = params.get("CustomPlayerStatus")
        self._CustomProfile = params.get("CustomProfile")
        if params.get("RegionLatencies") is not None:
            self._RegionLatencies = []
            for item in params.get("RegionLatencies"):
                obj = RegionLatency()
                obj._deserialize(item)
                self._RegionLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionLatency(AbstractModel):
    """The network delay time for players to reach different regions.

    """

    def __init__(self):
        r"""
        :param _Region: Region
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
        :param _Latency: Delay time in ms. Value range: 0 - 999999
        :type Latency: int
        """
        self._Region = None
        self._Latency = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Latency(self):
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportOverviewData(AbstractModel):
    """Matchmaking statistics overview

    """

    def __init__(self):
        r"""
        :param _TotalTimes: Total count
        :type TotalTimes: str
        :param _SuccessPercent: Success rate
        :type SuccessPercent: float
        :param _TimeoutPercent: Timeout rate
        :type TimeoutPercent: float
        :param _FailPercent: Failure rate
        :type FailPercent: float
        :param _AverageSec: Average matching time
        :type AverageSec: float
        """
        self._TotalTimes = None
        self._SuccessPercent = None
        self._TimeoutPercent = None
        self._FailPercent = None
        self._AverageSec = None

    @property
    def TotalTimes(self):
        return self._TotalTimes

    @TotalTimes.setter
    def TotalTimes(self, TotalTimes):
        self._TotalTimes = TotalTimes

    @property
    def SuccessPercent(self):
        return self._SuccessPercent

    @SuccessPercent.setter
    def SuccessPercent(self, SuccessPercent):
        self._SuccessPercent = SuccessPercent

    @property
    def TimeoutPercent(self):
        return self._TimeoutPercent

    @TimeoutPercent.setter
    def TimeoutPercent(self, TimeoutPercent):
        self._TimeoutPercent = TimeoutPercent

    @property
    def FailPercent(self):
        return self._FailPercent

    @FailPercent.setter
    def FailPercent(self, FailPercent):
        self._FailPercent = FailPercent

    @property
    def AverageSec(self):
        return self._AverageSec

    @AverageSec.setter
    def AverageSec(self, AverageSec):
        self._AverageSec = AverageSec


    def _deserialize(self, params):
        self._TotalTimes = params.get("TotalTimes")
        self._SuccessPercent = params.get("SuccessPercent")
        self._TimeoutPercent = params.get("TimeoutPercent")
        self._FailPercent = params.get("FailPercent")
        self._AverageSec = params.get("AverageSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTrendData(AbstractModel):
    """Trend data

    """

    def __init__(self):
        r"""
        :param _TotalList: Total count
        :type TotalList: list of str
        :param _CancelList: Number of requests cancelled
        :type CancelList: list of str
        :param _SuccessList: Number of successes
        :type SuccessList: list of str
        :param _FailList: Number of failures
        :type FailList: list of str
        :param _TimeoutList: Number of request timeout
        :type TimeoutList: list of str
        :param _TimeList: Time array in seconds
        :type TimeList: list of str
        """
        self._TotalList = None
        self._CancelList = None
        self._SuccessList = None
        self._FailList = None
        self._TimeoutList = None
        self._TimeList = None

    @property
    def TotalList(self):
        return self._TotalList

    @TotalList.setter
    def TotalList(self, TotalList):
        self._TotalList = TotalList

    @property
    def CancelList(self):
        return self._CancelList

    @CancelList.setter
    def CancelList(self, CancelList):
        self._CancelList = CancelList

    @property
    def SuccessList(self):
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

    @property
    def FailList(self):
        return self._FailList

    @FailList.setter
    def FailList(self, FailList):
        self._FailList = FailList

    @property
    def TimeoutList(self):
        return self._TimeoutList

    @TimeoutList.setter
    def TimeoutList(self, TimeoutList):
        self._TimeoutList = TimeoutList

    @property
    def TimeList(self):
        return self._TimeList

    @TimeList.setter
    def TimeList(self, TimeList):
        self._TimeList = TimeList


    def _deserialize(self, params):
        self._TotalList = params.get("TotalList")
        self._CancelList = params.get("CancelList")
        self._SuccessList = params.get("SuccessList")
        self._FailList = params.get("FailList")
        self._TimeoutList = params.get("TimeoutList")
        self._TimeList = params.get("TimeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleBriefInfo(AbstractModel):
    """Brief rule information

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name. It supports [a-zA-Z\d-\.]*.
        :type RuleName: str
        :param _MatchCodeList: The associated match
        :type MatchCodeList: list of StringKV
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _RuleCode: RuleCode
        :type RuleCode: str
        """
        self._RuleName = None
        self._MatchCodeList = None
        self._CreateTime = None
        self._RuleCode = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def MatchCodeList(self):
        return self._MatchCodeList

    @MatchCodeList.setter
    def MatchCodeList(self, MatchCodeList):
        self._MatchCodeList = MatchCodeList

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("MatchCodeList") is not None:
            self._MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self._MatchCodeList.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name. It supports [a-zA-Z0-9-\.]*.
        :type RuleName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _RuleDesc: Rule description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleDesc: str
        :param _RuleScript: Rule script
        :type RuleScript: str
        :param _Tags: Tag
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Tags: list of StringKV
        :param _MatchCodeList: The associated match
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MatchCodeList: list of StringKV
        :param _RuleCode: RuleCode
        :type RuleCode: str
        :param _Region: Region
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Region: str
        :param _AppId: User AppId
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AppId: str
        :param _Uin: User UIN
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Uin: str
        :param _CreateUin: User OwnerUin
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateUin: str
        """
        self._RuleName = None
        self._CreateTime = None
        self._RuleDesc = None
        self._RuleScript = None
        self._Tags = None
        self._MatchCodeList = None
        self._RuleCode = None
        self._Region = None
        self._AppId = None
        self._Uin = None
        self._CreateUin = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleDesc(self):
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def RuleScript(self):
        return self._RuleScript

    @RuleScript.setter
    def RuleScript(self, RuleScript):
        self._RuleScript = RuleScript

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MatchCodeList(self):
        return self._MatchCodeList

    @MatchCodeList.setter
    def MatchCodeList(self, MatchCodeList):
        self._MatchCodeList = MatchCodeList

    @property
    def RuleCode(self):
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._CreateTime = params.get("CreateTime")
        self._RuleDesc = params.get("RuleDesc")
        self._RuleScript = params.get("RuleScript")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("MatchCodeList") is not None:
            self._MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self._MatchCodeList.append(obj)
        self._RuleCode = params.get("RuleCode")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CreateUin = params.get("CreateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillRequest(AbstractModel):
    """StartMatchingBackfill request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _Players: Player information
        :type Players: list of Player
        :param _GameServerSessionId: Game server session ID. It should contain 1 to 256 ASCII characters.
        :type GameServerSessionId: str
        :param _MatchTicketId: MatchTicket ID, which can contain 1 to 128 characters. This parameter is left empty by default, and in this case, MatchTicket ID will be automatically generated by GPM.
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._Players = None
        self._GameServerSessionId = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def Players(self):
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def GameServerSessionId(self):
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def MatchTicketId(self):
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillResponse(AbstractModel):
    """StartMatchingBackfill response structure.

    """

    def __init__(self):
        r"""
        :param _MatchTicket: MatchTicket
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MatchTicket = None
        self._RequestId = None

    @property
    def MatchTicket(self):
        return self._MatchTicket

    @MatchTicket.setter
    def MatchTicket(self, MatchTicket):
        self._MatchTicket = MatchTicket

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchTicket") is not None:
            self._MatchTicket = MatchTicket()
            self._MatchTicket._deserialize(params.get("MatchTicket"))
        self._RequestId = params.get("RequestId")


class StartMatchingRequest(AbstractModel):
    """StartMatching request structure.

    """

    def __init__(self):
        r"""
        :param _MatchCode: MatchCode
        :type MatchCode: str
        :param _Players: Player information. Up to 200 entries can be entered.
        :type Players: list of Player
        :param _MatchTicketId: MatchTicket ID, which can contain up to 128 characters and can only contain numbers, letters, “.”, and “-”. This parameter is left empty by default. When it is empty, the MatchTicket ID will be automatically generated by GPM.
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._Players = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def Players(self):
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def MatchTicketId(self):
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingResponse(AbstractModel):
    """StartMatching response structure.

    """

    def __init__(self):
        r"""
        :param _ErrCode: Error code
        :type ErrCode: int
        :param _MatchTicketId: MatchTicket ID. Up to 128 characters are allowed.
        :type MatchTicketId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrCode = None
        self._MatchTicketId = None
        self._RequestId = None

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def MatchTicketId(self):
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrCode = params.get("ErrCode")
        self._MatchTicketId = params.get("MatchTicketId")
        self._RequestId = params.get("RequestId")


class StringKV(AbstractModel):
    """Key-value structure. Both key and value are string types.

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
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
        


class Tag(AbstractModel):
    """Tag key-value pair

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        