# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AlarmLable(AbstractModel):
    r"""Alarming Label

    """

    def __init__(self):
        r"""
        :param _Name: label name
        :type Name: str
        :param _Value: label value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""label name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""label value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotifyHistory(AbstractModel):
    r"""Notification history for each alert

    """

    def __init__(self):
        r"""
        :param _NotifyId: Unique notification ID.
        :type NotifyId: str
        :param _PolicyId: Alert policy ID
        :type PolicyId: str
        :param _SessionId: Alarm cycle iD
        :type SessionId: str
        :param _NotifyTime: Notification time in Unix timestamp (in seconds).
        :type NotifyTime: int
        :param _TriggerTime: Trigger time in Unix timestamp (in seconds).
        :type TriggerTime: int
        :param _TriggerLevel: Alarm severity level. Valid values: None, Note, Warn, and Serious.
        :type TriggerLevel: str
        :param _AlarmContent: alert content
        :type AlarmContent: str
        :param _AlarmObject: Alarm object
        :type AlarmObject: str
        :param _ChannelSet: Alarm notification channel collection involved this time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelSet: list of str
        :param _ChannelsReceivers: Recipient information of the channel
        :type ChannelsReceivers: list of ChannelsReceivers
        :param _PolicyName: Alarm policy name
        :type PolicyName: str
        :param _PromeInstanceID: Prometheus Instance ID, valid only when MT_PROME
        :type PromeInstanceID: str
        :param _PromeInstanceRegion: Region of the Prometheus Instance. Valid at that time only for MT_PROME.
        :type PromeInstanceRegion: str
        :param _Notices: Notification template related configuration information
        :type Notices: list of NotifyRelatedNotice
        :param _TriggerStatus: Alarm trigger status. Valid values: Trigger and Recovery.
        :type TriggerStatus: str
        :param _PromeConsoleURL: Console page address related to the present Prometheus notification history, valid only when MR_PROME
        :type PromeConsoleURL: str
        :param _Labels: Alarm label
        :type Labels: list of AlarmLable
        """
        self._NotifyId = None
        self._PolicyId = None
        self._SessionId = None
        self._NotifyTime = None
        self._TriggerTime = None
        self._TriggerLevel = None
        self._AlarmContent = None
        self._AlarmObject = None
        self._ChannelSet = None
        self._ChannelsReceivers = None
        self._PolicyName = None
        self._PromeInstanceID = None
        self._PromeInstanceRegion = None
        self._Notices = None
        self._TriggerStatus = None
        self._PromeConsoleURL = None
        self._Labels = None

    @property
    def NotifyId(self):
        r"""Unique notification ID.
        :rtype: str
        """
        return self._NotifyId

    @NotifyId.setter
    def NotifyId(self, NotifyId):
        self._NotifyId = NotifyId

    @property
    def PolicyId(self):
        r"""Alert policy ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def SessionId(self):
        r"""Alarm cycle iD
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def NotifyTime(self):
        r"""Notification time in Unix timestamp (in seconds).
        :rtype: int
        """
        return self._NotifyTime

    @NotifyTime.setter
    def NotifyTime(self, NotifyTime):
        self._NotifyTime = NotifyTime

    @property
    def TriggerTime(self):
        r"""Trigger time in Unix timestamp (in seconds).
        :rtype: int
        """
        return self._TriggerTime

    @TriggerTime.setter
    def TriggerTime(self, TriggerTime):
        self._TriggerTime = TriggerTime

    @property
    def TriggerLevel(self):
        r"""Alarm severity level. Valid values: None, Note, Warn, and Serious.
        :rtype: str
        """
        return self._TriggerLevel

    @TriggerLevel.setter
    def TriggerLevel(self, TriggerLevel):
        self._TriggerLevel = TriggerLevel

    @property
    def AlarmContent(self):
        r"""alert content
        :rtype: str
        """
        return self._AlarmContent

    @AlarmContent.setter
    def AlarmContent(self, AlarmContent):
        self._AlarmContent = AlarmContent

    @property
    def AlarmObject(self):
        r"""Alarm object
        :rtype: str
        """
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def ChannelSet(self):
        r"""Alarm notification channel collection involved this time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ChannelSet

    @ChannelSet.setter
    def ChannelSet(self, ChannelSet):
        self._ChannelSet = ChannelSet

    @property
    def ChannelsReceivers(self):
        r"""Recipient information of the channel
        :rtype: list of ChannelsReceivers
        """
        return self._ChannelsReceivers

    @ChannelsReceivers.setter
    def ChannelsReceivers(self, ChannelsReceivers):
        self._ChannelsReceivers = ChannelsReceivers

    @property
    def PolicyName(self):
        r"""Alarm policy name
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PromeInstanceID(self):
        r"""Prometheus Instance ID, valid only when MT_PROME
        :rtype: str
        """
        return self._PromeInstanceID

    @PromeInstanceID.setter
    def PromeInstanceID(self, PromeInstanceID):
        self._PromeInstanceID = PromeInstanceID

    @property
    def PromeInstanceRegion(self):
        r"""Region of the Prometheus Instance. Valid at that time only for MT_PROME.
        :rtype: str
        """
        return self._PromeInstanceRegion

    @PromeInstanceRegion.setter
    def PromeInstanceRegion(self, PromeInstanceRegion):
        self._PromeInstanceRegion = PromeInstanceRegion

    @property
    def Notices(self):
        r"""Notification template related configuration information
        :rtype: list of NotifyRelatedNotice
        """
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def TriggerStatus(self):
        r"""Alarm trigger status. Valid values: Trigger and Recovery.
        :rtype: str
        """
        return self._TriggerStatus

    @TriggerStatus.setter
    def TriggerStatus(self, TriggerStatus):
        self._TriggerStatus = TriggerStatus

    @property
    def PromeConsoleURL(self):
        r"""Console page address related to the present Prometheus notification history, valid only when MR_PROME
        :rtype: str
        """
        return self._PromeConsoleURL

    @PromeConsoleURL.setter
    def PromeConsoleURL(self, PromeConsoleURL):
        self._PromeConsoleURL = PromeConsoleURL

    @property
    def Labels(self):
        r"""Alarm label
        :rtype: list of AlarmLable
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._NotifyId = params.get("NotifyId")
        self._PolicyId = params.get("PolicyId")
        self._SessionId = params.get("SessionId")
        self._NotifyTime = params.get("NotifyTime")
        self._TriggerTime = params.get("TriggerTime")
        self._TriggerLevel = params.get("TriggerLevel")
        self._AlarmContent = params.get("AlarmContent")
        self._AlarmObject = params.get("AlarmObject")
        self._ChannelSet = params.get("ChannelSet")
        if params.get("ChannelsReceivers") is not None:
            self._ChannelsReceivers = []
            for item in params.get("ChannelsReceivers"):
                obj = ChannelsReceivers()
                obj._deserialize(item)
                self._ChannelsReceivers.append(obj)
        self._PolicyName = params.get("PolicyName")
        self._PromeInstanceID = params.get("PromeInstanceID")
        self._PromeInstanceRegion = params.get("PromeInstanceRegion")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = NotifyRelatedNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._TriggerStatus = params.get("TriggerStatus")
        self._PromeConsoleURL = params.get("PromeConsoleURL")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AlarmLable()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelsReceivers(AbstractModel):
    r"""Receiver details

    """

    def __init__(self):
        r"""
        :param _ChannelName: Notification channel name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelName: str
        :param _Receivers: Recipient.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Receivers: list of str
        :param _SendStatus: Sending result. Valid values: 0, (invalid), 1 (successful), 2 (failed), and 3 (no sending required).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SendStatus: str
        """
        self._ChannelName = None
        self._Receivers = None
        self._SendStatus = None

    @property
    def ChannelName(self):
        r"""Notification channel name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        r"""Recipient.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def SendStatus(self):
        r"""Sending result. Valid values: 0, (invalid), 1 (successful), 2 (failed), and 3 (no sending required).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._SendStatus = params.get("SendStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNotifyHistoriesRequest(AbstractModel):
    r"""DescribeAlarmNotifyHistories request structure.

    """

    def __init__(self):
        r"""
        :param _MonitorType: Monitoring type
        :type MonitorType: str
        :param _QueryBaseTime: Start time, used as a Unix timestamp in seconds.
        :type QueryBaseTime: int
        :param _QueryBeforeSeconds: Period to query before QueryBaseTime, in seconds.
        :type QueryBeforeSeconds: int
        :param _PageParams: Pagination parameter.
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        :param _Namespace: Fill in when the monitoring type is MT_QCE. Namespace of the affiliation.
        :type Namespace: str
        :param _ModelName: Fill in when the monitoring type is MT_QCE. Alarm policy type
        :type ModelName: str
        :param _PolicyId: Query the notification history of a policy
        :type PolicyId: str
        """
        self._MonitorType = None
        self._QueryBaseTime = None
        self._QueryBeforeSeconds = None
        self._PageParams = None
        self._Namespace = None
        self._ModelName = None
        self._PolicyId = None

    @property
    def MonitorType(self):
        r"""Monitoring type
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def QueryBaseTime(self):
        r"""Start time, used as a Unix timestamp in seconds.
        :rtype: int
        """
        return self._QueryBaseTime

    @QueryBaseTime.setter
    def QueryBaseTime(self, QueryBaseTime):
        self._QueryBaseTime = QueryBaseTime

    @property
    def QueryBeforeSeconds(self):
        r"""Period to query before QueryBaseTime, in seconds.
        :rtype: int
        """
        return self._QueryBeforeSeconds

    @QueryBeforeSeconds.setter
    def QueryBeforeSeconds(self, QueryBeforeSeconds):
        self._QueryBeforeSeconds = QueryBeforeSeconds

    @property
    def PageParams(self):
        r"""Pagination parameter.
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams

    @property
    def Namespace(self):
        r"""Fill in when the monitoring type is MT_QCE. Namespace of the affiliation.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ModelName(self):
        r"""Fill in when the monitoring type is MT_QCE. Alarm policy type
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PolicyId(self):
        r"""Query the notification history of a policy
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._QueryBaseTime = params.get("QueryBaseTime")
        self._QueryBeforeSeconds = params.get("QueryBeforeSeconds")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNoParams()
            self._PageParams._deserialize(params.get("PageParams"))
        self._Namespace = params.get("Namespace")
        self._ModelName = params.get("ModelName")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNotifyHistoriesResponse(AbstractModel):
    r"""DescribeAlarmNotifyHistories response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyHistoryList: Alarm history
        :type AlarmNotifyHistoryList: list of AlarmNotifyHistory
        :param _PageResult: Pagination condition
        :type PageResult: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmNotifyHistoryList = None
        self._PageResult = None
        self._RequestId = None

    @property
    def AlarmNotifyHistoryList(self):
        r"""Alarm history
        :rtype: list of AlarmNotifyHistory
        """
        return self._AlarmNotifyHistoryList

    @AlarmNotifyHistoryList.setter
    def AlarmNotifyHistoryList(self, AlarmNotifyHistoryList):
        self._AlarmNotifyHistoryList = AlarmNotifyHistoryList

    @property
    def PageResult(self):
        r"""Pagination condition
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoResult`
        """
        return self._PageResult

    @PageResult.setter
    def PageResult(self, PageResult):
        self._PageResult = PageResult

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlarmNotifyHistoryList") is not None:
            self._AlarmNotifyHistoryList = []
            for item in params.get("AlarmNotifyHistoryList"):
                obj = AlarmNotifyHistory()
                obj._deserialize(item)
                self._AlarmNotifyHistoryList.append(obj)
        if params.get("PageResult") is not None:
            self._PageResult = PageByNoResult()
            self._PageResult._deserialize(params.get("PageResult"))
        self._RequestId = params.get("RequestId")


class NotifyRelatedNotice(AbstractModel):
    r"""Notification template information associated with notification history

    """

    def __init__(self):
        r"""
        :param _NoticeId: Notification template ID
        :type NoticeId: str
        :param _NoticeName: Name of the notification template
        :type NoticeName: str
        """
        self._NoticeId = None
        self._NoticeName = None

    @property
    def NoticeId(self):
        r"""Notification template ID
        :rtype: str
        """
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def NoticeName(self):
        r"""Name of the notification template
        :rtype: str
        """
        return self._NoticeName

    @NoticeName.setter
    def NoticeName(self, NoticeName):
        self._NoticeName = NoticeName


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._NoticeName = params.get("NoticeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoParams(AbstractModel):
    r"""Pagination request parameters

    """

    def __init__(self):
        r"""
        :param _PerPage: Number of items per page.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PerPage: int
        :param _PageNo: Page number, starting from 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNo: str
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""Number of items per page.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""Page number, starting from 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoResult(AbstractModel):
    r"""Pagination result parameters

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _TotalPage: Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalPage: int
        :param _CurrentPageNo: Current page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentPageNo: int
        :param _IsEnd: [Deprecated] Whether it has reached the end.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsEnd: bool
        :param _End: Whether it has traversed to the end.
        :type End: bool
        """
        self._TotalCount = None
        self._TotalPage = None
        self._CurrentPageNo = None
        self._IsEnd = None
        self._End = None

    @property
    def TotalCount(self):
        r"""Total data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPage(self):
        r"""Total number of pages.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def CurrentPageNo(self):
        r"""Current page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentPageNo

    @CurrentPageNo.setter
    def CurrentPageNo(self, CurrentPageNo):
        self._CurrentPageNo = CurrentPageNo

    @property
    def IsEnd(self):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        r"""[Deprecated] Whether it has reached the end.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        warnings.warn("parameter `IsEnd` is deprecated", DeprecationWarning) 

        self._IsEnd = IsEnd

    @property
    def End(self):
        r"""Whether it has traversed to the end.
        :rtype: bool
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPage = params.get("TotalPage")
        self._CurrentPageNo = params.get("CurrentPageNo")
        self._IsEnd = params.get("IsEnd")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        