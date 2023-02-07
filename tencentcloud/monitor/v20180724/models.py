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
        :param EventName: Event name
        :type EventName: str
        :param Description: Event display name
        :type Description: str
        :param Namespace: Alarm policy type
        :type Namespace: str
        """
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
        


class AlarmHierarchicalNotice(AbstractModel):
    """Notification template ID and the list of alarm notification levels. The values `Remind` and `Serious` indicate that the notification template only sends alarms at the `Remind` and `Serious` levels.

    """

    def __init__(self):
        r"""
        :param NoticeId: Notification template ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoticeId: str
        :param Classification: The list of alarm notification levels. The values `Remind` and `Serious` indicate that the notification template only sends alarms at the `Remind` and `Serious` levels.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Classification: list of str
        """
        self.NoticeId = None
        self.Classification = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.Classification = params.get("Classification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmHierarchicalValue(AbstractModel):
    """The configuration of alarm level threshold

    """

    def __init__(self):
        r"""
        :param Remind: Threshold for the `Remind` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remind: str
        :param Warn: Threshold for the `Warn` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warn: str
        :param Serious: Threshold for the `Serious` level
Note: This field may return null, indicating that no valid values can be obtained.
        :type Serious: str
        """
        self.Remind = None
        self.Warn = None
        self.Serious = None


    def _deserialize(self, params):
        self.Remind = params.get("Remind")
        self.Warn = params.get("Warn")
        self.Serious = params.get("Serious")
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
        r"""
        :param AlarmId: Alarm record ID
        :type AlarmId: str
        :param MonitorType: Monitor type
        :type MonitorType: str
        :param Namespace: Policy type
        :type Namespace: str
        :param AlarmObject: Alarm object
        :type AlarmObject: str
        :param Content: Alarm content
        :type Content: str
        :param FirstOccurTime: Timestamp of the first occurrence
        :type FirstOccurTime: int
        :param LastOccurTime: Timestamp of the last occurrence
        :type LastOccurTime: int
        :param AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data)
        :type AlarmStatus: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param PolicyName: Policy name
        :type PolicyName: str
        :param VPC: VPC of alarm object for basic product alarm
        :type VPC: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param ProjectName: Project name
        :type ProjectName: str
        :param InstanceGroup: Instance group of alarm object
        :type InstanceGroup: list of InstanceGroups
        :param ReceiverUids: Recipient list
        :type ReceiverUids: list of int
        :param ReceiverGroups: Recipient group list
        :type ReceiverGroups: list of int
        :param NoticeWays: Alarm channel list. Valid values: SMS (SMS), EMAIL (email), CALL (phone), WECHAT (WeChat)
        :type NoticeWays: list of str
        :param OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy
        :type OriginId: str
        :param AlarmType: Alarm type
        :type AlarmType: str
        :param EventId: Event ID
        :type EventId: int
        :param Region: Region
        :type Region: str
        :param PolicyExists: Whether the policy exists. Valid values: 0 (no), 1 (yes)
        :type PolicyExists: int
        :param MetricsInfo: Metric information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricsInfo: list of AlarmHistoryMetric
        :param Dimensions: Dimension information of an instance that triggered alarms.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Dimensions: str
        """
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
        r"""
        :param QceNamespace: Namespace used to query data by Tencent Cloud service monitoring type
        :type QceNamespace: str
        :param MetricName: Metric name
        :type MetricName: str
        :param Period: Statistical period
        :type Period: int
        :param Value: Value triggering alarm
        :type Value: str
        :param Description: Metric display name
        :type Description: str
        """
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
        r"""
        :param Id: Alarm notification template ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param Name: Alarm notification template name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param UpdatedAt: Last modified time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param UpdatedBy: Last modified by
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdatedBy: str
        :param NoticeType: Alarm notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeType: str
        :param UserNotices: User notification list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserNotices: list of UserNotice
        :param URLNotices: Callback notification list
Note: this field may return null, indicating that no valid values can be obtained.
        :type URLNotices: list of URLNotice
        :param IsPreset: Whether it is the system default notification template. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsPreset: int
        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeLanguage: str
        :param PolicyIds: List of IDs of the alarm policies bound to alarm notification template
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyIds: list of str
        :param AMPConsumerId: Backend AMP consumer ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AMPConsumerId: str
        :param CLSNotices: Channel to push alarm notifications to CLS.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CLSNotices: list of CLSNotice
        :param Tags: Tags bound to a notification template
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
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
        self.AMPConsumerId = None
        self.CLSNotices = None
        self.Tags = None


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
        self.AMPConsumerId = params.get("AMPConsumerId")
        if params.get("CLSNotices") is not None:
            self.CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self.CLSNotices.append(obj)
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
        


class AlarmPolicy(AbstractModel):
    """Alarm policy details

    """

    def __init__(self):
        r"""
        :param PolicyId: Alarm policy ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyId: str
        :param PolicyName: Alarm policy name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyName: str
        :param Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MonitorType: str
        :param Enable: Status. Valid values: 0 (disabled), 1 (enabled)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Enable: int
        :param UseSum: Number of instances bound to policy group
Note: this field may return null, indicating that no valid values can be obtained.
        :type UseSum: int
        :param ProjectId: Project ID. Valid values: -1 (no project), 0 (default project)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param ProjectName: Project name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectName: str
        :param Namespace: Alarm policy type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param ConditionTemplateId: Trigger condition template ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConditionTemplateId: str
        :param Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param NoticeIds: Notification rule ID list
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeIds: list of str
        :param Notices: Notification rule list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Notices: list of AlarmNotice
        :param TriggerTasks: Triggered task list
Note: this field may return null, indicating that no valid values can be obtained.
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param ConditionsTemp: Template policy group
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.ConditionsTemp`
        :param LastEditUin: `Uin` of the last modifying user
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastEditUin: str
        :param UpdateTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: int
        :param InsertTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InsertTime: int
        :param Region: Region
Note: this field may return null, indicating that no valid values can be obtained.
        :type Region: list of str
        :param NamespaceShowName: Namespace display name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceShowName: str
        :param IsDefault: Whether it is the default policy. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefault: int
        :param CanSetDefault: Whether the default policy can be set. Valid values: 1 (yes), 0 (no)
Note: this field may return null, indicating that no valid values can be obtained.
        :type CanSetDefault: int
        :param InstanceGroupId: Instance group ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupId: int
        :param InstanceSum: Total number of instances in instance group
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceSum: int
        :param InstanceGroupName: Instance group name
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceGroupName: str
        :param RuleType: Trigger condition type. Valid values: STATIC (static threshold), DYNAMIC (dynamic)
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param OriginId: Policy ID for instance/instance group binding and unbinding APIs (BindingPolicyObject, UnBindingAllPolicyObject, UnBindingPolicyObject)
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginId: str
        :param TagInstances: Tag
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagInstances: list of TagInstance
        :param FilterDimensionsParam: Information on the filter dimension associated with a policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FilterDimensionsParam: str
        :param IsOneClick: Whether it is a quick alarm policy.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOneClick: int
        :param OneClickStatus: Whether the quick alarm policy is enabled.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OneClickStatus: int
        :param AdvancedMetricNumber: The number of advanced metrics.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AdvancedMetricNumber: int
        :param IsBindAll: Whether the policy is associated with all objects
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsBindAll: int
        :param Tags: Policy tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        """
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
        self.FilterDimensionsParam = None
        self.IsOneClick = None
        self.OneClickStatus = None
        self.AdvancedMetricNumber = None
        self.IsBindAll = None
        self.Tags = None


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
        self.FilterDimensionsParam = params.get("FilterDimensionsParam")
        self.IsOneClick = params.get("IsOneClick")
        self.OneClickStatus = params.get("OneClickStatus")
        self.AdvancedMetricNumber = params.get("AdvancedMetricNumber")
        self.IsBindAll = params.get("IsBindAll")
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
        


class AlarmPolicyCondition(AbstractModel):
    """Metric trigger condition of alarm policy

    """

    def __init__(self):
        r"""
        :param IsUnionRule: Metric trigger condition operator. Valid values: 0 (OR), 1 (AND)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsUnionRule: int
        :param Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of AlarmPolicyRule
        """
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
        r"""
        :param Rules: Alarm trigger condition list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rules: list of AlarmPolicyRule
        """
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
        r"""
        :param Type: Filter condition type. Valid values: DIMENSION (uses dimensions for filtering)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param Dimensions: JSON string generated by serializing the `AlarmPolicyDimension` two-dimensional array. The one-dimensional arrays are in OR relationship, and the elements in a one-dimensional array are in AND relationship
Note: this field may return null, indicating that no valid values can be obtained.
        :type Dimensions: str
        """
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
        r"""
        :param MetricName: Metric name or event name. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1) and the supported events via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MetricName: str
        :param Period: Statistical period in seconds. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Period: int
        :param Operator: Operator
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
        :param Value: Threshold. The valid value range can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Value: str
        :param ContinuePeriod: Number of periods. `1`: continue for one period; `2`: continue for two periods; and so on. The valid values can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ContinuePeriod: int
        :param NoticeFrequency: Alarm interval in seconds. Valid values: 0 (do not repeat), 300 (alarm once every 5 minutes), 600 (alarm once every 10 minutes), 900 (alarm once every 15 minutes), 1800 (alarm once every 30 minutes), 3600 (alarm once every hour), 7200 (alarm once every 2 hours), 10800 (alarm once every 3 hours), 21600 (alarm once every 6 hours),  43200 (alarm once every 12 hours), 86400 (alarm once every day)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NoticeFrequency: int
        :param IsPowerNotice: Whether the alarm frequency increases exponentially. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsPowerNotice: int
        :param Filter: Filter condition for one single trigger rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param Description: Metric display name, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Unit: Unit, which is used in the output parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param RuleType: Trigger condition type. `STATIC`: static threshold; `dynamic`: dynamic threshold. If you do not specify this parameter when creating or editing a policy, `STATIC` is used by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleType: str
        :param IsAdvanced: Whether it is an advanced metric. 0: No; 1: Yes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsAdvanced: int
        :param IsOpen: Whether the advanced metric feature is enabled. 0: No; 1: Yes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOpen: int
        :param ProductId: Integration center product ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProductId: str
        :param ValueMax: Maximum value
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValueMax: float
        :param ValueMin: Minimum value
Note: This field may return null, indicating that no valid values can be obtained.
        :type ValueMin: float
        :param HierarchicalValue: The configuration of alarm level threshold
Note: This field may return null, indicating that no valid values can be obtained.
        :type HierarchicalValue: :class:`tencentcloud.monitor.v20180724.models.AlarmHierarchicalValue`
        """
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
        self.IsAdvanced = None
        self.IsOpen = None
        self.ProductId = None
        self.ValueMax = None
        self.ValueMin = None
        self.HierarchicalValue = None


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
        self.IsAdvanced = params.get("IsAdvanced")
        self.IsOpen = params.get("IsOpen")
        self.ProductId = params.get("ProductId")
        self.ValueMax = params.get("ValueMax")
        self.ValueMin = params.get("ValueMin")
        if params.get("HierarchicalValue") is not None:
            self.HierarchicalValue = AlarmHierarchicalValue()
            self.HierarchicalValue._deserialize(params.get("HierarchicalValue"))
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
        r"""
        :param Type: Triggered task type. Valid value: AS (auto scaling)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param TaskConfig: Configuration information in JSON format, such as {"Key1":"Value1","Key2":"Value2"}
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskConfig: str
        """
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
        


class BindPrometheusManagedGrafanaRequest(AbstractModel):
    """BindPrometheusManagedGrafana request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param GrafanaId: Grafana instance ID
        :type GrafanaId: str
        """
        self.InstanceId = None
        self.GrafanaId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPrometheusManagedGrafanaResponse(AbstractModel):
    """BindPrometheusManagedGrafana response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindingPolicyObjectDimension(AbstractModel):
    """Dimensions of instances bound to a policy

    """

    def __init__(self):
        r"""
        :param Region: Region name.
        :type Region: str
        :param RegionId: Region ID.
        :type RegionId: int
        :param Dimensions: Instance dimension information in the following format:
{"unInstanceId":"ins-00jvv9mo"}. The dimension information varies by Tencent Cloud services. For more information, please see:
[Dimension List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)
        :type Dimensions: str
        :param EventDimensions: Event dimensions.
        :type EventDimensions: str
        """
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
        r"""
        :param Module: Required. The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID, such as `4739573`. This parameter will be disused soon. Another parameter `PolicyId` is recommended.
        :type GroupId: int
        :param PolicyId: Alarm policy ID, such as `policy-gh892hg0`. At least one of the two parameters, `PolicyId` and `GroupId`, must be specified; otherwise, an error will be reported. `PolicyId` is preferred over `GroupId` when both of them are specified.
        :type PolicyId: str
        :param InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param Dimensions: Dimensions of an object to be bound.
        :type Dimensions: list of BindingPolicyObjectDimension
        :param EbSubject: The alert configured for an event
        :type EbSubject: str
        :param EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self.Module = None
        self.GroupId = None
        self.PolicyId = None
        self.InstanceGroupId = None
        self.Dimensions = None
        self.EbSubject = None
        self.EbEventFlag = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        self.InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.EbSubject = params.get("EbSubject")
        self.EbEventFlag = params.get("EbEventFlag")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CLSNotice(AbstractModel):
    """The operation of pushing alarm notifications to CLS

    """

    def __init__(self):
        r"""
        :param Region: Region.
        :type Region: str
        :param LogSetId: Logset ID.
        :type LogSetId: str
        :param TopicId: Topic ID.
        :type TopicId: str
        :param Enable: Status. Valid values: `0` (disabled), `1` (enabled). Default value: `1` (enabled). This parameter can be left empty.
        :type Enable: int
        """
        self.Region = None
        self.LogSetId = None
        self.TopicId = None
        self.Enable = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CleanGrafanaInstanceRequest(AbstractModel):
    """CleanGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanGrafanaInstanceResponse(AbstractModel):
    """CleanGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CommonNamespace(AbstractModel):
    """Unified namespace information

    """

    def __init__(self):
        r"""
        :param Id: Namespace ID
        :type Id: str
        :param Name: Namespace name
        :type Name: str
        :param Value: Namespace value
        :type Value: str
        :param ProductName: Product name
        :type ProductName: str
        :param Config: Configuration information
        :type Config: str
        :param AvailableRegions: List of supported regions
        :type AvailableRegions: list of str
        :param SortId: Sort ID
        :type SortId: int
        :param DashboardId: Unique ID in Dashboard
        :type DashboardId: str
        """
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
        


class CommonNamespaceNew(AbstractModel):
    """Policy type information

    """

    def __init__(self):
        r"""
        :param Id: Namespace ID
        :type Id: str
        :param Name: Namespace name
        :type Name: str
        :param MonitorType: Monitoring type
        :type MonitorType: str
        :param Dimensions: Dimension information
        :type Dimensions: list of DimensionNew
        """
        self.Id = None
        self.Name = None
        self.MonitorType = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MonitorType = params.get("MonitorType")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionNew()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Condition(AbstractModel):
    """Alarm condition

    """

    def __init__(self):
        r"""
        :param AlarmNotifyPeriod: Alarm notification frequency.
        :type AlarmNotifyPeriod: int
        :param AlarmNotifyType: Predefined repeated notification policy. `0`: One-time alarm; `1`: exponential alarm; `2`: consecutive alarm.
        :type AlarmNotifyType: int
        :param CalcType: Detection method.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CalcType: str
        :param CalcValue: Detection value.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CalcValue: str
        :param ContinueTime: Duration in seconds.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContinueTime: str
        :param MetricID: Metric ID.
        :type MetricID: int
        :param MetricDisplayName: Displayed metric name.
        :type MetricDisplayName: str
        :param Period: Statistical period.
        :type Period: int
        :param RuleID: Rule ID.
        :type RuleID: int
        :param Unit: Metric unit.
        :type Unit: str
        :param IsAdvanced: Whether it is an advanced metric. Valid values: `0` (no), `1` (yes).
        :type IsAdvanced: int
        :param IsOpen: Whether the advance metric feature is enabled. Valid values: `0` (no), `1` (yes).
        :type IsOpen: int
        :param ProductId: Product ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductId: str
        """
        self.AlarmNotifyPeriod = None
        self.AlarmNotifyType = None
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.MetricID = None
        self.MetricDisplayName = None
        self.Period = None
        self.RuleID = None
        self.Unit = None
        self.IsAdvanced = None
        self.IsOpen = None
        self.ProductId = None


    def _deserialize(self, params):
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.ContinueTime = params.get("ContinueTime")
        self.MetricID = params.get("MetricID")
        self.MetricDisplayName = params.get("MetricDisplayName")
        self.Period = params.get("Period")
        self.RuleID = params.get("RuleID")
        self.Unit = params.get("Unit")
        self.IsAdvanced = params.get("IsAdvanced")
        self.IsOpen = params.get("IsOpen")
        self.ProductId = params.get("ProductId")
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
        r"""
        :param TemplateName: Template name
Note: this field may return null, indicating that no valid values can be obtained.
        :type TemplateName: str
        :param Condition: Metric trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: Event trigger condition
Note: this field may return null, indicating that no valid values can be obtained.
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param Name: Notification template name, which can contain up to 60 characters
        :type Name: str
        :param NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
        :type NoticeType: str
        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
        :type NoticeLanguage: str
        :param UserNotices: User notifications (up to 5)
        :type UserNotices: list of UserNotice
        :param URLNotices: Callback notifications (up to 3)
        :type URLNotices: list of URLNotice
        :param CLSNotices: The operation of pushing alarm notifications to CLS. Up to one CLS log topic can be configured.
        :type CLSNotices: list of CLSNotice
        :param Tags: Tags bound to a template
        :type Tags: list of Tag
        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.UserNotices = None
        self.URLNotices = None
        self.CLSNotices = None
        self.Tags = None


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
        if params.get("CLSNotices") is not None:
            self.CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self.CLSNotices.append(obj)
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
        


class CreateAlarmNoticeResponse(AbstractModel):
    """CreateAlarmNotice response structure.

    """

    def __init__(self):
        r"""
        :param NoticeId: Alarm notification template ID
        :type NoticeId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NoticeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.RequestId = params.get("RequestId")


class CreateAlarmPolicyRequest(AbstractModel):
    """CreateAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param PolicyName: Policy name, which can contain up to 20 characters
        :type PolicyName: str
        :param MonitorType: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorType: str
        :param Namespace: Type of alarm policy, which can be obtained via [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1). For the monitoring of Tencent Cloud services, the value of this parameter is `QceNamespacesNew.N.Id` of the output parameter of `DescribeAllNamespaces`, for example, `cvm_device`.
        :type Namespace: str
        :param Remark: Remarks with up to 100 letters, digits, underscores, and hyphens
        :type Remark: str
        :param Enable: Whether to enable. Valid values: 0 (no), 1 (yes). Default value: 1. This parameter can be left empty
        :type Enable: int
        :param ProjectId: Project ID. For products with different projects, a value other than `-1` must be passed in. `-1`: no project; `0`: default project. If no value is passed in, `-1` will be used. The supported project IDs can be viewed on the [**Account Center** > **Project Management**](https://console.cloud.tencent.com/project) page of the console.
        :type ProjectId: int
        :param ConditionTemplateId: Trigger condition template ID. Pass in this parameter if the policy is associated with the trigger condition template; otherwise, pass in the `Condition` parameter. The trigger condition template ID can be obtained via [`DescribeConditionsTemplateList`](https://intl.cloud.tencent.com/document/api/248/70250?from_cn_redirect=1).
        :type ConditionTemplateId: int
        :param Condition: Metric trigger condition. The supported metrics can be queried via [DescribeAlarmMetrics](https://intl.cloud.tencent.com/document/product/248/51283?from_cn_redirect=1).
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: Event trigger condition. The supported events can be queried via [DescribeAlarmEvents](https://intl.cloud.tencent.com/document/product/248/51284?from_cn_redirect=1).
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param NoticeIds: List of notification rule IDs, which can be obtained via [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1)
        :type NoticeIds: list of str
        :param TriggerTasks: Triggered task list
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param Filter: Global filter.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.
        :type GroupBy: list of str
        :param Tags: Tags bound to a template
        :type Tags: list of Tag
        :param LogAlarmReqInfo: Log alarm information
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param HierarchicalNotices: Notification rules for different alarm levels
        :type HierarchicalNotices: list of AlarmHierarchicalNotice
        :param MigrateFlag: A dedicated field for migration policies. 0: Implement authentication logic; 1: Skip authentication logic.
        :type MigrateFlag: int
        :param EbSubject: The alert configured for an event
        :type EbSubject: str
        """
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
        self.Tags = None
        self.LogAlarmReqInfo = None
        self.HierarchicalNotices = None
        self.MigrateFlag = None
        self.EbSubject = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("LogAlarmReqInfo") is not None:
            self.LogAlarmReqInfo = LogAlarmReq()
            self.LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        if params.get("HierarchicalNotices") is not None:
            self.HierarchicalNotices = []
            for item in params.get("HierarchicalNotices"):
                obj = AlarmHierarchicalNotice()
                obj._deserialize(item)
                self.HierarchicalNotices.append(obj)
        self.MigrateFlag = params.get("MigrateFlag")
        self.EbSubject = params.get("EbSubject")
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
        r"""
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param OriginId: Alarm policy ID, which can be used when you call APIs ([BindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40421?from_cn_redirect=1), [UnBindingAllPolicyObject](https://intl.cloud.tencent.com/document/product/248/40568?from_cn_redirect=1), [UnBindingPolicyObject](https://intl.cloud.tencent.com/document/product/248/40567?from_cn_redirect=1)) to bind/unbind instances or instance groups to/from an alarm policy
        :type OriginId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class CreateAlertRuleRequest(AbstractModel):
    """CreateAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param RuleName: Rule name
        :type RuleName: str
        :param Expr: Alerting rule expression. For more information, see <a href="https://www.tencentcloud.com/document/product/1116/43192?lang=en&pg=">Alerting Rule Description</a>
        :type Expr: str
        :param Receivers: List of alert notification template IDs
        :type Receivers: list of str
        :param RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param Duration: Rule alert duration
        :type Duration: str
        :param Labels: List of tags
        :type Labels: list of PrometheusRuleKV
        :param Annotations: List of annotations.

Alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively.
        :type Annotations: list of PrometheusRuleKV
        :param Type: Alerting rule template category
        :type Type: str
        """
        self.InstanceId = None
        self.RuleName = None
        self.Expr = None
        self.Receivers = None
        self.RuleState = None
        self.Duration = None
        self.Labels = None
        self.Annotations = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")
        self.Expr = params.get("Expr")
        self.Receivers = params.get("Receivers")
        self.RuleState = params.get("RuleState")
        self.Duration = params.get("Duration")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertRuleResponse(AbstractModel):
    """CreateAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateExporterIntegrationRequest(AbstractModel):
    """CreateExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Kind: Type
        :type Kind: str
        :param Content: Integrated configuration
        :type Content: str
        :param KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.InstanceId = None
        self.Kind = None
        self.Content = None
        self.KubeType = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        self.KubeType = params.get("KubeType")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExporterIntegrationResponse(AbstractModel):
    """CreateExporterIntegration response structure.

    """

    def __init__(self):
        r"""
        :param Names: The list of successfully created integrations.
        :type Names: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Names = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.RequestId = params.get("RequestId")


class CreateGrafanaInstanceRequest(AbstractModel):
    """CreateGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceName: Instance name
        :type InstanceName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param GrafanaInitPassword: Initial Grafana password
        :type GrafanaInitPassword: str
        :param EnableInternet: Whether to enable public network access
        :type EnableInternet: bool
        :param TagSpecification: Tag
        :type TagSpecification: list of PrometheusTag
        """
        self.InstanceName = None
        self.VpcId = None
        self.SubnetIds = None
        self.GrafanaInitPassword = None
        self.EnableInternet = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.GrafanaInitPassword = params.get("GrafanaInitPassword")
        self.EnableInternet = params.get("EnableInternet")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaInstanceResponse(AbstractModel):
    """CreateGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance name
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CreateGrafanaIntegrationRequest(AbstractModel):
    """CreateGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param Kind: Integration type, such as “tencent-cloud-prometheus”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type Kind: str
        :param Content: Integration configuration
        :type Content: str
        """
        self.InstanceId = None
        self.Kind = None
        self.Content = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaIntegrationResponse(AbstractModel):
    """CreateGrafanaIntegration response structure.

    """

    def __init__(self):
        r"""
        :param IntegrationId: Integration ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntegrationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IntegrationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntegrationId = params.get("IntegrationId")
        self.RequestId = params.get("RequestId")


