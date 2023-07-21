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


class AddMachineGroupInfoRequest(AbstractModel):
    """AddMachineGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _MachineGroupType: Machine group type
Supported types: `ip` and `label`
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMachineGroupInfoResponse(AbstractModel):
    """AddMachineGroupInfo response structure.

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


class AlarmAnalysisConfig(AbstractModel):
    """Alarm configuration for the multidimensional analysis

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
        


class AlarmInfo(AbstractModel):
    """Alarm policy description

    """

    def __init__(self):
        r"""
        :param _Name: Alarm policy name
        :type Name: str
        :param _AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTargetInfo
        :param _MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: Trigger condition
        :type Condition: str
        :param _TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param _AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param _Status: Enablement status
        :type Status: bool
        :param _AlarmId: Alarm policy ID
        :type AlarmId: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Last update time
        :type UpdateTime: str
        :param _MessageTemplate: Custom notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MessageTemplate: str
        :param _CallBack: Custom callback template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: Multi-Dimensional analysis settings
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Analysis: list of AnalysisDimensional
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Status = None
        self._AlarmId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTargetInfo()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Status = params.get("Status")
        self._AlarmId = params.get("AlarmId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """Alarm notification template type

    """

    def __init__(self):
        r"""
        :param _Name: Alarm notification template name
        :type Name: str
        :param _Type: Alarm template type. Valid values:
<br><li> `Trigger`: alarm triggered
<br><li> `Recovery`: alarm cleared
<br><li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param _NoticeReceivers: Information of the recipient in alarm notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: Callback information of alarm notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebCallbacks: list of WebCallback
        :param _AlarmNoticeId: Alarm notification template ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNoticeId: str
        :param _CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Last update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None
        self._AlarmNoticeId = None
        self._CreateTime = None
        self._UpdateTime = None

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
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTarget(AbstractModel):
    """Monitoring object

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Query: Query statement
        :type Query: str
        :param _Number: Monitoring object number, which is incremental from 1.
        :type Number: int
        :param _StartTimeOffset: Offset of the query start time from the alarm execution time in minutes. The value cannot be positive. Value range: -1440–0.
        :type StartTimeOffset: int
        :param _EndTimeOffset: Offset of the query end time from the alarm execution time in minutes. The value cannot be positive and must be greater than `StartTimeOffset`. Value range: -1440–0.
        :type EndTimeOffset: int
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _SyntaxRule: Search syntax. Valid values:
`0` (default): Lucene; `1`: CQL
For more information, see <a href="https://intl.cloud.tencent.com/document/product/614/47044?from_cn_redirect=1#RetrievesConditionalRules" target="_blank">Search Syntax</a>.
        :type SyntaxRule: int
        """
        self._TopicId = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._LogsetId = None
        self._SyntaxRule = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._LogsetId = params.get("LogsetId")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTargetInfo(AbstractModel):
    """Alarm object

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _LogsetName: Logset name
        :type LogsetName: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _Query: Query statement
        :type Query: str
        :param _Number: Monitoring object number
        :type Number: int
        :param _StartTimeOffset: Offset of the query start time from the alarm execution time in minutes. The value cannot be positive. Value range: -1440–0.
        :type StartTimeOffset: int
        :param _EndTimeOffset: Offset of the query end time from the alarm execution time in minutes. The value cannot be positive and must be greater than `StartTimeOffset`. Value range: -1440–0.
        :type EndTimeOffset: int
        """
        self._LogsetId = None
        self._LogsetName = None
        self._TopicId = None
        self._TopicName = None
        self._Query = None
        self._Number = None
        self._StartTimeOffset = None
        self._EndTimeOffset = None

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
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Query = params.get("Query")
        self._Number = params.get("Number")
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryNotice(AbstractModel):
    """Details about an alarm notification group

    """

    def __init__(self):
        r"""
        :param _Name: Notification group name
        :type Name: str
        :param _AlarmNoticeId: Notification group ID
        :type AlarmNoticeId: str
        """
        self._Name = None
        self._AlarmNoticeId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertHistoryRecord(AbstractModel):
    """Alarm record details

    """

    def __init__(self):
        r"""
        :param _RecordId: Alarm record ID
        :type RecordId: str
        :param _AlarmId: Alarm policy ID
        :type AlarmId: str
        :param _AlarmName: Alarm policy name
        :type AlarmName: str
        :param _TopicId: ID of the monitored object
        :type TopicId: str
        :param _TopicName: Name of the monitored object
        :type TopicName: str
        :param _Region: Region of the monitored object
        :type Region: str
        :param _Trigger: Trigger condition
        :type Trigger: str
        :param _TriggerCount: Number of cycles for which the alarm lasts. An alarm will be triggered only after the trigger condition is met for the number of cycles specified by `TriggerCount`.
        :type TriggerCount: int
        :param _AlarmPeriod: Alarm notification frequency (minutes)
        :type AlarmPeriod: int
        :param _Notices: Notification group
        :type Notices: list of AlertHistoryNotice
        :param _Duration: Alarm duration (minutes)
        :type Duration: int
        :param _Status: Alarm status. Valid values: `0` (uncleared), `1` (cleared), `2` (expired)
        :type Status: int
        :param _CreateTime: Alarm generation time, which is a Unix timestamp in ms
        :type CreateTime: int
        :param _GroupTriggerCondition: Group information corresponding to triggering by group
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupTriggerCondition: list of GroupTriggerConditionInfo
        :param _AlarmLevel: Alarm severity. Valid values: `0` (Warn), `1` (Info), `2` (Critical)
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlarmLevel: int
        :param _MonitorObjectType: Type of the monitored object
`0`: The same object is specified for all statements. `1`: An object is separately specified for each statement. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonitorObjectType: int
        """
        self._RecordId = None
        self._AlarmId = None
        self._AlarmName = None
        self._TopicId = None
        self._TopicName = None
        self._Region = None
        self._Trigger = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._Notices = None
        self._Duration = None
        self._Status = None
        self._CreateTime = None
        self._GroupTriggerCondition = None
        self._AlarmLevel = None
        self._MonitorObjectType = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def AlarmName(self):
        return self._AlarmName

    @AlarmName.setter
    def AlarmName(self, AlarmName):
        self._AlarmName = AlarmName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupTriggerCondition(self):
        return self._GroupTriggerCondition

    @GroupTriggerCondition.setter
    def GroupTriggerCondition(self, GroupTriggerCondition):
        self._GroupTriggerCondition = GroupTriggerCondition

    @property
    def AlarmLevel(self):
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def MonitorObjectType(self):
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._AlarmId = params.get("AlarmId")
        self._AlarmName = params.get("AlarmName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Region = params.get("Region")
        self._Trigger = params.get("Trigger")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlertHistoryNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._Duration = params.get("Duration")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        if params.get("GroupTriggerCondition") is not None:
            self._GroupTriggerCondition = []
            for item in params.get("GroupTriggerCondition"):
                obj = GroupTriggerConditionInfo()
                obj._deserialize(item)
                self._GroupTriggerCondition.append(obj)
        self._AlarmLevel = params.get("AlarmLevel")
        self._MonitorObjectType = params.get("MonitorObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisDimensional(AbstractModel):
    """Multi-Dimensional analysis dimension

    """

    def __init__(self):
        r"""
        :param _Name: Analysis name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Type: Type of data being analyzed. Valid values: `query`, `field`, `original`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Content: Analysis content
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param _ConfigInfo: Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConfigInfo: list of AlarmAnalysisConfig
        """
        self._Name = None
        self._Type = None
        self._Content = None
        self._ConfigInfo = None

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
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ConfigInfo(self):
        return self._ConfigInfo

    @ConfigInfo.setter
    def ConfigInfo(self, ConfigInfo):
        self._ConfigInfo = ConfigInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        if params.get("ConfigInfo") is not None:
            self._ConfigInfo = []
            for item in params.get("ConfigInfo"):
                obj = AlarmAnalysisConfig()
                obj._deserialize(item)
                self._ConfigInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupRequest(AbstractModel):
    """ApplyConfigToMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection configuration ID
        :type ConfigId: str
        :param _GroupId: Machine group ID
        :type GroupId: str
        """
        self._ConfigId = None
        self._GroupId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupResponse(AbstractModel):
    """ApplyConfigToMachineGroup response structure.

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


class CallBackInfo(AbstractModel):
    """Callback configuration

    """

    def __init__(self):
        r"""
        :param _Body: `Body` during callback
        :type Body: str
        :param _Headers: `Headers` during callback
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Headers: list of str
        """
        self._Body = None
        self._Headers = None

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRechargeKafkaServerRequest(AbstractModel):
    """CheckRechargeKafkaServer request structure.

    """

    def __init__(self):
        r"""
        :param _KafkaType: Kafka type. Valid values: 0 (Tencent Cloud CKafka) and 1 (customer's Kafka).
        :type KafkaType: int
        :param _KafkaInstance: CKafka instance ID, which is required when `KafkaType` is set to `0`
        :type KafkaInstance: str
        :param _ServerAddr: Service address
        :type ServerAddr: str
        :param _IsEncryptionAddr: Whether the service address uses an encrypted connection
        :type IsEncryptionAddr: bool
        :param _Protocol: Encryption access protocol, which is required when `IsEncryptionAddr` is set to `true`
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        """
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRechargeKafkaServerResponse(AbstractModel):
    """CheckRechargeKafkaServer response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Kafka cluster accessibility. 0: Accessible.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class Ckafka(AbstractModel):
    """Information of the CKafka instance to ship to

    """

    def __init__(self):
        r"""
        :param _Vip: CKafka VIP
        :type Vip: str
        :param _Vport: CKafka Vport
        :type Vport: str
        :param _InstanceId: CKafka instance ID
        :type InstanceId: str
        :param _InstanceName: CKafka instance name
        :type InstanceName: str
        :param _TopicId: CKafka topic ID
        :type TopicId: str
        :param _TopicName: CKafka topic name
        :type TopicName: str
        """
        self._Vip = None
        self._Vport = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicId = None
        self._TopicName = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerRequest(AbstractModel):
    """CloseKafkaConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _FromTopicId: CLS topic identifier
        :type FromTopicId: str
        """
        self._FromTopicId = None

    @property
    def FromTopicId(self):
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerResponse(AbstractModel):
    """CloseKafkaConsumer response structure.

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


class Column(AbstractModel):
    """Column attribute of log analysis

    """

    def __init__(self):
        r"""
        :param _Name: Column name
        :type Name: str
        :param _Type: Column attribute
        :type Type: str
        """
        self._Name = None
        self._Type = None

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


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressInfo(AbstractModel):
    """Compression configuration of shipped log

    """

    def __init__(self):
        r"""
        :param _Format: Compression format. Valid values: `gzip`; `lzop`; `snappy`; `none` (no compression)
        :type Format: str
        """
        self._Format = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigInfo(AbstractModel):
    """Collection rule configuration information

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection rule configuration ID
        :type ConfigId: str
        :param _Name: Name of the collection rule configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _LogFormat: Log formatting method
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogFormat: str
        :param _Path: Log collection path
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param _LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogType: str
        :param _ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: Collection path blocklist
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: Log topic ID (TopicId) of collection configuration
        :type Output: str
        :param _UpdateTime: Update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UserDefineRule: Custom parsing string
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UserDefineRule: str
        """
        self._ConfigId = None
        self._Name = None
        self._LogFormat = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UpdateTime = None
        self._CreateTime = None
        self._UserDefineRule = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._LogFormat = params.get("LogFormat")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerContent(AbstractModel):
    """Shipping content

    """

    def __init__(self):
        r"""
        :param _EnableTag: Whether to ship tag information
Note: This field may return `null`, indicating that no valid value was found.
        :type EnableTag: bool
        :param _MetaFields: List of metadata to ship. Supported metadata types: \_\_SOURCE\_\_, \_\_FILENAME\_\_, \_\_TIMESTAMP\_\_, \_\_HOSTNAME\_\_, and \_\_PKGID\_\_.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetaFields: list of str
        :param _TagJsonNotTiled: This parameter is required if `EnableTag` is `true`, and is used to specify whether the tag information is JSON tiled. Valid values: `true` (not tiled); `false` (tiled)
Note: This field may return `null`, indicating that no valid value was found.
        :type TagJsonNotTiled: bool
        :param _TimestampAccuracy: Shipping timestamp precision in seconds (default) or milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimestampAccuracy: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._TagJsonNotTiled = None
        self._TimestampAccuracy = None

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagJsonNotTiled(self):
        return self._TagJsonNotTiled

    @TagJsonNotTiled.setter
    def TagJsonNotTiled(self, TagJsonNotTiled):
        self._TagJsonNotTiled = TagJsonNotTiled

    @property
    def TimestampAccuracy(self):
        return self._TimestampAccuracy

    @TimestampAccuracy.setter
    def TimestampAccuracy(self, TimestampAccuracy):
        self._TimestampAccuracy = TimestampAccuracy


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagJsonNotTiled = params.get("TagJsonNotTiled")
        self._TimestampAccuracy = params.get("TimestampAccuracy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentInfo(AbstractModel):
    """Format configuration of shipped log content

    """

    def __init__(self):
        r"""
        :param _Format: Content format. Valid values: `json`, `csv`
        :type Format: str
        :param _Csv: CSV format content description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Csv: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        :param _Json: JSON format content description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Json: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        :param _Parquet: `Parquet` format description
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Parquet: :class:`tencentcloud.cls.v20201016.models.ParquetInfo`
        """
        self._Format = None
        self._Csv = None
        self._Json = None
        self._Parquet = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Csv(self):
        return self._Csv

    @Csv.setter
    def Csv(self, Csv):
        self._Csv = Csv

    @property
    def Json(self):
        return self._Json

    @Json.setter
    def Json(self, Json):
        self._Json = Json

    @property
    def Parquet(self):
        return self._Parquet

    @Parquet.setter
    def Parquet(self, Parquet):
        self._Parquet = Parquet


    def _deserialize(self, params):
        self._Format = params.get("Format")
        if params.get("Csv") is not None:
            self._Csv = CsvInfo()
            self._Csv._deserialize(params.get("Csv"))
        if params.get("Json") is not None:
            self._Json = JsonInfo()
            self._Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self._Parquet = ParquetInfo()
            self._Parquet._deserialize(params.get("Parquet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosRechargeInfo(AbstractModel):
    """COS import configuration information.

    """

    def __init__(self):
        r"""
        :param _Id: COS import configuration ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _TopicId: ID of the log topic.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _LogsetId: ID of the logset.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogsetId: str
        :param _Name: COS import task name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Bucket: COS bucket.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bucket: str
        :param _BucketRegion: Region where the COS bucket is located.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BucketRegion: str
        :param _Prefix: The prefix of the folder where COS files are located.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Prefix: str
        :param _LogType: The type of log collected. `json_log`: JSON logs; `delimiter_log`: separator logs; `minimalist_log`: full text in a single line
Default value: `minimalist_log`
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogType: str
        :param _Status: Status. `0`: Created, `1`: Running, `2`: Stopped, `3`: Completed, `4`: Run failed
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Enable: Whether the configuration is enabled. `0`: Not enabled, `1`: Enabled
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enable: int
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Progress: Progress in percentage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param _Compress: Valid values: "" (default), "gzip", "lzop", "snappy"
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compress: str
        :param _ExtractRuleInfo: See the description of the `ExtractRuleInfo` structure.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        self._Id = None
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Status = None
        self._Enable = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Progress = None
        self._Compress = None
        self._ExtractRuleInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Progress = params.get("Progress")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Notification group name
        :type Name: str
        :param _Type: Notification type. Valid values:
<li> `Trigger`: alarm triggered
<li> `Recovery`: alarm cleared
<li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param _NoticeReceivers: Notification recipient
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: API callback information (including WeCom)
        :type WebCallbacks: list of WebCallback
        """
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None

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
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: Alarm template ID
        :type AlarmNoticeId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmNoticeId = None
        self._RequestId = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._RequestId = params.get("RequestId")


class CreateAlarmRequest(AbstractModel):
    """CreateAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Alarm policy name
        :type Name: str
        :param _AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTarget
        :param _MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: Trigger condition
        :type Condition: str
        :param _TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param _AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param _Status: Whether to enable the alarm policy. Default value: true
        :type Status: bool
        :param _MessageTemplate: Custom alarm content
        :type MessageTemplate: str
        :param _CallBack: Custom callback
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: Multi-Dimensional analysis
        :type Analysis: list of AnalysisDimensional
        """
        self._Name = None
        self._AlarmTargets = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._Status = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        self._Status = params.get("Status")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    """CreateAlarm response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmId: Alarm policy ID.
        :type AlarmId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmId = None
        self._RequestId = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Collection configuration name
        :type Name: str
        :param _Output: Log topic ID (TopicId) of collection configuration
        :type Output: str
        :param _Path: Log collection path containing the filename
        :type Path: str
        :param _LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
        :type LogType: str
        :param _ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: Collection path blocklist
        :type ExcludePaths: list of ExcludePathInfo
        :param _UserDefineRule: Custom collection rule, which is a serialized JSON string
        :type UserDefineRule: str
        :param _AdvancedConfig: Advanced collection configuration
        :type AdvancedConfig: str
        """
        self._Name = None
        self._Output = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._UserDefineRule = None
        self._AdvancedConfig = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule

    @property
    def AdvancedConfig(self):
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Output = params.get("Output")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._UserDefineRule = params.get("UserDefineRule")
        self._AdvancedConfig = params.get("AdvancedConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection configuration ID
        :type ConfigId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigId = None
        self._RequestId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID to bind
        :type TopicId: str
        :param _NeedContent: Whether to ship log metadata. Default value: `true`
        :type NeedContent: bool
        :param _Content: Metadata to ship if `NeedContent` is `true`
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: Compression mode. Valid values: `0` (no compression), `2` (snappy), `3` (LZ4).
        :type Compression: int
        """
        self._TopicId = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer response structure.

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


class CreateCosRechargeRequest(AbstractModel):
    """CreateCosRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: ID of the log topic.
        :type TopicId: str
        :param _LogsetId: ID of the logset.
        :type LogsetId: str
        :param _Name: Shipping task name.
        :type Name: str
        :param _Bucket: COS bucket.
        :type Bucket: str
        :param _BucketRegion: Region where the COS bucket is located.
        :type BucketRegion: str
        :param _Prefix: The prefix of the folder where COS files are located.
        :type Prefix: str
        :param _LogType: The type of log collected. `json_log`: JSON logs; `delimiter_log`: separator logs; `minimalist_log`: full text in a single line
Default value: `minimalist_log`
        :type LogType: str
        :param _Compress: Valid values: "" (default), "gzip", "lzop", "snappy"
        :type Compress: str
        :param _ExtractRuleInfo: Extraction rule. If `ExtractRule` is set, `LogType` must be set.
        :type ExtractRuleInfo: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        """
        self._TopicId = None
        self._LogsetId = None
        self._Name = None
        self._Bucket = None
        self._BucketRegion = None
        self._Prefix = None
        self._LogType = None
        self._Compress = None
        self._ExtractRuleInfo = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def BucketRegion(self):
        return self._BucketRegion

    @BucketRegion.setter
    def BucketRegion(self, BucketRegion):
        self._BucketRegion = BucketRegion

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def ExtractRuleInfo(self):
        return self._ExtractRuleInfo

    @ExtractRuleInfo.setter
    def ExtractRuleInfo(self, ExtractRuleInfo):
        self._ExtractRuleInfo = ExtractRuleInfo


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Name = params.get("Name")
        self._Bucket = params.get("Bucket")
        self._BucketRegion = params.get("BucketRegion")
        self._Prefix = params.get("Prefix")
        self._LogType = params.get("LogType")
        self._Compress = params.get("Compress")
        if params.get("ExtractRuleInfo") is not None:
            self._ExtractRuleInfo = ExtractRuleInfo()
            self._ExtractRuleInfo._deserialize(params.get("ExtractRuleInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosRechargeResponse(AbstractModel):
    """CreateCosRecharge response structure.

    """

    def __init__(self):
        r"""
        :param _Id: cos_recharge record ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateDataTransformRequest(AbstractModel):
    """CreateDataTransform request structure.

    """

    def __init__(self):
        r"""
        :param _FuncType: Task type. Valid values: 1 (specified topic) and 2 (dynamically created).
        :type FuncType: int
        :param _SrcTopicId: Source log topic
        :type SrcTopicId: str
        :param _Name: Data processing task name
        :type Name: str
        :param _EtlContent: Data processing statement
        :type EtlContent: str
        :param _TaskType: Data processing type. Valid values: `1`: Use random data from the source log topic for processing preview. `2`: Use user-defined test data for processing preview. `3`: Create a real processing task.
        :type TaskType: int
        :param _EnableFlag: Task status. Valid values: 1 (enabled) and 2 (disabled).
        :type EnableFlag: int
        :param _DstResources: Target topic ID and alias of the data processing task
        :type DstResources: list of DataTransformResouceInfo
        :param _PreviewLogStatistics: Test data used for previewing the processing result
        :type PreviewLogStatistics: list of PreviewLogStatistic
        """
        self._FuncType = None
        self._SrcTopicId = None
        self._Name = None
        self._EtlContent = None
        self._TaskType = None
        self._EnableFlag = None
        self._DstResources = None
        self._PreviewLogStatistics = None

    @property
    def FuncType(self):
        return self._FuncType

    @FuncType.setter
    def FuncType(self, FuncType):
        self._FuncType = FuncType

    @property
    def SrcTopicId(self):
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def PreviewLogStatistics(self):
        return self._PreviewLogStatistics

    @PreviewLogStatistics.setter
    def PreviewLogStatistics(self, PreviewLogStatistics):
        self._PreviewLogStatistics = PreviewLogStatistics


    def _deserialize(self, params):
        self._FuncType = params.get("FuncType")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._TaskType = params.get("TaskType")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        if params.get("PreviewLogStatistics") is not None:
            self._PreviewLogStatistics = []
            for item in params.get("PreviewLogStatistics"):
                obj = PreviewLogStatistic()
                obj._deserialize(item)
                self._PreviewLogStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataTransformResponse(AbstractModel):
    """CreateDataTransform response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateExportRequest(AbstractModel):
    """CreateExport request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Count: Number of logs to be exported. Maximum value: 50 million
        :type Count: int
        :param _Query: Search statements for log export. <a href="https://intl.cloud.tencent.com/document/product/614/44061?from_cn_redirect=1" target="_blank">[SQL statements]</a> are not supported.
        :type Query: str
        :param _From: Start time of the log to be exported, which is a timestamp in milliseconds
        :type From: int
        :param _To: End time of the log to be exported, which is a timestamp in milliseconds
        :type To: int
        :param _Order: Exported log sorting order by time. Valid values: `asc`: ascending; `desc`: descending. Default value: `desc`
        :type Order: str
        :param _Format: Exported log data format. Valid values: `json`, `csv`. Default value: `json`
        :type Format: str
        """
        self._TopicId = None
        self._Count = None
        self._Query = None
        self._From = None
        self._To = None
        self._Order = None
        self._Format = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Count = params.get("Count")
        self._Query = params.get("Query")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportResponse(AbstractModel):
    """CreateExport response structure.

    """

    def __init__(self):
        r"""
        :param _ExportId: Log export ID.
        :type ExportId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExportId = None
        self._RequestId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        self._RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Rule: Index rule
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _Status: Whether to take effect. Default value: true
        :type Status: bool
        :param _IncludeInternalFields: Whether full-text indexing includes internal fields (`__FILENAME__`, `__HOSTNAME__`, and `__SOURCE__`). Default value: `false`. Recommended value: `true`.
* `false`: Full-text indexing does not include internal fields.
* `true`: Full-text indexing includes internal fields.
        :type IncludeInternalFields: bool
        :param _MetadataFlag: Whether full-text indexing includes metadata fields (which are prefixed with `__TAG__`). Default value: `0`. Recommended value: `1`.
* `0`: Full-text indexing includes only the metadata fields with key-value indexing enabled.
* `1`: Full-text indexing includes all metadata fields.
* `2`: Full-text indexing does not include metadata fields.
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Rule = None
        self._Status = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._Status = params.get("Status")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex response structure.

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


class CreateKafkaRechargeRequest(AbstractModel):
    """CreateKafkaRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Target topic ID
        :type TopicId: str
        :param _Name: Kafka data import configuration name
        :type Name: str
        :param _KafkaType: Kafka type. Valid values: 0 (Tencent Cloud CKafka) and 1 (customer's Kafka).
        :type KafkaType: int
        :param _UserKafkaTopics: List of Kafka topics to import data from. Separate multiple topics with commas (,).
        :type UserKafkaTopics: str
        :param _Offset: Position for data import. Valid values: -2 (earliest, default) and -1 (latest).
        :type Offset: int
        :param _KafkaInstance: CKafka instance ID, which is required when `KafkaType` is set to `0`
        :type KafkaInstance: str
        :param _ServerAddr: Service address, which is required when `KafkaType` is set to `1`
        :type ServerAddr: str
        :param _IsEncryptionAddr: Whether the service address uses an encrypted connection, which is required when `KafkaType` is set to `1`
        :type IsEncryptionAddr: bool
        :param _Protocol: Encryption access protocol, which is required when `IsEncryptionAddr` is set to `true`
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: Kafka consumer group name
        :type ConsumerGroupName: str
        :param _LogRechargeRule: Log import rule
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKafkaRechargeResponse(AbstractModel):
    """CreateKafkaRecharge response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Kafka data import configuration ID
        :type Id: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateLogsetRequest(AbstractModel):
    """CreateLogset request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetName: Logset name, which must be unique
        :type LogsetName: str
        :param _Tags: Tag description list. Up to 10 tag key-value pairs are supported and must be unique.
        :type Tags: list of Tag
        """
        self._LogsetName = None
        self._Tags = None

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetName = params.get("LogsetName")
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
        


class CreateLogsetResponse(AbstractModel):
    """CreateLogset response structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogsetId = None
        self._RequestId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Machine group name, which must be unique
        :type GroupName: str
        :param _MachineGroupType: Type of the machine group to be created. Valid values: `ip`: use the IP string list in `Values` to create a machine group; `label`: use the tag string list in `Values` to create a machine group
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: Tag description list. This parameter is used to bind a tag to a machine group. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key.
        :type Tags: list of Tag
        :param _AutoUpdate: Whether to enable automatic update for the machine group
        :type AutoUpdate: bool
        :param _UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
        :type UpdateStartTime: str
        :param _UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
        :type UpdateEndTime: str
        :param _ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees
        :type ServiceLogging: bool
        :param _MetaTags: Metadata information list of a machine group
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMachineGroupResponse(AbstractModel):
    """CreateMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateShipperRequest(AbstractModel):
    """CreateShipper request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: ID of the log topic to which the shipping rule to be created belongs
        :type TopicId: str
        :param _Bucket: Destination bucket in the shipping rule to be created
        :type Bucket: str
        :param _Prefix: Prefix of the shipping directory in the shipping rule to be created
        :type Prefix: str
        :param _ShipperName: Shipping rule name
        :type ShipperName: str
        :param _Interval: Interval between shipping tasks (in sec). Default value: 300. Value range: 300-900
        :type Interval: int
        :param _MaxSize: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 5-256
        :type MaxSize: int
        :param _FilterRules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: Rules for partitioning logs to be shipped. `strftime` can be used to define the presentation of time format.
        :type Partition: str
        :param _Compress: Compression configuration of shipped log
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: Format configuration of shipped log content
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: Naming a shipping file. Valid values: `0` (by random number); `1` (by shipping time). Default value: `0`.
        :type FilenameMode: int
        :param _StartTime: Start time for data shipping, which cannot be earlier than the lifecycle start time of the log topic. If you do not specify this parameter, it will be set to the time when you create the data shipping task.
        :type StartTime: int
        :param _EndTime: End time for data shipping, which cannot be set to a future time. If you do not specify this parameter, it indicates continuous data shipping.
        :type EndTime: int
        """
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

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
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShipperResponse(AbstractModel):
    """CreateShipper response structure.

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping task ID.
        :type ShipperId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ShipperId = None
        self._RequestId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _PartitionCount: Number of log topic partitions. Default value: 1. Maximum value: 10
        :type PartitionCount: int
        :param _Tags: Tag description list. This parameter is used to bind a tag to a log topic. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key.
        :type Tags: list of Tag
        :param _AutoSplit: Whether to enable automatic split. Default value: true
        :type AutoSplit: bool
        :param _MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled. Default value: 50
        :type MaxSplitPartitions: int
        :param _StorageType: Log topic storage type. Valid values: `hot` (STANDARD storage); `cold` (IA storage). Default value: `hot`.
        :type StorageType: str
        :param _Period: Lifecycle in days. Value range: 1–3600 (STANDARD storage); 7–3600 (IA storage). `3640` indicates permanent retention.
        :type Period: int
        :param _Describes: Log topic description
        :type Describes: str
        :param _HotPeriod: `0`: Disable log transitioning.
A value other than `0`: The number of STANDARD storage days after log transitioning is enabled (valid only if `StorageType` is `hot`). Note: `HotPeriod` should be greater than or equal to `7` and less than `Period`.
        :type HotPeriod: int
        :param _IsWebTracking: Whether to enable web tracking. Valid values: `false` (disable); `true` (enable)
        :type IsWebTracking: bool
        """
        self._LogsetId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._IsWebTracking = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def IsWebTracking(self):
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._IsWebTracking = params.get("IsWebTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CsvInfo(AbstractModel):
    """CSV content description

    """

    def __init__(self):
        r"""
        :param _PrintKey: Whether to print `key` on the first row of the CSV file
        :type PrintKey: bool
        :param _Keys: Names of keys
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Keys: list of str
        :param _Delimiter: Field delimiter
        :type Delimiter: str
        :param _EscapeChar: Escape character used to enclose any field delimiter in field content. You can enter only a single quotation mark, double quotation mark, or an empty string.
        :type EscapeChar: str
        :param _NonExistingField: Content used to populate non-existing fields
        :type NonExistingField: str
        """
        self._PrintKey = None
        self._Keys = None
        self._Delimiter = None
        self._EscapeChar = None
        self._NonExistingField = None

    @property
    def PrintKey(self):
        return self._PrintKey

    @PrintKey.setter
    def PrintKey(self, PrintKey):
        self._PrintKey = PrintKey

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def EscapeChar(self):
        return self._EscapeChar

    @EscapeChar.setter
    def EscapeChar(self, EscapeChar):
        self._EscapeChar = EscapeChar

    @property
    def NonExistingField(self):
        return self._NonExistingField

    @NonExistingField.setter
    def NonExistingField(self, NonExistingField):
        self._NonExistingField = NonExistingField


    def _deserialize(self, params):
        self._PrintKey = params.get("PrintKey")
        self._Keys = params.get("Keys")
        self._Delimiter = params.get("Delimiter")
        self._EscapeChar = params.get("EscapeChar")
        self._NonExistingField = params.get("NonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformResouceInfo(AbstractModel):
    """Information about the resource for data processing

    """

    def __init__(self):
        r"""
        :param _TopicId: Target topic ID
        :type TopicId: str
        :param _Alias: Alias
        :type Alias: str
        """
        self._TopicId = None
        self._Alias = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTransformTaskInfo(AbstractModel):
    """Basic information of a data processing task

    """

    def __init__(self):
        r"""
        :param _Name: Data processing task name
        :type Name: str
        :param _TaskId: Data processing task ID
        :type TaskId: str
        :param _EnableFlag: Task status. Valid values: 1 (enabled) and 2 (disabled).
        :type EnableFlag: int
        :param _Type: Task type. Valid values: 1 (DSL) and 2 (SQL).
        :type Type: int
        :param _SrcTopicId: Source log topic
        :type SrcTopicId: str
        :param _Status: Current task status. Valid values: 1 (preparing), 2 (in progress), 3 (being stopped), and 4 (stopped).
        :type Status: int
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _UpdateTime: Last modified time
        :type UpdateTime: str
        :param _LastEnableTime: Last enabled time. If you need to rebuild a cluster, modify this time.
        :type LastEnableTime: str
        :param _SrcTopicName: Log topic name
        :type SrcTopicName: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _DstResources: Target topic ID and alias of the data processing task
        :type DstResources: list of DataTransformResouceInfo
        :param _EtlContent: Logical function for data processing
        :type EtlContent: str
        """
        self._Name = None
        self._TaskId = None
        self._EnableFlag = None
        self._Type = None
        self._SrcTopicId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LastEnableTime = None
        self._SrcTopicName = None
        self._LogsetId = None
        self._DstResources = None
        self._EtlContent = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SrcTopicId(self):
        return self._SrcTopicId

    @SrcTopicId.setter
    def SrcTopicId(self, SrcTopicId):
        self._SrcTopicId = SrcTopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastEnableTime(self):
        return self._LastEnableTime

    @LastEnableTime.setter
    def LastEnableTime(self, LastEnableTime):
        self._LastEnableTime = LastEnableTime

    @property
    def SrcTopicName(self):
        return self._SrcTopicName

    @SrcTopicName.setter
    def SrcTopicName(self, SrcTopicName):
        self._SrcTopicName = SrcTopicName

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._EnableFlag = params.get("EnableFlag")
        self._Type = params.get("Type")
        self._SrcTopicId = params.get("SrcTopicId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastEnableTime = params.get("LastEnableTime")
        self._SrcTopicName = params.get("SrcTopicName")
        self._LogsetId = params.get("LogsetId")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        self._EtlContent = params.get("EtlContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: Notification group ID
        :type AlarmNoticeId: str
        """
        self._AlarmNoticeId = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeResponse(AbstractModel):
    """DeleteAlarmNotice response structure.

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


class DeleteAlarmRequest(AbstractModel):
    """DeleteAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _AlarmId: Alarm policy ID.
        :type AlarmId: str
        """
        self._AlarmId = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    """DeleteAlarm response structure.

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


class DeleteConfigFromMachineGroupRequest(AbstractModel):
    """DeleteConfigFromMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _ConfigId: Collection configuration ID
        :type ConfigId: str
        """
        self._GroupId = None
        self._ConfigId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFromMachineGroupResponse(AbstractModel):
    """DeleteConfigFromMachineGroup response structure.

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


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection rule configuration ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig response structure.

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


class DeleteConsumerRequest(AbstractModel):
    """DeleteConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID bound to the task
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerResponse(AbstractModel):
    """DeleteConsumer response structure.

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


class DeleteDataTransformRequest(AbstractModel):
    """DeleteDataTransform request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Data processing task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDataTransformResponse(AbstractModel):
    """DeleteDataTransform response structure.

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


class DeleteExportRequest(AbstractModel):
    """DeleteExport request structure.

    """

    def __init__(self):
        r"""
        :param _ExportId: Log export ID
        :type ExportId: str
        """
        self._ExportId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExportResponse(AbstractModel):
    """DeleteExport response structure.

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


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex response structure.

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


class DeleteKafkaRechargeRequest(AbstractModel):
    """DeleteKafkaRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Kafka data import configuration ID
        :type Id: str
        :param _TopicId: Target CLS log topic ID
        :type TopicId: str
        """
        self._Id = None
        self._TopicId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKafkaRechargeResponse(AbstractModel):
    """DeleteKafkaRecharge response structure.

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


class DeleteLogsetRequest(AbstractModel):
    """DeleteLogset request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        """
        self._LogsetId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogsetResponse(AbstractModel):
    """DeleteLogset response structure.

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


class DeleteMachineGroupInfoRequest(AbstractModel):
    """DeleteMachineGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _MachineGroupType: Machine group type
Supported types: `ip` and `label`
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        """
        self._GroupId = None
        self._MachineGroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupInfoResponse(AbstractModel):
    """DeleteMachineGroupInfo response structure.

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


class DeleteMachineGroupRequest(AbstractModel):
    """DeleteMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupResponse(AbstractModel):
    """DeleteMachineGroup response structure.

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


class DeleteShipperRequest(AbstractModel):
    """DeleteShipper request structure.

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping rule ID
        :type ShipperId: str
        """
        self._ShipperId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShipperResponse(AbstractModel):
    """DeleteShipper response structure.

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


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

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


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <li> name
Filter by **notification group name**.
Type: String
Required: No
<li> alarmNoticeId
Filter by **notification group ID**.
Type: String
Required: No
<li> uid
Filter by **recipient ID**.
Type: String
Required: No
<li> groupId
Filter by **recipient ID**.
Type: String
Required: No

Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNotices: Alarm notification template list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotices: list of AlarmNotice
        :param _TotalCount: Total number of eligible alarm notification templates
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmNotices = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AlarmNotices(self):
        return self._AlarmNotices

    @AlarmNotices.setter
    def AlarmNotices(self, AlarmNotices):
        self._AlarmNotices = AlarmNotices

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
        if params.get("AlarmNotices") is not None:
            self._AlarmNotices = []
            for item in params.get("AlarmNotices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._AlarmNotices.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: name
- Filter by **alarm policy name**
- Type: String
- Required: No

alarmId
- Filter by **alarm policy ID**
- Type: String
- Required: No

topicId
- Filter by **log topic ID**
- Type: String
- Required: No

enable
- Filter by **enablement status**
- Type: String
- Note: The valid values of `enable` include `1`, `t`, `T`, `TRUE`, `true`, `True`, `0`, `f`, `F`, `FALSE`, `false`, and `False`. If other values are entered, an "invalid parameter" error will be returned.
- Required: No

Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms response structure.

    """

    def __init__(self):
        r"""
        :param _Alarms: Alarm policy list
        :type Alarms: list of AlarmInfo
        :param _TotalCount: Number of eligible alarm policies
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Alarms = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

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
        if params.get("Alarms") is not None:
            self._Alarms = []
            for item in params.get("Alarms"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAlertRecordHistoryRequest(AbstractModel):
    """DescribeAlertRecordHistory request structure.

    """

    def __init__(self):
        r"""
        :param _From: Start time of the query range, which is a Unix timestamp in ms
        :type From: int
        :param _To: End time of the query range, which is a Unix timestamp in ms
        :type To: int
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Maximum value: 100
        :type Limit: int
        :param _Filters: - alertId: Filter by alarm policy ID. Type: String; optional
- topicId: Filter by ID of monitored object. Type: String; optional
- status: Filter by alarm status. Type: String, optional. Valid values: `0` (uncleared), `1` (cleared), `2` (expired)
- alarmLevel: Filter by alarm severity. Type: String, optional. Valid values: `0` (Warn), `1` (Info), `2` (Critical)

Each request can have up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        """
        self._From = None
        self._To = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRecordHistoryResponse(AbstractModel):
    """DescribeAlertRecordHistory response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total alarm records
        :type TotalCount: int
        :param _Records: Alarm record details
        :type Records: list of AlertHistoryRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Records = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = AlertHistoryRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigMachineGroupsRequest(AbstractModel):
    """DescribeConfigMachineGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection configuration ID
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMachineGroupsResponse(AbstractModel):
    """DescribeConfigMachineGroups response structure.

    """

    def __init__(self):
        r"""
        :param _MachineGroups: List of machine groups bound to the collection rule configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MachineGroups: list of MachineGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MachineGroups = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: configName
- Filter by fuzzy match of **collection configuration name**
- Type: String
- Required: No

configId
- Filter by **collection configuration ID**
- Type: String
- Required: No

topicId
- Filter by **log topic**
- Type: String
- Required: No

Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _Configs: Collection configuration list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Configs: list of ConfigInfo
        :param _TotalCount: Total number of filtered items
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Configs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

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
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConsumerRequest(AbstractModel):
    """DescribeConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID bound to the task
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerResponse(AbstractModel):
    """DescribeConsumer response structure.

    """

    def __init__(self):
        r"""
        :param _Effective: Whether the shipping task is effective
        :type Effective: bool
        :param _NeedContent: Whether log metadata is shipped
        :type NeedContent: bool
        :param _Content: Metadata shipped if `NeedContent` is `true`
Note: This field may return `null`, indicating that no valid value was found.
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: Compression mode. Valid values: `0` (no compression), `2` (snappy), `3` (LZ4).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None
        self._RequestId = None

    @property
    def Effective(self):
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        self._RequestId = params.get("RequestId")


class DescribeCosRechargesRequest(AbstractModel):
    """DescribeCosRecharges request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: ID of the log topic.
        :type TopicId: str
        :param _Status: Status. `0`: Created, `1`: Running, `2`: Stopped, `3`: Completed, `4`: Run failed
        :type Status: int
        :param _Enable: Whether the configuration is enabled. `0`: Not enabled, `1`: Enabled
        :type Enable: int
        """
        self._TopicId = None
        self._Status = None
        self._Enable = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosRechargesResponse(AbstractModel):
    """DescribeCosRecharges response structure.

    """

    def __init__(self):
        r"""
        :param _Data: See the description of the `CosRechargeInfo` structure.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of CosRechargeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CosRechargeInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataTransformInfoRequest(AbstractModel):
    """DescribeDataTransformInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <br><li>taskName

Filter by **processing task name**.
Type: String

Required: No

<br><li>taskId

Filter by **processing task ID**.
Type: String

Required: No

<br><li>srctopicId

Filter by **source topic ID**.
Type: String

Required: No

Each request can have up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: The pagination offset. Default value: 0.
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Type: Task type. Valid values: 1: Get the details of a single task. 2 (default): Get the task list.
        :type Type: int
        :param _TaskId: Task ID, which is required when `Type` is set to `1`
        :type TaskId: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Type = None
        self._TaskId = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Type = params.get("Type")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataTransformInfoResponse(AbstractModel):
    """DescribeDataTransformInfo response structure.

    """

    def __init__(self):
        r"""
        :param _DataTransformTaskInfos: List of data processing tasks
        :type DataTransformTaskInfos: list of DataTransformTaskInfo
        :param _TotalCount: Total tasks
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataTransformTaskInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DataTransformTaskInfos(self):
        return self._DataTransformTaskInfos

    @DataTransformTaskInfos.setter
    def DataTransformTaskInfos(self, DataTransformTaskInfos):
        self._DataTransformTaskInfos = DataTransformTaskInfos

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
        if params.get("DataTransformTaskInfos") is not None:
            self._DataTransformTaskInfos = []
            for item in params.get("DataTransformTaskInfos"):
                obj = DataTransformTaskInfo()
                obj._deserialize(item)
                self._DataTransformTaskInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._TopicId = None
        self._Offset = None
        self._Limit = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

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
        self._TopicId = params.get("TopicId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportsResponse(AbstractModel):
    """DescribeExports response structure.

    """

    def __init__(self):
        r"""
        :param _Exports: List of exported logs
        :type Exports: list of ExportInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Exports = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Exports(self):
        return self._Exports

    @Exports.setter
    def Exports(self, Exports):
        self._Exports = Exports

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
        if params.get("Exports") is not None:
            self._Exports = []
            for item in params.get("Exports"):
                obj = ExportInfo()
                obj._deserialize(item)
                self._Exports.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIndexRequest(AbstractModel):
    """DescribeIndex request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexResponse(AbstractModel):
    """DescribeIndex response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Status: Whether it takes effect
        :type Status: bool
        :param _Rule: Index configuration information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _ModifyTime: Index modification time. The default value is the index creation time.
        :type ModifyTime: str
        :param _IncludeInternalFields: Whether full-text indexing includes internal fields (`__FILENAME__`, `__HOSTNAME__`, and `__SOURCE__`)
* `false`: Full-text indexing does not include internal fields.
* `true`: Full-text indexing includes internal fields.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeInternalFields: bool
        :param _MetadataFlag: Whether full-text indexing includes metadata fields (which are prefixed with `__TAG__`)
* `0`: Full-text indexing includes only the metadata fields with key-value indexing enabled.
* `1`: Full-text indexing includes all metadata fields.
* `2`: Full-text indexing does not include metadata fields.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetadataFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._ModifyTime = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._ModifyTime = params.get("ModifyTime")
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        self._RequestId = params.get("RequestId")


class DescribeKafkaRechargesRequest(AbstractModel):
    """DescribeKafkaRecharges request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Id: Import configuration ID
        :type Id: str
        :param _Status: Status. Valid values: 1 (running) and 2 (suspended).
        :type Status: int
        """
        self._TopicId = None
        self._Id = None
        self._Status = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKafkaRechargesResponse(AbstractModel):
    """DescribeKafkaRecharges response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: KafkaRechargeInfo list
        :type Infos: list of KafkaRechargeInfo
        :param _TotalCount: Total Kafka data records imported
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = KafkaRechargeInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLogContextRequest(AbstractModel):
    """DescribeLogContext request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID to be queried
        :type TopicId: str
        :param _BTime: Log time in the format of YYYY-mm-dd HH:MM:SS.FFF
        :type BTime: str
        :param _PkgId: Log package number
        :type PkgId: str
        :param _PkgLogId: Log number in log package
        :type PkgLogId: int
        :param _PrevLogs: Number of previous logs. Default value: 10
        :type PrevLogs: int
        :param _NextLogs: Number of next logs. Default value: 10
        :type NextLogs: int
        """
        self._TopicId = None
        self._BTime = None
        self._PkgId = None
        self._PkgLogId = None
        self._PrevLogs = None
        self._NextLogs = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def PrevLogs(self):
        return self._PrevLogs

    @PrevLogs.setter
    def PrevLogs(self, PrevLogs):
        self._PrevLogs = PrevLogs

    @property
    def NextLogs(self):
        return self._NextLogs

    @NextLogs.setter
    def NextLogs(self, NextLogs):
        self._NextLogs = NextLogs


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._BTime = params.get("BTime")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._PrevLogs = params.get("PrevLogs")
        self._NextLogs = params.get("NextLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogContextResponse(AbstractModel):
    """DescribeLogContext response structure.

    """

    def __init__(self):
        r"""
        :param _LogContextInfos: Log context information set
        :type LogContextInfos: list of LogContextInfo
        :param _PrevOver: Whether the previous logs have been returned
        :type PrevOver: bool
        :param _NextOver: Whether the next logs have been returned
        :type NextOver: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogContextInfos = None
        self._PrevOver = None
        self._NextOver = None
        self._RequestId = None

    @property
    def LogContextInfos(self):
        return self._LogContextInfos

    @LogContextInfos.setter
    def LogContextInfos(self, LogContextInfos):
        self._LogContextInfos = LogContextInfos

    @property
    def PrevOver(self):
        return self._PrevOver

    @PrevOver.setter
    def PrevOver(self, PrevOver):
        self._PrevOver = PrevOver

    @property
    def NextOver(self):
        return self._NextOver

    @NextOver.setter
    def NextOver(self, NextOver):
        self._NextOver = NextOver

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LogContextInfos") is not None:
            self._LogContextInfos = []
            for item in params.get("LogContextInfos"):
                obj = LogContextInfo()
                obj._deserialize(item)
                self._LogContextInfos.append(obj)
        self._PrevOver = params.get("PrevOver")
        self._NextOver = params.get("NextOver")
        self._RequestId = params.get("RequestId")


class DescribeLogHistogramRequest(AbstractModel):
    """DescribeLogHistogram request structure.

    """

    def __init__(self):
        r"""
        :param _From: Start time of the log to be queried, which is a Unix timestamp in milliseconds
        :type From: int
        :param _To: End time of the log to be queried, which is a Unix timestamp in milliseconds
        :type To: int
        :param _Query: Query statement
        :type Query: str
        :param _TopicId: ID of the log topic to be queried
        :type TopicId: str
        :param _Interval: Interval in milliseconds. Condition: (To – From) / Interval ≤ 200
        :type Interval: int
        :param _SyntaxRule: Search syntax. Valid values:
`0` (default): Lucene; `1`: CQL
For more information, see <a href="https://intl.cloud.tencent.com/document/product/614/47044?from_cn_redirect=1#RetrievesConditionalRules" target="_blank">Search Syntax</a>.
        :type SyntaxRule: int
        """
        self._From = None
        self._To = None
        self._Query = None
        self._TopicId = None
        self._Interval = None
        self._SyntaxRule = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Interval = params.get("Interval")
        self._SyntaxRule = params.get("SyntaxRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogHistogramResponse(AbstractModel):
    """DescribeLogHistogram response structure.

    """

    def __init__(self):
        r"""
        :param _Interval: Statistical period in milliseconds
        :type Interval: int
        :param _TotalCount: The number of logs that hit the keywords
        :type TotalCount: int
        :param _HistogramInfos: Statistical result details within the period
        :type HistogramInfos: list of HistogramInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Interval = None
        self._TotalCount = None
        self._HistogramInfos = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistogramInfos(self):
        return self._HistogramInfos

    @HistogramInfos.setter
    def HistogramInfos(self, HistogramInfos):
        self._HistogramInfos = HistogramInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._TotalCount = params.get("TotalCount")
        if params.get("HistogramInfos") is not None:
            self._HistogramInfos = []
            for item in params.get("HistogramInfos"):
                obj = HistogramInfo()
                obj._deserialize(item)
                self._HistogramInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogsetsRequest(AbstractModel):
    """DescribeLogsets request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: logsetName
- Filter by **logset name**
- Type: String
- Required: No

logsetId
- Filter by **logset ID**
- Type: String
- Required: No

tagKey
- Filter by **tag key**
- Type: String
- Required: No

tag:tagKey
- Filter by **tag key-value pair**. The `tagKey` should be replaced with a specified tag key.
- Type: String
- Required: No

Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogsetsResponse(AbstractModel):
    """DescribeLogsets response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of pages
        :type TotalCount: int
        :param _Logsets: Logset list
        :type Logsets: list of LogsetInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Logsets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Logsets(self):
        return self._Logsets

    @Logsets.setter
    def Logsets(self, Logsets):
        self._Logsets = Logsets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Logsets") is not None:
            self._Logsets = []
            for item in params.get("Logsets"):
                obj = LogsetInfo()
                obj._deserialize(item)
                self._Logsets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupConfigsRequest(AbstractModel):
    """DescribeMachineGroupConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupConfigsResponse(AbstractModel):
    """DescribeMachineGroupConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _Configs: Collection rule configuration list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Configs: list of ConfigInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Configs = None
        self._RequestId = None

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: machineGroupName
- Filter by **machine group name**
- Type: String
- Required: No

machineGroupId
- Filter by **machine group ID**
- Type: String
- Required: No

tagKey
- Filter by **tag key**
- Type: String
- Required: No

tag:tagKey
- Filter by **tag key-value pair**. The `tagKey` should be replaced with a specified tag key.
- Type: String
- Required: No

Each request can have up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupsResponse(AbstractModel):
    """DescribeMachineGroups response structure.

    """

    def __init__(self):
        r"""
        :param _MachineGroups: Machine group information list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MachineGroups: list of MachineGroupInfo
        :param _TotalCount: Total number of pages
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MachineGroups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MachineGroups(self):
        return self._MachineGroups

    @MachineGroups.setter
    def MachineGroups(self, MachineGroups):
        self._MachineGroups = MachineGroups

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
        if params.get("MachineGroups") is not None:
            self._MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self._MachineGroups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the machine group to be queried
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines response structure.

    """

    def __init__(self):
        r"""
        :param _Machines: Group of machine status information
        :type Machines: list of MachineInfo
        :param _AutoUpdate: Whether to enable the automatic update feature for the machine group
        :type AutoUpdate: int
        :param _UpdateStartTime: Preset start time of automatic update of machine group
        :type UpdateStartTime: str
        :param _UpdateEndTime: Preset end time of automatic update of machine group
        :type UpdateEndTime: str
        :param _LatestAgentVersion: Latest LogListener version available to the current user
        :type LatestAgentVersion: str
        :param _ServiceLogging: Whether to enable the service log
        :type ServiceLogging: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Machines = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._LatestAgentVersion = None
        self._ServiceLogging = None
        self._RequestId = None

    @property
    def Machines(self):
        return self._Machines

    @Machines.setter
    def Machines(self, Machines):
        self._Machines = Machines

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def LatestAgentVersion(self):
        return self._LatestAgentVersion

    @LatestAgentVersion.setter
    def LatestAgentVersion(self, LatestAgentVersion):
        self._LatestAgentVersion = LatestAgentVersion

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self._Machines = []
            for item in params.get("Machines"):
                obj = MachineInfo()
                obj._deserialize(item)
                self._Machines.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._LatestAgentVersion = params.get("LatestAgentVersion")
        self._ServiceLogging = params.get("ServiceLogging")
        self._RequestId = params.get("RequestId")


class DescribePartitionsRequest(AbstractModel):
    """DescribePartitions request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePartitionsResponse(AbstractModel):
    """DescribePartitions response structure.

    """

    def __init__(self):
        r"""
        :param _Partitions: Partition list
        :type Partitions: list of PartitionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShipperTasksRequest(AbstractModel):
    """DescribeShipperTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping rule ID
        :type ShipperId: str
        :param _StartTime: Query start timestamp in milliseconds, which can be within the last three days
        :type StartTime: int
        :param _EndTime: Query end timestamp in milliseconds
        :type EndTime: int
        """
        self._ShipperId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

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
        self._ShipperId = params.get("ShipperId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShipperTasksResponse(AbstractModel):
    """DescribeShipperTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: Shipping task list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tasks: list of ShipperTaskInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ShipperTaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShippersRequest(AbstractModel):
    """DescribeShippers request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: - shipperName: Filter by **shipping rule name**. Type: String. Required: No.
- shipperId: Filter by **shipping rule ID**. Type: String. Required: No.
- topicId: Filter by **log topic**. Type: String. Required: No.

Each request can have up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShippersResponse(AbstractModel):
    """DescribeShippers response structure.

    """

    def __init__(self):
        r"""
        :param _Shippers: Shipping rule list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Shippers: list of ShipperInfo
        :param _TotalCount: Total number of results obtained in this query
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Shippers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Shippers(self):
        return self._Shippers

    @Shippers.setter
    def Shippers(self, Shippers):
        self._Shippers = Shippers

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
        if params.get("Shippers") is not None:
            self._Shippers = []
            for item in params.get("Shippers"):
                obj = ShipperInfo()
                obj._deserialize(item)
                self._Shippers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <li>topicName: Filter by **log topic name**. Fuzzy match is implemented by default. You can use the `PreciseSearch` parameter to set exact match. Type: String. Required. No. <br><li>logsetName: Filter by **logset name**. Fuzzy match is implemented by default. You can use the `PreciseSearch` parameter to set exact match. Type: String. Required: No. <br><li>topicId: Filter by **log topic ID**. Type: String. Required: No. <br><li>logsetId: Filter by **logset ID**. You can call `DescribeLogsets` to query the list of created logsets or log in to the console to view them. You can also call `CreateLogset` to create a logset. Type: String. Required: No. <br><li>tagKey: Filter by **tag key**. Type: String. Required: No. <br><li>tag:tagKey: Filter by **tag key-value pair**. The `tagKey` should be replaced with a specified tag key, such as `tag:exampleKey`. Type: String. Required: No. <br><li>storageType: Filter by **log topic storage type**. Valid values: `hot` (standard storage) and `cold` (IA storage). Type: String. Required: No. Each request can have up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        :param _Offset: Page offset. Default value: 0.
        :type Offset: int
        :param _Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _PreciseSearch: Match mode for `Filters` fields.
- 0: Fuzzy match for `topicName` and `logsetName`. This is the default value.
- 1: Exact match for `topicName`.
- 2: Exact match for `logsetName`.
- 3: Exact match for `topicName` and `logsetName`.
        :type PreciseSearch: int
        :param _BizType: Topic type
- 0 (default): Log topic.
- 1: Metric topic.

        :type BizType: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._PreciseSearch = None
        self._BizType = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def PreciseSearch(self):
        return self._PreciseSearch

    @PreciseSearch.setter
    def PreciseSearch(self, PreciseSearch):
        self._PreciseSearch = PreciseSearch

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PreciseSearch = params.get("PreciseSearch")
        self._BizType = params.get("BizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics response structure.

    """

    def __init__(self):
        r"""
        :param _Topics: Log topic list
        :type Topics: list of TopicInfo
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Topics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DynamicIndex(AbstractModel):
    """Dynamic index configuration

    Note: This feature is currently in a beta test. To use it, please contact technical support.

    """

    def __init__(self):
        r"""
        :param _Status: Dynamic index configuration status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExcludePathInfo(AbstractModel):
    """Blocklist path information

    """

    def __init__(self):
        r"""
        :param _Type: Type. Valid values: `File`, `Path`
        :type Type: str
        :param _Value: Specific content corresponding to `Type`
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInfo(AbstractModel):
    """Log export information

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _ExportId: Log export task ID
        :type ExportId: str
        :param _Query: Log export query statement
        :type Query: str
        :param _FileName: Log export filename
        :type FileName: str
        :param _FileSize: Log file size
        :type FileSize: int
        :param _Order: Log export time sorting
        :type Order: str
        :param _Format: Log export format
        :type Format: str
        :param _Count: Number of logs to be exported
        :type Count: int
        :param _Status: Log download status. Valid values: `Processing`, `Completed`, `Failed`, `Expired` (three-day validity period), and `Queuing`.
        :type Status: str
        :param _From: Log export start time
        :type From: int
        :param _To: Log export end time
        :type To: int
        :param _CosPath: Log export path
        :type CosPath: str
        :param _CreateTime: Log export creation time
        :type CreateTime: str
        """
        self._TopicId = None
        self._ExportId = None
        self._Query = None
        self._FileName = None
        self._FileSize = None
        self._Order = None
        self._Format = None
        self._Count = None
        self._Status = None
        self._From = None
        self._To = None
        self._CosPath = None
        self._CreateTime = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def CosPath(self):
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ExportId = params.get("ExportId")
        self._Query = params.get("Query")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._From = params.get("From")
        self._To = params.get("To")
        self._CosPath = params.get("CosPath")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractRuleInfo(AbstractModel):
    """Log extraction rule

    """

    def __init__(self):
        r"""
        :param _TimeKey: Time field key name. `time_key` and `time_format` must appear in pairs
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeKey: str
        :param _TimeFormat: Time field format. For more information, please see the output parameters of the time format description of the `strftime` function in C language
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeFormat: str
        :param _Delimiter: Delimiter for delimited log, which is valid only if `log_type` is `delimiter_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Delimiter: str
        :param _LogRegex: Full log matching rule, which is valid only if `log_type` is `fullregex_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogRegex: str
        :param _BeginRegex: First-Line matching rule, which is valid only if `log_type` is `multiline_log` or `fullregex_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BeginRegex: str
        :param _Keys: Key name of each extracted field. An empty key indicates to discard the field. This parameter is valid only if `log_type` is `delimiter_log`. `json_log` logs use the key of JSON itself. A maximum of 100 keys are supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Keys: list of str
        :param _FilterKeyRegex: Log keys to be filtered and the corresponding regex
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FilterKeyRegex: list of KeyRegexInfo
        :param _UnMatchUpLoadSwitch: Whether to upload the logs that failed to be parsed. Valid values: `true`: yes; `false`: no
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnMatchUpLoadSwitch: bool
        :param _UnMatchLogKey: Unmatched log key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnMatchLogKey: str
        :param _Backtracking: Size of the data to be rewound in incremental collection mode. Default value: -1 (full collection)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Backtracking: int
        :param _IsGBK: Whether to be encoded in GBK format. Valid values: `0` (No) and `1` (Yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsGBK: int
        :param _JsonStandard: Whether to be formatted as JSON (standard). Valid values: `0` (No) and `1` (Yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonStandard: int
        :param _Protocol: Syslog protocol. Valid values: `tcp`, `udp`.
This field can be used when you create or modify collection rule configurations.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Address: Listening address and port specified by the syslog collection. Format: [ip]:[port]. Example: 127.0.0.1:9000.
This field can be used when you create or modify collection rule configurations.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _ParseProtocol: `rfc3164`: Resolve logs by using the RFC 3164 protocol during the syslog collection.
`rfc5424`: Resolve logs by using the RFC 5424 protocol during the syslog collection.
`auto`: Automatically match either the RFC 3164 or RFC 5424 protocol.
This field can be used when you create or modify collection rule configurations.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParseProtocol: str
        :param _MetadataType: Metadata type. Valid values:
0: Do not use metadata.
1: Use machine group metadata.
2: Use user-defined metadata.
3: Use the collection path to extract metadata.
        :type MetadataType: int
        :param _PathRegex: Regular expression of the collection configuration path, which is required when `MetadataType` is set to `3`
Note: This field may return null, indicating that no valid values can be obtained.
        :type PathRegex: str
        :param _MetaTags: User-defined metadata, which is required when `MetadataType` is set to `2`.
        :type MetaTags: list of MetaTagInfo
        """
        self._TimeKey = None
        self._TimeFormat = None
        self._Delimiter = None
        self._LogRegex = None
        self._BeginRegex = None
        self._Keys = None
        self._FilterKeyRegex = None
        self._UnMatchUpLoadSwitch = None
        self._UnMatchLogKey = None
        self._Backtracking = None
        self._IsGBK = None
        self._JsonStandard = None
        self._Protocol = None
        self._Address = None
        self._ParseProtocol = None
        self._MetadataType = None
        self._PathRegex = None
        self._MetaTags = None

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def BeginRegex(self):
        return self._BeginRegex

    @BeginRegex.setter
    def BeginRegex(self, BeginRegex):
        self._BeginRegex = BeginRegex

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def FilterKeyRegex(self):
        return self._FilterKeyRegex

    @FilterKeyRegex.setter
    def FilterKeyRegex(self, FilterKeyRegex):
        self._FilterKeyRegex = FilterKeyRegex

    @property
    def UnMatchUpLoadSwitch(self):
        return self._UnMatchUpLoadSwitch

    @UnMatchUpLoadSwitch.setter
    def UnMatchUpLoadSwitch(self, UnMatchUpLoadSwitch):
        self._UnMatchUpLoadSwitch = UnMatchUpLoadSwitch

    @property
    def UnMatchLogKey(self):
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def Backtracking(self):
        return self._Backtracking

    @Backtracking.setter
    def Backtracking(self, Backtracking):
        self._Backtracking = Backtracking

    @property
    def IsGBK(self):
        return self._IsGBK

    @IsGBK.setter
    def IsGBK(self, IsGBK):
        self._IsGBK = IsGBK

    @property
    def JsonStandard(self):
        return self._JsonStandard

    @JsonStandard.setter
    def JsonStandard(self, JsonStandard):
        self._JsonStandard = JsonStandard

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ParseProtocol(self):
        return self._ParseProtocol

    @ParseProtocol.setter
    def ParseProtocol(self, ParseProtocol):
        self._ParseProtocol = ParseProtocol

    @property
    def MetadataType(self):
        return self._MetadataType

    @MetadataType.setter
    def MetadataType(self, MetadataType):
        self._MetadataType = MetadataType

    @property
    def PathRegex(self):
        return self._PathRegex

    @PathRegex.setter
    def PathRegex(self, PathRegex):
        self._PathRegex = PathRegex

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._TimeFormat = params.get("TimeFormat")
        self._Delimiter = params.get("Delimiter")
        self._LogRegex = params.get("LogRegex")
        self._BeginRegex = params.get("BeginRegex")
        self._Keys = params.get("Keys")
        if params.get("FilterKeyRegex") is not None:
            self._FilterKeyRegex = []
            for item in params.get("FilterKeyRegex"):
                obj = KeyRegexInfo()
                obj._deserialize(item)
                self._FilterKeyRegex.append(obj)
        self._UnMatchUpLoadSwitch = params.get("UnMatchUpLoadSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._Backtracking = params.get("Backtracking")
        self._IsGBK = params.get("IsGBK")
        self._JsonStandard = params.get("JsonStandard")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._ParseProtocol = params.get("ParseProtocol")
        self._MetadataType = params.get("MetadataType")
        self._PathRegex = params.get("PathRegex")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param _Key: Field to be filtered
        :type Key: str
        :param _Values: Value to be filtered
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterRuleInfo(AbstractModel):
    """Filter rule for shipped log

    """

    def __init__(self):
        r"""
        :param _Key: Filter rule key
        :type Key: str
        :param _Regex: Filter rule
        :type Regex: str
        :param _Value: Filter rule value
        :type Value: str
        """
        self._Key = None
        self._Regex = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullTextInfo(AbstractModel):
    """Full-Text index configuration

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param _Tokenizer: Separator of the full-text index. Each character represents a separator.
Only symbols, \n\t\r, and escape character \ are supported.
Note: \n\t\r can be directly enclosed in double quotes as the input parameter without escaping. When debugging with API Explorer, use the JSON parameter input method to avoid repeated escaping of \n\t\r.
        :type Tokenizer: str
        :param _ContainZH: Whether Chinese characters are contained
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ContainZH: bool
        """
        self._CaseSensitive = None
        self._Tokenizer = None
        self._ContainZH = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._Tokenizer = params.get("Tokenizer")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogRequest(AbstractModel):
    """GetAlarmLog request structure.

    """

    def __init__(self):
        r"""
        :param _From: Start time of the log to be queried, which is a Unix timestamp in milliseconds
        :type From: int
        :param _To: End time of the log to be queried, which is a Unix timestamp in milliseconds
        :type To: int
        :param _Query: Query statement. Maximum length: 1024
        :type Query: str
        :param _Limit: Number of logs returned in a single query. Maximum value: 1000
        :type Limit: int
        :param _Context: This field is used to load more logs. Pass through the last `Context` value returned to get more log content.
        :type Context: str
        :param _Sort: Order of the logs sorted by time returned by the log API. Valid values: `asc`: ascending; `desc`: descending. Default value: `desc`
        :type Sort: str
        :param _UseNewAnalysis: If the value is `true`, the new search method will be used, and the response parameters `AnalysisRecords` and `Columns` will be valid. If the value is `false`, the old search method will be used, and `AnalysisResults` and `ColNames` will be valid.
        :type UseNewAnalysis: bool
        """
        self._From = None
        self._To = None
        self._Query = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseNewAnalysis = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseNewAnalysis(self):
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogResponse(AbstractModel):
    """GetAlarmLog response structure.

    """

    def __init__(self):
        r"""
        :param _Context: `Context` for loading subsequent content
        :type Context: str
        :param _ListOver: Whether all log query results are returned
        :type ListOver: bool
        :param _Analysis: Whether the return is the analysis result
        :type Analysis: bool
        :param _ColNames: If `Analysis` is `true`, column name of the analysis result will be returned; otherwise, empty content will be returned.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ColNames: list of str
        :param _Results: Log query result. If `Analysis` is `True`, `null` may be returned
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Results: list of LogInfo
        :param _AnalysisResults: Log analysis result. If `Analysis` is `False`, `null` may be returned
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: New log analysis result, which will be valid if `UseNewAnalysis` is `true`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AnalysisRecords: list of str
        :param _Columns: Column attribute of log analysis, which will be valid if `UseNewAnalysis` is `true`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Columns: list of Column
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._ColNames = None
        self._Results = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def ColNames(self):
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def AnalysisResults(self):
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        self._ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._RequestId = params.get("RequestId")


class GroupTriggerConditionInfo(AbstractModel):
    """Condition of triggering by group

    """

    def __init__(self):
        r"""
        :param _Key: Name of the field for triggering by group
        :type Key: str
        :param _Value: Value of the field for triggering by group
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
        


class HistogramInfo(AbstractModel):
    """Histogram details

    """

    def __init__(self):
        r"""
        :param _Count: The number of logs within the statistical period
        :type Count: int
        :param _BTime: Unix timestamp rounded by `period`, in milliseconds
        :type BTime: int
        """
        self._Count = None
        self._BTime = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._BTime = params.get("BTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonInfo(AbstractModel):
    """JSON type description

    """

    def __init__(self):
        r"""
        :param _EnableTag: Enablement flag
        :type EnableTag: bool
        :param _MetaFields: List of metadata. Supported metadata types: __SOURCE__, __FILENAME__, __TIMESTAMP__, __HOSTNAME__.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetaFields: list of str
        :param _JsonType: JSON format for shipping. `0`: String format; `1`: Structured format.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JsonType: int
        """
        self._EnableTag = None
        self._MetaFields = None
        self._JsonType = None

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def JsonType(self):
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaConsumerContent(AbstractModel):
    """Kafka consumer content

    """

    def __init__(self):
        r"""
        :param _Format: Format. Valid values: 0 (full-text) and 1 (JSON).
        :type Format: int
        :param _EnableTag: Whether to ship tag information
This parameter does not need to be set when `Format` is set to `0`.
        :type EnableTag: bool
        :param _MetaFields: Metadata information list. Valid values: \_\_SOURCE\_\_, \_\_FILENAME\_\_,
\_\_TIMESTAMP\_\_, \_\_HOSTNAME\_\_, and \_\_PKGID\_\_.
This parameter does not need to be set when `Format` is set to `0`.
        :type MetaFields: list of str
        :param _TagTransaction: Tag data processing mode. Valid values:
1 (default): Do not tile data.
2: Tile data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagTransaction: int
        :param _JsonType: JSON data format. Valid values:
1 (default): Not escaped.
2: Escaped.
        :type JsonType: int
        """
        self._Format = None
        self._EnableTag = None
        self._MetaFields = None
        self._TagTransaction = None
        self._JsonType = None

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def EnableTag(self):
        return self._EnableTag

    @EnableTag.setter
    def EnableTag(self, EnableTag):
        self._EnableTag = EnableTag

    @property
    def MetaFields(self):
        return self._MetaFields

    @MetaFields.setter
    def MetaFields(self, MetaFields):
        self._MetaFields = MetaFields

    @property
    def TagTransaction(self):
        return self._TagTransaction

    @TagTransaction.setter
    def TagTransaction(self, TagTransaction):
        self._TagTransaction = TagTransaction

    @property
    def JsonType(self):
        return self._JsonType

    @JsonType.setter
    def JsonType(self, JsonType):
        self._JsonType = JsonType


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._EnableTag = params.get("EnableTag")
        self._MetaFields = params.get("MetaFields")
        self._TagTransaction = params.get("TagTransaction")
        self._JsonType = params.get("JsonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaProtocolInfo(AbstractModel):
    """Kafka access protocol

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol type. Valid values: `plaintext`, `sasl_plaintext`, and `sasl_ssl`. `sasl_ssl` is recommended. Using this protocol will encrypt the connection and implement user authentication.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Mechanism: Encryption type. Valid values: `PLAIN`, `SCRAM-SHA-256`, and SCRAM-SHA-512`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mechanism: str
        :param _UserName: Username
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Password: User password
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
        self._Protocol = None
        self._Mechanism = None
        self._UserName = None
        self._Password = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Mechanism(self):
        return self._Mechanism

    @Mechanism.setter
    def Mechanism(self, Mechanism):
        self._Mechanism = Mechanism

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Mechanism = params.get("Mechanism")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaRechargeInfo(AbstractModel):
    """Kafka data import configuration

    """

    def __init__(self):
        r"""
        :param _Id: Primary key ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _TopicId: Log topic ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _Name: Kafka data import task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _KafkaType: Kafka type. Valid values: 0 (Tencent Cloud CKafka) and 1 (customer's Kafka).
Note: This field may return null, indicating that no valid values can be obtained.
        :type KafkaType: int
        :param _KafkaInstance: CKafka instance ID, which is required when `KafkaType` is set to `0`
Note: This field may return null, indicating that no valid values can be obtained.
        :type KafkaInstance: str
        :param _ServerAddr: Service address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerAddr: str
        :param _IsEncryptionAddr: Whether the service address uses an encrypted connection	
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsEncryptionAddr: bool
        :param _Protocol: Encryption access protocol, which is required when `IsEncryptionAddr` is set to `true`
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: List of Kafka topics to import data from. Separate multiple topics with commas (,).
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: Kafka consumer group name	
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerGroupName: str
        :param _Status: Status. Valid values: 1 (running) and 2 (suspended).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Offset: Position for data import. Valid values: -2 (earliest, default) and -1 (latest).  
Note: This field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _LogRechargeRule: Log import rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._Status = None
        self._Offset = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LogRechargeRule = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRegexInfo(AbstractModel):
    """Log keys to be filtered and the corresponding regex

    """

    def __init__(self):
        r"""
        :param _Key: Log key to be filtered
        :type Key: str
        :param _Regex: Filter rule regex corresponding to key
        :type Regex: str
        """
        self._Key = None
        self._Regex = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueInfo(AbstractModel):
    """Field information of key value or metafield index

    """

    def __init__(self):
        r"""
        :param _Key: Name of the field for which you want to configure a key-value or metadata field index. The name can contain letters, digits, underscores, and symbols -./@ and cannot start with an underscore.

Note:
For a metadata field, set its `Key` to be consistent with the one for log uploading, without prefixing it with `__TAG__.`. `__TAG__.` will be prefixed automatically for display in the console.
2. The total number of keys in key-value indexes (`KeyValue`) and metadata field indexes (`Tag`) cannot exceed 300.
3. The number of levels in `Key` cannot exceed 10. Example: a.b.c.d.e.f.g.h.j.k
4. JSON parent and child fields (such as “a” and “a.b”) cannot be contained at the same time.
        :type Key: str
        :param _Value: Field index description information
        :type Value: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
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
        if params.get("Value") is not None:
            self._Value = ValueInfo()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContextInfo(AbstractModel):
    """Log context information

    """

    def __init__(self):
        r"""
        :param _Source: Log source device
        :type Source: str
        :param _Filename: Collection path
        :type Filename: str
        :param _Content: Log content
        :type Content: str
        :param _PkgId: Log package number
        :type PkgId: str
        :param _PkgLogId: Log number in log package
        :type PkgLogId: int
        :param _BTime: Log timestamp
        :type BTime: int
        :param _HostName: Source host name of logs
Note: This field may return `null`, indicating that no valid value was found.
        :type HostName: str
        :param _RawLog: Raw log (this parameter has a value only when an exception occurred while creating indexes for logs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawLog: str
        :param _IndexStatus: The cause of index creation exception (this parameter has a value only when an exception occurred while creating indexes for logs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexStatus: str
        """
        self._Source = None
        self._Filename = None
        self._Content = None
        self._PkgId = None
        self._PkgLogId = None
        self._BTime = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Filename(self):
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Filename = params.get("Filename")
        self._Content = params.get("Content")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._BTime = params.get("BTime")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """Log result information

    """

    def __init__(self):
        r"""
        :param _Time: Log time in milliseconds
        :type Time: int
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _Source: Log source IP
        :type Source: str
        :param _FileName: Log filename
        :type FileName: str
        :param _PkgId: ID of the request package for log reporting
        :type PkgId: str
        :param _PkgLogId: Log ID in request package
        :type PkgLogId: str
        :param _LogJson: Serialized JSON string of log content
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogJson: str
        :param _HostName: Source host name of logs
Note: This field may return `null`, indicating that no valid value was found.
        :type HostName: str
        :param _RawLog: Raw log (this parameter has a value only when an exception occurred while creating indexes for logs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawLog: str
        :param _IndexStatus: The cause of index creation exception (this parameter has a value only when an exception occurred while creating indexes for logs).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexStatus: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._Source = None
        self._FileName = None
        self._PkgId = None
        self._PkgLogId = None
        self._LogJson = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def LogJson(self):
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Source = params.get("Source")
        self._FileName = params.get("FileName")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._LogJson = params.get("LogJson")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """Key-Value pair in log

    """

    def __init__(self):
        r"""
        :param _Key: Log key
        :type Key: str
        :param _Value: Log value
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
        


class LogItems(AbstractModel):
    """`LogItem` array

    """

    def __init__(self):
        r"""
        :param _Data: Key-Value pair returned in analysis result
        :type Data: list of LogItem
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogRechargeRuleInfo(AbstractModel):
    """Log import rule

    """

    def __init__(self):
        r"""
        :param _RechargeType: Import type. Valid values: `json_log` (JSON logs), `minimalist_log` (single-line full text), and fullregex_log u200d(single-line full regex)
        :type RechargeType: str
        :param _EncodingFormat: Encoding format. Valid values: 0 (default, UTF-8) and 1 GBK).
        :type EncodingFormat: int
        :param _DefaultTimeSwitch: Whether to use the default time. Valid values: `true` (default) and `false`.
        :type DefaultTimeSwitch: bool
        :param _LogRegex: Full log matching rule, which is valid only if `RechargeType` is `fullregex_log`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogRegex: str
        :param _UnMatchLogSwitch: Whether to upload the logs that failed to be parsed. Valid values: `true` and `false`.
        :type UnMatchLogSwitch: bool
        :param _UnMatchLogKey: Key of the log that failed to be parsed
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnMatchLogKey: str
        :param _UnMatchLogTimeSrc: Time source of the log that failed to be parsed. Valid values: 0 (current system time) and 1 (Kafka message timestamp).
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnMatchLogTimeSrc: int
        :param _DefaultTimeSrc: Default time source. Valid values: 0 (current system time) and 1 (Kafka message timestamp).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultTimeSrc: int
        :param _TimeKey: Time field
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeKey: str
        :param _TimeRegex: Time regular expression
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeRegex: str
        :param _TimeFormat: Time field format
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeFormat: str
        :param _TimeZone: Time zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeZone: str
        :param _Metadata: Metadata information. Kafka supports import of kafka_topic, kafka_partition, kafka_offset, and kafka_timestamp.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Metadata: list of str
        :param _Keys: List of log keys, which is required when `RechargeType` is set to `full_regex_log`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Keys: list of str
        """
        self._RechargeType = None
        self._EncodingFormat = None
        self._DefaultTimeSwitch = None
        self._LogRegex = None
        self._UnMatchLogSwitch = None
        self._UnMatchLogKey = None
        self._UnMatchLogTimeSrc = None
        self._DefaultTimeSrc = None
        self._TimeKey = None
        self._TimeRegex = None
        self._TimeFormat = None
        self._TimeZone = None
        self._Metadata = None
        self._Keys = None

    @property
    def RechargeType(self):
        return self._RechargeType

    @RechargeType.setter
    def RechargeType(self, RechargeType):
        self._RechargeType = RechargeType

    @property
    def EncodingFormat(self):
        return self._EncodingFormat

    @EncodingFormat.setter
    def EncodingFormat(self, EncodingFormat):
        self._EncodingFormat = EncodingFormat

    @property
    def DefaultTimeSwitch(self):
        return self._DefaultTimeSwitch

    @DefaultTimeSwitch.setter
    def DefaultTimeSwitch(self, DefaultTimeSwitch):
        self._DefaultTimeSwitch = DefaultTimeSwitch

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def UnMatchLogSwitch(self):
        return self._UnMatchLogSwitch

    @UnMatchLogSwitch.setter
    def UnMatchLogSwitch(self, UnMatchLogSwitch):
        self._UnMatchLogSwitch = UnMatchLogSwitch

    @property
    def UnMatchLogKey(self):
        return self._UnMatchLogKey

    @UnMatchLogKey.setter
    def UnMatchLogKey(self, UnMatchLogKey):
        self._UnMatchLogKey = UnMatchLogKey

    @property
    def UnMatchLogTimeSrc(self):
        return self._UnMatchLogTimeSrc

    @UnMatchLogTimeSrc.setter
    def UnMatchLogTimeSrc(self, UnMatchLogTimeSrc):
        self._UnMatchLogTimeSrc = UnMatchLogTimeSrc

    @property
    def DefaultTimeSrc(self):
        return self._DefaultTimeSrc

    @DefaultTimeSrc.setter
    def DefaultTimeSrc(self, DefaultTimeSrc):
        self._DefaultTimeSrc = DefaultTimeSrc

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeRegex(self):
        return self._TimeRegex

    @TimeRegex.setter
    def TimeRegex(self, TimeRegex):
        self._TimeRegex = TimeRegex

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys


    def _deserialize(self, params):
        self._RechargeType = params.get("RechargeType")
        self._EncodingFormat = params.get("EncodingFormat")
        self._DefaultTimeSwitch = params.get("DefaultTimeSwitch")
        self._LogRegex = params.get("LogRegex")
        self._UnMatchLogSwitch = params.get("UnMatchLogSwitch")
        self._UnMatchLogKey = params.get("UnMatchLogKey")
        self._UnMatchLogTimeSrc = params.get("UnMatchLogTimeSrc")
        self._DefaultTimeSrc = params.get("DefaultTimeSrc")
        self._TimeKey = params.get("TimeKey")
        self._TimeRegex = params.get("TimeRegex")
        self._TimeFormat = params.get("TimeFormat")
        self._TimeZone = params.get("TimeZone")
        self._Metadata = params.get("Metadata")
        self._Keys = params.get("Keys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogsetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _LogsetName: Logset name
        :type LogsetName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _AssumerName: Cloud product identifier. If the logset is created by another cloud product, this field returns the name of the cloud product, such as `CDN` or `TKE`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssumerName: str
        :param _Tags: Tag bound to logset
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _TopicCount: Number of log topics in logset
        :type TopicCount: int
        :param _RoleName: If `AssumerName` is not empty, it indicates the service provider who creates the logset.
        :type RoleName: str
        """
        self._LogsetId = None
        self._LogsetName = None
        self._CreateTime = None
        self._AssumerName = None
        self._Tags = None
        self._TopicCount = None
        self._RoleName = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AssumerName(self):
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TopicCount(self):
        return self._TopicCount

    @TopicCount.setter
    def TopicCount(self, TopicCount):
        self._TopicCount = TopicCount

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._CreateTime = params.get("CreateTime")
        self._AssumerName = params.get("AssumerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TopicCount = params.get("TopicCount")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupInfo(AbstractModel):
    """Machine group information

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _GroupName: Machine group name
        :type GroupName: str
        :param _MachineGroupType: Machine group type
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Tags: List of tags bound to machine group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _AutoUpdate: Whether to enable automatic update for the machine group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoUpdate: str
        :param _UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateStartTime: str
        :param _UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateEndTime: str
        :param _ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServiceLogging: bool
        :param _MetaTags: Metadata information list of a machine group
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._CreateTime = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupTypeInfo(AbstractModel):
    """Machine group type description

    """

    def __init__(self):
        r"""
        :param _Type: Machine group type. Valid values: `ip`: the IP addresses of collection machines are stored in `Values` of the machine group; `label`: the tags of the machines are stored in `Values` of the machine group
        :type Type: str
        :param _Values: Machine description list
        :type Values: list of str
        """
        self._Type = None
        self._Values = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """Machine status information

    """

    def __init__(self):
        r"""
        :param _Ip: Machine IP
        :type Ip: str
        :param _Status: Machine status. Valid values: `0`: exceptional; `1`: normal
        :type Status: int
        :param _OfflineTime: Machine disconnection time. If the value is empty, the machine is normal. If the machine is exceptional, a specific value will be returned.
        :type OfflineTime: str
        :param _AutoUpdate: Whether to enable automatic update for the machine. Valid values: `0`: no; `1`: yes
        :type AutoUpdate: int
        :param _Version: Current machine version number
        :type Version: str
        :param _UpdateStatus: Machine update feature status
        :type UpdateStatus: int
        :param _ErrCode: Machine update result flag
        :type ErrCode: int
        :param _ErrMsg: Machine update result information
        :type ErrMsg: str
        """
        self._Ip = None
        self._Status = None
        self._OfflineTime = None
        self._AutoUpdate = None
        self._Version = None
        self._UpdateStatus = None
        self._ErrCode = None
        self._ErrMsg = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateStatus(self):
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoUpdate = params.get("AutoUpdate")
        self._Version = params.get("Version")
        self._UpdateStatus = params.get("UpdateStatus")
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionRequest(AbstractModel):
    """MergePartition request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _PartitionId: Merged `PartitionId`
        :type PartitionId: int
        """
        self._TopicId = None
        self._PartitionId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionResponse(AbstractModel):
    """MergePartition response structure.

    """

    def __init__(self):
        r"""
        :param _Partitions: Merge result set
        :type Partitions: list of PartitionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class MetaTagInfo(AbstractModel):
    """Metadata information

    """

    def __init__(self):
        r"""
        :param _Key: Metadata key
        :type Key: str
        :param _Value: Metadata value
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
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param _AlarmNoticeId: Notification group ID
        :type AlarmNoticeId: str
        :param _Name: Notification group name
        :type Name: str
        :param _Type: Notification type. Valid values:
<li> `Trigger`: alarm triggered
<li> `Recovery`: alarm cleared
<li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param _NoticeReceivers: Notification recipient
        :type NoticeReceivers: list of NoticeReceiver
        :param _WebCallbacks: API callback information (including WeCom)
        :type WebCallbacks: list of WebCallback
        """
        self._AlarmNoticeId = None
        self._Name = None
        self._Type = None
        self._NoticeReceivers = None
        self._WebCallbacks = None

    @property
    def AlarmNoticeId(self):
        return self._AlarmNoticeId

    @AlarmNoticeId.setter
    def AlarmNoticeId(self, AlarmNoticeId):
        self._AlarmNoticeId = AlarmNoticeId

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
    def NoticeReceivers(self):
        return self._NoticeReceivers

    @NoticeReceivers.setter
    def NoticeReceivers(self, NoticeReceivers):
        self._NoticeReceivers = NoticeReceivers

    @property
    def WebCallbacks(self):
        return self._WebCallbacks

    @WebCallbacks.setter
    def WebCallbacks(self, WebCallbacks):
        self._WebCallbacks = WebCallbacks


    def _deserialize(self, params):
        self._AlarmNoticeId = params.get("AlarmNoticeId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self._NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self._NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self._WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self._WebCallbacks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice response structure.

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


class ModifyAlarmRequest(AbstractModel):
    """ModifyAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _AlarmId: Alarm policy ID
        :type AlarmId: str
        :param _Name: Alarm policy name
        :type Name: str
        :param _MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param _Condition: Trigger condition
        :type Condition: str
        :param _TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param _AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param _AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param _AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTarget
        :param _Status: Whether to enable the alarm policy
        :type Status: bool
        :param _MessageTemplate: Custom alarm content
        :type MessageTemplate: str
        :param _CallBack: Custom callback
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param _Analysis: Multi-Dimensional analysis
        :type Analysis: list of AnalysisDimensional
        """
        self._AlarmId = None
        self._Name = None
        self._MonitorTime = None
        self._Condition = None
        self._TriggerCount = None
        self._AlarmPeriod = None
        self._AlarmNoticeIds = None
        self._AlarmTargets = None
        self._Status = None
        self._MessageTemplate = None
        self._CallBack = None
        self._Analysis = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def TriggerCount(self):
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def AlarmPeriod(self):
        return self._AlarmPeriod

    @AlarmPeriod.setter
    def AlarmPeriod(self, AlarmPeriod):
        self._AlarmPeriod = AlarmPeriod

    @property
    def AlarmNoticeIds(self):
        return self._AlarmNoticeIds

    @AlarmNoticeIds.setter
    def AlarmNoticeIds(self, AlarmNoticeIds):
        self._AlarmNoticeIds = AlarmNoticeIds

    @property
    def AlarmTargets(self):
        return self._AlarmTargets

    @AlarmTargets.setter
    def AlarmTargets(self, AlarmTargets):
        self._AlarmTargets = AlarmTargets

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageTemplate(self):
        return self._MessageTemplate

    @MessageTemplate.setter
    def MessageTemplate(self, MessageTemplate):
        self._MessageTemplate = MessageTemplate

    @property
    def CallBack(self):
        return self._CallBack

    @CallBack.setter
    def CallBack(self, CallBack):
        self._CallBack = CallBack

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._Name = params.get("Name")
        if params.get("MonitorTime") is not None:
            self._MonitorTime = MonitorTime()
            self._MonitorTime._deserialize(params.get("MonitorTime"))
        self._Condition = params.get("Condition")
        self._TriggerCount = params.get("TriggerCount")
        self._AlarmPeriod = params.get("AlarmPeriod")
        self._AlarmNoticeIds = params.get("AlarmNoticeIds")
        if params.get("AlarmTargets") is not None:
            self._AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self._AlarmTargets.append(obj)
        self._Status = params.get("Status")
        self._MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self._CallBack = CallBackInfo()
            self._CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self._Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self._Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmResponse(AbstractModel):
    """ModifyAlarm response structure.

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


class ModifyConfigRequest(AbstractModel):
    """ModifyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: Collection rule configuration ID
        :type ConfigId: str
        :param _Name: Collection rule configuration name
        :type Name: str
        :param _Path: Log collection path containing the filename
        :type Path: str
        :param _LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
        :type LogType: str
        :param _ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param _ExcludePaths: Collection path blocklist
        :type ExcludePaths: list of ExcludePathInfo
        :param _Output: Log topic (TopicId) associated with collection configuration
        :type Output: str
        :param _UserDefineRule: Custom parsing string, which is a serialized JSON string
        :type UserDefineRule: str
        """
        self._ConfigId = None
        self._Name = None
        self._Path = None
        self._LogType = None
        self._ExtractRule = None
        self._ExcludePaths = None
        self._Output = None
        self._UserDefineRule = None

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule

    @property
    def ExcludePaths(self):
        return self._ExcludePaths

    @ExcludePaths.setter
    def ExcludePaths(self, ExcludePaths):
        self._ExcludePaths = ExcludePaths

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def UserDefineRule(self):
        return self._UserDefineRule

    @UserDefineRule.setter
    def UserDefineRule(self, UserDefineRule):
        self._UserDefineRule = UserDefineRule


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._Path = params.get("Path")
        self._LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = ExtractRuleInfo()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self._ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self._ExcludePaths.append(obj)
        self._Output = params.get("Output")
        self._UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigResponse(AbstractModel):
    """ModifyConfig response structure.

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


class ModifyConsumerRequest(AbstractModel):
    """ModifyConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID bound to the task
        :type TopicId: str
        :param _Effective: Whether the shipping task takes effect (default: no)
        :type Effective: bool
        :param _NeedContent: Whether to ship metadata. Default value: `false`
        :type NeedContent: bool
        :param _Content: Metadata to ship if `NeedContent` is `true`
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param _Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param _Compression: Compression mode. Valid values: `0` (no compression), `2` (snappy), `3` (LZ4).
        :type Compression: int
        """
        self._TopicId = None
        self._Effective = None
        self._NeedContent = None
        self._Content = None
        self._Ckafka = None
        self._Compression = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Effective(self):
        return self._Effective

    @Effective.setter
    def Effective(self, Effective):
        self._Effective = Effective

    @property
    def NeedContent(self):
        return self._NeedContent

    @NeedContent.setter
    def NeedContent(self, NeedContent):
        self._NeedContent = NeedContent

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Effective = params.get("Effective")
        self._NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self._Content = ConsumerContent()
            self._Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self._Ckafka = Ckafka()
            self._Ckafka._deserialize(params.get("Ckafka"))
        self._Compression = params.get("Compression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerResponse(AbstractModel):
    """ModifyConsumer response structure.

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


class ModifyCosRechargeRequest(AbstractModel):
    """ModifyCosRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _Id: COS import configuration ID.
        :type Id: str
        :param _TopicId: ID of the log topic.
        :type TopicId: str
        :param _Name: COS import task name.
        :type Name: str
        :param _Enable: Whether the configuration is enabled. `0`: Not enabled, `1`: Enabled
        :type Enable: int
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._Enable = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCosRechargeResponse(AbstractModel):
    """ModifyCosRecharge response structure.

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


class ModifyDataTransformRequest(AbstractModel):
    """ModifyDataTransform request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Data processing task ID
        :type TaskId: str
        :param _Name: Data processing task name
        :type Name: str
        :param _EtlContent: Data processing statement
        :type EtlContent: str
        :param _EnableFlag: Task status. Valid values: 1 (enabled) and 2 (disabled).
        :type EnableFlag: int
        :param _DstResources: Destination topic ID and alias of the data processing task
        :type DstResources: list of DataTransformResouceInfo
        """
        self._TaskId = None
        self._Name = None
        self._EtlContent = None
        self._EnableFlag = None
        self._DstResources = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EtlContent(self):
        return self._EtlContent

    @EtlContent.setter
    def EtlContent(self, EtlContent):
        self._EtlContent = EtlContent

    @property
    def EnableFlag(self):
        return self._EnableFlag

    @EnableFlag.setter
    def EnableFlag(self, EnableFlag):
        self._EnableFlag = EnableFlag

    @property
    def DstResources(self):
        return self._DstResources

    @DstResources.setter
    def DstResources(self, DstResources):
        self._DstResources = DstResources


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._EtlContent = params.get("EtlContent")
        self._EnableFlag = params.get("EnableFlag")
        if params.get("DstResources") is not None:
            self._DstResources = []
            for item in params.get("DstResources"):
                obj = DataTransformResouceInfo()
                obj._deserialize(item)
                self._DstResources.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataTransformResponse(AbstractModel):
    """ModifyDataTransform response structure.

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


class ModifyIndexRequest(AbstractModel):
    """ModifyIndex request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Status: It does not take effect by default
        :type Status: bool
        :param _Rule: Index rule
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param _IncludeInternalFields: Whether full-text indexing includes internal fields (`__FILENAME__`, `__HOSTNAME__`, and `__SOURCE__`). Default value: `false`. Recommended value: `true`.
* `false`: Full-text indexing does not include internal fields.
* `true`: Full-text indexing includes internal fields.
        :type IncludeInternalFields: bool
        :param _MetadataFlag: Whether full-text indexing includes metadata fields (which are prefixed with `__TAG__`). Default value: `0`. Recommended value: `1`.
* `0`: Full-text indexing includes only metadata fields with key-value indexing enabled.
* `1`: Full-text indexing includes all metadata fields.
* `2`: Full-text indexing does not include metadata fields.
        :type MetadataFlag: int
        """
        self._TopicId = None
        self._Status = None
        self._Rule = None
        self._IncludeInternalFields = None
        self._MetadataFlag = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def IncludeInternalFields(self):
        return self._IncludeInternalFields

    @IncludeInternalFields.setter
    def IncludeInternalFields(self, IncludeInternalFields):
        self._IncludeInternalFields = IncludeInternalFields

    @property
    def MetadataFlag(self):
        return self._MetadataFlag

    @MetadataFlag.setter
    def MetadataFlag(self, MetadataFlag):
        self._MetadataFlag = MetadataFlag


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = RuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._IncludeInternalFields = params.get("IncludeInternalFields")
        self._MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIndexResponse(AbstractModel):
    """ModifyIndex response structure.

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


class ModifyKafkaRechargeRequest(AbstractModel):
    """ModifyKafkaRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Kafka data import configuration ID
        :type Id: str
        :param _TopicId: Target topic ID
        :type TopicId: str
        :param _Name: Kafka data import configuration name
        :type Name: str
        :param _KafkaType: Kafka type. Valid values: 0 (Tencent Cloud CKafka) and 1 (customer's Kafka)
        :type KafkaType: int
        :param _KafkaInstance: CKafka instance ID, which is required when `KafkaType` is set to `0`
        :type KafkaInstance: str
        :param _ServerAddr: Service address
        :type ServerAddr: str
        :param _IsEncryptionAddr: Whether the service address uses an encrypted connection
        :type IsEncryptionAddr: bool
        :param _Protocol: Encryption access protocol, which is required when IsEncryptionAddr` is set to `true`
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _UserKafkaTopics: List of Kafka topics to import data from. Separate multiple topics with commas (,).
        :type UserKafkaTopics: str
        :param _ConsumerGroupName: Kafka consumer group name
        :type ConsumerGroupName: str
        :param _LogRechargeRule: Log import rule
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        :param _StatusControl: Import control. Valid values: 1 (suspend) and 2 (resume).
        :type StatusControl: int
        """
        self._Id = None
        self._TopicId = None
        self._Name = None
        self._KafkaType = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._UserKafkaTopics = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None
        self._StatusControl = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule

    @property
    def StatusControl(self):
        return self._StatusControl

    @StatusControl.setter
    def StatusControl(self, StatusControl):
        self._StatusControl = StatusControl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TopicId = params.get("TopicId")
        self._Name = params.get("Name")
        self._KafkaType = params.get("KafkaType")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        self._StatusControl = params.get("StatusControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKafkaRechargeResponse(AbstractModel):
    """ModifyKafkaRecharge response structure.

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


class ModifyLogsetRequest(AbstractModel):
    """ModifyLogset request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _LogsetName: Logset name
        :type LogsetName: str
        :param _Tags: Tag key-value pair bound to logset. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key at any time.
        :type Tags: list of Tag
        """
        self._LogsetId = None
        self._LogsetName = None
        self._Tags = None

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
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
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
        


class ModifyLogsetResponse(AbstractModel):
    """ModifyLogset response structure.

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


class ModifyMachineGroupRequest(AbstractModel):
    """ModifyMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Machine group ID
        :type GroupId: str
        :param _GroupName: Machine group name
        :type GroupName: str
        :param _MachineGroupType: Machine group type
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _AutoUpdate: Whether to enable automatic update for the machine group
        :type AutoUpdate: bool
        :param _UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
        :type UpdateStartTime: str
        :param _UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
        :type UpdateEndTime: str
        :param _ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees.
        :type ServiceLogging: bool
        :param _MetaTags: Metadata information list of a machine group
        :type MetaTags: list of MetaTagInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._MachineGroupType = None
        self._Tags = None
        self._AutoUpdate = None
        self._UpdateStartTime = None
        self._UpdateEndTime = None
        self._ServiceLogging = None
        self._MetaTags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MachineGroupType(self):
        return self._MachineGroupType

    @MachineGroupType.setter
    def MachineGroupType(self, MachineGroupType):
        self._MachineGroupType = MachineGroupType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoUpdate(self):
        return self._AutoUpdate

    @AutoUpdate.setter
    def AutoUpdate(self, AutoUpdate):
        self._AutoUpdate = AutoUpdate

    @property
    def UpdateStartTime(self):
        return self._UpdateStartTime

    @UpdateStartTime.setter
    def UpdateStartTime(self, UpdateStartTime):
        self._UpdateStartTime = UpdateStartTime

    @property
    def UpdateEndTime(self):
        return self._UpdateEndTime

    @UpdateEndTime.setter
    def UpdateEndTime(self, UpdateEndTime):
        self._UpdateEndTime = UpdateEndTime

    @property
    def ServiceLogging(self):
        return self._ServiceLogging

    @ServiceLogging.setter
    def ServiceLogging(self, ServiceLogging):
        self._ServiceLogging = ServiceLogging

    @property
    def MetaTags(self):
        return self._MetaTags

    @MetaTags.setter
    def MetaTags(self, MetaTags):
        self._MetaTags = MetaTags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self._MachineGroupType = MachineGroupTypeInfo()
            self._MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoUpdate = params.get("AutoUpdate")
        self._UpdateStartTime = params.get("UpdateStartTime")
        self._UpdateEndTime = params.get("UpdateEndTime")
        self._ServiceLogging = params.get("ServiceLogging")
        if params.get("MetaTags") is not None:
            self._MetaTags = []
            for item in params.get("MetaTags"):
                obj = MetaTagInfo()
                obj._deserialize(item)
                self._MetaTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMachineGroupResponse(AbstractModel):
    """ModifyMachineGroup response structure.

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


class ModifyShipperRequest(AbstractModel):
    """ModifyShipper request structure.

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping rule ID
        :type ShipperId: str
        :param _Bucket: New destination bucket in shipping rule
        :type Bucket: str
        :param _Prefix: New destination directory prefix in shipping rule
        :type Prefix: str
        :param _Status: Shipping rule status
        :type Status: bool
        :param _ShipperName: Shipping rule name
        :type ShipperName: str
        :param _Interval: Shipping time interval in seconds. Default value: 300. Value range: 300–900
        :type Interval: int
        :param _MaxSize: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 5-256
        :type MaxSize: int
        :param _FilterRules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: Partition rule of shipped log, which can be represented in `strftime` time format
        :type Partition: str
        :param _Compress: Compression configuration of shipped log
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: Format configuration of shipped log content
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _FilenameMode: Naming a shipping file. Valid values: `0` (by random number), `1` (by shipping time). Default value: `0`.
        :type FilenameMode: int
        """
        self._ShipperId = None
        self._Bucket = None
        self._Prefix = None
        self._Status = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._FilenameMode = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._Status = params.get("Status")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._FilenameMode = params.get("FilenameMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyShipperResponse(AbstractModel):
    """ModifyShipper response structure.

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


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _Tags: Tag description list. This parameter is used to bind a tag to a log topic. Up to 10 tag key-value pairs are supported, and they must be unique.
        :type Tags: list of Tag
        :param _Status: Whether to start collection for this log topic
        :type Status: bool
        :param _AutoSplit: Whether to enable automatic split
        :type AutoSplit: bool
        :param _MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled
        :type MaxSplitPartitions: int
        :param _Period: Lifecycle in days. Value range: 1–3600 (STANDARD storage); 7–3600 (IA storage). `3640` indicates permanent retention.
        :type Period: int
        :param _Describes: Log topic description
        :type Describes: str
        :param _HotPeriod: `0`: Disable log transitioning.
A value other than `0`: The number of STANDARD storage days after log transitioning is enabled (valid only if `StorageType` is `hot`). Note: `HotPeriod` should be greater than or equal to `7` and less than `Period`.
        :type HotPeriod: int
        :param _IsWebTracking: Whether to enable web tracking. Valid values: `false` (disable); `true` (enable)
        :type IsWebTracking: bool
        """
        self._TopicId = None
        self._TopicName = None
        self._Tags = None
        self._Status = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._Period = None
        self._Describes = None
        self._HotPeriod = None
        self._IsWebTracking = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod

    @property
    def IsWebTracking(self):
        return self._IsWebTracking

    @IsWebTracking.setter
    def IsWebTracking(self, IsWebTracking):
        self._IsWebTracking = IsWebTracking


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._Period = params.get("Period")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        self._IsWebTracking = params.get("IsWebTracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic response structure.

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


class MonitorTime(AbstractModel):
    """Monitoring task execution time point in alarm policy

    """

    def __init__(self):
        r"""
        :param _Type: Valid values:
<br><li> `Period`: periodic execution
<br><li> `Fixed`: scheduled execution
        :type Type: str
        :param _Time: Execution interval or scheduled time point in minutes. Value range: 1–1440.
        :type Time: int
        """
        self._Type = None
        self._Time = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiTopicSearchInformation(AbstractModel):
    """Log topic search information

    """

    def __init__(self):
        r"""
        :param _TopicId: ID of the log topic to be searched for
        :type TopicId: str
        :param _Context: You can pass through the `Context` value (validity: 1 hour) returned by the last API to continue to get logs, which can get up to 10,000 raw logs.
        :type Context: str
        """
        self._TopicId = None
        self._Context = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeReceiver(AbstractModel):
    """Alarm notification recipient information

    """

    def __init__(self):
        r"""
        :param _ReceiverType: Recipient type. Valid values:
<br><li> `Uin`: user ID
<br><li> `Group`: user group ID
Currently, other recipient types are not supported.
        :type ReceiverType: str
        :param _ReceiverIds: Recipient
        :type ReceiverIds: list of int
        :param _ReceiverChannels: Notification method
<br><li> `Email`: email
<br><li> `Sms`: SMS
<br><li> `WeChat`: WeChat
<br><li> `Phone`: phone
        :type ReceiverChannels: list of str
        :param _StartTime: Start time for allowed message receipt
        :type StartTime: str
        :param _EndTime: End time for allowed message receipt
        :type EndTime: str
        :param _Index: Index
        :type Index: int
        """
        self._ReceiverType = None
        self._ReceiverIds = None
        self._ReceiverChannels = None
        self._StartTime = None
        self._EndTime = None
        self._Index = None

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def ReceiverIds(self):
        return self._ReceiverIds

    @ReceiverIds.setter
    def ReceiverIds(self, ReceiverIds):
        self._ReceiverIds = ReceiverIds

    @property
    def ReceiverChannels(self):
        return self._ReceiverChannels

    @ReceiverChannels.setter
    def ReceiverChannels(self, ReceiverChannels):
        self._ReceiverChannels = ReceiverChannels

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
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._ReceiverIds = params.get("ReceiverIds")
        self._ReceiverChannels = params.get("ReceiverChannels")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerRequest(AbstractModel):
    """OpenKafkaConsumer request structure.

    """

    def __init__(self):
        r"""
        :param _FromTopicId: `TopicId` created by the CLS console
        :type FromTopicId: str
        :param _Compression: Compression mode. Valid values: `0` (no compression); `2` (snappy); `3` (LZ4)
        :type Compression: int
        :param _ConsumerContent: Kafka consumer data format
        :type ConsumerContent: :class:`tencentcloud.cls.v20201016.models.KafkaConsumerContent`
        """
        self._FromTopicId = None
        self._Compression = None
        self._ConsumerContent = None

    @property
    def FromTopicId(self):
        return self._FromTopicId

    @FromTopicId.setter
    def FromTopicId(self, FromTopicId):
        self._FromTopicId = FromTopicId

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def ConsumerContent(self):
        return self._ConsumerContent

    @ConsumerContent.setter
    def ConsumerContent(self, ConsumerContent):
        self._ConsumerContent = ConsumerContent


    def _deserialize(self, params):
        self._FromTopicId = params.get("FromTopicId")
        self._Compression = params.get("Compression")
        if params.get("ConsumerContent") is not None:
            self._ConsumerContent = KafkaConsumerContent()
            self._ConsumerContent._deserialize(params.get("ConsumerContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerResponse(AbstractModel):
    """OpenKafkaConsumer response structure.

    """

    def __init__(self):
        r"""
        :param _TopicID: `TopicId` to be consumed
        :type TopicID: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicID = None
        self._RequestId = None

    @property
    def TopicID(self):
        return self._TopicID

    @TopicID.setter
    def TopicID(self, TopicID):
        self._TopicID = TopicID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicID = params.get("TopicID")
        self._RequestId = params.get("RequestId")


class ParquetInfo(AbstractModel):
    """`Parquet` contents

    """

    def __init__(self):
        r"""
        :param _ParquetKeyInfo: `ParquetKeyInfo` array
        :type ParquetKeyInfo: list of ParquetKeyInfo
        """
        self._ParquetKeyInfo = None

    @property
    def ParquetKeyInfo(self):
        return self._ParquetKeyInfo

    @ParquetKeyInfo.setter
    def ParquetKeyInfo(self, ParquetKeyInfo):
        self._ParquetKeyInfo = ParquetKeyInfo


    def _deserialize(self, params):
        if params.get("ParquetKeyInfo") is not None:
            self._ParquetKeyInfo = []
            for item in params.get("ParquetKeyInfo"):
                obj = ParquetKeyInfo()
                obj._deserialize(item)
                self._ParquetKeyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParquetKeyInfo(AbstractModel):
    """`Parquet` content description

    """

    def __init__(self):
        r"""
        :param _KeyName: Key name
        :type KeyName: str
        :param _KeyType: Supported data types: string, boolean, int32, int64, float, and double
        :type KeyType: str
        :param _KeyNonExistingField: Assignment information returned upon resolution failure
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type KeyNonExistingField: str
        """
        self._KeyName = None
        self._KeyType = None
        self._KeyNonExistingField = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def KeyType(self):
        return self._KeyType

    @KeyType.setter
    def KeyType(self, KeyType):
        self._KeyType = KeyType

    @property
    def KeyNonExistingField(self):
        return self._KeyNonExistingField

    @KeyNonExistingField.setter
    def KeyNonExistingField(self, KeyNonExistingField):
        self._KeyNonExistingField = KeyNonExistingField


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._KeyType = params.get("KeyType")
        self._KeyNonExistingField = params.get("KeyNonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """Log topic partition information

    """

    def __init__(self):
        r"""
        :param _PartitionId: Partition ID
        :type PartitionId: int
        :param _Status: Partition status. Valid values: `readwrite`, `readonly`
        :type Status: str
        :param _InclusiveBeginKey: Partition hash start key
        :type InclusiveBeginKey: str
        :param _ExclusiveEndKey: Partition hash end key
        :type ExclusiveEndKey: str
        :param _CreateTime: Partition creation time
        :type CreateTime: str
        :param _LastWriteTime: Last modified of read-only partition
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LastWriteTime: str
        """
        self._PartitionId = None
        self._Status = None
        self._InclusiveBeginKey = None
        self._ExclusiveEndKey = None
        self._CreateTime = None
        self._LastWriteTime = None

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InclusiveBeginKey(self):
        return self._InclusiveBeginKey

    @InclusiveBeginKey.setter
    def InclusiveBeginKey(self, InclusiveBeginKey):
        self._InclusiveBeginKey = InclusiveBeginKey

    @property
    def ExclusiveEndKey(self):
        return self._ExclusiveEndKey

    @ExclusiveEndKey.setter
    def ExclusiveEndKey(self, ExclusiveEndKey):
        self._ExclusiveEndKey = ExclusiveEndKey

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastWriteTime(self):
        return self._LastWriteTime

    @LastWriteTime.setter
    def LastWriteTime(self, LastWriteTime):
        self._LastWriteTime = LastWriteTime


    def _deserialize(self, params):
        self._PartitionId = params.get("PartitionId")
        self._Status = params.get("Status")
        self._InclusiveBeginKey = params.get("InclusiveBeginKey")
        self._ExclusiveEndKey = params.get("ExclusiveEndKey")
        self._CreateTime = params.get("CreateTime")
        self._LastWriteTime = params.get("LastWriteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeRequest(AbstractModel):
    """PreviewKafkaRecharge request structure.

    """

    def __init__(self):
        r"""
        :param _PreviewType: Preview type. Valid values: 1 (source data preview) and 2 (result preview).
        :type PreviewType: int
        :param _KafkaType: Kafka type. Valid values: 0 (Tencent Cloud CKafka) and 1 (customer's Kafka)
        :type KafkaType: int
        :param _UserKafkaTopics: List of Kafka topics to import data from. Separate multiple topics with commas (,).
        :type UserKafkaTopics: str
        :param _Offset: Position for data import. Valid values: -2 (earliest, default) and -1 (latest).
        :type Offset: int
        :param _KafkaInstance: CKafka instance ID, which is required when `KafkaType` is set to `0`
        :type KafkaInstance: str
        :param _ServerAddr: Service address
        :type ServerAddr: str
        :param _IsEncryptionAddr: Whether the service address uses an encrypted connection
        :type IsEncryptionAddr: bool
        :param _Protocol: Encryption access protocol, which is required when `IsEncryptionAddr` is set to `true`
        :type Protocol: :class:`tencentcloud.cls.v20201016.models.KafkaProtocolInfo`
        :param _ConsumerGroupName: Kafka consumer group name
        :type ConsumerGroupName: str
        :param _LogRechargeRule: Log import rule
        :type LogRechargeRule: :class:`tencentcloud.cls.v20201016.models.LogRechargeRuleInfo`
        """
        self._PreviewType = None
        self._KafkaType = None
        self._UserKafkaTopics = None
        self._Offset = None
        self._KafkaInstance = None
        self._ServerAddr = None
        self._IsEncryptionAddr = None
        self._Protocol = None
        self._ConsumerGroupName = None
        self._LogRechargeRule = None

    @property
    def PreviewType(self):
        return self._PreviewType

    @PreviewType.setter
    def PreviewType(self, PreviewType):
        self._PreviewType = PreviewType

    @property
    def KafkaType(self):
        return self._KafkaType

    @KafkaType.setter
    def KafkaType(self, KafkaType):
        self._KafkaType = KafkaType

    @property
    def UserKafkaTopics(self):
        return self._UserKafkaTopics

    @UserKafkaTopics.setter
    def UserKafkaTopics(self, UserKafkaTopics):
        self._UserKafkaTopics = UserKafkaTopics

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def KafkaInstance(self):
        return self._KafkaInstance

    @KafkaInstance.setter
    def KafkaInstance(self, KafkaInstance):
        self._KafkaInstance = KafkaInstance

    @property
    def ServerAddr(self):
        return self._ServerAddr

    @ServerAddr.setter
    def ServerAddr(self, ServerAddr):
        self._ServerAddr = ServerAddr

    @property
    def IsEncryptionAddr(self):
        return self._IsEncryptionAddr

    @IsEncryptionAddr.setter
    def IsEncryptionAddr(self, IsEncryptionAddr):
        self._IsEncryptionAddr = IsEncryptionAddr

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ConsumerGroupName(self):
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def LogRechargeRule(self):
        return self._LogRechargeRule

    @LogRechargeRule.setter
    def LogRechargeRule(self, LogRechargeRule):
        self._LogRechargeRule = LogRechargeRule


    def _deserialize(self, params):
        self._PreviewType = params.get("PreviewType")
        self._KafkaType = params.get("KafkaType")
        self._UserKafkaTopics = params.get("UserKafkaTopics")
        self._Offset = params.get("Offset")
        self._KafkaInstance = params.get("KafkaInstance")
        self._ServerAddr = params.get("ServerAddr")
        self._IsEncryptionAddr = params.get("IsEncryptionAddr")
        if params.get("Protocol") is not None:
            self._Protocol = KafkaProtocolInfo()
            self._Protocol._deserialize(params.get("Protocol"))
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("LogRechargeRule") is not None:
            self._LogRechargeRule = LogRechargeRuleInfo()
            self._LogRechargeRule._deserialize(params.get("LogRechargeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewKafkaRechargeResponse(AbstractModel):
    """PreviewKafkaRecharge response structure.

    """

    def __init__(self):
        r"""
        :param _LogSample: Log sample, which is returned when `PreviewType` is set to `2`
        :type LogSample: str
        :param _LogData: Log preview result
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogSample = None
        self._LogData = None
        self._RequestId = None

    @property
    def LogSample(self):
        return self._LogSample

    @LogSample.setter
    def LogSample(self, LogSample):
        self._LogSample = LogSample

    @property
    def LogData(self):
        return self._LogData

    @LogData.setter
    def LogData(self, LogData):
        self._LogData = LogData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogSample = params.get("LogSample")
        self._LogData = params.get("LogData")
        self._RequestId = params.get("RequestId")


class PreviewLogStatistic(AbstractModel):
    """Preview data details

    """

    def __init__(self):
        r"""
        :param _LogContent: Log content
        :type LogContent: str
        :param _LineNum: Line number
        :type LineNum: int
        :param _DstTopicId: Target log topic
        :type DstTopicId: str
        :param _FailReason: Error code. An empty string "" indicates no error.
        :type FailReason: str
        :param _Time: Log timestamp
        :type Time: str
        :param _DstTopicName: Target topic name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstTopicName: str
        """
        self._LogContent = None
        self._LineNum = None
        self._DstTopicId = None
        self._FailReason = None
        self._Time = None
        self._DstTopicName = None

    @property
    def LogContent(self):
        return self._LogContent

    @LogContent.setter
    def LogContent(self, LogContent):
        self._LogContent = LogContent

    @property
    def LineNum(self):
        return self._LineNum

    @LineNum.setter
    def LineNum(self, LineNum):
        self._LineNum = LineNum

    @property
    def DstTopicId(self):
        return self._DstTopicId

    @DstTopicId.setter
    def DstTopicId(self, DstTopicId):
        self._DstTopicId = DstTopicId

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def DstTopicName(self):
        return self._DstTopicName

    @DstTopicName.setter
    def DstTopicName(self, DstTopicName):
        self._DstTopicName = DstTopicName


    def _deserialize(self, params):
        self._LogContent = params.get("LogContent")
        self._LineNum = params.get("LineNum")
        self._DstTopicId = params.get("DstTopicId")
        self._FailReason = params.get("FailReason")
        self._Time = params.get("Time")
        self._DstTopicName = params.get("DstTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskRequest(AbstractModel):
    """RetryShipperTask request structure.

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping rule ID
        :type ShipperId: str
        :param _TaskId: Shipping task ID
        :type TaskId: str
        """
        self._ShipperId = None
        self._TaskId = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskResponse(AbstractModel):
    """RetryShipperTask response structure.

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


class RuleInfo(AbstractModel):
    """Index rule. At least one of the `FullText`, `KeyValue`, and `Tag` parameters must be valid.

    """

    def __init__(self):
        r"""
        :param _FullText: Full-text index configuration. If the configuration is left empty, full-text indexing is not enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullText: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        :param _KeyValue: Key-value index configuration. If the configuration is left empty, key-value indexing is not enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyValue: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        :param _Tag: Metadata field index configuration. If the configuration is left empty, metadata field indexing is not enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tag: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        :param _DynamicIndex: Dynamic index configuration. If the configuration is empty, dynamic indexing is not enabled.

Note: This feature is currently in a beta test. To use it, please contact technical support.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DynamicIndex: :class:`tencentcloud.cls.v20201016.models.DynamicIndex`
        """
        self._FullText = None
        self._KeyValue = None
        self._Tag = None
        self._DynamicIndex = None

    @property
    def FullText(self):
        return self._FullText

    @FullText.setter
    def FullText(self, FullText):
        self._FullText = FullText

    @property
    def KeyValue(self):
        return self._KeyValue

    @KeyValue.setter
    def KeyValue(self, KeyValue):
        self._KeyValue = KeyValue

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DynamicIndex(self):
        return self._DynamicIndex

    @DynamicIndex.setter
    def DynamicIndex(self, DynamicIndex):
        self._DynamicIndex = DynamicIndex


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self._FullText = FullTextInfo()
            self._FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self._KeyValue = RuleKeyValueInfo()
            self._KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self._Tag = RuleTagInfo()
            self._Tag._deserialize(params.get("Tag"))
        if params.get("DynamicIndex") is not None:
            self._DynamicIndex = DynamicIndex()
            self._DynamicIndex._deserialize(params.get("DynamicIndex"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleKeyValueInfo(AbstractModel):
    """Key-Value index configuration

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param _KeyValues: Key-value pair information of the index to be created
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTagInfo(AbstractModel):
    """Metafield index configuration

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param _KeyValues: Field information in the metafield index configuration
        :type KeyValues: list of KeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog request structure.

    """

    def __init__(self):
        r"""
        :param _From: Start time of the log to be searched, which is a Unix timestamp in milliseconds
        :type From: int
        :param _To: End time of the log to be searched, which is a Unix timestamp in milliseconds
        :type To: int
        :param _Query: Search and analysis statement. Maximum length: 12 KB
A statement is in the format of <a href="https://intl.cloud.tencent.com/document/product/614/47044?from_cn_redirect=1" target="_blank">[search criteria]</a> | <a href="https://intl.cloud.tencent.com/document/product/614/44061?from_cn_redirect=1" target="_blank">[SQL statement]</a>. You can omit the pipe symbol <code> | </code> and SQL statement when log analysis is not required.
Queries all logs using * or an empty string
        :type Query: str
        :param _TopicId: - The ID of the log topic to be searched for. Only one log topic can be specified.
- To search for multiple log topics at a time, use the `Topics` parameter.
        :type TopicId: str
        :param _Limit: The number of raw logs returned by a single query. Maximum value: 1000. You need to use `Context` to continue to get logs.
Notes:
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To limit the number of analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58977?from_cn_redirect=1" target="_blank">SQL LIMIT Syntax</a>.
        :type Limit: int
        :param _Context: You can pass through the `Context` value (validity: an hour) returned by the API last time to continue to get logs (up to 10,000 raw logs).
Notes:
* Do not modify any other parameters while passing through the `Context` parameter.
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To continue to get analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58977?from_cn_redirect=1" target="_blank">SQL LIMIT Syntax</a>.
        :type Context: str
        :param _Sort: Time order of the logs returned. Valid values: `asc` (ascending); `desc`: (descending). Default value: `desc`
Notes:
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To sort the analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58978?from_cn_redirect=1" target="_blank">SQL ORDER BY Syntax</a>.
        :type Sort: str
        :param _UseNewAnalysis: If the value is `true`, the new response method will be used, and the output parameters `AnalysisRecords` and `Columns` will be valid.
If the value is `false`, the old response method will be used, and the output parameters `AnalysisResults` and `ColNames` will be valid.
The two response methods differ slightly in terms of encoding format. You are advised to use the new method (`true`).
        :type UseNewAnalysis: bool
        :param _SamplingRate: Indicates whether to sample raw logs before statistical analysis (`Query` includes SQL statements).
`0`: Auto-sample.
`0–1`: Sample by the specified sample rate, such as `0.02`.
`1`: Precise analysis without sampling.
Default value: `1`
        :type SamplingRate: float
        :param _SyntaxRule: Search syntax
`0` (default): Lucene; `1`: CQL.
For more information, see <a href="https://intl.cloud.tencent.com/document/product/614/47044?from_cn_redirect=1#RetrievesConditionalRules" target="_blank">Syntax Rules</a>
        :type SyntaxRule: int
        :param _Topics: - The IDs of the log topics (up to 20) to be searched for.
- To search for a single log topic, use the `TopicId` parameter.
- You cannot use both `TopicId` and `Topics`.
        :type Topics: list of MultiTopicSearchInformation
        """
        self._From = None
        self._To = None
        self._Query = None
        self._TopicId = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._UseNewAnalysis = None
        self._SamplingRate = None
        self._SyntaxRule = None
        self._Topics = None

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def UseNewAnalysis(self):
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis

    @property
    def SamplingRate(self):
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def SyntaxRule(self):
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._TopicId = params.get("TopicId")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        self._SamplingRate = params.get("SamplingRate")
        self._SyntaxRule = params.get("SyntaxRule")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = MultiTopicSearchInformation()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog response structure.

    """

    def __init__(self):
        r"""
        :param _Context: You can pass through the `Context` value (validity: 1 hour) returned by this API to continue to get more logs.
        :type Context: str
        :param _ListOver: Whether to return all raw log query results. If not, you can use `Context` to continue to get logs.
Note: This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
        :type ListOver: bool
        :param _Analysis: Whether the returned data is the analysis (SQL) result
        :type Analysis: bool
        :param _Results: Raw logs that meet the search conditions
Note: This field may return `null`, indicating that no valid value was found.
        :type Results: list of LogInfo
        :param _ColNames: Column names of log analysis
This parameter is valid only when `UseNewAnalysis` is `false`.
Note: This field may return `null`, indicating that no valid value was found.
        :type ColNames: list of str
        :param _AnalysisResults: Log analysis result
This parameter is valid only when `UseNewAnalysis` is `false`.
Note: This field may return `null`, indicating that no valid value was found.
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: Log analysis result
This parameter is valid only when `UseNewAnalysis` is `true`.
Note: This field may return `null`, indicating that no valid value was found.
        :type AnalysisRecords: list of str
        :param _Columns: Column attributes of log analysis
This parameter is valid only when `UseNewAnalysis` is `true`.
Note: This field may return `null`, indicating that no valid value was found.
        :type Columns: list of Column
        :param _SamplingRate: Sample rate used in this statistical analysis
Note: This field may return null, indicating that no valid values can be obtained.
        :type SamplingRate: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._Results = None
        self._ColNames = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._SamplingRate = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ColNames(self):
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def AnalysisResults(self):
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def SamplingRate(self):
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        self._ColNames = params.get("ColNames")
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._SamplingRate = params.get("SamplingRate")
        self._RequestId = params.get("RequestId")


class ShipperInfo(AbstractModel):
    """Shipping rule

    """

    def __init__(self):
        r"""
        :param _ShipperId: Shipping rule ID
        :type ShipperId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Bucket: Bucket address shipped to
        :type Bucket: str
        :param _Prefix: Shipping prefix directory
        :type Prefix: str
        :param _ShipperName: Shipping rule name
        :type ShipperName: str
        :param _Interval: Shipping time interval in seconds
        :type Interval: int
        :param _MaxSize: Maximum size of shipped file in MB
        :type MaxSize: int
        :param _Status: Whether it takes effect
        :type Status: bool
        :param _FilterRules: Filter rule for shipped log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FilterRules: list of FilterRuleInfo
        :param _Partition: Partition rule of shipped log, which can be represented in `strftime` time format
        :type Partition: str
        :param _Compress: Compression configuration of shipped log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param _Content: Format configuration of shipped log content
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param _CreateTime: Creation time of shipped log
        :type CreateTime: str
        :param _FilenameMode: Shipping file naming configuration. Valid values: `0` (by random number); `1` (by shipping time). Default value: `0`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilenameMode: int
        :param _StartTime: Start time for data shipping
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param _EndTime: End time for data shipping
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _Progress: Progress of historical data shipping (valid only when the selected data scope contains historical data)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: float
        :param _RemainTime: Remaining time required for shipping all historical data (valid only when the selected data scope contains historical data)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RemainTime: int
        :param _HistoryStatus: Status of historical data shipping. Valid values:
0: Real-time data is being shipped.
1: The system is preparing for historical data shipping.
2: Historical data is being shipped.
3: An error occurred while shipping historical data.
4: Historical data shipping ended.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HistoryStatus: int
        """
        self._ShipperId = None
        self._TopicId = None
        self._Bucket = None
        self._Prefix = None
        self._ShipperName = None
        self._Interval = None
        self._MaxSize = None
        self._Status = None
        self._FilterRules = None
        self._Partition = None
        self._Compress = None
        self._Content = None
        self._CreateTime = None
        self._FilenameMode = None
        self._StartTime = None
        self._EndTime = None
        self._Progress = None
        self._RemainTime = None
        self._HistoryStatus = None

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def ShipperName(self):
        return self._ShipperName

    @ShipperName.setter
    def ShipperName(self, ShipperName):
        self._ShipperName = ShipperName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FilenameMode(self):
        return self._FilenameMode

    @FilenameMode.setter
    def FilenameMode(self, FilenameMode):
        self._FilenameMode = FilenameMode

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
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RemainTime(self):
        return self._RemainTime

    @RemainTime.setter
    def RemainTime(self, RemainTime):
        self._RemainTime = RemainTime

    @property
    def HistoryStatus(self):
        return self._HistoryStatus

    @HistoryStatus.setter
    def HistoryStatus(self, HistoryStatus):
        self._HistoryStatus = HistoryStatus


    def _deserialize(self, params):
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._Bucket = params.get("Bucket")
        self._Prefix = params.get("Prefix")
        self._ShipperName = params.get("ShipperName")
        self._Interval = params.get("Interval")
        self._MaxSize = params.get("MaxSize")
        self._Status = params.get("Status")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self._Compress = CompressInfo()
            self._Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self._Content = ContentInfo()
            self._Content._deserialize(params.get("Content"))
        self._CreateTime = params.get("CreateTime")
        self._FilenameMode = params.get("FilenameMode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Progress = params.get("Progress")
        self._RemainTime = params.get("RemainTime")
        self._HistoryStatus = params.get("HistoryStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperTaskInfo(AbstractModel):
    """Shipping task information

    """

    def __init__(self):
        r"""
        :param _TaskId: Shipping task ID
        :type TaskId: str
        :param _ShipperId: Shipping information ID
        :type ShipperId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _RangeStart: Start timestamp of the current batch of shipped logs in milliseconds
        :type RangeStart: int
        :param _RangeEnd: End timestamp of the current batch of shipped logs in milliseconds
        :type RangeEnd: int
        :param _StartTime: Start timestamp of the current shipping task in milliseconds
        :type StartTime: int
        :param _EndTime: End timestamp of the current shipping task in milliseconds
        :type EndTime: int
        :param _Status: Result of the current shipping task. Valid values: `success`, `running`, `failed`
        :type Status: str
        :param _Message: Result details
        :type Message: str
        """
        self._TaskId = None
        self._ShipperId = None
        self._TopicId = None
        self._RangeStart = None
        self._RangeEnd = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Message = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShipperId(self):
        return self._ShipperId

    @ShipperId.setter
    def ShipperId(self, ShipperId):
        self._ShipperId = ShipperId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RangeStart(self):
        return self._RangeStart

    @RangeStart.setter
    def RangeStart(self, RangeStart):
        self._RangeStart = RangeStart

    @property
    def RangeEnd(self):
        return self._RangeEnd

    @RangeEnd.setter
    def RangeEnd(self, RangeEnd):
        self._RangeEnd = RangeEnd

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ShipperId = params.get("ShipperId")
        self._TopicId = params.get("TopicId")
        self._RangeStart = params.get("RangeStart")
        self._RangeEnd = params.get("RangeEnd")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionRequest(AbstractModel):
    """SplitPartition request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _PartitionId: ID of the partition to be split
        :type PartitionId: int
        :param _SplitKey: Partition split hash key position, which is meaningful only if `Number=2` is set
        :type SplitKey: str
        :param _Number: Number of partitions to split into, which is optional. Default value: 2
        :type Number: int
        """
        self._TopicId = None
        self._PartitionId = None
        self._SplitKey = None
        self._Number = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def PartitionId(self):
        return self._PartitionId

    @PartitionId.setter
    def PartitionId(self, PartitionId):
        self._PartitionId = PartitionId

    @property
    def SplitKey(self):
        return self._SplitKey

    @SplitKey.setter
    def SplitKey(self, SplitKey):
        self._SplitKey = SplitKey

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._PartitionId = params.get("PartitionId")
        self._SplitKey = params.get("SplitKey")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionResponse(AbstractModel):
    """SplitPartition response structure.

    """

    def __init__(self):
        r"""
        :param _Partitions: Split result set
        :type Partitions: list of PartitionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Partitions = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self._Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._Partitions.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Description of the tag pair bound to a resource instance when it is created

    """

    def __init__(self):
        r"""
        :param _Key: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class TopicInfo(AbstractModel):
    """Log topic information

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _PartitionCount: Number of topic partitions
        :type PartitionCount: int
        :param _Index: Whether index is enabled
        :type Index: bool
        :param _AssumerName: Cloud product identifier. If the log topic is created by another cloud product, this field returns the name of the cloud product, such as `CDN` or `TKE`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssumerName: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Status: Whether collection is enabled in the log topic
        :type Status: bool
        :param _Tags: Information of tags bound to log topic
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _AutoSplit: Whether automatic split is enabled for this topic
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoSplit: bool
        :param _MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxSplitPartitions: int
        :param _StorageType: Log topic storage class
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageType: str
        :param _Period: Lifecycle in days. Value range: 1-3600 (3640 indicates permanent retention)
Note: This field may return `null`, indicating that no valid value was found.
        :type Period: int
        :param _SubAssumerName: Cloud product sub-identifier. If the log topic is created by another cloud product, this field returns the name of the cloud product and its log type, such as `TKE-Audit` or `TKE-Event`. Some products only return the cloud product identifier (`AssumerName`), without this field.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubAssumerName: str
        :param _Describes: Log topic description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describes: str
        :param _HotPeriod: The lifecycle of hot storage when log transitioning is enabled. The value of `hotPeriod` is smaller than that of `Period`.
The hot storage period is the value of `hotPeriod`, and the cold storage period is the value of `Period` minus the value of `hotPeriod`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HotPeriod: int
        """
        self._LogsetId = None
        self._TopicId = None
        self._TopicName = None
        self._PartitionCount = None
        self._Index = None
        self._AssumerName = None
        self._CreateTime = None
        self._Status = None
        self._Tags = None
        self._AutoSplit = None
        self._MaxSplitPartitions = None
        self._StorageType = None
        self._Period = None
        self._SubAssumerName = None
        self._Describes = None
        self._HotPeriod = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionCount(self):
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AssumerName(self):
        return self._AssumerName

    @AssumerName.setter
    def AssumerName(self, AssumerName):
        self._AssumerName = AssumerName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoSplit(self):
        return self._AutoSplit

    @AutoSplit.setter
    def AutoSplit(self, AutoSplit):
        self._AutoSplit = AutoSplit

    @property
    def MaxSplitPartitions(self):
        return self._MaxSplitPartitions

    @MaxSplitPartitions.setter
    def MaxSplitPartitions(self, MaxSplitPartitions):
        self._MaxSplitPartitions = MaxSplitPartitions

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SubAssumerName(self):
        return self._SubAssumerName

    @SubAssumerName.setter
    def SubAssumerName(self, SubAssumerName):
        self._SubAssumerName = SubAssumerName

    @property
    def Describes(self):
        return self._Describes

    @Describes.setter
    def Describes(self, Describes):
        self._Describes = Describes

    @property
    def HotPeriod(self):
        return self._HotPeriod

    @HotPeriod.setter
    def HotPeriod(self, HotPeriod):
        self._HotPeriod = HotPeriod


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._PartitionCount = params.get("PartitionCount")
        self._Index = params.get("Index")
        self._AssumerName = params.get("AssumerName")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoSplit = params.get("AutoSplit")
        self._MaxSplitPartitions = params.get("MaxSplitPartitions")
        self._StorageType = params.get("StorageType")
        self._Period = params.get("Period")
        self._SubAssumerName = params.get("SubAssumerName")
        self._Describes = params.get("Describes")
        self._HotPeriod = params.get("HotPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogRequest(AbstractModel):
    """UploadLog request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _HashKey: Topic partition where data will be written into by `HashKey` 
        :type HashKey: str
        :param _CompressType: Compression type
        :type CompressType: str
        """
        self._TopicId = None
        self._HashKey = None
        self._CompressType = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def HashKey(self):
        return self._HashKey

    @HashKey.setter
    def HashKey(self, HashKey):
        self._HashKey = HashKey

    @property
    def CompressType(self):
        return self._CompressType

    @CompressType.setter
    def CompressType(self, CompressType):
        self._CompressType = CompressType


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._HashKey = params.get("HashKey")
        self._CompressType = params.get("CompressType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogResponse(AbstractModel):
    """UploadLog response structure.

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


class ValueInfo(AbstractModel):
    """Index description information of the field for which key-value index needs to be enabled

    """

    def __init__(self):
        r"""
        :param _Type: Field type. Valid values: `long`, `text`, `double`
        :type Type: str
        :param _Tokenizer: Separator of fields. Each character represents a separator.
Only symbols, \n\t\r, and escape character \ are supported.
`long` and `double` fields need to be null.
Note: \n\t\r can be directly enclosed in double quotes as the input parameter without escaping. When debugging with API Explorer, use the JSON parameter input method to avoid repeated escaping of \n\t\r.
        :type Tokenizer: str
        :param _SqlFlag: Whether the analysis feature is enabled for the field
        :type SqlFlag: bool
        :param _ContainZH: Whether Chinese characters are contained. For `long` and `double` fields, set them to `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContainZH: bool
        """
        self._Type = None
        self._Tokenizer = None
        self._SqlFlag = None
        self._ContainZH = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def SqlFlag(self):
        return self._SqlFlag

    @SqlFlag.setter
    def SqlFlag(self, SqlFlag):
        self._SqlFlag = SqlFlag

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Tokenizer = params.get("Tokenizer")
        self._SqlFlag = params.get("SqlFlag")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallback(AbstractModel):
    """Callback address

    """

    def __init__(self):
        r"""
        :param _Url: Callback address
        :type Url: str
        :param _CallbackType: Callback type. Valid values:
<li> WeCom
<li> Http
        :type CallbackType: str
        :param _Method: Callback method. Valid values:
<li> POST
<li> PUT
Default value: `POST`. This parameter is required if `CallbackType` is `Http`.
Note: This field may return `null`, indicating that no valid value was found.
        :type Method: str
        :param _Headers: Request header
Note: This parameter is disused. To specify request headers, see `CallBack` in <a href="https://intl.cloud.tencent.com/document/product/614/56466?from_cn_redirect=1">CreateAlarmNotice</a>.
Note: This field may return `null`, indicating that no valid value was found.
        :type Headers: list of str
        :param _Body: Request content
Note: This parameter is disused. To specify request content, see `CallBack` in <a href="https://intl.cloud.tencent.com/document/product/614/56466?from_cn_redirect=1">CreateAlarmNotice</a>.
Note: This field may return `null`, indicating that no valid value was found.
        :type Body: str
        :param _Index: Number
        :type Index: int
        """
        self._Url = None
        self._CallbackType = None
        self._Method = None
        self._Headers = None
        self._Body = None
        self._Index = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CallbackType(self):
        return self._CallbackType

    @CallbackType.setter
    def CallbackType(self, CallbackType):
        self._CallbackType = CallbackType

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._CallbackType = params.get("CallbackType")
        self._Method = params.get("Method")
        self._Headers = params.get("Headers")
        self._Body = params.get("Body")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        