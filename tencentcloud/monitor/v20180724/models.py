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


class AlarmEvent(AbstractModel):
    """Alarm event

    """

    def __init__(self):
        r"""
        :param _EventName: Event name
        :type EventName: str
        :param _Description: Event display name
        :type Description: str
        :param _Namespace: Alarm policy type
        :type Namespace: str
        """
        self._EventName = None
        self._Description = None
        self._Namespace = None

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._Description = params.get("Description")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHierarchicalNotice(AbstractModel):
    """Notification template ID and the list of alarm notification levels. The values `Remind` and `Serious` indicate that the notification template only sends alarms at the `Remind` and `Serious` levels.

    """

    def __init__(self):
        r"""
        :param _NoticeId: Notification template ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoticeId: str
        :param _Classification: The list of alarm notification levels. The values `Remind` and `Serious` indicate that the notification template only sends alarms at the `Remind` and `Serious` levels.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Classification: list of str
        """
        self._NoticeId = None
        self._Classification = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def Classification(self):
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._Classification = params.get("Classification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHierarchicalValue(AbstractModel):
    """The configuration of alarm level threshold

    """

    def __init__(self):
        r"""
        :param _Remind: Threshold for the `Remind` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remind: str
        :param _Warn: Threshold for the `Warn` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warn: str
        :param _Serious: Threshold for the `Serious` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Serious: str
        """
        self._Remind = None
        self._Warn = None
        self._Serious = None

    @property
    def Remind(self):
        return self._Remind

    @Remind.setter
    def Remind(self, Remind):
        self._Remind = Remind

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Serious(self):
        return self._Serious

    @Serious.setter
    def Serious(self, Serious):
        self._Serious = Serious


    def _deserialize(self, params):
        self._Remind = params.get("Remind")
        self._Warn = params.get("Warn")
        self._Serious = params.get("Serious")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistory(AbstractModel):
    """Alarm record data

    """

    def __init__(self):
        r"""
        :param _AlarmId: Alarm record ID
        :type AlarmId: str
        :param _MonitorType: Monitor type
        :type MonitorType: str
        :param _Namespace: Policy type
        :type Namespace: str
        :param _AlarmObject: Alarm object
        :type AlarmObject: str
        :param _Content: Alarm content
        :type Content: str
        :param _FirstOccurTime: Timestamp of the first occurrence
        :type FirstOccurTime: int
        :param _LastOccurTime: Timestamp of the last occurrence
        :type LastOccurTime: int
        :param _AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data)
        :type AlarmStatus: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _VPC: VPC of alarm object for basic product alarm
        :type VPC: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _InstanceGroup: Instance group of alarm object
        :type InstanceGroup: list of InstanceGroups
        :param _ReceiverUids: Recipient list
        :type ReceiverUids: list of int
        :param _ReceiverGroups: Recipient group list
        :type ReceiverGroups: list of int
        :param _NoticeWays: Alarm channel list. Valid values: SMS (SMS), EMAIL (email), CALL (phone), WECHAT (WeChat)
        :type NoticeWays: list of str
        :param _OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy
        :type OriginId: str
        :param _AlarmType: Alarm type
        :type AlarmType: str
        :param _EventId: Event ID
        :type EventId: int
        :param _Region: Region
        :type Region: str
        :param _PolicyExists: Whether the policy exists. Valid values: 0 (no), 1 (yes)
        :type PolicyExists: int
        :param _MetricsInfo: Metric information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricsInfo: list of AlarmHistoryMetric
        :param _Dimensions: Dimension information of an instance that triggered alarms.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Dimensions: str
        """
        self._AlarmId = None
        self._MonitorType = None
        self._Namespace = None
        self._AlarmObject = None
        self._Content = None
        self._FirstOccurTime = None
        self._LastOccurTime = None
        self._AlarmStatus = None
        self._PolicyId = None
        self._PolicyName = None
        self._VPC = None
        self._ProjectId = None
        self._ProjectName = None
        self._InstanceGroup = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._NoticeWays = None
        self._OriginId = None
        self._AlarmType = None
        self._EventId = None
        self._Region = None
        self._PolicyExists = None
        self._MetricsInfo = None
        self._Dimensions = None

    @property
    def AlarmId(self):
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def AlarmObject(self):
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FirstOccurTime(self):
        return self._FirstOccurTime

    @FirstOccurTime.setter
    def FirstOccurTime(self, FirstOccurTime):
        self._FirstOccurTime = FirstOccurTime

    @property
    def LastOccurTime(self):
        return self._LastOccurTime

    @LastOccurTime.setter
    def LastOccurTime(self, LastOccurTime):
        self._LastOccurTime = LastOccurTime

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def VPC(self):
        return self._VPC

    @VPC.setter
    def VPC(self, VPC):
        self._VPC = VPC

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def NoticeWays(self):
        return self._NoticeWays

    @NoticeWays.setter
    def NoticeWays(self, NoticeWays):
        self._NoticeWays = NoticeWays

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PolicyExists(self):
        return self._PolicyExists

    @PolicyExists.setter
    def PolicyExists(self, PolicyExists):
        self._PolicyExists = PolicyExists

    @property
    def MetricsInfo(self):
        return self._MetricsInfo

    @MetricsInfo.setter
    def MetricsInfo(self, MetricsInfo):
        self._MetricsInfo = MetricsInfo

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._AlarmId = params.get("AlarmId")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        self._AlarmObject = params.get("AlarmObject")
        self._Content = params.get("Content")
        self._FirstOccurTime = params.get("FirstOccurTime")
        self._LastOccurTime = params.get("LastOccurTime")
        self._AlarmStatus = params.get("AlarmStatus")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._VPC = params.get("VPC")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroups()
                obj._deserialize(item)
                self._InstanceGroup.append(obj)
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._NoticeWays = params.get("NoticeWays")
        self._OriginId = params.get("OriginId")
        self._AlarmType = params.get("AlarmType")
        self._EventId = params.get("EventId")
        self._Region = params.get("Region")
        self._PolicyExists = params.get("PolicyExists")
        if params.get("MetricsInfo") is not None:
            self._MetricsInfo = []
            for item in params.get("MetricsInfo"):
                obj = AlarmHistoryMetric()
                obj._deserialize(item)
                self._MetricsInfo.append(obj)
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistoryMetric(AbstractModel):
    """Metric information of alarm records

    """

    def __init__(self):
        r"""
        :param _QceNamespace: Namespace used to query data by Tencent Cloud service monitoring type
        :type QceNamespace: str
        :param _MetricName: Metric name
        :type MetricName: str
        :param _Period: Statistical period
        :type Period: int
        :param _Value: Value triggering alarm
        :type Value: str
        :param _Description: Metric display name
        :type Description: str
        """
        self._QceNamespace = None
        self._MetricName = None
        self._Period = None
        self._Value = None
        self._Description = None

    @property
    def QceNamespace(self):
        return self._QceNamespace

    @QceNamespace.setter
    def QceNamespace(self, QceNamespace):
        self._QceNamespace = QceNamespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._QceNamespace = params.get("QceNamespace")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Value = params.get("Value")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """Alarm notification template details

    """

    def __init__(self):
        r"""
        :param _Id: Alarm notification template ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Name: Alarm notification template name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _UpdatedAt: Last modified time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _UpdatedBy: Last modified by
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedBy: str
        :param _NoticeType: Alarm notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeType: str
        :param _UserNotices: User notification list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserNotices: list of UserNotice
        :param _URLNotices: Callback notification list
Note: this field may return null, indicating that no valid values can be obtained.
        :type URLNotices: list of URLNotice
        :param _IsPreset: Whether it is the system default notification template. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsPreset: int
        :param _NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeLanguage: str
        :param _PolicyIds: List of IDs of the alarm policies bound to alarm notification template
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyIds: list of str
        :param _AMPConsumerId: Backend AMP consumer ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AMPConsumerId: str
        :param _CLSNotices: Channel to push alarm notifications to CLS.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CLSNotices: list of CLSNotice
        :param _Tags: Tags bound to a notification template
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._Id = None
        self._Name = None
        self._UpdatedAt = None
        self._UpdatedBy = None
        self._NoticeType = None
        self._UserNotices = None
        self._URLNotices = None
        self._IsPreset = None
        self._NoticeLanguage = None
        self._PolicyIds = None
        self._AMPConsumerId = None
        self._CLSNotices = None
        self._Tags = None

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
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def UpdatedBy(self):
        return self._UpdatedBy

    @UpdatedBy.setter
    def UpdatedBy(self, UpdatedBy):
        self._UpdatedBy = UpdatedBy

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def IsPreset(self):
        return self._IsPreset

    @IsPreset.setter
    def IsPreset(self, IsPreset):
        self._IsPreset = IsPreset

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def AMPConsumerId(self):
        return self._AMPConsumerId

    @AMPConsumerId.setter
    def AMPConsumerId(self, AMPConsumerId):
        self._AMPConsumerId = AMPConsumerId

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._UpdatedAt = params.get("UpdatedAt")
        self._UpdatedBy = params.get("UpdatedBy")
        self._NoticeType = params.get("NoticeType")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        self._IsPreset = params.get("IsPreset")
        self._NoticeLanguage = params.get("NoticeLanguage")
        self._PolicyIds = params.get("PolicyIds")
        self._AMPConsumerId = params.get("AMPConsumerId")
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
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
        


class AlarmPolicy(AbstractModel):
    """Alarm policy details

    """

    def __init__(self):
        r"""
        :param _PolicyId: Alarm policy ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyId: str
        :param _PolicyName: Alarm policy name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param _Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MonitorType: str
        :param _Enable: Status. Valid values: 0 (disabled), 1 (enabled)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Enable: int
        :param _UseSum: Number of instances bound to policy group
Note: this field may return null, indicating that no valid values can be obtained.
        :type UseSum: int
        :param _ProjectId: Project ID. Valid values: -1 (no project), 0 (default project)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param _Namespace: Alarm policy type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _ConditionTemplateId: Trigger condition template ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConditionTemplateId: str
        :param _Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _NoticeIds: Notification rule ID list
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeIds: list of str
        :param _Notices: Notification rule list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Notices: list of AlarmNotice
        :param _TriggerTasks: Triggered task list
Note: this field may return null, indicating that no valid values can be obtained.
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _ConditionsTemp: Template policy group
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.ConditionsTemp`
        :param _LastEditUin: `Uin` of the last modifying user
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastEditUin: str
        :param _UpdateTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: int
        :param _InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: int
        :param _Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: list of str
        :param _NamespaceShowName: Namespace display name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceShowName: str
        :param _IsDefault: Whether it is the default policy. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefault: int
        :param _CanSetDefault: Whether the default policy can be set. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.
        :type CanSetDefault: int
        :param _InstanceGroupId: Instance group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupId: int
        :param _InstanceSum: Total number of instances in instance group
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceSum: int
        :param _InstanceGroupName: Instance group name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupName: str
        :param _RuleType: Trigger condition type. Valid values: STATIC (static threshold), DYNAMIC (dynamic)
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _OriginId: Policy ID for instance/instance group binding and unbinding APIs (BindingPolicyObject, UnBindingAllPolicyObject, UnBindingPolicyObject)
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        :param _TagInstances: Tag
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagInstances: list of TagInstance
        :param _FilterDimensionsParam: Information on the filter dimension associated with a policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FilterDimensionsParam: str
        :param _IsOneClick: Whether it is a quick alarm policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOneClick: int
        :param _OneClickStatus: Whether the quick alarm policy is enabled.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OneClickStatus: int
        :param _AdvancedMetricNumber: The number of advanced metrics.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AdvancedMetricNumber: int
        :param _IsBindAll: Whether the policy is associated with all objects
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsBindAll: int
        :param _Tags: Policy tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Remark = None
        self._MonitorType = None
        self._Enable = None
        self._UseSum = None
        self._ProjectId = None
        self._ProjectName = None
        self._Namespace = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._NoticeIds = None
        self._Notices = None
        self._TriggerTasks = None
        self._ConditionsTemp = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._Region = None
        self._NamespaceShowName = None
        self._IsDefault = None
        self._CanSetDefault = None
        self._InstanceGroupId = None
        self._InstanceSum = None
        self._InstanceGroupName = None
        self._RuleType = None
        self._OriginId = None
        self._TagInstances = None
        self._FilterDimensionsParam = None
        self._IsOneClick = None
        self._OneClickStatus = None
        self._AdvancedMetricNumber = None
        self._IsBindAll = None
        self._Tags = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def UseSum(self):
        return self._UseSum

    @UseSum.setter
    def UseSum(self, UseSum):
        self._UseSum = UseSum

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def NamespaceShowName(self):
        return self._NamespaceShowName

    @NamespaceShowName.setter
    def NamespaceShowName(self, NamespaceShowName):
        self._NamespaceShowName = NamespaceShowName

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def InstanceGroupName(self):
        return self._InstanceGroupName

    @InstanceGroupName.setter
    def InstanceGroupName(self, InstanceGroupName):
        self._InstanceGroupName = InstanceGroupName

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def TagInstances(self):
        return self._TagInstances

    @TagInstances.setter
    def TagInstances(self, TagInstances):
        self._TagInstances = TagInstances

    @property
    def FilterDimensionsParam(self):
        return self._FilterDimensionsParam

    @FilterDimensionsParam.setter
    def FilterDimensionsParam(self, FilterDimensionsParam):
        self._FilterDimensionsParam = FilterDimensionsParam

    @property
    def IsOneClick(self):
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick

    @property
    def OneClickStatus(self):
        return self._OneClickStatus

    @OneClickStatus.setter
    def OneClickStatus(self, OneClickStatus):
        self._OneClickStatus = OneClickStatus

    @property
    def AdvancedMetricNumber(self):
        return self._AdvancedMetricNumber

    @AdvancedMetricNumber.setter
    def AdvancedMetricNumber(self, AdvancedMetricNumber):
        self._AdvancedMetricNumber = AdvancedMetricNumber

    @property
    def IsBindAll(self):
        return self._IsBindAll

    @IsBindAll.setter
    def IsBindAll(self, IsBindAll):
        self._IsBindAll = IsBindAll

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Remark = params.get("Remark")
        self._MonitorType = params.get("MonitorType")
        self._Enable = params.get("Enable")
        self._UseSum = params.get("UseSum")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Namespace = params.get("Namespace")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        self._NoticeIds = params.get("NoticeIds")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = ConditionsTemp()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._Region = params.get("Region")
        self._NamespaceShowName = params.get("NamespaceShowName")
        self._IsDefault = params.get("IsDefault")
        self._CanSetDefault = params.get("CanSetDefault")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceSum = params.get("InstanceSum")
        self._InstanceGroupName = params.get("InstanceGroupName")
        self._RuleType = params.get("RuleType")
        self._OriginId = params.get("OriginId")
        if params.get("TagInstances") is not None:
            self._TagInstances = []
            for item in params.get("TagInstances"):
                obj = TagInstance()
                obj._deserialize(item)
                self._TagInstances.append(obj)
        self._FilterDimensionsParam = params.get("FilterDimensionsParam")
        self._IsOneClick = params.get("IsOneClick")
        self._OneClickStatus = params.get("OneClickStatus")
        self._AdvancedMetricNumber = params.get("AdvancedMetricNumber")
        self._IsBindAll = params.get("IsBindAll")
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
        


class AlarmPolicyCondition(AbstractModel):
    """Metric trigger condition of alarm policy

    """

    def __init__(self):
        r"""
        :param _IsUnionRule: Judgment condition of an alarm trigger condition (`0`: Any; `1`: All; `2`: Composite). When the value is set to `2` (i.e., composite trigger conditions), this parameter should be used together with `ComplexExpression`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsUnionRule: int
        :param _Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of AlarmPolicyRule
        :param _ComplexExpression: The judgment expression of composite alarm trigger conditions, which is valid when the value of `IsUnionRule` is `2`. This parameter is used to determine that an alarm condition is met only when the expression values are `True` for multiple trigger conditions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComplexExpression: str
        """
        self._IsUnionRule = None
        self._Rules = None
        self._ComplexExpression = None

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ComplexExpression(self):
        return self._ComplexExpression

    @ComplexExpression.setter
    def ComplexExpression(self, ComplexExpression):
        self._ComplexExpression = ComplexExpression


    def _deserialize(self, params):
        self._IsUnionRule = params.get("IsUnionRule")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ComplexExpression = params.get("ComplexExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyEventCondition(AbstractModel):
    """Event trigger condition of alarm policy

    """

    def __init__(self):
        r"""
        :param _Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of AlarmPolicyRule
        """
        self._Rules = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyFilter(AbstractModel):
    """Filter condition of alarm policy

    """

    def __init__(self):
        r"""
        :param _Type: Filter condition type. Valid values: DIMENSION (uses dimensions for filtering)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Dimensions: JSON string generated by serializing the `AlarmPolicyDimension` two-dimensional array. The one-dimensional arrays are in OR relationship, and the elements in a one-dimensional array are in AND relationship
Note: this field may return null, indicating that no valid values can be obtained.
        :type Dimensions: str
        """
        self._Type = None
        self._Dimensions = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyRule(AbstractModel):
    """Trigger condition of alarm policy

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name or event name. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1) and the supported events via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MetricName: str
        :param _Period: Statistical period in seconds. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Period: int
        :param _Operator: Operator
intelligent = intelligent detection without threshold
eq = equal to
ge = greater than or equal to
gt = greater than
le = less than or equal to
lt = less than
ne = not equal to
day_increase = day-on-day increase
day_decrease = day-on-day decrease
day_wave = day-on-day fluctuation
week_increase = week-on-week increase
week_decrease = week-on-week decrease
week_wave = week-on-week fluctuation
cycle_increase = cyclical increase
cycle_decrease = cyclical decrease
cycle_wave = cyclical fluctuation
re = regex match
The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Operator: str
        :param _Value: Threshold. The valid value range can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Value: str
        :param _ContinuePeriod: Number of periods. `1`: continue for one period; `2`: continue for two periods; and so on. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ContinuePeriod: int
        :param _NoticeFrequency: Alarm interval in seconds. Valid values: 0 (do not repeat), 300 (alarm once every 5 minutes), 600 (alarm once every 10 minutes), 900 (alarm once every 15 minutes), 1800 (alarm once every 30 minutes), 3600 (alarm once every hour), 7200 (alarm once every 2 hours), 10800 (alarm once every 3 hours), 21600 (alarm once every 6 hours),  43200 (alarm once every 12 hours), 86400 (alarm once every day)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeFrequency: int
        :param _IsPowerNotice: Whether the alarm frequency increases exponentially. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsPowerNotice: int
        :param _Filter: Filter condition for one single trigger rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _Description: Metric display name, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Unit: Unit, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param _RuleType: Trigger condition type. `STATIC`: static threshold; `dynamic`: dynamic threshold. If you do not specify this parameter when creating or editing a policy, `STATIC` is used by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleType: str
        :param _IsAdvanced: Whether it is an advanced metric. 0: No; 1: Yes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsAdvanced: int
        :param _IsOpen: Whether the advanced metric feature is enabled. 0: No; 1: Yes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOpen: int
        :param _ProductId: Integration center product ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProductId: str
        :param _ValueMax: Maximum value
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValueMax: float
        :param _ValueMin: Minimum value
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValueMin: float
        :param _HierarchicalValue: The configuration of alarm level threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type HierarchicalValue: :class:`tencentcloud.monitor.v20180724.models.AlarmHierarchicalValue`
        """
        self._MetricName = None
        self._Period = None
        self._Operator = None
        self._Value = None
        self._ContinuePeriod = None
        self._NoticeFrequency = None
        self._IsPowerNotice = None
        self._Filter = None
        self._Description = None
        self._Unit = None
        self._RuleType = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None
        self._ValueMax = None
        self._ValueMin = None
        self._HierarchicalValue = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def NoticeFrequency(self):
        return self._NoticeFrequency

    @NoticeFrequency.setter
    def NoticeFrequency(self, NoticeFrequency):
        self._NoticeFrequency = NoticeFrequency

    @property
    def IsPowerNotice(self):
        return self._IsPowerNotice

    @IsPowerNotice.setter
    def IsPowerNotice(self, IsPowerNotice):
        self._IsPowerNotice = IsPowerNotice

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ValueMax(self):
        return self._ValueMax

    @ValueMax.setter
    def ValueMax(self, ValueMax):
        self._ValueMax = ValueMax

    @property
    def ValueMin(self):
        return self._ValueMin

    @ValueMin.setter
    def ValueMin(self, ValueMin):
        self._ValueMin = ValueMin

    @property
    def HierarchicalValue(self):
        return self._HierarchicalValue

    @HierarchicalValue.setter
    def HierarchicalValue(self, HierarchicalValue):
        self._HierarchicalValue = HierarchicalValue


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._NoticeFrequency = params.get("NoticeFrequency")
        self._IsPowerNotice = params.get("IsPowerNotice")
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Description = params.get("Description")
        self._Unit = params.get("Unit")
        self._RuleType = params.get("RuleType")
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        self._ValueMax = params.get("ValueMax")
        self._ValueMin = params.get("ValueMin")
        if params.get("HierarchicalValue") is not None:
            self._HierarchicalValue = AlarmHierarchicalValue()
            self._HierarchicalValue._deserialize(params.get("HierarchicalValue"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyTriggerTask(AbstractModel):
    """Task triggered by alarm policy

    """

    def __init__(self):
        r"""
        :param _Type: Triggered task type. Valid value: AS (auto scaling)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _TaskConfig: Configuration information in JSON format, such as {"Key1":"Value1","Key2":"Value2"}
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskConfig: str
        """
        self._Type = None
        self._TaskConfig = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskConfig(self):
        return self._TaskConfig

    @TaskConfig.setter
    def TaskConfig(self, TaskConfig):
        self._TaskConfig = TaskConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TaskConfig = params.get("TaskConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPrometheusManagedGrafanaRequest(AbstractModel):
    """BindPrometheusManagedGrafana request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _GrafanaId: Grafana instance ID
        :type GrafanaId: str
        """
        self._InstanceId = None
        self._GrafanaId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GrafanaId(self):
        return self._GrafanaId

    @GrafanaId.setter
    def GrafanaId(self, GrafanaId):
        self._GrafanaId = GrafanaId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPrometheusManagedGrafanaResponse(AbstractModel):
    """BindPrometheusManagedGrafana response structure.

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


class BindingPolicyObjectDimension(AbstractModel):
    """Dimensions of instances bound to a policy

    """

    def __init__(self):
        r"""
        :param _Region: Region name.
        :type Region: str
        :param _RegionId: Region ID.
        :type RegionId: int
        :param _Dimensions: Instance dimension information in the following format:
{"unInstanceId":"ins-00jvv9mo"}. The dimension information varies by Tencent Cloud services. For more information, please see:
[Dimension List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)
        :type Dimensions: str
        :param _EventDimensions: Event dimensions.
        :type EventDimensions: str
        """
        self._Region = None
        self._RegionId = None
        self._Dimensions = None
        self._EventDimensions = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EventDimensions(self):
        return self._EventDimensions

    @EventDimensions.setter
    def EventDimensions(self, EventDimensions):
        self._EventDimensions = EventDimensions


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._Dimensions = params.get("Dimensions")
        self._EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Required. The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID, such as `4739573`. This parameter will be disused soon. Another parameter `PolicyId` is recommended.
        :type GroupId: int
        :param _PolicyId: Alarm policy ID, such as `policy-gh892hg0`. At least one of the two parameters, `PolicyId` and `GroupId`, must be specified; otherwise, an error will be reported. `PolicyId` is preferred over `GroupId` when both of them are specified.
        :type PolicyId: str
        :param _InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param _Dimensions: Dimensions of an object to be bound.
        :type Dimensions: list of BindingPolicyObjectDimension
        :param _EbSubject: The alert configured for an event
        :type EbSubject: str
        :param _EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._InstanceGroupId = None
        self._Dimensions = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject response structure.

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


class CLSNotice(AbstractModel):
    """The operation of pushing alarm notifications to CLS

    """

    def __init__(self):
        r"""
        :param _Region: Region.
        :type Region: str
        :param _LogSetId: Logset ID.
        :type LogSetId: str
        :param _TopicId: Topic ID.
        :type TopicId: str
        :param _Enable: Status. Valid values: `0` (disabled), `1` (enabled). Default value: `1` (enabled). This parameter can be left empty.
        :type Enable: int
        """
        self._Region = None
        self._LogSetId = None
        self._TopicId = None
        self._Enable = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._LogSetId = params.get("LogSetId")
        self._TopicId = params.get("TopicId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIsPrometheusNewUserRequest(AbstractModel):
    """CheckIsPrometheusNewUser request structure.

    """


class CheckIsPrometheusNewUserResponse(AbstractModel):
    """CheckIsPrometheusNewUser response structure.

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


class CleanGrafanaInstanceRequest(AbstractModel):
    """CleanGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanGrafanaInstanceResponse(AbstractModel):
    """CleanGrafanaInstance response structure.

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


class CommonNamespace(AbstractModel):
    """Unified namespace information

    """

    def __init__(self):
        r"""
        :param _Id: Namespace ID
        :type Id: str
        :param _Name: Namespace name
        :type Name: str
        :param _Value: Namespace value
        :type Value: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _Config: Configuration information
        :type Config: str
        :param _AvailableRegions: List of supported regions
        :type AvailableRegions: list of str
        :param _SortId: Sort ID
        :type SortId: int
        :param _DashboardId: Unique ID in Dashboard
        :type DashboardId: str
        """
        self._Id = None
        self._Name = None
        self._Value = None
        self._ProductName = None
        self._Config = None
        self._AvailableRegions = None
        self._SortId = None
        self._DashboardId = None

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
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def AvailableRegions(self):
        return self._AvailableRegions

    @AvailableRegions.setter
    def AvailableRegions(self, AvailableRegions):
        self._AvailableRegions = AvailableRegions

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def DashboardId(self):
        return self._DashboardId

    @DashboardId.setter
    def DashboardId(self, DashboardId):
        self._DashboardId = DashboardId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._ProductName = params.get("ProductName")
        self._Config = params.get("Config")
        self._AvailableRegions = params.get("AvailableRegions")
        self._SortId = params.get("SortId")
        self._DashboardId = params.get("DashboardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonNamespaceNew(AbstractModel):
    """Policy type information

    """

    def __init__(self):
        r"""
        :param _Id: Namespace ID
        :type Id: str
        :param _Name: Namespace name
        :type Name: str
        :param _MonitorType: Monitoring type
        :type MonitorType: str
        :param _Dimensions: Dimension information
        :type Dimensions: list of DimensionNew
        """
        self._Id = None
        self._Name = None
        self._MonitorType = None
        self._Dimensions = None

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
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MonitorType = params.get("MonitorType")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionNew()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Condition(AbstractModel):
    """Alarm condition

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyPeriod: Alarm notification frequency.
        :type AlarmNotifyPeriod: int
        :param _AlarmNotifyType: Predefined repeated notification policy. `0`: One-time alarm; `1`: exponential alarm; `2`: consecutive alarm.
        :type AlarmNotifyType: int
        :param _CalcType: Detection method.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CalcType: str
        :param _CalcValue: Detection value.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CalcValue: str
        :param _ContinueTime: Duration in seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContinueTime: str
        :param _MetricID: Metric ID.
        :type MetricID: int
        :param _MetricDisplayName: Displayed metric name.
        :type MetricDisplayName: str
        :param _Period: Statistical period.
        :type Period: int
        :param _RuleID: Rule ID.
        :type RuleID: int
        :param _Unit: Metric unit.
        :type Unit: str
        :param _IsAdvanced: Whether it is an advanced metric. Valid values: `0` (no), `1` (yes).
        :type IsAdvanced: int
        :param _IsOpen: Whether the advance metric feature is enabled. Valid values: `0` (no), `1` (yes).
        :type IsOpen: int
        :param _ProductId: Product ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductId: str
        """
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._MetricID = None
        self._MetricDisplayName = None
        self._Period = None
        self._RuleID = None
        self._Unit = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def MetricID(self):
        return self._MetricID

    @MetricID.setter
    def MetricID(self, MetricID):
        self._MetricID = MetricID

    @property
    def MetricDisplayName(self):
        return self._MetricDisplayName

    @MetricDisplayName.setter
    def MetricDisplayName(self, MetricDisplayName):
        self._MetricDisplayName = MetricDisplayName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._ContinueTime = params.get("ContinueTime")
        self._MetricID = params.get("MetricID")
        self._MetricDisplayName = params.get("MetricDisplayName")
        self._Period = params.get("Period")
        self._RuleID = params.get("RuleID")
        self._Unit = params.get("Unit")
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionsTemp(AbstractModel):
    """Alarm condition template

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TemplateName: str
        :param _Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        """
        self._TemplateName = None
        self._Condition = None
        self._EventCondition = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
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
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _Name: Notification template name, which can contain up to 60 characters
        :type Name: str
        :param _NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
        :type NoticeType: str
        :param _NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
        :type NoticeLanguage: str
        :param _UserNotices: User notifications (up to 5)
        :type UserNotices: list of UserNotice
        :param _URLNotices: Callback notifications (up to 3)
        :type URLNotices: list of URLNotice
        :param _CLSNotices: The operation of pushing alarm notifications to CLS. Up to one CLS log topic can be configured.
        :type CLSNotices: list of CLSNotice
        :param _Tags: Tags bound to a template
        :type Tags: list of Tag
        """
        self._Module = None
        self._Name = None
        self._NoticeType = None
        self._NoticeLanguage = None
        self._UserNotices = None
        self._URLNotices = None
        self._CLSNotices = None
        self._Tags = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Name = params.get("Name")
        self._NoticeType = params.get("NoticeType")
        self._NoticeLanguage = params.get("NoticeLanguage")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
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
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice response structure.

    """

    def __init__(self):
        r"""
        :param _NoticeId: Alarm notification template ID
        :type NoticeId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NoticeId = None
        self._RequestId = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._RequestId = params.get("RequestId")


class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _PolicyName: Policy name, which can contain up to 20 characters
        :type PolicyName: str
        :param _MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorType: str
        :param _Namespace: Type of alarm policy, which can be obtained via [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1). For the monitoring of Tencent Cloud services, the value of this parameter is `QceNamespacesNew.N.Id` of the output parameter of `DescribeAllNamespaces`, for example, `cvm_device`.
        :type Namespace: str
        :param _Remark: Remarks with up to 100 letters, digits, underscores, and hyphens
        :type Remark: str
        :param _Enable: Whether to enable. Valid values: 0 (no), 1 (yes). Default value: 1. This parameter can be left empty
        :type Enable: int
        :param _ProjectId: Project ID. For products with different projects, a value other than `-1` must be passed in. `-1`: no project; `0`: default project. If no value is passed in, `-1` will be used. The supported project IDs can be viewed on the [**Account Center** > **Project Management**](https://console.cloud.tencent.com/project) page of the console.
        :type ProjectId: int
        :param _ConditionTemplateId: Trigger condition template ID. Pass in this parameter if the policy is associated with the trigger condition template; otherwise, pass in the `Condition` parameter. The trigger condition template ID can be obtained via [`DescribeConditionsTemplateList`](https://intl.cloud.tencent.com/document/api/248/70250?from_cn_redirect=1).
        :type ConditionTemplateId: int
        :param _Condition: Metric trigger condition. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: Event trigger condition. The supported events can be queried via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _NoticeIds: List of notification rule IDs, which can be obtained via [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1)
        :type NoticeIds: list of str
        :param _TriggerTasks: Triggered task list
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _Filter: Global filter.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.
        :type GroupBy: list of str
        :param _Tags: Tags bound to a template
        :type Tags: list of Tag
        :param _LogAlarmReqInfo: Log alarm information
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param _HierarchicalNotices: Notification rules for different alarm levels
        :type HierarchicalNotices: list of AlarmHierarchicalNotice
        :param _MigrateFlag: A dedicated field for migration policies. 0: Implement authentication logic; 1: Skip authentication logic.
        :type MigrateFlag: int
        :param _EbSubject: The alert configured for an event
        :type EbSubject: str
        """
        self._Module = None
        self._PolicyName = None
        self._MonitorType = None
        self._Namespace = None
        self._Remark = None
        self._Enable = None
        self._ProjectId = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._NoticeIds = None
        self._TriggerTasks = None
        self._Filter = None
        self._GroupBy = None
        self._Tags = None
        self._LogAlarmReqInfo = None
        self._HierarchicalNotices = None
        self._MigrateFlag = None
        self._EbSubject = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LogAlarmReqInfo(self):
        return self._LogAlarmReqInfo

    @LogAlarmReqInfo.setter
    def LogAlarmReqInfo(self, LogAlarmReqInfo):
        self._LogAlarmReqInfo = LogAlarmReqInfo

    @property
    def HierarchicalNotices(self):
        return self._HierarchicalNotices

    @HierarchicalNotices.setter
    def HierarchicalNotices(self, HierarchicalNotices):
        self._HierarchicalNotices = HierarchicalNotices

    @property
    def MigrateFlag(self):
        return self._MigrateFlag

    @MigrateFlag.setter
    def MigrateFlag(self, MigrateFlag):
        self._MigrateFlag = MigrateFlag

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyName = params.get("PolicyName")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        self._Remark = params.get("Remark")
        self._Enable = params.get("Enable")
        self._ProjectId = params.get("ProjectId")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        self._NoticeIds = params.get("NoticeIds")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._GroupBy = params.get("GroupBy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("LogAlarmReqInfo") is not None:
            self._LogAlarmReqInfo = LogAlarmReq()
            self._LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        if params.get("HierarchicalNotices") is not None:
            self._HierarchicalNotices = []
            for item in params.get("HierarchicalNotices"):
                obj = AlarmHierarchicalNotice()
                obj._deserialize(item)
                self._HierarchicalNotices.append(obj)
        self._MigrateFlag = params.get("MigrateFlag")
        self._EbSubject = params.get("EbSubject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmPolicyResponse(AbstractModel):
    """CreateAlarmPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy
        :type OriginId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._OriginId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class CreateAlertRuleRequest(AbstractModel):
    """CreateAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param _RuleName: Rule name
        :type RuleName: str
        :param _Expr: Alerting rule expression. For more information, see <a href="https://www.tencentcloud.com/document/product/1116/43192?lang=en&pg=">Alerting Rule Description</a>
        :type Expr: str
        :param _Receivers: List of alert notification template IDs
        :type Receivers: list of str
        :param _RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _Duration: Rule alert duration
        :type Duration: str
        :param _Labels: List of tags
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: List of annotations.

Alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively.
        :type Annotations: list of PrometheusRuleKV
        :param _Type: Alerting rule template category
        :type Type: str
        """
        self._InstanceId = None
        self._RuleName = None
        self._Expr = None
        self._Receivers = None
        self._RuleState = None
        self._Duration = None
        self._Labels = None
        self._Annotations = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RuleName = params.get("RuleName")
        self._Expr = params.get("Expr")
        self._Receivers = params.get("Receivers")
        self._RuleState = params.get("RuleState")
        self._Duration = params.get("Duration")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertRuleResponse(AbstractModel):
    """CreateAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateExporterIntegrationRequest(AbstractModel):
    """CreateExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Kind: Type
        :type Kind: str
        :param _Content: Integrated configuration
        :type Content: str
        :param _KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Content = None
        self._KubeType = None
        self._ClusterId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExporterIntegrationResponse(AbstractModel):
    """CreateExporterIntegration response structure.

    """

    def __init__(self):
        r"""
        :param _Names: The list of successfully created integrations.
        :type Names: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Names = None
        self._RequestId = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Names = params.get("Names")
        self._RequestId = params.get("RequestId")


class CreateGrafanaInstanceRequest(AbstractModel):
    """CreateGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param _GrafanaInitPassword: Initial Grafana password
        :type GrafanaInitPassword: str
        :param _EnableInternet: Whether to enable public network access
        :type EnableInternet: bool
        :param _TagSpecification: Tag
        :type TagSpecification: list of PrometheusTag
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetIds = None
        self._GrafanaInitPassword = None
        self._EnableInternet = None
        self._TagSpecification = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def GrafanaInitPassword(self):
        return self._GrafanaInitPassword

    @GrafanaInitPassword.setter
    def GrafanaInitPassword(self, GrafanaInitPassword):
        self._GrafanaInitPassword = GrafanaInitPassword

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._GrafanaInitPassword = params.get("GrafanaInitPassword")
        self._EnableInternet = params.get("EnableInternet")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaInstanceResponse(AbstractModel):
    """CreateGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateGrafanaIntegrationRequest(AbstractModel):
    """CreateGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _Kind: Integration type, such as “tencent-cloud-prometheus”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type Kind: str
        :param _Content: Integration configuration
        :type Content: str
        """
        self._InstanceId = None
        self._Kind = None
        self._Content = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaIntegrationResponse(AbstractModel):
    """CreateGrafanaIntegration response structure.

    """

    def __init__(self):
        r"""
        :param _IntegrationId: Integration ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntegrationId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IntegrationId = None
        self._RequestId = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._RequestId = params.get("RequestId")


class CreateGrafanaNotificationChannelRequest(AbstractModel):
    """CreateGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param _OrgId: Default value: `1`. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type OrgId: int
        :param _Receivers: Array of notification channel IDs
        :type Receivers: list of str
        :param _ExtraOrgIds: Array of extra organization IDs. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type ExtraOrgIds: list of str
        :param _OrganizationIds: Array of all valid organization IDs. Default value: `1`.
        :type OrganizationIds: list of str
        """
        self._InstanceId = None
        self._ChannelName = None
        self._OrgId = None
        self._Receivers = None
        self._ExtraOrgIds = None
        self._OrganizationIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ChannelName = params.get("ChannelName")
        self._OrgId = params.get("OrgId")
        self._Receivers = params.get("Receivers")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaNotificationChannelResponse(AbstractModel):
    """CreateGrafanaNotificationChannel response structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ChannelId = None
        self._RequestId = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """Alarm threshold condition passed in when a policy is created.

    """

    def __init__(self):
        r"""
        :param _MetricId: Metric ID.
        :type MetricId: int
        :param _AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param _CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. This parameter is optional if a default comparative type is configured for the metric.
        :type CalcType: int
        :param _CalcValue: Comparative value. This parameter is optional if the metric has no requirement.
        :type CalcValue: float
        :param _CalcPeriod: Data aggregation period in seconds. This parameter is optional if the metric has a default value.
        :type CalcPeriod: int
        :param _ContinuePeriod: Number of consecutive periods after which an alarm will be triggered.
        :type ContinuePeriod: int
        :param _RuleId: If a metric is created based on a template, the `RuleId` of the metric in the template must be passed in.
        :type RuleId: int
        """
        self._MetricId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._CalcType = None
        self._CalcValue = None
        self._CalcPeriod = None
        self._ContinuePeriod = None
        self._RuleId = None

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def CalcPeriod(self):
        return self._CalcPeriod

    @CalcPeriod.setter
    def CalcPeriod(self, CalcPeriod):
        self._CalcPeriod = CalcPeriod

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._MetricId = params.get("MetricId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._CalcPeriod = params.get("CalcPeriod")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupEventCondition(AbstractModel):
    """Event alarm condition passed in when a policy is created.

    """

    def __init__(self):
        r"""
        :param _EventId: Alarm event ID.
        :type EventId: int
        :param _AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param _RuleId: If a metric is created based on a template, the `RuleId` of the metric in the template must be passed in.
        :type RuleId: int
        """
        self._EventId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Policy group name.
        :type GroupName: str
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _ViewName: Name of the view to which the policy group belongs. If the policy group is created based on a template, this parameter is optional.
        :type ViewName: str
        :param _ProjectId: ID of the project to which the policy group belongs, which will be used for authentication.
        :type ProjectId: int
        :param _ConditionTempGroupId: ID of a template-based policy group. This parameter is required only when the policy group is created based on a template.
        :type ConditionTempGroupId: int
        :param _IsShielded: Whether the policy group is shielded. The value 0 indicates that the policy group is not shielded. The value 1 indicates that the policy group is shielded. The default value is 0.
        :type IsShielded: int
        :param _Remark: Remarks of the policy group.
        :type Remark: str
        :param _InsertTime: Insertion time in the format of Unix timestamp. If this parameter is not configured, the backend processing time is used.
        :type InsertTime: int
        :param _Conditions: Alarm threshold rules in the policy group.
        :type Conditions: list of CreatePolicyGroupCondition
        :param _EventConditions: Event alarm rules in the policy group.
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param _BackEndCall: Whether it is a backend call. Rules pulled from the policy template will be used to fill in the `Conditions` and `EventConditions` fields only when the value of this parameter is `1`.
        :type BackEndCall: int
        :param _IsUnionRule: The 'AND' and 'OR' rules for alarm metrics. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met.
        :type IsUnionRule: int
        """
        self._GroupName = None
        self._Module = None
        self._ViewName = None
        self._ProjectId = None
        self._ConditionTempGroupId = None
        self._IsShielded = None
        self._Remark = None
        self._InsertTime = None
        self._Conditions = None
        self._EventConditions = None
        self._BackEndCall = None
        self._IsUnionRule = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId

    @property
    def IsShielded(self):
        return self._IsShielded

    @IsShielded.setter
    def IsShielded(self, IsShielded):
        self._IsShielded = IsShielded

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def BackEndCall(self):
        return self._BackEndCall

    @BackEndCall.setter
    def BackEndCall(self, BackEndCall):
        self._BackEndCall = BackEndCall

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Module = params.get("Module")
        self._ViewName = params.get("ViewName")
        self._ProjectId = params.get("ProjectId")
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        self._IsShielded = params.get("IsShielded")
        self._Remark = params.get("Remark")
        self._InsertTime = params.get("InsertTime")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = CreatePolicyGroupCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = CreatePolicyGroupEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        self._BackEndCall = params.get("BackEndCall")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the created policy group.
        :type GroupId: int
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


class CreatePrometheusAgentRequest(AbstractModel):
    """CreatePrometheusAgent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Agent name
        :type Name: str
        """
        self._InstanceId = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAgentResponse(AbstractModel):
    """CreatePrometheusAgent response structure.

    """

    def __init__(self):
        r"""
        :param _AgentId: ID of a successfully created agent.
        :type AgentId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusAlertPolicyRequest(AbstractModel):
    """CreatePrometheusAlertPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertRule: Alert configuration
        :type AlertRule: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertPolicyItem`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertPolicyItem()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertPolicyResponse(AbstractModel):
    """CreatePrometheusAlertPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Alerting rule ID
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


class CreatePrometheusClusterAgentRequest(AbstractModel):
    """CreatePrometheusClusterAgent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Agents: Agent list
        :type Agents: list of PrometheusClusterAgentBasic
        """
        self._InstanceId = None
        self._Agents = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusClusterAgentBasic()
                obj._deserialize(item)
                self._Agents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusClusterAgentResponse(AbstractModel):
    """CreatePrometheusClusterAgent response structure.

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


class CreatePrometheusConfigRequest(AbstractModel):
    """CreatePrometheusConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ServiceMonitors: Configuration of service monitors
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: Configuration of pod monitors
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: Configuration of Prometheus raw job
        :type RawJobs: list of PrometheusConfigItem
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusConfigResponse(AbstractModel):
    """CreatePrometheusConfig response structure.

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


class CreatePrometheusGlobalNotificationRequest(AbstractModel):
    """CreatePrometheusGlobalNotification request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Notification: Alert notification channel
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        """
        self._InstanceId = None
        self._Notification = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusGlobalNotificationResponse(AbstractModel):
    """CreatePrometheusGlobalNotification response structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of the global alert notification channel
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


class CreatePrometheusMultiTenantInstancePostPayModeRequest(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _DataRetentionTime: Data retention period in days. Valid values: 15, 30, 45.
        :type DataRetentionTime: int
        :param _Zone: AZ
        :type Zone: str
        :param _TagSpecification: Instance tag
        :type TagSpecification: list of PrometheusTag
        :param _GrafanaInstanceId: The Grafana instance to be associated
        :type GrafanaInstanceId: str
        """
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._DataRetentionTime = None
        self._Zone = None
        self._TagSpecification = None
        self._GrafanaInstanceId = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def GrafanaInstanceId(self):
        return self._GrafanaInstanceId

    @GrafanaInstanceId.setter
    def GrafanaInstanceId(self, GrafanaInstanceId):
        self._GrafanaInstanceId = GrafanaInstanceId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._GrafanaInstanceId = params.get("GrafanaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusMultiTenantInstancePostPayModeResponse(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusRecordRuleYamlRequest(AbstractModel):
    """CreatePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Content: YAML content
        :type Content: str
        :param _Name: Rule name
        :type Name: str
        """
        self._InstanceId = None
        self._Content = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Content = params.get("Content")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusRecordRuleYamlResponse(AbstractModel):
    """CreatePrometheusRecordRuleYaml response structure.

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


class CreatePrometheusScrapeJobRequest(AbstractModel):
    """CreatePrometheusScrapeJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param _AgentId: Agent ID, such as “agent-abcd1234”. It can be obtained on the **Agent Management** page in the console.
        :type AgentId: str
        :param _Config: Scrape task ID in the format of “job_name:xx”
        :type Config: str
        """
        self._InstanceId = None
        self._AgentId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusScrapeJobResponse(AbstractModel):
    """CreatePrometheusScrapeJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: ID of a successfully created scrape task.
        :type JobId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreatePrometheusTempRequest(AbstractModel):
    """CreatePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param _Template: Template settings
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTemp`
        """
        self._Template = None

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self._Template = PrometheusTemp()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTempResponse(AbstractModel):
    """CreatePrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class CreateRecordingRuleRequest(AbstractModel):
    """CreateRecordingRule request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Recording rule name
        :type Name: str
        :param _Group: Recording rule group content in YAML format
        :type Group: str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self._Name = None
        self._Group = None
        self._InstanceId = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordingRuleResponse(AbstractModel):
    """CreateRecordingRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateSSOAccountRequest(AbstractModel):
    """CreateSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _UserId: User account ID, such as “10000000”.
        :type UserId: str
        :param _Role: Permission
        :type Role: list of GrafanaAccountRole
        :param _Notes: Remarks
        :type Notes: str
        """
        self._InstanceId = None
        self._UserId = None
        self._Role = None
        self._Notes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSOAccountResponse(AbstractModel):
    """CreateSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param _UserId: The added user UIN
        :type UserId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class CreateServiceDiscoveryRequest(AbstractModel):
    """CreateServiceDiscovery request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _KubeClusterId: <li>TKE: ID of the integrated TKE cluster</li>
        :type KubeClusterId: str
        :param _KubeType: Kubernetes cluster type:
<li> 1 = TKE </li>
        :type KubeType: int
        :param _Type: Scrape configuration type. Valid values:
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param _Yaml: Scrape configuration information
        :type Yaml: str
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None
        self._Type = None
        self._Yaml = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        self._Type = params.get("Type")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceDiscoveryResponse(AbstractModel):
    """CreateServiceDiscovery response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceDiscovery: The scrape configuration information returned after successful creation
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceDiscovery = None
        self._RequestId = None

    @property
    def ServiceDiscovery(self):
        return self._ServiceDiscovery

    @ServiceDiscovery.setter
    def ServiceDiscovery(self, ServiceDiscovery):
        self._ServiceDiscovery = ServiceDiscovery

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self._ServiceDiscovery = ServiceDiscoveryItem()
            self._ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self._RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        r"""
        :param _Dimensions: Combination of instance object dimensions
        :type Dimensions: list of Dimension
        :param _Timestamps: The array of timestamps indicating at which points in time there is data. Missing timestamps have no data points (i.e., missed)
        :type Timestamps: list of float
        :param _Values: The array of monitoring values, which is in one-to-one correspondence to Timestamps
        :type Values: list of float
        """
        self._Dimensions = None
        self._Timestamps = None
        self._Values = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Timestamps(self):
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesRequest(AbstractModel):
    """DeleteAlarmNotices request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _NoticeIds: Alarm notification template ID list
        :type NoticeIds: list of str
        :param _NoticeBindPolicys: Binding between a notification template and a policy
        :type NoticeBindPolicys: list of NoticeBindPolicys
        """
        self._Module = None
        self._NoticeIds = None
        self._NoticeBindPolicys = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def NoticeBindPolicys(self):
        return self._NoticeBindPolicys

    @NoticeBindPolicys.setter
    def NoticeBindPolicys(self, NoticeBindPolicys):
        self._NoticeBindPolicys = NoticeBindPolicys


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._NoticeIds = params.get("NoticeIds")
        if params.get("NoticeBindPolicys") is not None:
            self._NoticeBindPolicys = []
            for item in params.get("NoticeBindPolicys"):
                obj = NoticeBindPolicys()
                obj._deserialize(item)
                self._NoticeBindPolicys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesResponse(AbstractModel):
    """DeleteAlarmNotices response structure.

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


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param _PolicyIds: Alarm policy ID list
        :type PolicyIds: list of str
        """
        self._Module = None
        self._PolicyIds = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmPolicyResponse(AbstractModel):
    """DeleteAlarmPolicy response structure.

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


class DeleteAlertRulesRequest(AbstractModel):
    """DeleteAlertRules request structure.

    """

    def __init__(self):
        r"""
        :param _RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        """
        self._RuleIds = None
        self._InstanceId = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertRulesResponse(AbstractModel):
    """DeleteAlertRules response structure.

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


class DeleteExporterIntegrationRequest(AbstractModel):
    """DeleteExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Kind: Type
        :type Kind: str
        :param _Name: Name
        :type Name: str
        """
        self._InstanceId = None
        self._KubeType = None
        self._ClusterId = None
        self._Kind = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExporterIntegrationResponse(AbstractModel):
    """DeleteExporterIntegration response structure.

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


class DeleteGrafanaInstanceRequest(AbstractModel):
    """DeleteGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIDs: Array of instance names
        :type InstanceIDs: list of str
        """
        self._InstanceIDs = None

    @property
    def InstanceIDs(self):
        return self._InstanceIDs

    @InstanceIDs.setter
    def InstanceIDs(self, InstanceIDs):
        self._InstanceIDs = InstanceIDs


    def _deserialize(self, params):
        self._InstanceIDs = params.get("InstanceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaInstanceResponse(AbstractModel):
    """DeleteGrafanaInstance response structure.

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


class DeleteGrafanaIntegrationRequest(AbstractModel):
    """DeleteGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _IntegrationId: Integration ID, such as “integration-abcd1234”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type IntegrationId: str
        """
        self._InstanceId = None
        self._IntegrationId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationId = params.get("IntegrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaIntegrationResponse(AbstractModel):
    """DeleteGrafanaIntegration response structure.

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


class DeleteGrafanaNotificationChannelRequest(AbstractModel):
    """DeleteGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelIDs: Array of channel IDs, such as “nchannel-abcd1234”.
        :type ChannelIDs: list of str
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._ChannelIDs = None
        self._InstanceId = None

    @property
    def ChannelIDs(self):
        return self._ChannelIDs

    @ChannelIDs.setter
    def ChannelIDs(self, ChannelIDs):
        self._ChannelIDs = ChannelIDs

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ChannelIDs = params.get("ChannelIDs")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaNotificationChannelResponse(AbstractModel):
    """DeleteGrafanaNotificationChannel response structure.

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


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID.
        :type GroupId: list of int
        """
        self._Module = None
        self._GroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup response structure.

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


class DeletePrometheusAlertPolicyRequest(AbstractModel):
    """DeletePrometheusAlertPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertIds: List of alerting rule IDs
        :type AlertIds: list of str
        :param _Names: Alerting rule name
        :type Names: list of str
        """
        self._InstanceId = None
        self._AlertIds = None
        self._Names = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertIds(self):
        return self._AlertIds

    @AlertIds.setter
    def AlertIds(self, AlertIds):
        self._AlertIds = AlertIds

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AlertIds = params.get("AlertIds")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertPolicyResponse(AbstractModel):
    """DeletePrometheusAlertPolicy response structure.

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


class DeletePrometheusClusterAgentRequest(AbstractModel):
    """DeletePrometheusClusterAgent request structure.

    """

    def __init__(self):
        r"""
        :param _Agents: Agent list
        :type Agents: list of PrometheusAgentInfo
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._Agents = None
        self._InstanceId = None

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusAgentInfo()
                obj._deserialize(item)
                self._Agents.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusClusterAgentResponse(AbstractModel):
    """DeletePrometheusClusterAgent response structure.

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


class DeletePrometheusConfigRequest(AbstractModel):
    """DeletePrometheusConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ServiceMonitors: List of names of the service monitors to be deleted
        :type ServiceMonitors: list of str
        :param _PodMonitors: List of names of the pod monitors to be deleted
        :type PodMonitors: list of str
        :param _RawJobs: List of names of the raw jobs to be deleted
        :type RawJobs: list of str
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._ServiceMonitors = params.get("ServiceMonitors")
        self._PodMonitors = params.get("PodMonitors")
        self._RawJobs = params.get("RawJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusConfigResponse(AbstractModel):
    """DeletePrometheusConfig response structure.

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


class DeletePrometheusRecordRuleYamlRequest(AbstractModel):
    """DeletePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Names: List of recording rules
        :type Names: list of str
        """
        self._InstanceId = None
        self._Names = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusRecordRuleYamlResponse(AbstractModel):
    """DeletePrometheusRecordRuleYaml response structure.

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


class DeletePrometheusScrapeJobsRequest(AbstractModel):
    """DeletePrometheusScrapeJobs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _JobIds: List of task IDs
        :type JobIds: list of str
        """
        self._InstanceId = None
        self._AgentId = None
        self._JobIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusScrapeJobsResponse(AbstractModel):
    """DeletePrometheusScrapeJobs response structure.

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


class DeletePrometheusTempRequest(AbstractModel):
    """DeletePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempResponse(AbstractModel):
    """DeletePrometheusTemp response structure.

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


class DeletePrometheusTempSyncRequest(AbstractModel):
    """DeletePrometheusTempSync request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: str
        :param _Targets: List of unsynced objects
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self._TemplateId = None
        self._Targets = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempSyncResponse(AbstractModel):
    """DeletePrometheusTempSync response structure.

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


class DeleteRecordingRulesRequest(AbstractModel):
    """DeleteRecordingRules request structure.

    """

    def __init__(self):
        r"""
        :param _RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        """
        self._RuleIds = None
        self._InstanceId = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordingRulesResponse(AbstractModel):
    """DeleteRecordingRules response structure.

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


class DeleteSSOAccountRequest(AbstractModel):
    """DeleteSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _UserId: User account ID, such as “10000000”.
        :type UserId: str
        """
        self._InstanceId = None
        self._UserId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSSOAccountResponse(AbstractModel):
    """DeleteSSOAccount response structure.

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


class DescribeAccidentEventListAlarms(AbstractModel):
    """Output parameter type of the DescribeAccidentEventList API

    """

    def __init__(self):
        r"""
        :param _BusinessTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type BusinessTypeDesc: str
        :param _AccidentTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type AccidentTypeDesc: str
        :param _BusinessID: ID of the event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.
Note: This field may return null, indicating that no valid value was found.
        :type BusinessID: int
        :param _EventStatus: Event status ID. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.
Note: This field may return null, indicating that no valid value was found.
        :type EventStatus: int
        :param _AffectResource: Affected object.
Note: This field may return null, indicating that no valid value was found.
        :type AffectResource: str
        :param _Region: Region where the event occurs.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param _OccurTime: Time when the event occurs.
Note: This field may return null, indicating that no valid value was found.
        :type OccurTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: str
        """
        self._BusinessTypeDesc = None
        self._AccidentTypeDesc = None
        self._BusinessID = None
        self._EventStatus = None
        self._AffectResource = None
        self._Region = None
        self._OccurTime = None
        self._UpdateTime = None

    @property
    def BusinessTypeDesc(self):
        return self._BusinessTypeDesc

    @BusinessTypeDesc.setter
    def BusinessTypeDesc(self, BusinessTypeDesc):
        self._BusinessTypeDesc = BusinessTypeDesc

    @property
    def AccidentTypeDesc(self):
        return self._AccidentTypeDesc

    @AccidentTypeDesc.setter
    def AccidentTypeDesc(self, AccidentTypeDesc):
        self._AccidentTypeDesc = AccidentTypeDesc

    @property
    def BusinessID(self):
        return self._BusinessID

    @BusinessID.setter
    def BusinessID(self, BusinessID):
        self._BusinessID = BusinessID

    @property
    def EventStatus(self):
        return self._EventStatus

    @EventStatus.setter
    def EventStatus(self, EventStatus):
        self._EventStatus = EventStatus

    @property
    def AffectResource(self):
        return self._AffectResource

    @AffectResource.setter
    def AffectResource(self, AffectResource):
        self._AffectResource = AffectResource

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def OccurTime(self):
        return self._OccurTime

    @OccurTime.setter
    def OccurTime(self, OccurTime):
        self._OccurTime = OccurTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._BusinessTypeDesc = params.get("BusinessTypeDesc")
        self._AccidentTypeDesc = params.get("AccidentTypeDesc")
        self._BusinessID = params.get("BusinessID")
        self._EventStatus = params.get("EventStatus")
        self._AffectResource = params.get("AffectResource")
        self._Region = params.get("Region")
        self._OccurTime = params.get("OccurTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param _StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param _EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param _Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.
        :type Limit: int
        :param _Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.
        :type Offset: int
        :param _UpdateTimeOrder: Sorting rule by UpdateTime. Valid values: asc and desc.
        :type UpdateTimeOrder: str
        :param _OccurTimeOrder: Sorting rule by OccurTime. Valid values: asc or desc. Sorting by UpdateTimeOrder takes priority.
        :type OccurTimeOrder: str
        :param _AccidentType: Filter by event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.
        :type AccidentType: list of int
        :param _AccidentEvent: Filter by event. The value 1 indicates CVM storage issues. The value 2 indicates CVM network connection issues. The value 3 indicates that the CVM has an exception. The value 202 indicates that an ISP network jitter occurs.
        :type AccidentEvent: list of int
        :param _AccidentStatus: Filter by event status. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.
        :type AccidentStatus: list of int
        :param _AccidentRegion: Filter by region where the event occurs. The value gz indicates Guangzhou. The value sh indicates Shanghai.
        :type AccidentRegion: list of str
        :param _AffectResource: Filter by affected resource, such as ins-19a06bka.
        :type AffectResource: str
        """
        self._Module = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._UpdateTimeOrder = None
        self._OccurTimeOrder = None
        self._AccidentType = None
        self._AccidentEvent = None
        self._AccidentStatus = None
        self._AccidentRegion = None
        self._AffectResource = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def OccurTimeOrder(self):
        return self._OccurTimeOrder

    @OccurTimeOrder.setter
    def OccurTimeOrder(self, OccurTimeOrder):
        self._OccurTimeOrder = OccurTimeOrder

    @property
    def AccidentType(self):
        return self._AccidentType

    @AccidentType.setter
    def AccidentType(self, AccidentType):
        self._AccidentType = AccidentType

    @property
    def AccidentEvent(self):
        return self._AccidentEvent

    @AccidentEvent.setter
    def AccidentEvent(self, AccidentEvent):
        self._AccidentEvent = AccidentEvent

    @property
    def AccidentStatus(self):
        return self._AccidentStatus

    @AccidentStatus.setter
    def AccidentStatus(self, AccidentStatus):
        self._AccidentStatus = AccidentStatus

    @property
    def AccidentRegion(self):
        return self._AccidentRegion

    @AccidentRegion.setter
    def AccidentRegion(self, AccidentRegion):
        self._AccidentRegion = AccidentRegion

    @property
    def AffectResource(self):
        return self._AffectResource

    @AffectResource.setter
    def AffectResource(self, AffectResource):
        self._AffectResource = AffectResource


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._OccurTimeOrder = params.get("OccurTimeOrder")
        self._AccidentType = params.get("AccidentType")
        self._AccidentEvent = params.get("AccidentEvent")
        self._AccidentStatus = params.get("AccidentStatus")
        self._AccidentRegion = params.get("AccidentRegion")
        self._AffectResource = params.get("AffectResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList response structure.

    """

    def __init__(self):
        r"""
        :param _Alarms: Platform event list.
Note: This field may return null, indicating that no valid value was found.
        :type Alarms: list of DescribeAccidentEventListAlarms
        :param _Total: Total number of platform events.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Alarms = None
        self._Total = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
                obj = DescribeAccidentEventListAlarms()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAlarmEventsRequest(AbstractModel):
    """DescribeAlarmEvents request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param _Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API
        :type Namespace: str
        :param _MonitorType: Monitoring type, such as `MT_QCE`, which is set to default.
        :type MonitorType: str
        """
        self._Module = None
        self._Namespace = None
        self._MonitorType = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Namespace = params.get("Namespace")
        self._MonitorType = params.get("MonitorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmEventsResponse(AbstractModel):
    """DescribeAlarmEvents response structure.

    """

    def __init__(self):
        r"""
        :param _Events: Alarm event list
        :type Events: list of AlarmEvent
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Events = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = AlarmEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmHistoriesRequest(AbstractModel):
    """DescribeAlarmHistories request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _PageNumber: Page number starting from 1. Default value: 1
        :type PageNumber: int
        :param _PageSize: Number of entries per page. Value range: 1–100. Default value: 20
        :type PageSize: int
        :param _Order: Sort by the first occurrence time in descending order by default. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param _StartTime: Start time, which is the timestamp one day ago by default and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is later than the `StartTime`.
        :type StartTime: int
        :param _EndTime: End time, which is the current timestamp and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is earlier than the `EndTime`.
        :type EndTime: int
        :param _MonitorTypes: Filter by monitor type. Valid values: "MT_QCE" (Tencent Cloud service monitoring), "MT_TAW" (application performance monitoring), "MT_RUM" (frontend performance monitoring), "MT_PROBE" (cloud automated testing). If this parameter is left empty, all types will be queried by default.
        :type MonitorTypes: list of str
        :param _AlarmObject: Filter by alarm object. Fuzzy search with string is supported
        :type AlarmObject: str
        :param _AlarmStatus: Filter by alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data). If this parameter is left empty, all will be queried by default
        :type AlarmStatus: list of str
        :param _ProjectIds: Filter by project ID. Valid values: `-1` (no project), `0` (default project)
        :type ProjectIds: list of int
        :param _InstanceGroupIds: Filter by instance group ID
        :type InstanceGroupIds: list of int
        :param _Namespaces: Filter by policy type. Monitoring type and policy type are first-level and second-level filters respectively and both need to be passed in. For example, `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`
        :type Namespaces: list of MonitorTypeNamespace
        :param _MetricNames: Filter by metric name
        :type MetricNames: list of str
        :param _PolicyName: Fuzzy search by policy name
        :type PolicyName: str
        :param _Content: Fuzzy search by alarm content
        :type Content: str
        :param _ReceiverUids: Search by recipient
        :type ReceiverUids: list of int
        :param _ReceiverGroups: Search by recipient group
        :type ReceiverGroups: list of int
        :param _PolicyIds: Search by alarm policy ID list
        :type PolicyIds: list of str
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._Order = None
        self._StartTime = None
        self._EndTime = None
        self._MonitorTypes = None
        self._AlarmObject = None
        self._AlarmStatus = None
        self._ProjectIds = None
        self._InstanceGroupIds = None
        self._Namespaces = None
        self._MetricNames = None
        self._PolicyName = None
        self._Content = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._PolicyIds = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

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
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def AlarmObject(self):
        return self._AlarmObject

    @AlarmObject.setter
    def AlarmObject(self, AlarmObject):
        self._AlarmObject = AlarmObject

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def InstanceGroupIds(self):
        return self._InstanceGroupIds

    @InstanceGroupIds.setter
    def InstanceGroupIds(self, InstanceGroupIds):
        self._InstanceGroupIds = InstanceGroupIds

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MonitorTypes = params.get("MonitorTypes")
        self._AlarmObject = params.get("AlarmObject")
        self._AlarmStatus = params.get("AlarmStatus")
        self._ProjectIds = params.get("ProjectIds")
        self._InstanceGroupIds = params.get("InstanceGroupIds")
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = MonitorTypeNamespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._MetricNames = params.get("MetricNames")
        self._PolicyName = params.get("PolicyName")
        self._Content = params.get("Content")
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmHistoriesResponse(AbstractModel):
    """DescribeAlarmHistories response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Histories: Alarm record list
        :type Histories: list of AlarmHistory
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Histories = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Histories(self):
        return self._Histories

    @Histories.setter
    def Histories(self, Histories):
        self._Histories = Histories

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Histories") is not None:
            self._Histories = []
            for item in params.get("Histories"):
                obj = AlarmHistory()
                obj._deserialize(item)
                self._Histories.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmMetricsRequest(AbstractModel):
    """DescribeAlarmMetrics request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _MonitorType: Monitor type filter. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorType: str
        :param _Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API
        :type Namespace: str
        """
        self._Module = None
        self._MonitorType = None
        self._Namespace = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmMetricsResponse(AbstractModel):
    """DescribeAlarmMetrics response structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: Alarm metric list
        :type Metrics: list of Metric
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Metrics = None
        self._RequestId = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticeCallbacksRequest(AbstractModel):
    """DescribeAlarmNoticeCallbacks request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeCallbacksResponse(AbstractModel):
    """DescribeAlarmNoticeCallbacks response structure.

    """

    def __init__(self):
        r"""
        :param _URLNotices: Alarm callback notification
Note: this field may return null, indicating that no valid values can be obtained.
        :type URLNotices: list of URLNotice
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._URLNotices = None
        self._RequestId = None

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticeRequest(AbstractModel):
    """DescribeAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _NoticeId: Alarm notification template ID
        :type NoticeId: str
        """
        self._Module = None
        self._NoticeId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeResponse(AbstractModel):
    """DescribeAlarmNotice response structure.

    """

    def __init__(self):
        r"""
        :param _Notice: Alarm notification template details
        :type Notice: :class:`tencentcloud.monitor.v20180724.models.AlarmNotice`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Notice = None
        self._RequestId = None

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Notice") is not None:
            self._Notice = AlarmNotice()
            self._Notice._deserialize(params.get("Notice"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _PageNumber: Page number. Minimum value: 1
        :type PageNumber: int
        :param _PageSize: Number of entries per page. Value range: 1–200
        :type PageSize: int
        :param _Order: Sort by update time. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param _OwnerUid: Root account `uid`, which is used to create preset notifications
        :type OwnerUid: int
        :param _Name: Alarm notification template name, which is used for fuzzy search
        :type Name: str
        :param _ReceiverType: Filter by recipient. The type of notified users should be selected for the alarm notification template. Valid values: USER (user), GROUP (user group). If this parameter is left empty, no filter by recipient will be performed
        :type ReceiverType: str
        :param _UserIds: Recipient object list
        :type UserIds: list of int
        :param _GroupIds: Recipient group list
        :type GroupIds: list of int
        :param _NoticeIds: Filter by notification template ID. If an empty array is passed in or if this parameter is left empty, the filter operation will not be performed.
        :type NoticeIds: list of str
        :param _Tags: Filter templates by tag
        :type Tags: list of Tag
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._Order = None
        self._OwnerUid = None
        self._Name = None
        self._ReceiverType = None
        self._UserIds = None
        self._GroupIds = None
        self._NoticeIds = None
        self._Tags = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OwnerUid(self):
        return self._OwnerUid

    @OwnerUid.setter
    def OwnerUid(self, OwnerUid):
        self._OwnerUid = OwnerUid

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Order = params.get("Order")
        self._OwnerUid = params.get("OwnerUid")
        self._Name = params.get("Name")
        self._ReceiverType = params.get("ReceiverType")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._NoticeIds = params.get("NoticeIds")
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
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of alarm notification templates
        :type TotalCount: int
        :param _Notices: Alarm notification template list
        :type Notices: list of AlarmNotice
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Notices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Notices(self):
        return self._Notices

    @Notices.setter
    def Notices(self, Notices):
        self._Notices = Notices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Notices") is not None:
            self._Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self._Notices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmPoliciesRequest(AbstractModel):
    """DescribeAlarmPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _PageNumber: Page number starting from 1. Default value: 1
        :type PageNumber: int
        :param _PageSize: Number of entries per page. Value range: 1–100. Default value: 20
        :type PageSize: int
        :param _PolicyName: Fuzzy search by policy name
        :type PolicyName: str
        :param _MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default
        :type MonitorTypes: list of str
        :param _Namespaces: Filter by namespace. For the values of different policy types, please see:
[Policy Type List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)
        :type Namespaces: list of str
        :param _Dimensions: The alarm object list, which is a JSON string. The outer array corresponds to multiple instances, and the inner array is the dimension of an object. For example, “CVM - Basic Monitor” can be written as:
`[ {"Dimensions": {"unInstanceId": "ins-qr8d555g"}}, {"Dimensions": {"unInstanceId": "ins-qr8d555h"}} ]`
You can also refer to the “Example 2” below.

For more information on the parameter samples of different Tencent Cloud services, see [Product Policy Type and Dimension Information](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1).

Note: If `1` is passed in for `NeedCorrespondence`, the relationship between a policy and an instance needs to be returned. You can pass in up to 20 alarm object dimensions to avoid request timeout.
        :type Dimensions: str
        :param _ReceiverUids: Search by recipient. You can get the user list with the API [ListUsers](https://intl.cloud.tencent.com/document/product/598/34587?from_cn_redirect=1) in “Cloud Access Management” or query the sub-user information with the API [GetUser](https://intl.cloud.tencent.com/document/product/598/34590?from_cn_redirect=1). The `Uid` field in the returned result should be entered here.
        :type ReceiverUids: list of int
        :param _ReceiverGroups: Search by recipient group. You can get the user group list with the API [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) in “Cloud Access Management” or query the user group list where a sub-user is in with the API [ListGroupsForUser](https://intl.cloud.tencent.com/document/product/598/34588?from_cn_redirect=1). The `GroupId` field in the returned result should be entered here.
        :type ReceiverGroups: list of int
        :param _PolicyType: Filter by default policy. Valid values: DEFAULT (display default policy), NOT_DEFAULT (display non-default policies). If this parameter is left empty, all policies will be displayed
        :type PolicyType: list of str
        :param _Field: Sort by field. For example, to sort by the last modification time, use Field: "UpdateTime".
        :type Field: str
        :param _Order: Sort order. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param _ProjectIds: ID array of the policy project, which can be viewed on the following page:
[Project Management](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param _NoticeIds: ID list of the notification template, which can be obtained by querying the notification template list.
It can be queried with the API [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1).
        :type NoticeIds: list of str
        :param _RuleTypes: Filter by trigger condition. Valid values: STATIC (display policies with static threshold), DYNAMIC (display policies with dynamic threshold). If this parameter is left empty, all policies will be displayed
        :type RuleTypes: list of str
        :param _Enable: Filter by alarm status. Valid values: [1]: enabled; [0]: disabled; [0, 1]: all
        :type Enable: list of int
        :param _NotBindingNoticeRule: If `1` is passed in, alarm policies with no notification rules configured are queried. If it is left empty or other values are passed in, all alarm policies are queried.
        :type NotBindingNoticeRule: int
        :param _InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param _NeedCorrespondence: Whether the relationship between a policy and the input parameter filter dimension is required. `1`: Yes. `0`: No. Default value: `0`.
        :type NeedCorrespondence: int
        :param _TriggerTasks: Filter alarm policy by triggered task (such as auto scaling task). Up to 10 tasks can be specified.
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param _OneClickPolicyType: Filter by quick alarm policy. If this parameter is left empty, all policies are displayed. `ONECLICK`: Display quick alarm policies; `NOT_ONECLICK`: Display non-quick alarm policies.
        :type OneClickPolicyType: list of str
        :param _NotBindAll: Whether the returned result filters policies associated with all objects. Valid values: `1` (Yes), `0` (No).
        :type NotBindAll: int
        :param _NotInstanceGroup: Whether the returned result filters policies associated with instance groups. Valid values: `1` (Yes), `0` (No).
        :type NotInstanceGroup: int
        :param _Tags: Filter policies by tag
        :type Tags: list of Tag
        """
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._PolicyName = None
        self._MonitorTypes = None
        self._Namespaces = None
        self._Dimensions = None
        self._ReceiverUids = None
        self._ReceiverGroups = None
        self._PolicyType = None
        self._Field = None
        self._Order = None
        self._ProjectIds = None
        self._NoticeIds = None
        self._RuleTypes = None
        self._Enable = None
        self._NotBindingNoticeRule = None
        self._InstanceGroupId = None
        self._NeedCorrespondence = None
        self._TriggerTasks = None
        self._OneClickPolicyType = None
        self._NotBindAll = None
        self._NotInstanceGroup = None
        self._Tags = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def ReceiverUids(self):
        return self._ReceiverUids

    @ReceiverUids.setter
    def ReceiverUids(self, ReceiverUids):
        self._ReceiverUids = ReceiverUids

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def RuleTypes(self):
        return self._RuleTypes

    @RuleTypes.setter
    def RuleTypes(self, RuleTypes):
        self._RuleTypes = RuleTypes

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def NotBindingNoticeRule(self):
        return self._NotBindingNoticeRule

    @NotBindingNoticeRule.setter
    def NotBindingNoticeRule(self, NotBindingNoticeRule):
        self._NotBindingNoticeRule = NotBindingNoticeRule

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def NeedCorrespondence(self):
        return self._NeedCorrespondence

    @NeedCorrespondence.setter
    def NeedCorrespondence(self, NeedCorrespondence):
        self._NeedCorrespondence = NeedCorrespondence

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks

    @property
    def OneClickPolicyType(self):
        return self._OneClickPolicyType

    @OneClickPolicyType.setter
    def OneClickPolicyType(self, OneClickPolicyType):
        self._OneClickPolicyType = OneClickPolicyType

    @property
    def NotBindAll(self):
        return self._NotBindAll

    @NotBindAll.setter
    def NotBindAll(self, NotBindAll):
        self._NotBindAll = NotBindAll

    @property
    def NotInstanceGroup(self):
        return self._NotInstanceGroup

    @NotInstanceGroup.setter
    def NotInstanceGroup(self, NotInstanceGroup):
        self._NotInstanceGroup = NotInstanceGroup

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._PolicyName = params.get("PolicyName")
        self._MonitorTypes = params.get("MonitorTypes")
        self._Namespaces = params.get("Namespaces")
        self._Dimensions = params.get("Dimensions")
        self._ReceiverUids = params.get("ReceiverUids")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PolicyType = params.get("PolicyType")
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        self._ProjectIds = params.get("ProjectIds")
        self._NoticeIds = params.get("NoticeIds")
        self._RuleTypes = params.get("RuleTypes")
        self._Enable = params.get("Enable")
        self._NotBindingNoticeRule = params.get("NotBindingNoticeRule")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._NeedCorrespondence = params.get("NeedCorrespondence")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        self._OneClickPolicyType = params.get("OneClickPolicyType")
        self._NotBindAll = params.get("NotBindAll")
        self._NotInstanceGroup = params.get("NotInstanceGroup")
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
        


class DescribeAlarmPoliciesResponse(AbstractModel):
    """DescribeAlarmPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of policies
        :type TotalCount: int
        :param _Policies: Policy array
        :type Policies: list of AlarmPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Policies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Policies(self):
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Policies") is not None:
            self._Policies = []
            for item in params.get("Policies"):
                obj = AlarmPolicy()
                obj._deserialize(item)
                self._Policies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAlarmPolicyRequest(AbstractModel):
    """DescribeAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        """
        self._Module = None
        self._PolicyId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmPolicyResponse(AbstractModel):
    """DescribeAlarmPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Policy: Policy details
        :type Policy: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicy`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Policy = None
        self._RequestId = None

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self._Policy = AlarmPolicy()
            self._Policy._deserialize(params.get("Policy"))
        self._RequestId = params.get("RequestId")


class DescribeAlertRulesRequest(AbstractModel):
    """DescribeAlertRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _RuleName: Rule name
        :type RuleName: str
        :param _Type: Alerting rule template category
        :type Type: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._RuleState = None
        self._RuleName = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._RuleName = params.get("RuleName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRulesResponse(AbstractModel):
    """DescribeAlertRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of alerting rules
        :type TotalCount: int
        :param _AlertRuleSet: Alerting rule details
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRuleSet: list of PrometheusRuleSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AlertRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AlertRuleSet(self):
        return self._AlertRuleSet

    @AlertRuleSet.setter
    def AlertRuleSet(self, AlertRuleSet):
        self._AlertRuleSet = AlertRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AlertRuleSet") is not None:
            self._AlertRuleSet = []
            for item in params.get("AlertRuleSet"):
                obj = PrometheusRuleSet()
                obj._deserialize(item)
                self._AlertRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllNamespacesRequest(AbstractModel):
    """DescribeAllNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _SceneType: Filter by use case. Currently, the only valid value is `ST_ALARM` (alarm type).
        :type SceneType: str
        :param _Module: Value fixed at "monitor"
        :type Module: str
        :param _MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default
        :type MonitorTypes: list of str
        :param _Ids: Filter by namespace ID. If this parameter is left empty, all will be queried
        :type Ids: list of str
        """
        self._SceneType = None
        self._Module = None
        self._MonitorTypes = None
        self._Ids = None

    @property
    def SceneType(self):
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._SceneType = params.get("SceneType")
        self._Module = params.get("Module")
        self._MonitorTypes = params.get("MonitorTypes")
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllNamespacesResponse(AbstractModel):
    """DescribeAllNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param _QceNamespaces: Alarm policy type of Tencent Cloud service (disused)
        :type QceNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param _CustomNamespaces: Other alarm policy type (disused)
        :type CustomNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param _QceNamespacesNew: Alarm policy type of Tencent Cloud service
        :type QceNamespacesNew: list of CommonNamespace
        :param _CustomNamespacesNew: Other alarm policy type (not supported currently)
        :type CustomNamespacesNew: list of CommonNamespace
        :param _CommonNamespaces: General alarm policy type, including TAPM, RUM, and CAT.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonNamespaces: list of CommonNamespaceNew
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QceNamespaces = None
        self._CustomNamespaces = None
        self._QceNamespacesNew = None
        self._CustomNamespacesNew = None
        self._CommonNamespaces = None
        self._RequestId = None

    @property
    def QceNamespaces(self):
        return self._QceNamespaces

    @QceNamespaces.setter
    def QceNamespaces(self, QceNamespaces):
        self._QceNamespaces = QceNamespaces

    @property
    def CustomNamespaces(self):
        return self._CustomNamespaces

    @CustomNamespaces.setter
    def CustomNamespaces(self, CustomNamespaces):
        self._CustomNamespaces = CustomNamespaces

    @property
    def QceNamespacesNew(self):
        return self._QceNamespacesNew

    @QceNamespacesNew.setter
    def QceNamespacesNew(self, QceNamespacesNew):
        self._QceNamespacesNew = QceNamespacesNew

    @property
    def CustomNamespacesNew(self):
        return self._CustomNamespacesNew

    @CustomNamespacesNew.setter
    def CustomNamespacesNew(self, CustomNamespacesNew):
        self._CustomNamespacesNew = CustomNamespacesNew

    @property
    def CommonNamespaces(self):
        return self._CommonNamespaces

    @CommonNamespaces.setter
    def CommonNamespaces(self, CommonNamespaces):
        self._CommonNamespaces = CommonNamespaces

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QceNamespaces") is not None:
            self._QceNamespaces = CommonNamespace()
            self._QceNamespaces._deserialize(params.get("QceNamespaces"))
        if params.get("CustomNamespaces") is not None:
            self._CustomNamespaces = CommonNamespace()
            self._CustomNamespaces._deserialize(params.get("CustomNamespaces"))
        if params.get("QceNamespacesNew") is not None:
            self._QceNamespacesNew = []
            for item in params.get("QceNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self._QceNamespacesNew.append(obj)
        if params.get("CustomNamespacesNew") is not None:
            self._CustomNamespacesNew = []
            for item in params.get("CustomNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self._CustomNamespacesNew.append(obj)
        if params.get("CommonNamespaces") is not None:
            self._CommonNamespaces = []
            for item in params.get("CommonNamespaces"):
                obj = CommonNamespaceNew()
                obj._deserialize(item)
                self._CommonNamespaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics request structure.

    """

    def __init__(self):
        r"""
        :param _Namespace: Service namespace. Tencent Cloud services have different namespaces. For more information on service namespaces, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the namespace of CVM
        :type Namespace: str
        :param _MetricName: Metric name. Tencent Cloud services have different metric names. For more information on metric names, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the metric names of CVM
        :type MetricName: str
        :param _Dimensions: Filter by dimension. This parameter is optional.
        :type Dimensions: list of str
        """
        self._Namespace = None
        self._MetricName = None
        self._Dimensions = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics response structure.

    """

    def __init__(self):
        r"""
        :param _MetricSet: Listed of queried metric descriptions
        :type MetricSet: list of MetricSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MetricSet = None
        self._RequestId = None

    @property
    def MetricSet(self):
        return self._MetricSet

    @MetricSet.setter
    def MetricSet(self, MetricSet):
        self._MetricSet = MetricSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self._MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self._MetricSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBasicAlarmListAlarms(AbstractModel):
    """Alarms returned by DescribeBasicAlarmList

    """

    def __init__(self):
        r"""
        :param _Id: Alarm ID.
        :type Id: int
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectId: int
        :param _ProjectName: Project name.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectName: str
        :param _Status: Alarm status ID. Valid values: 0 (not resolved), 1 (resolved), 2/3/5 (insufficient data), 4 (expired)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_DATA (insufficient data), NO_CONF (expired)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AlarmStatus: str
        :param _GroupId: Policy group ID.
Note: This field may return null, indicating that no valid value was found.
        :type GroupId: int
        :param _GroupName: Policy group name.
Note: This field may return null, indicating that no valid value was found.
        :type GroupName: str
        :param _FirstOccurTime: Occurrence time.
Note: This field may return null, indicating that no valid value was found.
        :type FirstOccurTime: str
        :param _Duration: Duration in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Duration: int
        :param _LastOccurTime: End time.
Note: This field may return null, indicating that no valid value was found.
        :type LastOccurTime: str
        :param _Content: Alarm content.
Note: This field may return null, indicating that no valid value was found.
        :type Content: str
        :param _ObjName: Alarm object.
Note: This field may return null, indicating that no valid value was found.
        :type ObjName: str
        :param _ObjId: Alarm object ID.
Note: This field may return null, indicating that no valid value was found.
        :type ObjId: str
        :param _ViewName: Policy type.
Note: This field may return null, indicating that no valid value was found.
        :type ViewName: str
        :param _Vpc: VPC, which is unique to CVM.
Note: This field may return null, indicating that no valid value was found.
        :type Vpc: str
        :param _MetricId: Metric ID.
Note: This field may return null, indicating that no valid value was found.
        :type MetricId: int
        :param _MetricName: Metric name.
Note: This field may return null, indicating that no valid value was found.
        :type MetricName: str
        :param _AlarmType: Alarm type. The value 0 indicates metric alarms. The value 2 indicates product event alarms. The value 3 indicates platform event alarms.
Note: This field may return null, indicating that no valid value was found.
        :type AlarmType: int
        :param _Region: Region.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param _Dimensions: Dimensions of an alarm object.
Note: This field may return null, indicating that no valid value was found.
        :type Dimensions: str
        :param _NotifyWay: Notification method.
Note: This field may return null, indicating that no valid value was found.
        :type NotifyWay: list of str
        :param _InstanceGroup: Instance group information.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: list of InstanceGroup
        """
        self._Id = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._AlarmStatus = None
        self._GroupId = None
        self._GroupName = None
        self._FirstOccurTime = None
        self._Duration = None
        self._LastOccurTime = None
        self._Content = None
        self._ObjName = None
        self._ObjId = None
        self._ViewName = None
        self._Vpc = None
        self._MetricId = None
        self._MetricName = None
        self._AlarmType = None
        self._Region = None
        self._Dimensions = None
        self._NotifyWay = None
        self._InstanceGroup = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

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
    def FirstOccurTime(self):
        return self._FirstOccurTime

    @FirstOccurTime.setter
    def FirstOccurTime(self, FirstOccurTime):
        self._FirstOccurTime = FirstOccurTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def LastOccurTime(self):
        return self._LastOccurTime

    @LastOccurTime.setter
    def LastOccurTime(self, LastOccurTime):
        self._LastOccurTime = LastOccurTime

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ObjName(self):
        return self._ObjName

    @ObjName.setter
    def ObjName(self, ObjName):
        self._ObjName = ObjName

    @property
    def ObjId(self):
        return self._ObjId

    @ObjId.setter
    def ObjId(self, ObjId):
        self._ObjId = ObjId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._AlarmStatus = params.get("AlarmStatus")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._FirstOccurTime = params.get("FirstOccurTime")
        self._Duration = params.get("Duration")
        self._LastOccurTime = params.get("LastOccurTime")
        self._Content = params.get("Content")
        self._ObjName = params.get("ObjName")
        self._ObjId = params.get("ObjId")
        self._ViewName = params.get("ViewName")
        self._Vpc = params.get("Vpc")
        self._MetricId = params.get("MetricId")
        self._MetricName = params.get("MetricName")
        self._AlarmType = params.get("AlarmType")
        self._Region = params.get("Region")
        self._Dimensions = params.get("Dimensions")
        self._NotifyWay = params.get("NotifyWay")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroup()
                obj._deserialize(item)
                self._InstanceGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param _StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param _EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param _Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.
        :type Limit: int
        :param _Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.
        :type Offset: int
        :param _OccurTimeOrder: Sorting by occurrence time. Valid values: asc and desc.
        :type OccurTimeOrder: str
        :param _ProjectIds: Filter by project ID.
        :type ProjectIds: list of int
        :param _ViewNames: Filter by policy type.
        :type ViewNames: list of str
        :param _AlarmStatus: Filter by alarm status.
        :type AlarmStatus: list of int
        :param _ObjLike: Filter by alarm object.
        :type ObjLike: str
        :param _InstanceGroupIds: Filter by instance group ID.
        :type InstanceGroupIds: list of int
        :param _MetricNames: Filtering by metric names
        :type MetricNames: list of str
        """
        self._Module = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OccurTimeOrder = None
        self._ProjectIds = None
        self._ViewNames = None
        self._AlarmStatus = None
        self._ObjLike = None
        self._InstanceGroupIds = None
        self._MetricNames = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OccurTimeOrder(self):
        return self._OccurTimeOrder

    @OccurTimeOrder.setter
    def OccurTimeOrder(self, OccurTimeOrder):
        self._OccurTimeOrder = OccurTimeOrder

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ViewNames(self):
        return self._ViewNames

    @ViewNames.setter
    def ViewNames(self, ViewNames):
        self._ViewNames = ViewNames

    @property
    def AlarmStatus(self):
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

    @property
    def ObjLike(self):
        return self._ObjLike

    @ObjLike.setter
    def ObjLike(self, ObjLike):
        self._ObjLike = ObjLike

    @property
    def InstanceGroupIds(self):
        return self._InstanceGroupIds

    @InstanceGroupIds.setter
    def InstanceGroupIds(self, InstanceGroupIds):
        self._InstanceGroupIds = InstanceGroupIds

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OccurTimeOrder = params.get("OccurTimeOrder")
        self._ProjectIds = params.get("ProjectIds")
        self._ViewNames = params.get("ViewNames")
        self._AlarmStatus = params.get("AlarmStatus")
        self._ObjLike = params.get("ObjLike")
        self._InstanceGroupIds = params.get("InstanceGroupIds")
        self._MetricNames = params.get("MetricNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList response structure.

    """

    def __init__(self):
        r"""
        :param _Alarms: Alarm list.
Note: This field may return null, indicating that no valid value was found.
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param _Total: Total number.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param _Warning: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warning: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Alarms = None
        self._Total = None
        self._Warning = None
        self._RequestId = None

    @property
    def Alarms(self):
        return self._Alarms

    @Alarms.setter
    def Alarms(self, Alarms):
        self._Alarms = Alarms

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Warning(self):
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

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
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self._Alarms.append(obj)
        self._Total = params.get("Total")
        self._Warning = params.get("Warning")
        self._RequestId = params.get("RequestId")


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """Dimensions of the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID.
        :type RegionId: int
        :param _Region: Region abbreviation.
        :type Region: str
        :param _Dimensions: Combined JSON string of dimensions.
        :type Dimensions: str
        :param _EventDimensions: Combined JSON string of event dimensions.
        :type EventDimensions: str
        """
        self._RegionId = None
        self._Region = None
        self._Dimensions = None
        self._EventDimensions = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def EventDimensions(self):
        return self._EventDimensions

    @EventDimensions.setter
    def EventDimensions(self, EventDimensions):
        self._EventDimensions = EventDimensions


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._Dimensions = params.get("Dimensions")
        self._EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """Object instance information returned by the DescribeBindingPolicyObjectListInstance API.

    """

    def __init__(self):
        r"""
        :param _UniqueId: Unique ID of the object.
        :type UniqueId: str
        :param _Dimensions: Dimension set of an object instance, which is a jsonObj string.
        :type Dimensions: str
        :param _IsShielded: Whether the object is shielded. The value 0 indicates that the object is not shielded. The value 1 indicates that the object is shielded.
        :type IsShielded: int
        :param _Region: Region where the object resides.
        :type Region: str
        """
        self._UniqueId = None
        self._Dimensions = None
        self._IsShielded = None
        self._Region = None

    @property
    def UniqueId(self):
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def IsShielded(self):
        return self._IsShielded

    @IsShielded.setter
    def IsShielded(self, IsShielded):
        self._IsShielded = IsShielded

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UniqueId = params.get("UniqueId")
        self._Dimensions = params.get("Dimensions")
        self._IsShielded = params.get("IsShielded")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """Instance group information returned by the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param _ViewName: Alarm policy type name.
        :type ViewName: str
        :param _LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param _GroupName: Instance group name.
        :type GroupName: str
        :param _InstanceSum: Number of instances.
        :type InstanceSum: int
        :param _UpdateTime: Update time.
        :type UpdateTime: int
        :param _InsertTime: Creation time.
        :type InsertTime: int
        :param _Regions: Regions where the instances reside.
Note: This field may return null, indicating that no valid value was found.
        :type Regions: list of str
        """
        self._InstanceGroupId = None
        self._ViewName = None
        self._LastEditUin = None
        self._GroupName = None
        self._InstanceSum = None
        self._UpdateTime = None
        self._InsertTime = None
        self._Regions = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._GroupName = params.get("GroupName")
        self._InstanceSum = params.get("InstanceSum")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID. If the ID is in the format of “policy-xxxx”, please enter it in the `PolicyId` field. Enter 0 in this field.
        :type GroupId: int
        :param _PolicyId: Alarm policy ID in the format of “policy-xxxx”. If a value has been entered in this field, you can enter 0 in the `GroupId` field.
        :type PolicyId: str
        :param _Limit: The number of alarm objects returned each time. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _Offset: Offset, which starts from 0 and is set to 0 by default. For example, the parameter `Offset=0&Limit=20` returns the zeroth to 19th alarm objects, and `Offset=20&Limit=20` returns the 20th to 39th alarm objects, and so on.
        :type Offset: int
        :param _Dimensions: Dimensions of filtering objects.
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._Limit = None
        self._Offset = None
        self._Dimensions = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList response structure.

    """

    def __init__(self):
        r"""
        :param _List: List of bound object instances.
Note: This field may return null, indicating that no valid value was found.
        :type List: list of DescribeBindingPolicyObjectListInstance
        :param _Total: Total number of bound object instances.
        :type Total: int
        :param _NoShieldedSum: Number of object instances that are not shielded.
        :type NoShieldedSum: int
        :param _InstanceGroup: Bound instance group information. This parameter is not configured if no instance group is bound.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._Total = None
        self._NoShieldedSum = None
        self._InstanceGroup = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NoShieldedSum(self):
        return self._NoShieldedSum

    @NoShieldedSum.setter
    def NoShieldedSum(self, NoShieldedSum):
        self._NoShieldedSum = NoShieldedSum

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DescribeBindingPolicyObjectListInstance()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._NoShieldedSum = params.get("NoShieldedSum")
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = DescribeBindingPolicyObjectListInstanceGroup()
            self._InstanceGroup._deserialize(params.get("InstanceGroup"))
        self._RequestId = params.get("RequestId")


class DescribeConditionsTemplateListRequest(AbstractModel):
    """DescribeConditionsTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to `monitor`.
        :type Module: str
        :param _ViewName: View name, which can be obtained via [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1). For the monitoring of Tencent Cloud services, the value of this parameter is `QceNamespacesNew.N.Id` of the output parameter of `DescribeAllNamespaces`, for example, `cvm_device`.
        :type ViewName: str
        :param _GroupName: Filter by trigger condition template name.
        :type GroupName: str
        :param _GroupID: Filter by trigger condition template ID.
        :type GroupID: str
        :param _Limit: Pagination parameter, which specifies the number of returned results per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param _Offset: Pagination offset starting from 0. Default value: 0.
        :type Offset: int
        :param _UpdateTimeOrder: Sorting method by update time. `asc`: Ascending order; `desc`: Descending order.
        :type UpdateTimeOrder: str
        :param _PolicyCountOrder: Sorting order based on the number of associated policies. Valid values: `asc` (ascending order), `desc` (descending order).
        :type PolicyCountOrder: str
        """
        self._Module = None
        self._ViewName = None
        self._GroupName = None
        self._GroupID = None
        self._Limit = None
        self._Offset = None
        self._UpdateTimeOrder = None
        self._PolicyCountOrder = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def PolicyCountOrder(self):
        return self._PolicyCountOrder

    @PolicyCountOrder.setter
    def PolicyCountOrder(self, PolicyCountOrder):
        self._PolicyCountOrder = PolicyCountOrder


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._ViewName = params.get("ViewName")
        self._GroupName = params.get("GroupName")
        self._GroupID = params.get("GroupID")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._PolicyCountOrder = params.get("PolicyCountOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConditionsTemplateListResponse(AbstractModel):
    """DescribeConditionsTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of templates.
        :type Total: int
        :param _TemplateGroupList: Template list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TemplateGroupList: list of TemplateGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._TemplateGroupList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TemplateGroupList(self):
        return self._TemplateGroupList

    @TemplateGroupList.setter
    def TemplateGroupList(self, TemplateGroupList):
        self._TemplateGroupList = TemplateGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("TemplateGroupList") is not None:
            self._TemplateGroupList = []
            for item in params.get("TemplateGroupList"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self._TemplateGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDNSConfigRequest(AbstractModel):
    """DescribeDNSConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDNSConfigResponse(AbstractModel):
    """DescribeDNSConfig response structure.

    """

    def __init__(self):
        r"""
        :param _NameServers: Array of DNS servers
        :type NameServers: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NameServers = None
        self._RequestId = None

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        self._RequestId = params.get("RequestId")


class DescribeExporterIntegrationsRequest(AbstractModel):
    """DescribeExporterIntegrations request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Kind: Type
        :type Kind: str
        :param _Name: Name
        :type Name: str
        """
        self._InstanceId = None
        self._KubeType = None
        self._ClusterId = None
        self._Kind = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExporterIntegrationsResponse(AbstractModel):
    """DescribeExporterIntegrations response structure.

    """

    def __init__(self):
        r"""
        :param _IntegrationSet: List of integration configurations
        :type IntegrationSet: list of IntegrationConfiguration
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IntegrationSet = None
        self._RequestId = None

    @property
    def IntegrationSet(self):
        return self._IntegrationSet

    @IntegrationSet.setter
    def IntegrationSet(self, IntegrationSet):
        self._IntegrationSet = IntegrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self._IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = IntegrationConfiguration()
                obj._deserialize(item)
                self._IntegrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaChannelsRequest(AbstractModel):
    """DescribeGrafanaChannels request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Number of items to be queried
        :type Limit: int
        :param _ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param _ChannelIds: Alert channel ID, such as “nchannel-abcd1234”.
        :type ChannelIds: list of str
        :param _ChannelState: Alert channel status
        :type ChannelState: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ChannelName = None
        self._ChannelIds = None
        self._ChannelState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelIds(self):
        return self._ChannelIds

    @ChannelIds.setter
    def ChannelIds(self, ChannelIds):
        self._ChannelIds = ChannelIds

    @property
    def ChannelState(self):
        return self._ChannelState

    @ChannelState.setter
    def ChannelState(self, ChannelState):
        self._ChannelState = ChannelState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ChannelName = params.get("ChannelName")
        self._ChannelIds = params.get("ChannelIds")
        self._ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaChannelsResponse(AbstractModel):
    """DescribeGrafanaChannels response structure.

    """

    def __init__(self):
        r"""
        :param _NotificationChannelSet: Array of alert channels
        :type NotificationChannelSet: list of GrafanaChannel
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NotificationChannelSet = None
        self._RequestId = None

    @property
    def NotificationChannelSet(self):
        return self._NotificationChannelSet

    @NotificationChannelSet.setter
    def NotificationChannelSet(self, NotificationChannelSet):
        self._NotificationChannelSet = NotificationChannelSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self._NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaChannel()
                obj._deserialize(item)
                self._NotificationChannelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaConfigRequest(AbstractModel):
    """DescribeGrafanaConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaConfigResponse(AbstractModel):
    """DescribeGrafanaConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Config: JSON-encoded string
        :type Config: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Config = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._RequestId = params.get("RequestId")


class DescribeGrafanaEnvironmentsRequest(AbstractModel):
    """DescribeGrafanaEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a TencentCloud Managed Service for Grafana instance, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaEnvironmentsResponse(AbstractModel):
    """DescribeGrafanaEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _Envs: Environment variable string
        :type Envs: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Envs = None
        self._RequestId = None

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Envs = params.get("Envs")
        self._RequestId = params.get("RequestId")


class DescribeGrafanaInstancesRequest(AbstractModel):
    """DescribeGrafanaInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset for query
        :type Offset: int
        :param _Limit: Number of items to be queried
        :type Limit: int
        :param _InstanceIds: Array of TCMG instance IDs
        :type InstanceIds: list of str
        :param _InstanceName: TCMG instance name, which can be fuzzily matched by prefix.
        :type InstanceName: str
        :param _InstanceStatus: Query status
        :type InstanceStatus: list of int
        :param _TagFilters: Array of tag filters
        :type TagFilters: list of PrometheusTag
        """
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None
        self._InstanceName = None
        self._InstanceStatus = None
        self._TagFilters = None

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        self._InstanceStatus = params.get("InstanceStatus")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaInstancesResponse(AbstractModel):
    """DescribeGrafanaInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceSet: This parameter has been disused. Use `Instances` instead.
        :type InstanceSet: list of GrafanaInstanceInfo
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _Instances: List of instances
        :type Instances: list of GrafanaInstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaIntegrationsRequest(AbstractModel):
    """DescribeGrafanaIntegrations request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _IntegrationId: Integration ID
        :type IntegrationId: str
        :param _Kind: Type
        :type Kind: str
        """
        self._InstanceId = None
        self._IntegrationId = None
        self._Kind = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationId = params.get("IntegrationId")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaIntegrationsResponse(AbstractModel):
    """DescribeGrafanaIntegrations response structure.

    """

    def __init__(self):
        r"""
        :param _IntegrationSet: Array of integrations
        :type IntegrationSet: list of GrafanaIntegrationConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IntegrationSet = None
        self._RequestId = None

    @property
    def IntegrationSet(self):
        return self._IntegrationSet

    @IntegrationSet.setter
    def IntegrationSet(self, IntegrationSet):
        self._IntegrationSet = IntegrationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self._IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = GrafanaIntegrationConfig()
                obj._deserialize(item)
                self._IntegrationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaNotificationChannelsRequest(AbstractModel):
    """DescribeGrafanaNotificationChannels request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number of items to be queried
        :type Limit: int
        :param _ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param _ChannelIDs: Alert channel ID, such as “nchannel-abcd1234”.
        :type ChannelIDs: list of str
        :param _ChannelState: Alert channel status
        :type ChannelState: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ChannelName = None
        self._ChannelIDs = None
        self._ChannelState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelIDs(self):
        return self._ChannelIDs

    @ChannelIDs.setter
    def ChannelIDs(self, ChannelIDs):
        self._ChannelIDs = ChannelIDs

    @property
    def ChannelState(self):
        return self._ChannelState

    @ChannelState.setter
    def ChannelState(self, ChannelState):
        self._ChannelState = ChannelState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ChannelName = params.get("ChannelName")
        self._ChannelIDs = params.get("ChannelIDs")
        self._ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaNotificationChannelsResponse(AbstractModel):
    """DescribeGrafanaNotificationChannels response structure.

    """

    def __init__(self):
        r"""
        :param _NotificationChannelSet: Array of notification channels
        :type NotificationChannelSet: list of GrafanaNotificationChannel
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NotificationChannelSet = None
        self._RequestId = None

    @property
    def NotificationChannelSet(self):
        return self._NotificationChannelSet

    @NotificationChannelSet.setter
    def NotificationChannelSet(self, NotificationChannelSet):
        self._NotificationChannelSet = NotificationChannelSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self._NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaNotificationChannel()
                obj._deserialize(item)
                self._NotificationChannelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGrafanaWhiteListRequest(AbstractModel):
    """DescribeGrafanaWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaWhiteListResponse(AbstractModel):
    """DescribeGrafanaWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param _WhiteList: Array
        :type WhiteList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WhiteList = None
        self._RequestId = None

    @property
    def WhiteList(self):
        return self._WhiteList

    @WhiteList.setter
    def WhiteList(self, WhiteList):
        self._WhiteList = WhiteList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WhiteList = params.get("WhiteList")
        self._RequestId = params.get("RequestId")


class DescribeInstalledPluginsRequest(AbstractModel):
    """DescribeInstalledPlugins request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-kleu3gt0”.
        :type InstanceId: str
        :param _PluginId: Filter by plugin ID such as “grafana-piechart-panel”. You can view the IDs of installed plugins through the `DescribeInstalledPlugins` API.
        :type PluginId: str
        """
        self._InstanceId = None
        self._PluginId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstalledPluginsResponse(AbstractModel):
    """DescribeInstalledPlugins response structure.

    """

    def __init__(self):
        r"""
        :param _PluginSet: List of plugins
        :type PluginSet: list of GrafanaPlugin
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PluginSet = None
        self._RequestId = None

    @property
    def PluginSet(self):
        return self._PluginSet

    @PluginSet.setter
    def PluginSet(self, PluginSet):
        self._PluginSet = PluginSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PluginSet") is not None:
            self._PluginSet = []
            for item in params.get("PluginSet"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self._PluginSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMonitorTypesRequest(AbstractModel):
    """DescribeMonitorTypes request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorTypesResponse(AbstractModel):
    """DescribeMonitorTypes response structure.

    """

    def __init__(self):
        r"""
        :param _MonitorTypes: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorTypes: list of str
        :param _MonitorTypeInfos: Monitoring type details
        :type MonitorTypeInfos: list of MonitorTypeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MonitorTypes = None
        self._MonitorTypeInfos = None
        self._RequestId = None

    @property
    def MonitorTypes(self):
        return self._MonitorTypes

    @MonitorTypes.setter
    def MonitorTypes(self, MonitorTypes):
        self._MonitorTypes = MonitorTypes

    @property
    def MonitorTypeInfos(self):
        return self._MonitorTypeInfos

    @MonitorTypeInfos.setter
    def MonitorTypeInfos(self, MonitorTypeInfos):
        self._MonitorTypeInfos = MonitorTypeInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MonitorTypes = params.get("MonitorTypes")
        if params.get("MonitorTypeInfos") is not None:
            self._MonitorTypeInfos = []
            for item in params.get("MonitorTypeInfos"):
                obj = MonitorTypeInfo()
                obj._deserialize(item)
                self._MonitorTypeInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicyConditionListCondition(AbstractModel):
    """Policy conditions returned by the DescribePolicyConditionList API

    """

    def __init__(self):
        r"""
        :param _PolicyViewName: Policy view name.
        :type PolicyViewName: str
        :param _EventMetrics: Event alarm conditions.
Note: This field may return null, indicating that no valid value was found.
        :type EventMetrics: list of DescribePolicyConditionListEventMetric
        :param _IsSupportMultiRegion: Whether to support multiple regions.
        :type IsSupportMultiRegion: bool
        :param _Metrics: Metric alarm conditions.
Note: This field may return null, indicating that no valid value was found.
        :type Metrics: list of DescribePolicyConditionListMetric
        :param _Name: Policy type name.
        :type Name: str
        :param _SortId: Sorting ID.
        :type SortId: int
        :param _SupportDefault: Whether to support default policies.
        :type SupportDefault: bool
        :param _SupportRegions: List of regions that support this policy type.
Note: This field may return null, indicating that no valid value was found.
        :type SupportRegions: list of str
        :param _DeprecatingInfo: Deprecated information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeprecatingInfo: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponseDeprecatingInfo`
        """
        self._PolicyViewName = None
        self._EventMetrics = None
        self._IsSupportMultiRegion = None
        self._Metrics = None
        self._Name = None
        self._SortId = None
        self._SupportDefault = None
        self._SupportRegions = None
        self._DeprecatingInfo = None

    @property
    def PolicyViewName(self):
        return self._PolicyViewName

    @PolicyViewName.setter
    def PolicyViewName(self, PolicyViewName):
        self._PolicyViewName = PolicyViewName

    @property
    def EventMetrics(self):
        return self._EventMetrics

    @EventMetrics.setter
    def EventMetrics(self, EventMetrics):
        self._EventMetrics = EventMetrics

    @property
    def IsSupportMultiRegion(self):
        return self._IsSupportMultiRegion

    @IsSupportMultiRegion.setter
    def IsSupportMultiRegion(self, IsSupportMultiRegion):
        self._IsSupportMultiRegion = IsSupportMultiRegion

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def SupportDefault(self):
        return self._SupportDefault

    @SupportDefault.setter
    def SupportDefault(self, SupportDefault):
        self._SupportDefault = SupportDefault

    @property
    def SupportRegions(self):
        return self._SupportRegions

    @SupportRegions.setter
    def SupportRegions(self, SupportRegions):
        self._SupportRegions = SupportRegions

    @property
    def DeprecatingInfo(self):
        return self._DeprecatingInfo

    @DeprecatingInfo.setter
    def DeprecatingInfo(self, DeprecatingInfo):
        self._DeprecatingInfo = DeprecatingInfo


    def _deserialize(self, params):
        self._PolicyViewName = params.get("PolicyViewName")
        if params.get("EventMetrics") is not None:
            self._EventMetrics = []
            for item in params.get("EventMetrics"):
                obj = DescribePolicyConditionListEventMetric()
                obj._deserialize(item)
                self._EventMetrics.append(obj)
        self._IsSupportMultiRegion = params.get("IsSupportMultiRegion")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = DescribePolicyConditionListMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        self._SupportDefault = params.get("SupportDefault")
        self._SupportRegions = params.get("SupportRegions")
        if params.get("DeprecatingInfo") is not None:
            self._DeprecatingInfo = DescribePolicyConditionListResponseDeprecatingInfo()
            self._DeprecatingInfo._deserialize(params.get("DeprecatingInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        r"""
        :param _CalcType: Check method.
Note: This field may return null, indicating that no valid value was found.
        :type CalcType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`
        :param _CalcValue: Threshold.
Note: This field may return null, indicating that no valid value was found.
        :type CalcValue: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`
        :param _ContinueTime: Duration.
Note: This field may return null, indicating that no valid value was found.
        :type ContinueTime: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`
        :param _Period: Data period.
Note: This field may return null, indicating that no valid value was found.
        :type Period: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`
        :param _PeriodNum: Number of periods.
Note: This field may return null, indicating that no valid value was found.
        :type PeriodNum: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`
        :param _StatType: Statistics method.
Note: This field may return null, indicating that no valid value was found.
        :type StatType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`
        """
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._Period = None
        self._PeriodNum = None
        self._StatType = None

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def PeriodNum(self):
        return self._PeriodNum

    @PeriodNum.setter
    def PeriodNum(self, PeriodNum):
        self._PeriodNum = PeriodNum

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType


    def _deserialize(self, params):
        if params.get("CalcType") is not None:
            self._CalcType = DescribePolicyConditionListConfigManualCalcType()
            self._CalcType._deserialize(params.get("CalcType"))
        if params.get("CalcValue") is not None:
            self._CalcValue = DescribePolicyConditionListConfigManualCalcValue()
            self._CalcValue._deserialize(params.get("CalcValue"))
        if params.get("ContinueTime") is not None:
            self._ContinueTime = DescribePolicyConditionListConfigManualContinueTime()
            self._ContinueTime._deserialize(params.get("ContinueTime"))
        if params.get("Period") is not None:
            self._Period = DescribePolicyConditionListConfigManualPeriod()
            self._Period._deserialize(params.get("Period"))
        if params.get("PeriodNum") is not None:
            self._PeriodNum = DescribePolicyConditionListConfigManualPeriodNum()
            self._PeriodNum._deserialize(params.get("PeriodNum"))
        if params.get("StatType") is not None:
            self._StatType = DescribePolicyConditionListConfigManualStatType()
            self._StatType._deserialize(params.get("StatType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        r"""
        :param _Keys: Value of CalcType.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param _Need: Required or not.
        :type Need: bool
        """
        self._Keys = None
        self._Need = None

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        r"""
        :param _Default: Default value.
Note: This field may return null, indicating that no valid value was found.
        :type Default: str
        :param _Fixed: Fixed value.
Note: This field may return null, indicating that no valid value was found.
        :type Fixed: str
        :param _Max: Maximum value.
Note: This field may return null, indicating that no valid value was found.
        :type Max: str
        :param _Min: Minimum value.
Note: This field may return null, indicating that no valid value was found.
        :type Min: str
        :param _Need: Required or not.
        :type Need: bool
        """
        self._Default = None
        self._Fixed = None
        self._Max = None
        self._Min = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Fixed(self):
        return self._Fixed

    @Fixed.setter
    def Fixed(self, Fixed):
        self._Fixed = Fixed

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Fixed = params.get("Fixed")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        r"""
        :param _Default: Default duration in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param _Keys: Custom durations in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param _Need: Required or not.
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        r"""
        :param _Default: Default period in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param _Keys: Custom periods in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param _Need: Required or not.
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        r"""
        :param _Default: Number of default periods.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param _Keys: Number of custom periods.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param _Need: Required or not.
        :type Need: bool
        """
        self._Default = None
        self._Keys = None
        self._Need = None

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Need(self):
        return self._Need

    @Need.setter
    def Need(self, Need):
        self._Need = Need


    def _deserialize(self, params):
        self._Default = params.get("Default")
        self._Keys = params.get("Keys")
        self._Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        r"""
        :param _P5: Data aggregation method in a period of 5 seconds.
Note: This field may return null, indicating that no valid value was found.
        :type P5: str
        :param _P10: Data aggregation method in a period of 10 seconds.
Note: This field may return null, indicating that no valid value was found.
        :type P10: str
        :param _P60: Data aggregation method in a period of 1 minute.
Note: This field may return null, indicating that no valid value was found.
        :type P60: str
        :param _P300: Data aggregation method in a period of 5 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P300: str
        :param _P600: Data aggregation method in a period of 10 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P600: str
        :param _P1800: Data aggregation method in a period of 30 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P1800: str
        :param _P3600: Data aggregation method in a period of 1 hour.
Note: This field may return null, indicating that no valid value was found.
        :type P3600: str
        :param _P86400: Data aggregation method in a period of 1 day.
Note: This field may return null, indicating that no valid value was found.
        :type P86400: str
        """
        self._P5 = None
        self._P10 = None
        self._P60 = None
        self._P300 = None
        self._P600 = None
        self._P1800 = None
        self._P3600 = None
        self._P86400 = None

    @property
    def P5(self):
        return self._P5

    @P5.setter
    def P5(self, P5):
        self._P5 = P5

    @property
    def P10(self):
        return self._P10

    @P10.setter
    def P10(self, P10):
        self._P10 = P10

    @property
    def P60(self):
        return self._P60

    @P60.setter
    def P60(self, P60):
        self._P60 = P60

    @property
    def P300(self):
        return self._P300

    @P300.setter
    def P300(self, P300):
        self._P300 = P300

    @property
    def P600(self):
        return self._P600

    @P600.setter
    def P600(self, P600):
        self._P600 = P600

    @property
    def P1800(self):
        return self._P1800

    @P1800.setter
    def P1800(self, P1800):
        self._P1800 = P1800

    @property
    def P3600(self):
        return self._P3600

    @P3600.setter
    def P3600(self, P3600):
        self._P3600 = P3600

    @property
    def P86400(self):
        return self._P86400

    @P86400.setter
    def P86400(self, P86400):
        self._P86400 = P86400


    def _deserialize(self, params):
        self._P5 = params.get("P5")
        self._P10 = params.get("P10")
        self._P60 = params.get("P60")
        self._P300 = params.get("P300")
        self._P600 = params.get("P600")
        self._P1800 = params.get("P1800")
        self._P3600 = params.get("P3600")
        self._P86400 = params.get("P86400")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID.
        :type EventId: int
        :param _EventShowName: Event name.
        :type EventShowName: str
        :param _NeedRecovered: Whether to recover.
        :type NeedRecovered: bool
        :param _Type: Event type, which is a reserved field. Currently, it is fixed to 2.
        :type Type: int
        """
        self._EventId = None
        self._EventShowName = None
        self._NeedRecovered = None
        self._Type = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventShowName(self):
        return self._EventShowName

    @EventShowName.setter
    def EventShowName(self, EventShowName):
        self._EventShowName = EventShowName

    @property
    def NeedRecovered(self):
        return self._NeedRecovered

    @NeedRecovered.setter
    def NeedRecovered(self, NeedRecovered):
        self._NeedRecovered = NeedRecovered

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._EventShowName = params.get("EventShowName")
        self._NeedRecovered = params.get("NeedRecovered")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListMetric(AbstractModel):
    """Metric alarm configuration.

    """

    def __init__(self):
        r"""
        :param _ConfigManual: Metric configuration.
Note: This field may return null, indicating that no valid value was found.
        :type ConfigManual: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`
        :param _MetricId: Metric ID.
        :type MetricId: int
        :param _MetricShowName: Metric name.
        :type MetricShowName: str
        :param _MetricUnit: Metric unit.
        :type MetricUnit: str
        """
        self._ConfigManual = None
        self._MetricId = None
        self._MetricShowName = None
        self._MetricUnit = None

    @property
    def ConfigManual(self):
        return self._ConfigManual

    @ConfigManual.setter
    def ConfigManual(self, ConfigManual):
        self._ConfigManual = ConfigManual

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def MetricShowName(self):
        return self._MetricShowName

    @MetricShowName.setter
    def MetricShowName(self, MetricShowName):
        self._MetricShowName = MetricShowName

    @property
    def MetricUnit(self):
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit


    def _deserialize(self, params):
        if params.get("ConfigManual") is not None:
            self._ConfigManual = DescribePolicyConditionListConfigManual()
            self._ConfigManual._deserialize(params.get("ConfigManual"))
        self._MetricId = params.get("MetricId")
        self._MetricShowName = params.get("MetricShowName")
        self._MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        """
        self._Module = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList response structure.

    """

    def __init__(self):
        r"""
        :param _Conditions: List of alarm policy conditions.
        :type Conditions: list of DescribePolicyConditionListCondition
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Conditions = None
        self._RequestId = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyConditionListCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePolicyConditionListResponseDeprecatingInfo(AbstractModel):
    """DescribePolicyConditionListResponseDeprecatingInfo

    """

    def __init__(self):
        r"""
        :param _Hidden: Whether to hide
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hidden: bool
        :param _NewViewNames: Names of new views
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewViewNames: list of str
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._Hidden = None
        self._NewViewNames = None
        self._Description = None

    @property
    def Hidden(self):
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def NewViewNames(self):
        return self._NewViewNames

    @NewViewNames.setter
    def NewViewNames(self, NewViewNames):
        self._NewViewNames = NewViewNames

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Hidden = params.get("Hidden")
        self._NewViewNames = params.get("NewViewNames")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoCallback(AbstractModel):
    """User callback information output by the policy query

    """

    def __init__(self):
        r"""
        :param _CallbackUrl: URL of the user callback API.
        :type CallbackUrl: str
        :param _ValidFlag: Status of the user callback API. The value 0 indicates that the API is not verified. The value 1 indicates that the API is verified. The value 2 indicates that a URL exists but the API fails to be verified.
        :type ValidFlag: int
        :param _VerifyCode: Verification code of the user callback API.
        :type VerifyCode: str
        """
        self._CallbackUrl = None
        self._ValidFlag = None
        self._VerifyCode = None

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def ValidFlag(self):
        return self._ValidFlag

    @ValidFlag.setter
    def ValidFlag(self, ValidFlag):
        self._ValidFlag = ValidFlag

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode


    def _deserialize(self, params):
        self._CallbackUrl = params.get("CallbackUrl")
        self._ValidFlag = params.get("ValidFlag")
        self._VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoCondition(AbstractModel):
    """Alarm threshold conditions output by the policy query.

    """

    def __init__(self):
        r"""
        :param _MetricShowName: Metric name.
        :type MetricShowName: str
        :param _Period: Data aggregation period in seconds.
        :type Period: int
        :param _MetricId: Metric ID.
        :type MetricId: int
        :param _RuleId: Threshold rule ID.
        :type RuleId: int
        :param _Unit: Metric unit.
        :type Unit: str
        :param _AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of `triggerTime`.
        :type AlarmNotifyPeriod: int
        :param _CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. The value 7 indicates day-on-day increase. The value 8 indicates day-on-day decrease. The value 9 indicates week-on-week increase. The value 10 indicates week-on-week decrease. The value 11 indicates periodical increase. The value 12 indicates periodical decrease.
        :type CalcType: int
        :param _CalcValue: Threshold.
        :type CalcValue: str
        :param _ContinueTime: Duration at which an alarm will be triggered in seconds.
        :type ContinueTime: int
        :param _MetricName: Alarm metric name.
        :type MetricName: str
        """
        self._MetricShowName = None
        self._Period = None
        self._MetricId = None
        self._RuleId = None
        self._Unit = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._CalcType = None
        self._CalcValue = None
        self._ContinueTime = None
        self._MetricName = None

    @property
    def MetricShowName(self):
        return self._MetricShowName

    @MetricShowName.setter
    def MetricShowName(self, MetricShowName):
        self._MetricShowName = MetricShowName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def ContinueTime(self):
        return self._ContinueTime

    @ContinueTime.setter
    def ContinueTime(self, ContinueTime):
        self._ContinueTime = ContinueTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._MetricShowName = params.get("MetricShowName")
        self._Period = params.get("Period")
        self._MetricId = params.get("MetricId")
        self._RuleId = params.get("RuleId")
        self._Unit = params.get("Unit")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._ContinueTime = params.get("ContinueTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """Template-based policy group information output by the policy query

    """

    def __init__(self):
        r"""
        :param _GroupId: Policy group ID.
        :type GroupId: int
        :param _GroupName: Policy group name.
        :type GroupName: str
        :param _ViewName: Policy type.
        :type ViewName: str
        :param _Remark: Policy group remarks.
        :type Remark: str
        :param _LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: int
        :param _InsertTime: Creation time.
Note: This field may return null, indicating that no valid value was found.
        :type InsertTime: int
        :param _IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        """
        self._GroupId = None
        self._GroupName = None
        self._ViewName = None
        self._Remark = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._IsUnionRule = None

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
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ViewName = params.get("ViewName")
        self._Remark = params.get("Remark")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """Event alarm conditions output by the policy query

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID.
        :type EventId: int
        :param _RuleId: Event alarm rule ID.
        :type RuleId: int
        :param _EventShowName: Event name.
        :type EventShowName: str
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param _AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        """
        self._EventId = None
        self._RuleId = None
        self._EventShowName = None
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventShowName(self):
        return self._EventShowName

    @EventShowName.setter
    def EventShowName(self, EventShowName):
        self._EventShowName = EventShowName

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._RuleId = params.get("RuleId")
        self._EventShowName = params.get("EventShowName")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """Alarm recipient information output by the policy query

    """

    def __init__(self):
        r"""
        :param _ReceiverGroupList: List of alarm recipient group IDs.
        :type ReceiverGroupList: list of int
        :param _ReceiverUserList: List of alarm recipient IDs.
        :type ReceiverUserList: list of int
        :param _StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates “10:0:0”.
        :type StartTime: int
        :param _EndTime: End time of the alarm period. The meaning is the same as that of StartTime.
        :type EndTime: int
        :param _ReceiverType: Recipient type. Valid values: group and user.
        :type ReceiverType: str
        :param _NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".
        :type NotifyWay: list of str
        :param _UidList: Uid of the alarm call recipient.
Note: This field may return null, indicating that no valid value was found.
        :type UidList: list of int
        :param _RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param _RoundInterval: Intervals of alarm call rounds in seconds.
        :type RoundInterval: int
        :param _PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param _NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.
        :type NeedSendNotice: int
        :param _SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).
        :type SendFor: list of str
        :param _RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.
        :type RecoverNotify: list of str
        :param _ReceiveLanguage: Alarm language.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiveLanguage: str
        """
        self._ReceiverGroupList = None
        self._ReceiverUserList = None
        self._StartTime = None
        self._EndTime = None
        self._ReceiverType = None
        self._NotifyWay = None
        self._UidList = None
        self._RoundNumber = None
        self._RoundInterval = None
        self._PersonInterval = None
        self._NeedSendNotice = None
        self._SendFor = None
        self._RecoverNotify = None
        self._ReceiveLanguage = None

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

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
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def UidList(self):
        return self._UidList

    @UidList.setter
    def UidList(self, UidList):
        self._UidList = UidList

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def ReceiveLanguage(self):
        return self._ReceiveLanguage

    @ReceiveLanguage.setter
    def ReceiveLanguage(self, ReceiveLanguage):
        self._ReceiveLanguage = ReceiveLanguage


    def _deserialize(self, params):
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReceiverType = params.get("ReceiverType")
        self._NotifyWay = params.get("NotifyWay")
        self._UidList = params.get("UidList")
        self._RoundNumber = params.get("RoundNumber")
        self._RoundInterval = params.get("RoundInterval")
        self._PersonInterval = params.get("PersonInterval")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._SendFor = params.get("SendFor")
        self._RecoverNotify = params.get("RecoverNotify")
        self._ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID.
        :type GroupId: int
        """
        self._Module = None
        self._GroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Policy group name.
        :type GroupName: str
        :param _ProjectId: ID of the project to which the policy group belongs.
        :type ProjectId: int
        :param _IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.
        :type IsDefault: int
        :param _ViewName: Policy type.
        :type ViewName: str
        :param _Remark: Policy description
        :type Remark: str
        :param _ShowName: Policy type name.
        :type ShowName: str
        :param _LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param _UpdateTime: Last edited time.
        :type UpdateTime: str
        :param _Region: Regions supported by this policy.
        :type Region: list of str
        :param _DimensionGroup: List of policy type dimensions.
        :type DimensionGroup: list of str
        :param _ConditionsConfig: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition
        :param _EventConfig: Product event rule list.
Note: This field may return null, indicating that no valid value was found.
        :type EventConfig: list of DescribePolicyGroupInfoEventCondition
        :param _ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param _Callback: User callback information.
Note: This field may return null, indicating that no valid value was found.
        :type Callback: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`
        :param _ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param _CanSetDefault: Whether the policy can be configured as the default policy.
        :type CanSetDefault: bool
        :param _IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupName = None
        self._ProjectId = None
        self._IsDefault = None
        self._ViewName = None
        self._Remark = None
        self._ShowName = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._Region = None
        self._DimensionGroup = None
        self._ConditionsConfig = None
        self._EventConfig = None
        self._ReceiverInfos = None
        self._Callback = None
        self._ConditionsTemp = None
        self._CanSetDefault = None
        self._IsUnionRule = None
        self._RequestId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ShowName(self):
        return self._ShowName

    @ShowName.setter
    def ShowName(self, ShowName):
        self._ShowName = ShowName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DimensionGroup(self):
        return self._DimensionGroup

    @DimensionGroup.setter
    def DimensionGroup(self, DimensionGroup):
        self._DimensionGroup = DimensionGroup

    @property
    def ConditionsConfig(self):
        return self._ConditionsConfig

    @ConditionsConfig.setter
    def ConditionsConfig(self, ConditionsConfig):
        self._ConditionsConfig = ConditionsConfig

    @property
    def EventConfig(self):
        return self._EventConfig

    @EventConfig.setter
    def EventConfig(self, EventConfig):
        self._EventConfig = EventConfig

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        self._IsDefault = params.get("IsDefault")
        self._ViewName = params.get("ViewName")
        self._Remark = params.get("Remark")
        self._ShowName = params.get("ShowName")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._Region = params.get("Region")
        self._DimensionGroup = params.get("DimensionGroup")
        if params.get("ConditionsConfig") is not None:
            self._ConditionsConfig = []
            for item in params.get("ConditionsConfig"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self._ConditionsConfig.append(obj)
        if params.get("EventConfig") is not None:
            self._EventConfig = []
            for item in params.get("EventConfig"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self._EventConfig.append(obj)
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        if params.get("Callback") is not None:
            self._Callback = DescribePolicyGroupInfoCallback()
            self._Callback._deserialize(params.get("Callback"))
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self._CanSetDefault = params.get("CanSetDefault")
        self._IsUnionRule = params.get("IsUnionRule")
        self._RequestId = params.get("RequestId")


class DescribePolicyGroupListGroup(AbstractModel):
    """DescribePolicyGroupList.Group

    """

    def __init__(self):
        r"""
        :param _GroupId: Policy group ID.
        :type GroupId: int
        :param _GroupName: Policy group name.
        :type GroupName: str
        :param _IsOpen: Whether it is enabled.
        :type IsOpen: bool
        :param _ViewName: Policy view name.
        :type ViewName: str
        :param _LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param _UpdateTime: Last modified time.
        :type UpdateTime: int
        :param _InsertTime: Creation time.
        :type InsertTime: int
        :param _UseSum: Number of instances that are bound to the policy group.
        :type UseSum: int
        :param _NoShieldedSum: Number of unshielded instances that are bound to the policy group.
        :type NoShieldedSum: int
        :param _IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.
        :type IsDefault: int
        :param _CanSetDefault: Whether the policy can be configured as the default policy.
        :type CanSetDefault: bool
        :param _ParentGroupId: Parent policy group ID.
        :type ParentGroupId: int
        :param _Remark: Remarks of the policy group.
        :type Remark: str
        :param _ProjectId: ID of the project to which the policy group belongs.
        :type ProjectId: int
        :param _Conditions: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.
        :type Conditions: list of DescribePolicyGroupInfoCondition
        :param _EventConditions: Product event rule list.
Note: This field may return null, indicating that no valid value was found.
        :type EventConditions: list of DescribePolicyGroupInfoEventCondition
        :param _ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param _ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param _InstanceGroup: Instance group that is bound to the policy group.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`
        :param _IsUnionRule: The 'AND' or 'OR' rule. The value 0 indicates the 'OR' rule (indicating that an alarm will be triggered if any rule meets the threshold condition). The value 1 indicates the 'AND' rule (indicating that an alarm will be triggered when all rules meet the threshold conditions).
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        """
        self._GroupId = None
        self._GroupName = None
        self._IsOpen = None
        self._ViewName = None
        self._LastEditUin = None
        self._UpdateTime = None
        self._InsertTime = None
        self._UseSum = None
        self._NoShieldedSum = None
        self._IsDefault = None
        self._CanSetDefault = None
        self._ParentGroupId = None
        self._Remark = None
        self._ProjectId = None
        self._Conditions = None
        self._EventConditions = None
        self._ReceiverInfos = None
        self._ConditionsTemp = None
        self._InstanceGroup = None
        self._IsUnionRule = None

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
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def UseSum(self):
        return self._UseSum

    @UseSum.setter
    def UseSum(self, UseSum):
        self._UseSum = UseSum

    @property
    def NoShieldedSum(self):
        return self._NoShieldedSum

    @NoShieldedSum.setter
    def NoShieldedSum(self, NoShieldedSum):
        self._NoShieldedSum = NoShieldedSum

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def ParentGroupId(self):
        return self._ParentGroupId

    @ParentGroupId.setter
    def ParentGroupId(self, ParentGroupId):
        self._ParentGroupId = ParentGroupId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def ConditionsTemp(self):
        return self._ConditionsTemp

    @ConditionsTemp.setter
    def ConditionsTemp(self, ConditionsTemp):
        self._ConditionsTemp = ConditionsTemp

    @property
    def InstanceGroup(self):
        return self._InstanceGroup

    @InstanceGroup.setter
    def InstanceGroup(self, InstanceGroup):
        self._InstanceGroup = InstanceGroup

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._IsOpen = params.get("IsOpen")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        self._UseSum = params.get("UseSum")
        self._NoShieldedSum = params.get("NoShieldedSum")
        self._IsDefault = params.get("IsDefault")
        self._CanSetDefault = params.get("CanSetDefault")
        self._ParentGroupId = params.get("ParentGroupId")
        self._Remark = params.get("Remark")
        self._ProjectId = params.get("ProjectId")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        if params.get("ConditionsTemp") is not None:
            self._ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self._ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        if params.get("InstanceGroup") is not None:
            self._InstanceGroup = DescribePolicyGroupListGroupInstanceGroup()
            self._InstanceGroup._deserialize(params.get("InstanceGroup"))
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """Instance group that is bound to a policy group of the DescribePolicyGroupList API

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: Instance group name ID.
        :type InstanceGroupId: int
        :param _ViewName: Policy type view name.
        :type ViewName: str
        :param _LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param _GroupName: Instance group name.
        :type GroupName: str
        :param _InstanceSum: Number of instances.
        :type InstanceSum: int
        :param _UpdateTime: Update time.
        :type UpdateTime: int
        :param _InsertTime: Creation time.
        :type InsertTime: int
        """
        self._InstanceGroupId = None
        self._ViewName = None
        self._LastEditUin = None
        self._GroupName = None
        self._InstanceSum = None
        self._UpdateTime = None
        self._InsertTime = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._ViewName = params.get("ViewName")
        self._LastEditUin = params.get("LastEditUin")
        self._GroupName = params.get("GroupName")
        self._InstanceSum = params.get("InstanceSum")
        self._UpdateTime = params.get("UpdateTime")
        self._InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _Limit: Number of parameters that can be returned on each page. Value range: 1 - 100.
        :type Limit: int
        :param _Offset: Parameter offset on each page. The value starts from 0.
        :type Offset: int
        :param _Like: Search by policy name.
        :type Like: str
        :param _InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param _UpdateTimeOrder: Sort by update time. Valid values: asc and desc.
        :type UpdateTimeOrder: str
        :param _ProjectIds: Project ID list.
        :type ProjectIds: list of int
        :param _ViewNames: List of alarm policy types.
        :type ViewNames: list of str
        :param _FilterUnuseReceiver: Whether to filter policy groups without recipients. The value 1 indicates that policy groups without recipients will be filtered. The value 0 indicates that policy groups without recipients will not be filtered.
        :type FilterUnuseReceiver: int
        :param _Receivers: Filter by recipient group.
        :type Receivers: list of str
        :param _ReceiverUserList: Filter by recipient.
        :type ReceiverUserList: list of str
        :param _Dimensions: Dimension set field (json string), for example, [[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]].
        :type Dimensions: str
        :param _ConditionTempGroupId: Template-based policy group IDs, which are separated by commas.
        :type ConditionTempGroupId: str
        :param _ReceiverType: Filter by recipient or recipient group. The value 'user' indicates by recipient. The value 'group' indicates by recipient group.
        :type ReceiverType: str
        :param _IsOpen: Filter conditions. Whether the alarm policy has been enabled or disabled
        :type IsOpen: bool
        """
        self._Module = None
        self._Limit = None
        self._Offset = None
        self._Like = None
        self._InstanceGroupId = None
        self._UpdateTimeOrder = None
        self._ProjectIds = None
        self._ViewNames = None
        self._FilterUnuseReceiver = None
        self._Receivers = None
        self._ReceiverUserList = None
        self._Dimensions = None
        self._ConditionTempGroupId = None
        self._ReceiverType = None
        self._IsOpen = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Like(self):
        return self._Like

    @Like.setter
    def Like(self, Like):
        self._Like = Like

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def UpdateTimeOrder(self):
        return self._UpdateTimeOrder

    @UpdateTimeOrder.setter
    def UpdateTimeOrder(self, UpdateTimeOrder):
        self._UpdateTimeOrder = UpdateTimeOrder

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ViewNames(self):
        return self._ViewNames

    @ViewNames.setter
    def ViewNames(self, ViewNames):
        self._ViewNames = ViewNames

    @property
    def FilterUnuseReceiver(self):
        return self._FilterUnuseReceiver

    @FilterUnuseReceiver.setter
    def FilterUnuseReceiver(self, FilterUnuseReceiver):
        self._FilterUnuseReceiver = FilterUnuseReceiver

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Like = params.get("Like")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._UpdateTimeOrder = params.get("UpdateTimeOrder")
        self._ProjectIds = params.get("ProjectIds")
        self._ViewNames = params.get("ViewNames")
        self._FilterUnuseReceiver = params.get("FilterUnuseReceiver")
        self._Receivers = params.get("Receivers")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._Dimensions = params.get("Dimensions")
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        self._ReceiverType = params.get("ReceiverType")
        self._IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _GroupList: Policy group list.
Note: This field may return null, indicating that no valid value was found.
        :type GroupList: list of DescribePolicyGroupListGroup
        :param _Total: Total number of policy groups.
        :type Total: int
        :param _Warning: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warning: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupList = None
        self._Total = None
        self._Warning = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Warning(self):
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._Total = params.get("Total")
        self._Warning = params.get("Warning")
        self._RequestId = params.get("RequestId")


class DescribeProductEventListDimensions(AbstractModel):
    """Input parameter Dimensions of the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param _Name: Dimension name.
        :type Name: str
        :param _Value: Dimension value.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class DescribeProductEventListEvents(AbstractModel):
    """Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID.
Note: This field may return null, indicating that no valid value was found.
        :type EventId: int
        :param _EventCName: Event name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type EventCName: str
        :param _EventEName: Event name in English.
Note: This field may return null, indicating that no valid value was found.
        :type EventEName: str
        :param _EventName: Event name abbreviation.
Note: This field may return null, indicating that no valid value was found.
        :type EventName: str
        :param _ProductCName: Product name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type ProductCName: str
        :param _ProductEName: Product name in English.
Note: This field may return null, indicating that no valid value was found.
        :type ProductEName: str
        :param _ProductName: Product name abbreviation.
Note: This field may return null, indicating that no valid value was found.
        :type ProductName: str
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceId: str
        :param _InstanceName: Instance name.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceName: str
        :param _ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectId: str
        :param _Region: Region.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param _Status: Status.
Note: This field may return null, indicating that no valid value was found.
        :type Status: str
        :param _SupportAlarm: Whether to support alarms.
Note: This field may return null, indicating that no valid value was found.
        :type SupportAlarm: int
        :param _Type: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type Type: str
        :param _StartTime: Start time.
Note: This field may return null, indicating that no valid value was found.
        :type StartTime: int
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: int
        :param _Dimensions: Instance object information.
Note: This field may return null, indicating that no valid value was found.
        :type Dimensions: list of DescribeProductEventListEventsDimensions
        :param _AdditionMsg: Additional information of the instance object.
Note: This field may return null, indicating that no valid value was found.
        :type AdditionMsg: list of DescribeProductEventListEventsDimensions
        :param _IsAlarmConfig: Whether to configure alarms.
Note: This field may return null, indicating that no valid value was found.
        :type IsAlarmConfig: int
        :param _GroupInfo: Policy information.
Note: This field may return null, indicating that no valid value was found.
        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo
        :param _ViewName: Display name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ViewName: str
        """
        self._EventId = None
        self._EventCName = None
        self._EventEName = None
        self._EventName = None
        self._ProductCName = None
        self._ProductEName = None
        self._ProductName = None
        self._InstanceId = None
        self._InstanceName = None
        self._ProjectId = None
        self._Region = None
        self._Status = None
        self._SupportAlarm = None
        self._Type = None
        self._StartTime = None
        self._UpdateTime = None
        self._Dimensions = None
        self._AdditionMsg = None
        self._IsAlarmConfig = None
        self._GroupInfo = None
        self._ViewName = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def EventCName(self):
        return self._EventCName

    @EventCName.setter
    def EventCName(self, EventCName):
        self._EventCName = EventCName

    @property
    def EventEName(self):
        return self._EventEName

    @EventEName.setter
    def EventEName(self, EventEName):
        self._EventEName = EventEName

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def ProductCName(self):
        return self._ProductCName

    @ProductCName.setter
    def ProductCName(self, ProductCName):
        self._ProductCName = ProductCName

    @property
    def ProductEName(self):
        return self._ProductEName

    @ProductEName.setter
    def ProductEName(self, ProductEName):
        self._ProductEName = ProductEName

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SupportAlarm(self):
        return self._SupportAlarm

    @SupportAlarm.setter
    def SupportAlarm(self, SupportAlarm):
        self._SupportAlarm = SupportAlarm

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def AdditionMsg(self):
        return self._AdditionMsg

    @AdditionMsg.setter
    def AdditionMsg(self, AdditionMsg):
        self._AdditionMsg = AdditionMsg

    @property
    def IsAlarmConfig(self):
        return self._IsAlarmConfig

    @IsAlarmConfig.setter
    def IsAlarmConfig(self, IsAlarmConfig):
        self._IsAlarmConfig = IsAlarmConfig

    @property
    def GroupInfo(self):
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._EventCName = params.get("EventCName")
        self._EventEName = params.get("EventEName")
        self._EventName = params.get("EventName")
        self._ProductCName = params.get("ProductCName")
        self._ProductEName = params.get("ProductEName")
        self._ProductName = params.get("ProductName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._SupportAlarm = params.get("SupportAlarm")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        if params.get("AdditionMsg") is not None:
            self._AdditionMsg = []
            for item in params.get("AdditionMsg"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self._AdditionMsg.append(obj)
        self._IsAlarmConfig = params.get("IsAlarmConfig")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = DescribeProductEventListEventsGroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsDimensions(AbstractModel):
    """Dimensions of events returned by the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param _Key: Dimension name in English.
Note: This field may return null, indicating that no valid value was found.
        :type Key: str
        :param _Name: Dimension name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type Name: str
        :param _Value: Dimension value.
Note: This field may return null, indicating that no valid value was found.
        :type Value: str
        """
        self._Key = None
        self._Name = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """GroupInfo in Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param _GroupId: Policy ID.
Note: This field may return null, indicating that no valid value was found.
        :type GroupId: int
        :param _GroupName: Policy name.
Note: This field may return null, indicating that no valid value was found.
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

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


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListOverView(AbstractModel):
    """OverView object returned by the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param _StatusChangeAmount: Number of events whose statuses have changed.
Note: This field may return null, indicating that no valid value was found.
        :type StatusChangeAmount: int
        :param _UnConfigAlarmAmount: Number of events whose alarm statuses are not configured.
Note: This field may return null, indicating that no valid value was found.
        :type UnConfigAlarmAmount: int
        :param _UnNormalEventAmount: Number of events with exceptions.
Note: This field may return null, indicating that no valid value was found.
        :type UnNormalEventAmount: int
        :param _UnRecoverAmount: Number of events that have not been recovered.
Note: This field may return null, indicating that no valid value was found.
        :type UnRecoverAmount: int
        """
        self._StatusChangeAmount = None
        self._UnConfigAlarmAmount = None
        self._UnNormalEventAmount = None
        self._UnRecoverAmount = None

    @property
    def StatusChangeAmount(self):
        return self._StatusChangeAmount

    @StatusChangeAmount.setter
    def StatusChangeAmount(self, StatusChangeAmount):
        self._StatusChangeAmount = StatusChangeAmount

    @property
    def UnConfigAlarmAmount(self):
        return self._UnConfigAlarmAmount

    @UnConfigAlarmAmount.setter
    def UnConfigAlarmAmount(self, UnConfigAlarmAmount):
        self._UnConfigAlarmAmount = UnConfigAlarmAmount

    @property
    def UnNormalEventAmount(self):
        return self._UnNormalEventAmount

    @UnNormalEventAmount.setter
    def UnNormalEventAmount(self, UnNormalEventAmount):
        self._UnNormalEventAmount = UnNormalEventAmount

    @property
    def UnRecoverAmount(self):
        return self._UnRecoverAmount

    @UnRecoverAmount.setter
    def UnRecoverAmount(self, UnRecoverAmount):
        self._UnRecoverAmount = UnRecoverAmount


    def _deserialize(self, params):
        self._StatusChangeAmount = params.get("StatusChangeAmount")
        self._UnConfigAlarmAmount = params.get("UnConfigAlarmAmount")
        self._UnNormalEventAmount = params.get("UnNormalEventAmount")
        self._UnRecoverAmount = params.get("UnRecoverAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList request structure.

    """

    def __init__(self):
        r"""
        :param _Module: API component name. It is fixed to monitor.
        :type Module: str
        :param _ProductName: Filter by product type. For example, "cvm" indicates Cloud Virtual Machine.
        :type ProductName: list of str
        :param _EventName: Filter by event name. For example, "guest_reboot" indicates instance restart.
        :type EventName: list of str
        :param _InstanceId: Affected object, such as "ins-19708ino".
        :type InstanceId: list of str
        :param _Dimensions: Filter by dimension, such as by public IP: 10.0.0.1.
        :type Dimensions: list of DescribeProductEventListDimensions
        :param _RegionList: Region filter parameter for service events.
        :type RegionList: list of str
        :param _Type: Filter by event type. Valid values: ["status_change","abnormal"], which indicate events whose statuses have changed and events with exceptions respectively.
        :type Type: list of str
        :param _Status: Filter by event status. Valid values: ["recover","alarm","-"], which indicate that an event has been recovered, has not been recovered, and has no status respectively.
        :type Status: list of str
        :param _Project: Filter by project ID.
        :type Project: list of str
        :param _IsAlarmConfig: Filter by alarm status configuration. The value 1 indicates that the alarm status has been configured. The value 0 indicates that the alarm status has not been configured.
        :type IsAlarmConfig: int
        :param _TimeOrder: Sorting by update time. The value ASC indicates the ascending order. The value DESC indicates the descending order. The default value is DESC.
        :type TimeOrder: str
        :param _StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param _EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param _Offset: Page offset. The default value is 0.
        :type Offset: int
        :param _Limit: The number of parameters that can be returned on each page. The default value is 20.
        :type Limit: int
        """
        self._Module = None
        self._ProductName = None
        self._EventName = None
        self._InstanceId = None
        self._Dimensions = None
        self._RegionList = None
        self._Type = None
        self._Status = None
        self._Project = None
        self._IsAlarmConfig = None
        self._TimeOrder = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def IsAlarmConfig(self):
        return self._IsAlarmConfig

    @IsAlarmConfig.setter
    def IsAlarmConfig(self, IsAlarmConfig):
        self._IsAlarmConfig = IsAlarmConfig

    @property
    def TimeOrder(self):
        return self._TimeOrder

    @TimeOrder.setter
    def TimeOrder(self, TimeOrder):
        self._TimeOrder = TimeOrder

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
        self._Module = params.get("Module")
        self._ProductName = params.get("ProductName")
        self._EventName = params.get("EventName")
        self._InstanceId = params.get("InstanceId")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListDimensions()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._RegionList = params.get("RegionList")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Project = params.get("Project")
        self._IsAlarmConfig = params.get("IsAlarmConfig")
        self._TimeOrder = params.get("TimeOrder")
        self._StartTime = params.get("StartTime")
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
        


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList response structure.

    """

    def __init__(self):
        r"""
        :param _Events: Event list
Note: This field may return null, indicating that no valid value was found.
        :type Events: list of DescribeProductEventListEvents
        :param _OverView: Event statistics.
        :type OverView: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListOverView`
        :param _Total: Total number of events.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Events = None
        self._OverView = None
        self._Total = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def OverView(self):
        return self._OverView

    @OverView.setter
    def OverView(self, OverView):
        self._OverView = OverView

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = DescribeProductEventListEvents()
                obj._deserialize(item)
                self._Events.append(obj)
        if params.get("OverView") is not None:
            self._OverView = DescribeProductEventListOverView()
            self._OverView._deserialize(params.get("OverView"))
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
It can be the ID of a TKE, EKS, or edge cluster.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: List of instances associated with the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Instances: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Instances = params.get("Instances")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Agent name
        :type Name: str
        :param _AgentIds: List of agent IDs
        :type AgentIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceId = None
        self._Name = None
        self._AgentIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentIds(self):
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds

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
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._AgentIds = params.get("AgentIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents response structure.

    """

    def __init__(self):
        r"""
        :param _AgentSet: List of agents
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentSet: list of PrometheusAgent
        :param _TotalCount: Total number of agents
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AgentSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AgentSet(self):
        return self._AgentSet

    @AgentSet.setter
    def AgentSet(self, AgentSet):
        self._AgentSet = AgentSet

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
        if params.get("AgentSet") is not None:
            self._AgentSet = []
            for item in params.get("AgentSet"):
                obj = PrometheusAgent()
                obj._deserialize(item)
                self._AgentSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusAlertPolicyRequest(AbstractModel):
    """DescribePrometheusAlertPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _Filters: Filter
Valid values: `ID`, `Name`.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
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
        


class DescribePrometheusAlertPolicyResponse(AbstractModel):
    """DescribePrometheusAlertPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _AlertRules: Alert details
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRules: list of PrometheusAlertPolicyItem
        :param _Total: Total number
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlertRules = None
        self._Total = None
        self._RequestId = None

    @property
    def AlertRules(self):
        return self._AlertRules

    @AlertRules.setter
    def AlertRules(self, AlertRules):
        self._AlertRules = AlertRules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlertRules") is not None:
            self._AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertRules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusClusterAgentsRequest(AbstractModel):
    """DescribePrometheusClusterAgents request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Page limit
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusClusterAgentsResponse(AbstractModel):
    """DescribePrometheusClusterAgents response structure.

    """

    def __init__(self):
        r"""
        :param _Agents: Information of the associated cluster
        :type Agents: list of PrometheusAgentOverview
        :param _Total: The total number of the associated clusters
        :type Total: int
        :param _IsFirstBind: Whether the TMP instance is associated with the cluster for the first time. If so, you need to configure recording rules for it. This also applies if it has no default recording rule.
        :type IsFirstBind: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Agents = None
        self._Total = None
        self._IsFirstBind = None
        self._RequestId = None

    @property
    def Agents(self):
        return self._Agents

    @Agents.setter
    def Agents(self, Agents):
        self._Agents = Agents

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def IsFirstBind(self):
        return self._IsFirstBind

    @IsFirstBind.setter
    def IsFirstBind(self, IsFirstBind):
        self._IsFirstBind = IsFirstBind

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self._Agents = []
            for item in params.get("Agents"):
                obj = PrometheusAgentOverview()
                obj._deserialize(item)
                self._Agents.append(obj)
        self._Total = params.get("Total")
        self._IsFirstBind = params.get("IsFirstBind")
        self._RequestId = params.get("RequestId")


class DescribePrometheusConfigRequest(AbstractModel):
    """DescribePrometheusConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        """
        self._InstanceId = None
        self._ClusterId = None
        self._ClusterType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusConfigResponse(AbstractModel):
    """DescribePrometheusConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Config: Global configuration
        :type Config: str
        :param _ServiceMonitors: ServiceMonitor configuration
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: PodMonitor configuration
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: Raw jobs
        :type RawJobs: list of PrometheusConfigItem
        :param _Probes: Probes
        :type Probes: list of PrometheusConfigItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Config = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._Probes = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def Probes(self):
        return self._Probes

    @Probes.setter
    def Probes(self, Probes):
        self._Probes = Probes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("Probes") is not None:
            self._Probes = []
            for item in params.get("Probes"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._Probes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusGlobalConfigRequest(AbstractModel):
    """DescribePrometheusGlobalConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance-level scrape configuration
        :type InstanceId: str
        :param _DisableStatistics: Whether to disable statistics
        :type DisableStatistics: bool
        """
        self._InstanceId = None
        self._DisableStatistics = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DisableStatistics(self):
        return self._DisableStatistics

    @DisableStatistics.setter
    def DisableStatistics(self, DisableStatistics):
        self._DisableStatistics = DisableStatistics


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DisableStatistics = params.get("DisableStatistics")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusGlobalConfigResponse(AbstractModel):
    """DescribePrometheusGlobalConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Config: Configuration content
        :type Config: str
        :param _ServiceMonitors: List of service monitors and the corresponding targets information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: List of pod monitors and the corresponding targets information
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: List of raw jobs and the corresponding targets information
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawJobs: list of PrometheusConfigItem
        :param _Probes: List of probes and the corresponding targets information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Probes: list of PrometheusConfigItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Config = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._Probes = None
        self._RequestId = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def Probes(self):
        return self._Probes

    @Probes.setter
    def Probes(self, Probes):
        self._Probes = Probes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Config = params.get("Config")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("Probes") is not None:
            self._Probes = []
            for item in params.get("Probes"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._Probes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusGlobalNotificationRequest(AbstractModel):
    """DescribePrometheusGlobalNotification request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusGlobalNotificationResponse(AbstractModel):
    """DescribePrometheusGlobalNotification response structure.

    """

    def __init__(self):
        r"""
        :param _Notification: Global alert notification channel
Note: This field may return null, indicating that no valid values can be obtained.
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Notification = None
        self._RequestId = None

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceDetailRequest(AbstractModel):
    """DescribePrometheusInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceDetailResponse(AbstractModel):
    """DescribePrometheusInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _InstanceStatus: Instance status. Valid values:

`1`: Creating
`2`: Running
`3`: Abnormal
`4`: Rebooting
`5`: Terminating
`6`: Service suspended
`8`: Suspending service for overdue payment
`9`: Service suspended for overdue payment
        :type InstanceStatus: int
        :param _ChargeStatus: Billing status

`1`: Normal
`2`: Expired
`3`: Terminated
`4`: Assigning
`5`: Failed to assign
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param _EnableGrafana: Whether Grafana is enabled
`0`: Disabled
`1`: Enabled
        :type EnableGrafana: int
        :param _GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param _InstanceChargeType: Instance billing mode. Valid values:

`2`: Monthly subscription
`3`: Pay-as-you-go
        :type InstanceChargeType: int
        :param _SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param _ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AutoRenewFlag: Auto-renewal flag

`0`: Auto-renewal not enabled
`1`: Auto-renewal enabled
`2`: Auto-renewal prohibited
`-1`: Invalid
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceStatus = None
        self._ChargeStatus = None
        self._EnableGrafana = None
        self._GrafanaURL = None
        self._InstanceChargeType = None
        self._SpecName = None
        self._DataRetentionTime = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._RequestId = None

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
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ChargeStatus = params.get("ChargeStatus")
        self._EnableGrafana = params.get("EnableGrafana")
        self._GrafanaURL = params.get("GrafanaURL")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SpecName = params.get("SpecName")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceInitStatusRequest(AbstractModel):
    """DescribePrometheusInstanceInitStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceInitStatusResponse(AbstractModel):
    """DescribePrometheusInstanceInitStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Instance initialization status. Valid values:
`uninitialized` 
`initializing`
`running`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Steps: Initialize task steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type Steps: list of TaskStepInfo
        :param _EksClusterId: EKS cluster ID of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type EksClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Steps = None
        self._EksClusterId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def EksClusterId(self):
        return self._EksClusterId

    @EksClusterId.setter
    def EksClusterId(self, EksClusterId):
        self._EksClusterId = EksClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._EksClusterId = params.get("EksClusterId")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceUsageRequest(AbstractModel):
    """DescribePrometheusInstanceUsage request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Query by one or more instance IDs. Instance ID is in the format of `prom-xxxxxxxx`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param _StartCalcDate: Start time
        :type StartCalcDate: str
        :param _EndCalcDate: End time
        :type EndCalcDate: str
        """
        self._InstanceIds = None
        self._StartCalcDate = None
        self._EndCalcDate = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StartCalcDate(self):
        return self._StartCalcDate

    @StartCalcDate.setter
    def StartCalcDate(self, StartCalcDate):
        self._StartCalcDate = StartCalcDate

    @property
    def EndCalcDate(self):
        return self._EndCalcDate

    @EndCalcDate.setter
    def EndCalcDate(self, EndCalcDate):
        self._EndCalcDate = EndCalcDate


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._StartCalcDate = params.get("StartCalcDate")
        self._EndCalcDate = params.get("EndCalcDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceUsageResponse(AbstractModel):
    """DescribePrometheusInstanceUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageSet: Usage list
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageSet: list of PrometheusInstanceTenantUsage
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageSet = None
        self._RequestId = None

    @property
    def UsageSet(self):
        return self._UsageSet

    @UsageSet.setter
    def UsageSet(self, UsageSet):
        self._UsageSet = UsageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsageSet") is not None:
            self._UsageSet = []
            for item in params.get("UsageSet"):
                obj = PrometheusInstanceTenantUsage()
                obj._deserialize(item)
                self._UsageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstancesOverviewRequest(AbstractModel):
    """DescribePrometheusInstancesOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _Filters: Instance filter. Valid values:
`ID`: Filter by instance ID 
`Name`: Filter by instance name
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
        


class DescribePrometheusInstancesOverviewResponse(AbstractModel):
    """DescribePrometheusInstancesOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: List of instances
        :type Instances: list of PrometheusInstancesOverview
        :param _Total: Total number of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._Total = None
        self._RequestId = None

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = PrometheusInstancesOverview()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstancesRequest(AbstractModel):
    """DescribePrometheusInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Queries by instance ID or IDs. Instance ID is in the format of `prom-xxxxxxxx`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param _InstanceStatus: Filter by instance status
<ul>
<li>1: Creating</li>
<li>2: Running</li>
<li>3: Abnormal</li>
<li>4: Rebooting</li>
<li>5: Terminating</li>
<li>6: Service suspended</li>
<li>8: Suspending service for overdue payment</li>
<li>9: Service suspended for overdue payment</li>
</ul>
        :type InstanceStatus: list of int
        :param _InstanceName: Filter by instance name
        :type InstanceName: str
        :param _Zones: Filter by AZ in the format of `ap-guangzhou-1`
        :type Zones: list of str
        :param _TagFilters: Filter by tag key-value pair. The `tag-key` should be replaced with a specific tag key.
        :type TagFilters: list of PrometheusTag
        :param _IPv4Address: Filter by instance IPv4 address
        :type IPv4Address: list of str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _InstanceChargeType: Filter by billing mode
<li>2: Monthly subscription</li>
<li>3: Pay-as-you-go</li>
        :type InstanceChargeType: int
        """
        self._InstanceIds = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._Zones = None
        self._TagFilters = None
        self._IPv4Address = None
        self._Limit = None
        self._Offset = None
        self._InstanceChargeType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def IPv4Address(self):
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._Zones = params.get("Zones")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._IPv4Address = params.get("IPv4Address")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstancesResponse(AbstractModel):
    """DescribePrometheusInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceSet: List of instance details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceSet: list of PrometheusInstancesItem
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = PrometheusInstancesItem()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusRecordRuleYamlRequest(AbstractModel):
    """DescribePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _Filters: Filter. Valid values:
`Name`: Name
`Values`: List of target names
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
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
        


class DescribePrometheusRecordRuleYamlResponse(AbstractModel):
    """DescribePrometheusRecordRuleYaml response structure.

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


class DescribePrometheusRecordRulesRequest(AbstractModel):
    """DescribePrometheusRecordRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
        :type Limit: int
        :param _Filters: Filter
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
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
        


class DescribePrometheusRecordRulesResponse(AbstractModel):
    """DescribePrometheusRecordRules response structure.

    """

    def __init__(self):
        r"""
        :param _Records: Recording rule
        :type Records: list of PrometheusRecordRuleYamlItem
        :param _Total: Total number
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Records = None
        self._Total = None
        self._RequestId = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = PrometheusRecordRuleYamlItem()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusScrapeJobsRequest(AbstractModel):
    """DescribePrometheusScrapeJobs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _Name: Task name
        :type Name: str
        :param _JobIds: List of task IDs
        :type JobIds: list of str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._InstanceId = None
        self._AgentId = None
        self._Name = None
        self._JobIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

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
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._JobIds = params.get("JobIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusScrapeJobsResponse(AbstractModel):
    """DescribePrometheusScrapeJobs response structure.

    """

    def __init__(self):
        r"""
        :param _ScrapeJobSet: List of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScrapeJobSet: list of PrometheusScrapeJob
        :param _TotalCount: Total number of tasks
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScrapeJobSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScrapeJobSet(self):
        return self._ScrapeJobSet

    @ScrapeJobSet.setter
    def ScrapeJobSet(self, ScrapeJobSet):
        self._ScrapeJobSet = ScrapeJobSet

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
        if params.get("ScrapeJobSet") is not None:
            self._ScrapeJobSet = []
            for item in params.get("ScrapeJobSet"):
                obj = PrometheusScrapeJob()
                obj._deserialize(item)
                self._ScrapeJobSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrometheusTargetsTMPRequest(AbstractModel):
    """DescribePrometheusTargetsTMP request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Filters: Filters.
You can filter by `RawJob`, `Job`, `ServiceMonitor`, `PodMonitor`, or `Health`.
`Health` contains three values: `up`, `down`, `unknown`.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
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
        


class DescribePrometheusTargetsTMPResponse(AbstractModel):
    """DescribePrometheusTargetsTMP response structure.

    """

    def __init__(self):
        r"""
        :param _Jobs: Targets information of all jobs
        :type Jobs: list of PrometheusJobTargets
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = PrometheusJobTargets()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusTempRequest(AbstractModel):
    """DescribePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Fuzzy filter. Valid values:
`Level`: Filter by template level
`Name`: Filter by name
`Describe`: Filter by description
`ID`: Filter by templateId
        :type Filters: list of Filter
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of results per page
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
        


class DescribePrometheusTempResponse(AbstractModel):
    """DescribePrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param _Templates: List of templates
        :type Templates: list of PrometheusTemp
        :param _Total: Total number
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Templates = None
        self._Total = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = PrometheusTemp()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribePrometheusTempSyncRequest(AbstractModel):
    """DescribePrometheusTempSync request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempSyncResponse(AbstractModel):
    """DescribePrometheusTempSync response structure.

    """

    def __init__(self):
        r"""
        :param _Targets: Details of the sync target
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of PrometheusTemplateSyncTarget
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Targets = None
        self._RequestId = None

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusZonesRequest(AbstractModel):
    """DescribePrometheusZones request structure.

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID. You only need to specify the value of either `RegionId` or `RegionName`.
        :type RegionId: int
        :param _RegionName: Region name. You only need to specify the value of either `RegionId` or `RegionName`.
        :type RegionName: str
        """
        self._RegionId = None
        self._RegionName = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusZonesResponse(AbstractModel):
    """DescribePrometheusZones response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneSet: Region list
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneSet: list of PrometheusZoneItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneSet = None
        self._RequestId = None

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = PrometheusZoneItem()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordingRulesRequest(AbstractModel):
    """DescribeRecordingRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param _Name: Rule name
        :type Name: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._RuleId = None
        self._RuleState = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingRulesResponse(AbstractModel):
    """DescribeRecordingRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of rule groups
        :type TotalCount: int
        :param _RecordingRuleSet: Rule group details
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordingRuleSet: list of RecordingRuleSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordingRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordingRuleSet(self):
        return self._RecordingRuleSet

    @RecordingRuleSet.setter
    def RecordingRuleSet(self, RecordingRuleSet):
        self._RecordingRuleSet = RecordingRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordingRuleSet") is not None:
            self._RecordingRuleSet = []
            for item in params.get("RecordingRuleSet"):
                obj = RecordingRuleSet()
                obj._deserialize(item)
                self._RecordingRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSSOAccountRequest(AbstractModel):
    """DescribeSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _UserId: Filter by account ID such as “10000”
        :type UserId: str
        """
        self._InstanceId = None
        self._UserId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSSOAccountResponse(AbstractModel):
    """DescribeSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param _AccountSet: List of authorized accounts
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountSet: list of GrafanaAccountInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountSet = None
        self._RequestId = None

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = GrafanaAccountInfo()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceDiscoveryRequest(AbstractModel):
    """DescribeServiceDiscovery request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _KubeClusterId: <li>TKE: ID of the integrated TKE cluster</li>
        :type KubeClusterId: str
        :param _KubeType: Kubernetes cluster type:
<li> 1 = TKE </li>
        :type KubeType: int
        """
        self._InstanceId = None
        self._KubeClusterId = None
        self._KubeType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeClusterId(self):
        return self._KubeClusterId

    @KubeClusterId.setter
    def KubeClusterId(self, KubeClusterId):
        self._KubeClusterId = KubeClusterId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeClusterId = params.get("KubeClusterId")
        self._KubeType = params.get("KubeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceDiscoveryResponse(AbstractModel):
    """DescribeServiceDiscovery response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceDiscoverySet: List of returned scrape configurations
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDiscoverySet: list of ServiceDiscoveryItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceDiscoverySet = None
        self._RequestId = None

    @property
    def ServiceDiscoverySet(self):
        return self._ServiceDiscoverySet

    @ServiceDiscoverySet.setter
    def ServiceDiscoverySet(self, ServiceDiscoverySet):
        self._ServiceDiscoverySet = ServiceDiscoverySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceDiscoverySet") is not None:
            self._ServiceDiscoverySet = []
            for item in params.get("ServiceDiscoverySet"):
                obj = ServiceDiscoveryItem()
                obj._deserialize(item)
                self._ServiceDiscoverySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStatisticDataRequest(AbstractModel):
    """DescribeStatisticData request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module, whose value is fixed at `monitor`
        :type Module: str
        :param _Namespace: Namespace. Valid values: `QCE`, `TKE2`.
        :type Namespace: str
        :param _MetricNames: Metric name list
        :type MetricNames: list of str
        :param _Conditions: Dimension condition. The `=` and `in` operators are supported
        :type Conditions: list of MidQueryCondition
        :param _Period: Statistical period in seconds. Default value: 300. Optional values: 60, 300, 3,600, and 86,400.
Due to the storage period limit, the statistical period is subject to the time range of statistics:
60s: The time range is less than 12 hours, and the timespan between `StartTime` and the current time cannot exceed 15 days.
300s: The time range is less than three days, and the timespan between `StartTime` and the current time cannot exceed 31 days.
3,600s: The time range is less than 30 days, and the timespan between `StartTime` and the current time cannot exceed 93 days.
86,400s: The time range is less than 186 days, and the timespan between `StartTime` and the current time cannot exceed 186 days.
        :type Period: int
        :param _StartTime: Start time, which is the current time by default, such as 2020-12-08T19:51:23+08:00
        :type StartTime: str
        :param _EndTime: End time, which is the current time by default, such as 2020-12-08T19:51:23+08:00
        :type EndTime: str
        :param _GroupBys: `groupBy` by the specified dimension
        :type GroupBys: list of str
        """
        self._Module = None
        self._Namespace = None
        self._MetricNames = None
        self._Conditions = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._GroupBys = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def GroupBys(self):
        return self._GroupBys

    @GroupBys.setter
    def GroupBys(self, GroupBys):
        self._GroupBys = GroupBys


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Namespace = params.get("Namespace")
        self._MetricNames = params.get("MetricNames")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = MidQueryCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GroupBys = params.get("GroupBys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticDataResponse(AbstractModel):
    """DescribeStatisticData response structure.

    """

    def __init__(self):
        r"""
        :param _Period: Statistical period
        :type Period: int
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Data: Monitoring data
        :type Data: list of MetricData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyPrometheusInstanceRequest(AbstractModel):
    """DestroyPrometheusInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. The instance must be terminated first.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPrometheusInstanceResponse(AbstractModel):
    """DestroyPrometheusInstance response structure.

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


class Dimension(AbstractModel):
    """Combination of instance object dimensions

    """

    def __init__(self):
        r"""
        :param _Name: Instance dimension name
        :type Name: str
        :param _Value: Instance dimension value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class DimensionNew(AbstractModel):
    """Dimension information of the policy type

    """

    def __init__(self):
        r"""
        :param _Key: Dimension key ID displayed on the backend
        :type Key: str
        :param _Name: Dimension key name displayed on the frontend
        :type Name: str
        :param _IsRequired: Whether it is required
        :type IsRequired: bool
        :param _Operators: List of supported operators
        :type Operators: list of Operator
        :param _IsMultiple: Whether multiple items can be selected
        :type IsMultiple: bool
        :param _IsMutable: Whether it can be modified after creation
        :type IsMutable: bool
        :param _IsVisible: Whether it is displayed to users
        :type IsVisible: bool
        :param _CanFilterPolicy: Whether it can be used to filter policies
        :type CanFilterPolicy: bool
        :param _CanFilterHistory: Whether it can be used to filter historical alarms
        :type CanFilterHistory: bool
        :param _CanGroupBy: Whether it can be used as an aggregate dimension
        :type CanGroupBy: bool
        :param _MustGroupBy: Whether it must be used as an aggregate dimension
        :type MustGroupBy: bool
        :param _ShowValueReplace: The key to be replaced on the frontend
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowValueReplace: str
        """
        self._Key = None
        self._Name = None
        self._IsRequired = None
        self._Operators = None
        self._IsMultiple = None
        self._IsMutable = None
        self._IsVisible = None
        self._CanFilterPolicy = None
        self._CanFilterHistory = None
        self._CanGroupBy = None
        self._MustGroupBy = None
        self._ShowValueReplace = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsRequired(self):
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Operators(self):
        return self._Operators

    @Operators.setter
    def Operators(self, Operators):
        self._Operators = Operators

    @property
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsMutable(self):
        return self._IsMutable

    @IsMutable.setter
    def IsMutable(self, IsMutable):
        self._IsMutable = IsMutable

    @property
    def IsVisible(self):
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, IsVisible):
        self._IsVisible = IsVisible

    @property
    def CanFilterPolicy(self):
        return self._CanFilterPolicy

    @CanFilterPolicy.setter
    def CanFilterPolicy(self, CanFilterPolicy):
        self._CanFilterPolicy = CanFilterPolicy

    @property
    def CanFilterHistory(self):
        return self._CanFilterHistory

    @CanFilterHistory.setter
    def CanFilterHistory(self, CanFilterHistory):
        self._CanFilterHistory = CanFilterHistory

    @property
    def CanGroupBy(self):
        return self._CanGroupBy

    @CanGroupBy.setter
    def CanGroupBy(self, CanGroupBy):
        self._CanGroupBy = CanGroupBy

    @property
    def MustGroupBy(self):
        return self._MustGroupBy

    @MustGroupBy.setter
    def MustGroupBy(self, MustGroupBy):
        self._MustGroupBy = MustGroupBy

    @property
    def ShowValueReplace(self):
        return self._ShowValueReplace

    @ShowValueReplace.setter
    def ShowValueReplace(self, ShowValueReplace):
        self._ShowValueReplace = ShowValueReplace


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._IsRequired = params.get("IsRequired")
        if params.get("Operators") is not None:
            self._Operators = []
            for item in params.get("Operators"):
                obj = Operator()
                obj._deserialize(item)
                self._Operators.append(obj)
        self._IsMultiple = params.get("IsMultiple")
        self._IsMutable = params.get("IsMutable")
        self._IsVisible = params.get("IsVisible")
        self._CanFilterPolicy = params.get("CanFilterPolicy")
        self._CanFilterHistory = params.get("CanFilterHistory")
        self._CanGroupBy = params.get("CanGroupBy")
        self._MustGroupBy = params.get("MustGroupBy")
        self._ShowValueReplace = params.get("ShowValueReplace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionsDesc(AbstractModel):
    """Dimension information

    """

    def __init__(self):
        r"""
        :param _Dimensions: Array of dimension names
        :type Dimensions: list of str
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        self._Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetRequest(AbstractModel):
    """EnableGrafanaInternet request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: TCMG instance ID, such as “grafana-kleu3gt0”.
        :type InstanceID: str
        :param _EnableInternet: Whether to enable public network access (`true`: Yes; `false`: No)
        :type EnableInternet: bool
        """
        self._InstanceID = None
        self._EnableInternet = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._EnableInternet = params.get("EnableInternet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetResponse(AbstractModel):
    """EnableGrafanaInternet response structure.

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


class EnableGrafanaSSORequest(AbstractModel):
    """EnableGrafanaSSO request structure.

    """

    def __init__(self):
        r"""
        :param _EnableSSO: Whether to enable SSO (`true`: Yes; `false`: No)
        :type EnableSSO: bool
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._EnableSSO = None
        self._InstanceId = None

    @property
    def EnableSSO(self):
        return self._EnableSSO

    @EnableSSO.setter
    def EnableSSO(self, EnableSSO):
        self._EnableSSO = EnableSSO

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EnableSSO = params.get("EnableSSO")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaSSOResponse(AbstractModel):
    """EnableGrafanaSSO response structure.

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


class EnableSSOCamCheckRequest(AbstractModel):
    """EnableSSOCamCheck request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _EnableSSOCamCheck: Whether to enable CAM authentication (`true`: Yes; `false`: No)
        :type EnableSSOCamCheck: bool
        """
        self._InstanceId = None
        self._EnableSSOCamCheck = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EnableSSOCamCheck(self):
        return self._EnableSSOCamCheck

    @EnableSSOCamCheck.setter
    def EnableSSOCamCheck(self, EnableSSOCamCheck):
        self._EnableSSOCamCheck = EnableSSOCamCheck


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSSOCamCheckResponse(AbstractModel):
    """EnableSSOCamCheck response structure.

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


class EventCondition(AbstractModel):
    """Event alarm conditions

    """

    def __init__(self):
        r"""
        :param _AlarmNotifyPeriod: Alarm notification frequency.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotifyPeriod: str
        :param _AlarmNotifyType: Predefined repeated notification policy. `0`: One-time alarm; `1`: exponential alarm; `2`: consecutive alarm
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotifyType: str
        :param _EventID: Event ID.
        :type EventID: str
        :param _EventDisplayName: Displayed event name.
        :type EventDisplayName: str
        :param _RuleID: Rule ID.
        :type RuleID: str
        """
        self._AlarmNotifyPeriod = None
        self._AlarmNotifyType = None
        self._EventID = None
        self._EventDisplayName = None
        self._RuleID = None

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def EventDisplayName(self):
        return self._EventDisplayName

    @EventDisplayName.setter
    def EventDisplayName(self, EventDisplayName):
        self._EventDisplayName = EventDisplayName

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID


    def _deserialize(self, params):
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._EventID = params.get("EventID")
        self._EventDisplayName = params.get("EventDisplayName")
        self._RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param _Type: Filter method. Valid values: `=`, `!=`, `in`.
        :type Type: str
        :param _Key: Filter dimension name
        :type Key: str
        :param _Value: Filter value. For the `in` filter method, separate multiple values by comma.
        :type Value: str
        :param _Name: Filter name
        :type Name: str
        :param _Values: Filter value range
        :type Values: list of str
        """
        self._Type = None
        self._Key = None
        self._Value = None
        self._Name = None
        self._Values = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData request structure.

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace, such as QCE/CVM. For more information on the namespaces of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1)
        :type Namespace: str
        :param _MetricName: Metric name, such as `CPUUsage`. Only one monitoring metric can be pulled at a time. For more information on the metrics of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The corresponding metric name is `MetricName`.
        :type MetricName: str
        :param _Instances: The dimension combination for instance objects, which is in the form of a set of key-value pairs. The dimension fields for instances of different Tencent Cloud services are completely different. For example, the field is [{"Name":"InstanceId","Value":"ins-j0hk02zo"}] for CVM instances, [{"Name":"instanceId","Value":"ckafka-l49k54dd"}] for CKafka instances, and [{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}] for COS instances. For more information on the dimensions of various Tencent Cloud services, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). In each document, the dimension column displays a dimension combination’s key, which has a corresponding value. A single request can get the data of up to 10 instances.
        :type Instances: list of Instance
        :param _Period: Monitoring statistical period in seconds, such as 60. Default value: 300. The statistical period varies by metric. For more information on the statistical periods supported by each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The values in the statistical period column are the supported statistical periods. A single request can get up to 1,440 data points.
        :type Period: int
        :param _StartTime: Start time such as 2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param _EndTime: End time, which is the current time by default, such as 2018-09-22T20:51:23+08:00. `EndTime` cannot be earlier than `StartTime`
        :type EndTime: str
        """
        self._Namespace = None
        self._MetricName = None
        self._Instances = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData response structure.

    """

    def __init__(self):
        r"""
        :param _Period: Statistical period
        :type Period: int
        :param _MetricName: Metric name
        :type MetricName: str
        :param _DataPoints: Array of data points
        :type DataPoints: list of DataPoint
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _Msg: Returned message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Period = None
        self._MetricName = None
        self._DataPoints = None
        self._StartTime = None
        self._EndTime = None
        self._Msg = None
        self._RequestId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def DataPoints(self):
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

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
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self._DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self._DataPoints.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class GetPrometheusAgentManagementCommandRequest(AbstractModel):
    """GetPrometheusAgentManagementCommand request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _AgentId: Prometheus Agent ID
        :type AgentId: str
        """
        self._InstanceId = None
        self._AgentId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPrometheusAgentManagementCommandResponse(AbstractModel):
    """GetPrometheusAgentManagementCommand response structure.

    """

    def __init__(self):
        r"""
        :param _Command: Agent management command
        :type Command: :class:`tencentcloud.monitor.v20180724.models.ManagementCommand`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Command = None
        self._RequestId = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Command") is not None:
            self._Command = ManagementCommand()
            self._Command._deserialize(params.get("Command"))
        self._RequestId = params.get("RequestId")


class GrafanaAccountInfo(AbstractModel):
    """TCMG authorized account information

    """

    def __init__(self):
        r"""
        :param _UserId: User account ID
        :type UserId: str
        :param _Role: User permission
        :type Role: list of GrafanaAccountRole
        :param _Notes: Remarks
        :type Notes: str
        :param _CreateAt: Creation time
        :type CreateAt: str
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Uin: User’s root account UIN
        :type Uin: str
        """
        self._UserId = None
        self._Role = None
        self._Notes = None
        self._CreateAt = None
        self._InstanceId = None
        self._Uin = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        self._CreateAt = params.get("CreateAt")
        self._InstanceId = params.get("InstanceId")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaAccountRole(AbstractModel):
    """TCMG account permission

    """

    def __init__(self):
        r"""
        :param _Organization: Organization
        :type Organization: str
        :param _Role: Permission
        :type Role: str
        """
        self._Organization = None
        self._Role = None

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._Organization = params.get("Organization")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaChannel(AbstractModel):
    """Grafana alert channel

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelName: Channel name
        :type ChannelName: str
        :param _Receivers: Array of alert channel template IDs
        :type Receivers: list of str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _UpdatedAt: Update time
        :type UpdatedAt: str
        :param _OrganizationIds: All valid organizations in an alert channel
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrganizationIds: list of str
        """
        self._ChannelId = None
        self._ChannelName = None
        self._Receivers = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaInstanceInfo(AbstractModel):
    """Instance type when the Grafana instance is queried

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Region: Region
        :type Region: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param _InternetUrl: Grafana private network address
        :type InternetUrl: str
        :param _InternalUrl: Grafana public network address
        :type InternalUrl: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _InstanceStatus: Status. Valid values: `1` (creating), `2` (running), `3` (abnormal), `4` (restarting), `5` (stopping), `6` (stopped), `7` (deleted).
        :type InstanceStatus: int
        :param _TagSpecification: Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: list of PrometheusTag
        :param _Zone: Instance AZ
        :type Zone: str
        :param _InstanceChargeType: Billing mode. Valid value: `1` (monthly subscription).
        :type InstanceChargeType: int
        :param _VpcName: VPC name
        :type VpcName: str
        :param _SubnetName: Subnet name
        :type SubnetName: str
        :param _RegionId: Region ID
        :type RegionId: int
        :param _RootUrl: The full URL used to access this instance
        :type RootUrl: str
        :param _EnableSSO: Whether to enable SSO
        :type EnableSSO: bool
        :param _Version: Version number
        :type Version: str
        :param _EnableSSOCamCheck: Whether to enable CAM authentication during SSO
        :type EnableSSOCamCheck: bool
        """
        self._InstanceName = None
        self._InstanceId = None
        self._Region = None
        self._VpcId = None
        self._SubnetIds = None
        self._InternetUrl = None
        self._InternalUrl = None
        self._CreatedAt = None
        self._InstanceStatus = None
        self._TagSpecification = None
        self._Zone = None
        self._InstanceChargeType = None
        self._VpcName = None
        self._SubnetName = None
        self._RegionId = None
        self._RootUrl = None
        self._EnableSSO = None
        self._Version = None
        self._EnableSSOCamCheck = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def InternetUrl(self):
        return self._InternetUrl

    @InternetUrl.setter
    def InternetUrl(self, InternetUrl):
        self._InternetUrl = InternetUrl

    @property
    def InternalUrl(self):
        return self._InternalUrl

    @InternalUrl.setter
    def InternalUrl(self, InternalUrl):
        self._InternalUrl = InternalUrl

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RootUrl(self):
        return self._RootUrl

    @RootUrl.setter
    def RootUrl(self, RootUrl):
        self._RootUrl = RootUrl

    @property
    def EnableSSO(self):
        return self._EnableSSO

    @EnableSSO.setter
    def EnableSSO(self, EnableSSO):
        self._EnableSSO = EnableSSO

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def EnableSSOCamCheck(self):
        return self._EnableSSOCamCheck

    @EnableSSOCamCheck.setter
    def EnableSSOCamCheck(self, EnableSSOCamCheck):
        self._EnableSSOCamCheck = EnableSSOCamCheck


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._InternetUrl = params.get("InternetUrl")
        self._InternalUrl = params.get("InternalUrl")
        self._CreatedAt = params.get("CreatedAt")
        self._InstanceStatus = params.get("InstanceStatus")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._Zone = params.get("Zone")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._RegionId = params.get("RegionId")
        self._RootUrl = params.get("RootUrl")
        self._EnableSSO = params.get("EnableSSO")
        self._Version = params.get("Version")
        self._EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaIntegrationConfig(AbstractModel):
    """Grafana instance configuration

    """

    def __init__(self):
        r"""
        :param _IntegrationId: Integration ID
        :type IntegrationId: str
        :param _Kind: Integration type
        :type Kind: str
        :param _Content: Integration content
        :type Content: str
        :param _Description: Integration description
        :type Description: str
        :param _GrafanaURL: Grafana redirection address
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        """
        self._IntegrationId = None
        self._Kind = None
        self._Content = None
        self._Description = None
        self._GrafanaURL = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._Description = params.get("Description")
        self._GrafanaURL = params.get("GrafanaURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaNotificationChannel(AbstractModel):
    """Grafana notification channel

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelName: Channel name
        :type ChannelName: str
        :param _Receivers: Array of notification channel template IDs
        :type Receivers: list of str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _UpdatedAt: Update time
        :type UpdatedAt: str
        :param _OrgId: Default valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type OrgId: str
        :param _ExtraOrgIds: Extra valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraOrgIds: list of str
        :param _OrgIds: Valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgIds: str
        :param _OrganizationIds: All valid organizations in an alert channel
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrganizationIds: str
        """
        self._ChannelId = None
        self._ChannelName = None
        self._Receivers = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._OrgId = None
        self._ExtraOrgIds = None
        self._OrgIds = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrgIds(self):
        return self._OrgIds

    @OrgIds.setter
    def OrgIds(self, OrgIds):
        self._OrgIds = OrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._OrgId = params.get("OrgId")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrgIds = params.get("OrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaPlugin(AbstractModel):
    """Grafana plugin

    """

    def __init__(self):
        r"""
        :param _PluginId: Grafana plugin ID
        :type PluginId: str
        :param _Version: Grafana plugin version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self._PluginId = None
        self._Version = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsRequest(AbstractModel):
    """InstallPlugins request structure.

    """

    def __init__(self):
        r"""
        :param _Plugins: Plugin information
        :type Plugins: list of GrafanaPlugin
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self._Plugins = None
        self._InstanceId = None

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self._Plugins.append(obj)
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsResponse(AbstractModel):
    """InstallPlugins response structure.

    """

    def __init__(self):
        r"""
        :param _PluginIds: ID of the installed plugin
Note: This field may return null, indicating that no valid values can be obtained.
        :type PluginIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PluginIds = None
        self._RequestId = None

    @property
    def PluginIds(self):
        return self._PluginIds

    @PluginIds.setter
    def PluginIds(self, PluginIds):
        self._PluginIds = PluginIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PluginIds = params.get("PluginIds")
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Array of instance dimension combinations

    """

    def __init__(self):
        r"""
        :param _Dimensions: Combination of instance dimensions
        :type Dimensions: list of Dimension
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroup(AbstractModel):
    """InstanceGroup in Alarms returned by the DescribeBasicAlarmList API

    """

    def __init__(self):
        r"""
        :param _InstanceGroupId: Instance group ID.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroupId: int
        :param _InstanceGroupName: Instance group name.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroupName: str
        """
        self._InstanceGroupId = None
        self._InstanceGroupName = None

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def InstanceGroupName(self):
        return self._InstanceGroupName

    @InstanceGroupName.setter
    def InstanceGroupName(self, InstanceGroupName):
        self._InstanceGroupName = InstanceGroupName


    def _deserialize(self, params):
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._InstanceGroupName = params.get("InstanceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroups(AbstractModel):
    """Instance group of alarm object

    """

    def __init__(self):
        r"""
        :param _Id: Instance group ID
        :type Id: int
        :param _Name: Instance group name
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationConfiguration(AbstractModel):
    """Export integration configuration

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Kind: Type
        :type Kind: str
        :param _Content: Content
        :type Content: str
        :param _Status: Status
        :type Status: int
        :param _Category: Instance type
        :type Category: str
        :param _InstanceDesc: Instance description
        :type InstanceDesc: str
        :param _GrafanaDashboardURL: Dashboard URL
        :type GrafanaDashboardURL: str
        """
        self._Name = None
        self._Kind = None
        self._Content = None
        self._Status = None
        self._Category = None
        self._InstanceDesc = None
        self._GrafanaDashboardURL = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def GrafanaDashboardURL(self):
        return self._GrafanaDashboardURL

    @GrafanaDashboardURL.setter
    def GrafanaDashboardURL(self, GrafanaDashboardURL):
        self._GrafanaDashboardURL = GrafanaDashboardURL


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        self._Status = params.get("Status")
        self._Category = params.get("Category")
        self._InstanceDesc = params.get("InstanceDesc")
        self._GrafanaDashboardURL = params.get("GrafanaDashboardURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """Tags in K8s, which generally exist in the form of an array.

    """

    def __init__(self):
        r"""
        :param _Name: Label name
        :type Name: str
        :param _Value: Label value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class LogAlarmReq(AbstractModel):
    """Log alarm request information

    """

    def __init__(self):
        r"""
        :param _InstanceId: APM instance ID
        :type InstanceId: str
        :param _Filter: Search condition
        :type Filter: list of LogFilterInfo
        :param _AlarmMerge: The switch to enable/disable alarm merging
        :type AlarmMerge: str
        :param _AlarmMergeTime: Alarm merging time
        :type AlarmMergeTime: str
        """
        self._InstanceId = None
        self._Filter = None
        self._AlarmMerge = None
        self._AlarmMergeTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AlarmMerge(self):
        return self._AlarmMerge

    @AlarmMerge.setter
    def AlarmMerge(self, AlarmMerge):
        self._AlarmMerge = AlarmMerge

    @property
    def AlarmMergeTime(self):
        return self._AlarmMergeTime

    @AlarmMergeTime.setter
    def AlarmMergeTime(self, AlarmMergeTime):
        self._AlarmMergeTime = AlarmMergeTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = LogFilterInfo()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._AlarmMerge = params.get("AlarmMerge")
        self._AlarmMergeTime = params.get("AlarmMergeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFilterInfo(AbstractModel):
    """Log alarm search condition structure

    """

    def __init__(self):
        r"""
        :param _Key: Field name
        :type Key: str
        :param _Operator: Comparison operator
        :type Operator: str
        :param _Value: Field value
        :type Value: str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagementCommand(AbstractModel):
    """Prometheus agent management command line

    """

    def __init__(self):
        r"""
        :param _Install: Agent installation command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Install: str
        :param _Restart: Agent restart command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Restart: str
        :param _Stop: Agent stop command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stop: str
        :param _StatusCheck: Agent status detection command
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusCheck: str
        :param _LogCheck: Agent log detection command
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogCheck: str
        """
        self._Install = None
        self._Restart = None
        self._Stop = None
        self._StatusCheck = None
        self._LogCheck = None

    @property
    def Install(self):
        return self._Install

    @Install.setter
    def Install(self, Install):
        self._Install = Install

    @property
    def Restart(self):
        return self._Restart

    @Restart.setter
    def Restart(self, Restart):
        self._Restart = Restart

    @property
    def Stop(self):
        return self._Stop

    @Stop.setter
    def Stop(self, Stop):
        self._Stop = Stop

    @property
    def StatusCheck(self):
        return self._StatusCheck

    @StatusCheck.setter
    def StatusCheck(self, StatusCheck):
        self._StatusCheck = StatusCheck

    @property
    def LogCheck(self):
        return self._LogCheck

    @LogCheck.setter
    def LogCheck(self, LogCheck):
        self._LogCheck = LogCheck


    def _deserialize(self, params):
        self._Install = params.get("Install")
        self._Restart = params.get("Restart")
        self._Stop = params.get("Stop")
        self._StatusCheck = params.get("StatusCheck")
        self._LogCheck = params.get("LogCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metric(AbstractModel):
    """Metric, which can be used to set alarms and query data

    """

    def __init__(self):
        r"""
        :param _Namespace: Alarm policy type
        :type Namespace: str
        :param _MetricName: Metric name
        :type MetricName: str
        :param _Description: Metric display name
        :type Description: str
        :param _Min: Minimum value
        :type Min: float
        :param _Max: Maximum value
        :type Max: float
        :param _Dimensions: Dimension list
        :type Dimensions: list of str
        :param _Unit: Unit
        :type Unit: str
        :param _MetricConfig: Metric configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type MetricConfig: :class:`tencentcloud.monitor.v20180724.models.MetricConfig`
        :param _IsAdvanced: Whether it is an advanced metric. 1: Yes; 0: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsAdvanced: int
        :param _IsOpen: Whether the advanced metric feature is enabled. 1: Yes; 0: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOpen: int
        :param _ProductId: Integration center product ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProductId: int
        """
        self._Namespace = None
        self._MetricName = None
        self._Description = None
        self._Min = None
        self._Max = None
        self._Dimensions = None
        self._Unit = None
        self._MetricConfig = None
        self._IsAdvanced = None
        self._IsOpen = None
        self._ProductId = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def MetricConfig(self):
        return self._MetricConfig

    @MetricConfig.setter
    def MetricConfig(self, MetricConfig):
        self._MetricConfig = MetricConfig

    @property
    def IsAdvanced(self):
        return self._IsAdvanced

    @IsAdvanced.setter
    def IsAdvanced(self, IsAdvanced):
        self._IsAdvanced = IsAdvanced

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Description = params.get("Description")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Dimensions = params.get("Dimensions")
        self._Unit = params.get("Unit")
        if params.get("MetricConfig") is not None:
            self._MetricConfig = MetricConfig()
            self._MetricConfig._deserialize(params.get("MetricConfig"))
        self._IsAdvanced = params.get("IsAdvanced")
        self._IsOpen = params.get("IsOpen")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricConfig(AbstractModel):
    """Metric configuration

    """

    def __init__(self):
        r"""
        :param _Operator: Allowed operator
        :type Operator: list of str
        :param _Period: Allowed data cycle in seconds
        :type Period: list of int
        :param _ContinuePeriod: Allowed number of continuous cycles
        :type ContinuePeriod: list of int
        """
        self._Operator = None
        self._Period = None
        self._ContinuePeriod = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._Period = params.get("Period")
        self._ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """`DescribeMetricData` output parameters

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name
        :type MetricName: str
        :param _Points: Monitoring data point
        :type Points: list of MetricDataPoint
        """
        self._MetricName = None
        self._Points = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataPoint(AbstractModel):
    """`DescribeMetricData` output parameters

    """

    def __init__(self):
        r"""
        :param _Dimensions: Combination of instance object dimensions
        :type Dimensions: list of Dimension
        :param _Values: Data point list
        :type Values: list of Point
        """
        self._Dimensions = None
        self._Values = None

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = Point()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDatum(AbstractModel):
    """Metric names and values

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name.
        :type MetricName: str
        :param _Value: Metric value.
        :type Value: int
        """
        self._MetricName = None
        self._Value = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricObjectMeaning(AbstractModel):
    """Meaning of metric data

    """

    def __init__(self):
        r"""
        :param _En: Meaning of the metric in English
        :type En: str
        :param _Zh: Meaning of the metric in Chinese
        :type Zh: str
        """
        self._En = None
        self._Zh = None

    @property
    def En(self):
        return self._En

    @En.setter
    def En(self, En):
        self._En = En

    @property
    def Zh(self):
        return self._Zh

    @Zh.setter
    def Zh(self, Zh):
        self._Zh = Zh


    def _deserialize(self, params):
        self._En = params.get("En")
        self._Zh = params.get("Zh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricSet(AbstractModel):
    """Description of the unit and supported statistical period of the business metric

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace. Each Tencent Cloud product has a namespace
        :type Namespace: str
        :param _MetricName: Metric Name
        :type MetricName: str
        :param _Unit: Unit used by the metric
        :type Unit: str
        :param _UnitCname: Unit used by the metric
        :type UnitCname: str
        :param _Period: Statistical period in seconds supported by the metric, such as 60 and 300
        :type Period: list of int
        :param _Periods: Metric method during the statistical period
        :type Periods: list of PeriodsSt
        :param _Meaning: Meaning of the statistical metric
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param _Dimensions: Dimension description
        :type Dimensions: list of DimensionsDesc
        :param _MetricCName: Metric name (in Chinese).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricCName: str
        :param _MetricEName: Metric name (in English).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricEName: str
        """
        self._Namespace = None
        self._MetricName = None
        self._Unit = None
        self._UnitCname = None
        self._Period = None
        self._Periods = None
        self._Meaning = None
        self._Dimensions = None
        self._MetricCName = None
        self._MetricEName = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def UnitCname(self):
        return self._UnitCname

    @UnitCname.setter
    def UnitCname(self, UnitCname):
        self._UnitCname = UnitCname

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Periods(self):
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def Meaning(self):
        return self._Meaning

    @Meaning.setter
    def Meaning(self, Meaning):
        self._Meaning = Meaning

    @property
    def Dimensions(self):
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def MetricCName(self):
        return self._MetricCName

    @MetricCName.setter
    def MetricCName(self, MetricCName):
        self._MetricCName = MetricCName

    @property
    def MetricEName(self):
        return self._MetricEName

    @MetricEName.setter
    def MetricEName(self, MetricEName):
        self._MetricEName = MetricEName


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        self._Unit = params.get("Unit")
        self._UnitCname = params.get("UnitCname")
        self._Period = params.get("Period")
        if params.get("Periods") is not None:
            self._Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self._Periods.append(obj)
        if params.get("Meaning") is not None:
            self._Meaning = MetricObjectMeaning()
            self._Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._MetricCName = params.get("MetricCName")
        self._MetricEName = params.get("MetricEName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MidQueryCondition(AbstractModel):
    """`DescribeMidDimensionValueList` query conditions

    """

    def __init__(self):
        r"""
        :param _Key: Dimension
        :type Key: str
        :param _Operator: Operator. Valid values: eq (equal to), ne (not equal to), in
        :type Operator: str
        :param _Value: Dimension value. If `Operator` is `eq` or `ne`, only the first element will be used
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
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
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _Name: Alarm notification rule name, which can contain up to 60 characters
        :type Name: str
        :param _NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
        :type NoticeType: str
        :param _NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
        :type NoticeLanguage: str
        :param _NoticeId: Alarm notification template ID
        :type NoticeId: str
        :param _UserNotices: User notifications (up to 5)
        :type UserNotices: list of UserNotice
        :param _URLNotices: Callback notifications (up to 3)
        :type URLNotices: list of URLNotice
        :param _CLSNotices: The operation of pushing alarm notifications to CLS. Up to one CLS log topic can be configured.
        :type CLSNotices: list of CLSNotice
        :param _PolicyIds: List of IDs of the alerting rules bound to an alarm notification template
        :type PolicyIds: list of str
        """
        self._Module = None
        self._Name = None
        self._NoticeType = None
        self._NoticeLanguage = None
        self._NoticeId = None
        self._UserNotices = None
        self._URLNotices = None
        self._CLSNotices = None
        self._PolicyIds = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def NoticeLanguage(self):
        return self._NoticeLanguage

    @NoticeLanguage.setter
    def NoticeLanguage(self, NoticeLanguage):
        self._NoticeLanguage = NoticeLanguage

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def UserNotices(self):
        return self._UserNotices

    @UserNotices.setter
    def UserNotices(self, UserNotices):
        self._UserNotices = UserNotices

    @property
    def URLNotices(self):
        return self._URLNotices

    @URLNotices.setter
    def URLNotices(self, URLNotices):
        self._URLNotices = URLNotices

    @property
    def CLSNotices(self):
        return self._CLSNotices

    @CLSNotices.setter
    def CLSNotices(self, CLSNotices):
        self._CLSNotices = CLSNotices

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Name = params.get("Name")
        self._NoticeType = params.get("NoticeType")
        self._NoticeLanguage = params.get("NoticeLanguage")
        self._NoticeId = params.get("NoticeId")
        if params.get("UserNotices") is not None:
            self._UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self._UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self._URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self._URLNotices.append(obj)
        if params.get("CLSNotices") is not None:
            self._CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self._CLSNotices.append(obj)
        self._PolicyIds = params.get("PolicyIds")
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


class ModifyAlarmPolicyConditionRequest(AbstractModel):
    """ModifyAlarmPolicyCondition request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _ConditionTemplateId: ID of trigger condition template. This parameter can be left empty.
        :type ConditionTemplateId: int
        :param _Condition: Metric trigger condition
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param _EventCondition: Event trigger condition
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param _Filter: Global filter.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param _GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.
        :type GroupBy: list of str
        :param _LogAlarmReqInfo: Log alarm creation request parameters
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param _NoticeIds: Template ID, which is dedicated to TMP.
        :type NoticeIds: list of str
        :param _Enable: Status (`0`: Disabled; `1`: Enabled)
        :type Enable: int
        :param _PolicyName: Name of the policy dedicated to TMP
        :type PolicyName: str
        :param _EbSubject: The alert configured for an event
        :type EbSubject: str
        """
        self._Module = None
        self._PolicyId = None
        self._ConditionTemplateId = None
        self._Condition = None
        self._EventCondition = None
        self._Filter = None
        self._GroupBy = None
        self._LogAlarmReqInfo = None
        self._NoticeIds = None
        self._Enable = None
        self._PolicyName = None
        self._EbSubject = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ConditionTemplateId(self):
        return self._ConditionTemplateId

    @ConditionTemplateId.setter
    def ConditionTemplateId(self, ConditionTemplateId):
        self._ConditionTemplateId = ConditionTemplateId

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def EventCondition(self):
        return self._EventCondition

    @EventCondition.setter
    def EventCondition(self, EventCondition):
        self._EventCondition = EventCondition

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def LogAlarmReqInfo(self):
        return self._LogAlarmReqInfo

    @LogAlarmReqInfo.setter
    def LogAlarmReqInfo(self, LogAlarmReqInfo):
        self._LogAlarmReqInfo = LogAlarmReqInfo

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self._Condition = AlarmPolicyCondition()
            self._Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self._EventCondition = AlarmPolicyEventCondition()
            self._EventCondition._deserialize(params.get("EventCondition"))
        if params.get("Filter") is not None:
            self._Filter = AlarmPolicyFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._GroupBy = params.get("GroupBy")
        if params.get("LogAlarmReqInfo") is not None:
            self._LogAlarmReqInfo = LogAlarmReq()
            self._LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        self._NoticeIds = params.get("NoticeIds")
        self._Enable = params.get("Enable")
        self._PolicyName = params.get("PolicyName")
        self._EbSubject = params.get("EbSubject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyConditionResponse(AbstractModel):
    """ModifyAlarmPolicyCondition response structure.

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


class ModifyAlarmPolicyInfoRequest(AbstractModel):
    """ModifyAlarmPolicyInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _Key: Field to be modified. Valid values: NAME (policy name), REMARK (policy remarks)
        :type Key: str
        :param _Value: Value after modification
        :type Value: str
        """
        self._Module = None
        self._PolicyId = None
        self._Key = None
        self._Value = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyInfoResponse(AbstractModel):
    """ModifyAlarmPolicyInfo response structure.

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


class ModifyAlarmPolicyNoticeRequest(AbstractModel):
    """ModifyAlarmPolicyNotice request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is specified as `monitor`.
        :type Module: str
        :param _PolicyId: Alarm policy ID. If both `PolicyIds` and this parameter are returned, only `PolicyIds` takes effect.
        :type PolicyId: str
        :param _NoticeIds: List of alarm notification template IDs.
        :type NoticeIds: list of str
        :param _PolicyIds: Alarm policy ID array, which can be used to associate notification templates with multiple alarm policies. Max value: 30.
        :type PolicyIds: list of str
        :param _HierarchicalNotices: Notification rules for different alarm levels
        :type HierarchicalNotices: list of AlarmHierarchicalNotice
        """
        self._Module = None
        self._PolicyId = None
        self._NoticeIds = None
        self._PolicyIds = None
        self._HierarchicalNotices = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def HierarchicalNotices(self):
        return self._HierarchicalNotices

    @HierarchicalNotices.setter
    def HierarchicalNotices(self, HierarchicalNotices):
        self._HierarchicalNotices = HierarchicalNotices


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._NoticeIds = params.get("NoticeIds")
        self._PolicyIds = params.get("PolicyIds")
        if params.get("HierarchicalNotices") is not None:
            self._HierarchicalNotices = []
            for item in params.get("HierarchicalNotices"):
                obj = AlarmHierarchicalNotice()
                obj._deserialize(item)
                self._HierarchicalNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyNoticeResponse(AbstractModel):
    """ModifyAlarmPolicyNotice response structure.

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


class ModifyAlarmPolicyStatusRequest(AbstractModel):
    """ModifyAlarmPolicyStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _Enable: Status. Valid values: 0 (disabled), 1 (enabled)
        :type Enable: int
        """
        self._Module = None
        self._PolicyId = None
        self._Enable = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyStatusResponse(AbstractModel):
    """ModifyAlarmPolicyStatus response structure.

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


class ModifyAlarmPolicyTasksRequest(AbstractModel):
    """ModifyAlarmPolicyTasks request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name. Enter "monitor" here
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        :param _TriggerTasks: List of tasks triggered by alarm policy. If this parameter is left empty, it indicates to unbind all tasks
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        """
        self._Module = None
        self._PolicyId = None
        self._TriggerTasks = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def TriggerTasks(self):
        return self._TriggerTasks

    @TriggerTasks.setter
    def TriggerTasks(self, TriggerTasks):
        self._TriggerTasks = TriggerTasks


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        if params.get("TriggerTasks") is not None:
            self._TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self._TriggerTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyTasksResponse(AbstractModel):
    """ModifyAlarmPolicyTasks response structure.

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


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of a policy group whose recipient needs to be modified.
        :type GroupId: int
        :param _Module: Required. The value is fixed to monitor.
        :type Module: str
        :param _ReceiverInfos: New recipient information. If this parameter is not configured, all recipients will be deleted.
        :type ReceiverInfos: list of ReceiverInfo
        """
        self._GroupId = None
        self._Module = None
        self._ReceiverInfos = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Module = params.get("Module")
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = ReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers response structure.

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


class ModifyGrafanaInstanceRequest(AbstractModel):
    """ModifyGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _InstanceName: TCMG instance name, such as “test”.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGrafanaInstanceResponse(AbstractModel):
    """ModifyGrafanaInstance response structure.

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


class ModifyPolicyGroupCondition(AbstractModel):
    """Modification of the metric threshold condition passed in by the alarm policy group.

    """

    def __init__(self):
        r"""
        :param _MetricId: Metric ID.
        :type MetricId: int
        :param _CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to.
        :type CalcType: int
        :param _CalcValue: Threshold.
        :type CalcValue: str
        :param _CalcPeriod: Data period of the detected metric.
        :type CalcPeriod: int
        :param _ContinuePeriod: Number of consecutive periods.
        :type ContinuePeriod: int
        :param _AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param _RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.
        :type RuleId: int
        """
        self._MetricId = None
        self._CalcType = None
        self._CalcValue = None
        self._CalcPeriod = None
        self._ContinuePeriod = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def MetricId(self):
        return self._MetricId

    @MetricId.setter
    def MetricId(self, MetricId):
        self._MetricId = MetricId

    @property
    def CalcType(self):
        return self._CalcType

    @CalcType.setter
    def CalcType(self, CalcType):
        self._CalcType = CalcType

    @property
    def CalcValue(self):
        return self._CalcValue

    @CalcValue.setter
    def CalcValue(self, CalcValue):
        self._CalcValue = CalcValue

    @property
    def CalcPeriod(self):
        return self._CalcPeriod

    @CalcPeriod.setter
    def CalcPeriod(self, CalcPeriod):
        self._CalcPeriod = CalcPeriod

    @property
    def ContinuePeriod(self):
        return self._ContinuePeriod

    @ContinuePeriod.setter
    def ContinuePeriod(self, ContinuePeriod):
        self._ContinuePeriod = ContinuePeriod

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._MetricId = params.get("MetricId")
        self._CalcType = params.get("CalcType")
        self._CalcValue = params.get("CalcValue")
        self._CalcPeriod = params.get("CalcPeriod")
        self._ContinuePeriod = params.get("ContinuePeriod")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupEventCondition(AbstractModel):
    """Modification of the event alarm condition passed in by the alarm policy group.

    """

    def __init__(self):
        r"""
        :param _EventId: Event ID.
        :type EventId: int
        :param _AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param _AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param _RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.
        :type RuleId: int
        """
        self._EventId = None
        self._AlarmNotifyType = None
        self._AlarmNotifyPeriod = None
        self._RuleId = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AlarmNotifyType(self):
        return self._AlarmNotifyType

    @AlarmNotifyType.setter
    def AlarmNotifyType(self, AlarmNotifyType):
        self._AlarmNotifyType = AlarmNotifyType

    @property
    def AlarmNotifyPeriod(self):
        return self._AlarmNotifyPeriod

    @AlarmNotifyPeriod.setter
    def AlarmNotifyPeriod(self, AlarmNotifyPeriod):
        self._AlarmNotifyPeriod = AlarmNotifyPeriod

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AlarmNotifyType = params.get("AlarmNotifyType")
        self._AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupRequest(AbstractModel):
    """ModifyPolicyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID.
        :type GroupId: int
        :param _ViewName: Alarm type.
        :type ViewName: str
        :param _GroupName: Policy group name.
        :type GroupName: str
        :param _IsUnionRule: The 'AND' and 'OR' rules for metric alarms. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met.
        :type IsUnionRule: int
        :param _Conditions: Metric alarm condition rules. No filling indicates that all existing metric alarm condition rules will be deleted.
        :type Conditions: list of ModifyPolicyGroupCondition
        :param _EventConditions: Event alarm conditions. No filling indicates that all existing event alarm conditions will be deleted.
        :type EventConditions: list of ModifyPolicyGroupEventCondition
        :param _ConditionTempGroupId: Template-based policy group ID.
        :type ConditionTempGroupId: int
        """
        self._Module = None
        self._GroupId = None
        self._ViewName = None
        self._GroupName = None
        self._IsUnionRule = None
        self._Conditions = None
        self._EventConditions = None
        self._ConditionTempGroupId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def ConditionTempGroupId(self):
        return self._ConditionTempGroupId

    @ConditionTempGroupId.setter
    def ConditionTempGroupId(self, ConditionTempGroupId):
        self._ConditionTempGroupId = ConditionTempGroupId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._ViewName = params.get("ViewName")
        self._GroupName = params.get("GroupName")
        self._IsUnionRule = params.get("IsUnionRule")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ModifyPolicyGroupCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = ModifyPolicyGroupEventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        self._ConditionTempGroupId = params.get("ConditionTempGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupResponse(AbstractModel):
    """ModifyPolicyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Policy group ID.
        :type GroupId: int
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


class ModifyPrometheusAgentExternalLabelsRequest(AbstractModel):
    """ModifyPrometheusAgentExternalLabels request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ExternalLabels: New external labels
        :type ExternalLabels: list of Label
        """
        self._InstanceId = None
        self._ClusterId = None
        self._ExternalLabels = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAgentExternalLabelsResponse(AbstractModel):
    """ModifyPrometheusAgentExternalLabels response structure.

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


class ModifyPrometheusAlertPolicyRequest(AbstractModel):
    """ModifyPrometheusAlertPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertRule: Alert configuration
        :type AlertRule: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertPolicyItem`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertPolicyItem()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertPolicyResponse(AbstractModel):
    """ModifyPrometheusAlertPolicy response structure.

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


class ModifyPrometheusConfigRequest(AbstractModel):
    """ModifyPrometheusConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ServiceMonitors: Configuration of service monitors
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: Configuration of pod monitors
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: Configuration of Prometheus raw jobs
        :type RawJobs: list of PrometheusConfigItem
        """
        self._InstanceId = None
        self._ClusterType = None
        self._ClusterId = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusConfigResponse(AbstractModel):
    """ModifyPrometheusConfig response structure.

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


class ModifyPrometheusGlobalNotificationRequest(AbstractModel):
    """ModifyPrometheusGlobalNotification request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Notification: Alert notification channel
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        """
        self._InstanceId = None
        self._Notification = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusGlobalNotificationResponse(AbstractModel):
    """ModifyPrometheusGlobalNotification response structure.

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


class ModifyPrometheusInstanceAttributesRequest(AbstractModel):
    """ModifyPrometheusInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DataRetentionTime: Storage period. Valid values: 15, 30, 45. This parameter is not applicable to monthly subscribed instances.
        :type DataRetentionTime: int
        """
        self._InstanceName = None
        self._InstanceId = None
        self._DataRetentionTime = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._DataRetentionTime = params.get("DataRetentionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusInstanceAttributesResponse(AbstractModel):
    """ModifyPrometheusInstanceAttributes response structure.

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


class ModifyPrometheusRecordRuleYamlRequest(AbstractModel):
    """ModifyPrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Recording instance name
        :type Name: str
        :param _Content: New content
        :type Content: str
        """
        self._InstanceId = None
        self._Name = None
        self._Content = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusRecordRuleYamlResponse(AbstractModel):
    """ModifyPrometheusRecordRuleYaml response structure.

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


class ModifyPrometheusTempRequest(AbstractModel):
    """ModifyPrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: str
        :param _Template: Modified content
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTempModify`
        """
        self._TemplateId = None
        self._Template = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Template") is not None:
            self._Template = PrometheusTempModify()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTempResponse(AbstractModel):
    """ModifyPrometheusTemp response structure.

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


class MonitorTypeInfo(AbstractModel):
    """Monitoring type details

    """

    def __init__(self):
        r"""
        :param _Id: Monitoring type ID
        :type Id: str
        :param _Name: Monitoring type
        :type Name: str
        :param _SortId: Sort order
        :type SortId: int
        """
        self._Id = None
        self._Name = None
        self._SortId = None

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
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTypeNamespace(AbstractModel):
    """Policy type

    """

    def __init__(self):
        r"""
        :param _MonitorType: Monitor type
        :type MonitorType: str
        :param _Namespace: Policy type value
        :type Namespace: str
        """
        self._MonitorType = None
        self._Namespace = None

    @property
    def MonitorType(self):
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeBindPolicys(AbstractModel):
    """Binding between a notification template and a policy

    """

    def __init__(self):
        r"""
        :param _NoticeId: Alert notification template ID
        :type NoticeId: str
        :param _PolicyIds: List of IDs of the alerting rules bound to an alarm notification template
        :type PolicyIds: list of str
        """
        self._NoticeId = None
        self._PolicyIds = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operator(AbstractModel):
    """Operators supported by the instance

    """

    def __init__(self):
        r"""
        :param _Id: Operator ID
        :type Id: str
        :param _Name: Operator name
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeriodsSt(AbstractModel):
    """Statistical method during the period

    """

    def __init__(self):
        r"""
        :param _Period: Period
        :type Period: str
        :param _StatType: Statistical method
        :type StatType: list of str
        """
        self._Period = None
        self._StatType = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StatType = params.get("StatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        r"""
        :param _Timestamp: Time point when this monitoring data point is generated
        :type Timestamp: int
        :param _Value: Monitoring data point value
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: float
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyGroup(AbstractModel):
    """Policy group information

    """

    def __init__(self):
        r"""
        :param _CanSetDefault: Whether the alarm policy can be set to default.
        :type CanSetDefault: bool
        :param _GroupID: Alarm policy group ID.
        :type GroupID: int
        :param _GroupName: Alarm policy group name.
        :type GroupName: str
        :param _InsertTime: Creation time.
        :type InsertTime: int
        :param _IsDefault: Whether the alarm policy is set to default.
        :type IsDefault: int
        :param _Enable: Whether the alarm policy is enabled.
        :type Enable: bool
        :param _LastEditUin: UIN of the last modifier.
        :type LastEditUin: int
        :param _NoShieldedInstanceCount: Number of unshielded instances.
        :type NoShieldedInstanceCount: int
        :param _ParentGroupID: Parent policy group ID.
        :type ParentGroupID: int
        :param _ProjectID: Project ID.
        :type ProjectID: int
        :param _ReceiverInfos: Alarm recipient information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverInfos: list of PolicyGroupReceiverInfo
        :param _Remark: Remarks.
        :type Remark: str
        :param _UpdateTime: Modification time.
        :type UpdateTime: int
        :param _TotalInstanceCount: The total number of associated instances.
        :type TotalInstanceCount: int
        :param _ViewName: View.
        :type ViewName: str
        :param _IsUnionRule: Whether the logical relationship between rules is AND.
        :type IsUnionRule: int
        """
        self._CanSetDefault = None
        self._GroupID = None
        self._GroupName = None
        self._InsertTime = None
        self._IsDefault = None
        self._Enable = None
        self._LastEditUin = None
        self._NoShieldedInstanceCount = None
        self._ParentGroupID = None
        self._ProjectID = None
        self._ReceiverInfos = None
        self._Remark = None
        self._UpdateTime = None
        self._TotalInstanceCount = None
        self._ViewName = None
        self._IsUnionRule = None

    @property
    def CanSetDefault(self):
        return self._CanSetDefault

    @CanSetDefault.setter
    def CanSetDefault(self, CanSetDefault):
        self._CanSetDefault = CanSetDefault

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def NoShieldedInstanceCount(self):
        return self._NoShieldedInstanceCount

    @NoShieldedInstanceCount.setter
    def NoShieldedInstanceCount(self, NoShieldedInstanceCount):
        self._NoShieldedInstanceCount = NoShieldedInstanceCount

    @property
    def ParentGroupID(self):
        return self._ParentGroupID

    @ParentGroupID.setter
    def ParentGroupID(self, ParentGroupID):
        self._ParentGroupID = ParentGroupID

    @property
    def ProjectID(self):
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ReceiverInfos(self):
        return self._ReceiverInfos

    @ReceiverInfos.setter
    def ReceiverInfos(self, ReceiverInfos):
        self._ReceiverInfos = ReceiverInfos

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TotalInstanceCount(self):
        return self._TotalInstanceCount

    @TotalInstanceCount.setter
    def TotalInstanceCount(self, TotalInstanceCount):
        self._TotalInstanceCount = TotalInstanceCount

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        self._CanSetDefault = params.get("CanSetDefault")
        self._GroupID = params.get("GroupID")
        self._GroupName = params.get("GroupName")
        self._InsertTime = params.get("InsertTime")
        self._IsDefault = params.get("IsDefault")
        self._Enable = params.get("Enable")
        self._LastEditUin = params.get("LastEditUin")
        self._NoShieldedInstanceCount = params.get("NoShieldedInstanceCount")
        self._ParentGroupID = params.get("ParentGroupID")
        self._ProjectID = params.get("ProjectID")
        if params.get("ReceiverInfos") is not None:
            self._ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = PolicyGroupReceiverInfo()
                obj._deserialize(item)
                self._ReceiverInfos.append(obj)
        self._Remark = params.get("Remark")
        self._UpdateTime = params.get("UpdateTime")
        self._TotalInstanceCount = params.get("TotalInstanceCount")
        self._ViewName = params.get("ViewName")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyGroupReceiverInfo(AbstractModel):
    """Information on recipients in the policy template list (API v2018)

    """

    def __init__(self):
        r"""
        :param _EndTime: End time of a valid time period.
        :type EndTime: int
        :param _NeedSendNotice: Whether it is required to send notifications.
        :type NeedSendNotice: int
        :param _NotifyWay: Alarm receiving channel.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NotifyWay: list of str
        :param _PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param _ReceiverGroupList: Message recipient group list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverGroupList: list of int
        :param _ReceiverType: Recipient type.
        :type ReceiverType: str
        :param _ReceiverUserList: Recipient list. The list of recipient IDs that is queried by a platform API.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverUserList: list of int
        :param _RecoverNotify: Alarm resolution notification method.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RecoverNotify: list of str
        :param _RoundInterval: Alarm call interval per round in seconds.
        :type RoundInterval: int
        :param _RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param _SendFor: Alarm call notification time. Valid values: `OCCUR` (indicating that a notification is sent when the alarm is triggered) and `RECOVER` (indicating that a notification is sent when the alarm is resolved).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SendFor: list of str
        :param _StartTime: Start time of a valid time period.
        :type StartTime: int
        :param _UIDList: UID of the alarm call recipient.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UIDList: list of int
        """
        self._EndTime = None
        self._NeedSendNotice = None
        self._NotifyWay = None
        self._PersonInterval = None
        self._ReceiverGroupList = None
        self._ReceiverType = None
        self._ReceiverUserList = None
        self._RecoverNotify = None
        self._RoundInterval = None
        self._RoundNumber = None
        self._SendFor = None
        self._StartTime = None
        self._UIDList = None

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UIDList(self):
        return self._UIDList

    @UIDList.setter
    def UIDList(self, UIDList):
        self._UIDList = UIDList


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._NotifyWay = params.get("NotifyWay")
        self._PersonInterval = params.get("PersonInterval")
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverType = params.get("ReceiverType")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._RecoverNotify = params.get("RecoverNotify")
        self._RoundInterval = params.get("RoundInterval")
        self._RoundNumber = params.get("RoundNumber")
        self._SendFor = params.get("SendFor")
        self._StartTime = params.get("StartTime")
        self._UIDList = params.get("UIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgent(AbstractModel):
    """prometheus agent

    """

    def __init__(self):
        r"""
        :param _Name: Agent name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Ipv4: Agent IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv4: str
        :param _HeartbeatTime: Heartbeat time
Note: This field may return null, indicating that no valid values can be obtained.
        :type HeartbeatTime: str
        :param _LastError: Last error
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastError: str
        :param _AgentVersion: Agent version
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentVersion: str
        :param _Status: Agent status
        :type Status: int
        """
        self._Name = None
        self._AgentId = None
        self._InstanceId = None
        self._Ipv4 = None
        self._HeartbeatTime = None
        self._LastError = None
        self._AgentVersion = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ipv4(self):
        return self._Ipv4

    @Ipv4.setter
    def Ipv4(self, Ipv4):
        self._Ipv4 = Ipv4

    @property
    def HeartbeatTime(self):
        return self._HeartbeatTime

    @HeartbeatTime.setter
    def HeartbeatTime(self, HeartbeatTime):
        self._HeartbeatTime = HeartbeatTime

    @property
    def LastError(self):
        return self._LastError

    @LastError.setter
    def LastError(self, LastError):
        self._LastError = LastError

    @property
    def AgentVersion(self):
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AgentId = params.get("AgentId")
        self._InstanceId = params.get("InstanceId")
        self._Ipv4 = params.get("Ipv4")
        self._HeartbeatTime = params.get("HeartbeatTime")
        self._LastError = params.get("LastError")
        self._AgentVersion = params.get("AgentVersion")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgentInfo(AbstractModel):
    """Information of managed Prometheus agent

    """

    def __init__(self):
        r"""
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Describe: Remarks
        :type Describe: str
        """
        self._ClusterType = None
        self._ClusterId = None
        self._Describe = None

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgentOverview(AbstractModel):
    """Overview of managed Prometheus agent

    """

    def __init__(self):
        r"""
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Status: Agent status. Valid values: 
`normal`
`abnormal`
        :type Status: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ExternalLabels: External labels
External labels, which will be attached to all metrics in this cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExternalLabels: list of Label
        :param _Region: Cluster region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _VpcId: ID of the VPC where the cluster resides
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _FailedReason: Recorded information of failed operations, such as association.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedReason: str
        :param _Name: Agent name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        """
        self._ClusterType = None
        self._ClusterId = None
        self._Status = None
        self._ClusterName = None
        self._ExternalLabels = None
        self._Region = None
        self._VpcId = None
        self._FailedReason = None
        self._Name = None

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._Status = params.get("Status")
        self._ClusterName = params.get("ClusterName")
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._FailedReason = params.get("FailedReason")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertManagerConfig(AbstractModel):
    """Self-built AlertManager configuration used by the alert channel

    """

    def __init__(self):
        r"""
        :param _Url: AlertManager URL
        :type Url: str
        :param _ClusterType: Type of the cluster where AlertManager is deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: str
        :param _ClusterId: ID of the cluster where AlertManager is deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self._Url = None
        self._ClusterType = None
        self._ClusterId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertPolicyItem(AbstractModel):
    """TMP alerting rule instance

    """

    def __init__(self):
        r"""
        :param _Name: Rule name
        :type Name: str
        :param _Rules: List of rules
        :type Rules: list of PrometheusAlertRule
        :param _Id: Alerting rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _TemplateId: If the alert comes from a template, `TemplateId` is the template ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param _Notification: Alert channel, which may be returned as null if used in a template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        :param _UpdatedAt: Last modification time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _ClusterId: If the alerting rule comes from the user cluster CRD resource definition, `ClusterId` is the cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self._Name = None
        self._Rules = None
        self._Id = None
        self._TemplateId = None
        self._Notification = None
        self._UpdatedAt = None
        self._ClusterId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Id = params.get("Id")
        self._TemplateId = params.get("TemplateId")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotificationItem()
            self._Notification._deserialize(params.get("Notification"))
        self._UpdatedAt = params.get("UpdatedAt")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """Prometheus alerting rule

    """

    def __init__(self):
        r"""
        :param _Name: Rule name
        :type Name: str
        :param _Rule: Prometheus statement
        :type Rule: str
        :param _Labels: Additional tags
        :type Labels: list of Label
        :param _Template: Alert sending template
        :type Template: str
        :param _For: Duration
        :type For: str
        :param _Describe: Rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param _Annotations: See `annotations` in the Prometheus rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Annotations: list of Label
        :param _RuleState: Alerting rule status
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleState: int
        """
        self._Name = None
        self._Rule = None
        self._Labels = None
        self._Template = None
        self._For = None
        self._Describe = None
        self._Annotations = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def For(self):
        return self._For

    @For.setter
    def For(self, For):
        self._For = For

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Template = params.get("Template")
        self._For = params.get("For")
        self._Describe = params.get("Describe")
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusClusterAgentBasic(AbstractModel):
    """Basic information of the cluster associated with a Tencent Cloud Observability Platform (TCOP)-integrated TMP instance.

    """

    def __init__(self):
        r"""
        :param _Region: Cluster ID
        :type Region: str
        :param _ClusterType: Cluster type
        :type ClusterType: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _EnableExternal: Whether to enable public network CLB
        :type EnableExternal: bool
        :param _InClusterPodConfig: Pod configurations of components deployed in the cluster
        :type InClusterPodConfig: :class:`tencentcloud.monitor.v20180724.models.PrometheusClusterAgentPodConfig`
        :param _ExternalLabels: External labels, which will be attached to all metrics collected by this cluster
        :type ExternalLabels: list of Label
        :param _NotInstallBasicScrape: Whether to install the default collection configuration.
        :type NotInstallBasicScrape: bool
        :param _NotScrape: Whether to collect metrics (`true`: Drop all metrics; `false`: Collect default metrics)
        :type NotScrape: bool
        :param _OpenDefaultRecord: Whether to enable the default recording rule
        :type OpenDefaultRecord: bool
        """
        self._Region = None
        self._ClusterType = None
        self._ClusterId = None
        self._EnableExternal = None
        self._InClusterPodConfig = None
        self._ExternalLabels = None
        self._NotInstallBasicScrape = None
        self._NotScrape = None
        self._OpenDefaultRecord = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnableExternal(self):
        return self._EnableExternal

    @EnableExternal.setter
    def EnableExternal(self, EnableExternal):
        self._EnableExternal = EnableExternal

    @property
    def InClusterPodConfig(self):
        return self._InClusterPodConfig

    @InClusterPodConfig.setter
    def InClusterPodConfig(self, InClusterPodConfig):
        self._InClusterPodConfig = InClusterPodConfig

    @property
    def ExternalLabels(self):
        return self._ExternalLabels

    @ExternalLabels.setter
    def ExternalLabels(self, ExternalLabels):
        self._ExternalLabels = ExternalLabels

    @property
    def NotInstallBasicScrape(self):
        return self._NotInstallBasicScrape

    @NotInstallBasicScrape.setter
    def NotInstallBasicScrape(self, NotInstallBasicScrape):
        self._NotInstallBasicScrape = NotInstallBasicScrape

    @property
    def NotScrape(self):
        return self._NotScrape

    @NotScrape.setter
    def NotScrape(self, NotScrape):
        self._NotScrape = NotScrape

    @property
    def OpenDefaultRecord(self):
        return self._OpenDefaultRecord

    @OpenDefaultRecord.setter
    def OpenDefaultRecord(self, OpenDefaultRecord):
        self._OpenDefaultRecord = OpenDefaultRecord


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._EnableExternal = params.get("EnableExternal")
        if params.get("InClusterPodConfig") is not None:
            self._InClusterPodConfig = PrometheusClusterAgentPodConfig()
            self._InClusterPodConfig._deserialize(params.get("InClusterPodConfig"))
        if params.get("ExternalLabels") is not None:
            self._ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self._ExternalLabels.append(obj)
        self._NotInstallBasicScrape = params.get("NotInstallBasicScrape")
        self._NotScrape = params.get("NotScrape")
        self._OpenDefaultRecord = params.get("OpenDefaultRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusClusterAgentPodConfig(AbstractModel):
    """Additional pod configurations of the components deployed in the cluster when a cluster is associated

    """

    def __init__(self):
        r"""
        :param _HostNet: Whether to use HostNetWork
        :type HostNet: bool
        :param _NodeSelector: A parameter used to specify the running nodes for a pod
        :type NodeSelector: list of Label
        :param _Tolerations: Tolerable taints
        :type Tolerations: list of Toleration
        """
        self._HostNet = None
        self._NodeSelector = None
        self._Tolerations = None

    @property
    def HostNet(self):
        return self._HostNet

    @HostNet.setter
    def HostNet(self, HostNet):
        self._HostNet = HostNet

    @property
    def NodeSelector(self):
        return self._NodeSelector

    @NodeSelector.setter
    def NodeSelector(self, NodeSelector):
        self._NodeSelector = NodeSelector

    @property
    def Tolerations(self):
        return self._Tolerations

    @Tolerations.setter
    def Tolerations(self, Tolerations):
        self._Tolerations = Tolerations


    def _deserialize(self, params):
        self._HostNet = params.get("HostNet")
        if params.get("NodeSelector") is not None:
            self._NodeSelector = []
            for item in params.get("NodeSelector"):
                obj = Label()
                obj._deserialize(item)
                self._NodeSelector.append(obj)
        if params.get("Tolerations") is not None:
            self._Tolerations = []
            for item in params.get("Tolerations"):
                obj = Toleration()
                obj._deserialize(item)
                self._Tolerations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfigItem(AbstractModel):
    """Prometheus configuration

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Config: Configuration content
        :type Config: str
        :param _TemplateId: If the configuration comes from a template, this parameter is the template ID, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param _Targets: Number of targets
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: :class:`tencentcloud.monitor.v20180724.models.Targets`
        """
        self._Name = None
        self._Config = None
        self._TemplateId = None
        self._Targets = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Config = params.get("Config")
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = Targets()
            self._Targets._deserialize(params.get("Targets"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceGrantInfo(AbstractModel):
    """Instance authorization information

    """

    def __init__(self):
        r"""
        :param _HasChargeOperation: Whether there is permission to operate on the billing information. Valid values: 1 (yes), 2 (no).
        :type HasChargeOperation: int
        :param _HasVpcDisplay: Whether there is permission to display the VPC information. Valid values: 1 (yes), 2 (no).
        :type HasVpcDisplay: int
        :param _HasGrafanaStatusChange: Whether there is permission to change the Grafana status. Valid values: 1 (yes), 2 (no).
        :type HasGrafanaStatusChange: int
        :param _HasAgentManage: Whether there is permission to manage agents. Valid values: 1 (yes), 2 (no).
        :type HasAgentManage: int
        :param _HasTkeManage: Whether there is permission to manage TKE integrations. Valid values: 1 (yes), 2 (no).
        :type HasTkeManage: int
        :param _HasApiOperation: Whether there is permission to display the API information. Valid values: 1 (yes), 2 (no).
        :type HasApiOperation: int
        """
        self._HasChargeOperation = None
        self._HasVpcDisplay = None
        self._HasGrafanaStatusChange = None
        self._HasAgentManage = None
        self._HasTkeManage = None
        self._HasApiOperation = None

    @property
    def HasChargeOperation(self):
        return self._HasChargeOperation

    @HasChargeOperation.setter
    def HasChargeOperation(self, HasChargeOperation):
        self._HasChargeOperation = HasChargeOperation

    @property
    def HasVpcDisplay(self):
        return self._HasVpcDisplay

    @HasVpcDisplay.setter
    def HasVpcDisplay(self, HasVpcDisplay):
        self._HasVpcDisplay = HasVpcDisplay

    @property
    def HasGrafanaStatusChange(self):
        return self._HasGrafanaStatusChange

    @HasGrafanaStatusChange.setter
    def HasGrafanaStatusChange(self, HasGrafanaStatusChange):
        self._HasGrafanaStatusChange = HasGrafanaStatusChange

    @property
    def HasAgentManage(self):
        return self._HasAgentManage

    @HasAgentManage.setter
    def HasAgentManage(self, HasAgentManage):
        self._HasAgentManage = HasAgentManage

    @property
    def HasTkeManage(self):
        return self._HasTkeManage

    @HasTkeManage.setter
    def HasTkeManage(self, HasTkeManage):
        self._HasTkeManage = HasTkeManage

    @property
    def HasApiOperation(self):
        return self._HasApiOperation

    @HasApiOperation.setter
    def HasApiOperation(self, HasApiOperation):
        self._HasApiOperation = HasApiOperation


    def _deserialize(self, params):
        self._HasChargeOperation = params.get("HasChargeOperation")
        self._HasVpcDisplay = params.get("HasVpcDisplay")
        self._HasGrafanaStatusChange = params.get("HasGrafanaStatusChange")
        self._HasAgentManage = params.get("HasAgentManage")
        self._HasTkeManage = params.get("HasTkeManage")
        self._HasApiOperation = params.get("HasApiOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceTenantUsage(AbstractModel):
    """TMP usage information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _CalcDate: Billing cycle
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcDate: str
        :param _Total: Total usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: float
        :param _Basic: Usage of basic (free) metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type Basic: float
        :param _Fee: Usage of paid metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fee: float
        """
        self._InstanceId = None
        self._CalcDate = None
        self._Total = None
        self._Basic = None
        self._Fee = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CalcDate(self):
        return self._CalcDate

    @CalcDate.setter
    def CalcDate(self, CalcDate):
        self._CalcDate = CalcDate

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Basic(self):
        return self._Basic

    @Basic.setter
    def Basic(self, Basic):
        self._Basic = Basic

    @property
    def Fee(self):
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CalcDate = params.get("CalcDate")
        self._Total = params.get("Total")
        self._Basic = params.get("Basic")
        self._Fee = params.get("Fee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesItem(AbstractModel):
    """Prometheus service response body

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _InstanceChargeType: Instance billing mode. Valid values:
<ul>
<li>2: Monthly subscription</li>
<li>3: Pay-as-you-go</li>
</ul>
        :type InstanceChargeType: int
        :param _RegionId: Region ID
        :type RegionId: int
        :param _Zone: AZ
        :type Zone: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param _InstanceStatus: Instance status. Valid values:
<ul>
<li>1: Creating</li>
<li>2: Running</li>
<li>3: Abnormal</li>
<li>4: Rebooting</li>
<li>5: Terminating</li>
<li>6: Service suspended</li>
<li>8: Suspending service for overdue payment</li>
<li>9: Service suspended for overdue payment</li>
</ul>
        :type InstanceStatus: int
        :param _GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _EnableGrafana: Whether Grafana is enabled
<li>0: Disabled</li>
<li>1: Enabled</li>
        :type EnableGrafana: int
        :param _IPv4Address: Instance IPv4 address
Note: This field may return null, indicating that no valid values can be obtained.
        :type IPv4Address: str
        :param _TagSpecification: List of tags associated with the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: list of PrometheusTag
        :param _ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _ChargeStatus: Billing status
<ul>
<li>1: Normal</li>
<li>2: Expired</li>
<li>3: Terminated</li>
<li>4: Assigning</li>
<li>5: Assignment failed</li>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param _SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _AutoRenewFlag: Auto-renewal flag
<ul>
<li>0: Auto-renewal not enabled</li>
<li>1: Auto-renewal enabled</li>
<li>2: Auto-renewal prohibited</li>
<li>-1: Invalid</ii>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _IsNearExpire: Expiring soon
<ul>
<li>0: No</li>
<li>1: Yes</li>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsNearExpire: int
        :param _AuthToken: The token required for data writing
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthToken: str
        :param _RemoteWrite: Prometheus remote write address
Note: This field may return null, indicating that no valid values can be obtained.
        :type RemoteWrite: str
        :param _ApiRootPath: Prometheus HTTP API root address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApiRootPath: str
        :param _ProxyAddress: Proxy address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyAddress: str
        :param _GrafanaStatus: Grafana status
<ul>
<li>1: Creating</li>
<li>2: Running</li>
<li>3: Abnormal</li>
<li>4: Restarting</li>
<li>5: Terminating</li>
<li>6: Service suspended</li>
<li>7: Deleted</li>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaStatus: int
        :param _GrafanaIpWhiteList: Grafana IP allowlist, where IPs are separated by comma.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaIpWhiteList: str
        :param _Grant: Instance authorization information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Grant: :class:`tencentcloud.monitor.v20180724.models.PrometheusInstanceGrantInfo`
        :param _GrafanaInstanceId: ID of the bound Grafana instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaInstanceId: str
        :param _AlertRuleLimit: The alert rule limit
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRuleLimit: int
        :param _RecordingRuleLimit: The recording rule limit
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordingRuleLimit: int
        :param _MigrationType: Migration status. 0: Not migrating; 1: Migrating from source instance; 2: Migrating to target instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrationType: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._RegionId = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._DataRetentionTime = None
        self._InstanceStatus = None
        self._GrafanaURL = None
        self._CreatedAt = None
        self._EnableGrafana = None
        self._IPv4Address = None
        self._TagSpecification = None
        self._ExpireTime = None
        self._ChargeStatus = None
        self._SpecName = None
        self._AutoRenewFlag = None
        self._IsNearExpire = None
        self._AuthToken = None
        self._RemoteWrite = None
        self._ApiRootPath = None
        self._ProxyAddress = None
        self._GrafanaStatus = None
        self._GrafanaIpWhiteList = None
        self._Grant = None
        self._GrafanaInstanceId = None
        self._AlertRuleLimit = None
        self._RecordingRuleLimit = None
        self._MigrationType = None

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
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def IPv4Address(self):
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def IsNearExpire(self):
        return self._IsNearExpire

    @IsNearExpire.setter
    def IsNearExpire(self, IsNearExpire):
        self._IsNearExpire = IsNearExpire

    @property
    def AuthToken(self):
        return self._AuthToken

    @AuthToken.setter
    def AuthToken(self, AuthToken):
        self._AuthToken = AuthToken

    @property
    def RemoteWrite(self):
        return self._RemoteWrite

    @RemoteWrite.setter
    def RemoteWrite(self, RemoteWrite):
        self._RemoteWrite = RemoteWrite

    @property
    def ApiRootPath(self):
        return self._ApiRootPath

    @ApiRootPath.setter
    def ApiRootPath(self, ApiRootPath):
        self._ApiRootPath = ApiRootPath

    @property
    def ProxyAddress(self):
        return self._ProxyAddress

    @ProxyAddress.setter
    def ProxyAddress(self, ProxyAddress):
        self._ProxyAddress = ProxyAddress

    @property
    def GrafanaStatus(self):
        return self._GrafanaStatus

    @GrafanaStatus.setter
    def GrafanaStatus(self, GrafanaStatus):
        self._GrafanaStatus = GrafanaStatus

    @property
    def GrafanaIpWhiteList(self):
        return self._GrafanaIpWhiteList

    @GrafanaIpWhiteList.setter
    def GrafanaIpWhiteList(self, GrafanaIpWhiteList):
        self._GrafanaIpWhiteList = GrafanaIpWhiteList

    @property
    def Grant(self):
        return self._Grant

    @Grant.setter
    def Grant(self, Grant):
        self._Grant = Grant

    @property
    def GrafanaInstanceId(self):
        return self._GrafanaInstanceId

    @GrafanaInstanceId.setter
    def GrafanaInstanceId(self, GrafanaInstanceId):
        self._GrafanaInstanceId = GrafanaInstanceId

    @property
    def AlertRuleLimit(self):
        return self._AlertRuleLimit

    @AlertRuleLimit.setter
    def AlertRuleLimit(self, AlertRuleLimit):
        self._AlertRuleLimit = AlertRuleLimit

    @property
    def RecordingRuleLimit(self):
        return self._RecordingRuleLimit

    @RecordingRuleLimit.setter
    def RecordingRuleLimit(self, RecordingRuleLimit):
        self._RecordingRuleLimit = RecordingRuleLimit

    @property
    def MigrationType(self):
        return self._MigrationType

    @MigrationType.setter
    def MigrationType(self, MigrationType):
        self._MigrationType = MigrationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._RegionId = params.get("RegionId")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._InstanceStatus = params.get("InstanceStatus")
        self._GrafanaURL = params.get("GrafanaURL")
        self._CreatedAt = params.get("CreatedAt")
        self._EnableGrafana = params.get("EnableGrafana")
        self._IPv4Address = params.get("IPv4Address")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._ExpireTime = params.get("ExpireTime")
        self._ChargeStatus = params.get("ChargeStatus")
        self._SpecName = params.get("SpecName")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._IsNearExpire = params.get("IsNearExpire")
        self._AuthToken = params.get("AuthToken")
        self._RemoteWrite = params.get("RemoteWrite")
        self._ApiRootPath = params.get("ApiRootPath")
        self._ProxyAddress = params.get("ProxyAddress")
        self._GrafanaStatus = params.get("GrafanaStatus")
        self._GrafanaIpWhiteList = params.get("GrafanaIpWhiteList")
        if params.get("Grant") is not None:
            self._Grant = PrometheusInstanceGrantInfo()
            self._Grant._deserialize(params.get("Grant"))
        self._GrafanaInstanceId = params.get("GrafanaInstanceId")
        self._AlertRuleLimit = params.get("AlertRuleLimit")
        self._RecordingRuleLimit = params.get("RecordingRuleLimit")
        self._MigrationType = params.get("MigrationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesOverview(AbstractModel):
    """TMP v2 instance overview

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _InstanceStatus: Running status. Valid values: `1` (creating); `2` (running); `3` (abnormal); `4` (restarting); `5` (terminating); `6` (stopped); `7` (deleted).
        :type InstanceStatus: int
        :param _ChargeStatus: Billing status. Valid values: `1` (normal); `2` (expired); `3` (terminated); `4` (assigning); `5` (failed to assign)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param _EnableGrafana: Whether Grafana is enabled. Valid values: `0` (no); `1` (yes).
        :type EnableGrafana: int
        :param _GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param _InstanceChargeType: Instance payment type. Valid values: `1` (trial edition); `2` (prepaid)
        :type InstanceChargeType: int
        :param _SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param _ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: `0` (auto-renewal not enabled); `1` (auto-renewal enabled); `2` (auto-renewal prohibited); `-1` (invalid).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param _BoundTotal: Total number of bound clusters
        :type BoundTotal: int
        :param _BoundNormal: Total number of bound clusters in the normal status
        :type BoundNormal: int
        :param _ResourcePackageStatus: Resource pack status (`0`: Unavailable; `1`: Available)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackageStatus: int
        :param _ResourcePackageSpecName: Resource pack specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourcePackageSpecName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceStatus = None
        self._ChargeStatus = None
        self._EnableGrafana = None
        self._GrafanaURL = None
        self._InstanceChargeType = None
        self._SpecName = None
        self._DataRetentionTime = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._BoundTotal = None
        self._BoundNormal = None
        self._ResourcePackageStatus = None
        self._ResourcePackageSpecName = None

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
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def EnableGrafana(self):
        return self._EnableGrafana

    @EnableGrafana.setter
    def EnableGrafana(self, EnableGrafana):
        self._EnableGrafana = EnableGrafana

    @property
    def GrafanaURL(self):
        return self._GrafanaURL

    @GrafanaURL.setter
    def GrafanaURL(self, GrafanaURL):
        self._GrafanaURL = GrafanaURL

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataRetentionTime(self):
        return self._DataRetentionTime

    @DataRetentionTime.setter
    def DataRetentionTime(self, DataRetentionTime):
        self._DataRetentionTime = DataRetentionTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def BoundTotal(self):
        return self._BoundTotal

    @BoundTotal.setter
    def BoundTotal(self, BoundTotal):
        self._BoundTotal = BoundTotal

    @property
    def BoundNormal(self):
        return self._BoundNormal

    @BoundNormal.setter
    def BoundNormal(self, BoundNormal):
        self._BoundNormal = BoundNormal

    @property
    def ResourcePackageStatus(self):
        return self._ResourcePackageStatus

    @ResourcePackageStatus.setter
    def ResourcePackageStatus(self, ResourcePackageStatus):
        self._ResourcePackageStatus = ResourcePackageStatus

    @property
    def ResourcePackageSpecName(self):
        return self._ResourcePackageSpecName

    @ResourcePackageSpecName.setter
    def ResourcePackageSpecName(self, ResourcePackageSpecName):
        self._ResourcePackageSpecName = ResourcePackageSpecName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ChargeStatus = params.get("ChargeStatus")
        self._EnableGrafana = params.get("EnableGrafana")
        self._GrafanaURL = params.get("GrafanaURL")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SpecName = params.get("SpecName")
        self._DataRetentionTime = params.get("DataRetentionTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._BoundTotal = params.get("BoundTotal")
        self._BoundNormal = params.get("BoundNormal")
        self._ResourcePackageStatus = params.get("ResourcePackageStatus")
        self._ResourcePackageSpecName = params.get("ResourcePackageSpecName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusJobTargets(AbstractModel):
    """Targets of a Prometheus job

    """


class PrometheusNotificationItem(AbstractModel):
    """Alert notification channel configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether it is enabled
        :type Enabled: bool
        :param _Type: Channel type. Default value: `amp`. Valid values:
`amp`
`webhook`
`alertmanager`
        :type Type: str
        :param _WebHook: If `Type` is `webhook`, this field is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WebHook: str
        :param _AlertManager: If `Type` is `alertmanager`, this field is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertManager: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertManagerConfig`
        :param _RepeatInterval: Convergence time
        :type RepeatInterval: str
        :param _TimeRangeStart: Effect start time
        :type TimeRangeStart: str
        :param _TimeRangeEnd: Effect end time
        :type TimeRangeEnd: str
        :param _NotifyWay: Alert notification channel. Valid values: `SMS`, `EMAIL`, `CALL`, `WECHAT`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NotifyWay: list of str
        :param _ReceiverGroups: Alert recipient group (user group)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReceiverGroups: list of str
        :param _PhoneNotifyOrder: Alert call sequence.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNotifyOrder: list of int non-negative
        :param _PhoneCircleTimes: Number of alert calls.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleTimes: int
        :param _PhoneInnerInterval: Alert call interval within a cycle in seconds.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneInnerInterval: int
        :param _PhoneCircleInterval: Alert call cycle interval in seconds.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleInterval: int
        :param _PhoneArriveNotice: Alert call receipt notification
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneArriveNotice: bool
        """
        self._Enabled = None
        self._Type = None
        self._WebHook = None
        self._AlertManager = None
        self._RepeatInterval = None
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._NotifyWay = None
        self._ReceiverGroups = None
        self._PhoneNotifyOrder = None
        self._PhoneCircleTimes = None
        self._PhoneInnerInterval = None
        self._PhoneCircleInterval = None
        self._PhoneArriveNotice = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WebHook(self):
        return self._WebHook

    @WebHook.setter
    def WebHook(self, WebHook):
        self._WebHook = WebHook

    @property
    def AlertManager(self):
        return self._AlertManager

    @AlertManager.setter
    def AlertManager(self, AlertManager):
        self._AlertManager = AlertManager

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

    @property
    def TimeRangeStart(self):
        return self._TimeRangeStart

    @TimeRangeStart.setter
    def TimeRangeStart(self, TimeRangeStart):
        self._TimeRangeStart = TimeRangeStart

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PhoneNotifyOrder(self):
        return self._PhoneNotifyOrder

    @PhoneNotifyOrder.setter
    def PhoneNotifyOrder(self, PhoneNotifyOrder):
        self._PhoneNotifyOrder = PhoneNotifyOrder

    @property
    def PhoneCircleTimes(self):
        return self._PhoneCircleTimes

    @PhoneCircleTimes.setter
    def PhoneCircleTimes(self, PhoneCircleTimes):
        self._PhoneCircleTimes = PhoneCircleTimes

    @property
    def PhoneInnerInterval(self):
        return self._PhoneInnerInterval

    @PhoneInnerInterval.setter
    def PhoneInnerInterval(self, PhoneInnerInterval):
        self._PhoneInnerInterval = PhoneInnerInterval

    @property
    def PhoneCircleInterval(self):
        return self._PhoneCircleInterval

    @PhoneCircleInterval.setter
    def PhoneCircleInterval(self, PhoneCircleInterval):
        self._PhoneCircleInterval = PhoneCircleInterval

    @property
    def PhoneArriveNotice(self):
        return self._PhoneArriveNotice

    @PhoneArriveNotice.setter
    def PhoneArriveNotice(self, PhoneArriveNotice):
        self._PhoneArriveNotice = PhoneArriveNotice


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Type = params.get("Type")
        self._WebHook = params.get("WebHook")
        if params.get("AlertManager") is not None:
            self._AlertManager = PrometheusAlertManagerConfig()
            self._AlertManager._deserialize(params.get("AlertManager"))
        self._RepeatInterval = params.get("RepeatInterval")
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._NotifyWay = params.get("NotifyWay")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self._PhoneCircleTimes = params.get("PhoneCircleTimes")
        self._PhoneInnerInterval = params.get("PhoneInnerInterval")
        self._PhoneCircleInterval = params.get("PhoneCircleInterval")
        self._PhoneArriveNotice = params.get("PhoneArriveNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRecordRuleYamlItem(AbstractModel):
    """Details of the Prometheus recording rule instance, including the cluster ID.

    """

    def __init__(self):
        r"""
        :param _Name: Instance name
        :type Name: str
        :param _UpdateTime: Last update time
        :type UpdateTime: str
        :param _TemplateId: YAML content
        :type TemplateId: str
        :param _Content: If the recording rule comes from a template, `TemplateId` is the template ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param _ClusterId: If the recording rule comes from the user cluster CRD resource definition, `ClusterId` is the cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Id: id
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Count: Number of rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        """
        self._Name = None
        self._UpdateTime = None
        self._TemplateId = None
        self._Content = None
        self._ClusterId = None
        self._Status = None
        self._Id = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._UpdateTime = params.get("UpdateTime")
        self._TemplateId = params.get("TemplateId")
        self._Content = params.get("Content")
        self._ClusterId = params.get("ClusterId")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRuleKV(AbstractModel):
    """KV parameter of the Prometheus alerting rule

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
        


class PrometheusRuleSet(AbstractModel):
    """Set of Prometheus alerting rules

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleName: Rule name
        :type RuleName: str
        :param _RuleState: Rule status code
        :type RuleState: int
        :param _Type: Rule category
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Labels: List of rule tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: List of rule annotations
Note: This field may return null, indicating that no valid values can be obtained.
        :type Annotations: list of PrometheusRuleKV
        :param _Expr: Rule expression
Note: This field may return null, indicating that no valid values can be obtained.
        :type Expr: str
        :param _Duration: Rule alert duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: str
        :param _Receivers: List of alert recipient groups
Note: This field may return null, indicating that no valid values can be obtained.
        :type Receivers: list of str
        :param _Health: Rule status. Valid values:
<li>unknown: Unknown</li>
<li>pending: Loading</li>
<li>ok: Running</li>
<li>err: Error</li>
        :type Health: str
        :param _CreatedAt: Rule creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedAt: Rule update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        """
        self._RuleId = None
        self._RuleName = None
        self._RuleState = None
        self._Type = None
        self._Labels = None
        self._Annotations = None
        self._Expr = None
        self._Duration = None
        self._Receivers = None
        self._Health = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleState = params.get("RuleState")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Expr = params.get("Expr")
        self._Duration = params.get("Duration")
        self._Receivers = params.get("Receivers")
        self._Health = params.get("Health")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusScrapeJob(AbstractModel):
    """Prometheus scrape task

    """

    def __init__(self):
        r"""
        :param _Name: Task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _AgentId: Agent ID
        :type AgentId: str
        :param _JobId: Task ID
        :type JobId: str
        :param _Config: Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Config: str
        """
        self._Name = None
        self._AgentId = None
        self._JobId = None
        self._Config = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AgentId = params.get("AgentId")
        self._JobId = params.get("JobId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTag(AbstractModel):
    """TMP tag

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
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
        


class PrometheusTemp(AbstractModel):
    """Template instance

    """

    def __init__(self):
        r"""
        :param _Name: Template name
        :type Name: str
        :param _Level: Template dimension. Valid values:
`instance`
`cluster`
        :type Level: str
        :param _Describe: Template description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param _RecordRules: This parameter is valid if `Level` is `instance`.
List of recording rules in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordRules: list of PrometheusConfigItem
        :param _ServiceMonitors: This parameter is valid if `Level` is `cluster`.
List of ServiceMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: This parameter is valid if `Level` is `cluster`.
List of PodMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: This parameter is valid if `Level` is `cluster`.
List of RawJob rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawJobs: list of PrometheusConfigItem
        :param _TemplateId: Template ID, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param _UpdateTime: Last update time, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Version: The current version, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _IsDefault: Whether it is the default template provided by the system, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDefault: bool
        :param _AlertDetailRules: This parameter is valid if `Level` is `instance`.
List of alert configurations in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        :param _TargetsTotal: Number of associated instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetsTotal: int
        """
        self._Name = None
        self._Level = None
        self._Describe = None
        self._RecordRules = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._TemplateId = None
        self._UpdateTime = None
        self._Version = None
        self._IsDefault = None
        self._AlertDetailRules = None
        self._TargetsTotal = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def RecordRules(self):
        return self._RecordRules

    @RecordRules.setter
    def RecordRules(self, RecordRules):
        self._RecordRules = RecordRules

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def AlertDetailRules(self):
        return self._AlertDetailRules

    @AlertDetailRules.setter
    def AlertDetailRules(self, AlertDetailRules):
        self._AlertDetailRules = AlertDetailRules

    @property
    def TargetsTotal(self):
        return self._TargetsTotal

    @TargetsTotal.setter
    def TargetsTotal(self, TargetsTotal):
        self._TargetsTotal = TargetsTotal


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Describe = params.get("Describe")
        if params.get("RecordRules") is not None:
            self._RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RecordRules.append(obj)
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._UpdateTime = params.get("UpdateTime")
        self._Version = params.get("Version")
        self._IsDefault = params.get("IsDefault")
        if params.get("AlertDetailRules") is not None:
            self._AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertDetailRules.append(obj)
        self._TargetsTotal = params.get("TargetsTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTempModify(AbstractModel):
    """Modifiable items in the TMP template

    """

    def __init__(self):
        r"""
        :param _Name: Name
        :type Name: str
        :param _Describe: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param _ServiceMonitors: This parameter is valid if `Level` is `cluster`.
List of ServiceMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceMonitors: list of PrometheusConfigItem
        :param _PodMonitors: This parameter is valid if `Level` is `cluster`.
List of PodMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodMonitors: list of PrometheusConfigItem
        :param _RawJobs: This parameter is valid if `Level` is `cluster`.
List of RawJob rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawJobs: list of PrometheusConfigItem
        :param _RecordRules: This parameter is valid if `Level` is `instance`.
List of recording rules in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordRules: list of PrometheusConfigItem
        :param _AlertDetailRules: Modification content, which is valid only if template type is `Alert`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        """
        self._Name = None
        self._Describe = None
        self._ServiceMonitors = None
        self._PodMonitors = None
        self._RawJobs = None
        self._RecordRules = None
        self._AlertDetailRules = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ServiceMonitors(self):
        return self._ServiceMonitors

    @ServiceMonitors.setter
    def ServiceMonitors(self, ServiceMonitors):
        self._ServiceMonitors = ServiceMonitors

    @property
    def PodMonitors(self):
        return self._PodMonitors

    @PodMonitors.setter
    def PodMonitors(self, PodMonitors):
        self._PodMonitors = PodMonitors

    @property
    def RawJobs(self):
        return self._RawJobs

    @RawJobs.setter
    def RawJobs(self, RawJobs):
        self._RawJobs = RawJobs

    @property
    def RecordRules(self):
        return self._RecordRules

    @RecordRules.setter
    def RecordRules(self, RecordRules):
        self._RecordRules = RecordRules

    @property
    def AlertDetailRules(self):
        return self._AlertDetailRules

    @AlertDetailRules.setter
    def AlertDetailRules(self, AlertDetailRules):
        self._AlertDetailRules = AlertDetailRules


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Describe = params.get("Describe")
        if params.get("ServiceMonitors") is not None:
            self._ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self._PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self._RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RawJobs.append(obj)
        if params.get("RecordRules") is not None:
            self._RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self._RecordRules.append(obj)
        if params.get("AlertDetailRules") is not None:
            self._AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self._AlertDetailRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """Sync target of the TMP template

    """

    def __init__(self):
        r"""
        :param _Region: Target region
        :type Region: str
        :param _InstanceId: Target instance
        :type InstanceId: str
        :param _ClusterId: Cluster ID, which is required only if the `Level` of the collection template is `cluster`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _SyncTime: Last sync time, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SyncTime: str
        :param _Version: The currently used template version, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _ClusterType: Cluster type, which is required only if the `Level` of the collection template is `cluster`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: str
        :param _InstanceName: Instance name, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _ClusterName: Cluster name, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        """
        self._Region = None
        self._InstanceId = None
        self._ClusterId = None
        self._SyncTime = None
        self._Version = None
        self._ClusterType = None
        self._InstanceName = None
        self._ClusterName = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SyncTime(self):
        return self._SyncTime

    @SyncTime.setter
    def SyncTime(self, SyncTime):
        self._SyncTime = SyncTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._SyncTime = params.get("SyncTime")
        self._Version = params.get("Version")
        self._ClusterType = params.get("ClusterType")
        self._InstanceName = params.get("InstanceName")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusZoneItem(AbstractModel):
    """Region information returned by `PrometheusZoneItem`

    """

    def __init__(self):
        r"""
        :param _Zone: AZ
        :type Zone: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _ZoneState: AZ status. Valid values: `0`(Unavailable), `1` (Available).
        :type ZoneState: int
        :param _RegionId: Region ID
        :type RegionId: int
        :param _ZoneName: AZ name
        :type ZoneName: str
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneState = None
        self._RegionId = None
        self._ZoneName = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        self._RegionId = params.get("RegionId")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMonitorDataRequest(AbstractModel):
    """PutMonitorData request structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: A group of metrics and data.
        :type Metrics: list of MetricDatum
        :param _AnnounceIp: IP address that is automatically specified when monitoring data is reported.
        :type AnnounceIp: str
        :param _AnnounceTimestamp: Timestamp that is automatically specified when monitoring data is reported.
        :type AnnounceTimestamp: int
        :param _AnnounceInstance: IP address or product instance ID that is automatically specified when monitoring data is reported.
        :type AnnounceInstance: str
        """
        self._Metrics = None
        self._AnnounceIp = None
        self._AnnounceTimestamp = None
        self._AnnounceInstance = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def AnnounceIp(self):
        return self._AnnounceIp

    @AnnounceIp.setter
    def AnnounceIp(self, AnnounceIp):
        self._AnnounceIp = AnnounceIp

    @property
    def AnnounceTimestamp(self):
        return self._AnnounceTimestamp

    @AnnounceTimestamp.setter
    def AnnounceTimestamp(self, AnnounceTimestamp):
        self._AnnounceTimestamp = AnnounceTimestamp

    @property
    def AnnounceInstance(self):
        return self._AnnounceInstance

    @AnnounceInstance.setter
    def AnnounceInstance(self, AnnounceInstance):
        self._AnnounceInstance = AnnounceInstance


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = MetricDatum()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._AnnounceIp = params.get("AnnounceIp")
        self._AnnounceTimestamp = params.get("AnnounceTimestamp")
        self._AnnounceInstance = params.get("AnnounceInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMonitorDataResponse(AbstractModel):
    """PutMonitorData response structure.

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


class ReceiverInfo(AbstractModel):
    """Recipient information.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates “10:0:0”.
        :type StartTime: int
        :param _EndTime: End time of the alarm period. The meaning is the same as that of StartTime.
        :type EndTime: int
        :param _NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".
        :type NotifyWay: list of str
        :param _ReceiverType: Recipient type. Valid values: group and user.
        :type ReceiverType: str
        :param _Id: ReceiverId
        :type Id: int
        :param _SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).
        :type SendFor: list of str
        :param _UidList: UID of the phone call alarm.
        :type UidList: list of int
        :param _RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param _PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param _RoundInterval: Intervals of alarm call rounds in seconds.
        :type RoundInterval: int
        :param _RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.
        :type RecoverNotify: list of str
        :param _NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.
        :type NeedSendNotice: int
        :param _ReceiverGroupList: Recipient group list. The list of recipient group IDs that is queried by API.
        :type ReceiverGroupList: list of int
        :param _ReceiverUserList: Recipient list. The list of recipient IDs that is queried by API.
        :type ReceiverUserList: list of int
        :param _ReceiveLanguage: Language of received alarms. Enumerated values: zh-CN and en-US.
        :type ReceiveLanguage: str
        """
        self._StartTime = None
        self._EndTime = None
        self._NotifyWay = None
        self._ReceiverType = None
        self._Id = None
        self._SendFor = None
        self._UidList = None
        self._RoundNumber = None
        self._PersonInterval = None
        self._RoundInterval = None
        self._RecoverNotify = None
        self._NeedSendNotice = None
        self._ReceiverGroupList = None
        self._ReceiverUserList = None
        self._ReceiveLanguage = None

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
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SendFor(self):
        return self._SendFor

    @SendFor.setter
    def SendFor(self, SendFor):
        self._SendFor = SendFor

    @property
    def UidList(self):
        return self._UidList

    @UidList.setter
    def UidList(self, UidList):
        self._UidList = UidList

    @property
    def RoundNumber(self):
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def PersonInterval(self):
        return self._PersonInterval

    @PersonInterval.setter
    def PersonInterval(self, PersonInterval):
        self._PersonInterval = PersonInterval

    @property
    def RoundInterval(self):
        return self._RoundInterval

    @RoundInterval.setter
    def RoundInterval(self, RoundInterval):
        self._RoundInterval = RoundInterval

    @property
    def RecoverNotify(self):
        return self._RecoverNotify

    @RecoverNotify.setter
    def RecoverNotify(self, RecoverNotify):
        self._RecoverNotify = RecoverNotify

    @property
    def NeedSendNotice(self):
        return self._NeedSendNotice

    @NeedSendNotice.setter
    def NeedSendNotice(self, NeedSendNotice):
        self._NeedSendNotice = NeedSendNotice

    @property
    def ReceiverGroupList(self):
        return self._ReceiverGroupList

    @ReceiverGroupList.setter
    def ReceiverGroupList(self, ReceiverGroupList):
        self._ReceiverGroupList = ReceiverGroupList

    @property
    def ReceiverUserList(self):
        return self._ReceiverUserList

    @ReceiverUserList.setter
    def ReceiverUserList(self, ReceiverUserList):
        self._ReceiverUserList = ReceiverUserList

    @property
    def ReceiveLanguage(self):
        return self._ReceiveLanguage

    @ReceiveLanguage.setter
    def ReceiveLanguage(self, ReceiveLanguage):
        self._ReceiveLanguage = ReceiveLanguage


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NotifyWay = params.get("NotifyWay")
        self._ReceiverType = params.get("ReceiverType")
        self._Id = params.get("Id")
        self._SendFor = params.get("SendFor")
        self._UidList = params.get("UidList")
        self._RoundNumber = params.get("RoundNumber")
        self._PersonInterval = params.get("PersonInterval")
        self._RoundInterval = params.get("RoundInterval")
        self._RecoverNotify = params.get("RecoverNotify")
        self._NeedSendNotice = params.get("NeedSendNotice")
        self._ReceiverGroupList = params.get("ReceiverGroupList")
        self._ReceiverUserList = params.get("ReceiverUserList")
        self._ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordingRuleSet(AbstractModel):
    """Response structure information of the Prometheus recording rule

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleState: Rule status code
        :type RuleState: int
        :param _Name: Group name
        :type Name: str
        :param _Group: Rule group
        :type Group: str
        :param _Total: Number of rules
        :type Total: int
        :param _CreatedAt: Rule creation time
        :type CreatedAt: str
        :param _UpdatedAt: Rule update time
        :type UpdatedAt: str
        :param _RuleName: Rule name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleName: str
        """
        self._RuleId = None
        self._RuleState = None
        self._Name = None
        self._Group = None
        self._Total = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._RuleName = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._Total = params.get("Total")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeGrafanaInstanceRequest(AbstractModel):
    """ResumeGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeGrafanaInstanceResponse(AbstractModel):
    """ResumeGrafanaInstance response structure.

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


class RunPrometheusInstanceRequest(AbstractModel):
    """RunPrometheusInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SubnetId: Subnet ID. Initialization is performed with the subnet used by the instance by default and can also be performed with the subnet passed in by this parameter.
        :type SubnetId: str
        """
        self._InstanceId = None
        self._SubnetId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunPrometheusInstanceResponse(AbstractModel):
    """RunPrometheusInstance response structure.

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


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg request structure.

    """

    def __init__(self):
        r"""
        :param _Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param _PolicyId: Message policy ID, which is configured on the custom message page.
        :type PolicyId: str
        :param _Msg: Custom message content that a user wants to send.
        :type Msg: str
        """
        self._Module = None
        self._PolicyId = None
        self._Msg = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        self._Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCustomAlarmMsgResponse(AbstractModel):
    """SendCustomAlarmMsg response structure.

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


class ServiceDiscoveryItem(AbstractModel):
    """Prometheus scrape configuration information

    """

    def __init__(self):
        r"""
        :param _Name: Scrape configuration name
        :type Name: str
        :param _Namespace: Namespace of the scrape configuration
        :type Namespace: str
        :param _Kind: Scrape configuration type: ServiceMonitor/PodMonitor
        :type Kind: str
        :param _NamespaceSelector: Namespace selection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type NamespaceSelector: str
        :param _Selector: Label selection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type Selector: str
        :param _Endpoints: `Endpoints` information (PodMonitor does not have this parameter)
        :type Endpoints: str
        :param _Yaml: Scrape configuration information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Yaml: str
        """
        self._Name = None
        self._Namespace = None
        self._Kind = None
        self._NamespaceSelector = None
        self._Selector = None
        self._Endpoints = None
        self._Yaml = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def NamespaceSelector(self):
        return self._NamespaceSelector

    @NamespaceSelector.setter
    def NamespaceSelector(self, NamespaceSelector):
        self._NamespaceSelector = NamespaceSelector

    @property
    def Selector(self):
        return self._Selector

    @Selector.setter
    def Selector(self, Selector):
        self._Selector = Selector

    @property
    def Endpoints(self):
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Kind = params.get("Kind")
        self._NamespaceSelector = params.get("NamespaceSelector")
        self._Selector = params.get("Selector")
        self._Endpoints = params.get("Endpoints")
        self._Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyRequest(AbstractModel):
    """SetDefaultAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param _PolicyId: Alarm policy ID
        :type PolicyId: str
        """
        self._Module = None
        self._PolicyId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyResponse(AbstractModel):
    """SetDefaultAlarmPolicy response structure.

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


class SyncPrometheusTempRequest(AbstractModel):
    """SyncPrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Instance ID
        :type TemplateId: str
        :param _Targets: Sync target
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self._TemplateId = None
        self._Targets = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTempResponse(AbstractModel):
    """SyncPrometheusTemp response structure.

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


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
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
        


class TagInstance(AbstractModel):
    """Instance tag information of the alarm policy

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Tag value
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Value: str
        :param _InstanceSum: Number of instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceSum: int
        :param _ServiceType: Service type, for example, CVM
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param _RegionId: Region ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RegionId: str
        :param _BindingStatus: Binding status. 2: bound; 1: binding
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BindingStatus: int
        :param _TagStatus: Tag status. 2: existent; 1: nonexistent
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagStatus: int
        """
        self._Key = None
        self._Value = None
        self._InstanceSum = None
        self._ServiceType = None
        self._RegionId = None
        self._BindingStatus = None
        self._TagStatus = None

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

    @property
    def InstanceSum(self):
        return self._InstanceSum

    @InstanceSum.setter
    def InstanceSum(self, InstanceSum):
        self._InstanceSum = InstanceSum

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def BindingStatus(self):
        return self._BindingStatus

    @BindingStatus.setter
    def BindingStatus(self, BindingStatus):
        self._BindingStatus = BindingStatus

    @property
    def TagStatus(self):
        return self._TagStatus

    @TagStatus.setter
    def TagStatus(self, TagStatus):
        self._TagStatus = TagStatus


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._InstanceSum = params.get("InstanceSum")
        self._ServiceType = params.get("ServiceType")
        self._RegionId = params.get("RegionId")
        self._BindingStatus = params.get("BindingStatus")
        self._TagStatus = params.get("TagStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Targets(AbstractModel):
    """Number of scrape targets

    """

    def __init__(self):
        r"""
        :param _Total: The total count
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Up: Number of online targets
Note: This field may return null, indicating that no valid values can be obtained.
        :type Up: int
        :param _Down: Number of offline targets
Note: This field may return null, indicating that no valid values can be obtained.
        :type Down: int
        :param _Unknown: Number of unknown status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unknown: int
        """
        self._Total = None
        self._Up = None
        self._Down = None
        self._Unknown = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Up(self):
        return self._Up

    @Up.setter
    def Up(self, Up):
        self._Up = Up

    @property
    def Down(self):
        return self._Down

    @Down.setter
    def Down(self, Down):
        self._Down = Down

    @property
    def Unknown(self):
        return self._Unknown

    @Unknown.setter
    def Unknown(self, Unknown):
        self._Unknown = Unknown


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Up = params.get("Up")
        self._Down = params.get("Down")
        self._Unknown = params.get("Unknown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
        :param _Step: Step name
        :type Step: str
        :param _LifeState: Lifecycle
`pending`
`running`
`success`
`failed`
        :type LifeState: str
        :param _StartAt: Step start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartAt: str
        :param _EndAt: Step end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndAt: str
        :param _FailedMsg: If `LifeState` is `failed`, this field displays the error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedMsg: str
        """
        self._Step = None
        self._LifeState = None
        self._StartAt = None
        self._EndAt = None
        self._FailedMsg = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def FailedMsg(self):
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._LifeState = params.get("LifeState")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """Template list

    """

    def __init__(self):
        r"""
        :param _Conditions: Metric alarm rules.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Conditions: list of Condition
        :param _EventConditions: Event alarm rules.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EventConditions: list of EventCondition
        :param _PolicyGroups: The associated alarm policy groups.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PolicyGroups: list of PolicyGroup
        :param _GroupID: Template-based policy group ID.
        :type GroupID: int
        :param _GroupName: Template-based policy group name.
        :type GroupName: str
        :param _InsertTime: Creation time.
        :type InsertTime: int
        :param _LastEditUin: UIN of the last modifier.
        :type LastEditUin: int
        :param _Remark: Remarks.
        :type Remark: str
        :param _UpdateTime: Update time.
        :type UpdateTime: int
        :param _ViewName: View.
        :type ViewName: str
        :param _IsUnionRule: Whether the logical relationship between rules is AND.
        :type IsUnionRule: int
        """
        self._Conditions = None
        self._EventConditions = None
        self._PolicyGroups = None
        self._GroupID = None
        self._GroupName = None
        self._InsertTime = None
        self._LastEditUin = None
        self._Remark = None
        self._UpdateTime = None
        self._ViewName = None
        self._IsUnionRule = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def EventConditions(self):
        return self._EventConditions

    @EventConditions.setter
    def EventConditions(self, EventConditions):
        self._EventConditions = EventConditions

    @property
    def PolicyGroups(self):
        return self._PolicyGroups

    @PolicyGroups.setter
    def PolicyGroups(self, PolicyGroups):
        self._PolicyGroups = PolicyGroups

    @property
    def GroupID(self):
        return self._GroupID

    @GroupID.setter
    def GroupID(self, GroupID):
        self._GroupID = GroupID

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def LastEditUin(self):
        return self._LastEditUin

    @LastEditUin.setter
    def LastEditUin(self, LastEditUin):
        self._LastEditUin = LastEditUin

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def IsUnionRule(self):
        return self._IsUnionRule

    @IsUnionRule.setter
    def IsUnionRule(self, IsUnionRule):
        self._IsUnionRule = IsUnionRule


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = Condition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self._EventConditions = []
            for item in params.get("EventConditions"):
                obj = EventCondition()
                obj._deserialize(item)
                self._EventConditions.append(obj)
        if params.get("PolicyGroups") is not None:
            self._PolicyGroups = []
            for item in params.get("PolicyGroups"):
                obj = PolicyGroup()
                obj._deserialize(item)
                self._PolicyGroups.append(obj)
        self._GroupID = params.get("GroupID")
        self._GroupName = params.get("GroupName")
        self._InsertTime = params.get("InsertTime")
        self._LastEditUin = params.get("LastEditUin")
        self._Remark = params.get("Remark")
        self._UpdateTime = params.get("UpdateTime")
        self._ViewName = params.get("ViewName")
        self._IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminatePrometheusInstancesRequest(AbstractModel):
    """TerminatePrometheusInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminatePrometheusInstancesResponse(AbstractModel):
    """TerminatePrometheusInstances response structure.

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


class Toleration(AbstractModel):
    """Kubernetes taint

    """

    def __init__(self):
        r"""
        :param _Key: Key of the taint to which the toleration is applied
        :type Key: str
        :param _Operator: The key-value relationship
        :type Operator: str
        :param _Effect: The taint effect to be matched
        :type Effect: str
        """
        self._Key = None
        self._Operator = None
        self._Effect = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class URLNotice(AbstractModel):
    """Alarm notification template – callback notification details

    """

    def __init__(self):
        r"""
        :param _URL: Callback URL, which can contain up to 256 characters
Note: this field may return null, indicating that no valid values can be obtained.
        :type URL: str
        :param _IsValid: Whether verification is passed. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsValid: int
        :param _ValidationCode: Verification code
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidationCode: str
        :param _StartTime: Start time of the notification in seconds, which is calculated from 00:00:00.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTime: int
        :param _EndTime: End time of the notification in seconds, which is calculated from 00:00:00.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _Weekday: Notification cycle. The values 1-7 indicate Monday to Sunday.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Weekday: list of int
        """
        self._URL = None
        self._IsValid = None
        self._ValidationCode = None
        self._StartTime = None
        self._EndTime = None
        self._Weekday = None

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def IsValid(self):
        return self._IsValid

    @IsValid.setter
    def IsValid(self, IsValid):
        self._IsValid = IsValid

    @property
    def ValidationCode(self):
        return self._ValidationCode

    @ValidationCode.setter
    def ValidationCode(self, ValidationCode):
        self._ValidationCode = ValidationCode

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
    def Weekday(self):
        return self._Weekday

    @Weekday.setter
    def Weekday(self, Weekday):
        self._Weekday = Weekday


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._IsValid = params.get("IsValid")
        self._ValidationCode = params.get("ValidationCode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Weekday = params.get("Weekday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.
        :type GroupId: int
        :param _PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.
        :type PolicyId: str
        :param _EbSubject: The alert configured for an event
        :type EbSubject: str
        :param _EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._PolicyId = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject response structure.

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


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject request structure.

    """

    def __init__(self):
        r"""
        :param _Module: The value is fixed to monitor.
        :type Module: str
        :param _GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.
        :type GroupId: int
        :param _UniqueId: List of unique IDs of the object instances to be deleted. `UniqueId` can be obtained from the output parameter `List` of the [DescribeBindingPolicyObjectList](https://intl.cloud.tencent.com/document/api/248/40570?from_cn_redirect=1) API
        :type UniqueId: list of str
        :param _InstanceGroupId: Instance group ID. The `UniqueId` parameter is invalid if object instances are deleted by instance group.
        :type InstanceGroupId: int
        :param _PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.
        :type PolicyId: str
        :param _EbSubject: The alert configured for an event
        :type EbSubject: str
        :param _EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self._Module = None
        self._GroupId = None
        self._UniqueId = None
        self._InstanceGroupId = None
        self._PolicyId = None
        self._EbSubject = None
        self._EbEventFlag = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UniqueId(self):
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def InstanceGroupId(self):
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def EbSubject(self):
        return self._EbSubject

    @EbSubject.setter
    def EbSubject(self, EbSubject):
        self._EbSubject = EbSubject

    @property
    def EbEventFlag(self):
        return self._EbEventFlag

    @EbEventFlag.setter
    def EbEventFlag(self, EbEventFlag):
        self._EbEventFlag = EbEventFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._GroupId = params.get("GroupId")
        self._UniqueId = params.get("UniqueId")
        self._InstanceGroupId = params.get("InstanceGroupId")
        self._PolicyId = params.get("PolicyId")
        self._EbSubject = params.get("EbSubject")
        self._EbEventFlag = params.get("EbEventFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject response structure.

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


class UnbindPrometheusManagedGrafanaRequest(AbstractModel):
    """UnbindPrometheusManagedGrafana request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _GrafanaId: Grafana instance ID
        :type GrafanaId: str
        """
        self._InstanceId = None
        self._GrafanaId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GrafanaId(self):
        return self._GrafanaId

    @GrafanaId.setter
    def GrafanaId(self, GrafanaId):
        self._GrafanaId = GrafanaId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPrometheusManagedGrafanaResponse(AbstractModel):
    """UnbindPrometheusManagedGrafana response structure.

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


class UninstallGrafanaDashboardRequest(AbstractModel):
    """UninstallGrafanaDashboard request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IntegrationCodes: Prometheus integration code, indicating to delete the corresponding dashboard. Valid values:
<li>spring_mvc</li>
<li>mysql</li>
<li>go</li>
<li>redis</li>
<li>jvm</li>
<li>pgsql</li>
<li>mongo</li>
<li>kafka</li>
<li>es</li>
<li>flink</li>
<li>blackbox</li>
<li>consule</li>
<li>memcached</li>
<li>zk</li>
<li>tps</li>
<li>istio</li>
<li>etcd</li>
        :type IntegrationCodes: list of str
        """
        self._InstanceId = None
        self._IntegrationCodes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationCodes(self):
        return self._IntegrationCodes

    @IntegrationCodes.setter
    def IntegrationCodes(self, IntegrationCodes):
        self._IntegrationCodes = IntegrationCodes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaDashboardResponse(AbstractModel):
    """UninstallGrafanaDashboard response structure.

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


class UninstallGrafanaPluginsRequest(AbstractModel):
    """UninstallGrafanaPlugins request structure.

    """

    def __init__(self):
        r"""
        :param _PluginIds: Array of plugin IDs, such as "PluginIds": [ "grafana-clock-panel" ]. The plugin ID can be obtained through the `DescribePluginOverviews` API.
        :type PluginIds: list of str
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefg”.
        :type InstanceId: str
        """
        self._PluginIds = None
        self._InstanceId = None

    @property
    def PluginIds(self):
        return self._PluginIds

    @PluginIds.setter
    def PluginIds(self, PluginIds):
        self._PluginIds = PluginIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._PluginIds = params.get("PluginIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaPluginsResponse(AbstractModel):
    """UninstallGrafanaPlugins response structure.

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


class UpdateAlertRuleRequest(AbstractModel):
    """UpdateAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Prometheus alerting rule ID
        :type RuleId: str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        :param _RuleName: Alerting rule name
        :type RuleName: str
        :param _Expr: Alerting rule expression
        :type Expr: str
        :param _Duration: Alerting rule duration
        :type Duration: str
        :param _Receivers: List of alerting rule recipient groups
        :type Receivers: list of str
        :param _Labels: List of alerting rule tags
        :type Labels: list of PrometheusRuleKV
        :param _Annotations: List of alerting rule annotations.

Alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively.
        :type Annotations: list of PrometheusRuleKV
        :param _Type: Alerting rule template category
        :type Type: str
        """
        self._RuleId = None
        self._InstanceId = None
        self._RuleState = None
        self._RuleName = None
        self._Expr = None
        self._Duration = None
        self._Receivers = None
        self._Labels = None
        self._Annotations = None
        self._Type = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Expr(self):
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        self._RuleName = params.get("RuleName")
        self._Expr = params.get("Expr")
        self._Duration = params.get("Duration")
        self._Receivers = params.get("Receivers")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleResponse(AbstractModel):
    """UpdateAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class UpdateAlertRuleStateRequest(AbstractModel):
    """UpdateAlertRuleState request structure.

    """

    def __init__(self):
        r"""
        :param _RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self._RuleIds = None
        self._InstanceId = None
        self._RuleState = None

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._InstanceId = params.get("InstanceId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleStateResponse(AbstractModel):
    """UpdateAlertRuleState response structure.

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


class UpdateDNSConfigRequest(AbstractModel):
    """UpdateDNSConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _NameServers: Array of DNS servers
        :type NameServers: list of str
        """
        self._InstanceId = None
        self._NameServers = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDNSConfigResponse(AbstractModel):
    """UpdateDNSConfig response structure.

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


class UpdateExporterIntegrationRequest(AbstractModel):
    """UpdateExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Kind: Type
        :type Kind: str
        :param _Content: Configuration content
        :type Content: str
        """
        self._InstanceId = None
        self._KubeType = None
        self._ClusterId = None
        self._Kind = None
        self._Content = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KubeType(self):
        return self._KubeType

    @KubeType.setter
    def KubeType(self, KubeType):
        self._KubeType = KubeType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KubeType = params.get("KubeType")
        self._ClusterId = params.get("ClusterId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateExporterIntegrationResponse(AbstractModel):
    """UpdateExporterIntegration response structure.

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


class UpdateGrafanaConfigRequest(AbstractModel):
    """UpdateGrafanaConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Config: JSON-encoded string
        :type Config: str
        """
        self._InstanceId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaConfigResponse(AbstractModel):
    """UpdateGrafanaConfig response structure.

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


class UpdateGrafanaEnvironmentsRequest(AbstractModel):
    """UpdateGrafanaEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _Envs: Environment variable string
        :type Envs: str
        """
        self._InstanceId = None
        self._Envs = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Envs(self):
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Envs = params.get("Envs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaEnvironmentsResponse(AbstractModel):
    """UpdateGrafanaEnvironments response structure.

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


class UpdateGrafanaIntegrationRequest(AbstractModel):
    """UpdateGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param _IntegrationId: Integration ID, such as “integration-abcd1234”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type IntegrationId: str
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _Kind: Integration type, such as “tencent-cloud-prometheus”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type Kind: str
        :param _Content: Integration content
        :type Content: str
        """
        self._IntegrationId = None
        self._InstanceId = None
        self._Kind = None
        self._Content = None

    @property
    def IntegrationId(self):
        return self._IntegrationId

    @IntegrationId.setter
    def IntegrationId(self, IntegrationId):
        self._IntegrationId = IntegrationId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._IntegrationId = params.get("IntegrationId")
        self._InstanceId = params.get("InstanceId")
        self._Kind = params.get("Kind")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaIntegrationResponse(AbstractModel):
    """UpdateGrafanaIntegration response structure.

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


class UpdateGrafanaNotificationChannelRequest(AbstractModel):
    """UpdateGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID, such as “nchannel-abcd1234”.
        :type ChannelId: str
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param _Receivers: Array of notification channel IDs
        :type Receivers: list of str
        :param _ExtraOrgIds: This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type ExtraOrgIds: list of str
        :param _OrganizationIds: Array of valid organization IDs
        :type OrganizationIds: list of str
        """
        self._ChannelId = None
        self._InstanceId = None
        self._ChannelName = None
        self._Receivers = None
        self._ExtraOrgIds = None
        self._OrganizationIds = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Receivers(self):
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def ExtraOrgIds(self):
        return self._ExtraOrgIds

    @ExtraOrgIds.setter
    def ExtraOrgIds(self, ExtraOrgIds):
        self._ExtraOrgIds = ExtraOrgIds

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._InstanceId = params.get("InstanceId")
        self._ChannelName = params.get("ChannelName")
        self._Receivers = params.get("Receivers")
        self._ExtraOrgIds = params.get("ExtraOrgIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaNotificationChannelResponse(AbstractModel):
    """UpdateGrafanaNotificationChannel response structure.

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


class UpdateGrafanaWhiteListRequest(AbstractModel):
    """UpdateGrafanaWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _Whitelist: Array of public IPs (such as “127.0.0.1”) in the allowlist, which can be viewed through the `DescribeGrafanaWhiteList` API.
        :type Whitelist: list of str
        """
        self._InstanceId = None
        self._Whitelist = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Whitelist(self):
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaWhiteListResponse(AbstractModel):
    """UpdateGrafanaWhiteList response structure.

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


class UpdatePrometheusAgentStatusRequest(AbstractModel):
    """UpdatePrometheusAgentStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param _AgentIds: List of agent IDs such as “agent-abcd1234”, which can be obtained on the **Agent Management** page in the console.
        :type AgentIds: list of str
        :param _Status: Status to update
<li> 1 = enabled </li>
<li> 2 = disabled </li>
        :type Status: int
        """
        self._InstanceId = None
        self._AgentIds = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentIds(self):
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        self._AgentIds = AgentIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentIds = params.get("AgentIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusAgentStatusResponse(AbstractModel):
    """UpdatePrometheusAgentStatus response structure.

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


class UpdatePrometheusScrapeJobRequest(AbstractModel):
    """UpdatePrometheusScrapeJob request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param _AgentId: Agent ID such as “agent-abcd1234”, which can be obtained on the **Agent Management** page in the console
        :type AgentId: str
        :param _JobId: Scrape task ID such as “job-abcd1234”. You can go to the **Agent Management** page and obtain the ID in the pop-up **Create Scrape Task** window.
        :type JobId: str
        :param _Config: Scrape task ID in the format of “job_name:xx”
        :type Config: str
        """
        self._InstanceId = None
        self._AgentId = None
        self._JobId = None
        self._Config = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentId(self):
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentId = params.get("AgentId")
        self._JobId = params.get("JobId")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusScrapeJobResponse(AbstractModel):
    """UpdatePrometheusScrapeJob response structure.

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


class UpdateRecordingRuleRequest(AbstractModel):
    """UpdateRecordingRule request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Recording rule name
        :type Name: str
        :param _Group: Recording rule group content, which is in YAML format and is Base64-encoded.
        :type Group: str
        :param _InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param _RuleId: Prometheus recording rule ID
        :type RuleId: str
        :param _RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self._Name = None
        self._Group = None
        self._InstanceId = None
        self._RuleId = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Group = params.get("Group")
        self._InstanceId = params.get("InstanceId")
        self._RuleId = params.get("RuleId")
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordingRuleResponse(AbstractModel):
    """UpdateRecordingRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class UpdateSSOAccountRequest(AbstractModel):
    """UpdateSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param _UserId: User account ID, such as “10000000”.
        :type UserId: str
        :param _Role: Permission
        :type Role: list of GrafanaAccountRole
        :param _Notes: Remarks
        :type Notes: str
        """
        self._InstanceId = None
        self._UserId = None
        self._Role = None
        self._Notes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Notes(self):
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserId = params.get("UserId")
        if params.get("Role") is not None:
            self._Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self._Role.append(obj)
        self._Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSSOAccountResponse(AbstractModel):
    """UpdateSSOAccount response structure.

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


class UpgradeGrafanaDashboardRequest(AbstractModel):
    """UpgradeGrafanaDashboard request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _IntegrationCodes: Prometheus integration code, indicating to upgrade to the corresponding dashboard. Valid values:
<li>spring_mvc</li>
<li>mysql</li>
<li>go</li>
<li>redis</li>
<li>jvm</li>
<li>pgsql</li>
<li>mongo</li>
<li>kafka</li>
<li>es</li>
<li>flink</li>
<li>blackbox</li>
<li>consule</li>
<li>memcached</li>
<li>zk</li>
<li>tps</li>
<li>istio</li>
<li>etcd</li>
        :type IntegrationCodes: list of str
        """
        self._InstanceId = None
        self._IntegrationCodes = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IntegrationCodes(self):
        return self._IntegrationCodes

    @IntegrationCodes.setter
    def IntegrationCodes(self, IntegrationCodes):
        self._IntegrationCodes = IntegrationCodes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaDashboardResponse(AbstractModel):
    """UpgradeGrafanaDashboard response structure.

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


class UpgradeGrafanaInstanceRequest(AbstractModel):
    """UpgradeGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param _Alias: Version alias, such as v7.4.2.
        :type Alias: str
        """
        self._InstanceId = None
        self._Alias = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaInstanceResponse(AbstractModel):
    """UpgradeGrafanaInstance response structure.

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


class UserNotice(AbstractModel):
    """Alarm notification template – user notification details

    """

    def __init__(self):
        r"""
        :param _ReceiverType: Recipient type. Valid values: USER (user), GROUP (user group)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReceiverType: str
        :param _StartTime: Notification start time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param _EndTime: Notification end time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _NoticeWay: Notification channel list. Valid values: `EMAIL` (email), `SMS` (SMS), `CALL` (phone), `WECHAT` (WeChat), `RTX` (WeCom)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NoticeWay: list of str
        :param _UserIds: User `uid` list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserIds: list of int
        :param _GroupIds: User group ID list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupIds: list of int
        :param _PhoneOrder: Phone polling list
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneOrder: list of int
        :param _PhoneCircleTimes: Number of phone pollings. Value range: 1–5
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleTimes: int
        :param _PhoneInnerInterval: Call interval in seconds within one polling. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneInnerInterval: int
        :param _PhoneCircleInterval: Polling interval in seconds. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleInterval: int
        :param _NeedPhoneArriveNotice: Whether receipt notification is required. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NeedPhoneArriveNotice: int
        :param _PhoneCallType: Dial type. `SYNC` (simultaneous dial), `CIRCLE` (polled dial). Default value: `CIRCLE`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PhoneCallType: str
        :param _Weekday: Notification cycle. The values 1-7 indicate Monday to Sunday.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Weekday: list of int
        """
        self._ReceiverType = None
        self._StartTime = None
        self._EndTime = None
        self._NoticeWay = None
        self._UserIds = None
        self._GroupIds = None
        self._PhoneOrder = None
        self._PhoneCircleTimes = None
        self._PhoneInnerInterval = None
        self._PhoneCircleInterval = None
        self._NeedPhoneArriveNotice = None
        self._PhoneCallType = None
        self._Weekday = None

    @property
    def ReceiverType(self):
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

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
    def NoticeWay(self):
        return self._NoticeWay

    @NoticeWay.setter
    def NoticeWay(self, NoticeWay):
        self._NoticeWay = NoticeWay

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def PhoneOrder(self):
        return self._PhoneOrder

    @PhoneOrder.setter
    def PhoneOrder(self, PhoneOrder):
        self._PhoneOrder = PhoneOrder

    @property
    def PhoneCircleTimes(self):
        return self._PhoneCircleTimes

    @PhoneCircleTimes.setter
    def PhoneCircleTimes(self, PhoneCircleTimes):
        self._PhoneCircleTimes = PhoneCircleTimes

    @property
    def PhoneInnerInterval(self):
        return self._PhoneInnerInterval

    @PhoneInnerInterval.setter
    def PhoneInnerInterval(self, PhoneInnerInterval):
        self._PhoneInnerInterval = PhoneInnerInterval

    @property
    def PhoneCircleInterval(self):
        return self._PhoneCircleInterval

    @PhoneCircleInterval.setter
    def PhoneCircleInterval(self, PhoneCircleInterval):
        self._PhoneCircleInterval = PhoneCircleInterval

    @property
    def NeedPhoneArriveNotice(self):
        return self._NeedPhoneArriveNotice

    @NeedPhoneArriveNotice.setter
    def NeedPhoneArriveNotice(self, NeedPhoneArriveNotice):
        self._NeedPhoneArriveNotice = NeedPhoneArriveNotice

    @property
    def PhoneCallType(self):
        return self._PhoneCallType

    @PhoneCallType.setter
    def PhoneCallType(self, PhoneCallType):
        self._PhoneCallType = PhoneCallType

    @property
    def Weekday(self):
        return self._Weekday

    @Weekday.setter
    def Weekday(self, Weekday):
        self._Weekday = Weekday


    def _deserialize(self, params):
        self._ReceiverType = params.get("ReceiverType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NoticeWay = params.get("NoticeWay")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._PhoneOrder = params.get("PhoneOrder")
        self._PhoneCircleTimes = params.get("PhoneCircleTimes")
        self._PhoneInnerInterval = params.get("PhoneInnerInterval")
        self._PhoneCircleInterval = params.get("PhoneCircleInterval")
        self._NeedPhoneArriveNotice = params.get("NeedPhoneArriveNotice")
        self._PhoneCallType = params.get("PhoneCallType")
        self._Weekday = params.get("Weekday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        