class CreateGrafanaNotificationChannelRequest(AbstractModel):
    """CreateGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param OrgId: Default value: `1`. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type OrgId: int
        :param Receivers: Array of notification channel IDs
        :type Receivers: list of str
        :param ExtraOrgIds: Array of extra organization IDs. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type ExtraOrgIds: list of str
        :param OrganizationIds: Array of all valid organization IDs. Default value: `1`.
        :type OrganizationIds: list of str
        """
        self.InstanceId = None
        self.ChannelName = None
        self.OrgId = None
        self.Receivers = None
        self.ExtraOrgIds = None
        self.OrganizationIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ChannelName = params.get("ChannelName")
        self.OrgId = params.get("OrgId")
        self.Receivers = params.get("Receivers")
        self.ExtraOrgIds = params.get("ExtraOrgIds")
        self.OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGrafanaNotificationChannelResponse(AbstractModel):
    """CreateGrafanaNotificationChannel response structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChannelId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ChannelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """Alarm threshold condition passed in when a policy is created.

    """

    def __init__(self):
        r"""
        :param MetricId: Metric ID.
        :type MetricId: int
        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. This parameter is optional if a default comparative type is configured for the metric.
        :type CalcType: int
        :param CalcValue: Comparative value. This parameter is optional if the metric has no requirement.
        :type CalcValue: float
        :param CalcPeriod: Data aggregation period in seconds. This parameter is optional if the metric has a default value.
        :type CalcPeriod: int
        :param ContinuePeriod: Number of consecutive periods after which an alarm will be triggered.
        :type ContinuePeriod: int
        :param RuleId: If a metric is created based on a template, the RuleId of the metric in the template must be passed in.
        :type RuleId: int
        """
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
        r"""
        :param EventId: Alarm event ID.
        :type EventId: int
        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param RuleId: If a metric is created based on a template, the RuleId of the metric in the template must be passed in.
        :type RuleId: int
        """
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
        r"""
        :param GroupName: Policy group name.
        :type GroupName: str
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param ViewName: Name of the view to which the policy group belongs. If the policy group is created based on a template, this parameter is optional.
        :type ViewName: str
        :param ProjectId: ID of the project to which the policy group belongs, which will be used for authentication.
        :type ProjectId: int
        :param ConditionTempGroupId: ID of a template-based policy group. This parameter is required only when the policy group is created based on a template.
        :type ConditionTempGroupId: int
        :param IsShielded: Whether the policy group is shielded. The value 0 indicates that the policy group is not shielded. The value 1 indicates that the policy group is shielded. The default value is 0.
        :type IsShielded: int
        :param Remark: Remarks of the policy group.
        :type Remark: str
        :param InsertTime: Insertion time in the format of Unix timestamp. If this parameter is not configured, the backend processing time is used.
        :type InsertTime: int
        :param Conditions: Alarm threshold rules in the policy group.
        :type Conditions: list of CreatePolicyGroupCondition
        :param EventConditions: Event alarm rules in the policy group.
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param BackEndCall: Whether it is a backend call. If the value is 1, rules from the policy template will be used to fill in the `Conditions` and `EventConditions` fields.
        :type BackEndCall: int
        :param IsUnionRule: The 'AND' and 'OR' rules for alarm metrics. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met.
        :type IsUnionRule: int
        """
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
        r"""
        :param GroupId: ID of the created policy group.
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusAgentRequest(AbstractModel):
    """CreatePrometheusAgent request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Agent name
        :type Name: str
        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAgentResponse(AbstractModel):
    """CreatePrometheusAgent response structure.

    """

    def __init__(self):
        r"""
        :param AgentId: ID of a successfully created agent.
        :type AgentId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AgentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusMultiTenantInstancePostPayModeRequest(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode request structure.

    """

    def __init__(self):
        r"""
        :param InstanceName: Instance name
        :type InstanceName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param DataRetentionTime: Data retention period in days. Valid values: 15, 30, 45.
        :type DataRetentionTime: int
        :param Zone: AZ
        :type Zone: str
        :param TagSpecification: Instance tag
        :type TagSpecification: list of PrometheusTag
        :param GrafanaInstanceId: The Grafana instance to be associated
        :type GrafanaInstanceId: str
        """
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.DataRetentionTime = None
        self.Zone = None
        self.TagSpecification = None
        self.GrafanaInstanceId = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DataRetentionTime = params.get("DataRetentionTime")
        self.Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.GrafanaInstanceId = params.get("GrafanaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusMultiTenantInstancePostPayModeResponse(AbstractModel):
    """CreatePrometheusMultiTenantInstancePostPayMode response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusRecordRuleYamlRequest(AbstractModel):
    """CreatePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Content: YAML content
        :type Content: str
        """
        self.InstanceId = None
        self.Content = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusRecordRuleYamlResponse(AbstractModel):
    """CreatePrometheusRecordRuleYaml response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePrometheusScrapeJobRequest(AbstractModel):
    """CreatePrometheusScrapeJob request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param AgentId: Agent ID, such as “agent-abcd1234”. It can be obtained on the **Agent Management** page in the console.
        :type AgentId: str
        :param Config: Scrape task ID in the format of “job_name:xx”
        :type Config: str
        """
        self.InstanceId = None
        self.AgentId = None
        self.Config = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentId = params.get("AgentId")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusScrapeJobResponse(AbstractModel):
    """CreatePrometheusScrapeJob response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of a successfully created scrape task.
        :type JobId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusTempRequest(AbstractModel):
    """CreatePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param Template: Template settings
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTemp`
        """
        self.Template = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = PrometheusTemp()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTempResponse(AbstractModel):
    """CreatePrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID
        :type TemplateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateRecordingRuleRequest(AbstractModel):
    """CreateRecordingRule request structure.

    """

    def __init__(self):
        r"""
        :param Name: Recording rule name
        :type Name: str
        :param Group: Recording rule group content in YAML format
        :type Group: str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self.Name = None
        self.Group = None
        self.InstanceId = None
        self.RuleState = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Group = params.get("Group")
        self.InstanceId = params.get("InstanceId")
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordingRuleResponse(AbstractModel):
    """CreateRecordingRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateSSOAccountRequest(AbstractModel):
    """CreateSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param UserId: User account ID, such as “10000000”.
        :type UserId: str
        :param Role: Permission
        :type Role: list of GrafanaAccountRole
        :param Notes: Remarks
        :type Notes: str
        """
        self.InstanceId = None
        self.UserId = None
        self.Role = None
        self.Notes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserId = params.get("UserId")
        if params.get("Role") is not None:
            self.Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self.Role.append(obj)
        self.Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSOAccountResponse(AbstractModel):
    """CreateSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param UserId: The added user UIN
        :type UserId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class CreateServiceDiscoveryRequest(AbstractModel):
    """CreateServiceDiscovery request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param KubeClusterId: <li>TKE: ID of the integrated TKE cluster</li>
        :type KubeClusterId: str
        :param KubeType: Kubernetes cluster type:
<li> 1 = TKE </li>
        :type KubeType: int
        :param Type: Scrape configuration type. Valid values:
<li> 1 = ServiceMonitor</li>
<li> 2 = PodMonitor</li>
<li> 3 = JobMonitor</li>
        :type Type: int
        :param Yaml: Scrape configuration information
        :type Yaml: str
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None
        self.Type = None
        self.Yaml = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        self.Type = params.get("Type")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceDiscoveryResponse(AbstractModel):
    """CreateServiceDiscovery response structure.

    """

    def __init__(self):
        r"""
        :param ServiceDiscovery: The scrape configuration information returned after successful creation
        :type ServiceDiscovery: :class:`tencentcloud.monitor.v20180724.models.ServiceDiscoveryItem`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceDiscovery = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceDiscovery") is not None:
            self.ServiceDiscovery = ServiceDiscoveryItem()
            self.ServiceDiscovery._deserialize(params.get("ServiceDiscovery"))
        self.RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        r"""
        :param Dimensions: Combination of instance object dimensions
        :type Dimensions: list of Dimension
        :param Timestamps: The array of timestamps indicating at which points in time there is data. Missing timestamps have no data points (i.e., missed)
        :type Timestamps: list of float
        :param Values: The array of monitoring values, which is in one-to-one correspondence to Timestamps
        :type Values: list of float
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param NoticeIds: Alarm notification template ID list
        :type NoticeIds: list of str
        :param NoticeBindPolicys: Binding between a notification template and a policy
        :type NoticeBindPolicys: list of NoticeBindPolicys
        """
        self.Module = None
        self.NoticeIds = None
        self.NoticeBindPolicys = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.NoticeIds = params.get("NoticeIds")
        if params.get("NoticeBindPolicys") is not None:
            self.NoticeBindPolicys = []
            for item in params.get("NoticeBindPolicys"):
                obj = NoticeBindPolicys()
                obj._deserialize(item)
                self.NoticeBindPolicys.append(obj)
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAlarmPolicyRequest(AbstractModel):
    """DeleteAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param PolicyIds: Alarm policy ID list
        :type PolicyIds: list of str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAlertRulesRequest(AbstractModel):
    """DeleteAlertRules request structure.

    """

    def __init__(self):
        r"""
        :param RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        """
        self.RuleIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertRulesResponse(AbstractModel):
    """DeleteAlertRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteExporterIntegrationRequest(AbstractModel):
    """DeleteExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Kind: Type
        :type Kind: str
        :param Name: Name
        :type Name: str
        """
        self.InstanceId = None
        self.KubeType = None
        self.ClusterId = None
        self.Kind = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeType = params.get("KubeType")
        self.ClusterId = params.get("ClusterId")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExporterIntegrationResponse(AbstractModel):
    """DeleteExporterIntegration response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGrafanaInstanceRequest(AbstractModel):
    """DeleteGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIDs: Array of instance names
        :type InstanceIDs: list of str
        """
        self.InstanceIDs = None


    def _deserialize(self, params):
        self.InstanceIDs = params.get("InstanceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaInstanceResponse(AbstractModel):
    """DeleteGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGrafanaIntegrationRequest(AbstractModel):
    """DeleteGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param IntegrationId: Integration ID, such as “integration-abcd1234”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type IntegrationId: str
        """
        self.InstanceId = None
        self.IntegrationId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IntegrationId = params.get("IntegrationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaIntegrationResponse(AbstractModel):
    """DeleteGrafanaIntegration response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGrafanaNotificationChannelRequest(AbstractModel):
    """DeleteGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param ChannelIDs: Array of channel IDs, such as “nchannel-abcd1234”.
        :type ChannelIDs: list of str
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.ChannelIDs = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ChannelIDs = params.get("ChannelIDs")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGrafanaNotificationChannelResponse(AbstractModel):
    """DeleteGrafanaNotificationChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup request structure.

    """

    def __init__(self):
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: list of int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusRecordRuleYamlRequest(AbstractModel):
    """DeletePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Names: List of recording rules
        :type Names: list of str
        """
        self.InstanceId = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusRecordRuleYamlResponse(AbstractModel):
    """DeletePrometheusRecordRuleYaml response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusScrapeJobsRequest(AbstractModel):
    """DeletePrometheusScrapeJobs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AgentId: Agent ID
        :type AgentId: str
        :param JobIds: List of task IDs
        :type JobIds: list of str
        """
        self.InstanceId = None
        self.AgentId = None
        self.JobIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentId = params.get("AgentId")
        self.JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusScrapeJobsResponse(AbstractModel):
    """DeletePrometheusScrapeJobs response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTempRequest(AbstractModel):
    """DeletePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempResponse(AbstractModel):
    """DeletePrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTempSyncRequest(AbstractModel):
    """DeletePrometheusTempSync request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID
        :type TemplateId: str
        :param Targets: List of unsynced objects
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self.TemplateId = None
        self.Targets = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempSyncResponse(AbstractModel):
    """DeletePrometheusTempSync response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordingRulesRequest(AbstractModel):
    """DeleteRecordingRules request structure.

    """

    def __init__(self):
        r"""
        :param RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        """
        self.RuleIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordingRulesResponse(AbstractModel):
    """DeleteRecordingRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSSOAccountRequest(AbstractModel):
    """DeleteSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param UserId: User account ID, such as “10000000”.
        :type UserId: str
        """
        self.InstanceId = None
        self.UserId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSSOAccountResponse(AbstractModel):
    """DeleteSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccidentEventListAlarms(AbstractModel):
    """Output parameter type of the DescribeAccidentEventList API

    """

    def __init__(self):
        r"""
        :param BusinessTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type BusinessTypeDesc: str
        :param AccidentTypeDesc: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type AccidentTypeDesc: str
        :param BusinessID: ID of the event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.
Note: This field may return null, indicating that no valid value was found.
        :type BusinessID: int
        :param EventStatus: Event status ID. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.
Note: This field may return null, indicating that no valid value was found.
        :type EventStatus: int
        :param AffectResource: Affected object.
Note: This field may return null, indicating that no valid value was found.
        :type AffectResource: str
        :param Region: Region where the event occurs.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param OccurTime: Time when the event occurs.
Note: This field may return null, indicating that no valid value was found.
        :type OccurTime: str
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: str
        """
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
        r"""
        :param Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.
        :type Limit: int
        :param Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.
        :type Offset: int
        :param UpdateTimeOrder: Sorting rule by UpdateTime. Valid values: asc and desc.
        :type UpdateTimeOrder: str
        :param OccurTimeOrder: Sorting rule by OccurTime. Valid values: asc or desc. Sorting by UpdateTimeOrder takes priority.
        :type OccurTimeOrder: str
        :param AccidentType: Filter by event type. The value 1 indicates service issues. The value 2 indicates other subscriptions.
        :type AccidentType: list of int
        :param AccidentEvent: Filter by event. The value 1 indicates CVM storage issues. The value 2 indicates CVM network connection issues. The value 3 indicates that the CVM has an exception. The value 202 indicates that an ISP network jitter occurs.
        :type AccidentEvent: list of int
        :param AccidentStatus: Filter by event status. The value 0 indicates that the event has been recovered. The value 1 indicates that the event has not been recovered.
        :type AccidentStatus: list of int
        :param AccidentRegion: Filter by region where the event occurs. The value gz indicates Guangzhou. The value sh indicates Shanghai.
        :type AccidentRegion: list of str
        :param AffectResource: Filter by affected resource, such as ins-19a06bka.
        :type AffectResource: str
        """
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
        r"""
        :param Alarms: Platform event list.
Note: This field may return null, indicating that no valid value was found.
        :type Alarms: list of DescribeAccidentEventListAlarms
        :param Total: Total number of platform events.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API
        :type Namespace: str
        :param MonitorType: Monitoring type, such as `MT_QCE`, which is set to default.
        :type MonitorType: str
        """
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
        r"""
        :param Events: Alarm event list
        :type Events: list of AlarmEvent
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param PageNumber: Page number starting from 1. Default value: 1
        :type PageNumber: int
        :param PageSize: Number of entries per page. Value range: 1–100. Default value: 20
        :type PageSize: int
        :param Order: Sort by the first occurrence time in descending order by default. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param StartTime: Start time, which is the timestamp one day ago by default and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is later than the `StartTime`.
        :type StartTime: int
        :param EndTime: End time, which is the current timestamp and the time when the alarm `FirstOccurTime` first occurs. An alarm record can be searched only if its `FirstOccurTime` is earlier than the `EndTime`.
        :type EndTime: int
        :param MonitorTypes: Filter by monitor type. Valid values: "MT_QCE" (Tencent Cloud service monitoring), "MT_TAW" (application performance monitoring), "MT_RUM" (frontend performance monitoring), "MT_PROBE" (cloud automated testing). If this parameter is left empty, all types will be queried by default.
        :type MonitorTypes: list of str
        :param AlarmObject: Filter by alarm object. Fuzzy search with string is supported
        :type AlarmObject: str
        :param AlarmStatus: Filter by alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_CONF (expired), NO_DATA (insufficient data). If this parameter is left empty, all will be queried by default
        :type AlarmStatus: list of str
        :param ProjectIds: Filter by project ID. Valid values: `-1` (no project), `0` (default project)
        :type ProjectIds: list of int
        :param InstanceGroupIds: Filter by instance group ID
        :type InstanceGroupIds: list of int
        :param Namespaces: Filter by policy type. Monitoring type and policy type are first-level and second-level filters respectively and both need to be passed in. For example, `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`
        :type Namespaces: list of MonitorTypeNamespace
        :param MetricNames: Filter by metric name
        :type MetricNames: list of str
        :param PolicyName: Fuzzy search by policy name
        :type PolicyName: str
        :param Content: Fuzzy search by alarm content
        :type Content: str
        :param ReceiverUids: Search by recipient
        :type ReceiverUids: list of int
        :param ReceiverGroups: Search by recipient group
        :type ReceiverGroups: list of int
        :param PolicyIds: Search by alarm policy ID list
        :type PolicyIds: list of str
        """
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
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Histories: Alarm record list
        :type Histories: list of AlarmHistory
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param MonitorType: Monitor type filter. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorType: str
        :param Namespace: Alarm policy type such as cvm_device, which is obtained through the `DescribeAllNamespaces` API
        :type Namespace: str
        """
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
        r"""
        :param Metrics: Alarm metric list
        :type Metrics: list of Metric
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        """
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
        r"""
        :param URLNotices: Alarm callback notification
Note: this field may return null, indicating that no valid values can be obtained.
        :type URLNotices: list of URLNotice
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param NoticeId: Alarm notification template ID
        :type NoticeId: str
        """
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
        r"""
        :param Notice: Alarm notification template details
        :type Notice: :class:`tencentcloud.monitor.v20180724.models.AlarmNotice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param PageNumber: Page number. Minimum value: 1
        :type PageNumber: int
        :param PageSize: Number of entries per page. Value range: 1–200
        :type PageSize: int
        :param Order: Sort by update time. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param OwnerUid: Root account `uid`, which is used to create preset notifications
        :type OwnerUid: int
        :param Name: Alarm notification template name, which is used for fuzzy search
        :type Name: str
        :param ReceiverType: Filter by recipient. The type of notified users should be selected for the alarm notification template. Valid values: USER (user), GROUP (user group). If this parameter is left empty, no filter by recipient will be performed
        :type ReceiverType: str
        :param UserIds: Recipient object list
        :type UserIds: list of int
        :param GroupIds: Recipient group list
        :type GroupIds: list of int
        :param NoticeIds: Filter by notification template ID. If an empty array is passed in or if this parameter is left empty, the filter operation will not be performed.
        :type NoticeIds: list of str
        :param Tags: Filter templates by tag
        :type Tags: list of Tag
        """
        self.Module = None
        self.PageNumber = None
        self.PageSize = None
        self.Order = None
        self.OwnerUid = None
        self.Name = None
        self.ReceiverType = None
        self.UserIds = None
        self.GroupIds = None
        self.NoticeIds = None
        self.Tags = None


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
        self.NoticeIds = params.get("NoticeIds")
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
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of alarm notification templates
        :type TotalCount: int
        :param Notices: Alarm notification template list
        :type Notices: list of AlarmNotice
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param PageNumber: Page number starting from 1. Default value: 1
        :type PageNumber: int
        :param PageSize: Number of entries per page. Value range: 1–100. Default value: 20
        :type PageSize: int
        :param PolicyName: Fuzzy search by policy name
        :type PolicyName: str
        :param MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default
        :type MonitorTypes: list of str
        :param Namespaces: Filter by namespace. For the values of different policy types, please see:
[Policy Type List](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1)
        :type Namespaces: list of str
        :param Dimensions: The alarm object list, which is a JSON string. The outer array corresponds to multiple instances, and the inner array is the dimension of an object. For example, “CVM - Basic Monitor” can be written as:
`[ {"Dimensions": {"unInstanceId": "ins-qr8d555g"}}, {"Dimensions": {"unInstanceId": "ins-qr8d555h"}} ]`
You can also refer to the “Example 2” below.

For more information on the parameter samples of different Tencent Cloud services, see [Product Policy Type and Dimension Information](https://intl.cloud.tencent.com/document/product/248/50397?from_cn_redirect=1).

Note: If `1` is passed in for `NeedCorrespondence`, the relationship between a policy and an instance needs to be returned. You can pass in up to 20 alarm object dimensions to avoid request timeout.
        :type Dimensions: str
        :param ReceiverUids: Search by recipient. You can get the user list with the API [ListUsers](https://intl.cloud.tencent.com/document/product/598/34587?from_cn_redirect=1) in “Cloud Access Management” or query the sub-user information with the API [GetUser](https://intl.cloud.tencent.com/document/product/598/34590?from_cn_redirect=1). The `Uid` field in the returned result should be entered here.
        :type ReceiverUids: list of int
        :param ReceiverGroups: Search by recipient group. You can get the user group list with the API [ListGroups](https://intl.cloud.tencent.com/document/product/598/34589?from_cn_redirect=1) in “Cloud Access Management” or query the user group list where a sub-user is in with the API [ListGroupsForUser](https://intl.cloud.tencent.com/document/product/598/34588?from_cn_redirect=1). The `GroupId` field in the returned result should be entered here.
        :type ReceiverGroups: list of int
        :param PolicyType: Filter by default policy. Valid values: DEFAULT (display default policy), NOT_DEFAULT (display non-default policies). If this parameter is left empty, all policies will be displayed
        :type PolicyType: list of str
        :param Field: Sort by field. For example, to sort by the last modification time, use Field: "UpdateTime".
        :type Field: str
        :param Order: Sort order. Valid values: ASC (ascending), DESC (descending)
        :type Order: str
        :param ProjectIds: ID array of the policy project, which can be viewed on the following page:
[Project Management](https://console.cloud.tencent.com/project)
        :type ProjectIds: list of int
        :param NoticeIds: ID list of the notification template, which can be obtained by querying the notification template list.
It can be queried with the API [DescribeAlarmNotices](https://intl.cloud.tencent.com/document/product/248/51280?from_cn_redirect=1).
        :type NoticeIds: list of str
        :param RuleTypes: Filter by trigger condition. Valid values: STATIC (display policies with static threshold), DYNAMIC (display policies with dynamic threshold). If this parameter is left empty, all policies will be displayed
        :type RuleTypes: list of str
        :param Enable: Filter by alarm status. Valid values: [1]: enabled; [0]: disabled; [0, 1]: all
        :type Enable: list of int
        :param NotBindingNoticeRule: If `1` is passed in, alarm policies with no notification rules configured are queried. If it is left empty or other values are passed in, all alarm policies are queried.
        :type NotBindingNoticeRule: int
        :param InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param NeedCorrespondence: Whether the relationship between a policy and the input parameter filter dimension is required. `1`: Yes. `0`: No. Default value: `0`.
        :type NeedCorrespondence: int
        :param TriggerTasks: Filter alarm policy by triggered task (such as auto scaling task). Up to 10 tasks can be specified.
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        :param OneClickPolicyType: Filter by quick alarm policy. If this parameter is left empty, all policies are displayed. `ONECLICK`: Display quick alarm policies; `NOT_ONECLICK`: Display non-quick alarm policies.
        :type OneClickPolicyType: list of str
        :param NotBindAll: Whether the returned result filters policies associated with all objects. Valid values: `1` (Yes), `0` (No).
        :type NotBindAll: int
        :param NotInstanceGroup: Whether the returned result filters policies associated with instance groups. Valid values: `1` (Yes), `0` (No).
        :type NotInstanceGroup: int
        :param Tags: Filter policies by tag
        :type Tags: list of Tag
        """
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
        self.InstanceGroupId = None
        self.NeedCorrespondence = None
        self.TriggerTasks = None
        self.OneClickPolicyType = None
        self.NotBindAll = None
        self.NotInstanceGroup = None
        self.Tags = None


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
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.NeedCorrespondence = params.get("NeedCorrespondence")
        if params.get("TriggerTasks") is not None:
            self.TriggerTasks = []
            for item in params.get("TriggerTasks"):
                obj = AlarmPolicyTriggerTask()
                obj._deserialize(item)
                self.TriggerTasks.append(obj)
        self.OneClickPolicyType = params.get("OneClickPolicyType")
        self.NotBindAll = params.get("NotBindAll")
        self.NotInstanceGroup = params.get("NotInstanceGroup")
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
        


class DescribeAlarmPoliciesResponse(AbstractModel):
    """DescribeAlarmPolicies response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of policies
        :type TotalCount: int
        :param Policies: Policy array
        :type Policies: list of AlarmPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        """
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
        r"""
        :param Policy: Policy details
        :type Policy: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicy`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Policy = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = AlarmPolicy()
            self.Policy._deserialize(params.get("Policy"))
        self.RequestId = params.get("RequestId")


class DescribeAlertRulesRequest(AbstractModel):
    """DescribeAlertRules request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param RuleId: Rule ID
        :type RuleId: str
        :param RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param RuleName: Rule name
        :type RuleName: str
        :param Type: Alerting rule template category
        :type Type: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.RuleId = None
        self.RuleState = None
        self.RuleName = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleId = params.get("RuleId")
        self.RuleState = params.get("RuleState")
        self.RuleName = params.get("RuleName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRulesResponse(AbstractModel):
    """DescribeAlertRules response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of alerting rules
        :type TotalCount: int
        :param AlertRuleSet: Alerting rule details
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRuleSet: list of PrometheusRuleSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AlertRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AlertRuleSet") is not None:
            self.AlertRuleSet = []
            for item in params.get("AlertRuleSet"):
                obj = PrometheusRuleSet()
                obj._deserialize(item)
                self.AlertRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllNamespacesRequest(AbstractModel):
    """DescribeAllNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param SceneType: Filter by use case. Currently, the only valid value is `ST_ALARM` (alarm type).
        :type SceneType: str
        :param Module: Value fixed at "monitor"
        :type Module: str
        :param MonitorTypes: Filter by monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring). If this parameter is left empty, all will be queried by default
        :type MonitorTypes: list of str
        :param Ids: Filter by namespace ID. If this parameter is left empty, all will be queried
        :type Ids: list of str
        """
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
        r"""
        :param QceNamespaces: Alarm policy type of Tencent Cloud service (disused)
        :type QceNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param CustomNamespaces: Other alarm policy type (disused)
        :type CustomNamespaces: :class:`tencentcloud.monitor.v20180724.models.CommonNamespace`
        :param QceNamespacesNew: Alarm policy type of Tencent Cloud service
        :type QceNamespacesNew: list of CommonNamespace
        :param CustomNamespacesNew: Other alarm policy type (not supported currently)
        :type CustomNamespacesNew: list of CommonNamespace
        :param CommonNamespaces: General alarm policy type, including TAPM, RUM, and CAT.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonNamespaces: list of CommonNamespaceNew
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.QceNamespaces = None
        self.CustomNamespaces = None
        self.QceNamespacesNew = None
        self.CustomNamespacesNew = None
        self.CommonNamespaces = None
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
        if params.get("CommonNamespaces") is not None:
            self.CommonNamespaces = []
            for item in params.get("CommonNamespaces"):
                obj = CommonNamespaceNew()
                obj._deserialize(item)
                self.CommonNamespaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics request structure.

    """

    def __init__(self):
        r"""
        :param Namespace: Service namespace. Tencent Cloud services have different namespaces. For more information on service namespaces, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the namespace of CVM
        :type Namespace: str
        :param MetricName: Metric name. Tencent Cloud services have different metric names. For more information on metric names, see the monitoring metric documentation of each service. For example, see [CVM Monitoring Metrics](https://intl.cloud.tencent.com/document/product/248/6843?from_cn_redirect=1) for the metric names of CVM
        :type MetricName: str
        :param Dimensions: Filter by dimension. This parameter is optional.
        :type Dimensions: list of str
        """
        self.Namespace = None
        self.MetricName = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Dimensions = params.get("Dimensions")
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
        r"""
        :param MetricSet: Listed of queried metric descriptions
        :type MetricSet: list of MetricSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param Id: Alarm ID.
        :type Id: int
        :param ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectId: int
        :param ProjectName: Project name.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectName: str
        :param Status: Alarm status ID. Valid values: 0 (not resolved), 1 (resolved), 2/3/5 (insufficient data), 4 (expired)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param AlarmStatus: Alarm status. Valid values: ALARM (not resolved), OK (resolved), NO_DATA (insufficient data), NO_CONF (expired)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AlarmStatus: str
        :param GroupId: Policy group ID.
Note: This field may return null, indicating that no valid value was found.
        :type GroupId: int
        :param GroupName: Policy group name.
Note: This field may return null, indicating that no valid value was found.
        :type GroupName: str
        :param FirstOccurTime: Occurrence time.
Note: This field may return null, indicating that no valid value was found.
        :type FirstOccurTime: str
        :param Duration: Duration in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Duration: int
        :param LastOccurTime: End time.
Note: This field may return null, indicating that no valid value was found.
        :type LastOccurTime: str
        :param Content: Alarm content.
Note: This field may return null, indicating that no valid value was found.
        :type Content: str
        :param ObjName: Alarm object.
Note: This field may return null, indicating that no valid value was found.
        :type ObjName: str
        :param ObjId: Alarm object ID.
Note: This field may return null, indicating that no valid value was found.
        :type ObjId: str
        :param ViewName: Policy type.
Note: This field may return null, indicating that no valid value was found.
        :type ViewName: str
        :param Vpc: VPC, which is unique to CVM.
Note: This field may return null, indicating that no valid value was found.
        :type Vpc: str
        :param MetricId: Metric ID.
Note: This field may return null, indicating that no valid value was found.
        :type MetricId: int
        :param MetricName: Metric name.
Note: This field may return null, indicating that no valid value was found.
        :type MetricName: str
        :param AlarmType: Alarm type. The value 0 indicates metric alarms. The value 2 indicates product event alarms. The value 3 indicates platform event alarms.
Note: This field may return null, indicating that no valid value was found.
        :type AlarmType: int
        :param Region: Region.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param Dimensions: Dimensions of an alarm object.
Note: This field may return null, indicating that no valid value was found.
        :type Dimensions: str
        :param NotifyWay: Notification method.
Note: This field may return null, indicating that no valid value was found.
        :type NotifyWay: list of str
        :param InstanceGroup: Instance group information.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: list of InstanceGroup
        """
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
        r"""
        :param Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.
        :type Limit: int
        :param Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.
        :type Offset: int
        :param OccurTimeOrder: Sorting by occurrence time. Valid values: asc and desc.
        :type OccurTimeOrder: str
        :param ProjectIds: Filter by project ID.
        :type ProjectIds: list of int
        :param ViewNames: Filter by policy type.
        :type ViewNames: list of str
        :param AlarmStatus: Filter by alarm status.
        :type AlarmStatus: list of int
        :param ObjLike: Filter by alarm object.
        :type ObjLike: str
        :param InstanceGroupIds: Filter by instance group ID.
        :type InstanceGroupIds: list of int
        :param MetricNames: Filtering by metric names
        :type MetricNames: list of str
        """
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
        r"""
        :param Alarms: Alarm list.
Note: This field may return null, indicating that no valid value was found.
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param Total: Total number.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param Warning: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warning: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Alarms = None
        self.Total = None
        self.Warning = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.Warning = params.get("Warning")
        self.RequestId = params.get("RequestId")


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """Dimensions of the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID.
        :type RegionId: int
        :param Region: Region abbreviation.
        :type Region: str
        :param Dimensions: Combined JSON string of dimensions.
        :type Dimensions: str
        :param EventDimensions: Combined JSON string of event dimensions.
        :type EventDimensions: str
        """
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
        r"""
        :param UniqueId: Unique ID of the object.
        :type UniqueId: str
        :param Dimensions: Dimension set of an object instance, which is a jsonObj string.
        :type Dimensions: str
        :param IsShielded: Whether the object is shielded. The value 0 indicates that the object is not shielded. The value 1 indicates that the object is shielded.
        :type IsShielded: int
        :param Region: Region where the object resides.
        :type Region: str
        """
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
        r"""
        :param InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param ViewName: Alarm policy type name.
        :type ViewName: str
        :param LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param GroupName: Instance group name.
        :type GroupName: str
        :param InstanceSum: Number of instances.
        :type InstanceSum: int
        :param UpdateTime: Update time.
        :type UpdateTime: int
        :param InsertTime: Creation time.
        :type InsertTime: int
        :param Regions: Regions where the instances reside.
Note: This field may return null, indicating that no valid value was found.
        :type Regions: list of str
        """
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID. If the ID is in the format of “policy-xxxx”, please enter it in the `PolicyId` field. Enter 0 in this field.
        :type GroupId: int
        :param PolicyId: Alarm policy ID in the format of “policy-xxxx”. If a value has been entered in this field, you can enter 0 in the `GroupId` field.
        :type PolicyId: str
        :param Limit: The number of alarm objects returned each time. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param Offset: Offset, which starts from 0 and is set to 0 by default. For example, the parameter `Offset=0&Limit=20` returns the zeroth to 19th alarm objects, and `Offset=20&Limit=20` returns the 20th to 39th alarm objects, and so on.
        :type Offset: int
        :param Dimensions: Dimensions of filtering objects.
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
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
        r"""
        :param List: List of bound object instances.
Note: This field may return null, indicating that no valid value was found.
        :type List: list of DescribeBindingPolicyObjectListInstance
        :param Total: Total number of bound object instances.
        :type Total: int
        :param NoShieldedSum: Number of object instances that are not shielded.
        :type NoShieldedSum: int
        :param InstanceGroup: Bound instance group information. This parameter is not configured if no instance group is bound.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeConditionsTemplateListRequest(AbstractModel):
    """DescribeConditionsTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param Module: The value is fixed to `monitor`.
        :type Module: str
        :param ViewName: View name, which can be obtained via [DescribeAllNamespaces](https://intl.cloud.tencent.com/document/product/248/48683?from_cn_redirect=1). For the monitoring of Tencent Cloud services, the value of this parameter is `QceNamespacesNew.N.Id` of the output parameter of `DescribeAllNamespaces`, for example, `cvm_device`.
        :type ViewName: str
        :param GroupName: Filter by trigger condition template name.
        :type GroupName: str
        :param GroupID: Filter by trigger condition template ID.
        :type GroupID: str
        :param Limit: Pagination parameter, which specifies the number of returned results per page. Value range: 1-100. Default value: 20.
        :type Limit: int
        :param Offset: Pagination offset starting from 0. Default value: 0.
        :type Offset: int
        :param UpdateTimeOrder: Sorting method by update time. `asc`: Ascending order; `desc`: Descending order.
        :type UpdateTimeOrder: str
        :param PolicyCountOrder: Sorting order based on the number of associated policies. Valid values: `asc` (ascending order), `desc` (descending order).
        :type PolicyCountOrder: str
        """
        self.Module = None
        self.ViewName = None
        self.GroupName = None
        self.GroupID = None
        self.Limit = None
        self.Offset = None
        self.UpdateTimeOrder = None
        self.PolicyCountOrder = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.ViewName = params.get("ViewName")
        self.GroupName = params.get("GroupName")
        self.GroupID = params.get("GroupID")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.PolicyCountOrder = params.get("PolicyCountOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConditionsTemplateListResponse(AbstractModel):
    """DescribeConditionsTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total number of templates.
        :type Total: int
        :param TemplateGroupList: Template list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TemplateGroupList: list of TemplateGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.TemplateGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("TemplateGroupList") is not None:
            self.TemplateGroupList = []
            for item in params.get("TemplateGroupList"):
                obj = TemplateGroup()
                obj._deserialize(item)
                self.TemplateGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDNSConfigRequest(AbstractModel):
    """DescribeDNSConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDNSConfigResponse(AbstractModel):
    """DescribeDNSConfig response structure.

    """

    def __init__(self):
        r"""
        :param NameServers: Array of DNS servers
        :type NameServers: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NameServers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NameServers = params.get("NameServers")
        self.RequestId = params.get("RequestId")


class DescribeExporterIntegrationsRequest(AbstractModel):
    """DescribeExporterIntegrations request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Kind: Type
        :type Kind: str
        :param Name: Name
        :type Name: str
        """
        self.InstanceId = None
        self.KubeType = None
        self.ClusterId = None
        self.Kind = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeType = params.get("KubeType")
        self.ClusterId = params.get("ClusterId")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExporterIntegrationsResponse(AbstractModel):
    """DescribeExporterIntegrations response structure.

    """

    def __init__(self):
        r"""
        :param IntegrationSet: List of integration configurations
        :type IntegrationSet: list of IntegrationConfiguration
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IntegrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self.IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = IntegrationConfiguration()
                obj._deserialize(item)
                self.IntegrationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGrafanaChannelsRequest(AbstractModel):
    """DescribeGrafanaChannels request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param Offset: Offset.
        :type Offset: int
        :param Limit: Number of items to be queried
        :type Limit: int
        :param ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param ChannelIds: Alert channel ID, such as “nchannel-abcd1234”.
        :type ChannelIds: list of str
        :param ChannelState: Alert channel status
        :type ChannelState: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.ChannelName = None
        self.ChannelIds = None
        self.ChannelState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ChannelName = params.get("ChannelName")
        self.ChannelIds = params.get("ChannelIds")
        self.ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaChannelsResponse(AbstractModel):
    """DescribeGrafanaChannels response structure.

    """

    def __init__(self):
        r"""
        :param NotificationChannelSet: Array of alert channels
        :type NotificationChannelSet: list of GrafanaChannel
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NotificationChannelSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self.NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaChannel()
                obj._deserialize(item)
                self.NotificationChannelSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGrafanaConfigRequest(AbstractModel):
    """DescribeGrafanaConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaConfigResponse(AbstractModel):
    """DescribeGrafanaConfig response structure.

    """

    def __init__(self):
        r"""
        :param Config: JSON-encoded string
        :type Config: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Config = params.get("Config")
        self.RequestId = params.get("RequestId")


class DescribeGrafanaEnvironmentsRequest(AbstractModel):
    """DescribeGrafanaEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaEnvironmentsResponse(AbstractModel):
    """DescribeGrafanaEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param Envs: Environment variable string
        :type Envs: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Envs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Envs = params.get("Envs")
        self.RequestId = params.get("RequestId")


class DescribeGrafanaInstancesRequest(AbstractModel):
    """DescribeGrafanaInstances request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for query
        :type Offset: int
        :param Limit: Number of items to be queried
        :type Limit: int
        :param InstanceIds: Array of TCMG instance IDs
        :type InstanceIds: list of str
        :param InstanceName: TCMG instance name, which can be fuzzily matched by prefix.
        :type InstanceName: str
        :param InstanceStatus: Query status
        :type InstanceStatus: list of int
        :param TagFilters: Array of tag filters
        :type TagFilters: list of PrometheusTag
        """
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceName = None
        self.InstanceStatus = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
        self.InstanceStatus = params.get("InstanceStatus")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaInstancesResponse(AbstractModel):
    """DescribeGrafanaInstances response structure.

    """

    def __init__(self):
        r"""
        :param InstanceSet: This parameter has been disused. Use `Instances` instead.
        :type InstanceSet: list of GrafanaInstanceInfo
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param Instances: List of instances
        :type Instances: list of GrafanaInstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceSet = None
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = GrafanaInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGrafanaIntegrationsRequest(AbstractModel):
    """DescribeGrafanaIntegrations request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param IntegrationId: Integration ID
        :type IntegrationId: str
        :param Kind: Type
        :type Kind: str
        """
        self.InstanceId = None
        self.IntegrationId = None
        self.Kind = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IntegrationId = params.get("IntegrationId")
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaIntegrationsResponse(AbstractModel):
    """DescribeGrafanaIntegrations response structure.

    """

    def __init__(self):
        r"""
        :param IntegrationSet: Array of integrations
        :type IntegrationSet: list of GrafanaIntegrationConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IntegrationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IntegrationSet") is not None:
            self.IntegrationSet = []
            for item in params.get("IntegrationSet"):
                obj = GrafanaIntegrationConfig()
                obj._deserialize(item)
                self.IntegrationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGrafanaNotificationChannelsRequest(AbstractModel):
    """DescribeGrafanaNotificationChannels request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of items to be queried
        :type Limit: int
        :param ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param ChannelIDs: Alert channel ID, such as “nchannel-abcd1234”.
        :type ChannelIDs: list of str
        :param ChannelState: Alert channel status
        :type ChannelState: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.ChannelName = None
        self.ChannelIDs = None
        self.ChannelState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ChannelName = params.get("ChannelName")
        self.ChannelIDs = params.get("ChannelIDs")
        self.ChannelState = params.get("ChannelState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaNotificationChannelsResponse(AbstractModel):
    """DescribeGrafanaNotificationChannels response structure.

    """

    def __init__(self):
        r"""
        :param NotificationChannelSet: Array of notification channels
        :type NotificationChannelSet: list of GrafanaNotificationChannel
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NotificationChannelSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotificationChannelSet") is not None:
            self.NotificationChannelSet = []
            for item in params.get("NotificationChannelSet"):
                obj = GrafanaNotificationChannel()
                obj._deserialize(item)
                self.NotificationChannelSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGrafanaWhiteListRequest(AbstractModel):
    """DescribeGrafanaWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGrafanaWhiteListResponse(AbstractModel):
    """DescribeGrafanaWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param WhiteList: Array
        :type WhiteList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WhiteList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WhiteList = params.get("WhiteList")
        self.RequestId = params.get("RequestId")


class DescribeInstalledPluginsRequest(AbstractModel):
    """DescribeInstalledPlugins request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-kleu3gt0”.
        :type InstanceId: str
        :param PluginId: Filter by plugin ID such as “grafana-piechart-panel”. You can view the IDs of installed plugins through the `DescribeInstalledPlugins` API.
        :type PluginId: str
        """
        self.InstanceId = None
        self.PluginId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstalledPluginsResponse(AbstractModel):
    """DescribeInstalledPlugins response structure.

    """

    def __init__(self):
        r"""
        :param PluginSet: List of plugins
        :type PluginSet: list of GrafanaPlugin
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PluginSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PluginSet") is not None:
            self.PluginSet = []
            for item in params.get("PluginSet"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self.PluginSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMonitorTypesRequest(AbstractModel):
    """DescribeMonitorTypes request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        """
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
        r"""
        :param MonitorTypes: Monitor type. Valid values: MT_QCE (Tencent Cloud service monitoring)
        :type MonitorTypes: list of str
        :param MonitorTypeInfos: Monitoring type details
        :type MonitorTypeInfos: list of MonitorTypeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MonitorTypes = None
        self.MonitorTypeInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MonitorTypes = params.get("MonitorTypes")
        if params.get("MonitorTypeInfos") is not None:
            self.MonitorTypeInfos = []
            for item in params.get("MonitorTypeInfos"):
                obj = MonitorTypeInfo()
                obj._deserialize(item)
                self.MonitorTypeInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePolicyConditionListCondition(AbstractModel):
    """Policy conditions returned by the DescribePolicyConditionList API

    """

    def __init__(self):
        r"""
        :param PolicyViewName: Policy view name.
        :type PolicyViewName: str
        :param EventMetrics: Event alarm conditions.
Note: This field may return null, indicating that no valid value was found.
        :type EventMetrics: list of DescribePolicyConditionListEventMetric
        :param IsSupportMultiRegion: Whether to support multiple regions.
        :type IsSupportMultiRegion: bool
        :param Metrics: Metric alarm conditions.
Note: This field may return null, indicating that no valid value was found.
        :type Metrics: list of DescribePolicyConditionListMetric
        :param Name: Policy type name.
        :type Name: str
        :param SortId: Sorting ID.
        :type SortId: int
        :param SupportDefault: Whether to support default policies.
        :type SupportDefault: bool
        :param SupportRegions: List of regions that support this policy type.
Note: This field may return null, indicating that no valid value was found.
        :type SupportRegions: list of str
        """
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
        r"""
        :param CalcType: Check method.
Note: This field may return null, indicating that no valid value was found.
        :type CalcType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`
        :param CalcValue: Threshold.
Note: This field may return null, indicating that no valid value was found.
        :type CalcValue: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`
        :param ContinueTime: Duration.
Note: This field may return null, indicating that no valid value was found.
        :type ContinueTime: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`
        :param Period: Data period.
Note: This field may return null, indicating that no valid value was found.
        :type Period: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`
        :param PeriodNum: Number of periods.
Note: This field may return null, indicating that no valid value was found.
        :type PeriodNum: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`
        :param StatType: Statistics method.
Note: This field may return null, indicating that no valid value was found.
        :type StatType: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`
        """
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
        r"""
        :param Keys: Value of CalcType.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param Need: Required or not.
        :type Need: bool
        """
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
        r"""
        :param Default: Default value.
Note: This field may return null, indicating that no valid value was found.
        :type Default: str
        :param Fixed: Fixed value.
Note: This field may return null, indicating that no valid value was found.
        :type Fixed: str
        :param Max: Maximum value.
Note: This field may return null, indicating that no valid value was found.
        :type Max: str
        :param Min: Minimum value.
Note: This field may return null, indicating that no valid value was found.
        :type Min: str
        :param Need: Required or not.
        :type Need: bool
        """
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
        r"""
        :param Default: Default duration in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param Keys: Custom durations in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param Need: Required or not.
        :type Need: bool
        """
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
        r"""
        :param Default: Default period in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param Keys: Custom periods in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param Need: Required or not.
        :type Need: bool
        """
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
        r"""
        :param Default: Number of default periods.
Note: This field may return null, indicating that no valid value was found.
        :type Default: int
        :param Keys: Number of custom periods.
Note: This field may return null, indicating that no valid value was found.
        :type Keys: list of int
        :param Need: Required or not.
        :type Need: bool
        """
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
        r"""
        :param P5: Data aggregation method in a period of 5 seconds.
Note: This field may return null, indicating that no valid value was found.
        :type P5: str
        :param P10: Data aggregation method in a period of 10 seconds.
Note: This field may return null, indicating that no valid value was found.
        :type P10: str
        :param P60: Data aggregation method in a period of 1 minute.
Note: This field may return null, indicating that no valid value was found.
        :type P60: str
        :param P300: Data aggregation method in a period of 5 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P300: str
        :param P600: Data aggregation method in a period of 10 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P600: str
        :param P1800: Data aggregation method in a period of 30 minutes.
Note: This field may return null, indicating that no valid value was found.
        :type P1800: str
        :param P3600: Data aggregation method in a period of 1 hour.
Note: This field may return null, indicating that no valid value was found.
        :type P3600: str
        :param P86400: Data aggregation method in a period of 1 day.
Note: This field may return null, indicating that no valid value was found.
        :type P86400: str
        """
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
        r"""
        :param EventId: Event ID.
        :type EventId: int
        :param EventShowName: Event name.
        :type EventShowName: str
        :param NeedRecovered: Whether to recover.
        :type NeedRecovered: bool
        :param Type: Event type, which is a reserved field. Currently, it is fixed to 2.
        :type Type: int
        """
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
        r"""
        :param ConfigManual: Metric configuration.
Note: This field may return null, indicating that no valid value was found.
        :type ConfigManual: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`
        :param MetricId: Metric ID.
        :type MetricId: int
        :param MetricShowName: Metric name.
        :type MetricShowName: str
        :param MetricUnit: Metric unit.
        :type MetricUnit: str
        """
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        """
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
        r"""
        :param Conditions: List of alarm policy conditions.
        :type Conditions: list of DescribePolicyConditionListCondition
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param CallbackUrl: URL of the user callback API.
        :type CallbackUrl: str
        :param ValidFlag: Status of the user callback API. The value 0 indicates that the API is not verified. The value 1 indicates that the API is verified. The value 2 indicates that a URL exists but the API fails to be verified.
        :type ValidFlag: int
        :param VerifyCode: Verification code of the user callback API.
        :type VerifyCode: str
        """
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
        r"""
        :param MetricShowName: Metric name.
        :type MetricShowName: str
        :param Period: Data aggregation period in seconds.
        :type Period: int
        :param MetricId: Metric ID.
        :type MetricId: int
        :param RuleId: Threshold rule ID.
        :type RuleId: int
        :param Unit: Metric unit.
        :type Unit: str
        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of `triggerTime`.
        :type AlarmNotifyPeriod: int
        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. The value 7 indicates day-on-day increase. The value 8 indicates day-on-day decrease. The value 9 indicates week-on-week increase. The value 10 indicates week-on-week decrease. The value 11 indicates periodical increase. The value 12 indicates periodical decrease.
        :type CalcType: int
        :param CalcValue: Threshold.
        :type CalcValue: str
        :param ContinueTime: Duration at which an alarm will be triggered in seconds.
        :type ContinueTime: int
        :param MetricName: Alarm metric name.
        :type MetricName: str
        """
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
        r"""
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param GroupName: Policy group name.
        :type GroupName: str
        :param ViewName: Policy type.
        :type ViewName: str
        :param Remark: Policy group remarks.
        :type Remark: str
        :param LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: int
        :param InsertTime: Creation time.
Note: This field may return null, indicating that no valid value was found.
        :type InsertTime: int
        :param IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        """
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
        r"""
        :param EventId: Event ID.
        :type EventId: int
        :param RuleId: Event alarm rule ID.
        :type RuleId: int
        :param EventShowName: Event name.
        :type EventShowName: str
        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param AlarmNotifyType: Alarm sending and converging type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        """
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
        r"""
        :param ReceiverGroupList: List of alarm recipient group IDs.
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: List of alarm recipient IDs.
        :type ReceiverUserList: list of int
        :param StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates “10:0:0”.
        :type StartTime: int
        :param EndTime: End time of the alarm period. The meaning is the same as that of StartTime.
        :type EndTime: int
        :param ReceiverType: Recipient type. Valid values: group and user.
        :type ReceiverType: str
        :param NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".
        :type NotifyWay: list of str
        :param UidList: Uid of the alarm call recipient.
Note: This field may return null, indicating that no valid value was found.
        :type UidList: list of int
        :param RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param RoundInterval: Intervals of alarm call rounds in seconds.
        :type RoundInterval: int
        :param PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.
        :type NeedSendNotice: int
        :param SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).
        :type SendFor: list of str
        :param RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.
        :type RecoverNotify: list of str
        :param ReceiveLanguage: Alarm language.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiveLanguage: str
        """
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: int
        """
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
        r"""
        :param GroupName: Policy group name.
        :type GroupName: str
        :param ProjectId: ID of the project to which the policy group belongs.
        :type ProjectId: int
        :param IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.
        :type IsDefault: int
        :param ViewName: Policy type.
        :type ViewName: str
        :param Remark: Policy description
        :type Remark: str
        :param ShowName: Policy type name.
        :type ShowName: str
        :param LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param UpdateTime: Last edited time.
        :type UpdateTime: str
        :param Region: Regions supported by this policy.
        :type Region: list of str
        :param DimensionGroup: List of policy type dimensions.
        :type DimensionGroup: list of str
        :param ConditionsConfig: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition
        :param EventConfig: Product event rule list.
Note: This field may return null, indicating that no valid value was found.
        :type EventConfig: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param Callback: User callback information.
Note: This field may return null, indicating that no valid value was found.
        :type Callback: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`
        :param ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param CanSetDefault: Whether the policy can be configured as the default policy.
        :type CanSetDefault: bool
        :param IsUnionRule: Whether the 'AND' rule is used.
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        r"""
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param GroupName: Policy group name.
        :type GroupName: str
        :param IsOpen: Whether it is enabled.
        :type IsOpen: bool
        :param ViewName: Policy view name.
        :type ViewName: str
        :param LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param UpdateTime: Last modified time.
        :type UpdateTime: int
        :param InsertTime: Creation time.
        :type InsertTime: int
        :param UseSum: Number of instances that are bound to the policy group.
        :type UseSum: int
        :param NoShieldedSum: Number of unshielded instances that are bound to the policy group.
        :type NoShieldedSum: int
        :param IsDefault: Whether it is the default policy. The value 0 indicates that it is not the default policy. The value 1 indicates that it is the default policy.
        :type IsDefault: int
        :param CanSetDefault: Whether the policy can be configured as the default policy.
        :type CanSetDefault: bool
        :param ParentGroupId: Parent policy group ID.
        :type ParentGroupId: int
        :param Remark: Remarks of the policy group.
        :type Remark: str
        :param ProjectId: ID of the project to which the policy group belongs.
        :type ProjectId: int
        :param Conditions: Threshold rule list.
Note: This field may return null, indicating that no valid value was found.
        :type Conditions: list of DescribePolicyGroupInfoCondition
        :param EventConditions: Product event rule list.
Note: This field may return null, indicating that no valid value was found.
        :type EventConditions: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: Recipient list.
Note: This field may return null, indicating that no valid value was found.
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param ConditionsTemp: Template-based policy group.
Note: This field may return null, indicating that no valid value was found.
        :type ConditionsTemp: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param InstanceGroup: Instance group that is bound to the policy group.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroup: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`
        :param IsUnionRule: The 'AND' or 'OR' rule. The value 0 indicates the 'OR' rule (indicating that an alarm will be triggered if any rule meets the threshold condition). The value 1 indicates the 'AND' rule (indicating that an alarm will be triggered when all rules meet the threshold conditions).
Note: This field may return null, indicating that no valid value was found.
        :type IsUnionRule: int
        """
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
        r"""
        :param InstanceGroupId: Instance group name ID.
        :type InstanceGroupId: int
        :param ViewName: Policy type view name.
        :type ViewName: str
        :param LastEditUin: Uin that was last edited.
        :type LastEditUin: str
        :param GroupName: Instance group name.
        :type GroupName: str
        :param InstanceSum: Number of instances.
        :type InstanceSum: int
        :param UpdateTime: Update time.
        :type UpdateTime: int
        :param InsertTime: Creation time.
        :type InsertTime: int
        """
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100.
        :type Limit: int
        :param Offset: Parameter offset on each page. The value starts from 0.
        :type Offset: int
        :param Like: Search by policy name.
        :type Like: str
        :param InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param UpdateTimeOrder: Sort by update time. Valid values: asc and desc.
        :type UpdateTimeOrder: str
        :param ProjectIds: Project ID list.
        :type ProjectIds: list of int
        :param ViewNames: List of alarm policy types.
        :type ViewNames: list of str
        :param FilterUnuseReceiver: Whether to filter policy groups without recipients. The value 1 indicates that policy groups without recipients will be filtered. The value 0 indicates that policy groups without recipients will not be filtered.
        :type FilterUnuseReceiver: int
        :param Receivers: Filter by recipient group.
        :type Receivers: list of str
        :param ReceiverUserList: Filter by recipient.
        :type ReceiverUserList: list of str
        :param Dimensions: Dimension set field (json string), for example, [[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]].
        :type Dimensions: str
        :param ConditionTempGroupId: Template-based policy group IDs, which are separated by commas.
        :type ConditionTempGroupId: str
        :param ReceiverType: Filter by recipient or recipient group. The value 'user' indicates by recipient. The value 'group' indicates by recipient group.
        :type ReceiverType: str
        :param IsOpen: Filter conditions. Whether the alarm policy has been enabled or disabled
        :type IsOpen: bool
        """
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
        r"""
        :param GroupList: Policy group list.
Note: This field may return null, indicating that no valid value was found.
        :type GroupList: list of DescribePolicyGroupListGroup
        :param Total: Total number of policy groups.
        :type Total: int
        :param Warning: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warning: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupList = None
        self.Total = None
        self.Warning = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.Total = params.get("Total")
        self.Warning = params.get("Warning")
        self.RequestId = params.get("RequestId")


class DescribeProductEventListDimensions(AbstractModel):
    """Input parameter Dimensions of the DescribeProductEventList API

    """

    def __init__(self):
        r"""
        :param Name: Dimension name.
        :type Name: str
        :param Value: Dimension value.
        :type Value: str
        """
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
        r"""
        :param EventId: Event ID.
Note: This field may return null, indicating that no valid value was found.
        :type EventId: int
        :param EventCName: Event name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type EventCName: str
        :param EventEName: Event name in English.
Note: This field may return null, indicating that no valid value was found.
        :type EventEName: str
        :param EventName: Event name abbreviation.
Note: This field may return null, indicating that no valid value was found.
        :type EventName: str
        :param ProductCName: Product name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type ProductCName: str
        :param ProductEName: Product name in English.
Note: This field may return null, indicating that no valid value was found.
        :type ProductEName: str
        :param ProductName: Product name abbreviation.
Note: This field may return null, indicating that no valid value was found.
        :type ProductName: str
        :param InstanceId: Instance ID.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceId: str
        :param InstanceName: Instance name.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceName: str
        :param ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectId: str
        :param Region: Region.
Note: This field may return null, indicating that no valid value was found.
        :type Region: str
        :param Status: Status.
Note: This field may return null, indicating that no valid value was found.
        :type Status: str
        :param SupportAlarm: Whether to support alarms.
Note: This field may return null, indicating that no valid value was found.
        :type SupportAlarm: int
        :param Type: Event type.
Note: This field may return null, indicating that no valid value was found.
        :type Type: str
        :param StartTime: Start time.
Note: This field may return null, indicating that no valid value was found.
        :type StartTime: int
        :param UpdateTime: Update time.
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: int
        :param Dimensions: Instance object information.
Note: This field may return null, indicating that no valid value was found.
        :type Dimensions: list of DescribeProductEventListEventsDimensions
        :param AdditionMsg: Additional information of the instance object.
Note: This field may return null, indicating that no valid value was found.
        :type AdditionMsg: list of DescribeProductEventListEventsDimensions
        :param IsAlarmConfig: Whether to configure alarms.
Note: This field may return null, indicating that no valid value was found.
        :type IsAlarmConfig: int
        :param GroupInfo: Policy information.
Note: This field may return null, indicating that no valid value was found.
        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo
        :param ViewName: Display name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ViewName: str
        """
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
        r"""
        :param Key: Dimension name in English.
Note: This field may return null, indicating that no valid value was found.
        :type Key: str
        :param Name: Dimension name in Chinese.
Note: This field may return null, indicating that no valid value was found.
        :type Name: str
        :param Value: Dimension value.
Note: This field may return null, indicating that no valid value was found.
        :type Value: str
        """
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
        r"""
        :param GroupId: Policy ID.
Note: This field may return null, indicating that no valid value was found.
        :type GroupId: int
        :param GroupName: Policy name.
Note: This field may return null, indicating that no valid value was found.
        :type GroupName: str
        """
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
        r"""
        :param StatusChangeAmount: Number of events whose statuses have changed.
Note: This field may return null, indicating that no valid value was found.
        :type StatusChangeAmount: int
        :param UnConfigAlarmAmount: Number of events whose alarm statuses are not configured.
Note: This field may return null, indicating that no valid value was found.
        :type UnConfigAlarmAmount: int
        :param UnNormalEventAmount: Number of events with exceptions.
Note: This field may return null, indicating that no valid value was found.
        :type UnNormalEventAmount: int
        :param UnRecoverAmount: Number of events that have not been recovered.
Note: This field may return null, indicating that no valid value was found.
        :type UnRecoverAmount: int
        """
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
        r"""
        :param Module: API component name. It is fixed to monitor.
        :type Module: str
        :param ProductName: Filter by product type. For example, 'cvm' indicates Cloud Virtual Machine.
        :type ProductName: list of str
        :param EventName: Filter by product name. For example, "guest_reboot" indicates server restart.
        :type EventName: list of str
        :param InstanceId: Affected object, such as "ins-19708ino"
        :type InstanceId: list of str
        :param Dimensions: Filter by dimension, such as by public IP: 10.0.0.1.
        :type Dimensions: list of DescribeProductEventListDimensions
        :param RegionList: Region filter parameter for service events.
        :type RegionList: list of str
        :param Type: Filter by event type. Valid values: ["status_change","abnormal"], which indicate events whose statuses have changed and events with exceptions respectively.
        :type Type: list of str
        :param Status: Filter by event status. Valid values: ["recover","alarm","-"], which indicate that an event has been recovered, has not been recovered, and has no status respectively.
        :type Status: list of str
        :param Project: Filter by project ID.
        :type Project: list of str
        :param IsAlarmConfig: Filter by alarm status configuration. The value 1 indicates that the alarm status has been configured. The value 0 indicates that the alarm status has not been configured.
        :type IsAlarmConfig: int
        :param TimeOrder: Sorting by update time. The value ASC indicates the ascending order. The value DESC indicates the descending order. The default value is DESC.
        :type TimeOrder: str
        :param StartTime: Start time, which is the timestamp one day prior by default.
        :type StartTime: int
        :param EndTime: End time, which is the current timestamp by default.
        :type EndTime: int
        :param Offset: Page offset. The default value is 0.
        :type Offset: int
        :param Limit: The number of parameters that can be returned on each page. The default value is 20.
        :type Limit: int
        """
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
        r"""
        :param Events: Event list
Note: This field may return null, indicating that no valid value was found.
        :type Events: list of DescribeProductEventListEvents
        :param OverView: Event statistics.
        :type OverView: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListOverView`
        :param Total: Total number of events.
Note: This field may return null, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
It can be the ID of a TKE, EKS, or edge cluster.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances response structure.

    """

    def __init__(self):
        r"""
        :param Instances: List of instances associated with the cluster
Note: This field may return null, indicating that no valid values can be obtained.
        :type Instances: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Instances = params.get("Instances")
        self.RequestId = params.get("RequestId")


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Agent name
        :type Name: str
        :param AgentIds: List of agent IDs
        :type AgentIds: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.InstanceId = None
        self.Name = None
        self.AgentIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.AgentIds = params.get("AgentIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents response structure.

    """

    def __init__(self):
        r"""
        :param AgentSet: List of agents
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentSet: list of PrometheusAgent
        :param TotalCount: Total number of agents
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AgentSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentSet") is not None:
            self.AgentSet = []
            for item in params.get("AgentSet"):
                obj = PrometheusAgent()
                obj._deserialize(item)
                self.AgentSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrometheusAlertPolicyRequest(AbstractModel):
    """DescribePrometheusAlertPolicy request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of results per page
        :type Limit: int
        :param Filters: Filter
Valid values: `ID`, `Name`.
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertPolicyResponse(AbstractModel):
    """DescribePrometheusAlertPolicy response structure.

    """

    def __init__(self):
        r"""
        :param AlertRules: Alert details
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRules: list of PrometheusAlertPolicyItem
        :param Total: Total number
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AlertRules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlertRules") is not None:
            self.AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertRules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusConfigRequest(AbstractModel):
    """DescribePrometheusConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterType: Cluster type
        :type ClusterType: str
        """
        self.InstanceId = None
        self.ClusterId = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusConfigResponse(AbstractModel):
    """DescribePrometheusConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstanceDetailRequest(AbstractModel):
    """DescribePrometheusInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceDetailResponse(AbstractModel):
    """DescribePrometheusInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param InstanceStatus: Instance status. Valid values:

`1`: Creating
`2`: Running
`3`: Abnormal
`4`: Rebooting
`5`: Terminating
`6`: Service suspended
`8`: Suspending service for overdue payment
`9`: Service suspended for overdue payment
        :type InstanceStatus: int
        :param ChargeStatus: Billing status

`1`: Normal
`2`: Expired
`3`: Terminated
`4`: Assigning
`5`: Failed to assign
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param EnableGrafana: Whether Grafana is enabled
`0`: Disabled
`1`: Enabled
        :type EnableGrafana: int
        :param GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param InstanceChargeType: Instance billing mode. Valid values:

`2`: Monthly subscription
`3`: Pay-as-you-go
        :type InstanceChargeType: int
        :param SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param AutoRenewFlag: Auto-renewal flag

`0`: Auto-renewal not enabled
`1`: Auto-renewal enabled
`2`: Auto-renewal prohibited
`-1`: Invalid
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceStatus = None
        self.ChargeStatus = None
        self.EnableGrafana = None
        self.GrafanaURL = None
        self.InstanceChargeType = None
        self.SpecName = None
        self.DataRetentionTime = None
        self.ExpireTime = None
        self.AutoRenewFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.ChargeStatus = params.get("ChargeStatus")
        self.EnableGrafana = params.get("EnableGrafana")
        self.GrafanaURL = params.get("GrafanaURL")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.SpecName = params.get("SpecName")
        self.DataRetentionTime = params.get("DataRetentionTime")
        self.ExpireTime = params.get("ExpireTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstanceInitStatusRequest(AbstractModel):
    """DescribePrometheusInstanceInitStatus request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceInitStatusResponse(AbstractModel):
    """DescribePrometheusInstanceInitStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Instance initialization status. Valid values:
`uninitialized` 
`initializing`
`running`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Steps: Initialize task steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type Steps: list of TaskStepInfo
        :param EksClusterId: EKS cluster ID of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type EksClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Steps = None
        self.EksClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self.Steps.append(obj)
        self.EksClusterId = params.get("EksClusterId")
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstanceUsageRequest(AbstractModel):
    """DescribePrometheusInstanceUsage request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Query by one or more instance IDs. Instance ID is in the format of `prom-xxxxxxxx`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param StartCalcDate: Start time
        :type StartCalcDate: str
        :param EndCalcDate: End time
        :type EndCalcDate: str
        """
        self.InstanceIds = None
        self.StartCalcDate = None
        self.EndCalcDate = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.StartCalcDate = params.get("StartCalcDate")
        self.EndCalcDate = params.get("EndCalcDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceUsageResponse(AbstractModel):
    """DescribePrometheusInstanceUsage response structure.

    """

    def __init__(self):
        r"""
        :param UsageSet: Usage list
Note: This field may return null, indicating that no valid values can be obtained.
        :type UsageSet: list of PrometheusInstanceTenantUsage
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UsageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsageSet") is not None:
            self.UsageSet = []
            for item in params.get("UsageSet"):
                obj = PrometheusInstanceTenantUsage()
                obj._deserialize(item)
                self.UsageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstancesOverviewRequest(AbstractModel):
    """DescribePrometheusInstancesOverview request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of results per page
        :type Limit: int
        :param Filters: Instance filter. Valid values:
`ID`: Filter by instance ID 
`Name`: Filter by instance name
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstancesOverviewResponse(AbstractModel):
    """DescribePrometheusInstancesOverview response structure.

    """

    def __init__(self):
        r"""
        :param Instances: List of instances
        :type Instances: list of PrometheusInstancesOverview
        :param Total: Total number of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Instances = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = PrometheusInstancesOverview()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstancesRequest(AbstractModel):
    """DescribePrometheusInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Queries by instance ID or IDs. Instance ID is in the format of `prom-xxxxxxxx`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param InstanceStatus: Filter by instance status
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
        :param InstanceName: Filter by instance name
        :type InstanceName: str
        :param Zones: Filter by AZ in the format of `ap-guangzhou-1`
        :type Zones: list of str
        :param TagFilters: Filter by tag key-value pair. The `tag-key` should be replaced with a specific tag key.
        :type TagFilters: list of PrometheusTag
        :param IPv4Address: Filter by instance IPv4 address
        :type IPv4Address: list of str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param InstanceChargeType: Filter by billing mode
<li>2: Monthly subscription</li>
<li>3: Pay-as-you-go</li>
        :type InstanceChargeType: int
        """
        self.InstanceIds = None
        self.InstanceStatus = None
        self.InstanceName = None
        self.Zones = None
        self.TagFilters = None
        self.IPv4Address = None
        self.Limit = None
        self.Offset = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceName = params.get("InstanceName")
        self.Zones = params.get("Zones")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.IPv4Address = params.get("IPv4Address")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstancesResponse(AbstractModel):
    """DescribePrometheusInstances response structure.

    """

    def __init__(self):
        r"""
        :param InstanceSet: List of instance details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceSet: list of PrometheusInstancesItem
        :param TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = PrometheusInstancesItem()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrometheusRecordRuleYamlRequest(AbstractModel):
    """DescribePrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of results per page
        :type Limit: int
        :param Filters: Filter. Valid values:
`Name`: Name
`Values`: List of target names
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusRecordRuleYamlResponse(AbstractModel):
    """DescribePrometheusRecordRuleYaml response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribePrometheusRecordRulesRequest(AbstractModel):
    """DescribePrometheusRecordRules request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of results per page
        :type Limit: int
        :param Filters: Filter
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusRecordRulesResponse(AbstractModel):
    """DescribePrometheusRecordRules response structure.

    """

    def __init__(self):
        r"""
        :param Records: Recording rule
        :type Records: list of PrometheusRecordRuleYamlItem
        :param Total: Total number
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Records = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = PrometheusRecordRuleYamlItem()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusScrapeJobsRequest(AbstractModel):
    """DescribePrometheusScrapeJobs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AgentId: Agent ID
        :type AgentId: str
        :param Name: Task name
        :type Name: str
        :param JobIds: List of task IDs
        :type JobIds: list of str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self.InstanceId = None
        self.AgentId = None
        self.Name = None
        self.JobIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentId = params.get("AgentId")
        self.Name = params.get("Name")
        self.JobIds = params.get("JobIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusScrapeJobsResponse(AbstractModel):
    """DescribePrometheusScrapeJobs response structure.

    """

    def __init__(self):
        r"""
        :param ScrapeJobSet: List of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScrapeJobSet: list of PrometheusScrapeJob
        :param TotalCount: Total number of tasks
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ScrapeJobSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScrapeJobSet") is not None:
            self.ScrapeJobSet = []
            for item in params.get("ScrapeJobSet"):
                obj = PrometheusScrapeJob()
                obj._deserialize(item)
                self.ScrapeJobSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrometheusTempRequest(AbstractModel):
    """DescribePrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Fuzzy filter. Valid values:
`Level`: Filter by template level
`Name`: Filter by name
`Describe`: Filter by description
`ID`: Filter by templateId
        :type Filters: list of Filter
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of results per page
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempResponse(AbstractModel):
    """DescribePrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param Templates: List of templates
        :type Templates: list of PrometheusTemp
        :param Total: Total number
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = PrometheusTemp()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusTempSyncRequest(AbstractModel):
    """DescribePrometheusTempSync request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempSyncResponse(AbstractModel):
    """DescribePrometheusTempSync response structure.

    """

    def __init__(self):
        r"""
        :param Targets: Details of the sync target
Note: This field may return null, indicating that no valid values can be obtained.
        :type Targets: list of PrometheusTemplateSyncTarget
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrometheusZonesRequest(AbstractModel):
    """DescribePrometheusZones request structure.

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID
        :type RegionId: int
        """
        self.RegionId = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusZonesResponse(AbstractModel):
    """DescribePrometheusZones response structure.

    """

    def __init__(self):
        r"""
        :param ZoneSet: Region list
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneSet: list of PrometheusZoneItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = PrometheusZoneItem()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordingRulesRequest(AbstractModel):
    """DescribeRecordingRules request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param RuleId: Rule ID
        :type RuleId: str
        :param RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
        :type RuleState: int
        :param Name: Rule name
        :type Name: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.RuleId = None
        self.RuleState = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleId = params.get("RuleId")
        self.RuleState = params.get("RuleState")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingRulesResponse(AbstractModel):
    """DescribeRecordingRules response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of rule groups
        :type TotalCount: int
        :param RecordingRuleSet: Rule group details
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordingRuleSet: list of RecordingRuleSet
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RecordingRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RecordingRuleSet") is not None:
            self.RecordingRuleSet = []
            for item in params.get("RecordingRuleSet"):
                obj = RecordingRuleSet()
                obj._deserialize(item)
                self.RecordingRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSSOAccountRequest(AbstractModel):
    """DescribeSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param UserId: Filter by account ID such as “10000”
        :type UserId: str
        """
        self.InstanceId = None
        self.UserId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSSOAccountResponse(AbstractModel):
    """DescribeSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param AccountSet: List of authorized accounts
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountSet: list of GrafanaAccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = GrafanaAccountInfo()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceDiscoveryRequest(AbstractModel):
    """DescribeServiceDiscovery request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param KubeClusterId: <li>TKE: ID of the integrated TKE cluster</li>
        :type KubeClusterId: str
        :param KubeType: Kubernetes cluster type:
<li> 1 = TKE </li>
        :type KubeType: int
        """
        self.InstanceId = None
        self.KubeClusterId = None
        self.KubeType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeClusterId = params.get("KubeClusterId")
        self.KubeType = params.get("KubeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceDiscoveryResponse(AbstractModel):
    """DescribeServiceDiscovery response structure.

    """

    def __init__(self):
        r"""
        :param ServiceDiscoverySet: List of returned scrape configurations
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDiscoverySet: list of ServiceDiscoveryItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceDiscoverySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceDiscoverySet") is not None:
            self.ServiceDiscoverySet = []
            for item in params.get("ServiceDiscoverySet"):
                obj = ServiceDiscoveryItem()
                obj._deserialize(item)
                self.ServiceDiscoverySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStatisticDataRequest(AbstractModel):
    """DescribeStatisticData request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module, whose value is fixed at `monitor`
        :type Module: str
        :param Namespace: Namespace. Valid values: QCE/TKE
        :type Namespace: str
        :param MetricNames: Metric name list
        :type MetricNames: list of str
        :param Conditions: Dimension condition. The `=` and `in` operators are supported
        :type Conditions: list of MidQueryCondition
        :param Period: Statistical period in seconds. Default value: 300. Optional values: 60, 300, 3,600, and 86,400.
Due to the storage period limit, the statistical period is subject to the time range of statistics:
60s: The time range is less than 12 hours, and the timespan between `StartTime` and the current time cannot exceed 15 days.
300s: The time range is less than three days, and the timespan between `StartTime` and the current time cannot exceed 31 days.
3,600s: The time range is less than 30 days, and the timespan between `StartTime` and the current time cannot exceed 93 days.
86,400s: The time range is less than 186 days, and the timespan between `StartTime` and the current time cannot exceed 186 days.
        :type Period: int
        :param StartTime: Start time, which is the current time by default, such as 2020-12-08T19:51:23+08:00
        :type StartTime: str
        :param EndTime: End time, which is the current time by default, such as 2020-12-08T19:51:23+08:00
        :type EndTime: str
        :param GroupBys: `groupBy` by the specified dimension
        :type GroupBys: list of str
        """
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
        r"""
        :param Period: Statistical period
        :type Period: int
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Data: Monitoring data
        :type Data: list of MetricData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DestroyPrometheusInstanceRequest(AbstractModel):
    """DestroyPrometheusInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID. The instance must be terminated first.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPrometheusInstanceResponse(AbstractModel):
    """DestroyPrometheusInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    """Combination of instance object dimensions

    """

    def __init__(self):
        r"""
        :param Name: Instance dimension name
        :type Name: str
        :param Value: Instance dimension value
        :type Value: str
        """
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
        


class DimensionNew(AbstractModel):
    """Dimension information of the policy type

    """

    def __init__(self):
        r"""
        :param Key: Dimension key ID displayed on the backend
        :type Key: str
        :param Name: Dimension key name displayed on the frontend
        :type Name: str
        :param IsRequired: Whether it is required
        :type IsRequired: bool
        :param Operators: List of supported operators
        :type Operators: list of Operator
        :param IsMultiple: Whether multiple items can be selected
        :type IsMultiple: bool
        :param IsMutable: Whether it can be modified after creation
        :type IsMutable: bool
        :param IsVisible: Whether it is displayed to users
        :type IsVisible: bool
        :param CanFilterPolicy: Whether it can be used to filter policies
        :type CanFilterPolicy: bool
        :param CanFilterHistory: Whether it can be used to filter historical alarms
        :type CanFilterHistory: bool
        :param CanGroupBy: Whether it can be used as an aggregate dimension
        :type CanGroupBy: bool
        :param MustGroupBy: Whether it must be used as an aggregate dimension
        :type MustGroupBy: bool
        :param ShowValueReplace: The key to be replaced on the frontend
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShowValueReplace: str
        """
        self.Key = None
        self.Name = None
        self.IsRequired = None
        self.Operators = None
        self.IsMultiple = None
        self.IsMutable = None
        self.IsVisible = None
        self.CanFilterPolicy = None
        self.CanFilterHistory = None
        self.CanGroupBy = None
        self.MustGroupBy = None
        self.ShowValueReplace = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.IsRequired = params.get("IsRequired")
        if params.get("Operators") is not None:
            self.Operators = []
            for item in params.get("Operators"):
                obj = Operator()
                obj._deserialize(item)
                self.Operators.append(obj)
        self.IsMultiple = params.get("IsMultiple")
        self.IsMutable = params.get("IsMutable")
        self.IsVisible = params.get("IsVisible")
        self.CanFilterPolicy = params.get("CanFilterPolicy")
        self.CanFilterHistory = params.get("CanFilterHistory")
        self.CanGroupBy = params.get("CanGroupBy")
        self.MustGroupBy = params.get("MustGroupBy")
        self.ShowValueReplace = params.get("ShowValueReplace")
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
        r"""
        :param Dimensions: Array of dimension names
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetRequest(AbstractModel):
    """EnableGrafanaInternet request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: TCMG instance ID, such as “grafana-kleu3gt0”.
        :type InstanceID: str
        :param EnableInternet: Whether to enable public network access (`true`: Yes; `false`: No)
        :type EnableInternet: bool
        """
        self.InstanceID = None
        self.EnableInternet = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.EnableInternet = params.get("EnableInternet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaInternetResponse(AbstractModel):
    """EnableGrafanaInternet response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableGrafanaSSORequest(AbstractModel):
    """EnableGrafanaSSO request structure.

    """

    def __init__(self):
        r"""
        :param EnableSSO: Whether to enable SSO (`true`: Yes; `false`: No)
        :type EnableSSO: bool
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.EnableSSO = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EnableSSO = params.get("EnableSSO")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGrafanaSSOResponse(AbstractModel):
    """EnableGrafanaSSO response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableSSOCamCheckRequest(AbstractModel):
    """EnableSSOCamCheck request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param EnableSSOCamCheck: Whether to enable CAM authentication (`true`: Yes; `false`: No)
        :type EnableSSOCamCheck: bool
        """
        self.InstanceId = None
        self.EnableSSOCamCheck = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSSOCamCheckResponse(AbstractModel):
    """EnableSSOCamCheck response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EventCondition(AbstractModel):
    """Event alarm conditions

    """

    def __init__(self):
        r"""
        :param AlarmNotifyPeriod: Alarm notification frequency.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotifyPeriod: str
        :param AlarmNotifyType: Predefined repeated notification policy. `0`: One-time alarm; `1`: exponential alarm; `2`: consecutive alarm
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotifyType: str
        :param EventID: Event ID.
        :type EventID: str
        :param EventDisplayName: Displayed event name.
        :type EventDisplayName: str
        :param RuleID: Rule ID.
        :type RuleID: str
        """
        self.AlarmNotifyPeriod = None
        self.AlarmNotifyType = None
        self.EventID = None
        self.EventDisplayName = None
        self.RuleID = None


    def _deserialize(self, params):
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.EventID = params.get("EventID")
        self.EventDisplayName = params.get("EventDisplayName")
        self.RuleID = params.get("RuleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param Type: Filter method. Valid values: `=`, `!=`, `in`.
        :type Type: str
        :param Key: Filter dimension name
        :type Key: str
        :param Value: Filter value. For the `in` filter method, separate multiple values by comma.
        :type Value: str
        """
        self.Type = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
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
        r"""
        :param Namespace: Namespace, such as QCE/CVM. For more information on the namespaces of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1)
        :type Namespace: str
        :param MetricName: Metric name, such as `CPUUsage`. Only one monitoring metric can be pulled at a time. For more information on the metrics of each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The corresponding metric name is `MetricName`.
        :type MetricName: str
        :param Instances: The dimension combination for instance objects, which is in the form of a set of key-value pairs. The dimension fields for instances of different Tencent Cloud services are completely different. For example, the field is [{"Name":"InstanceId","Value":"ins-j0hk02zo"}] for CVM instances, [{"Name":"instanceId","Value":"ckafka-l49k54dd"}] for CKafka instances, and [{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}] for COS instances. For more information on the dimensions of various Tencent Cloud services, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). In each document, the dimension column displays a dimension combination’s key, which has a corresponding value. A single request can get the data of up to 10 instances.
        :type Instances: list of Instance
        :param Period: Monitoring statistical period in seconds, such as 60. Default value: 300. The statistical period varies by metric. For more information on the statistical periods supported by each Tencent Cloud service, please see [Tencent Cloud Service Metrics](https://intl.cloud.tencent.com/document/product/248/6140?from_cn_redirect=1). The values in the statistical period column are the supported statistical periods. A single request can get up to 1,440 data points.
        :type Period: int
        :param StartTime: Start time such as 2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: End time, which is the current time by default, such as 2018-09-22T20:51:23+08:00. `EndTime` cannot be earlier than `StartTime`
        :type EndTime: str
        """
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
        r"""
        :param Period: Statistical period
        :type Period: int
        :param MetricName: Metric name
        :type MetricName: str
        :param DataPoints: Array of data points
        :type DataPoints: list of DataPoint
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Msg: Returned message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.Msg = None
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
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class GetPrometheusAgentManagementCommandRequest(AbstractModel):
    """GetPrometheusAgentManagementCommand request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param AgentId: Prometheus Agent ID
        :type AgentId: str
        """
        self.InstanceId = None
        self.AgentId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPrometheusAgentManagementCommandResponse(AbstractModel):
    """GetPrometheusAgentManagementCommand response structure.

    """

    def __init__(self):
        r"""
        :param Command: Agent management command
        :type Command: :class:`tencentcloud.monitor.v20180724.models.ManagementCommand`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Command = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Command") is not None:
            self.Command = ManagementCommand()
            self.Command._deserialize(params.get("Command"))
        self.RequestId = params.get("RequestId")


class GrafanaAccountInfo(AbstractModel):
    """TCMG authorized account information

    """

    def __init__(self):
        r"""
        :param UserId: User account ID
        :type UserId: str
        :param Role: User permission
        :type Role: list of GrafanaAccountRole
        :param Notes: Remarks
        :type Notes: str
        :param CreateAt: Creation time
        :type CreateAt: str
        :param InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Uin: User’s root account UIN
        :type Uin: str
        """
        self.UserId = None
        self.Role = None
        self.Notes = None
        self.CreateAt = None
        self.InstanceId = None
        self.Uin = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        if params.get("Role") is not None:
            self.Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self.Role.append(obj)
        self.Notes = params.get("Notes")
        self.CreateAt = params.get("CreateAt")
        self.InstanceId = params.get("InstanceId")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaAccountRole(AbstractModel):
    """TCMG account permission

    """

    def __init__(self):
        r"""
        :param Organization: Organization
        :type Organization: str
        :param Role: Permission
        :type Role: str
        """
        self.Organization = None
        self.Role = None


    def _deserialize(self, params):
        self.Organization = params.get("Organization")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaChannel(AbstractModel):
    """Grafana alert channel

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        :param ChannelName: Channel name
        :type ChannelName: str
        :param Receivers: Array of alert channel template IDs
        :type Receivers: list of str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        :param UpdatedAt: Update time
        :type UpdatedAt: str
        :param OrganizationIds: All valid organizations in an alert channel
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrganizationIds: list of str
        """
        self.ChannelId = None
        self.ChannelName = None
        self.Receivers = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.OrganizationIds = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.ChannelName = params.get("ChannelName")
        self.Receivers = params.get("Receivers")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaInstanceInfo(AbstractModel):
    """Instance type when the Grafana instance is queried

    """

    def __init__(self):
        r"""
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Region: Region
        :type Region: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param InternetUrl: Grafana private network address
        :type InternetUrl: str
        :param InternalUrl: Grafana public network address
        :type InternalUrl: str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        :param InstanceStatus: Status. Valid values: `1` (creating), `2` (running), `3` (abnormal), `4` (restarting), `5` (stopping), `6` (stopped), `7` (deleted).
        :type InstanceStatus: int
        :param TagSpecification: Instance tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: list of PrometheusTag
        :param Zone: Instance AZ
        :type Zone: str
        :param InstanceChargeType: Billing mode. Valid value: `1` (monthly subscription).
        :type InstanceChargeType: int
        :param VpcName: VPC name
        :type VpcName: str
        :param SubnetName: Subnet name
        :type SubnetName: str
        :param RegionId: Region ID
        :type RegionId: int
        :param RootUrl: The full URL used to access this instance
        :type RootUrl: str
        :param EnableSSO: Whether to enable SSO
        :type EnableSSO: bool
        :param Version: Version number
        :type Version: str
        :param EnableSSOCamCheck: Whether to enable CAM authentication during SSO
        :type EnableSSOCamCheck: bool
        """
        self.InstanceName = None
        self.InstanceId = None
        self.Region = None
        self.VpcId = None
        self.SubnetIds = None
        self.InternetUrl = None
        self.InternalUrl = None
        self.CreatedAt = None
        self.InstanceStatus = None
        self.TagSpecification = None
        self.Zone = None
        self.InstanceChargeType = None
        self.VpcName = None
        self.SubnetName = None
        self.RegionId = None
        self.RootUrl = None
        self.EnableSSO = None
        self.Version = None
        self.EnableSSOCamCheck = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.InternetUrl = params.get("InternetUrl")
        self.InternalUrl = params.get("InternalUrl")
        self.CreatedAt = params.get("CreatedAt")
        self.InstanceStatus = params.get("InstanceStatus")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.Zone = params.get("Zone")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        self.RegionId = params.get("RegionId")
        self.RootUrl = params.get("RootUrl")
        self.EnableSSO = params.get("EnableSSO")
        self.Version = params.get("Version")
        self.EnableSSOCamCheck = params.get("EnableSSOCamCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaIntegrationConfig(AbstractModel):
    """Grafana instance configuration

    """

    def __init__(self):
        r"""
        :param IntegrationId: Integration ID
        :type IntegrationId: str
        :param Kind: Integration type
        :type Kind: str
        :param Content: Integration content
        :type Content: str
        :param Description: Integration description
        :type Description: str
        :param GrafanaURL: Grafana redirection address
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        """
        self.IntegrationId = None
        self.Kind = None
        self.Content = None
        self.Description = None
        self.GrafanaURL = None


    def _deserialize(self, params):
        self.IntegrationId = params.get("IntegrationId")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        self.Description = params.get("Description")
        self.GrafanaURL = params.get("GrafanaURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaNotificationChannel(AbstractModel):
    """Grafana notification channel

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID
        :type ChannelId: str
        :param ChannelName: Channel name
        :type ChannelName: str
        :param Receivers: Array of notification channel template IDs
        :type Receivers: list of str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        :param UpdatedAt: Update time
        :type UpdatedAt: str
        :param OrgId: Default valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type OrgId: str
        :param ExtraOrgIds: Extra valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraOrgIds: list of str
        :param OrgIds: Valid organization. This parameter has been deprecated. Please use `OrganizationIds` instead.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrgIds: str
        :param OrganizationIds: All valid organizations in an alert channel
Note: This field may return null, indicating that no valid values can be obtained.
        :type OrganizationIds: str
        """
        self.ChannelId = None
        self.ChannelName = None
        self.Receivers = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.OrgId = None
        self.ExtraOrgIds = None
        self.OrgIds = None
        self.OrganizationIds = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.ChannelName = params.get("ChannelName")
        self.Receivers = params.get("Receivers")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.OrgId = params.get("OrgId")
        self.ExtraOrgIds = params.get("ExtraOrgIds")
        self.OrgIds = params.get("OrgIds")
        self.OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaPlugin(AbstractModel):
    """Grafana plugin

    """

    def __init__(self):
        r"""
        :param PluginId: Grafana plugin ID
        :type PluginId: str
        :param Version: Grafana plugin version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        """
        self.PluginId = None
        self.Version = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsRequest(AbstractModel):
    """InstallPlugins request structure.

    """

    def __init__(self):
        r"""
        :param Plugins: Plugin information
        :type Plugins: list of GrafanaPlugin
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        """
        self.Plugins = None
        self.InstanceId = None


    def _deserialize(self, params):
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = GrafanaPlugin()
                obj._deserialize(item)
                self.Plugins.append(obj)
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallPluginsResponse(AbstractModel):
    """InstallPlugins response structure.

    """

    def __init__(self):
        r"""
        :param PluginIds: ID of the installed plugin
Note: This field may return null, indicating that no valid values can be obtained.
        :type PluginIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PluginIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PluginIds = params.get("PluginIds")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Array of instance dimension combinations

    """

    def __init__(self):
        r"""
        :param Dimensions: Combination of instance dimensions
        :type Dimensions: list of Dimension
        """
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
        r"""
        :param InstanceGroupId: Instance group ID.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroupId: int
        :param InstanceGroupName: Instance group name.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceGroupName: str
        """
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
        r"""
        :param Id: Instance group ID
        :type Id: int
        :param Name: Instance group name
        :type Name: str
        """
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
        


class IntegrationConfiguration(AbstractModel):
    """Export integration configuration

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param Kind: Type
        :type Kind: str
        :param Content: Content
        :type Content: str
        :param Status: Status
        :type Status: int
        :param Category: Instance type
        :type Category: str
        :param InstanceDesc: Instance description
        :type InstanceDesc: str
        :param GrafanaDashboardURL: Dashboard URL
        :type GrafanaDashboardURL: str
        """
        self.Name = None
        self.Kind = None
        self.Content = None
        self.Status = None
        self.Category = None
        self.InstanceDesc = None
        self.GrafanaDashboardURL = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        self.Status = params.get("Status")
        self.Category = params.get("Category")
        self.InstanceDesc = params.get("InstanceDesc")
        self.GrafanaDashboardURL = params.get("GrafanaDashboardURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """Tags in K8s, which generally exist in the form of an array.

    """


class LogAlarmReq(AbstractModel):
    """Log alarm request information

    """

    def __init__(self):
        r"""
        :param InstanceId: APM instance ID
        :type InstanceId: str
        :param Filter: Search condition
        :type Filter: list of LogFilterInfo
        :param AlarmMerge: The switch to enable/disable alarm merging
        :type AlarmMerge: str
        :param AlarmMergeTime: Alarm merging time
        :type AlarmMergeTime: str
        """
        self.InstanceId = None
        self.Filter = None
        self.AlarmMerge = None
        self.AlarmMergeTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = LogFilterInfo()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.AlarmMerge = params.get("AlarmMerge")
        self.AlarmMergeTime = params.get("AlarmMergeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFilterInfo(AbstractModel):
    """Log alarm search condition structure

    """

    def __init__(self):
        r"""
        :param Key: Field name
        :type Key: str
        :param Operator: Comparison operator
        :type Operator: str
        :param Value: Field value
        :type Value: str
        """
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
        


class ManagementCommand(AbstractModel):
    """Prometheus agent management command line

    """

    def __init__(self):
        r"""
        :param Install: Agent installation command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Install: str
        :param Restart: Agent restart command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Restart: str
        :param Stop: Agent stop command
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stop: str
        :param StatusCheck: Agent status detection command
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusCheck: str
        :param LogCheck: Agent log detection command
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogCheck: str
        """
        self.Install = None
        self.Restart = None
        self.Stop = None
        self.StatusCheck = None
        self.LogCheck = None


    def _deserialize(self, params):
        self.Install = params.get("Install")
        self.Restart = params.get("Restart")
        self.Stop = params.get("Stop")
        self.StatusCheck = params.get("StatusCheck")
        self.LogCheck = params.get("LogCheck")
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
        r"""
        :param Namespace: Alarm policy type
        :type Namespace: str
        :param MetricName: Metric name
        :type MetricName: str
        :param Description: Metric display name
        :type Description: str
        :param Min: Minimum value
        :type Min: float
        :param Max: Maximum value
        :type Max: float
        :param Dimensions: Dimension list
        :type Dimensions: list of str
        :param Unit: Unit
        :type Unit: str
        :param MetricConfig: Metric configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type MetricConfig: :class:`tencentcloud.monitor.v20180724.models.MetricConfig`
        :param IsAdvanced: Whether it is an advanced metric. 1: Yes; 0: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsAdvanced: int
        :param IsOpen: Whether the advanced metric feature is enabled. 1: Yes; 0: No.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsOpen: int
        :param ProductId: Integration center product ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProductId: int
        """
        self.Namespace = None
        self.MetricName = None
        self.Description = None
        self.Min = None
        self.Max = None
        self.Dimensions = None
        self.Unit = None
        self.MetricConfig = None
        self.IsAdvanced = None
        self.IsOpen = None
        self.ProductId = None


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
        self.IsAdvanced = params.get("IsAdvanced")
        self.IsOpen = params.get("IsOpen")
        self.ProductId = params.get("ProductId")
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
        r"""
        :param Operator: Allowed operator
        :type Operator: list of str
        :param Period: Allowed data cycle in seconds
        :type Period: list of int
        :param ContinuePeriod: Allowed number of continuous cycles
        :type ContinuePeriod: list of int
        """
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
        r"""
        :param MetricName: Metric name
        :type MetricName: str
        :param Points: Monitoring data point
        :type Points: list of MetricDataPoint
        """
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
        r"""
        :param Dimensions: Combination of instance object dimensions
        :type Dimensions: list of Dimension
        :param Values: Data point list
        :type Values: list of Point
        """
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
        r"""
        :param MetricName: Metric name.
        :type MetricName: str
        :param Value: Metric value.
        :type Value: int
        """
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
        r"""
        :param En: Meaning of the metric in English
        :type En: str
        :param Zh: Meaning of the metric in Chinese
        :type Zh: str
        """
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
        r"""
        :param Namespace: Namespace. Each Tencent Cloud product has a namespace
        :type Namespace: str
        :param MetricName: Metric Name
        :type MetricName: str
        :param Unit: Unit used by the metric
        :type Unit: str
        :param UnitCname: Unit used by the metric
        :type UnitCname: str
        :param Period: Statistical period in seconds supported by the metric, such as 60 and 300
        :type Period: list of int
        :param Periods: Metric method during the statistical period
        :type Periods: list of PeriodsSt
        :param Meaning: Meaning of the statistical metric
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param Dimensions: Dimension description
        :type Dimensions: list of DimensionsDesc
        :param MetricCName: Metric name (in Chinese).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricCName: str
        :param MetricEName: Metric name (in English).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MetricEName: str
        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None
        self.MetricCName = None
        self.MetricEName = None


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
        self.MetricCName = params.get("MetricCName")
        self.MetricEName = params.get("MetricEName")
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
        r"""
        :param Key: Dimension
        :type Key: str
        :param Operator: Operator. Valid values: eq (equal to), ne (not equal to), in
        :type Operator: str
        :param Value: Dimension value. If `Operator` is `eq` or `ne`, only the first element will be used
        :type Value: list of str
        """
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
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param Name: Alarm notification rule name, which can contain up to 60 characters
        :type Name: str
        :param NoticeType: Notification type. Valid values: ALARM (for unresolved alarms), OK (for resolved alarms), ALL (for all alarms)
        :type NoticeType: str
        :param NoticeLanguage: Notification language. Valid values: zh-CN (Chinese), en-US (English)
        :type NoticeLanguage: str
        :param NoticeId: Alarm notification template ID
        :type NoticeId: str
        :param UserNotices: User notifications (up to 5)
        :type UserNotices: list of UserNotice
        :param URLNotices: Callback notifications (up to 3)
        :type URLNotices: list of URLNotice
        :param CLSNotices: The operation of pushing alarm notifications to CLS. Up to one CLS log topic can be configured.
        :type CLSNotices: list of CLSNotice
        :param PolicyIds: List of IDs of the alerting rules bound to an alarm notification template
        :type PolicyIds: list of str
        """
        self.Module = None
        self.Name = None
        self.NoticeType = None
        self.NoticeLanguage = None
        self.NoticeId = None
        self.UserNotices = None
        self.URLNotices = None
        self.CLSNotices = None
        self.PolicyIds = None


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
        if params.get("CLSNotices") is not None:
            self.CLSNotices = []
            for item in params.get("CLSNotices"):
                obj = CLSNotice()
                obj._deserialize(item)
                self.CLSNotices.append(obj)
        self.PolicyIds = params.get("PolicyIds")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyConditionRequest(AbstractModel):
    """ModifyAlarmPolicyCondition request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param ConditionTemplateId: ID of trigger condition template. This parameter can be left empty.
        :type ConditionTemplateId: int
        :param Condition: Metric trigger condition
        :type Condition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyCondition`
        :param EventCondition: Event trigger condition
        :type EventCondition: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyEventCondition`
        :param Filter: Global filter.
        :type Filter: :class:`tencentcloud.monitor.v20180724.models.AlarmPolicyFilter`
        :param GroupBy: Aggregation dimension list, which is used to specify which dimension keys data is grouped by.
        :type GroupBy: list of str
        :param LogAlarmReqInfo: Log alarm creation request parameters
        :type LogAlarmReqInfo: :class:`tencentcloud.monitor.v20180724.models.LogAlarmReq`
        :param NoticeIds: Template ID, which is dedicated to TMP.
        :type NoticeIds: list of str
        :param Enable: Status (`0`: Disabled; `1`: Enabled)
        :type Enable: int
        :param PolicyName: Name of the policy dedicated to TMP
        :type PolicyName: str
        :param EbSubject: The alert configured for an event
        :type EbSubject: str
        """
        self.Module = None
        self.PolicyId = None
        self.ConditionTemplateId = None
        self.Condition = None
        self.EventCondition = None
        self.Filter = None
        self.GroupBy = None
        self.LogAlarmReqInfo = None
        self.NoticeIds = None
        self.Enable = None
        self.PolicyName = None
        self.EbSubject = None


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
        if params.get("LogAlarmReqInfo") is not None:
            self.LogAlarmReqInfo = LogAlarmReq()
            self.LogAlarmReqInfo._deserialize(params.get("LogAlarmReqInfo"))
        self.NoticeIds = params.get("NoticeIds")
        self.Enable = params.get("Enable")
        self.PolicyName = params.get("PolicyName")
        self.EbSubject = params.get("EbSubject")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyInfoRequest(AbstractModel):
    """ModifyAlarmPolicyInfo request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param Key: Field to be modified. Valid values: NAME (policy name), REMARK (policy remarks)
        :type Key: str
        :param Value: Value after modification
        :type Value: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyNoticeRequest(AbstractModel):
    """ModifyAlarmPolicyNotice request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is specified as `monitor`.
        :type Module: str
        :param PolicyId: Alarm policy ID. If both `PolicyIds` and this parameter are returned, only `PolicyIds` takes effect.
        :type PolicyId: str
        :param NoticeIds: List of alarm notification template IDs.
        :type NoticeIds: list of str
        :param PolicyIds: Alarm policy ID array, which can be used to associate notification templates with multiple alarm policies. Max value: 30.
        :type PolicyIds: list of str
        """
        self.Module = None
        self.PolicyId = None
        self.NoticeIds = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.NoticeIds = params.get("NoticeIds")
        self.PolicyIds = params.get("PolicyIds")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyStatusRequest(AbstractModel):
    """ModifyAlarmPolicyStatus request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param Enable: Status. Valid values: 0 (disabled), 1 (enabled)
        :type Enable: int
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmPolicyTasksRequest(AbstractModel):
    """ModifyAlarmPolicyTasks request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name. Enter "monitor" here
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        :param TriggerTasks: List of tasks triggered by alarm policy. If this parameter is left empty, it indicates to unbind all tasks
        :type TriggerTasks: list of AlarmPolicyTriggerTask
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: ID of a policy group whose recipient needs to be modified.
        :type GroupId: int
        :param Module: Required. The value is fixed to monitor.
        :type Module: str
        :param ReceiverInfos: New recipient information. If this parameter is not configured, all recipients will be deleted.
        :type ReceiverInfos: list of ReceiverInfo
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGrafanaInstanceRequest(AbstractModel):
    """ModifyGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param InstanceName: TCMG instance name, such as “test”.
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGrafanaInstanceResponse(AbstractModel):
    """ModifyGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPolicyGroupCondition(AbstractModel):
    """Modification of the metric threshold condition passed in by the alarm policy group.

    """

    def __init__(self):
        r"""
        :param MetricId: Metric ID.
        :type MetricId: int
        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to.
        :type CalcType: int
        :param CalcValue: Threshold.
        :type CalcValue: str
        :param CalcPeriod: Data period of the detected metric.
        :type CalcPeriod: int
        :param ContinuePeriod: Number of consecutive periods.
        :type ContinuePeriod: int
        :param AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.
        :type RuleId: int
        """
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
        r"""
        :param EventId: Event ID.
        :type EventId: int
        :param AlarmNotifyType: Alarm sending and convergence type. The value 0 indicates that alarms are sent consecutively. The value 1 indicates that alarms are sent exponentially.
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: Alarm sending period in seconds. If the value is less than 0, no alarm will be triggered. If the value is 0, an alarm will be triggered only once. If the value is greater than 0, an alarm will be triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param RuleId: Rule ID. No filling means new addition while filling in ruleId means to modify existing rules.
        :type RuleId: int
        """
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param ViewName: Alarm type.
        :type ViewName: str
        :param GroupName: Policy group name.
        :type GroupName: str
        :param IsUnionRule: The 'AND' and 'OR' rules for metric alarms. The value 1 indicates 'AND', which means that an alarm will be triggered only when all rules are met. The value 0 indicates 'OR', which means that an alarm will be triggered when any rule is met.
        :type IsUnionRule: int
        :param Conditions: Metric alarm condition rules. No filling indicates that all existing metric alarm condition rules will be deleted.
        :type Conditions: list of ModifyPolicyGroupCondition
        :param EventConditions: Event alarm conditions. No filling indicates that all existing event alarm conditions will be deleted.
        :type EventConditions: list of ModifyPolicyGroupEventCondition
        :param ConditionTempGroupId: Template-based policy group ID.
        :type ConditionTempGroupId: int
        """
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
        r"""
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class ModifyPrometheusInstanceAttributesRequest(AbstractModel):
    """ModifyPrometheusInstanceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DataRetentionTime: Storage period. Valid values: 15, 30, 45. This parameter is not applicable to monthly subscribed instances.
        :type DataRetentionTime: int
        """
        self.InstanceName = None
        self.InstanceId = None
        self.DataRetentionTime = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.DataRetentionTime = params.get("DataRetentionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusInstanceAttributesResponse(AbstractModel):
    """ModifyPrometheusInstanceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusRecordRuleYamlRequest(AbstractModel):
    """ModifyPrometheusRecordRuleYaml request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Recording instance name
        :type Name: str
        :param Content: New content
        :type Content: str
        """
        self.InstanceId = None
        self.Name = None
        self.Content = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusRecordRuleYamlResponse(AbstractModel):
    """ModifyPrometheusRecordRuleYaml response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusTempRequest(AbstractModel):
    """ModifyPrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID
        :type TemplateId: str
        :param Template: Modified content
        :type Template: :class:`tencentcloud.monitor.v20180724.models.PrometheusTempModify`
        """
        self.TemplateId = None
        self.Template = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Template") is not None:
            self.Template = PrometheusTempModify()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTempResponse(AbstractModel):
    """ModifyPrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorTypeInfo(AbstractModel):
    """Monitoring type details

    """

    def __init__(self):
        r"""
        :param Id: Monitoring type ID
        :type Id: str
        :param Name: Monitoring type
        :type Name: str
        :param SortId: Sort order
        :type SortId: int
        """
        self.Id = None
        self.Name = None
        self.SortId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.SortId = params.get("SortId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTypeNamespace(AbstractModel):
    """Policy type

    """

    def __init__(self):
        r"""
        :param MonitorType: Monitor type
        :type MonitorType: str
        :param Namespace: Policy type value
        :type Namespace: str
        """
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
        


class NoticeBindPolicys(AbstractModel):
    """Binding between a notification template and a policy

    """

    def __init__(self):
        r"""
        :param NoticeId: Alert notification template ID
        :type NoticeId: str
        :param PolicyIds: List of IDs of the alerting rules bound to an alarm notification template
        :type PolicyIds: list of str
        """
        self.NoticeId = None
        self.PolicyIds = None


    def _deserialize(self, params):
        self.NoticeId = params.get("NoticeId")
        self.PolicyIds = params.get("PolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operator(AbstractModel):
    """Operators supported by the instance

    """

    def __init__(self):
        r"""
        :param Id: Operator ID
        :type Id: str
        :param Name: Operator name
        :type Name: str
        """
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
        


class PeriodsSt(AbstractModel):
    """Statistical method during the period

    """

    def __init__(self):
        r"""
        :param Period: Period
        :type Period: str
        :param StatType: Statistical method
        :type StatType: list of str
        """
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
        r"""
        :param Timestamp: Time point when this monitoring data point is generated
        :type Timestamp: int
        :param Value: Monitoring data point value
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: float
        """
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
        


class PolicyGroup(AbstractModel):
    """Policy group information

    """

    def __init__(self):
        r"""
        :param CanSetDefault: Whether the alarm policy can be set to default.
        :type CanSetDefault: bool
        :param GroupID: Alarm policy group ID.
        :type GroupID: int
        :param GroupName: Alarm policy group name.
        :type GroupName: str
        :param InsertTime: Creation time.
        :type InsertTime: int
        :param IsDefault: Whether the alarm policy is set to default.
        :type IsDefault: int
        :param Enable: Whether the alarm policy is enabled.
        :type Enable: bool
        :param LastEditUin: UIN of the last modifier.
        :type LastEditUin: int
        :param NoShieldedInstanceCount: Number of unshielded instances.
        :type NoShieldedInstanceCount: int
        :param ParentGroupID: Parent policy group ID.
        :type ParentGroupID: int
        :param ProjectID: Project ID.
        :type ProjectID: int
        :param ReceiverInfos: Alarm recipient information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverInfos: list of PolicyGroupReceiverInfo
        :param Remark: Remarks.
        :type Remark: str
        :param UpdateTime: Modification time.
        :type UpdateTime: int
        :param TotalInstanceCount: The total number of associated instances.
        :type TotalInstanceCount: int
        :param ViewName: View.
        :type ViewName: str
        :param IsUnionRule: Whether the logical relationship between rules is AND.
        :type IsUnionRule: int
        """
        self.CanSetDefault = None
        self.GroupID = None
        self.GroupName = None
        self.InsertTime = None
        self.IsDefault = None
        self.Enable = None
        self.LastEditUin = None
        self.NoShieldedInstanceCount = None
        self.ParentGroupID = None
        self.ProjectID = None
        self.ReceiverInfos = None
        self.Remark = None
        self.UpdateTime = None
        self.TotalInstanceCount = None
        self.ViewName = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.CanSetDefault = params.get("CanSetDefault")
        self.GroupID = params.get("GroupID")
        self.GroupName = params.get("GroupName")
        self.InsertTime = params.get("InsertTime")
        self.IsDefault = params.get("IsDefault")
        self.Enable = params.get("Enable")
        self.LastEditUin = params.get("LastEditUin")
        self.NoShieldedInstanceCount = params.get("NoShieldedInstanceCount")
        self.ParentGroupID = params.get("ParentGroupID")
        self.ProjectID = params.get("ProjectID")
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = PolicyGroupReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        self.Remark = params.get("Remark")
        self.UpdateTime = params.get("UpdateTime")
        self.TotalInstanceCount = params.get("TotalInstanceCount")
        self.ViewName = params.get("ViewName")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyGroupReceiverInfo(AbstractModel):
    """Information on recipients in the policy template list (API v2018)

    """

    def __init__(self):
        r"""
        :param EndTime: End time of a valid time period.
        :type EndTime: int
        :param NeedSendNotice: Whether it is required to send notifications.
        :type NeedSendNotice: int
        :param NotifyWay: Alarm receiving channel.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NotifyWay: list of str
        :param PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param ReceiverGroupList: Message recipient group list.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverGroupList: list of int
        :param ReceiverType: Recipient type.
        :type ReceiverType: str
        :param ReceiverUserList: Recipient list. The list of recipient IDs that is queried by a platform API.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReceiverUserList: list of int
        :param RecoverNotify: Alarm resolution notification method.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RecoverNotify: list of str
        :param RoundInterval: Alarm call interval per round in seconds.
        :type RoundInterval: int
        :param RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param SendFor: Alarm call notification time. Valid values: `OCCUR` (indicating that a notification is sent when the alarm is triggered) and `RECOVER` (indicating that a notification is sent when the alarm is resolved).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SendFor: list of str
        :param StartTime: Start time of a valid time period.
        :type StartTime: int
        :param UIDList: UID of the alarm call recipient.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UIDList: list of int
        """
        self.EndTime = None
        self.NeedSendNotice = None
        self.NotifyWay = None
        self.PersonInterval = None
        self.ReceiverGroupList = None
        self.ReceiverType = None
        self.ReceiverUserList = None
        self.RecoverNotify = None
        self.RoundInterval = None
        self.RoundNumber = None
        self.SendFor = None
        self.StartTime = None
        self.UIDList = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.NotifyWay = params.get("NotifyWay")
        self.PersonInterval = params.get("PersonInterval")
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverType = params.get("ReceiverType")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.RecoverNotify = params.get("RecoverNotify")
        self.RoundInterval = params.get("RoundInterval")
        self.RoundNumber = params.get("RoundNumber")
        self.SendFor = params.get("SendFor")
        self.StartTime = params.get("StartTime")
        self.UIDList = params.get("UIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgent(AbstractModel):
    """prometheus agent

    """

    def __init__(self):
        r"""
        :param Name: Agent name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param AgentId: Agent ID
        :type AgentId: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Ipv4: Agent IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv4: str
        :param HeartbeatTime: Heartbeat time
Note: This field may return null, indicating that no valid values can be obtained.
        :type HeartbeatTime: str
        :param LastError: Last error
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastError: str
        :param AgentVersion: Agent version
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentVersion: str
        :param Status: Agent status
        :type Status: int
        """
        self.Name = None
        self.AgentId = None
        self.InstanceId = None
        self.Ipv4 = None
        self.HeartbeatTime = None
        self.LastError = None
        self.AgentVersion = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AgentId = params.get("AgentId")
        self.InstanceId = params.get("InstanceId")
        self.Ipv4 = params.get("Ipv4")
        self.HeartbeatTime = params.get("HeartbeatTime")
        self.LastError = params.get("LastError")
        self.AgentVersion = params.get("AgentVersion")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertManagerConfig(AbstractModel):
    """Self-built AlertManager configuration used by the alert channel

    """

    def __init__(self):
        r"""
        :param Url: AlertManager URL
        :type Url: str
        :param ClusterType: Type of the cluster where AlertManager is deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: str
        :param ClusterId: ID of the cluster where AlertManager is deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self.Url = None
        self.ClusterType = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertPolicyItem(AbstractModel):
    """TMP alerting rule instance

    """

    def __init__(self):
        r"""
        :param Name: Rule name
        :type Name: str
        :param Rules: List of rules
        :type Rules: list of PrometheusAlertRule
        :param Id: Alerting rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param TemplateId: If the alert comes from a template, `TemplateId` is the template ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param Notification: Alert channel, which may be returned as null if used in a template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Notification: :class:`tencentcloud.monitor.v20180724.models.PrometheusNotificationItem`
        :param UpdatedAt: Last modification time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param ClusterId: If the alerting rule comes from the user cluster CRD resource definition, `ClusterId` is the cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self.Name = None
        self.Rules = None
        self.Id = None
        self.TemplateId = None
        self.Notification = None
        self.UpdatedAt = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Id = params.get("Id")
        self.TemplateId = params.get("TemplateId")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotificationItem()
            self.Notification._deserialize(params.get("Notification"))
        self.UpdatedAt = params.get("UpdatedAt")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """Prometheus alerting rule

    """

    def __init__(self):
        r"""
        :param Name: Rule name
        :type Name: str
        :param Rule: Prometheus statement
        :type Rule: str
        :param Labels: Additional tags
        :type Labels: list of Label
        :param Template: Alert sending template
        :type Template: str
        :param For: Duration
        :type For: str
        :param Describe: Rule description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param Annotations: See `annotations` in the Prometheus rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type Annotations: list of Label
        :param RuleState: Alerting rule status
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleState: int
        """
        self.Name = None
        self.Rule = None
        self.Labels = None
        self.Template = None
        self.For = None
        self.Describe = None
        self.Annotations = None
        self.RuleState = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.Template = params.get("Template")
        self.For = params.get("For")
        self.Describe = params.get("Describe")
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfigItem(AbstractModel):
    """Prometheus configuration

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param Config: Configuration content
        :type Config: str
        :param TemplateId: If the configuration comes from a template, this parameter is the template ID, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        """
        self.Name = None
        self.Config = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Config = params.get("Config")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceGrantInfo(AbstractModel):
    """Instance authorization information

    """

    def __init__(self):
        r"""
        :param HasChargeOperation: Whether there is permission to operate on the billing information. Valid values: 1 (yes), 2 (no).
        :type HasChargeOperation: int
        :param HasVpcDisplay: Whether there is permission to display the VPC information. Valid values: 1 (yes), 2 (no).
        :type HasVpcDisplay: int
        :param HasGrafanaStatusChange: Whether there is permission to change the Grafana status. Valid values: 1 (yes), 2 (no).
        :type HasGrafanaStatusChange: int
        :param HasAgentManage: Whether there is permission to manage agents. Valid values: 1 (yes), 2 (no).
        :type HasAgentManage: int
        :param HasTkeManage: Whether there is permission to manage TKE integrations. Valid values: 1 (yes), 2 (no).
        :type HasTkeManage: int
        :param HasApiOperation: Whether there is permission to display the API information. Valid values: 1 (yes), 2 (no).
        :type HasApiOperation: int
        """
        self.HasChargeOperation = None
        self.HasVpcDisplay = None
        self.HasGrafanaStatusChange = None
        self.HasAgentManage = None
        self.HasTkeManage = None
        self.HasApiOperation = None


    def _deserialize(self, params):
        self.HasChargeOperation = params.get("HasChargeOperation")
        self.HasVpcDisplay = params.get("HasVpcDisplay")
        self.HasGrafanaStatusChange = params.get("HasGrafanaStatusChange")
        self.HasAgentManage = params.get("HasAgentManage")
        self.HasTkeManage = params.get("HasTkeManage")
        self.HasApiOperation = params.get("HasApiOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceTenantUsage(AbstractModel):
    """TMP usage information

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param CalcDate: Billing cycle
Note: This field may return null, indicating that no valid values can be obtained.
        :type CalcDate: str
        :param Total: Total usage
Note: This field may return null, indicating that no valid values can be obtained.
        :type Total: float
        :param Basic: Usage of basic (free) metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type Basic: float
        :param Fee: Usage of paid metrics
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fee: float
        """
        self.InstanceId = None
        self.CalcDate = None
        self.Total = None
        self.Basic = None
        self.Fee = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CalcDate = params.get("CalcDate")
        self.Total = params.get("Total")
        self.Basic = params.get("Basic")
        self.Fee = params.get("Fee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesItem(AbstractModel):
    """Prometheus service response body

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param InstanceName: Instance name.
        :type InstanceName: str
        :param InstanceChargeType: Instance billing mode. Valid values:
<ul>
<li>2: Monthly subscription</li>
<li>3: Pay-as-you-go</li>
</ul>
        :type InstanceChargeType: int
        :param RegionId: Region ID
        :type RegionId: int
        :param Zone: AZ
        :type Zone: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param InstanceStatus: Instance status. Valid values:
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
        :param GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param CreatedAt: Creation time
        :type CreatedAt: str
        :param EnableGrafana: Whether Grafana is enabled
<li>0: Disabled</li>
<li>1: Enabled</li>
        :type EnableGrafana: int
        :param IPv4Address: Instance IPv4 address
Note: This field may return null, indicating that no valid values can be obtained.
        :type IPv4Address: str
        :param TagSpecification: List of tags associated with the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagSpecification: list of PrometheusTag
        :param ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param ChargeStatus: Billing status
<ul>
<li>1: Normal</li>
<li>2: Expired</li>
<li>3: Terminated</li>
<li>4: Assigning</li>
<li>5: Assignment failed</li>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param AutoRenewFlag: Auto-renewal flag
<ul>
<li>0: Auto-renewal not enabled</li>
<li>1: Auto-renewal enabled</li>
<li>2: Auto-renewal prohibited</li>
<li>-1: Invalid</ii>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param IsNearExpire: Expiring soon
<ul>
<li>0: No</li>
<li>1: Yes</li>
</ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsNearExpire: int
        :param AuthToken: The token required for data writing
Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthToken: str
        :param RemoteWrite: Prometheus remote write address
Note: This field may return null, indicating that no valid values can be obtained.
        :type RemoteWrite: str
        :param ApiRootPath: Prometheus HTTP API root address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApiRootPath: str
        :param ProxyAddress: Proxy address
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyAddress: str
        :param GrafanaStatus: Grafana status
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
        :param GrafanaIpWhiteList: Grafana IP allowlist, where IPs are separated by comma.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaIpWhiteList: str
        :param Grant: Instance authorization information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Grant: :class:`tencentcloud.monitor.v20180724.models.PrometheusInstanceGrantInfo`
        :param GrafanaInstanceId: ID of the bound Grafana instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaInstanceId: str
        :param AlertRuleLimit: The alert rule limit
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertRuleLimit: int
        :param RecordingRuleLimit: The recording rule limit
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordingRuleLimit: int
        :param MigrationType: Migration status. 0: Not migrating; 1: Migrating from source instance; 2: Migrating to target instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrationType: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.RegionId = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.DataRetentionTime = None
        self.InstanceStatus = None
        self.GrafanaURL = None
        self.CreatedAt = None
        self.EnableGrafana = None
        self.IPv4Address = None
        self.TagSpecification = None
        self.ExpireTime = None
        self.ChargeStatus = None
        self.SpecName = None
        self.AutoRenewFlag = None
        self.IsNearExpire = None
        self.AuthToken = None
        self.RemoteWrite = None
        self.ApiRootPath = None
        self.ProxyAddress = None
        self.GrafanaStatus = None
        self.GrafanaIpWhiteList = None
        self.Grant = None
        self.GrafanaInstanceId = None
        self.AlertRuleLimit = None
        self.RecordingRuleLimit = None
        self.MigrationType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.RegionId = params.get("RegionId")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DataRetentionTime = params.get("DataRetentionTime")
        self.InstanceStatus = params.get("InstanceStatus")
        self.GrafanaURL = params.get("GrafanaURL")
        self.CreatedAt = params.get("CreatedAt")
        self.EnableGrafana = params.get("EnableGrafana")
        self.IPv4Address = params.get("IPv4Address")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = PrometheusTag()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.ExpireTime = params.get("ExpireTime")
        self.ChargeStatus = params.get("ChargeStatus")
        self.SpecName = params.get("SpecName")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.IsNearExpire = params.get("IsNearExpire")
        self.AuthToken = params.get("AuthToken")
        self.RemoteWrite = params.get("RemoteWrite")
        self.ApiRootPath = params.get("ApiRootPath")
        self.ProxyAddress = params.get("ProxyAddress")
        self.GrafanaStatus = params.get("GrafanaStatus")
        self.GrafanaIpWhiteList = params.get("GrafanaIpWhiteList")
        if params.get("Grant") is not None:
            self.Grant = PrometheusInstanceGrantInfo()
            self.Grant._deserialize(params.get("Grant"))
        self.GrafanaInstanceId = params.get("GrafanaInstanceId")
        self.AlertRuleLimit = params.get("AlertRuleLimit")
        self.RecordingRuleLimit = params.get("RecordingRuleLimit")
        self.MigrationType = params.get("MigrationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstancesOverview(AbstractModel):
    """TMP v2 instance overview

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param InstanceStatus: Running status. Valid values: `1` (creating); `2` (running); `3` (abnormal); `4` (restarting); `5` (terminating); `6` (stopped); `7` (deleted).
        :type InstanceStatus: int
        :param ChargeStatus: Billing status. Valid values: `1` (normal); `2` (expired); `3` (terminated); `4` (assigning); `5` (failed to assign)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeStatus: int
        :param EnableGrafana: Whether Grafana is enabled. Valid values: `0` (no); `1` (yes).
        :type EnableGrafana: int
        :param GrafanaURL: Grafana dashboard URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type GrafanaURL: str
        :param InstanceChargeType: Instance payment type. Valid values: `1` (trial edition); `2` (prepaid)
        :type InstanceChargeType: int
        :param SpecName: Specification name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param DataRetentionTime: Storage period
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataRetentionTime: int
        :param ExpireTime: Expiration time of the purchased instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param AutoRenewFlag: Auto-renewal flag. Valid values: `0` (auto-renewal not enabled); `1` (auto-renewal enabled); `2` (auto-renewal prohibited); `-1` (invalid).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenewFlag: int
        :param BoundTotal: Total number of bound clusters
        :type BoundTotal: int
        :param BoundNormal: Total number of bound clusters in the normal status
        :type BoundNormal: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceStatus = None
        self.ChargeStatus = None
        self.EnableGrafana = None
        self.GrafanaURL = None
        self.InstanceChargeType = None
        self.SpecName = None
        self.DataRetentionTime = None
        self.ExpireTime = None
        self.AutoRenewFlag = None
        self.BoundTotal = None
        self.BoundNormal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.ChargeStatus = params.get("ChargeStatus")
        self.EnableGrafana = params.get("EnableGrafana")
        self.GrafanaURL = params.get("GrafanaURL")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.SpecName = params.get("SpecName")
        self.DataRetentionTime = params.get("DataRetentionTime")
        self.ExpireTime = params.get("ExpireTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.BoundTotal = params.get("BoundTotal")
        self.BoundNormal = params.get("BoundNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotificationItem(AbstractModel):
    """Alert notification channel configuration

    """

    def __init__(self):
        r"""
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param Type: Channel type. Default value: `amp`. Valid values:
`amp`
`webhook`
`alertmanager`
        :type Type: str
        :param WebHook: If `Type` is `webhook`, this field is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WebHook: str
        :param AlertManager: If `Type` is `alertmanager`, this field is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertManager: :class:`tencentcloud.monitor.v20180724.models.PrometheusAlertManagerConfig`
        :param RepeatInterval: Convergence time
        :type RepeatInterval: str
        :param TimeRangeStart: Effect start time
        :type TimeRangeStart: str
        :param TimeRangeEnd: Effect end time
        :type TimeRangeEnd: str
        :param NotifyWay: Alert notification channel. Valid values: `SMS`, `EMAIL`, `CALL`, `WECHAT`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NotifyWay: list of str
        :param ReceiverGroups: Alert recipient group (user group)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReceiverGroups: list of str
        :param PhoneNotifyOrder: Alert call sequence.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneNotifyOrder: list of int non-negative
        :param PhoneCircleTimes: Number of alert calls.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleTimes: int
        :param PhoneInnerInterval: Alert call interval within a cycle in seconds.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneInnerInterval: int
        :param PhoneCircleInterval: Alert call cycle interval in seconds.
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleInterval: int
        :param PhoneArriveNotice: Alert call receipt notification
Note: If `NotifyWay` is `CALL`, this parameter will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PhoneArriveNotice: bool
        """
        self.Enabled = None
        self.Type = None
        self.WebHook = None
        self.AlertManager = None
        self.RepeatInterval = None
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.NotifyWay = None
        self.ReceiverGroups = None
        self.PhoneNotifyOrder = None
        self.PhoneCircleTimes = None
        self.PhoneInnerInterval = None
        self.PhoneCircleInterval = None
        self.PhoneArriveNotice = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Type = params.get("Type")
        self.WebHook = params.get("WebHook")
        if params.get("AlertManager") is not None:
            self.AlertManager = PrometheusAlertManagerConfig()
            self.AlertManager._deserialize(params.get("AlertManager"))
        self.RepeatInterval = params.get("RepeatInterval")
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self.PhoneCircleTimes = params.get("PhoneCircleTimes")
        self.PhoneInnerInterval = params.get("PhoneInnerInterval")
        self.PhoneCircleInterval = params.get("PhoneCircleInterval")
        self.PhoneArriveNotice = params.get("PhoneArriveNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRecordRuleYamlItem(AbstractModel):
    """Details of the Prometheus recording rule instance, including the cluster ID.

    """

    def __init__(self):
        r"""
        :param Name: Instance name
        :type Name: str
        :param UpdateTime: Last update time
        :type UpdateTime: str
        :param TemplateId: YAML content
        :type TemplateId: str
        :param Content: If the recording rule comes from a template, `TemplateId` is the template ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: str
        :param ClusterId: If the recording rule comes from the user cluster CRD resource definition, `ClusterId` is the cluster ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        """
        self.Name = None
        self.UpdateTime = None
        self.TemplateId = None
        self.Content = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.Content = params.get("Content")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRuleKV(AbstractModel):
    """KV parameter of the Prometheus alerting rule

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRuleSet(AbstractModel):
    """Set of Prometheus alerting rules

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RuleName: Rule name
        :type RuleName: str
        :param RuleState: Rule status code
        :type RuleState: int
        :param Type: Rule category
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param Labels: List of rule tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of PrometheusRuleKV
        :param Annotations: List of rule annotations
Note: This field may return null, indicating that no valid values can be obtained.
        :type Annotations: list of PrometheusRuleKV
        :param Expr: Rule expression
Note: This field may return null, indicating that no valid values can be obtained.
        :type Expr: str
        :param Duration: Rule alert duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: str
        :param Receivers: List of alert recipient groups
Note: This field may return null, indicating that no valid values can be obtained.
        :type Receivers: list of str
        :param Health: Rule status. Valid values:
<li>unknown: Unknown</li>
<li>pending: Loading</li>
<li>ok: Running</li>
<li>err: Error</li>
        :type Health: str
        :param CreatedAt: Rule creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param UpdatedAt: Rule update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        """
        self.RuleId = None
        self.RuleName = None
        self.RuleState = None
        self.Type = None
        self.Labels = None
        self.Annotations = None
        self.Expr = None
        self.Duration = None
        self.Receivers = None
        self.Health = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleState = params.get("RuleState")
        self.Type = params.get("Type")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Expr = params.get("Expr")
        self.Duration = params.get("Duration")
        self.Receivers = params.get("Receivers")
        self.Health = params.get("Health")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusScrapeJob(AbstractModel):
    """Prometheus scrape task

    """

    def __init__(self):
        r"""
        :param Name: Task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param AgentId: Agent ID
        :type AgentId: str
        :param JobId: Task ID
        :type JobId: str
        :param Config: Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Config: str
        """
        self.Name = None
        self.AgentId = None
        self.JobId = None
        self.Config = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AgentId = params.get("AgentId")
        self.JobId = params.get("JobId")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTag(AbstractModel):
    """TMP tag

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemp(AbstractModel):
    """Template instance

    """

    def __init__(self):
        r"""
        :param Name: Template name
        :type Name: str
        :param Level: Template dimension. Valid values:
`instance`
`cluster`
        :type Level: str
        :param Describe: Template description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param RecordRules: This parameter is valid if `Level` is `instance`.
List of recording rules in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordRules: list of PrometheusConfigItem
        :param ServiceMonitors: This parameter is valid if `Level` is `cluster`.
List of ServiceMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceMonitors: list of PrometheusConfigItem
        :param PodMonitors: This parameter is valid if `Level` is `cluster`.
List of PodMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodMonitors: list of PrometheusConfigItem
        :param RawJobs: This parameter is valid if `Level` is `cluster`.
List of RawJob rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawJobs: list of PrometheusConfigItem
        :param TemplateId: Template ID, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TemplateId: str
        :param UpdateTime: Last update time, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param Version: The current version, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param IsDefault: Whether it is the default template provided by the system, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDefault: bool
        :param AlertDetailRules: This parameter is valid if `Level` is `instance`.
List of alert configurations in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        :param TargetsTotal: Number of associated instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetsTotal: int
        """
        self.Name = None
        self.Level = None
        self.Describe = None
        self.RecordRules = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.TemplateId = None
        self.UpdateTime = None
        self.Version = None
        self.IsDefault = None
        self.AlertDetailRules = None
        self.TargetsTotal = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Describe = params.get("Describe")
        if params.get("RecordRules") is not None:
            self.RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RecordRules.append(obj)
        if params.get("ServiceMonitors") is not None:
            self.ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self.PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self.RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RawJobs.append(obj)
        self.TemplateId = params.get("TemplateId")
        self.UpdateTime = params.get("UpdateTime")
        self.Version = params.get("Version")
        self.IsDefault = params.get("IsDefault")
        if params.get("AlertDetailRules") is not None:
            self.AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
        self.TargetsTotal = params.get("TargetsTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTempModify(AbstractModel):
    """Modifiable items in the TMP template

    """

    def __init__(self):
        r"""
        :param Name: Name
        :type Name: str
        :param Describe: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Describe: str
        :param ServiceMonitors: This parameter is valid if `Level` is `cluster`.
List of ServiceMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceMonitors: list of PrometheusConfigItem
        :param PodMonitors: This parameter is valid if `Level` is `cluster`.
List of PodMonitor rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodMonitors: list of PrometheusConfigItem
        :param RawJobs: This parameter is valid if `Level` is `cluster`.
List of RawJob rules in the template.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RawJobs: list of PrometheusConfigItem
        :param RecordRules: This parameter is valid if `Level` is `instance`.
List of recording rules in the template
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordRules: list of PrometheusConfigItem
        :param AlertDetailRules: Modification content, which is valid only if template type is `Alert`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        """
        self.Name = None
        self.Describe = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.RecordRules = None
        self.AlertDetailRules = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Describe = params.get("Describe")
        if params.get("ServiceMonitors") is not None:
            self.ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self.PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self.RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RawJobs.append(obj)
        if params.get("RecordRules") is not None:
            self.RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RecordRules.append(obj)
        if params.get("AlertDetailRules") is not None:
            self.AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """Sync target of the TMP template

    """

    def __init__(self):
        r"""
        :param Region: Target region
        :type Region: str
        :param InstanceId: Target instance
        :type InstanceId: str
        :param ClusterId: Cluster ID, which is required only if the `Level` of the collection template is `cluster`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param SyncTime: Last sync time, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SyncTime: str
        :param Version: The currently used template version, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param ClusterType: Cluster type, which is required only if the `Level` of the collection template is `cluster`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterType: str
        :param InstanceName: Instance name, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param ClusterName: Cluster name, which is used as an output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        """
        self.Region = None
        self.InstanceId = None
        self.ClusterId = None
        self.SyncTime = None
        self.Version = None
        self.ClusterType = None
        self.InstanceName = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.ClusterId = params.get("ClusterId")
        self.SyncTime = params.get("SyncTime")
        self.Version = params.get("Version")
        self.ClusterType = params.get("ClusterType")
        self.InstanceName = params.get("InstanceName")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusZoneItem(AbstractModel):
    """Region information returned by `PrometheusZoneItem`

    """

    def __init__(self):
        r"""
        :param Zone: AZ
        :type Zone: str
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param ZoneState: AZ status. Valid values: `0`(Unavailable), `1` (Available).
        :type ZoneState: int
        :param RegionId: Region ID
        :type RegionId: int
        :param ZoneName: AZ name
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneState = None
        self.RegionId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        self.RegionId = params.get("RegionId")
        self.ZoneName = params.get("ZoneName")
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
        r"""
        :param Metrics: A group of metrics and data.
        :type Metrics: list of MetricDatum
        :param AnnounceIp: IP address that is automatically specified when monitoring data is reported.
        :type AnnounceIp: str
        :param AnnounceTimestamp: Timestamp that is automatically specified when monitoring data is reported.
        :type AnnounceTimestamp: int
        :param AnnounceInstance: IP address or product instance ID that is automatically specified when monitoring data is reported.
        :type AnnounceInstance: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReceiverInfo(AbstractModel):
    """Recipient information.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the alarm period. Value range: [0,86400). Convert the Unix timestamp to Beijing time and then remove the date. For example, 7200 indicates “10:0:0”.
        :type StartTime: int
        :param EndTime: End time of the alarm period. The meaning is the same as that of StartTime.
        :type EndTime: int
        :param NotifyWay: Alarm notification method. Valid values: "SMS", "SITE", "EMAIL", "CALL", and "WECHAT".
        :type NotifyWay: list of str
        :param ReceiverType: Recipient type. Valid values: group and user.
        :type ReceiverType: str
        :param Id: ReceiverId
        :type Id: int
        :param SendFor: Alarm call notification time. Valid values: OCCUR (indicating that a notice is sent when the alarm is triggered) and RECOVER (indicating that a notice is sent when the alarm is recovered).
        :type SendFor: list of str
        :param UidList: UID of the phone call alarm.
        :type UidList: list of int
        :param RoundNumber: Number of alarm call rounds.
        :type RoundNumber: int
        :param PersonInterval: Alarm call intervals for individuals in seconds.
        :type PersonInterval: int
        :param RoundInterval: Intervals of alarm call rounds in seconds.
        :type RoundInterval: int
        :param RecoverNotify: Notification method when an alarm is recovered. Valid value: SMS.
        :type RecoverNotify: list of str
        :param NeedSendNotice: Whether to send an alarm call delivery notice. The value 0 indicates that no notice needs to be sent. The value 1 indicates that a notice needs to be sent.
        :type NeedSendNotice: int
        :param ReceiverGroupList: Recipient group list. The list of recipient group IDs that is queried by API.
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: Recipient list. The list of recipient IDs that is queried by API.
        :type ReceiverUserList: list of int
        :param ReceiveLanguage: Language of received alarms. Enumerated values: zh-CN and en-US.
        :type ReceiveLanguage: str
        """
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
        


class RecordingRuleSet(AbstractModel):
    """Response structure information of the Prometheus recording rule

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RuleState: Rule status code
        :type RuleState: int
        :param Name: Group name
        :type Name: str
        :param Group: Rule group
        :type Group: str
        :param Total: Number of rules
        :type Total: int
        :param CreatedAt: Rule creation time
        :type CreatedAt: str
        :param UpdatedAt: Rule update time
        :type UpdatedAt: str
        :param RuleName: Rule name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleName: str
        """
        self.RuleId = None
        self.RuleState = None
        self.Name = None
        self.Group = None
        self.Total = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleState = params.get("RuleState")
        self.Name = params.get("Name")
        self.Group = params.get("Group")
        self.Total = params.get("Total")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeGrafanaInstanceRequest(AbstractModel):
    """ResumeGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeGrafanaInstanceResponse(AbstractModel):
    """ResumeGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunPrometheusInstanceRequest(AbstractModel):
    """RunPrometheusInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SubnetId: Subnet ID. Initialization is performed with the subnet used by the instance by default and can also be performed with the subnet passed in by this parameter.
        :type SubnetId: str
        """
        self.InstanceId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunPrometheusInstanceResponse(AbstractModel):
    """RunPrometheusInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg request structure.

    """

    def __init__(self):
        r"""
        :param Module: API component name. The value for the current API is monitor.
        :type Module: str
        :param PolicyId: Message policy ID, which is configured on the custom message page of Cloud Monitor.
        :type PolicyId: str
        :param Msg: Custom message content that a user wants to send.
        :type Msg: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ServiceDiscoveryItem(AbstractModel):
    """Prometheus scrape configuration information

    """

    def __init__(self):
        r"""
        :param Name: Scrape configuration name
        :type Name: str
        :param Namespace: Namespace of the scrape configuration
        :type Namespace: str
        :param Kind: Scrape configuration type: ServiceMonitor/PodMonitor
        :type Kind: str
        :param NamespaceSelector: Namespace selection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type NamespaceSelector: str
        :param Selector: Label selection method
Note: This field may return null, indicating that no valid values can be obtained.
        :type Selector: str
        :param Endpoints: `Endpoints` information (PodMonitor does not have this parameter)
        :type Endpoints: str
        :param Yaml: Scrape configuration information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Yaml: str
        """
        self.Name = None
        self.Namespace = None
        self.Kind = None
        self.NamespaceSelector = None
        self.Selector = None
        self.Endpoints = None
        self.Yaml = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Kind = params.get("Kind")
        self.NamespaceSelector = params.get("NamespaceSelector")
        self.Selector = params.get("Selector")
        self.Endpoints = params.get("Endpoints")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultAlarmPolicyRequest(AbstractModel):
    """SetDefaultAlarmPolicy request structure.

    """

    def __init__(self):
        r"""
        :param Module: Module name, which is fixed at "monitor"
        :type Module: str
        :param PolicyId: Alarm policy ID
        :type PolicyId: str
        """
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncPrometheusTempRequest(AbstractModel):
    """SyncPrometheusTemp request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Instance ID
        :type TemplateId: str
        :param Targets: Sync target
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self.TemplateId = None
        self.Targets = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTempResponse(AbstractModel):
    """SyncPrometheusTemp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInstance(AbstractModel):
    """Instance tag information of the alarm policy

    """

    def __init__(self):
        r"""
        :param Key: Tag key
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Tag value
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Value: str
        :param InstanceSum: Number of instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceSum: int
        :param ServiceType: Service type, for example, CVM
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param RegionId: Region ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RegionId: str
        :param BindingStatus: Binding status. 2: bound; 1: binding
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BindingStatus: int
        :param TagStatus: Tag status. 2: existent; 1: nonexistent
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagStatus: int
        """
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
        


class TaskStepInfo(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
        :param Step: Step name
        :type Step: str
        :param LifeState: Lifecycle
`pending`
`running`
`success`
`failed`
        :type LifeState: str
        :param StartAt: Step start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartAt: str
        :param EndAt: Step end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndAt: str
        :param FailedMsg: If `LifeState` is `failed`, this field displays the error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedMsg: str
        """
        self.Step = None
        self.LifeState = None
        self.StartAt = None
        self.EndAt = None
        self.FailedMsg = None


    def _deserialize(self, params):
        self.Step = params.get("Step")
        self.LifeState = params.get("LifeState")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        self.FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateGroup(AbstractModel):
    """Template list

    """

    def __init__(self):
        r"""
        :param Conditions: Metric alarm rules.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Conditions: list of Condition
        :param EventConditions: Event alarm rules.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EventConditions: list of EventCondition
        :param PolicyGroups: The associated alarm policy groups.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PolicyGroups: list of PolicyGroup
        :param GroupID: Template-based policy group ID.
        :type GroupID: int
        :param GroupName: Template-based policy group name.
        :type GroupName: str
        :param InsertTime: Creation time.
        :type InsertTime: int
        :param LastEditUin: UIN of the last modifier.
        :type LastEditUin: int
        :param Remark: Remarks.
        :type Remark: str
        :param UpdateTime: Update time.
        :type UpdateTime: int
        :param ViewName: View.
        :type ViewName: str
        :param IsUnionRule: Whether the logical relationship between rules is AND.
        :type IsUnionRule: int
        """
        self.Conditions = None
        self.EventConditions = None
        self.PolicyGroups = None
        self.GroupID = None
        self.GroupName = None
        self.InsertTime = None
        self.LastEditUin = None
        self.Remark = None
        self.UpdateTime = None
        self.ViewName = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = Condition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = EventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        if params.get("PolicyGroups") is not None:
            self.PolicyGroups = []
            for item in params.get("PolicyGroups"):
                obj = PolicyGroup()
                obj._deserialize(item)
                self.PolicyGroups.append(obj)
        self.GroupID = params.get("GroupID")
        self.GroupName = params.get("GroupName")
        self.InsertTime = params.get("InsertTime")
        self.LastEditUin = params.get("LastEditUin")
        self.Remark = params.get("Remark")
        self.UpdateTime = params.get("UpdateTime")
        self.ViewName = params.get("ViewName")
        self.IsUnionRule = params.get("IsUnionRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminatePrometheusInstancesRequest(AbstractModel):
    """TerminatePrometheusInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminatePrometheusInstancesResponse(AbstractModel):
    """TerminatePrometheusInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class URLNotice(AbstractModel):
    """Cloud Monitor alarm notification template - callback notification details

    """

    def __init__(self):
        r"""
        :param URL: Callback URL, which can contain up to 256 characters
Note: this field may return null, indicating that no valid values can be obtained.
        :type URL: str
        :param IsValid: Whether verification is passed. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsValid: int
        :param ValidationCode: Verification code
Note: this field may return null, indicating that no valid values can be obtained.
        :type ValidationCode: str
        :param StartTime: Start time of the notification in seconds, which is calculated from 00:00:00.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTime: int
        :param EndTime: End time of the notification in seconds, which is calculated from 00:00:00.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EndTime: int
        :param Weekday: Notification cycle. The values 1-7 indicate Monday to Sunday.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Weekday: list of int
        """
        self.URL = None
        self.IsValid = None
        self.ValidationCode = None
        self.StartTime = None
        self.EndTime = None
        self.Weekday = None


    def _deserialize(self, params):
        self.URL = params.get("URL")
        self.IsValid = params.get("IsValid")
        self.ValidationCode = params.get("ValidationCode")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Weekday = params.get("Weekday")
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
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.
        :type GroupId: int
        :param PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.
        :type PolicyId: str
        :param EbSubject: The alert configured for an event
        :type EbSubject: str
        :param EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self.Module = None
        self.GroupId = None
        self.PolicyId = None
        self.EbSubject = None
        self.EbEventFlag = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        self.EbSubject = params.get("EbSubject")
        self.EbEventFlag = params.get("EbEventFlag")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject request structure.

    """

    def __init__(self):
        r"""
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID. If `PolicyId` is used, this parameter will be ignored, and any value, e.g., `0`, can be passed in.
        :type GroupId: int
        :param UniqueId: List of unique IDs of the object instances to be deleted. `UniqueId` can be obtained from the output parameter `List` of the [DescribeBindingPolicyObjectList](https://intl.cloud.tencent.com/document/api/248/40570?from_cn_redirect=1) API
        :type UniqueId: list of str
        :param InstanceGroupId: Instance group ID. The `UniqueId` parameter is invalid if object instances are deleted by instance group.
        :type InstanceGroupId: int
        :param PolicyId: Alarm policy ID. If this parameter is used, `GroupId` will be ignored.
        :type PolicyId: str
        :param EbSubject: The alert configured for an event
        :type EbSubject: str
        :param EbEventFlag: Whether the event alert has been configured
        :type EbEventFlag: int
        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None
        self.InstanceGroupId = None
        self.PolicyId = None
        self.EbSubject = None
        self.EbEventFlag = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.PolicyId = params.get("PolicyId")
        self.EbSubject = params.get("EbSubject")
        self.EbEventFlag = params.get("EbEventFlag")
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
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindPrometheusManagedGrafanaRequest(AbstractModel):
    """UnbindPrometheusManagedGrafana request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param GrafanaId: Grafana instance ID
        :type GrafanaId: str
        """
        self.InstanceId = None
        self.GrafanaId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GrafanaId = params.get("GrafanaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPrometheusManagedGrafanaResponse(AbstractModel):
    """UnbindPrometheusManagedGrafana response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UninstallGrafanaDashboardRequest(AbstractModel):
    """UninstallGrafanaDashboard request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param IntegrationCodes: Prometheus integration code, indicating to delete the corresponding dashboard. Valid values:
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
        self.InstanceId = None
        self.IntegrationCodes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaDashboardResponse(AbstractModel):
    """UninstallGrafanaDashboard response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UninstallGrafanaPluginsRequest(AbstractModel):
    """UninstallGrafanaPlugins request structure.

    """

    def __init__(self):
        r"""
        :param PluginIds: Array of plugin IDs, such as "PluginIds": [ "grafana-clock-panel" ]. The plugin ID can be obtained through the `DescribePluginOverviews` API.
        :type PluginIds: list of str
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefg”.
        :type InstanceId: str
        """
        self.PluginIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.PluginIds = params.get("PluginIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallGrafanaPluginsResponse(AbstractModel):
    """UninstallGrafanaPlugins response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAlertRuleRequest(AbstractModel):
    """UpdateAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Prometheus alerting rule ID
        :type RuleId: str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        :param RuleName: Alerting rule name
        :type RuleName: str
        :param Expr: Alerting rule expression
        :type Expr: str
        :param Duration: Alerting rule duration
        :type Duration: str
        :param Receivers: List of alerting rule recipient groups
        :type Receivers: list of str
        :param Labels: List of alerting rule tags
        :type Labels: list of PrometheusRuleKV
        :param Annotations: List of alerting rule annotations.

Alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively.
        :type Annotations: list of PrometheusRuleKV
        :param Type: Alerting rule template category
        :type Type: str
        """
        self.RuleId = None
        self.InstanceId = None
        self.RuleState = None
        self.RuleName = None
        self.Expr = None
        self.Duration = None
        self.Receivers = None
        self.Labels = None
        self.Annotations = None
        self.Type = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.InstanceId = params.get("InstanceId")
        self.RuleState = params.get("RuleState")
        self.RuleName = params.get("RuleName")
        self.Expr = params.get("Expr")
        self.Duration = params.get("Duration")
        self.Receivers = params.get("Receivers")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = PrometheusRuleKV()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleResponse(AbstractModel):
    """UpdateAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class UpdateAlertRuleStateRequest(AbstractModel):
    """UpdateAlertRuleState request structure.

    """

    def __init__(self):
        r"""
        :param RuleIds: List of rule IDs
        :type RuleIds: list of str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param RuleState: Rule status code. Valid values:
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self.RuleIds = None
        self.InstanceId = None
        self.RuleState = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        self.InstanceId = params.get("InstanceId")
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAlertRuleStateResponse(AbstractModel):
    """UpdateAlertRuleState response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDNSConfigRequest(AbstractModel):
    """UpdateDNSConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param NameServers: Array of DNS servers
        :type NameServers: list of str
        """
        self.InstanceId = None
        self.NameServers = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDNSConfigResponse(AbstractModel):
    """UpdateDNSConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateExporterIntegrationRequest(AbstractModel):
    """UpdateExporterIntegration request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param KubeType: Kubernetes cluster type. Valid values:
<li> 1 = TKE </li>
<li> 2 = EKS </li>
<li> 3 = MEKS </li>
        :type KubeType: int
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Kind: Type
        :type Kind: str
        :param Content: Configuration content
        :type Content: str
        """
        self.InstanceId = None
        self.KubeType = None
        self.ClusterId = None
        self.Kind = None
        self.Content = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KubeType = params.get("KubeType")
        self.ClusterId = params.get("ClusterId")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateExporterIntegrationResponse(AbstractModel):
    """UpdateExporterIntegration response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGrafanaConfigRequest(AbstractModel):
    """UpdateGrafanaConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Config: JSON-encoded string
        :type Config: str
        """
        self.InstanceId = None
        self.Config = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaConfigResponse(AbstractModel):
    """UpdateGrafanaConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGrafanaEnvironmentsRequest(AbstractModel):
    """UpdateGrafanaEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param Envs: Environment variable string
        :type Envs: str
        """
        self.InstanceId = None
        self.Envs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Envs = params.get("Envs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaEnvironmentsResponse(AbstractModel):
    """UpdateGrafanaEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGrafanaIntegrationRequest(AbstractModel):
    """UpdateGrafanaIntegration request structure.

    """

    def __init__(self):
        r"""
        :param IntegrationId: Integration ID, such as “integration-abcd1234”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type IntegrationId: str
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param Kind: Integration type, such as “tencent-cloud-prometheus”. You can view it by going to the instance details page and clicking **Tencent Cloud Service Integration** > **Integration List**.
        :type Kind: str
        :param Content: Integration content
        :type Content: str
        """
        self.IntegrationId = None
        self.InstanceId = None
        self.Kind = None
        self.Content = None


    def _deserialize(self, params):
        self.IntegrationId = params.get("IntegrationId")
        self.InstanceId = params.get("InstanceId")
        self.Kind = params.get("Kind")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaIntegrationResponse(AbstractModel):
    """UpdateGrafanaIntegration response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGrafanaNotificationChannelRequest(AbstractModel):
    """UpdateGrafanaNotificationChannel request structure.

    """

    def __init__(self):
        r"""
        :param ChannelId: Channel ID, such as “nchannel-abcd1234”.
        :type ChannelId: str
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param ChannelName: Alert channel name, such as “test”.
        :type ChannelName: str
        :param Receivers: Array of notification channel IDs
        :type Receivers: list of str
        :param ExtraOrgIds: This parameter has been deprecated. Please use `OrganizationIds` instead.
        :type ExtraOrgIds: list of str
        :param OrganizationIds: Array of valid organization IDs
        :type OrganizationIds: list of str
        """
        self.ChannelId = None
        self.InstanceId = None
        self.ChannelName = None
        self.Receivers = None
        self.ExtraOrgIds = None
        self.OrganizationIds = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.InstanceId = params.get("InstanceId")
        self.ChannelName = params.get("ChannelName")
        self.Receivers = params.get("Receivers")
        self.ExtraOrgIds = params.get("ExtraOrgIds")
        self.OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaNotificationChannelResponse(AbstractModel):
    """UpdateGrafanaNotificationChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGrafanaWhiteListRequest(AbstractModel):
    """UpdateGrafanaWhiteList request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param Whitelist: Array of public IPs (such as “127.0.0.1”) in the allowlist, which can be viewed through the `DescribeGrafanaWhiteList` API.
        :type Whitelist: list of str
        """
        self.InstanceId = None
        self.Whitelist = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGrafanaWhiteListResponse(AbstractModel):
    """UpdateGrafanaWhiteList response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePrometheusAgentStatusRequest(AbstractModel):
    """UpdatePrometheusAgentStatus request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param AgentIds: List of agent IDs such as “agent-abcd1234”, which can be obtained on the **Agent Management** page in the console.
        :type AgentIds: list of str
        :param Status: Status to update
<li> 1 = enabled </li>
<li> 2 = disabled </li>
        :type Status: int
        """
        self.InstanceId = None
        self.AgentIds = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentIds = params.get("AgentIds")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusAgentStatusResponse(AbstractModel):
    """UpdatePrometheusAgentStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePrometheusScrapeJobRequest(AbstractModel):
    """UpdatePrometheusScrapeJob request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TMP instance ID, such as “prom-abcd1234”.
        :type InstanceId: str
        :param AgentId: Agent ID such as “agent-abcd1234”, which can be obtained on the **Agent Management** page in the console
        :type AgentId: str
        :param JobId: Scrape task ID such as “job-abcd1234”. You can go to the **Agent Management** page and obtain the ID in the pop-up **Create Scrape Task** window.
        :type JobId: str
        :param Config: Scrape task ID in the format of “job_name:xx”
        :type Config: str
        """
        self.InstanceId = None
        self.AgentId = None
        self.JobId = None
        self.Config = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentId = params.get("AgentId")
        self.JobId = params.get("JobId")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrometheusScrapeJobResponse(AbstractModel):
    """UpdatePrometheusScrapeJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRecordingRuleRequest(AbstractModel):
    """UpdateRecordingRule request structure.

    """

    def __init__(self):
        r"""
        :param Name: Recording rule name
        :type Name: str
        :param Group: Recording rule group content, which is in YAML format and is Base64-encoded.
        :type Group: str
        :param InstanceId: Prometheus instance ID
        :type InstanceId: str
        :param RuleId: Prometheus recording rule ID
        :type RuleId: str
        :param RuleState: Rule status code. Valid values:
<li>1=RuleDeleted</li>
<li>2=RuleEnabled</li>
<li>3=RuleDisabled</li>
Default value: 2 (enabled).
        :type RuleState: int
        """
        self.Name = None
        self.Group = None
        self.InstanceId = None
        self.RuleId = None
        self.RuleState = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Group = params.get("Group")
        self.InstanceId = params.get("InstanceId")
        self.RuleId = params.get("RuleId")
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordingRuleResponse(AbstractModel):
    """UpdateRecordingRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class UpdateSSOAccountRequest(AbstractModel):
    """UpdateSSOAccount request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-abcdefgh”.
        :type InstanceId: str
        :param UserId: User account ID, such as “10000000”.
        :type UserId: str
        :param Role: Permission
        :type Role: list of GrafanaAccountRole
        :param Notes: Remarks
        :type Notes: str
        """
        self.InstanceId = None
        self.UserId = None
        self.Role = None
        self.Notes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserId = params.get("UserId")
        if params.get("Role") is not None:
            self.Role = []
            for item in params.get("Role"):
                obj = GrafanaAccountRole()
                obj._deserialize(item)
                self.Role.append(obj)
        self.Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSSOAccountResponse(AbstractModel):
    """UpdateSSOAccount response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeGrafanaDashboardRequest(AbstractModel):
    """UpgradeGrafanaDashboard request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param IntegrationCodes: Prometheus integration code, indicating to upgrade to the corresponding dashboard. Valid values:
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
        self.InstanceId = None
        self.IntegrationCodes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IntegrationCodes = params.get("IntegrationCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaDashboardResponse(AbstractModel):
    """UpgradeGrafanaDashboard response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeGrafanaInstanceRequest(AbstractModel):
    """UpgradeGrafanaInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: TCMG instance ID, such as “grafana-12345678”.
        :type InstanceId: str
        :param Alias: Version alias, such as v7.4.2.
        :type Alias: str
        """
        self.InstanceId = None
        self.Alias = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGrafanaInstanceResponse(AbstractModel):
    """UpgradeGrafanaInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserNotice(AbstractModel):
    """Cloud Monitor alarm notification template - user notification details

    """

    def __init__(self):
        r"""
        :param ReceiverType: Recipient type. Valid values: USER (user), GROUP (user group)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReceiverType: str
        :param StartTime: Notification start time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param EndTime: Notification end time, which is expressed by the number of seconds since 00:00:00. Value range: 0–86399
Note: this field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param NoticeWay: Notification channel list. Valid values: `EMAIL` (email), `SMS` (SMS), `CALL` (phone), `WECHAT` (WeChat), `RTX` (WeCom)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NoticeWay: list of str
        :param UserIds: User `uid` list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserIds: list of int
        :param GroupIds: User group ID list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupIds: list of int
        :param PhoneOrder: Phone polling list
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneOrder: list of int
        :param PhoneCircleTimes: Number of phone pollings. Value range: 1–5
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleTimes: int
        :param PhoneInnerInterval: Call interval in seconds within one polling. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneInnerInterval: int
        :param PhoneCircleInterval: Polling interval in seconds. Value range: 60–900
Note: this field may return null, indicating that no valid values can be obtained.
        :type PhoneCircleInterval: int
        :param NeedPhoneArriveNotice: Whether receipt notification is required. Valid values: 0 (no), 1 (yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type NeedPhoneArriveNotice: int
        :param PhoneCallType: Dial type. `SYNC` (simultaneous dial), `CIRCLE` (polled dial). Default value: `CIRCLE`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PhoneCallType: str
        :param Weekday: Notification cycle. The values 1-7 indicate Monday to Sunday.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Weekday: list of int
        """
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
        self.PhoneCallType = None
        self.Weekday = None


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
        self.PhoneCallType = params.get("PhoneCallType")
        self.Weekday = params.get("Weekday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        