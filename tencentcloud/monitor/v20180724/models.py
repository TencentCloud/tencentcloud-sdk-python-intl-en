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


class BindingPolicyObjectDimension(AbstractModel):
    """Dimensions of instances bound to a policy

    """

    def __init__(self):
        """
        :param Region: Region name.
        :type Region: str
        :param RegionId: Region ID.
        :type RegionId: int
        :param Dimensions: Dimensions.
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


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject request structure.

    """

    def __init__(self):
        """
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param Module: Required. The value is fixed to monitor.
        :type Module: str
        :param InstanceGroupId: Instance group ID.
        :type InstanceGroupId: int
        :param Dimensions: Dimensions of an object to be bound.
        :type Dimensions: list of BindingPolicyObjectDimension
        """
        self.GroupId = None
        self.Module = None
        self.InstanceGroupId = None
        self.Dimensions = None


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


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """Alarm threshold condition passed in when a policy is created.

    """

    def __init__(self):
        """
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


class CreatePolicyGroupEventCondition(AbstractModel):
    """Event alarm condition passed in when a policy is created.

    """

    def __init__(self):
        """
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


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup request structure.

    """

    def __init__(self):
        """
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
        :param IsUnionRule: The “AND” and “OR” rules for alarm metrics. The value 0 indicates “OR”, which means that an alarm will be triggered when any rule is met. The value 1 indicates “AND”, which means that an alarm will be triggered only when all rules are met.
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


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup response structure.

    """

    def __init__(self):
        """
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


class DataPoint(AbstractModel):
    """Monitoring data point

    """

    def __init__(self):
        """
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


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup request structure.

    """

    def __init__(self):
        """
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


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList request structure.

    """

    def __init__(self):
        """
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


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList response structure.

    """

    def __init__(self):
        """
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


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics request structure.

    """

    def __init__(self):
        """
        :param Namespace: Service namespace. Different Tencent Cloud services have different namespaces. For more information on service namespaces, see the monitoring API documentation of each product. For example, you can see [CVM Monitoring APIs](https://cloud.tencent.com/document/api/248/30385) for the namespace of CVM.
        :type Namespace: str
        :param MetricName: Metric name. Different Tencent Cloud services have different metric names. For more information on service metric names, see the monitoring API documentation of each product. For example, you can see the [CVM Monitoring APIs](https://cloud.tencent.com/document/api/248/30385) for the metric names of CVM.
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics response structure.

    """

    def __init__(self):
        """
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
        """
        :param Id: Alarm ID.
        :type Id: int
        :param ProjectId: Project ID.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectId: int
        :param ProjectName: Project name.
Note: This field may return null, indicating that no valid value was found.
        :type ProjectName: str
        :param Status: Alarm status ID.
Note: This field may return null, indicating that no valid value was found.
        :type Status: int
        :param AlarmStatus: Alarm status.
Note: This field may return null, indicating that no valid value was found.
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


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList request structure.

    """

    def __init__(self):
        """
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


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList response structure.

    """

    def __init__(self):
        """
        :param Alarms: Alarm list.
