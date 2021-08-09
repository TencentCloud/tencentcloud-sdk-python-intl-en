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
        """
        :param EventName: Event name\n        :type EventName: str\n        :param Description: Event display name\n        :type Description: str\n        :param Namespace: Alarm policy type\n        :type Namespace: str\n        """
        self.EventName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistory(AbstractModel):
    """Alarm record data

    """

    def __init__(self):
        """
        :param AlarmId: Alarm record ID\n        :type AlarmId: str\n        :param MonitorType: Monitor type\n        :type MonitorType: str\n        :param Namespace: Policy type\n        :type Namespace: str\n        :param AlarmObject: Alarm object\n        :type AlarmObject: str\n        :param Content: Alarm content\n        :type Content: str\n        :param FirstOccurTime: Timestamp of the first occurrence\n        :type FirstOccurTime: int\n        :param LastOccurTime: Timestamp of the last occurrence\n        :type LastOccurTime: int\n        :param AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data)\n        :type AlarmStatus: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param PolicyName: Policy name\n        :type PolicyName: str\n        :param VPC: VPC of alarm object for basic product alarm\n        :type VPC: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param ProjectName: Project name\n        :type ProjectName: str\n        :param InstanceGroup: Instance group of alarm object\n        :type InstanceGroup: list of InstanceGroups\n        :param ReceiverUids: Recipient list\n        :type ReceiverUids: list of int\n        :param ReceiverGroups: Recipient group list\n        :type ReceiverGroups: list of int\n        :param NoticeWays: Alarm channel list. Valid values: SMS (SMS), EMAIL (email), CALL (phone), WECHAT (WeChat)\n        :type NoticeWays: list of str\n        :param OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy\n        :type OriginId: str\n        :param AlarmType: Alarm type\n        :type AlarmType: str\n        :param EventId: Event ID\n        :type EventId: int\n        :param Region: Region\n        :type Region: str\n        :param PolicyExists: Whether the policy exists. Valid values: 0 (no), 1 (yes)\n        :type PolicyExists: int\n        :param MetricsInfo: Metric information
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type MetricsInfo: list of AlarmHistoryMetric\n        :param Dimensions: Dimension information of an instance that triggered alarms.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Dimensions: str\n        """
        self.AlarmId = None
        self.MonitorType = None
        self.Namespace = None
        self.AlarmObject = None
        self.Content = None
        self.FirstOccurTime = None
        self.LastOccurTime = None
        self.AlarmStatus = None
        self.PolicyId = None
        self.PolicyName = None
        self.VPC = None
        self.ProjectId = None
        self.ProjectName = None
        self.InstanceGroup = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.NoticeWays = None
        self.OriginId = None
        self.AlarmType = None
        self.EventId = None
        self.Region = None
        self.PolicyExists = None
        self.MetricsInfo = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        self.AlarmObject = params.get("AlarmObject")
        self.Content = params.get("Content")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.LastOccurTime = params.get("LastOccurTime")
        self.AlarmStatus = params.get("AlarmStatus")
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.VPC = params.get("VPC")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroups()
                obj._deserialize(item)
                self.InstanceGroup.append(obj)
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.NoticeWays = params.get("NoticeWays")
        self.OriginId = params.get("OriginId")
        self.AlarmType = params.get("AlarmType")
        self.EventId = params.get("EventId")
        self.Region = params.get("Region")
        self.PolicyExists = params.get("PolicyExists")
        if params.get("MetricsInfo") is not None:
            self.MetricsInfo = []
            for item in params.get("MetricsInfo"):
                obj = AlarmHistoryMetric()
                obj._deserialize(item)
                self.MetricsInfo.append(obj)
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHistoryMetric(AbstractModel):
    """Metric information of alarm records

    """

    def __init__(self):
        """
        :param QceNamespace: Namespace used to query data by Tencent Cloud service monitoring type\n        :type QceNamespace: str\n        :param MetricName: Metric name\n        :type MetricName: str\n        :param Period: Statistical period\n        :type Period: int\n        :param Value: Value triggering alarm\n        :type Value: str\n        :param Description: Metric display name\n        :type Description: str\n        """
        self.QceNamespace = None
        self.MetricName = None
        self.Period = None
        self.Value = None
        self.Description = None


    def _deserialize(self, params):
        self.QceNamespace = params.get("QceNamespace")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.Value = params.get("Value")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """Alarm notification template details

    """

    def __init__(self):
        """
        :param Id: Alarm notification template ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Id: str\n        :param Name: Alarm notification template name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Name: str\n        :param UpdatedAt: Last modified time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UpdatedAt: str\n        :param UpdatedBy: Last modified by
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UpdatedBy: str\n        :param NoticeType: Alarm notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NoticeType: str\n        :param UserNotices: User notification list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserNotices: list of UserNotice\n        :param URLNotices: Callback notification list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type URLNotices: list of URLNotice\n        :param IsPreset: Whether it is the system default notification template. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsPreset: int\n        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NoticeLanguage: str\n        :param PolicyIds: List of IDs of the alarm policies bound to alarm notification template
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PolicyIds: list of str\n        """
        self.Id = None
        self.Name = None
        self.UpdatedAt = None
        self.UpdatedBy = None
        self.NoticeType = None
        self.UserNotices = None
        self.URLNotices = None
        self.IsPreset = None
        self.NoticeLanguage = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.UpdatedAt = params.get("UpdatedAt")
        self.UpdatedBy = params.get("UpdatedBy")
        self.NoticeType = params.get("NoticeType")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        self.IsPreset = params.get("IsPreset")
        self.NoticeLanguage = params.get("NoticeLanguage")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicy(AbstractModel):
    """Alarm policy details

    """

    def __init__(self):
        """
        :param PolicyId: Alarm policy ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PolicyId: str\n        :param PolicyName: Alarm policy name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PolicyName: str\n        :param Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Remark: str\n        :param MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MonitorType: str\n        :param Enable: Status. Valid values: 0 (disabled), 1 (enabled)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Enable: int\n        :param UseSum: Number of instances bound to policy group
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UseSum: int\n        :param ProjectId: Project ID. Valid values: -1 (no project), 0 (default project)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: int\n        :param ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectName: str\n        :param Namespace: Alarm policy type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Namespace: str\n        :param ConditionTemplateId: Trigger condition template ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConditionTemplateId: str\n        :param Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`\n        :param EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`\n        :param NoticeIds: Notification rule ID list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NoticeIds: list of str\n        :param Notices: Notification rule list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Notices: list of AlarmNotice\n        :param TriggerTasks: Triggered task list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TriggerTasks: list of AlarmPolicyTriggerTask\n        :param ConditionsTemp: Template policy group
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.ConditionsTemp`\n        :param LastEditUin: `Uin` of the last modifying user
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LastEditUin: str\n        :param UpdateTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UpdateTime: int\n        :param InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InsertTime: int\n        :param Region: Region
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Region: list of str\n        :param NamespaceShowName: Namespace display name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NamespaceShowName: str\n        :param IsDefault: Whether it is the default policy. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsDefault: int\n        :param CanSetDefault: Whether the default policy can be set. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CanSetDefault: int\n        :param InstanceGroupId: Instance group ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceGroupId: int\n        :param InstanceSum: Total number of instances in instance group
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceSum: int\n        :param InstanceGroupName: Instance group name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceGroupName: str\n        :param RuleType: Trigger condition type. Valid values: STATIC (static threshold), DYNAMIC (dynamic)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RuleType: str\n        :param OriginId: Policy ID for instance/instance group binding and unbinding APIs (BindingPolicyObject, UnBindingAllPolicyObject, UnBindingPolicyObject)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginId: str\n        :param TagInstances: Tag
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type TagInstances: list of TagInstance\n        """
        self.PolicyId = None
        self.PolicyName = None
        self.Remark = None
        self.MonitorType = None
        self.Enable = None
        self.UseSum = None
        self.ProjectId = None
        self.ProjectName = None
        self.Namespace = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.NoticeIds = None
        self.Notices = None
        self.TriggerTasks = None
        self.ConditionsTemp = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.Region = None
        self.NamespaceShowName = None
        self.IsDefault = None
        self.CanSetDefault = None
        self.InstanceGroupId = None
        self.InstanceSum = None
        self.InstanceGroupName = None
        self.RuleType = None
        self.OriginId = None
        self.TagInstances = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Remark = params.get("Remark")
        self.MonitorType = params.get("MonitorType")
        self.Enable = params.get("Enable")
        self.UseSum = params.get("UseSum")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Namespace = params.get("Namespace")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        self.NoticeIds = params.get("NoticeIds")
        if params.get("Notices") is not None:
            self.Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.Notices.append(obj)
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = ConditionsTemp()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.Region = params.get("Region")
        self.NamespaceShowName = params.get("NamespaceShowName")
        self.IsDefault = params.get("IsDefault")
        self.CanSetDefault = params.get("CanSetDefault")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.InstanceSum = params.get("InstanceSum")
        self.InstanceGroupName = params.get("InstanceGroupName")
        self.RuleType = params.get("RuleType")
        self.OriginId = params.get("OriginId")
        if params.get("TagInstances") is not None:
            self.TagInstances = []
            for item in params.get("TagInstances"):
                obj = TagInstance()
                obj._deserialize(item)
                self.TagInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyCondition(AbstractModel):
    """Metric trigger condition of alarm policy

    """

    def __init__(self):
        """
        :param IsUnionRule: Metric trigger condition operator. Valid values: 0 (OR), 1 (AND)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsUnionRule: int\n        :param Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Rules: list of AlarmPolicyRule\n        """
        self.IsUnionRule = None
        self.Rules = None


    def _deserialize(self, params):
        self.IsUnionRule = params.get("IsUnionRule")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyEventCondition(AbstractModel):
    """Event trigger condition of alarm policy

    """

    def __init__(self):
        """
        :param Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Rules: list of AlarmPolicyRule\n        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = AlarmPolicyRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyFilter(AbstractModel):
    """Filter condition of alarm policy

    """

    def __init__(self):
        """
        :param Type: Filter condition type. Valid values: DIMENSION (uses dimensions for filtering)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Type: str\n        :param Dimensions: JSON string generated by serializing the `AlarmPolicyDimension` two-dimensional array. The one-dimensional arrays are in OR relationship, and the elements in a one-dimensional array are in AND relationship
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Dimensions: str\n        """
        self.Type = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyRule(AbstractModel):
    """Trigger condition of alarm policy

    """

    def __init__(self):
        """
        :param MetricName: Metric name or event name. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1) and the supported events via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type MetricName: str\n        :param Period: Statistical period in seconds. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Period: int\n        :param Operator: Operator
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
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Operator: str\n        :param Value: Threshold. The valid value range can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Value: str\n        :param ContinuePeriod: Number of periods. `1`: continue for one period; `2`: continue for two periods; and so on. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ContinuePeriod: int\n        :param NoticeFrequency: Alarm interval in seconds. Valid values: 0 (do not repeat), 300 (alarm once every 5 minutes), 600 (alarm once every 10 minutes), 900 (alarm once every 15 minutes), 1800 (alarm once every 30 minutes), 3600 (alarm once every hour), 7200 (alarm once every 2 hours), 10800 (alarm once every 3 hours), 21600 (alarm once every 6 hours),  43200 (alarm once every 12 hours), 86400 (alarm once every day)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NoticeFrequency: int\n        :param IsPowerNotice: Whether the alarm frequency increases exponentially. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsPowerNotice: int\n        :param Filter: Filter condition for one single trigger rule
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`\n        :param Description: Metric display name, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param Unit: Unit, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Unit: str\n        :param RuleType: Trigger condition type. `STATIC`: static threshold; `dynamic`: dynamic threshold. If you do not specify this parameter when creating or editing a policy, `STATIC` is used by default.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type RuleType: str\n        """
        self.MetricName = None
        self.Period = None
        self.Operator = None
        self.Value = None
        self.ContinuePeriod = None
        self.NoticeFrequency = None
        self.IsPowerNotice = None
        self.Filter = None
        self.Description = None
        self.Unit = None
        self.RuleType = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.NoticeFrequency = params.get("NoticeFrequency")
        self.IsPowerNotice = params.get("IsPowerNotice")
        if params.get("Filter") is not None:
            self.Filter = AlarmPolicyFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Description = params.get("Description")
        self.Unit = params.get("Unit")
        self.RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmPolicyTriggerTask(AbstractModel):
    """Task triggered by alarm policy

    """

    def __init__(self):
        """
        :param Type: Triggered task type. Valid value: AS (auto scaling)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Type: str\n        :param TaskConfig: Configuration information in JSON format, such as {"Key1":"Value1","Key2":"Value2"}
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskConfig: str\n        """
        self.Type = None
        self.TaskConfig = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TaskConfig = params.get("TaskConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectDimension(AbstractModel):
    """Dimensions of instances bound to a policy

    """

    def __init__(self):
        """
        :param Region: Region name.\n        :type Region: str\n        :param RegionId: Region ID.\n        :type RegionId: int\n        :param Dimensions: Instance dimension information in the following format:
{"unInstanceId":"ins-00jvv9mo"}. The dimension information varies by Tencent Cloud services. For more information, please see:
[Dimension List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)\n        :type Dimensions: str\n        :param EventDimensions: Event dimensions.\n        :type EventDimensions: str\n        """
        self.Region = None
        self.RegionId = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject request structure.

    """

    def __init__(self):
        """
        :param GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., 0, can be passed in.\n        :type GroupId: int\n        :param Module: Required. The value is fixed to monitor.\n        :type Module: str\n        :param InstanceGroupId: Instance group ID.\n        :type InstanceGroupId: int\n        :param Dimensions: Dimensions of an object to be bound.\n        :type Dimensions: list of BindingPolicyObjectDimension\n        :param PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.\n        :type PolicyId: str\n        """
        self.GroupId = None
        self.Module = None
        self.InstanceGroupId = None
        self.Dimensions = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        self.InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CommonNamespace(AbstractModel):
    """Unified namespace information

    """

    def __init__(self):
        """
        :param Id: Namespace ID\n        :type Id: str\n        :param Name: Namespace name\n        :type Name: str\n        :param Value: Namespace value\n        :type Value: str\n        :param ProductName: Product name\n        :type ProductName: str\n        :param Config: Configuration information\n        :type Config: str\n        :param AvailableRegions: List of supported regions\n        :type AvailableRegions: list of str\n        :param SortId: Sort ID\n        :type SortId: int\n        :param DashboardId: Unique ID in Dashboard\n        :type DashboardId: str\n        """
        self.Id = None
        self.Name = None
        self.Value = None
        self.ProductName = None
        self.Config = None
        self.AvailableRegions = None
        self.SortId = None
        self.DashboardId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.ProductName = params.get("ProductName")
        self.Config = params.get("Config")
        self.AvailableRegions = params.get("AvailableRegions")
        self.SortId = params.get("SortId")
        self.DashboardId = params.get("DashboardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConditionsTemp(AbstractModel):
    """Alarm condition template

    """

    def __init__(self):
        """
        :param TemplateName: Template name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TemplateName: str\n        :param Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`\n        :param EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`\n        """
        self.TemplateName = None
        self.Condition = None
        self.EventCondition = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeRequest(AbstractModel):
    """CreateAlarmNotice request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param Name: Notification template name, which can contain up to 60 characters\n        :type Name: str\n        :param NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)\n        :type NoticeType: str\n        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)\n        :type NoticeLanguage: str\n        :param UserNotices: User notifications (up to 5)\n        :type UserNotices: list of UserNotice\n        :param URLNotices: Callback notifications (up to 3)\n        :type URLNotices: list of URLNotice\n        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.UserNotices = None
        self.URLNotices = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Name = params.get("Name")
        self.NoticeType = params.get("NoticeType")
        self.NoticeLanguage = params.get("NoticeLanguage")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice response structure.

    """

    def __init__(self):
        """
        :param NoticeId: Alarm notification template ID\n        :type NoticeId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.NoticeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.RequestId = params.get("RequestId")


class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy request structure.

    """

    def __init__(self):
        """
        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param PolicyName: Policy name, which can contain up to 20 characters\n        :type PolicyName: str\n        :param MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)\n        :type MonitorType: str\n        :param Namespace: Type of alarm policy, which can be obtained via [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1). An example value is `cvm_device`.\n        :type Namespace: str\n        :param Remark: Remarks with up to 100 letters, digits, underscores, and hyphens\n        :type Remark: str\n        :param Enable: Whether to enable. Valid values: 0 (no), 1 (yes). Default value: 1. This parameter can be left empty\n        :type Enable: int\n        :param ProjectId: Project ID. For products with different projects, a value other than `-1` must be passed in. `-1`: no project; `0`: default project. If no value is passed in, `-1` will be used. The supported project IDs can be viewed on the [**Account Center** > **Project Management**](https://console.cloud.tencent.com/project) page of the console.\n        :type ProjectId: int\n        :param ConditionTemplateId: ID of trigger condition template. This parameter can be left empty.\n        :type ConditionTemplateId: int\n        :param Condition: Metric trigger condition. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).\n        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`\n        :param EventCondition: Event trigger condition. The supported events can be queried via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).\n        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`\n        :param NoticeIds: List of notification rule IDs, which can be obtained via [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1)\n        :type NoticeIds: list of str\n        :param TriggerTasks: Triggered task list\n        :type TriggerTasks: list of AlarmPolicyTriggerTask\n        :param Filter: Global filter.\n        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`\n        :param GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.\n        :type GroupBy: list of str\n        """
        self.Module = None
        self.PolicyName = None
        self.MonitorType = None
        self.Namespace = None
        self.Remark = None
        self.Enable = None
        self.ProjectId = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.NoticeIds = None
        self.TriggerTasks = None
        self.Filter = None
        self.GroupBy = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyName = params.get("PolicyName")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        self.Remark = params.get("Remark")
        self.Enable = params.get("Enable")
        self.ProjectId = params.get("ProjectId")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        self.NoticeIds = params.get("NoticeIds")
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        if params.get("Filter") is not None:
            self.Filter = AlarmPolicyFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmPolicyResponse(AbstractModel):
    """CreateAlarmPolicy response structure.

    """

    def __init__(self):
        """
        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy\n        :type OriginId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PolicyId = None
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """Alarm threshold condition passed in when a policy is created.

    """

    def __init__(self):
        """
        :param MetricId: Metric ID.\n        :type MetricId: int\n        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.\n        :type AlarmNotifyPeriod: int\n        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. This parameter is optional if a default comparative type is configured for the metric.\n        :type CalcType: int\n        :param CalcValue: Comparative value. This parameter is optional if the metric has no requirement.\n        :type CalcValue: float\n        :param CalcPeriod: Data aggregation period in seconds. This parameter is optional if the metric has a default value.\n        :type CalcPeriod: int\n        :param ContinuePeriod: Number of consecutive periods after which an alarm will be triggered.\n        :type ContinuePeriod: int\n        :param RuleId: If a metric is created based on a template, the RuleId of the metric in the template must be passed in.\n        :type RuleId: int\n        """
        self.MetricId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.CalcPeriod = None
        self.ContinuePeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.MetricId = params.get("MetricId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.CalcPeriod = params.get("CalcPeriod")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupEventCondition(AbstractModel):
    """Event alarm condition passed in when a policy is created.

    """

    def __init__(self):
        """
        :param EventId: Alarm event ID.\n        :type EventId: int\n        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.\n        :type AlarmNotifyPeriod: int\n        :param RuleId: If a metric is created based on a template, the RuleId of the metric in the template must be passed in.\n        :type RuleId: int\n        """
        self.EventId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup request structure.

    """

    def __init__(self):
        """
        :param GroupName: Policy group name.\n        :type GroupName: str\n        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param ViewName: Name of the view to which the policy group belongs. If the policy group is created based on a template, this parameter is optional.\n        :type ViewName: str\n        :param ProjectId: ID of the project to which the policy group belongs, which will be used for authentication.\n        :type ProjectId: int\n        :param ConditionTempGroupId: ID of a template-based policy group. This parameter is required only when the policy group is created based on a template.\n        :type ConditionTempGroupId: int\n        :param IsShielded: Whether the policy group is shielded. The value 0 indicates that the policy group is not shielded. The value 1 indicates that the policy group is shielded. The default value is 0.\n        :type IsShielded: int\n        :param Remark: Remarks of the policy group.\n        :type Remark: str\n        :param InsertTime: Insertion time in the format of Unix timestamp. If this parameter is not configured, the backend processing time is used.\n        :type InsertTime: int\n        :param Conditions: Alarm threshold rules in the policy group.\n        :type Conditions: list of CreatePolicyGroupCondition\n        :param EventConditions: Event alarm rules in the policy group.\n        :type EventConditions: list of CreatePolicyGroupEventCondition\n        :param BackEndCall: Whether it is a backend call. If the value is 1, rules from the policy template will be used to fill in the `Conditions` and `EventConditions` fields.\n        :type BackEndCall: int\n        :param IsUnionRule: The 'AND' and 'OR' rules for alarm metrics. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met.\n        :type IsUnionRule: int\n        """
        self.GroupName = None
        self.Module = None
        self.ViewName = None
        self.ProjectId = None
        self.ConditionTempGroupId = None
        self.IsShielded = None
        self.Remark = None
        self.InsertTime = None
        self.Conditions = None
        self.EventConditions = None
        self.BackEndCall = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Module = params.get("Module")
        self.ViewName = params.get("ViewName")
        self.ProjectId = params.get("ProjectId")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.IsShielded = params.get("IsShielded")
        self.Remark = params.get("Remark")
        self.InsertTime = params.get("InsertTime")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = CreatePolicyGroupCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = CreatePolicyGroupEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        self.BackEndCall = params.get("BackEndCall")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup response structure.

    """

    def __init__(self):
        """
        :param GroupId: ID of the created policy group.\n        :type GroupId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        """
        :param Dimensions: Combination of instance object dimensions\n        :type Dimensions: list of Dimension\n        :param Timestamps: The array of timestamps indicating at which points in time there is data. Missing timestamps have no data points (i.e., missed)\n        :type Timestamps: list of float\n        :param Values: The array of monitoring values, which is in one-to-one correspondence to Timestamps\n        :type Values: list of float\n        """
        self.Dimensions = None
        self.Timestamps = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.Timestamps = params.get("Timestamps")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesRequest(AbstractModel):
    """DeleteAlarmNotices request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param NoticeIds: Alarm notification template ID list\n        :type NoticeIds: list of str\n        """
        self.Module = None
        self.NoticeIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.NoticeIds = params.get("NoticeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticesResponse(AbstractModel):
    """DeleteAlarmNotices response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        :param PolicyIds: Alarm policy ID list\n        :type PolicyIds: list of str\n        """
        self.Module = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmPolicyResponse(AbstractModel):
    """DeleteAlarmPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID.\n        :type GroupId: list of int\n        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccidentEventListAlarms(AbstractModel):
    """Output parameter type of the DescribeAccidentEventList API

    """

    def __init__(self):
        """
        :param BusinessTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.\n        :type BusinessTypeDesc: str\n        :param AccidentTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.\n        :type AccidentTypeDesc: str\n        :param BusinessID: ID of the event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.
Note: This field may return null, indicating that no valid value was found.\n        :type BusinessID: int\n        :param EventStatus: Event status ID. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.
Note: This field may return null, indicating that no valid value was found.\n        :type EventStatus: int\n        :param AffectResource: Affected object.
Note: This field may return null, indicating that no valid value was found.\n        :type AffectResource: str\n        :param Region: Region where the event occurs.
Note: This field may return null, indicating that no valid value was found.\n        :type Region: str\n        :param OccurTime: Time when the event occurs.
Note: This field may return null, indicating that no valid value was found.\n        :type OccurTime: str\n        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.\n        :type UpdateTime: str\n        """
        self.BusinessTypeDesc = None
        self.AccidentTypeDesc = None
        self.BusinessID = None
        self.EventStatus = None
        self.AffectResource = None
        self.Region = None
        self.OccurTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.BusinessTypeDesc = params.get("BusinessTypeDesc")
        self.AccidentTypeDesc = params.get("AccidentTypeDesc")
        self.BusinessID = params.get("BusinessID")
        self.EventStatus = params.get("EventStatus")
        self.AffectResource = params.get("AffectResource")
        self.Region = params.get("Region")
        self.OccurTime = params.get("OccurTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList request structure.

    """

    def __init__(self):
        """
        :param Module: API component name. The value for the current API is monitor.\n        :type Module: str\n        :param StartTime: Start time, which is the timestamp one day prior by default.\n        :type StartTime: int\n        :param EndTime: End time, which is the current timestamp by default.\n        :type EndTime: int\n        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.\n        :type Limit: int\n        :param Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.\n        :type Offset: int\n        :param UpdateTimeOrder: Sorting rule by UpdateTime. Valid values: asc and desc.\n        :type UpdateTimeOrder: str\n        :param OccurTimeOrder: Sorting rule by OccurTime. Valid values: asc or desc. Sorting by UpdateTimeOrder takes priority.\n        :type OccurTimeOrder: str\n        :param AccidentType: Filter by event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.\n        :type AccidentType: list of int\n        :param AccidentEvent: Filter by event. The value 1 indicates CVM storage issues. The value 2 indicates CVM network connection issues. The value 3 indicates that the CVM has an exception. The value 202 indicates that an ISP network jitter occurs.\n        :type AccidentEvent: list of int\n        :param AccidentStatus: Filter by event status. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.\n        :type AccidentStatus: list of int\n        :param AccidentRegion: Filter by region where the event occurs. The value gz indicates Guangzhou. The value sh indicates Shanghai.\n        :type AccidentRegion: list of str\n        :param AffectResource: Filter by affected resource, such as ins-19a06bka.\n        :type AffectResource: str\n        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.UpdateTimeOrder = None
        self.OccurTimeOrder = None
        self.AccidentType = None
        self.AccidentEvent = None
        self.AccidentStatus = None
        self.AccidentRegion = None
        self.AffectResource = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.AccidentType = params.get("AccidentType")
        self.AccidentEvent = params.get("AccidentEvent")
        self.AccidentStatus = params.get("AccidentStatus")
        self.AccidentRegion = params.get("AccidentRegion")
        self.AffectResource = params.get("AffectResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList response structure.

    """

    def __init__(self):
        """
        :param Alarms: Platform event list.
Note: This field may return null, indicating that no valid value was found.\n        :type Alarms: list of DescribeAccidentEventListAlarms\n        :param Total: Total number of platform events.
Note: This field may return null, indicating that no valid value was found.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeAccidentEventListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAlarmEventsRequest(AbstractModel):
    """DescribeAlarmEvents request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        :param Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API\n        :type Namespace: str\n        :param MonitorType: Monitoring type, such as `MT_QCE`, which is set to default.\n        :type MonitorType: str\n        """
        self.Module = None
        self.Namespace = None
        self.MonitorType = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Namespace = params.get("Namespace")
        self.MonitorType = params.get("MonitorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmEventsResponse(AbstractModel):
    """DescribeAlarmEvents response structure.

    """

    def __init__(self):
        """
        :param Events: Alarm event list\n        :type Events: list of AlarmEvent\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = AlarmEvent()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmHistoriesRequest(AbstractModel):
    """DescribeAlarmHistories request structure.

    """

    def __init__(self):
        """
        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param PageNumber: Page number starting from 1. Default value: 1\n        :type PageNumber: int\n        :param PageSize: Number of entries per page. Value range: 1–100. Default value: 20\n        :type PageSize: int\n        :param Order: Sort by the first occurrence time in descending order by default. Valid values: ASC (ascending), DESC (descending)\n        :type Order: str\n        :param StartTime: Start time, which is the timestamp one day ago by default and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is later than the `StartTime`.\n        :type StartTime: int\n        :param EndTime: End time, which is the current timestamp and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is earlier than the `EndTime`.\n        :type EndTime: int\n        :param MonitorTypes: Filter by monitoring type. Valid value: `MT_QCE` (Tencent Cloud service monitoring). If this parameter is left empty, all types will be queried by default.\n        :type MonitorTypes: list of str\n        :param AlarmObject: Filter by alarm object. Fuzzy search with string is supported\n        :type AlarmObject: str\n        :param AlarmStatus: Filter by alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data). If this parameter is left empty, all will be queried by default\n        :type AlarmStatus: list of str\n        :param ProjectIds: Filter by project ID. Valid values: `-1` (no project), `0` (default project)
You can query [Project Management](https://console.cloud.tencent.com/project) on this page.\n        :type ProjectIds: list of int\n        :param InstanceGroupIds: Filter by instance group ID\n        :type InstanceGroupIds: list of int\n        :param Namespaces: Filter by policy type. Monitoring type and policy type are first-level and second-level filters respectively and both need to be passed in. For example, `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`
This parameter can be queried with the API [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1).\n        :type Namespaces: list of MonitorTypeNamespace\n        :param MetricNames: Filter by metric name\n        :type MetricNames: list of str\n        :param PolicyName: Fuzzy search by policy name\n        :type PolicyName: str\n        :param Content: Fuzzy search by alarm content\n        :type Content: str\n        :param ReceiverUids: Search by recipient. You can get the user list with the API [ListUsers](https://intl.cloud.tencent.com/document/product/598/34587?from_cn_redirect=1) in “Cloud Access Management” or query the sub-user information with the API [GetUser](https://intl.cloud.tencent.com/document/product/598/34590?from_cn_redirect=1). The `Uid` field in the returned result should be entered here.\n        :type ReceiverUids: list of int\n        :param ReceiverGroups: Search by recipient group. You can get the user group list with the API [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) in “Cloud Access Management” or query the user group list where a sub-user is in with the API [ListGroupsForUser](https://intl.cloud.tencent.com/document/product/598/34588?from_cn_redirect=1). The `GroupId` field in the returned result should be entered here.\n        :type ReceiverGroups: list of int\n        :param PolicyIds: Search by alarm policy ID list\n        :type PolicyIds: list of str\n        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.Order = None
        self.StartTime = None
        self.EndTime = None
        self.MonitorTypes = None
        self.AlarmObject = None
        self.AlarmStatus = None
        self.ProjectIds = None
        self.InstanceGroupIds = None
        self.Namespaces = None
        self.MetricNames = None
        self.PolicyName = None
        self.Content = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MonitorTypes = params.get("MonitorTypes")
        self.AlarmObject = params.get("AlarmObject")
        self.AlarmStatus = params.get("AlarmStatus")
        self.ProjectIds = params.get("ProjectIds")
        self.InstanceGroupIds = params.get("InstanceGroupIds")
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = MonitorTypeNamespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.MetricNames = params.get("MetricNames")
        self.PolicyName = params.get("PolicyName")
        self.Content = params.get("Content")
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmHistoriesResponse(AbstractModel):
    """DescribeAlarmHistories response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number\n        :type TotalCount: int\n        :param Histories: Alarm record list\n        :type Histories: list of AlarmHistory\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Histories = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Histories") is not None:
            self.Histories = []
            for item in params.get("Histories"):
                obj = AlarmHistory()
                obj._deserialize(item)
                self.Histories.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmMetricsRequest(AbstractModel):
    """DescribeAlarmMetrics request structure.

    """

    def __init__(self):
        """
        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param MonitorType: Monitor type filter. Valid values: MT_QCE (Tencent Cloud service monitoring)\n        :type MonitorType: str\n        :param Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API\n        :type Namespace: str\n        """
        self.Module = None
        self.MonitorType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmMetricsResponse(AbstractModel):
    """DescribeAlarmMetrics response structure.

    """

    def __init__(self):
        """
        :param Metrics: Alarm metric list\n        :type Metrics: list of Metric\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Metrics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmNoticeCallbacksRequest(AbstractModel):
    """DescribeAlarmNoticeCallbacks request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeCallbacksResponse(AbstractModel):
    """DescribeAlarmNoticeCallbacks response structure.

    """

    def __init__(self):
        """
        :param URLNotices: Alarm callback notification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type URLNotices: list of URLNotice\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.URLNotices = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmNoticeRequest(AbstractModel):
    """DescribeAlarmNotice request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param NoticeId: Alarm notification template ID\n        :type NoticeId: str\n        """
        self.Module = None
        self.NoticeId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticeResponse(AbstractModel):
    """DescribeAlarmNotice response structure.

    """

    def __init__(self):
        """
        :param Notice: Alarm notification template details\n        :type Notice: :class:`tencentcloud.monitor.v20180724.models.AlarmNotice`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Notice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Notice") is not None:
            self.Notice = AlarmNotice()
            self.Notice._deserialize(params.get("Notice"))
        self.RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param PageNumber: Page number. Minimum value: 1\n        :type PageNumber: int\n        :param PageSize: Number of entries per page. Value range: 1–200\n        :type PageSize: int\n        :param Order: Sort by update time. Valid values: ASC (ascending), DESC (descending)\n        :type Order: str\n        :param OwnerUid: Root account `uid`, which is used to create preset notifications\n        :type OwnerUid: int\n        :param Name: Alarm notification template name, which is used for fuzzy search\n        :type Name: str\n        :param ReceiverType: Filter by recipient. The type of notified users should be selected for the alarm notification template. Valid values: USER (user), GROUP (user group). If this parameter is left empty, no filter by recipient will be performed\n        :type ReceiverType: str\n        :param UserIds: Recipient object list\n        :type UserIds: list of int\n        :param GroupIds: Recipient group list\n        :type GroupIds: list of int\n        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.Order = None
        self.OwnerUid = None
        self.Name = None
        self.ReceiverType = None
        self.UserIds = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Order = params.get("Order")
        self.OwnerUid = params.get("OwnerUid")
        self.Name = params.get("Name")
        self.ReceiverType = params.get("ReceiverType")
        self.UserIds = params.get("UserIds")
        self.GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of alarm notification templates\n        :type TotalCount: int\n        :param Notices: Alarm notification template list\n        :type Notices: list of AlarmNotice\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Notices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Notices") is not None:
            self.Notices = []
            for item in params.get("Notices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.Notices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmPoliciesRequest(AbstractModel):
    """DescribeAlarmPolicies request structure.

    """

    def __init__(self):
        """
        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param PageNumber: Page number starting from 1. Default value: 1\n        :type PageNumber: int\n        :param PageSize: Number of entries per page. Value range: 1–100. Default value: 20\n        :type PageSize: int\n        :param PolicyName: Fuzzy search by policy name\n        :type PolicyName: str\n        :param MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default\n        :type MonitorTypes: list of str\n        :param Namespaces: Filter by namespace. For the values of different policy types, please see:
[Policy Type List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)\n        :type Namespaces: list of str\n        :param Dimensions: The alarm object list, which is a JSON string. The outer array corresponds to multiple instances, and the inner array is the dimension of an object. For example, “CVM - Basic Monitor” can be written as:
`[ {"Dimensions": {"unInstanceId": "ins-qr8d555g"}}, {"Dimensions": {"unInstanceId": "ins-qr8d555h"}} ]`
You can also refer to the “Example 2” below.

For more information on the parameter samples of different Tencent Cloud services, see [Product Policy Type and Dimension Information](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1).\n        :type Dimensions: str\n        :param ReceiverUids: Search by recipient. You can get the user list with the API [ListUsers](https://intl.cloud.tencent.com/document/product/598/34587?from_cn_redirect=1) in “Cloud Access Management” or query the sub-user information with the API [GetUser](https://intl.cloud.tencent.com/document/product/598/34590?from_cn_redirect=1). The `Uid` field in the returned result should be entered here.\n        :type ReceiverUids: list of int\n        :param ReceiverGroups: Search by recipient group. You can get the user group list with the API [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) in “Cloud Access Management” or query the user group list where a sub-user is in with the API [ListGroupsForUser](https://intl.cloud.tencent.com/document/product/598/34588?from_cn_redirect=1). The `GroupId` field in the returned result should be entered here.\n        :type ReceiverGroups: list of int\n        :param PolicyType: Filter by default policy. Valid values: DEFAULT (display default policy), NOT_DEFAULT (display non-default policies). If this parameter is left empty, all policies will be displayed\n        :type PolicyType: list of str\n        :param Field: Sort by field. For example, to sort by the last modification time, use Field: "UpdateTime".\n        :type Field: str\n        :param Order: Sort order. Valid values: ASC (ascending), DESC (descending)\n        :type Order: str\n        :param ProjectIds: ID array of the policy project, which can be viewed on the following page:
[Project Management](https://console.cloud.tencent.com/project)\n        :type ProjectIds: list of int\n        :param NoticeIds: ID list of the notification template, which can be obtained by querying the notification template list.
It can be queried with the API [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1).\n        :type NoticeIds: list of str\n        :param RuleTypes: Filter by trigger condition. Valid values: STATIC (display policies with static threshold), DYNAMIC (display policies with dynamic threshold). If this parameter is left empty, all policies will be displayed\n        :type RuleTypes: list of str\n        :param Enable: Filter by alarm status. Valid values: [1]: enabled; [0]: disabled; [0, 1]: all\n        :type Enable: list of int\n        :param NotBindingNoticeRule: If `1` is passed in, alarm policies with no notification rules configured are queried. If it is left empty or other values are passed in, all alarm policies are queried.\n        :type NotBindingNoticeRule: int\n        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.PolicyName = None
        self.MonitorTypes = None
        self.Namespaces = None
        self.Dimensions = None
        self.ReceiverUids = None
        self.ReceiverGroups = None
        self.PolicyType = None
        self.Field = None
        self.Order = None
        self.ProjectIds = None
        self.NoticeIds = None
        self.RuleTypes = None
        self.Enable = None
        self.NotBindingNoticeRule = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.PolicyName = params.get("PolicyName")
        self.MonitorTypes = params.get("MonitorTypes")
        self.Namespaces = params.get("Namespaces")
        self.Dimensions = params.get("Dimensions")
        self.ReceiverUids = params.get("ReceiverUids")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PolicyType = params.get("PolicyType")
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        self.ProjectIds = params.get("ProjectIds")
        self.NoticeIds = params.get("NoticeIds")
        self.RuleTypes = params.get("RuleTypes")
        self.Enable = params.get("Enable")
        self.NotBindingNoticeRule = params.get("NotBindingNoticeRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmPoliciesResponse(AbstractModel):
    """DescribeAlarmPolicies response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of policies\n        :type TotalCount: int\n        :param Policies: Policy array\n        :type Policies: list of AlarmPolicy\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Policies = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Policies") is not None:
            self.Policies = []
            for item in params.get("Policies"):
                obj = AlarmPolicy()
                obj._deserialize(item)
                self.Policies.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmPolicyRequest(AbstractModel):
    """DescribeAlarmPolicy request structure.

    """

    def __init__(self):
        """
        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        """
        self.Module = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmPolicyResponse(AbstractModel):
    """DescribeAlarmPolicy response structure.

    """

    def __init__(self):
        """
        :param Policy: Policy details\n        :type Policy: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicy`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Policy = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = AlarmPolicy()
            self.Policy._deserialize(params.get("Policy"))
        self.RequestId = params.get("RequestId")


class DescribeAllNamespacesRequest(AbstractModel):
    """DescribeAllNamespaces request structure.

    """

    def __init__(self):
        """
        :param SceneType: Filter by use case. Currently, the only valid value is `ST_ALARM` (alarm type).\n        :type SceneType: str\n        :param Module: Value fixed at "monitor"\n        :type Module: str\n        :param MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default\n        :type MonitorTypes: list of str\n        :param Ids: Filter by namespace ID. If this parameter is left empty, all will be queried\n        :type Ids: list of str\n        """
        self.SceneType = None
        self.Module = None
        self.MonitorTypes = None
        self.Ids = None


    def _deserialize(self, params):
        self.SceneType = params.get("SceneType")
        self.Module = params.get("Module")
        self.MonitorTypes = params.get("MonitorTypes")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllNamespacesResponse(AbstractModel):
    """DescribeAllNamespaces response structure.

    """

    def __init__(self):
        """
        :param QceNamespaces: Alarm policy type of Tencent Cloud service (disused)\n        :type QceNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`\n        :param CustomNamespaces: Other alarm policy type (disused)\n        :type CustomNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`\n        :param QceNamespacesNew: Alarm policy type of Tencent Cloud service\n        :type QceNamespacesNew: list of CommonNamespace\n        :param CustomNamespacesNew: Other alarm policy type (not supported currently)\n        :type CustomNamespacesNew: list of CommonNamespace\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.QceNamespaces = None
        self.CustomNamespaces = None
        self.QceNamespacesNew = None
        self.CustomNamespacesNew = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QceNamespaces") is not None:
            self.QceNamespaces = CommonNamespace()
            self.QceNamespaces._deserialize(params.get("QceNamespaces"))
        if params.get("CustomNamespaces") is not None:
            self.CustomNamespaces = CommonNamespace()
            self.CustomNamespaces._deserialize(params.get("CustomNamespaces"))
        if params.get("QceNamespacesNew") is not None:
            self.QceNamespacesNew = []
            for item in params.get("QceNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self.QceNamespacesNew.append(obj)
        if params.get("CustomNamespacesNew") is not None:
            self.CustomNamespacesNew = []
            for item in params.get("CustomNamespacesNew"):
                obj = CommonNamespace()
                obj._deserialize(item)
                self.CustomNamespacesNew.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics request structure.

    """

    def __init__(self):
        """
        :param Namespace: Service namespace. Tencent Cloud services have different namespaces. For more information on service namespaces, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the namespace of CVM\n        :type Namespace: str\n        :param MetricName: Metric name. Tencent Cloud services have different metric names. For more information on metric names, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the metric names of CVM\n        :type MetricName: str\n        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics response structure.

    """

    def __init__(self):
        """
        :param MetricSet: Listed of queried metric descriptions\n        :type MetricSet: list of MetricSet\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBasicAlarmListAlarms(AbstractModel):
    """Alarms returned by DescribeBasicAlarmList

    """

    def __init__(self):
        """
        :param Id: Alarm ID.\n        :type Id: int\n        :param ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.\n        :type ProjectId: int\n        :param ProjectName: Project name.
Note: This field may return null, indicating that no valid value was found.\n        :type ProjectName: str\n        :param Status: Alarm status ID. Valid values: 0 (not resolved), 1 (resolved), 2/3/5 (insufficient data), 4 (expired)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_DATA (insufficient data), NO_CONF (expired)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AlarmStatus: str\n        :param GroupId: Policy group ID.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupId: int\n        :param GroupName: Policy group name.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupName: str\n        :param FirstOccurTime: Occurrence time.
Note: This field may return null, indicating that no valid value was found.\n        :type FirstOccurTime: str\n        :param Duration: Duration in seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type Duration: int\n        :param LastOccurTime: End time.
Note: This field may return null, indicating that no valid value was found.\n        :type LastOccurTime: str\n        :param Content: Alarm content.
Note: This field may return null, indicating that no valid value was found.\n        :type Content: str\n        :param ObjName: Alarm object.
Note: This field may return null, indicating that no valid value was found.\n        :type ObjName: str\n        :param ObjId: Alarm object ID.
Note: This field may return null, indicating that no valid value was found.\n        :type ObjId: str\n        :param ViewName: Policy type.
Note: This field may return null, indicating that no valid value was found.\n        :type ViewName: str\n        :param Vpc: VPC, which is unique to CVM.
Note: This field may return null, indicating that no valid value was found.\n        :type Vpc: str\n        :param MetricId: Metric ID.
Note: This field may return null, indicating that no valid value was found.\n        :type MetricId: int\n        :param MetricName: Metric name.
Note: This field may return null, indicating that no valid value was found.\n        :type MetricName: str\n        :param AlarmType: Alarm type. The value 0 indicates metric alarms. The value 2 indicates product event alarms. The value 3 indicates platform event alarms.
Note: This field may return null, indicating that no valid value was found.\n        :type AlarmType: int\n        :param Region: Region.
Note: This field may return null, indicating that no valid value was found.\n        :type Region: str\n        :param Dimensions: Dimensions of an alarm object.
Note: This field may return null, indicating that no valid value was found.\n        :type Dimensions: str\n        :param NotifyWay: Notification method.
Note: This field may return null, indicating that no valid value was found.\n        :type NotifyWay: list of str\n        :param InstanceGroup: Instance group information.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceGroup: list of InstanceGroup\n        """
        self.Id = None
        self.ProjectId = None
        self.ProjectName = None
        self.Status = None
        self.AlarmStatus = None
        self.GroupId = None
        self.GroupName = None
        self.FirstOccurTime = None
        self.Duration = None
        self.LastOccurTime = None
        self.Content = None
        self.ObjName = None
        self.ObjId = None
        self.ViewName = None
        self.Vpc = None
        self.MetricId = None
        self.MetricName = None
        self.AlarmType = None
        self.Region = None
        self.Dimensions = None
        self.NotifyWay = None
        self.InstanceGroup = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Status = params.get("Status")
        self.AlarmStatus = params.get("AlarmStatus")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.Duration = params.get("Duration")
        self.LastOccurTime = params.get("LastOccurTime")
        self.Content = params.get("Content")
        self.ObjName = params.get("ObjName")
        self.ObjId = params.get("ObjId")
        self.ViewName = params.get("ViewName")
        self.Vpc = params.get("Vpc")
        self.MetricId = params.get("MetricId")
        self.MetricName = params.get("MetricName")
        self.AlarmType = params.get("AlarmType")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.NotifyWay = params.get("NotifyWay")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroup()
                obj._deserialize(item)
                self.InstanceGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList request structure.

    """

    def __init__(self):
        """
        :param Module: API component name. The value for the current API is monitor.\n        :type Module: str\n        :param StartTime: Start time, which is the timestamp one day prior by default.\n        :type StartTime: int\n        :param EndTime: End time, which is the current timestamp by default.\n        :type EndTime: int\n        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.\n        :type Limit: int\n        :param Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.\n        :type Offset: int\n        :param OccurTimeOrder: Sorting by occurrence time. Valid values: asc and desc.\n        :type OccurTimeOrder: str\n        :param ProjectIds: Filter by project ID.\n        :type ProjectIds: list of int\n        :param ViewNames: Filter by policy type.\n        :type ViewNames: list of str\n        :param AlarmStatus: Filter by alarm status.\n        :type AlarmStatus: list of int\n        :param ObjLike: Filter by alarm object.\n        :type ObjLike: str\n        :param InstanceGroupIds: Filter by instance group ID.\n        :type InstanceGroupIds: list of int\n        :param MetricNames: Filtering by metric names\n        :type MetricNames: list of str\n        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OccurTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.AlarmStatus = None
        self.ObjLike = None
        self.InstanceGroupIds = None
        self.MetricNames = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.AlarmStatus = params.get("AlarmStatus")
        self.ObjLike = params.get("ObjLike")
        self.InstanceGroupIds = params.get("InstanceGroupIds")
        self.MetricNames = params.get("MetricNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList response structure.

    """

    def __init__(self):
        """
        :param Alarms: Alarm list.
Note: This field may return null, indicating that no valid value was found.\n        :type Alarms: list of DescribeBasicAlarmListAlarms\n        :param Total: Total number.
Note: This field may return null, indicating that no valid value was found.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """Dimensions of the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        """
        :param RegionId: Region ID.\n        :type RegionId: int\n        :param Region: Region abbreviation.\n        :type Region: str\n        :param Dimensions: Combined JSON string of dimensions.\n        :type Dimensions: str\n        :param EventDimensions: Combined JSON string of event dimensions.\n        :type EventDimensions: str\n        """
        self.RegionId = None
        self.Region = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """Object instance information returned by the DescribeBindingPolicyObjectListInstance API.

    """

    def __init__(self):
        """
        :param UniqueId: Unique ID of the object.\n        :type UniqueId: str\n        :param Dimensions: Dimension set of an object instance, which is a jsonObj string.\n        :type Dimensions: str\n        :param IsShielded: Whether the object is shielded. The value 0 indicates that the object is not shielded. The value 1 indicates that the object is shielded.\n        :type IsShielded: int\n        :param Region: Region where the object resides.\n        :type Region: str\n        """
        self.UniqueId = None
        self.Dimensions = None
        self.IsShielded = None
        self.Region = None


    def _deserialize(self, params):
        self.UniqueId = params.get("UniqueId")
        self.Dimensions = params.get("Dimensions")
        self.IsShielded = params.get("IsShielded")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """Instance group information returned by the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        """
        :param InstanceGroupId: Instance group ID.\n        :type InstanceGroupId: int\n        :param ViewName: Alarm policy type name.\n        :type ViewName: str\n        :param LastEditUin: Uin that was last edited.\n        :type LastEditUin: str\n        :param GroupName: Instance group name.\n        :type GroupName: str\n        :param InstanceSum: Number of instances.\n        :type InstanceSum: int\n        :param UpdateTime: Update time.\n        :type UpdateTime: int\n        :param InsertTime: Creation time.\n        :type InsertTime: int\n        :param Regions: Regions where the instances reside.
Note: This field may return null, indicating that no valid value was found.\n        :type Regions: list of str\n        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None
        self.Regions = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID. If the ID is in the format of “policy-xxxx”, please enter it in the `PolicyId` field. Enter 0 in this field.\n        :type GroupId: int\n        :param PolicyId: Alarm policy ID in the format of “policy-xxxx”. If a value has been entered in this field, you can enter 0 in the `GroupId` field.\n        :type PolicyId: str\n        :param Limit: The number of alarm objects returned each time. Value range: 1-100. Default value: 20.\n        :type Limit: int\n        :param Offset: Offset, which starts from 0 and is set to 0 by default. For example, the parameter `Offset=0&Limit=20` returns the zeroth to 19th alarm objects, and `Offset=20&Limit=20` returns the 20th to 39th alarm objects, and so on.\n        :type Offset: int\n        :param Dimensions: Dimensions of filtering objects.\n        :type Dimensions: list of DescribeBindingPolicyObjectListDimension\n        """
        self.Module = None
        self.GroupId = None
        self.PolicyId = None
        self.Limit = None
        self.Offset = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList response structure.

    """

    def __init__(self):
        """
        :param List: List of bound object instances.
Note: This field may return null, indicating that no valid value was found.\n        :type List: list of DescribeBindingPolicyObjectListInstance\n        :param Total: Total number of bound object instances.\n        :type Total: int\n        :param NoShieldedSum: Number of object instances that are not shielded.\n        :type NoShieldedSum: int\n        :param InstanceGroup: Bound instance group information. This parameter is not configured if no instance group is bound.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.List = None
        self.Total = None
        self.NoShieldedSum = None
        self.InstanceGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DescribeBindingPolicyObjectListInstance()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.NoShieldedSum = params.get("NoShieldedSum")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribeBindingPolicyObjectListInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.RequestId = params.get("RequestId")


class DescribeMonitorTypesRequest(AbstractModel):
    """DescribeMonitorTypes request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorTypesResponse(AbstractModel):
    """DescribeMonitorTypes response structure.

    """

    def __init__(self):
        """
        :param MonitorTypes: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)\n        :type MonitorTypes: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.MonitorTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MonitorTypes = params.get("MonitorTypes")
        self.RequestId = params.get("RequestId")


class DescribePolicyConditionListCondition(AbstractModel):
    """Policy conditions returned by the DescribePolicyConditionList API

    """

    def __init__(self):
        """
        :param PolicyViewName: Policy view name.\n        :type PolicyViewName: str\n        :param EventMetrics: Event alarm conditions.
Note: This field may return null, indicating that no valid value was found.\n        :type EventMetrics: list of DescribePolicyConditionListEventMetric\n        :param IsSupportMultiRegion: Whether to support multiple regions.\n        :type IsSupportMultiRegion: bool\n        :param Metrics: Metric alarm conditions.
Note: This field may return null, indicating that no valid value was found.\n        :type Metrics: list of DescribePolicyConditionListMetric\n        :param Name: Policy type name.\n        :type Name: str\n        :param SortId: Sorting ID.\n        :type SortId: int\n        :param SupportDefault: Whether to support default policies.\n        :type SupportDefault: bool\n        :param SupportRegions: List of regions that support this policy type.
Note: This field may return null, indicating that no valid value was found.\n        :type SupportRegions: list of str\n        """
        self.PolicyViewName = None
        self.EventMetrics = None
        self.IsSupportMultiRegion = None
        self.Metrics = None
        self.Name = None
        self.SortId = None
        self.SupportDefault = None
        self.SupportRegions = None


    def _deserialize(self, params):
        self.PolicyViewName = params.get("PolicyViewName")
        if params.get("EventMetrics") is not None:
            self.EventMetrics = []
            for item in params.get("EventMetrics"):
                obj = DescribePolicyConditionListEventMetric()
                obj._deserialize(item)
                self.EventMetrics.append(obj)
        self.IsSupportMultiRegion = params.get("IsSupportMultiRegion")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = DescribePolicyConditionListMetric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Name = params.get("Name")
        self.SortId = params.get("SortId")
        self.SupportDefault = params.get("SupportDefault")
        self.SupportRegions = params.get("SupportRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        """
        :param CalcType: Check method.
Note: This field may return null, indicating that no valid value was found.\n        :type CalcType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`\n        :param CalcValue: Threshold.
Note: This field may return null, indicating that no valid value was found.\n        :type CalcValue: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`\n        :param ContinueTime: Duration.
Note: This field may return null, indicating that no valid value was found.\n        :type ContinueTime: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`\n        :param Period: Data period.
Note: This field may return null, indicating that no valid value was found.\n        :type Period: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`\n        :param PeriodNum: Number of periods.
Note: This field may return null, indicating that no valid value was found.\n        :type PeriodNum: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`\n        :param StatType: Statistics method.
Note: This field may return null, indicating that no valid value was found.\n        :type StatType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`\n        """
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.Period = None
        self.PeriodNum = None
        self.StatType = None


    def _deserialize(self, params):
        if params.get("CalcType") is not None:
            self.CalcType = DescribePolicyConditionListConfigManualCalcType()
            self.CalcType._deserialize(params.get("CalcType"))
        if params.get("CalcValue") is not None:
            self.CalcValue = DescribePolicyConditionListConfigManualCalcValue()
            self.CalcValue._deserialize(params.get("CalcValue"))
        if params.get("ContinueTime") is not None:
            self.ContinueTime = DescribePolicyConditionListConfigManualContinueTime()
            self.ContinueTime._deserialize(params.get("ContinueTime"))
        if params.get("Period") is not None:
            self.Period = DescribePolicyConditionListConfigManualPeriod()
            self.Period._deserialize(params.get("Period"))
        if params.get("PeriodNum") is not None:
            self.PeriodNum = DescribePolicyConditionListConfigManualPeriodNum()
            self.PeriodNum._deserialize(params.get("PeriodNum"))
        if params.get("StatType") is not None:
            self.StatType = DescribePolicyConditionListConfigManualStatType()
            self.StatType._deserialize(params.get("StatType"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        """
        :param Keys: Value of CalcType.
Note: This field may return null, indicating that no valid value was found.\n        :type Keys: list of int\n        :param Need: Required or not.\n        :type Need: bool\n        """
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        """
        :param Default: Default value.
Note: This field may return null, indicating that no valid value was found.\n        :type Default: str\n        :param Fixed: Fixed value.
Note: This field may return null, indicating that no valid value was found.\n        :type Fixed: str\n        :param Max: Maximum value.
Note: This field may return null, indicating that no valid value was found.\n        :type Max: str\n        :param Min: Minimum value.
Note: This field may return null, indicating that no valid value was found.\n        :type Min: str\n        :param Need: Required or not.\n        :type Need: bool\n        """
        self.Default = None
        self.Fixed = None
        self.Max = None
        self.Min = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Fixed = params.get("Fixed")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        """
        :param Default: Default duration in seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type Default: int\n        :param Keys: Custom durations in seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type Keys: list of int\n        :param Need: Required or not.\n        :type Need: bool\n        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        """
        :param Default: Default period in seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type Default: int\n        :param Keys: Custom periods in seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type Keys: list of int\n        :param Need: Required or not.\n        :type Need: bool\n        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        """
        :param Default: Number of default periods.
Note: This field may return null, indicating that no valid value was found.\n        :type Default: int\n        :param Keys: Number of custom periods.
Note: This field may return null, indicating that no valid value was found.\n        :type Keys: list of int\n        :param Need: Required or not.\n        :type Need: bool\n        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        """
        :param P5: Data aggregation method in a period of 5 seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type P5: str\n        :param P10: Data aggregation method in a period of 10 seconds.
Note: This field may return null, indicating that no valid value was found.\n        :type P10: str\n        :param P60: Data aggregation method in a period of 1 minute.
Note: This field may return null, indicating that no valid value was found.\n        :type P60: str\n        :param P300: Data aggregation method in a period of 5 minutes.
Note: This field may return null, indicating that no valid value was found.\n        :type P300: str\n        :param P600: Data aggregation method in a period of 10 minutes.
Note: This field may return null, indicating that no valid value was found.\n        :type P600: str\n        :param P1800: Data aggregation method in a period of 30 minutes.
Note: This field may return null, indicating that no valid value was found.\n        :type P1800: str\n        :param P3600: Data aggregation method in a period of 1 hour.
Note: This field may return null, indicating that no valid value was found.\n        :type P3600: str\n        :param P86400: Data aggregation method in a period of 1 day.
Note: This field may return null, indicating that no valid value was found.\n        :type P86400: str\n        """
        self.P5 = None
        self.P10 = None
        self.P60 = None
        self.P300 = None
        self.P600 = None
        self.P1800 = None
        self.P3600 = None
        self.P86400 = None


    def _deserialize(self, params):
        self.P5 = params.get("P5")
        self.P10 = params.get("P10")
        self.P60 = params.get("P60")
        self.P300 = params.get("P300")
        self.P600 = params.get("P600")
        self.P1800 = params.get("P1800")
        self.P3600 = params.get("P3600")
        self.P86400 = params.get("P86400")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        """
        :param EventId: Event ID.\n        :type EventId: int\n        :param EventShowName: Event name.\n        :type EventShowName: str\n        :param NeedRecovered: Whether to recover.\n        :type NeedRecovered: bool\n        :param Type: Event type, which is a reserved field. Currently, it is fixed to 2.\n        :type Type: int\n        """
        self.EventId = None
        self.EventShowName = None
        self.NeedRecovered = None
        self.Type = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventShowName = params.get("EventShowName")
        self.NeedRecovered = params.get("NeedRecovered")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListMetric(AbstractModel):
    """Metric alarm configuration.

    """

    def __init__(self):
        """
        :param ConfigManual: Metric configuration.
Note: This field may return null, indicating that no valid value was found.\n        :type ConfigManual: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`\n        :param MetricId: Metric ID.\n        :type MetricId: int\n        :param MetricShowName: Metric name.\n        :type MetricShowName: str\n        :param MetricUnit: Metric unit.\n        :type MetricUnit: str\n        """
        self.ConfigManual = None
        self.MetricId = None
        self.MetricShowName = None
        self.MetricUnit = None


    def _deserialize(self, params):
        if params.get("ConfigManual") is not None:
            self.ConfigManual = DescribePolicyConditionListConfigManual()
            self.ConfigManual._deserialize(params.get("ConfigManual"))
        self.MetricId = params.get("MetricId")
        self.MetricShowName = params.get("MetricShowName")
        self.MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList response structure.

    """

    def __init__(self):
        """
        :param Conditions: List of alarm policy conditions.\n        :type Conditions: list of DescribePolicyConditionListCondition\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Conditions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyConditionListCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePolicyGroupInfoCallback(AbstractModel):
    """User callback information output by the policy query

    """

    def __init__(self):
        """
        :param CallbackUrl: URL of the user callback API.\n        :type CallbackUrl: str\n        :param ValidFlag: Status of the user callback API. The value 0 indicates that the API is not verified. The value 1 indicates that the API is verified. The value 2 indicates that a URL exists but the API fails to be verified.\n        :type ValidFlag: int\n        :param VerifyCode: Verification code of the user callback API.\n        :type VerifyCode: str\n        """
        self.CallbackUrl = None
        self.ValidFlag = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ValidFlag = params.get("ValidFlag")
        self.VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoCondition(AbstractModel):
    """Alarm threshold conditions output by the policy query.

    """

    def __init__(self):
        """
        :param MetricShowName: Metric name.\n        :type MetricShowName: str\n        :param Period: Data aggregation period in seconds.\n        :type Period: int\n        :param MetricId: Metric ID.\n        :type MetricId: int\n        :param RuleId: Threshold rule ID.\n        :type RuleId: int\n        :param Unit: Metric unit.\n        :type Unit: str\n        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of `triggerTime`.\n        :type AlarmNotifyPeriod: int\n        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. The value 7 indicates day-on-day increase. The value 8 indicates day-on-day decrease. The value 9 indicates week-on-week increase. The value 10 indicates week-on-week decrease. The value 11 indicates periodical increase. The value 12 indicates periodical decrease.\n        :type CalcType: int\n        :param CalcValue: Threshold.\n        :type CalcValue: str\n        :param ContinueTime: Duration at which an alarm will be triggered in seconds.\n        :type ContinueTime: int\n        :param MetricName: Alarm metric name.\n        :type MetricName: str\n        """
        self.MetricShowName = None
        self.Period = None
        self.MetricId = None
        self.RuleId = None
        self.Unit = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.MetricShowName = params.get("MetricShowName")
        self.Period = params.get("Period")
        self.MetricId = params.get("MetricId")
        self.RuleId = params.get("RuleId")
        self.Unit = params.get("Unit")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.ContinueTime = params.get("ContinueTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """Template-based policy group information output by the policy query

    """

    def __init__(self):
        """
        :param GroupId: Policy group ID.\n        :type GroupId: int\n        :param GroupName: Policy group name.\n        :type GroupName: str\n        :param ViewName: Policy type.\n        :type ViewName: str\n        :param Remark: Policy group remarks.\n        :type Remark: str\n        :param LastEditUin: Uin that was last edited.\n        :type LastEditUin: str\n        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.\n        :type UpdateTime: int\n        :param InsertTime: Creation time.
Note: This field may return null, indicating that no valid value was found.\n        :type InsertTime: int\n        :param IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.\n        :type IsUnionRule: int\n        """
        self.GroupId = None
        self.GroupName = None
        self.ViewName = None
        self.Remark = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """Event alarm conditions output by the policy query

    """

    def __init__(self):
        """
        :param EventId: Event ID.\n        :type EventId: int\n        :param RuleId: Event alarm rule ID.\n        :type RuleId: int\n        :param EventShowName: Event name.\n        :type EventShowName: str\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.\n        :type AlarmNotifyPeriod: int\n        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        """
        self.EventId = None
        self.RuleId = None
        self.EventShowName = None
        self.AlarmNotifyPeriod = None
        self.AlarmNotifyType = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RuleId = params.get("RuleId")
        self.EventShowName = params.get("EventShowName")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """Alarm recipient information output by the policy query

    """

    def __init__(self):
        """
        :param ReceiverGroupList: List of alarm recipient group IDs.\n        :type ReceiverGroupList: list of int\n        :param ReceiverUserList: List of alarm recipient IDs.\n        :type ReceiverUserList: list of int\n        :param StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates '10:0:0'.\n        :type StartTime: int\n        :param EndTime: End time of the alarm period. The meaning is the same as that of StartTime.\n        :type EndTime: int\n        :param ReceiverType: Recipient type. Valid values: group and user.\n        :type ReceiverType: str\n        :param NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".\n        :type NotifyWay: list of str\n        :param UidList: Uid of the alarm call recipient.
Note: This field may return null, indicating that no valid value was found.\n        :type UidList: list of int\n        :param RoundNumber: Number of alarm call rounds.\n        :type RoundNumber: int\n        :param RoundInterval: Intervals of alarm call rounds in seconds.\n        :type RoundInterval: int\n        :param PersonInterval: Alarm call intervals for individuals in seconds.\n        :type PersonInterval: int\n        :param NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.\n        :type NeedSendNotice: int\n        :param SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).\n        :type SendFor: list of str\n        :param RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.\n        :type RecoverNotify: list of str\n        :param ReceiveLanguage: Alarm language.
Note: This field may return null, indicating that no valid value was found.\n        :type ReceiveLanguage: str\n        """
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.StartTime = None
        self.EndTime = None
        self.ReceiverType = None
        self.NotifyWay = None
        self.UidList = None
        self.RoundNumber = None
        self.RoundInterval = None
        self.PersonInterval = None
        self.NeedSendNotice = None
        self.SendFor = None
        self.RecoverNotify = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReceiverType = params.get("ReceiverType")
        self.NotifyWay = params.get("NotifyWay")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.RoundInterval = params.get("RoundInterval")
        self.PersonInterval = params.get("PersonInterval")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.SendFor = params.get("SendFor")
        self.RecoverNotify = params.get("RecoverNotify")
        self.ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID.\n        :type GroupId: int\n        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo response structure.

    """

    def __init__(self):
        """
        :param GroupName: Policy group name.\n        :type GroupName: str\n        :param ProjectId: ID of the project to which the policy group belongs.\n        :type ProjectId: int\n        :param IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.\n        :type IsDefault: int\n        :param ViewName: Policy type.\n        :type ViewName: str\n        :param Remark: Policy description\n        :type Remark: str\n        :param ShowName: Policy type name.\n        :type ShowName: str\n        :param LastEditUin: Uin that was last edited.\n        :type LastEditUin: str\n        :param UpdateTime: Last edited time.\n        :type UpdateTime: str\n        :param Region: Regions supported by this policy.\n        :type Region: list of str\n        :param DimensionGroup: List of policy type dimensions.\n        :type DimensionGroup: list of str\n        :param ConditionsConfig: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.\n        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition\n        :param EventConfig: Product event rule list.
Note: This field may return null, indicating that no valid value was found.\n        :type EventConfig: list of DescribePolicyGroupInfoEventCondition\n        :param ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.\n        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo\n        :param Callback: User callback information.
Note: This field may return null, indicating that no valid value was found.\n        :type Callback: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`\n        :param ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.\n        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`\n        :param CanSetDefault: Whether the policy can be configured as the default policy.\n        :type CanSetDefault: bool\n        :param IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.\n        :type IsUnionRule: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupName = None
        self.ProjectId = None
        self.IsDefault = None
        self.ViewName = None
        self.Remark = None
        self.ShowName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.Region = None
        self.DimensionGroup = None
        self.ConditionsConfig = None
        self.EventConfig = None
        self.ReceiverInfos = None
        self.Callback = None
        self.ConditionsTemp = None
        self.CanSetDefault = None
        self.IsUnionRule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.ShowName = params.get("ShowName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.DimensionGroup = params.get("DimensionGroup")
        if params.get("ConditionsConfig") is not None:
            self.ConditionsConfig = []
            for item in params.get("ConditionsConfig"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.ConditionsConfig.append(obj)
        if params.get("EventConfig") is not None:
            self.EventConfig = []
            for item in params.get("EventConfig"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConfig.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("Callback") is not None:
            self.Callback = DescribePolicyGroupInfoCallback()
            self.Callback._deserialize(params.get("Callback"))
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self.CanSetDefault = params.get("CanSetDefault")
        self.IsUnionRule = params.get("IsUnionRule")
        self.RequestId = params.get("RequestId")


class DescribePolicyGroupListGroup(AbstractModel):
    """DescribePolicyGroupList.Group

    """

    def __init__(self):
        """
        :param GroupId: Policy group ID.\n        :type GroupId: int\n        :param GroupName: Policy group name.\n        :type GroupName: str\n        :param IsOpen: Whether it is enabled.\n        :type IsOpen: bool\n        :param ViewName: Policy view name.\n        :type ViewName: str\n        :param LastEditUin: Uin that was last edited.\n        :type LastEditUin: str\n        :param UpdateTime: Last modified time.\n        :type UpdateTime: int\n        :param InsertTime: Creation time.\n        :type InsertTime: int\n        :param UseSum: Number of instances that are bound to the policy group.\n        :type UseSum: int\n        :param NoShieldedSum: Number of unshielded instances that are bound to the policy group.\n        :type NoShieldedSum: int\n        :param IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.\n        :type IsDefault: int\n        :param CanSetDefault: Whether the policy can be configured as the default policy.\n        :type CanSetDefault: bool\n        :param ParentGroupId: Parent policy group ID.\n        :type ParentGroupId: int\n        :param Remark: Remarks of the policy group.\n        :type Remark: str\n        :param ProjectId: ID of the project to which the policy group belongs.\n        :type ProjectId: int\n        :param Conditions: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.\n        :type Conditions: list of DescribePolicyGroupInfoCondition\n        :param EventConditions: Product event rule list.
Note: This field may return null, indicating that no valid value was found.\n        :type EventConditions: list of DescribePolicyGroupInfoEventCondition\n        :param ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.\n        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo\n        :param ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.\n        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`\n        :param InstanceGroup: Instance group that is bound to the policy group.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`\n        :param IsUnionRule: The 'AND' or 'OR' rule. The value 0 indicates the 'OR' rule (indicating that an alarm will be triggered if any rule meets the threshold condition). The value 1 indicates the 'AND' rule (indicating that an alarm will be triggered when all rules meet the threshold conditions).
Note: This field may return null, indicating that no valid value was found.\n        :type IsUnionRule: int\n        """
        self.GroupId = None
        self.GroupName = None
        self.IsOpen = None
        self.ViewName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.UseSum = None
        self.NoShieldedSum = None
        self.IsDefault = None
        self.CanSetDefault = None
        self.ParentGroupId = None
        self.Remark = None
        self.ProjectId = None
        self.Conditions = None
        self.EventConditions = None
        self.ReceiverInfos = None
        self.ConditionsTemp = None
        self.InstanceGroup = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsOpen = params.get("IsOpen")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.UseSum = params.get("UseSum")
        self.NoShieldedSum = params.get("NoShieldedSum")
        self.IsDefault = params.get("IsDefault")
        self.CanSetDefault = params.get("CanSetDefault")
        self.ParentGroupId = params.get("ParentGroupId")
        self.Remark = params.get("Remark")
        self.ProjectId = params.get("ProjectId")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribePolicyGroupListGroupInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """Instance group that is bound to a policy group of the DescribePolicyGroupList API

    """

    def __init__(self):
        """
        :param InstanceGroupId: Instance group name ID.\n        :type InstanceGroupId: int\n        :param ViewName: Policy type view name.\n        :type ViewName: str\n        :param LastEditUin: Uin that was last edited.\n        :type LastEditUin: str\n        :param GroupName: Instance group name.\n        :type GroupName: str\n        :param InstanceSum: Number of instances.\n        :type InstanceSum: int\n        :param UpdateTime: Update time.\n        :type UpdateTime: int\n        :param InsertTime: Creation time.\n        :type InsertTime: int\n        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100.\n        :type Limit: int\n        :param Offset: Parameter offset on each page. The value starts from 0.\n        :type Offset: int\n        :param Like: Search by policy name.\n        :type Like: str\n        :param InstanceGroupId: Instance group ID.\n        :type InstanceGroupId: int\n        :param UpdateTimeOrder: Sort by update time. Valid values: asc and desc.\n        :type UpdateTimeOrder: str\n        :param ProjectIds: Project ID list.\n        :type ProjectIds: list of int\n        :param ViewNames: List of alarm policy types.\n        :type ViewNames: list of str\n        :param FilterUnuseReceiver: Whether to filter policy groups without recipients. The value 1 indicates that policy groups without recipients will be filtered. The value 0 indicates that policy groups without recipients will not be filtered.\n        :type FilterUnuseReceiver: int\n        :param Receivers: Filter by recipient group.\n        :type Receivers: list of str\n        :param ReceiverUserList: Filter by recipient.\n        :type ReceiverUserList: list of str\n        :param Dimensions: Dimension set field (json string), for example, [[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]].\n        :type Dimensions: str\n        :param ConditionTempGroupId: Template-based policy group IDs, which are separated by commas.\n        :type ConditionTempGroupId: str\n        :param ReceiverType: Filter by recipient or recipient group. The value 'user' indicates by recipient. The value 'group' indicates by recipient group.\n        :type ReceiverType: str\n        :param IsOpen: Filter conditions. Whether the alarm policy has been enabled or disabled\n        :type IsOpen: bool\n        """
        self.Module = None
        self.Limit = None
        self.Offset = None
        self.Like = None
        self.InstanceGroupId = None
        self.UpdateTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.FilterUnuseReceiver = None
        self.Receivers = None
        self.ReceiverUserList = None
        self.Dimensions = None
        self.ConditionTempGroupId = None
        self.ReceiverType = None
        self.IsOpen = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Like = params.get("Like")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.FilterUnuseReceiver = params.get("FilterUnuseReceiver")
        self.Receivers = params.get("Receivers")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.Dimensions = params.get("Dimensions")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.ReceiverType = params.get("ReceiverType")
        self.IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList response structure.

    """

    def __init__(self):
        """
        :param GroupList: Policy group list.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupList: list of DescribePolicyGroupListGroup\n        :param Total: Total number of policy groups.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProductEventListDimensions(AbstractModel):
    """Input parameter Dimensions of the DescribeProductEventList API

    """

    def __init__(self):
        """
        :param Name: Dimension name.\n        :type Name: str\n        :param Value: Dimension value.\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEvents(AbstractModel):
    """Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
        :param EventId: Event ID.
Note: This field may return null, indicating that no valid value was found.\n        :type EventId: int\n        :param EventCName: Event name in Chinese.
Note: This field may return null, indicating that no valid value was found.\n        :type EventCName: str\n        :param EventEName: Event name in English.
Note: This field may return null, indicating that no valid value was found.\n        :type EventEName: str\n        :param EventName: Event name abbreviation.
Note: This field may return null, indicating that no valid value was found.\n        :type EventName: str\n        :param ProductCName: Product name in Chinese.
Note: This field may return null, indicating that no valid value was found.\n        :type ProductCName: str\n        :param ProductEName: Product name in English.
Note: This field may return null, indicating that no valid value was found.\n        :type ProductEName: str\n        :param ProductName: Product name abbreviation.
Note: This field may return null, indicating that no valid value was found.\n        :type ProductName: str\n        :param InstanceId: Instance ID.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceId: str\n        :param InstanceName: Instance name.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceName: str\n        :param ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.\n        :type ProjectId: str\n        :param Region: Region.
Note: This field may return null, indicating that no valid value was found.\n        :type Region: str\n        :param Status: Status.
Note: This field may return null, indicating that no valid value was found.\n        :type Status: str\n        :param SupportAlarm: Whether to support alarms.
Note: This field may return null, indicating that no valid value was found.\n        :type SupportAlarm: int\n        :param Type: Event type.
Note: This field may return null, indicating that no valid value was found.\n        :type Type: str\n        :param StartTime: Start time.
Note: This field may return null, indicating that no valid value was found.\n        :type StartTime: int\n        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.\n        :type UpdateTime: int\n        :param Dimensions: Instance object information.
Note: This field may return null, indicating that no valid value was found.\n        :type Dimensions: list of DescribeProductEventListEventsDimensions\n        :param AdditionMsg: Additional information of the instance object.
Note: This field may return null, indicating that no valid value was found.\n        :type AdditionMsg: list of DescribeProductEventListEventsDimensions\n        :param IsAlarmConfig: Whether to configure alarms.
Note: This field may return null, indicating that no valid value was found.\n        :type IsAlarmConfig: int\n        :param GroupInfo: Policy information.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo\n        :param ViewName: Display name
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type ViewName: str\n        """
        self.EventId = None
        self.EventCName = None
        self.EventEName = None
        self.EventName = None
        self.ProductCName = None
        self.ProductEName = None
        self.ProductName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Status = None
        self.SupportAlarm = None
        self.Type = None
        self.StartTime = None
        self.UpdateTime = None
        self.Dimensions = None
        self.AdditionMsg = None
        self.IsAlarmConfig = None
        self.GroupInfo = None
        self.ViewName = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventCName = params.get("EventCName")
        self.EventEName = params.get("EventEName")
        self.EventName = params.get("EventName")
        self.ProductCName = params.get("ProductCName")
        self.ProductEName = params.get("ProductEName")
        self.ProductName = params.get("ProductName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.SupportAlarm = params.get("SupportAlarm")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        if params.get("AdditionMsg") is not None:
            self.AdditionMsg = []
            for item in params.get("AdditionMsg"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.AdditionMsg.append(obj)
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = DescribeProductEventListEventsGroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsDimensions(AbstractModel):
    """Dimensions of events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
        :param Key: Dimension name in English.
Note: This field may return null, indicating that no valid value was found.\n        :type Key: str\n        :param Name: Dimension name in Chinese.
Note: This field may return null, indicating that no valid value was found.\n        :type Name: str\n        :param Value: Dimension value.
Note: This field may return null, indicating that no valid value was found.\n        :type Value: str\n        """
        self.Key = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """GroupInfo in Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
        :param GroupId: Policy ID.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupId: int\n        :param GroupName: Policy name.
Note: This field may return null, indicating that no valid value was found.\n        :type GroupName: str\n        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListOverView(AbstractModel):
    """OverView object returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
        :param StatusChangeAmount: Number of events whose statuses have changed.
Note: This field may return null, indicating that no valid value was found.\n        :type StatusChangeAmount: int\n        :param UnConfigAlarmAmount: Number of events whose alarm statuses are not configured.
Note: This field may return null, indicating that no valid value was found.\n        :type UnConfigAlarmAmount: int\n        :param UnNormalEventAmount: Number of events with exceptions.
Note: This field may return null, indicating that no valid value was found.\n        :type UnNormalEventAmount: int\n        :param UnRecoverAmount: Number of events that have not been recovered.
Note: This field may return null, indicating that no valid value was found.\n        :type UnRecoverAmount: int\n        """
        self.StatusChangeAmount = None
        self.UnConfigAlarmAmount = None
        self.UnNormalEventAmount = None
        self.UnRecoverAmount = None


    def _deserialize(self, params):
        self.StatusChangeAmount = params.get("StatusChangeAmount")
        self.UnConfigAlarmAmount = params.get("UnConfigAlarmAmount")
        self.UnNormalEventAmount = params.get("UnNormalEventAmount")
        self.UnRecoverAmount = params.get("UnRecoverAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList request structure.

    """

    def __init__(self):
        """
        :param Module: API component name. It is fixed to monitor.\n        :type Module: str\n        :param ProductName: Filter by product type. For example, 'cvm' indicates Cloud Virtual Machine.\n        :type ProductName: list of str\n        :param EventName: Filter by product name. For example, "guest_reboot" indicates server restart.\n        :type EventName: list of str\n        :param InstanceId: Affected object, such as "ins-19708ino"\n        :type InstanceId: list of str\n        :param Dimensions: Filter by dimension, such as by public IP: 10.0.0.1.\n        :type Dimensions: list of DescribeProductEventListDimensions\n        :param RegionList: Region filter parameter for service events, such as `gz`. For region abbreviations, please see [Region List](https://intl.cloud.tencent.com/document/product/248/50863?from_cn_redirect=1)\n        :type RegionList: list of str\n        :param Type: Filter by event type. Valid values: ["status_change","abnormal"], which indicate events whose statuses have changed and events with exceptions respectively.\n        :type Type: list of str\n        :param Status: Filter by event status. Valid values: ["recover","alarm","-"], which indicate that an event has been recovered, has not been recovered, and has no status respectively.\n        :type Status: list of str\n        :param Project: Filter by project ID.\n        :type Project: list of str\n        :param IsAlarmConfig: Filter by alarm status configuration. The value 1 indicates that the alarm status has been configured. The value 0 indicates that the alarm status has not been configured.\n        :type IsAlarmConfig: int\n        :param TimeOrder: Sorting by update time. The value ASC indicates the ascending order. The value DESC indicates the descending order. The default value is DESC.\n        :type TimeOrder: str\n        :param StartTime: Start time, which is the timestamp one day prior by default.\n        :type StartTime: int\n        :param EndTime: End time, which is the current timestamp by default.\n        :type EndTime: int\n        :param Offset: Page offset. The default value is 0.\n        :type Offset: int\n        :param Limit: The number of parameters that can be returned on each page. The default value is 20.\n        :type Limit: int\n        """
        self.Module = None
        self.ProductName = None
        self.EventName = None
        self.InstanceId = None
        self.Dimensions = None
        self.RegionList = None
        self.Type = None
        self.Status = None
        self.Project = None
        self.IsAlarmConfig = None
        self.TimeOrder = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.ProductName = params.get("ProductName")
        self.EventName = params.get("EventName")
        self.InstanceId = params.get("InstanceId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.RegionList = params.get("RegionList")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Project = params.get("Project")
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        self.TimeOrder = params.get("TimeOrder")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList response structure.

    """

    def __init__(self):
        """
        :param Events: Event list
Note: This field may return null, indicating that no valid value was found.\n        :type Events: list of DescribeProductEventListEvents\n        :param OverView: Event statistics.\n        :type OverView: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListOverView`\n        :param Total: Total number of events.
Note: This field may return null, indicating that no valid value was found.\n        :type Total: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Events = None
        self.OverView = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DescribeProductEventListEvents()
                obj._deserialize(item)
                self.Events.append(obj)
        if params.get("OverView") is not None:
            self.OverView = DescribeProductEventListOverView()
            self.OverView._deserialize(params.get("OverView"))
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeStatisticDataRequest(AbstractModel):
    """DescribeStatisticData request structure.

    """

    def __init__(self):
        """
        :param Module: Module, whose value is fixed at `monitor`\n        :type Module: str\n        :param Namespace: Namespace. Valid values: QCE/TKE\n        :type Namespace: str\n        :param MetricNames: Metric name list\n        :type MetricNames: list of str\n        :param Conditions: Dimension condition. The `=` and `in` operators are supported\n        :type Conditions: list of MidQueryCondition\n        :param Period: Statistical granularity in s. Default value: 300\n        :type Period: int\n        :param StartTime: Start time, which is the current time by default, such as 2020-12-08T19:51:23+08:00\n        :type StartTime: str\n        :param EndTime: End time, which is the current time by default, such as 2020-12-08T19:51:23+08:00\n        :type EndTime: str\n        :param GroupBys: `groupBy` by the specified dimension\n        :type GroupBys: list of str\n        """
        self.Module = None
        self.Namespace = None
        self.MetricNames = None
        self.Conditions = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.GroupBys = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Namespace = params.get("Namespace")
        self.MetricNames = params.get("MetricNames")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = MidQueryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.GroupBys = params.get("GroupBys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticDataResponse(AbstractModel):
    """DescribeStatisticData response structure.

    """

    def __init__(self):
        """
        :param Period: Statistical period\n        :type Period: int\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param Data: Monitoring data\n        :type Data: list of MetricData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    """Combination of instance object dimensions

    """

    def __init__(self):
        """
        :param Name: Instance dimension name\n        :type Name: str\n        :param Value: Instance dimension value\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionsDesc(AbstractModel):
    """Dimension information

    """

    def __init__(self):
        """
        :param Dimensions: Array of dimension names\n        :type Dimensions: list of str\n        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace, such as QCE/CVM. For more information on the namespaces of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1)\n        :type Namespace: str\n        :param MetricName: Metric name, such as `CPUUsage`. Only one monitoring metric can be pulled at a time. For more information on the metrics of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The corresponding metric name is `MetricName`.\n        :type MetricName: str\n        :param Instances: The dimension combination for instance objects, which is in the form of a set of key-value pairs. The dimension fields for instances of different Tencent Cloud services are completely different. For example, the field is [{"Name":"InstanceId","Value":"ins-j0hk02zo"}] for CVM instances, [{"Name":"instanceId","Value":"ckafka-l49k54dd"}] for CKafka instances, and [{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}] for COS instances. For more information on the dimensions of various Tencent Cloud services, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). In each document, the dimension column displays a dimension combination’s key, which has a corresponding value. A single request can get the data of up to 10 instances.\n        :type Instances: list of Instance\n        :param Period: Monitoring statistical period in seconds, such as 60. Default value: 300. The statistical period varies by metric. For more information on the statistical periods supported by each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The values in the statistical period column are the supported statistical periods. A single request can get up to 1,440 data points.\n        :type Period: int\n        :param StartTime: Start time such as 2018-09-22T19:51:23+08:00\n        :type StartTime: str\n        :param EndTime: End time, which is the current time by default, such as 2018-09-22T20:51:23+08:00. `EndTime` cannot be earlier than `StartTime`\n        :type EndTime: str\n        """
        self.Namespace = None
        self.MetricName = None
        self.Instances = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData response structure.

    """

    def __init__(self):
        """
        :param Period: Statistical period\n        :type Period: int\n        :param MetricName: Metric name\n        :type MetricName: str\n        :param DataPoints: Array of data points\n        :type DataPoints: list of DataPoint\n        :param StartTime: Start time\n        :type StartTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Array of instance dimension combinations

    """

    def __init__(self):
        """
        :param Dimensions: Combination of instance dimensions\n        :type Dimensions: list of Dimension\n        """
        self.Dimensions = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroup(AbstractModel):
    """InstanceGroup in Alarms returned by the DescribeBasicAlarmList API

    """

    def __init__(self):
        """
        :param InstanceGroupId: Instance group ID.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceGroupId: int\n        :param InstanceGroupName: Instance group name.
Note: This field may return null, indicating that no valid value was found.\n        :type InstanceGroupName: str\n        """
        self.InstanceGroupId = None
        self.InstanceGroupName = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.InstanceGroupName = params.get("InstanceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceGroups(AbstractModel):
    """Instance group of alarm object

    """

    def __init__(self):
        """
        :param Id: Instance group ID\n        :type Id: int\n        :param Name: Instance group name\n        :type Name: str\n        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metric(AbstractModel):
    """Metric, which can be used to set alarms and query data

    """

    def __init__(self):
        """
        :param Namespace: Alarm policy type\n        :type Namespace: str\n        :param MetricName: Metric name\n        :type MetricName: str\n        :param Description: Metric display name\n        :type Description: str\n        :param Min: Minimum value\n        :type Min: float\n        :param Max: Maximum value\n        :type Max: float\n        :param Dimensions: Dimension list\n        :type Dimensions: list of str\n        :param Unit: Unit\n        :type Unit: str\n        :param MetricConfig: Metric configuration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MetricConfig: :class:`tencentcloud.monitor.v20180724.models.MetricConfig`\n        """
        self.Namespace = None
        self.MetricName = None
        self.Description = None
        self.Min = None
        self.Max = None
        self.Dimensions = None
        self.Unit = None
        self.MetricConfig = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Description = params.get("Description")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.Dimensions = params.get("Dimensions")
        self.Unit = params.get("Unit")
        if params.get("MetricConfig") is not None:
            self.MetricConfig = MetricConfig()
            self.MetricConfig._deserialize(params.get("MetricConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricConfig(AbstractModel):
    """Metric configuration

    """

    def __init__(self):
        """
        :param Operator: Allowed operator\n        :type Operator: list of str\n        :param Period: Allowed data cycle in seconds\n        :type Period: list of int\n        :param ContinuePeriod: Allowed number of continuous cycles\n        :type ContinuePeriod: list of int\n        """
        self.Operator = None
        self.Period = None
        self.ContinuePeriod = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Period = params.get("Period")
        self.ContinuePeriod = params.get("ContinuePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """`DescribeMetricData` output parameters

    """

    def __init__(self):
        """
        :param MetricName: Metric name\n        :type MetricName: str\n        :param Points: Monitoring data point\n        :type Points: list of MetricDataPoint\n        """
        self.MetricName = None
        self.Points = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataPoint(AbstractModel):
    """`DescribeMetricData` output parameters

    """

    def __init__(self):
        """
        :param Dimensions: Combination of instance object dimensions\n        :type Dimensions: list of Dimension\n        :param Values: Data point list\n        :type Values: list of Point\n        """
        self.Dimensions = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = Point()
                obj._deserialize(item)
                self.Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDatum(AbstractModel):
    """Metric names and values

    """

    def __init__(self):
        """
        :param MetricName: Metric name.\n        :type MetricName: str\n        :param Value: Metric value.\n        :type Value: int\n        """
        self.MetricName = None
        self.Value = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricObjectMeaning(AbstractModel):
    """Meaning of metric data

    """

    def __init__(self):
        """
        :param En: Meaning of the metric in English\n        :type En: str\n        :param Zh: Meaning of the metric in Chinese\n        :type Zh: str\n        """
        self.En = None
        self.Zh = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Zh = params.get("Zh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricSet(AbstractModel):
    """Description of the unit and supported statistical period of the business metric

    """

    def __init__(self):
        """
        :param Namespace: Namespace. Each Tencent Cloud product has a namespace\n        :type Namespace: str\n        :param MetricName: Metric Name\n        :type MetricName: str\n        :param Unit: Unit used by the metric\n        :type Unit: str\n        :param UnitCname: Unit used by the metric\n        :type UnitCname: str\n        :param Period: Statistical period in seconds supported by the metric, such as 60 and 300\n        :type Period: list of int\n        :param Periods: Metric method during the statistical period\n        :type Periods: list of PeriodsSt\n        :param Meaning: Meaning of the statistical metric\n        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`\n        :param Dimensions: Dimension description\n        :type Dimensions: list of DimensionsDesc\n        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Unit = params.get("Unit")
        self.UnitCname = params.get("UnitCname")
        self.Period = params.get("Period")
        if params.get("Periods") is not None:
            self.Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self.Periods.append(obj)
        if params.get("Meaning") is not None:
            self.Meaning = MetricObjectMeaning()
            self.Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MidQueryCondition(AbstractModel):
    """`DescribeMidDimensionValueList` query conditions

    """

    def __init__(self):
        """
        :param Key: Dimension\n        :type Key: str\n        :param Operator: Operator. Valid values: eq (equal to), ne (not equal to), in\n        :type Operator: str\n        :param Value: Dimension value. If `Operator` is `eq` or `ne`, only the first element will be used\n        :type Value: list of str\n        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param Name: Alarm notification rule name, which can contain up to 60 characters\n        :type Name: str\n        :param NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)\n        :type NoticeType: str\n        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)\n        :type NoticeLanguage: str\n        :param NoticeId: Alarm notification template ID\n        :type NoticeId: str\n        :param UserNotices: User notifications (up to 5)\n        :type UserNotices: list of UserNotice\n        :param URLNotices: Callback notifications (up to 3)\n        :type URLNotices: list of URLNotice\n        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.NoticeId = None
        self.UserNotices = None
        self.URLNotices = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Name = params.get("Name")
        self.NoticeType = params.get("NoticeType")
        self.NoticeLanguage = params.get("NoticeLanguage")
        self.NoticeId = params.get("NoticeId")
        if params.get("UserNotices") is not None:
            self.UserNotices = []
            for item in params.get("UserNotices"):
                obj = UserNotice()
                obj._deserialize(item)
                self.UserNotices.append(obj)
        if params.get("URLNotices") is not None:
            self.URLNotices = []
            for item in params.get("URLNotices"):
                obj = URLNotice()
                obj._deserialize(item)
                self.URLNotices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmNoticeResponse(AbstractModel):
    """ModifyAlarmNotice response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyConditionRequest(AbstractModel):
    """ModifyAlarmPolicyCondition request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param ConditionTemplateId: ID of trigger condition template. This parameter can be left empty.\n        :type ConditionTemplateId: int\n        :param Condition: Metric trigger condition\n        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`\n        :param EventCondition: Event trigger condition\n        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`\n        :param Filter: Global filter.\n        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`\n        :param GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.\n        :type GroupBy: list of str\n        """
        self.Module = None
        self.PolicyId = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.Filter = None
        self.GroupBy = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.ConditionTemplateId = params.get("ConditionTemplateId")
        if params.get("Condition") is not None:
            self.Condition = AlarmPolicyCondition()
            self.Condition._deserialize(params.get("Condition"))
        if params.get("EventCondition") is not None:
            self.EventCondition = AlarmPolicyEventCondition()
            self.EventCondition._deserialize(params.get("EventCondition"))
        if params.get("Filter") is not None:
            self.Filter = AlarmPolicyFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyConditionResponse(AbstractModel):
    """ModifyAlarmPolicyCondition response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyInfoRequest(AbstractModel):
    """ModifyAlarmPolicyInfo request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param Key: Field to be modified. Valid values: NAME (policy name), REMARK (policy remarks)\n        :type Key: str\n        :param Value: Value after modification\n        :type Value: str\n        """
        self.Module = None
        self.PolicyId = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyInfoResponse(AbstractModel):
    """ModifyAlarmPolicyInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyNoticeRequest(AbstractModel):
    """ModifyAlarmPolicyNotice request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param NoticeIds: Alarm notification template ID list\n        :type NoticeIds: list of str\n        """
        self.Module = None
        self.PolicyId = None
        self.NoticeIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.NoticeIds = params.get("NoticeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyNoticeResponse(AbstractModel):
    """ModifyAlarmPolicyNotice response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyStatusRequest(AbstractModel):
    """ModifyAlarmPolicyStatus request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param Enable: Status. Valid values: 0 (disabled), 1 (enabled)\n        :type Enable: int\n        """
        self.Module = None
        self.PolicyId = None
        self.Enable = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyStatusResponse(AbstractModel):
    """ModifyAlarmPolicyStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyTasksRequest(AbstractModel):
    """ModifyAlarmPolicyTasks request structure.

    """

    def __init__(self):
        """
        :param Module: Module name. Enter "monitor" here\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        :param TriggerTasks: List of tasks triggered by alarm policy. If this parameter is left empty, it indicates to unbind all tasks\n        :type TriggerTasks: list of AlarmPolicyTriggerTask\n        """
        self.Module = None
        self.PolicyId = None
        self.TriggerTasks = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmPolicyTasksResponse(AbstractModel):
    """ModifyAlarmPolicyTasks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers request structure.

    """

    def __init__(self):
        """
        :param GroupId: ID of a policy group whose recipient needs to be modified.\n        :type GroupId: int\n        :param Module: Required. The value is fixed to monitor.\n        :type Module: str\n        :param ReceiverInfos: New recipient information. If this parameter is not configured, all recipients will be deleted.\n        :type ReceiverInfos: list of ReceiverInfo\n        """
        self.GroupId = None
        self.Module = None
        self.ReceiverInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = ReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPolicyGroupCondition(AbstractModel):
    """Modification of the metric threshold condition passed in by the alarm policy group.

    """

    def __init__(self):
        """
        :param MetricId: Metric ID.\n        :type MetricId: int\n        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to.\n        :type CalcType: int\n        :param CalcValue: Threshold.\n        :type CalcValue: str\n        :param CalcPeriod: Data period of the detected metric.\n        :type CalcPeriod: int\n        :param ContinuePeriod: Number of consecutive periods.\n        :type ContinuePeriod: int\n        :param AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.\n        :type AlarmNotifyPeriod: int\n        :param RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.\n        :type RuleId: int\n        """
        self.MetricId = None
        self.CalcType = None
        self.CalcValue = None
        self.CalcPeriod = None
        self.ContinuePeriod = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.MetricId = params.get("MetricId")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.CalcPeriod = params.get("CalcPeriod")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupEventCondition(AbstractModel):
    """Modification of the event alarm condition passed in by the alarm policy group.

    """

    def __init__(self):
        """
        :param EventId: Event ID.\n        :type EventId: int\n        :param AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.\n        :type AlarmNotifyType: int\n        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.\n        :type AlarmNotifyPeriod: int\n        :param RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.\n        :type RuleId: int\n        """
        self.EventId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupRequest(AbstractModel):
    """ModifyPolicyGroup request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID.\n        :type GroupId: int\n        :param ViewName: Alarm type.\n        :type ViewName: str\n        :param GroupName: Policy group name.\n        :type GroupName: str\n        :param IsUnionRule: The 'AND' and 'OR' rules for metric alarms. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met.\n        :type IsUnionRule: int\n        :param Conditions: Metric alarm condition rules. No filling indicates that all existing metric alarm condition rules will be deleted.\n        :type Conditions: list of ModifyPolicyGroupCondition\n        :param EventConditions: Event alarm conditions. No filling indicates that all existing event alarm conditions will be deleted.\n        :type EventConditions: list of ModifyPolicyGroupEventCondition\n        :param ConditionTempGroupId: Template-based policy group ID.\n        :type ConditionTempGroupId: int\n        """
        self.Module = None
        self.GroupId = None
        self.ViewName = None
        self.GroupName = None
        self.IsUnionRule = None
        self.Conditions = None
        self.EventConditions = None
        self.ConditionTempGroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.ViewName = params.get("ViewName")
        self.GroupName = params.get("GroupName")
        self.IsUnionRule = params.get("IsUnionRule")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ModifyPolicyGroupCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = ModifyPolicyGroupEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyGroupResponse(AbstractModel):
    """ModifyPolicyGroup response structure.

    """

    def __init__(self):
        """
        :param GroupId: Policy group ID.\n        :type GroupId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class MonitorTypeNamespace(AbstractModel):
    """Policy type

    """

    def __init__(self):
        """
        :param MonitorType: Monitor type\n        :type MonitorType: str\n        :param Namespace: Policy type value\n        :type Namespace: str\n        """
        self.MonitorType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.MonitorType = params.get("MonitorType")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeriodsSt(AbstractModel):
    """Statistical method during the period

    """

    def __init__(self):
        """
        :param Period: Period\n        :type Period: str\n        :param StatType: Statistical method\n        :type StatType: list of str\n        """
        self.Period = None
        self.StatType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StatType = params.get("StatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        """
        :param Timestamp: Time point when this monitoring data point is generated\n        :type Timestamp: int\n        :param Value: Monitoring data point value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Value: float\n        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMonitorDataRequest(AbstractModel):
    """PutMonitorData request structure.

    """

    def __init__(self):
        """
        :param Metrics: A group of metrics and data.\n        :type Metrics: list of MetricDatum\n        :param AnnounceIp: IP address that is automatically specified when monitoring data is reported.\n        :type AnnounceIp: str\n        :param AnnounceTimestamp: Timestamp that is automatically specified when monitoring data is reported.\n        :type AnnounceTimestamp: int\n        :param AnnounceInstance: IP address or product instance ID that is automatically specified when monitoring data is reported.\n        :type AnnounceInstance: str\n        """
        self.Metrics = None
        self.AnnounceIp = None
        self.AnnounceTimestamp = None
        self.AnnounceInstance = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = MetricDatum()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.AnnounceIp = params.get("AnnounceIp")
        self.AnnounceTimestamp = params.get("AnnounceTimestamp")
        self.AnnounceInstance = params.get("AnnounceInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMonitorDataResponse(AbstractModel):
    """PutMonitorData response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReceiverInfo(AbstractModel):
    """Recipient information.

    """

    def __init__(self):
        """
        :param StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates '10:0:0'.\n        :type StartTime: int\n        :param EndTime: End time of the alarm period. The meaning is the same as that of StartTime.\n        :type EndTime: int\n        :param NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".\n        :type NotifyWay: list of str\n        :param ReceiverType: Recipient type. Valid values: group and user.\n        :type ReceiverType: str\n        :param Id: ReceiverId\n        :type Id: int\n        :param SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).\n        :type SendFor: list of str\n        :param UidList: Uid of the alarm call recipient.\n        :type UidList: list of int\n        :param RoundNumber: Number of alarm call rounds.\n        :type RoundNumber: int\n        :param PersonInterval: Alarm call intervals for individuals in seconds.\n        :type PersonInterval: int\n        :param RoundInterval: Intervals of alarm call rounds in seconds.\n        :type RoundInterval: int\n        :param RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.\n        :type RecoverNotify: list of str\n        :param NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.\n        :type NeedSendNotice: int\n        :param ReceiverGroupList: Recipient group list. The list of recipient group IDs that is queried by a platform API.\n        :type ReceiverGroupList: list of int\n        :param ReceiverUserList: Recipient list. The list of recipient IDs that is queried by a platform API.\n        :type ReceiverUserList: list of int\n        :param ReceiveLanguage: Language of received alarms. Enumerated values: zh-CN and en-US.\n        :type ReceiveLanguage: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.NotifyWay = None
        self.ReceiverType = None
        self.Id = None
        self.SendFor = None
        self.UidList = None
        self.RoundNumber = None
        self.PersonInterval = None
        self.RoundInterval = None
        self.RecoverNotify = None
        self.NeedSendNotice = None
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverType = params.get("ReceiverType")
        self.Id = params.get("Id")
        self.SendFor = params.get("SendFor")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.PersonInterval = params.get("PersonInterval")
        self.RoundInterval = params.get("RoundInterval")
        self.RecoverNotify = params.get("RecoverNotify")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.ReceiveLanguage = params.get("ReceiveLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg request structure.

    """

    def __init__(self):
        """
        :param Module: API component name. The value for the current API is monitor.\n        :type Module: str\n        :param PolicyId: Message policy ID, which is configured on the custom message page of Cloud Monitor.\n        :type PolicyId: str\n        :param Msg: Custom message content that a user wants to send.\n        :type Msg: str\n        """
        self.Module = None
        self.PolicyId = None
        self.Msg = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCustomAlarmMsgResponse(AbstractModel):
    """SendCustomAlarmMsg response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetDefaultAlarmPolicyRequest(AbstractModel):
    """SetDefaultAlarmPolicy request structure.

    """

    def __init__(self):
        """
        :param Module: Module name, which is fixed at "monitor"\n        :type Module: str\n        :param PolicyId: Alarm policy ID\n        :type PolicyId: str\n        """
        self.Module = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyResponse(AbstractModel):
    """SetDefaultAlarmPolicy response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TagInstance(AbstractModel):
    """Instance tag information of the alarm policy

    """

    def __init__(self):
        """
        :param Key: Tag key
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Key: str\n        :param Value: Tag value
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Value: str\n        :param InstanceSum: Number of instances
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceSum: int\n        :param ServiceType: Service type, for example, CVM
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type ServiceType: str\n        :param RegionId: Region ID
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type RegionId: str\n        :param BindingStatus: Binding status. 2: bound; 1: binding
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type BindingStatus: int\n        :param TagStatus: Tag status. 2: existent; 1: nonexistent
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type TagStatus: int\n        """
        self.Key = None
        self.Value = None
        self.InstanceSum = None
        self.ServiceType = None
        self.RegionId = None
        self.BindingStatus = None
        self.TagStatus = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.InstanceSum = params.get("InstanceSum")
        self.ServiceType = params.get("ServiceType")
        self.RegionId = params.get("RegionId")
        self.BindingStatus = params.get("BindingStatus")
        self.TagStatus = params.get("TagStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class URLNotice(AbstractModel):
    """Cloud Monitor alarm notification template - callback notification details

    """

    def __init__(self):
        """
        :param URL: Callback URL, which can contain up to 256 characters
Note: this field may return null, indicating that no valid values can be obtained.\n        :type URL: str\n        :param IsValid: Whether verification is passed. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsValid: int\n        :param ValidationCode: Verification code
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ValidationCode: str\n        """
        self.URL = None
        self.IsValid = None
        self.ValidationCode = None


    def _deserialize(self, params):
        self.URL = params.get("URL")
        self.IsValid = params.get("IsValid")
        self.ValidationCode = params.get("ValidationCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.\n        :type GroupId: int\n        :param PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.\n        :type PolicyId: str\n        """
        self.Module = None
        self.GroupId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.\n        :type Module: str\n        :param GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.\n        :type GroupId: int\n        :param UniqueId: List of unique IDs of the object instances to be deleted. `UniqueId` can be obtained from the output parameter `List` of the [DescribeBindingPolicyObjectList](https://intl.cloud.tencent.com/document/api/248/40570?from_cn_redirect=1) API\n        :type UniqueId: list of str\n        :param InstanceGroupId: Instance group ID. The `UniqueId` parameter is invalid if object instances are deleted by instance group.\n        :type InstanceGroupId: int\n        :param PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.\n        :type PolicyId: str\n        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None
        self.InstanceGroupId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserNotice(AbstractModel):
    """Cloud Monitor alarm notification template - user notification details

    """

    def __init__(self):
        """
        :param ReceiverType: Recipient type. Valid values: USER (user), GROUP (user group)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReceiverType: str\n        :param StartTime: Notification start time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StartTime: int\n        :param EndTime: Notification end time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EndTime: int\n        :param NoticeWay: Notification channel list. Valid values: EMAIL (email), SMS (SMS), CALL (phone), WECHAT (WeChat)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NoticeWay: list of str\n        :param UserIds: User `uid` list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UserIds: list of int\n        :param GroupIds: User group ID list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GroupIds: list of int\n        :param PhoneOrder: Phone polling list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneOrder: list of int\n        :param PhoneCircleTimes: Number of phone pollings. Value range: 1–5
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneCircleTimes: int\n        :param PhoneInnerInterval: Call interval in seconds within one polling. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneInnerInterval: int\n        :param PhoneCircleInterval: Polling interval in seconds. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PhoneCircleInterval: int\n        :param NeedPhoneArriveNotice: Whether receipt notification is required. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NeedPhoneArriveNotice: int\n        """
        self.ReceiverType = None
        self.StartTime = None
        self.EndTime = None
        self.NoticeWay = None
        self.UserIds = None
        self.GroupIds = None
        self.PhoneOrder = None
        self.PhoneCircleTimes = None
        self.PhoneInnerInterval = None
        self.PhoneCircleInterval = None
        self.NeedPhoneArriveNotice = None


    def _deserialize(self, params):
        self.ReceiverType = params.get("ReceiverType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NoticeWay = params.get("NoticeWay")
        self.UserIds = params.get("UserIds")
        self.GroupIds = params.get("GroupIds")
        self.PhoneOrder = params.get("PhoneOrder")
        self.PhoneCircleTimes = params.get("PhoneCircleTimes")
        self.PhoneInnerInterval = params.get("PhoneInnerInterval")
        self.PhoneCircleInterval = params.get("PhoneCircleInterval")
        self.NeedPhoneArriveNotice = params.get("NeedPhoneArriveNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        