Note: This field may return null, indicating that no valid value was found.
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param Total: Total number.
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


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """Object instance information returned by the DescribeBindingPolicyObjectListInstance API.

    """

    def __init__(self):
        """
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


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """Instance group information returned by the DescribeBindingPolicyObjectList API

    """

    def __init__(self):
        """
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


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param Limit: Number of parameters that can be returned on each page. Value range: 1 - 100. Default value: 20.
        :type Limit: int
        :param Offset: Parameter offset on each page. The value starts from 0 and the default value is 0.
        :type Offset: int
        :param Dimensions: Dimensions of filtering objects.
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
        self.Module = None
        self.GroupId = None
        self.Limit = None
        self.Offset = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList response structure.

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListCondition(AbstractModel):
    """Policy conditions returned by the DescribePolicyConditionList API

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListMetric(AbstractModel):
    """Metric alarm configuration.

    """

    def __init__(self):
        """
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


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.
        :type Module: str
        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList response structure.

    """

    def __init__(self):
        """
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
        """
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


class DescribePolicyGroupInfoCondition(AbstractModel):
    """Alarm threshold conditions output by the policy query

    """

    def __init__(self):
        """
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
        :param AlarmNotifyPeriod: Alarm sending period in seconds. The value <0 indicates that no alarm will be triggered. The value 0 indicates that an alarm is triggered only once. The value >0 indicates that an alarm is triggered at the interval of triggerTime.
        :type AlarmNotifyPeriod: int
        :param CalcType: Comparative type. The value 1 indicates greater than. The value 2 indicates greater than or equal to. The value 3 indicates smaller than. The value 4 indicates smaller than or equal to. The value 5 indicates equal to. The value 6 indicates not equal to. The value 7 indicates day-on-day increase. The value 8 indicates day-on-day decrease. The value 9 indicates week-on-week increase. The value 10 indicates week-on-week decrease. The value 11 indicates periodical increase. The value 12 indicates periodical decrease.
Note: This field may return null, indicating that no valid value was found.
        :type CalcType: int
        :param CalcValue: Threshold.
Note: This field may return null, indicating that no valid value was found.
        :type CalcValue: str
        :param ContinueTime: Duration at which an alarm will be triggered in seconds.
Note: This field may return null, indicating that no valid value was found.
        :type ContinueTime: int
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


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """Template-based policy group information output by the policy query

    """

    def __init__(self):
        """
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
        :param IsUnionRule: Whether the “AND” rule is used.
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


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """Event alarm conditions output by the policy query

    """

    def __init__(self):
        """
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


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """Alarm recipient information output by the policy query

    """

    def __init__(self):
        """
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


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo request structure.

    """

    def __init__(self):
        """
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


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo response structure.

    """

    def __init__(self):
        """
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
        :param IsUnionRule: Whether the “AND” rule is used.
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
        """
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
        :param IsUnionRule: The “AND” or “OR” rule. The value 0 indicates the “OR” rule (indicating that an alarm will be triggered if any rule meets the threshold condition). The value 1 indicates the “AND” rule (indicating that an alarm will be triggered when all rules meet the threshold conditions).
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


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """Instance group that is bound to a policy group of the DescribePolicyGroupList API

    """

    def __init__(self):
        """
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


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList request structure.

    """

    def __init__(self):
        """
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
        :param ReceiverType: Filter by recipient or recipient group. The value “user” indicates by recipient. The value “group” indicates by recipient group.
        :type ReceiverType: str
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


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList response structure.

    """

    def __init__(self):
        """
        :param GroupList: Policy group list.
Note: This field may return null, indicating that no valid value was found.
        :type GroupList: list of DescribePolicyGroupListGroup
        :param Total: Total number of policy groups.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class DescribeProductEventListEvents(AbstractModel):
    """Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
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


class DescribeProductEventListEventsDimensions(AbstractModel):
    """Dimensions of events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
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


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """GroupInfo in Events returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
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


class DescribeProductEventListOverView(AbstractModel):
    """OverView object returned by the DescribeProductEventList API

    """

    def __init__(self):
        """
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


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList request structure.

    """

    def __init__(self):
        """
        :param Module: API component name. It is fixed to monitor.
        :type Module: str
        :param ProductName: Filter by product type. For example, “cvm” indicates Cloud Virtual Machine.
        :type ProductName: list of str
        :param EventName: Filter by product name. For example, "guest_reboot" indicates server restart.
        :type EventName: list of str
        :param InstanceId: Affected object, such as ins-19708ino.
        :type InstanceId: list of str
        :param Dimensions: Filter by dimension, such as by public IP: 10.0.0.1.
        :type Dimensions: list of DescribeProductEventListDimensions
        :param RegionList: Filter by region, such as by gz.
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


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList response structure.

    """

    def __init__(self):
        """
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


class Dimension(AbstractModel):
    """Combination of instance object dimensions

    """

    def __init__(self):
        """
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


class DimensionsDesc(AbstractModel):
    """Dimension information

    """

    def __init__(self):
        """
        :param Dimensions: Array of dimension names
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace. Each Tencent Cloud product has a namespace
        :type Namespace: str
        :param MetricName: Metric name. For detailed metric descriptions of each Tencent Cloud product, see the corresponding [Monitoring API](https://cloud.tencent.com/document/product/248/30384) document
        :type MetricName: str
        :param Instances: Combination of instance object dimensions
        :type Instances: list of Instance
        :param Period: Monitoring statistical period. The default value is 300, and the unit is s
        :type Period: int
        :param StartTime: Start time such as 2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: End time. Uses the current time by default and cannot be earlier than StartTime
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


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData response structure.

    """

    def __init__(self):
        """
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class InstanceGroup(AbstractModel):
    """InstanceGroup in Alarms returned by the DescribeBasicAlarmList API

    """

    def __init__(self):
        """
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


class MetricDatum(AbstractModel):
    """Metric names and values

    """

    def __init__(self):
        """
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


class MetricObjectMeaning(AbstractModel):
    """Meaning of metric data

    """

    def __init__(self):
        """
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


class MetricSet(AbstractModel):
    """Description of the unit and supported statistical period of the business metric

    """

    def __init__(self):
        """
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
        """
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


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers request structure.

    """

    def __init__(self):
        """
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


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers response structure.

    """

    def __init__(self):
        """
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
        """
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


class ModifyPolicyGroupEventCondition(AbstractModel):
    """Modification of the event alarm condition passed in by the alarm policy group.

    """

    def __init__(self):
        """
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


class ModifyPolicyGroupRequest(AbstractModel):
    """ModifyPolicyGroup request structure.

    """

    def __init__(self):
        """
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param ViewName: Alarm type.
        :type ViewName: str
        :param GroupName: Policy group name.
        :type GroupName: str
        :param IsUnionRule: The “AND” and “OR” rules for metric alarms. The value 1 indicates “AND”, which means that an alarm will be triggered only when all rules are met. The value 0 indicates “OR”, which means that an alarm will be triggered when any rule is met.
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


class ModifyPolicyGroupResponse(AbstractModel):
    """ModifyPolicyGroup response structure.

    """

    def __init__(self):
        """
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


class PeriodsSt(AbstractModel):
    """Statistical method during the period

    """

    def __init__(self):
        """
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


class PutMonitorDataRequest(AbstractModel):
    """PutMonitorData request structure.

    """

    def __init__(self):
        """
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


class PutMonitorDataResponse(AbstractModel):
    """PutMonitorData response structure.

    """

    def __init__(self):
        """
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
        """
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
        :param UidList: Uid of the alarm call recipient.
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
        :param ReceiverGroupList: Recipient group list. The list of recipient group IDs that is queried by a platform API.
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: Recipient list. The list of recipient IDs that is queried by a platform API.
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


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg request structure.

    """

    def __init__(self):
        """
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


class SendCustomAlarmMsgResponse(AbstractModel):
    """SendCustomAlarmMsg response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject request structure.

    """

    def __init__(self):
        """
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


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject response structure.

    """

    def __init__(self):
        """
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
        """
        :param Module: The value is fixed to monitor.
        :type Module: str
        :param GroupId: Policy group ID.
        :type GroupId: int
        :param UniqueId: List of unique IDs of object instances to be deleted.
        :type UniqueId: list of str
        :param InstanceGroupId: Instance group ID. The UniqueId parameter is invalid if object instances are deleted by instance group.
        :type InstanceGroupId: int
        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None
        self.InstanceGroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")
        self.InstanceGroupId = params.get("InstanceGroupId")


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")