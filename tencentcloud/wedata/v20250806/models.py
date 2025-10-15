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


class AlarmGroup(AbstractModel):
    r"""Alarm rule recipient configuration.

    """

    def __init__(self):
        r"""
        :param _AlarmEscalationRecipientIds: Specifies the list of Alarm escalation recipient ids.
If the Alarm recipient or supervisor does not confirm the Alarm within the Alarm interval, an Alarm will be sent to the next-level superior.
        :type AlarmEscalationRecipientIds: list of str
        :param _AlarmEscalationInterval: Escalation interval for alarms.
        :type AlarmEscalationInterval: int
        :param _NotificationFatigue: Alarm notification fatigue configuration.
        :type NotificationFatigue: :class:`tencentcloud.wedata.v20250806.models.NotificationFatigue`
        :param _AlarmWays: Alarm channel. valid values: 1. mail, 2. sms, 3. wechat, 4. voice, 5. wecom, 6. Http, 7. wecom group, 8. lark group, 9. dingtalk group, 10. Slack group, 11. Teams group (default: 1. mail). only select one channel.
        :type AlarmWays: list of str
        :param _WebHooks: webhook url list for wecom group/lark group/dingtalk group/Slack group/Teams group.
        :type WebHooks: list of AlarmWayWebHook
        :param _AlarmRecipientType: Alarm recipient type: 1. specified personnel, 2. task owner, 3. duty schedule (default: 1. specified personnel).
        :type AlarmRecipientType: int
        :param _AlarmRecipientIds: Specifies different business ids based on AlarmRecipientType. valid values: 1 (designated personnel): Alarm recipient id list. 2 (task owner): no configuration required. 3 (duty schedule): schedule id list.
        :type AlarmRecipientIds: list of str
        """
        self._AlarmEscalationRecipientIds = None
        self._AlarmEscalationInterval = None
        self._NotificationFatigue = None
        self._AlarmWays = None
        self._WebHooks = None
        self._AlarmRecipientType = None
        self._AlarmRecipientIds = None

    @property
    def AlarmEscalationRecipientIds(self):
        r"""Specifies the list of Alarm escalation recipient ids.
If the Alarm recipient or supervisor does not confirm the Alarm within the Alarm interval, an Alarm will be sent to the next-level superior.
        :rtype: list of str
        """
        return self._AlarmEscalationRecipientIds

    @AlarmEscalationRecipientIds.setter
    def AlarmEscalationRecipientIds(self, AlarmEscalationRecipientIds):
        self._AlarmEscalationRecipientIds = AlarmEscalationRecipientIds

    @property
    def AlarmEscalationInterval(self):
        r"""Escalation interval for alarms.
        :rtype: int
        """
        return self._AlarmEscalationInterval

    @AlarmEscalationInterval.setter
    def AlarmEscalationInterval(self, AlarmEscalationInterval):
        self._AlarmEscalationInterval = AlarmEscalationInterval

    @property
    def NotificationFatigue(self):
        r"""Alarm notification fatigue configuration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.NotificationFatigue`
        """
        return self._NotificationFatigue

    @NotificationFatigue.setter
    def NotificationFatigue(self, NotificationFatigue):
        self._NotificationFatigue = NotificationFatigue

    @property
    def AlarmWays(self):
        r"""Alarm channel. valid values: 1. mail, 2. sms, 3. wechat, 4. voice, 5. wecom, 6. Http, 7. wecom group, 8. lark group, 9. dingtalk group, 10. Slack group, 11. Teams group (default: 1. mail). only select one channel.
        :rtype: list of str
        """
        return self._AlarmWays

    @AlarmWays.setter
    def AlarmWays(self, AlarmWays):
        self._AlarmWays = AlarmWays

    @property
    def WebHooks(self):
        r"""webhook url list for wecom group/lark group/dingtalk group/Slack group/Teams group.
        :rtype: list of AlarmWayWebHook
        """
        return self._WebHooks

    @WebHooks.setter
    def WebHooks(self, WebHooks):
        self._WebHooks = WebHooks

    @property
    def AlarmRecipientType(self):
        r"""Alarm recipient type: 1. specified personnel, 2. task owner, 3. duty schedule (default: 1. specified personnel).
        :rtype: int
        """
        return self._AlarmRecipientType

    @AlarmRecipientType.setter
    def AlarmRecipientType(self, AlarmRecipientType):
        self._AlarmRecipientType = AlarmRecipientType

    @property
    def AlarmRecipientIds(self):
        r"""Specifies different business ids based on AlarmRecipientType. valid values: 1 (designated personnel): Alarm recipient id list. 2 (task owner): no configuration required. 3 (duty schedule): schedule id list.
        :rtype: list of str
        """
        return self._AlarmRecipientIds

    @AlarmRecipientIds.setter
    def AlarmRecipientIds(self, AlarmRecipientIds):
        self._AlarmRecipientIds = AlarmRecipientIds


    def _deserialize(self, params):
        self._AlarmEscalationRecipientIds = params.get("AlarmEscalationRecipientIds")
        self._AlarmEscalationInterval = params.get("AlarmEscalationInterval")
        if params.get("NotificationFatigue") is not None:
            self._NotificationFatigue = NotificationFatigue()
            self._NotificationFatigue._deserialize(params.get("NotificationFatigue"))
        self._AlarmWays = params.get("AlarmWays")
        if params.get("WebHooks") is not None:
            self._WebHooks = []
            for item in params.get("WebHooks"):
                obj = AlarmWayWebHook()
                obj._deserialize(item)
                self._WebHooks.append(obj)
        self._AlarmRecipientType = params.get("AlarmRecipientType")
        self._AlarmRecipientIds = params.get("AlarmRecipientIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmMessage(AbstractModel):
    r"""Alarm information.

    """

    def __init__(self):
        r"""
        :param _AlarmMessageId: Alarm message Id.
        :type AlarmMessageId: int
        :param _AlarmTime: Alarm time. the same Alarm may be sent multiple times, only the latest Alarm time is displayed.
        :type AlarmTime: str
        :param _TaskName: Task name.
        :type TaskName: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _CurRunDate: Instance data time of the task.
        :type CurRunDate: str
        :param _AlarmReason: Indicates the Alarm cause.
        :type AlarmReason: str
        :param _AlarmLevel: Alarm level. 1. ordinary, 2. important, 3. critical.
        :type AlarmLevel: int
        :param _AlarmRuleId: Specifies the Id of the Alarm rule.
        :type AlarmRuleId: str
        :param _AlarmWays: Alarm channel specifies the notification methods: 1. mail, 2. sms, 3. wechat, 4. voice, 5. wecom, 6. Http, 7. wecom group, 8. lark group, 9. dingtalk group, 10. Slack group, 11. Teams group (default: 1. mail).
        :type AlarmWays: list of str
        :param _AlarmRecipients: Alarm recipient
        :type AlarmRecipients: list of str
        """
        self._AlarmMessageId = None
        self._AlarmTime = None
        self._TaskName = None
        self._TaskId = None
        self._CurRunDate = None
        self._AlarmReason = None
        self._AlarmLevel = None
        self._AlarmRuleId = None
        self._AlarmWays = None
        self._AlarmRecipients = None

    @property
    def AlarmMessageId(self):
        r"""Alarm message Id.
        :rtype: int
        """
        return self._AlarmMessageId

    @AlarmMessageId.setter
    def AlarmMessageId(self, AlarmMessageId):
        self._AlarmMessageId = AlarmMessageId

    @property
    def AlarmTime(self):
        r"""Alarm time. the same Alarm may be sent multiple times, only the latest Alarm time is displayed.
        :rtype: str
        """
        return self._AlarmTime

    @AlarmTime.setter
    def AlarmTime(self, AlarmTime):
        self._AlarmTime = AlarmTime

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CurRunDate(self):
        r"""Instance data time of the task.
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def AlarmReason(self):
        r"""Indicates the Alarm cause.
        :rtype: str
        """
        return self._AlarmReason

    @AlarmReason.setter
    def AlarmReason(self, AlarmReason):
        self._AlarmReason = AlarmReason

    @property
    def AlarmLevel(self):
        r"""Alarm level. 1. ordinary, 2. important, 3. critical.
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRuleId(self):
        r"""Specifies the Id of the Alarm rule.
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmWays(self):
        r"""Alarm channel specifies the notification methods: 1. mail, 2. sms, 3. wechat, 4. voice, 5. wecom, 6. Http, 7. wecom group, 8. lark group, 9. dingtalk group, 10. Slack group, 11. Teams group (default: 1. mail).
        :rtype: list of str
        """
        return self._AlarmWays

    @AlarmWays.setter
    def AlarmWays(self, AlarmWays):
        self._AlarmWays = AlarmWays

    @property
    def AlarmRecipients(self):
        r"""Alarm recipient
        :rtype: list of str
        """
        return self._AlarmRecipients

    @AlarmRecipients.setter
    def AlarmRecipients(self, AlarmRecipients):
        self._AlarmRecipients = AlarmRecipients


    def _deserialize(self, params):
        self._AlarmMessageId = params.get("AlarmMessageId")
        self._AlarmTime = params.get("AlarmTime")
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._CurRunDate = params.get("CurRunDate")
        self._AlarmReason = params.get("AlarmReason")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmWays = params.get("AlarmWays")
        self._AlarmRecipients = params.get("AlarmRecipients")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmQuietInterval(AbstractModel):
    r"""Alarm do-not-disturb time interval.

    """

    def __init__(self):
        r"""
        :param _DaysOfWeek: ISO standard. 1 means monday, 7 means sunday.
        :type DaysOfWeek: list of int non-negative
        :param _StartTime: Start time. precision: hour/minute/second. format: HH:mm:ss.
        :type StartTime: str
        :param _EndTime: End time. precision: hour/minute/second. format: HH:mm:ss.
        :type EndTime: str
        """
        self._DaysOfWeek = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DaysOfWeek(self):
        r"""ISO standard. 1 means monday, 7 means sunday.
        :rtype: list of int non-negative
        """
        return self._DaysOfWeek

    @DaysOfWeek.setter
    def DaysOfWeek(self, DaysOfWeek):
        self._DaysOfWeek = DaysOfWeek

    @property
    def StartTime(self):
        r"""Start time. precision: hour/minute/second. format: HH:mm:ss.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time. precision: hour/minute/second. format: HH:mm:ss.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DaysOfWeek = params.get("DaysOfWeek")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmRuleData(AbstractModel):
    r"""Alarm Rule Details

    """

    def __init__(self):
        r"""
        :param _AlarmRuleId: Alarm Rule ID
        :type AlarmRuleId: str
        :param _AlarmRuleName: Specifies the Alarm rule name.
        :type AlarmRuleName: str
        :param _Description: Describes the Alarm rule.
        :type Description: str
        :param _MonitorObjectType: Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :type MonitorObjectType: int
        :param _MonitorObjectIds: Pass different business IDs depending on the value of MonitorType:

1 (Task): MonitorObjectIds should contain a list of task IDs.

2 (Workflow): MonitorObjectIds should contain a list of workflow IDs (workflow IDs can be obtained using the ListWorkflows API).

3 (Project): MonitorObjectIds should contain a list of project IDs.
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :type AlarmTypes: list of str
        :param _Status: Whether the Alarm rule is enabled.
Valid values: 0 (disabled), 1 (enabled).
        :type Status: int
        :param _AlarmRuleDetail: Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _AlarmLevel: Alarm level. 1. ordinary, 2. important, 3. critical.
        :type AlarmLevel: int
        :param _OwnerUin: Specifies the id of the Alarm rule creator.
        :type OwnerUin: str
        :param _BundleId: The Alarm rule bound to the bundle client. it is normal if empty, otherwise it corresponds to the rule bound to the bundle client.
        :type BundleId: str
        :param _BundleInfo: bundleId is not empty. it indicates the bound client name.

        :type BundleInfo: str
        :param _AlarmGroups: Describes the Alarm recipient configuration list.
        :type AlarmGroups: list of AlarmGroup
        """
        self._AlarmRuleId = None
        self._AlarmRuleName = None
        self._Description = None
        self._MonitorObjectType = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._Status = None
        self._AlarmRuleDetail = None
        self._AlarmLevel = None
        self._OwnerUin = None
        self._BundleId = None
        self._BundleInfo = None
        self._AlarmGroups = None

    @property
    def AlarmRuleId(self):
        r"""Alarm Rule ID
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmRuleName(self):
        r"""Specifies the Alarm rule name.
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def Description(self):
        r"""Describes the Alarm rule.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MonitorObjectType(self):
        r"""Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def MonitorObjectIds(self):
        r"""Pass different business IDs depending on the value of MonitorType:

1 (Task): MonitorObjectIds should contain a list of task IDs.

2 (Workflow): MonitorObjectIds should contain a list of workflow IDs (workflow IDs can be obtained using the ListWorkflows API).

3 (Project): MonitorObjectIds should contain a list of project IDs.
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def Status(self):
        r"""Whether the Alarm rule is enabled.
Valid values: 0 (disabled), 1 (enabled).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmRuleDetail(self):
        r"""Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def AlarmLevel(self):
        r"""Alarm level. 1. ordinary, 2. important, 3. critical.
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def OwnerUin(self):
        r"""Specifies the id of the Alarm rule creator.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def BundleId(self):
        r"""The Alarm rule bound to the bundle client. it is normal if empty, otherwise it corresponds to the rule bound to the bundle client.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""bundleId is not empty. it indicates the bound client name.

        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo

    @property
    def AlarmGroups(self):
        r"""Describes the Alarm recipient configuration list.
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups


    def _deserialize(self, params):
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._Description = params.get("Description")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        self._Status = params.get("Status")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._AlarmLevel = params.get("AlarmLevel")
        self._OwnerUin = params.get("OwnerUin")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmRuleDetail(AbstractModel):
    r"""Detailed configuration of the Alarm rule.

    """

    def __init__(self):
        r"""
        :param _Trigger: Failure Trigger Condition

1: Trigger on the first failure

2: Trigger after all retries are completed (default)
        :type Trigger: int
        :param _DataBackfillOrRerunTrigger: Backfill/Rerun Trigger Condition

1: Trigger on the first failure

2: Trigger after all retries are completed
        :type DataBackfillOrRerunTrigger: int
        :param _TimeOutExtInfo: Timeout configuration of the periodic instance.

        :type TimeOutExtInfo: list of TimeOutStrategyInfo
        :param _DataBackfillOrRerunTimeOutExtInfo: Specifies the timeout configuration details for rerunning a backfill instance.

        :type DataBackfillOrRerunTimeOutExtInfo: list of TimeOutStrategyInfo
        :param _ProjectInstanceStatisticsAlarmInfoList: Specifies the detail of Alarm configuration for project fluctuation.
        :type ProjectInstanceStatisticsAlarmInfoList: list of ProjectInstanceStatisticsAlarmInfo
        :param _ReconciliationExtInfo: Describes the Alarm configuration information for offline integration reconciliation.
        :type ReconciliationExtInfo: list of ReconciliationStrategyInfo
        """
        self._Trigger = None
        self._DataBackfillOrRerunTrigger = None
        self._TimeOutExtInfo = None
        self._DataBackfillOrRerunTimeOutExtInfo = None
        self._ProjectInstanceStatisticsAlarmInfoList = None
        self._ReconciliationExtInfo = None

    @property
    def Trigger(self):
        r"""Failure Trigger Condition

1: Trigger on the first failure

2: Trigger after all retries are completed (default)
        :rtype: int
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def DataBackfillOrRerunTrigger(self):
        r"""Backfill/Rerun Trigger Condition

1: Trigger on the first failure

2: Trigger after all retries are completed
        :rtype: int
        """
        return self._DataBackfillOrRerunTrigger

    @DataBackfillOrRerunTrigger.setter
    def DataBackfillOrRerunTrigger(self, DataBackfillOrRerunTrigger):
        self._DataBackfillOrRerunTrigger = DataBackfillOrRerunTrigger

    @property
    def TimeOutExtInfo(self):
        r"""Timeout configuration of the periodic instance.

        :rtype: list of TimeOutStrategyInfo
        """
        return self._TimeOutExtInfo

    @TimeOutExtInfo.setter
    def TimeOutExtInfo(self, TimeOutExtInfo):
        self._TimeOutExtInfo = TimeOutExtInfo

    @property
    def DataBackfillOrRerunTimeOutExtInfo(self):
        r"""Specifies the timeout configuration details for rerunning a backfill instance.

        :rtype: list of TimeOutStrategyInfo
        """
        return self._DataBackfillOrRerunTimeOutExtInfo

    @DataBackfillOrRerunTimeOutExtInfo.setter
    def DataBackfillOrRerunTimeOutExtInfo(self, DataBackfillOrRerunTimeOutExtInfo):
        self._DataBackfillOrRerunTimeOutExtInfo = DataBackfillOrRerunTimeOutExtInfo

    @property
    def ProjectInstanceStatisticsAlarmInfoList(self):
        r"""Specifies the detail of Alarm configuration for project fluctuation.
        :rtype: list of ProjectInstanceStatisticsAlarmInfo
        """
        return self._ProjectInstanceStatisticsAlarmInfoList

    @ProjectInstanceStatisticsAlarmInfoList.setter
    def ProjectInstanceStatisticsAlarmInfoList(self, ProjectInstanceStatisticsAlarmInfoList):
        self._ProjectInstanceStatisticsAlarmInfoList = ProjectInstanceStatisticsAlarmInfoList

    @property
    def ReconciliationExtInfo(self):
        r"""Describes the Alarm configuration information for offline integration reconciliation.
        :rtype: list of ReconciliationStrategyInfo
        """
        return self._ReconciliationExtInfo

    @ReconciliationExtInfo.setter
    def ReconciliationExtInfo(self, ReconciliationExtInfo):
        self._ReconciliationExtInfo = ReconciliationExtInfo


    def _deserialize(self, params):
        self._Trigger = params.get("Trigger")
        self._DataBackfillOrRerunTrigger = params.get("DataBackfillOrRerunTrigger")
        if params.get("TimeOutExtInfo") is not None:
            self._TimeOutExtInfo = []
            for item in params.get("TimeOutExtInfo"):
                obj = TimeOutStrategyInfo()
                obj._deserialize(item)
                self._TimeOutExtInfo.append(obj)
        if params.get("DataBackfillOrRerunTimeOutExtInfo") is not None:
            self._DataBackfillOrRerunTimeOutExtInfo = []
            for item in params.get("DataBackfillOrRerunTimeOutExtInfo"):
                obj = TimeOutStrategyInfo()
                obj._deserialize(item)
                self._DataBackfillOrRerunTimeOutExtInfo.append(obj)
        if params.get("ProjectInstanceStatisticsAlarmInfoList") is not None:
            self._ProjectInstanceStatisticsAlarmInfoList = []
            for item in params.get("ProjectInstanceStatisticsAlarmInfoList"):
                obj = ProjectInstanceStatisticsAlarmInfo()
                obj._deserialize(item)
                self._ProjectInstanceStatisticsAlarmInfoList.append(obj)
        if params.get("ReconciliationExtInfo") is not None:
            self._ReconciliationExtInfo = []
            for item in params.get("ReconciliationExtInfo"):
                obj = ReconciliationStrategyInfo()
                obj._deserialize(item)
                self._ReconciliationExtInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmWayWebHook(AbstractModel):
    r"""Alarm channel specifies the webhook url configuration for wecom group, dingtalk group, or lark group.

    """

    def __init__(self):
        r"""
        :param _AlarmWay: Specifies the Alarm channel value.
7. wecom group 8. lark group 9. dingtalk group 10. Slack group 11. Teams group.
        :type AlarmWay: str
        :param _WebHooks: webhook url list of the Alarm group.
        :type WebHooks: list of str
        """
        self._AlarmWay = None
        self._WebHooks = None

    @property
    def AlarmWay(self):
        r"""Specifies the Alarm channel value.
7. wecom group 8. lark group 9. dingtalk group 10. Slack group 11. Teams group.
        :rtype: str
        """
        return self._AlarmWay

    @AlarmWay.setter
    def AlarmWay(self, AlarmWay):
        self._AlarmWay = AlarmWay

    @property
    def WebHooks(self):
        r"""webhook url list of the Alarm group.
        :rtype: list of str
        """
        return self._WebHooks

    @WebHooks.setter
    def WebHooks(self, WebHooks):
        self._WebHooks = WebHooks


    def _deserialize(self, params):
        self._AlarmWay = params.get("AlarmWay")
        self._WebHooks = params.get("WebHooks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackfillInstance(AbstractModel):
    r"""Description of a supplementary instance.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name.
        :type TaskName: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _CurRunDate: Specifies the instance data time.
        :type CurRunDate: str
        :param _State: Execution status.
        :type State: str
        :param _StartTime: Start time.


        :type StartTime: str
        :param _EndTime: End time.


        :type EndTime: str
        :param _CostTime: Execution duration.


        :type CostTime: str
        """
        self._TaskName = None
        self._TaskId = None
        self._CurRunDate = None
        self._State = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CurRunDate(self):
        r"""Specifies the instance data time.
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def State(self):
        r"""Execution status.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def StartTime(self):
        r"""Start time.


        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.


        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        r"""Execution duration.


        :rtype: str
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._CurRunDate = params.get("CurRunDate")
        self._State = params.get("State")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackfillInstanceCollection(AbstractModel):
    r"""Replenishment plan all instances.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        :param _TotalPageNumber: Total pages
        :type TotalPageNumber: int
        :param _TotalCount: Total number of records
        :type TotalCount: int
        :param _Items: Specifies the backfill instance list.
        :type Items: list of BackfillInstance
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPageNumber(self):
        r"""Total pages
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""Total number of records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Specifies the backfill instance list.
        :rtype: list of BackfillInstance
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackfillInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChildDependencyConfigPage(AbstractModel):
    r"""Task downstream dependency details pagination.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results


        :type TotalCount: int
        :param _TotalPageNumber: Total pages

        :type TotalPageNumber: int
        :param _PageNumber: Page number.

        :type PageNumber: int
        :param _PageSize: Pagination size.

        :type PageSize: int
        :param _Items: Paging data

        :type Items: list of OpsTaskDepend
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""Total number of results


        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""Page number.

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""Paging data

        :rtype: list of OpsTaskDepend
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsTaskDepend()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFile(AbstractModel):
    r"""Explore data script business processing entity.

    """

    def __init__(self):
        r"""
        :param _CodeFileId: Script ID


        :type CodeFileId: str
        :param _CodeFileName: Script name.

        :type CodeFileName: str
        :param _OwnerUin: Specifies the script owner uin.

        :type OwnerUin: str
        :param _CodeFileConfig: Specifies the script configuration.

        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: Specifies the script content.

        :type CodeFileContent: str
        :param _UpdateUserUin: Latest operator.

        :type UpdateUserUin: str
        :param _ProjectId: Project ID.


        :type ProjectId: str
        :param _UpdateTime: Update time. format: yyyy-MM-dd hh:MM:ss.
Note: This field may return null, indicating that no valid 
        :type UpdateTime: str
        :param _CreateTime: Creation time. format: yyyy-MM-dd hh:MM:ss.

        :type CreateTime: str
        :param _AccessScope: Access permission: SHARED, PRIVATE.

        :type AccessScope: str
        :param _Path: Full path of the node, /aaa/bbb/ccc.ipynb, consists of the name of each node.

        :type Path: str
        """
        self._CodeFileId = None
        self._CodeFileName = None
        self._OwnerUin = None
        self._CodeFileConfig = None
        self._CodeFileContent = None
        self._UpdateUserUin = None
        self._ProjectId = None
        self._UpdateTime = None
        self._CreateTime = None
        self._AccessScope = None
        self._Path = None

    @property
    def CodeFileId(self):
        r"""Script ID


        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def CodeFileName(self):
        r"""Script name.

        :rtype: str
        """
        return self._CodeFileName

    @CodeFileName.setter
    def CodeFileName(self, CodeFileName):
        self._CodeFileName = CodeFileName

    @property
    def OwnerUin(self):
        r"""Specifies the script owner uin.

        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CodeFileConfig(self):
        r"""Specifies the script configuration.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""Specifies the script content.

        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent

    @property
    def UpdateUserUin(self):
        r"""Latest operator.

        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def ProjectId(self):
        r"""Project ID.


        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UpdateTime(self):
        r"""Update time. format: yyyy-MM-dd hh:MM:ss.
Note: This field may return null, indicating that no valid 
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""Creation time. format: yyyy-MM-dd hh:MM:ss.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.

        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""Full path of the node, /aaa/bbb/ccc.ipynb, consists of the name of each node.

        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._CodeFileId = params.get("CodeFileId")
        self._CodeFileName = params.get("CodeFileName")
        self._OwnerUin = params.get("OwnerUin")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._ProjectId = params.get("ProjectId")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFileConfig(AbstractModel):
    r"""Data exploration script configuration.

    """

    def __init__(self):
        r"""
        :param _Params: Advanced running parameter variable replacement map-json String,String.

        :type Params: str
        :param _NotebookSessionInfo: notebook kernel session information.

        :type NotebookSessionInfo: :class:`tencentcloud.wedata.v20250806.models.NotebookSessionInfo`
        """
        self._Params = None
        self._NotebookSessionInfo = None

    @property
    def Params(self):
        r"""Advanced running parameter variable replacement map-json String,String.

        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def NotebookSessionInfo(self):
        r"""notebook kernel session information.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.NotebookSessionInfo`
        """
        return self._NotebookSessionInfo

    @NotebookSessionInfo.setter
    def NotebookSessionInfo(self, NotebookSessionInfo):
        self._NotebookSessionInfo = NotebookSessionInfo


    def _deserialize(self, params):
        self._Params = params.get("Params")
        if params.get("NotebookSessionInfo") is not None:
            self._NotebookSessionInfo = NotebookSessionInfo()
            self._NotebookSessionInfo._deserialize(params.get("NotebookSessionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeFolderNode(AbstractModel):
    r"""Explores data script file tree node.

    """

    def __init__(self):
        r"""
        :param _Id: Unique identifier
        :type Id: str
        :param _Title: Name
        :type Title: str
        :param _Type: folder type, script.
        :type Type: str
        :param _IsLeaf: Whether it is a leaf node.
        :type IsLeaf: bool
        :param _Params: Business parameters	
	

        :type Params: str
        :param _AccessScope: Permission scope: SHARED, PRIVATE.

        :type AccessScope: str
        :param _Path: Node path.
        :type Path: str
        :param _OwnerUin: Specifies the uin of the responsible person for the directory/file.
        :type OwnerUin: str
        :param _CreateUserUin: Creator
        :type CreateUserUin: str
        :param _NodePermission: Specifies the permission of the current user for nodes.	

        :type NodePermission: str
        :param _Children: Sub-node list


        :type Children: list of CodeFolderNode
        """
        self._Id = None
        self._Title = None
        self._Type = None
        self._IsLeaf = None
        self._Params = None
        self._AccessScope = None
        self._Path = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._NodePermission = None
        self._Children = None

    @property
    def Id(self):
        r"""Unique identifier
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        r"""Name
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Type(self):
        r"""folder type, script.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsLeaf(self):
        r"""Whether it is a leaf node.
        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def Params(self):
        r"""Business parameters	
	

        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AccessScope(self):
        r"""Permission scope: SHARED, PRIVATE.

        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""Node path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def OwnerUin(self):
        r"""Specifies the uin of the responsible person for the directory/file.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""Creator
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def NodePermission(self):
        r"""Specifies the permission of the current user for nodes.	

        :rtype: str
        """
        return self._NodePermission

    @NodePermission.setter
    def NodePermission(self, NodePermission):
        self._NodePermission = NodePermission

    @property
    def Children(self):
        r"""Sub-node list


        :rtype: list of CodeFolderNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Title = params.get("Title")
        self._Type = params.get("Type")
        self._IsLeaf = params.get("IsLeaf")
        self._Params = params.get("Params")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._NodePermission = params.get("NodePermission")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = CodeFolderNode()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFileActionResult(AbstractModel):
    r"""CodeStudio file object operation result.

    """

    def __init__(self):
        r"""
        :param _Status: Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :type Status: bool
        :param _CodeFileId: Folder ID.

        :type CodeFileId: str
        """
        self._Status = None
        self._CodeFileId = None

    @property
    def Status(self):
        r"""Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CodeFileId(self):
        r"""Folder ID.

        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CodeFileId = params.get("CodeFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFolderActionResult(AbstractModel):
    r"""CodeStudio folder object operation result.

    """

    def __init__(self):
        r"""
        :param _Status: Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :type Status: bool
        :param _FolderId: Folder ID.


        :type FolderId: str
        """
        self._Status = None
        self._FolderId = None

    @property
    def Status(self):
        r"""Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""Folder ID.


        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeStudioFolderResult(AbstractModel):
    r"""CodeStudio folder object operation result.

    """

    def __init__(self):
        r"""
        :param _FolderId: Folder ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""Folder ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmRuleData(AbstractModel):
    r"""Describes the response result of creating an Alarm rule.

    """

    def __init__(self):
        r"""
        :param _AlarmRuleId: Specifies the unique id of the Alarm rule.
        :type AlarmRuleId: str
        """
        self._AlarmRuleId = None

    @property
    def AlarmRuleId(self):
        r"""Specifies the unique id of the Alarm rule.
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFileRequest(AbstractModel):
    r"""CreateCodeFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _CodeFileName: Filename of the code file.
        :type CodeFileName: str
        :param _ParentFolderPath: Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.
        :type ParentFolderPath: str
        :param _CodeFileConfig: Specifies the code file configuration.
        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: Specifies the code file content.
        :type CodeFileContent: str
        """
        self._ProjectId = None
        self._CodeFileName = None
        self._ParentFolderPath = None
        self._CodeFileConfig = None
        self._CodeFileContent = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileName(self):
        r"""Filename of the code file.
        :rtype: str
        """
        return self._CodeFileName

    @CodeFileName.setter
    def CodeFileName(self, CodeFileName):
        self._CodeFileName = CodeFileName

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def CodeFileConfig(self):
        r"""Specifies the code file configuration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""Specifies the code file content.
        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileName = params.get("CodeFileName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFileResponse(AbstractModel):
    r"""CreateCodeFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCodeFolderRequest(AbstractModel):
    r"""CreateCodeFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        :param _ParentFolderPath: Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.
        :type ParentFolderPath: str
        """
        self._ProjectId = None
        self._FolderName = None
        self._ParentFolderPath = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderName = params.get("FolderName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCodeFolderResponse(AbstractModel):
    r"""CreateCodeFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDataBackfillPlanRequest(AbstractModel):
    r"""CreateDataBackfillPlan request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _TaskIds: Backfill task collection.
        :type TaskIds: list of str
        :param _DataBackfillRangeList: Specifies the data time configuration for the backfill task.
        :type DataBackfillRangeList: list of DataBackfillRange
        :param _TimeZone: Time zone, default UTC+8.
        :type TimeZone: str
        :param _DataBackfillPlanName: Backfill plan name. if left empty, a string of characters is randomly generated by system.
        :type DataBackfillPlanName: str
        :param _CheckParentType: Check parent task type. valid values: NONE (do not check ALL), ALL (check ALL upstream parent tasks), MAKE_SCOPE (only check in the currently selected tasks of the backfill plan). default: NONE (do not check).
        :type CheckParentType: str
        :param _SkipEventListening: Specifies whether to ignore event dependency for backfill. default true.
        :type SkipEventListening: bool
        :param _RedefineSelfWorkflowDependency: Custom workflow self-dependency. valid values: yes or no. if not configured, use the original workflow self-dependency.
        :type RedefineSelfWorkflowDependency: str
        :param _RedefineParallelNum: Customizes the degree of concurrency for instance running. if without configuring, use the existing self-dependent of the task.
        :type RedefineParallelNum: int
        :param _SchedulerResourceGroupId: Scheduling resource group id. if left empty, indicates usage of the original task scheduling execution resource group.
        :type SchedulerResourceGroupId: str
        :param _IntegrationResourceGroupId: Integration task resource group id. indicates usage of the original task scheduling execution resource group if empty.
        :type IntegrationResourceGroupId: str
        :param _RedefineParamList: Custom parameter. re-specifies the task's parameters to facilitate the execution of new logic by replenished instances.
        :type RedefineParamList: list of KVPair
        :param _DataTimeOrder: Backfill Execution Order - The execution order for backfill instances based on their data time. Effective only when both conditions are met:

1. Must be the same cycle task.

2. Priority is given to dependency order. If no dependencies apply, execution follows the configured order.

Valid values:

-NORMAL: No specific order (default)

-ORDER: Execute in chronological order

-REVERSE: Execute in reverse chronological order
        :type DataTimeOrder: str
        :param _RedefineCycleType: Backfill Instance Regeneration Cycle - If set, this will redefine the generation cycle of backfill task instances. Currently, only daily instances can be converted into instances generated on the first day of each month.

Valid value:

MONTH_CYCLE: Monthly
        :type RedefineCycleType: str
        """
        self._ProjectId = None
        self._TaskIds = None
        self._DataBackfillRangeList = None
        self._TimeZone = None
        self._DataBackfillPlanName = None
        self._CheckParentType = None
        self._SkipEventListening = None
        self._RedefineSelfWorkflowDependency = None
        self._RedefineParallelNum = None
        self._SchedulerResourceGroupId = None
        self._IntegrationResourceGroupId = None
        self._RedefineParamList = None
        self._DataTimeOrder = None
        self._RedefineCycleType = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""Backfill task collection.
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def DataBackfillRangeList(self):
        r"""Specifies the data time configuration for the backfill task.
        :rtype: list of DataBackfillRange
        """
        return self._DataBackfillRangeList

    @DataBackfillRangeList.setter
    def DataBackfillRangeList(self, DataBackfillRangeList):
        self._DataBackfillRangeList = DataBackfillRangeList

    @property
    def TimeZone(self):
        r"""Time zone, default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def DataBackfillPlanName(self):
        r"""Backfill plan name. if left empty, a string of characters is randomly generated by system.
        :rtype: str
        """
        return self._DataBackfillPlanName

    @DataBackfillPlanName.setter
    def DataBackfillPlanName(self, DataBackfillPlanName):
        self._DataBackfillPlanName = DataBackfillPlanName

    @property
    def CheckParentType(self):
        r"""Check parent task type. valid values: NONE (do not check ALL), ALL (check ALL upstream parent tasks), MAKE_SCOPE (only check in the currently selected tasks of the backfill plan). default: NONE (do not check).
        :rtype: str
        """
        return self._CheckParentType

    @CheckParentType.setter
    def CheckParentType(self, CheckParentType):
        self._CheckParentType = CheckParentType

    @property
    def SkipEventListening(self):
        r"""Specifies whether to ignore event dependency for backfill. default true.
        :rtype: bool
        """
        return self._SkipEventListening

    @SkipEventListening.setter
    def SkipEventListening(self, SkipEventListening):
        self._SkipEventListening = SkipEventListening

    @property
    def RedefineSelfWorkflowDependency(self):
        r"""Custom workflow self-dependency. valid values: yes or no. if not configured, use the original workflow self-dependency.
        :rtype: str
        """
        return self._RedefineSelfWorkflowDependency

    @RedefineSelfWorkflowDependency.setter
    def RedefineSelfWorkflowDependency(self, RedefineSelfWorkflowDependency):
        self._RedefineSelfWorkflowDependency = RedefineSelfWorkflowDependency

    @property
    def RedefineParallelNum(self):
        r"""Customizes the degree of concurrency for instance running. if without configuring, use the existing self-dependent of the task.
        :rtype: int
        """
        return self._RedefineParallelNum

    @RedefineParallelNum.setter
    def RedefineParallelNum(self, RedefineParallelNum):
        self._RedefineParallelNum = RedefineParallelNum

    @property
    def SchedulerResourceGroupId(self):
        r"""Scheduling resource group id. if left empty, indicates usage of the original task scheduling execution resource group.
        :rtype: str
        """
        return self._SchedulerResourceGroupId

    @SchedulerResourceGroupId.setter
    def SchedulerResourceGroupId(self, SchedulerResourceGroupId):
        self._SchedulerResourceGroupId = SchedulerResourceGroupId

    @property
    def IntegrationResourceGroupId(self):
        r"""Integration task resource group id. indicates usage of the original task scheduling execution resource group if empty.
        :rtype: str
        """
        return self._IntegrationResourceGroupId

    @IntegrationResourceGroupId.setter
    def IntegrationResourceGroupId(self, IntegrationResourceGroupId):
        self._IntegrationResourceGroupId = IntegrationResourceGroupId

    @property
    def RedefineParamList(self):
        r"""Custom parameter. re-specifies the task's parameters to facilitate the execution of new logic by replenished instances.
        :rtype: list of KVPair
        """
        return self._RedefineParamList

    @RedefineParamList.setter
    def RedefineParamList(self, RedefineParamList):
        self._RedefineParamList = RedefineParamList

    @property
    def DataTimeOrder(self):
        r"""Backfill Execution Order - The execution order for backfill instances based on their data time. Effective only when both conditions are met:

1. Must be the same cycle task.

2. Priority is given to dependency order. If no dependencies apply, execution follows the configured order.

Valid values:

-NORMAL: No specific order (default)

-ORDER: Execute in chronological order

-REVERSE: Execute in reverse chronological order
        :rtype: str
        """
        return self._DataTimeOrder

    @DataTimeOrder.setter
    def DataTimeOrder(self, DataTimeOrder):
        self._DataTimeOrder = DataTimeOrder

    @property
    def RedefineCycleType(self):
        r"""Backfill Instance Regeneration Cycle - If set, this will redefine the generation cycle of backfill task instances. Currently, only daily instances can be converted into instances generated on the first day of each month.

Valid value:

MONTH_CYCLE: Monthly
        :rtype: str
        """
        return self._RedefineCycleType

    @RedefineCycleType.setter
    def RedefineCycleType(self, RedefineCycleType):
        self._RedefineCycleType = RedefineCycleType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        if params.get("DataBackfillRangeList") is not None:
            self._DataBackfillRangeList = []
            for item in params.get("DataBackfillRangeList"):
                obj = DataBackfillRange()
                obj._deserialize(item)
                self._DataBackfillRangeList.append(obj)
        self._TimeZone = params.get("TimeZone")
        self._DataBackfillPlanName = params.get("DataBackfillPlanName")
        self._CheckParentType = params.get("CheckParentType")
        self._SkipEventListening = params.get("SkipEventListening")
        self._RedefineSelfWorkflowDependency = params.get("RedefineSelfWorkflowDependency")
        self._RedefineParallelNum = params.get("RedefineParallelNum")
        self._SchedulerResourceGroupId = params.get("SchedulerResourceGroupId")
        self._IntegrationResourceGroupId = params.get("IntegrationResourceGroupId")
        if params.get("RedefineParamList") is not None:
            self._RedefineParamList = []
            for item in params.get("RedefineParamList"):
                obj = KVPair()
                obj._deserialize(item)
                self._RedefineParamList.append(obj)
        self._DataTimeOrder = params.get("DataTimeOrder")
        self._RedefineCycleType = params.get("RedefineCycleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataBackfillPlanResponse(AbstractModel):
    r"""CreateDataBackfillPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the creation result of the data backfill plan.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateDataReplenishmentPlan`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the creation result of the data backfill plan.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateDataReplenishmentPlan`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateDataReplenishmentPlan()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateDataReplenishmentPlan(AbstractModel):
    r"""Creates a data backfill plan result.

    """

    def __init__(self):
        r"""
        :param _DataBackfillPlanId: Specifies the backfill plan Id.
        :type DataBackfillPlanId: str
        """
        self._DataBackfillPlanId = None

    @property
    def DataBackfillPlanId(self):
        r"""Specifies the backfill plan Id.
        :rtype: str
        """
        return self._DataBackfillPlanId

    @DataBackfillPlanId.setter
    def DataBackfillPlanId(self, DataBackfillPlanId):
        self._DataBackfillPlanId = DataBackfillPlanId


    def _deserialize(self, params):
        self._DataBackfillPlanId = params.get("DataBackfillPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFolderResult(AbstractModel):
    r"""Folder creation result.

    """

    def __init__(self):
        r"""
        :param _FolderId: Folder ID upon successful creation. error will be reported if creation failed.
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""Folder ID upon successful creation. error will be reported if creation failed.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpsAlarmRuleRequest(AbstractModel):
    r"""CreateOpsAlarmRule request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AlarmRuleName: Specifies the Alarm rule name.
        :type AlarmRuleName: str
        :param _MonitorObjectIds: Monitoring Object Business ID List - Pass different business IDs depending on the value of MonitorType:

1 (Task): MonitorObjectIds should contain a list of task IDs.

2 (Workflow): MonitorObjectIds should contain a list of workflow IDs (workflow IDs can be obtained using the ListWorkflows API).

3 (Project): MonitorObjectIds should contain a list of project IDs.
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :type AlarmTypes: list of str
        :param _AlarmGroups: Alarm recipient configuration.
        :type AlarmGroups: list of AlarmGroup
        :param _MonitorObjectType: Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :type MonitorObjectType: int
        :param _AlarmRuleDetail: Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _AlarmLevel: Alarm level. 1. ordinary, 2. important, 3. critical (default: 1. ordinary).
        :type AlarmLevel: int
        :param _Description: Describes the Alarm rule.
        :type Description: str
        """
        self._ProjectId = None
        self._AlarmRuleName = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._AlarmGroups = None
        self._MonitorObjectType = None
        self._AlarmRuleDetail = None
        self._AlarmLevel = None
        self._Description = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleName(self):
        r"""Specifies the Alarm rule name.
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def MonitorObjectIds(self):
        r"""Monitoring Object Business ID List - Pass different business IDs depending on the value of MonitorType:

1 (Task): MonitorObjectIds should contain a list of task IDs.

2 (Workflow): MonitorObjectIds should contain a list of workflow IDs (workflow IDs can be obtained using the ListWorkflows API).

3 (Project): MonitorObjectIds should contain a list of project IDs.
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def AlarmGroups(self):
        r"""Alarm recipient configuration.
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups

    @property
    def MonitorObjectType(self):
        r"""Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def AlarmRuleDetail(self):
        r"""Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def AlarmLevel(self):
        r"""Alarm level. 1. ordinary, 2. important, 3. critical (default: 1. ordinary).
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def Description(self):
        r"""Describes the Alarm rule.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        self._MonitorObjectType = params.get("MonitorObjectType")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._AlarmLevel = params.get("AlarmLevel")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpsAlarmRuleResponse(AbstractModel):
    r"""CreateOpsAlarmRule response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the unique id of the Alarm rule.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateAlarmRuleData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the unique id of the Alarm rule.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateAlarmRuleData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateAlarmRuleData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateResourceFileRequest(AbstractModel):
    r"""CreateResourceFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ResourceName: Resource file name. should be consistent with the uploaded file name.
        :type ResourceName: str
        :param _BucketName: Bucket name. can be obtained from the GetResourceCosPath api.
        :type BucketName: str
        :param _CosRegion: BucketName specifies the cos storage bucket region.
        :type CosRegion: str
        :param _ParentFolderPath: Upload path for resource files in the project. value example: /wedata/qxxxm/. root directory, please use /.
        :type ParentFolderPath: str
        :param _ResourceFile: -Upload file and manual entry are two methods, choose one. if both are provided, the sequence is file > manual entry.
-The manually entered value must be an existing cos path. /datastudio/resource/ is the fixed prefix. projectId is the project ID. import a specific value. parentFolderPath is the folder path. name is the file name. value example: /datastudio/resource/projectId/parentFolderPath/name. 

        :type ResourceFile: str
        :param _BundleId: Bundle Client ID.
        :type BundleId: str
        :param _BundleInfo: bundle client info.
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceName = None
        self._BucketName = None
        self._CosRegion = None
        self._ParentFolderPath = None
        self._ResourceFile = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceName(self):
        r"""Resource file name. should be consistent with the uploaded file name.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def BucketName(self):
        r"""Bucket name. can be obtained from the GetResourceCosPath api.
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def CosRegion(self):
        r"""BucketName specifies the cos storage bucket region.
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def ParentFolderPath(self):
        r"""Upload path for resource files in the project. value example: /wedata/qxxxm/. root directory, please use /.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ResourceFile(self):
        r"""-Upload file and manual entry are two methods, choose one. if both are provided, the sequence is file > manual entry.
-The manually entered value must be an existing cos path. /datastudio/resource/ is the fixed prefix. projectId is the project ID. import a specific value. parentFolderPath is the folder path. name is the file name. value example: /datastudio/resource/projectId/parentFolderPath/name. 

        :rtype: str
        """
        return self._ResourceFile

    @ResourceFile.setter
    def ResourceFile(self, ResourceFile):
        self._ResourceFile = ResourceFile

    @property
    def BundleId(self):
        r"""Bundle Client ID.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""bundle client info.
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceName = params.get("ResourceName")
        self._BucketName = params.get("BucketName")
        self._CosRegion = params.get("CosRegion")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._ResourceFile = params.get("ResourceFile")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFileResponse(AbstractModel):
    r"""CreateResourceFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Create resource file result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Create resource file result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateResourceFileResult(AbstractModel):
    r"""Create resource file result.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource file ID.
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        r"""Resource file ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFolderRequest(AbstractModel):
    r"""CreateResourceFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Parent folder's absolute path. Example: /wedata/test. Use / to represent the root directory.
        :type ParentFolderPath: str
        :param _FolderName: Folder name.
        :type FolderName: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder's absolute path. Example: /wedata/test. Use / to represent the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceFolderResponse(AbstractModel):
    r"""CreateResourceFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Creation result of the folder. Error will be reported if failed to create.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Creation result of the folder. Error will be reported if failed to create.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateSQLFolderRequest(AbstractModel):
    r"""CreateSQLFolder request structure.

    """

    def __init__(self):
        r"""
        :param _FolderName: Folder name.
        :type FolderName: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Parent folder path, /aaa/bbb/ccc. path header must include a slash. pass / to query the root directory.
        :type ParentFolderPath: str
        :param _AccessScope: Access permission: SHARED, PRIVATE.
        :type AccessScope: str
        """
        self._FolderName = None
        self._ProjectId = None
        self._ParentFolderPath = None
        self._AccessScope = None

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, /aaa/bbb/ccc. path header must include a slash. pass / to query the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._FolderName = params.get("FolderName")
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSQLFolderResponse(AbstractModel):
    r"""CreateSQLFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :type Data: :class:`tencentcloud.wedata.v20250806.models.SqlCreateResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).

        :rtype: :class:`tencentcloud.wedata.v20250806.models.SqlCreateResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SqlCreateResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateSQLScriptRequest(AbstractModel):
    r"""CreateSQLScript request structure.

    """

    def __init__(self):
        r"""
        :param _ScriptName: Script name.
        :type ScriptName: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _ParentFolderPath: Parent folder path, /aaa/bbb/ccc. root directory is empty string or /.
        :type ParentFolderPath: str
        :param _ScriptConfig: Specifies the script configuration for data exploration.
        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: Specifies the script content, if any, needs to be base64 encoded.
        :type ScriptContent: str
        :param _AccessScope: Access permission: SHARED, PRIVATE.
        :type AccessScope: str
        """
        self._ScriptName = None
        self._ProjectId = None
        self._ParentFolderPath = None
        self._ScriptConfig = None
        self._ScriptContent = None
        self._AccessScope = None

    @property
    def ScriptName(self):
        r"""Script name.
        :rtype: str
        """
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, /aaa/bbb/ccc. root directory is empty string or /.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ScriptConfig(self):
        r"""Specifies the script configuration for data exploration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""Specifies the script content, if any, needs to be base64 encoded.
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._ScriptName = params.get("ScriptName")
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSQLScriptResponse(AbstractModel):
    r"""CreateSQLScript response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTaskBaseAttribute(AbstractModel):
    r"""Describes the basic attribute information of the task.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name.
        :type TaskName: str
        :param _TaskTypeId: Task type ID:

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 32:DLC SQL
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :type TaskTypeId: str
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _OwnerUin: Task owner ID. defaults to the current user.
        :type OwnerUin: str
        :param _TaskDescription: Task description
        :type TaskDescription: str
        """
        self._TaskName = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._OwnerUin = None
        self._TaskDescription = None

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeId(self):
        r"""Task type ID:

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 32:DLC SQL
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :rtype: str
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def OwnerUin(self):
        r"""Task owner ID. defaults to the current user.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""Task description
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskConfiguration(AbstractModel):
    r"""Creates task configuration information.

    """

    def __init__(self):
        r"""
        :param _ResourceGroup: Resource Group ID: Must be obtained via DescribeNormalSchedulerExecutorGroups API to get the ExecutorGroupId.
        :type ResourceGroup: str
        :param _CodeContent: Base64 encoding of the code content.
        :type CodeContent: str
        :param _TaskExtConfigurationList: Specifies the configuration list of task extended attributes.
        :type TaskExtConfigurationList: list of TaskExtParameter
        :param _DataCluster: Cluster ID
        :type DataCluster: str
        :param _BrokerIp: Specifies the running node.
        :type BrokerIp: str
        :param _YarnQueue: Resource Pool Queue Name: Must be obtained using DescribeProjectClusterQueues API.
        :type YarnQueue: str
        :param _SourceServiceId: Source Data Source ID - One or more IDs separated by semicolons (;). Retrieve IDs using the DescribeDataSourceWithoutInfo API.
        :type SourceServiceId: str
        :param _TargetServiceId: Target data source ID- One or more IDs separated by semicolons (;). Retrieve IDs using the DescribeDataSourceWithoutInfo API.
        :type TargetServiceId: str
        :param _TaskSchedulingParameterList: Scheduling parameter.
        :type TaskSchedulingParameterList: list of TaskSchedulingParameter
        :param _BundleId: ID used by the Bundle.
        :type BundleId: str
        :param _BundleInfo: Bundle info.
        :type BundleInfo: str
        """
        self._ResourceGroup = None
        self._CodeContent = None
        self._TaskExtConfigurationList = None
        self._DataCluster = None
        self._BrokerIp = None
        self._YarnQueue = None
        self._SourceServiceId = None
        self._TargetServiceId = None
        self._TaskSchedulingParameterList = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ResourceGroup(self):
        r"""Resource Group ID: Must be obtained via DescribeNormalSchedulerExecutorGroups API to get the ExecutorGroupId.
        :rtype: str
        """
        return self._ResourceGroup

    @ResourceGroup.setter
    def ResourceGroup(self, ResourceGroup):
        self._ResourceGroup = ResourceGroup

    @property
    def CodeContent(self):
        r"""Base64 encoding of the code content.
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def TaskExtConfigurationList(self):
        r"""Specifies the configuration list of task extended attributes.
        :rtype: list of TaskExtParameter
        """
        return self._TaskExtConfigurationList

    @TaskExtConfigurationList.setter
    def TaskExtConfigurationList(self, TaskExtConfigurationList):
        self._TaskExtConfigurationList = TaskExtConfigurationList

    @property
    def DataCluster(self):
        r"""Cluster ID
        :rtype: str
        """
        return self._DataCluster

    @DataCluster.setter
    def DataCluster(self, DataCluster):
        self._DataCluster = DataCluster

    @property
    def BrokerIp(self):
        r"""Specifies the running node.
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def YarnQueue(self):
        r"""Resource Pool Queue Name: Must be obtained using DescribeProjectClusterQueues API.
        :rtype: str
        """
        return self._YarnQueue

    @YarnQueue.setter
    def YarnQueue(self, YarnQueue):
        self._YarnQueue = YarnQueue

    @property
    def SourceServiceId(self):
        r"""Source Data Source ID - One or more IDs separated by semicolons (;). Retrieve IDs using the DescribeDataSourceWithoutInfo API.
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def TargetServiceId(self):
        r"""Target data source ID- One or more IDs separated by semicolons (;). Retrieve IDs using the DescribeDataSourceWithoutInfo API.
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def TaskSchedulingParameterList(self):
        r"""Scheduling parameter.
        :rtype: list of TaskSchedulingParameter
        """
        return self._TaskSchedulingParameterList

    @TaskSchedulingParameterList.setter
    def TaskSchedulingParameterList(self, TaskSchedulingParameterList):
        self._TaskSchedulingParameterList = TaskSchedulingParameterList

    @property
    def BundleId(self):
        r"""ID used by the Bundle.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle info.
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ResourceGroup = params.get("ResourceGroup")
        self._CodeContent = params.get("CodeContent")
        if params.get("TaskExtConfigurationList") is not None:
            self._TaskExtConfigurationList = []
            for item in params.get("TaskExtConfigurationList"):
                obj = TaskExtParameter()
                obj._deserialize(item)
                self._TaskExtConfigurationList.append(obj)
        self._DataCluster = params.get("DataCluster")
        self._BrokerIp = params.get("BrokerIp")
        self._YarnQueue = params.get("YarnQueue")
        self._SourceServiceId = params.get("SourceServiceId")
        self._TargetServiceId = params.get("TargetServiceId")
        if params.get("TaskSchedulingParameterList") is not None:
            self._TaskSchedulingParameterList = []
            for item in params.get("TaskSchedulingParameterList"):
                obj = TaskSchedulingParameter()
                obj._deserialize(item)
                self._TaskSchedulingParameterList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskRequest(AbstractModel):
    r"""CreateTask request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskBaseAttribute: The basic attributes of the task.
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.CreateTaskBaseAttribute`
        :param _TaskConfiguration: Task configurations.
        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.CreateTaskConfiguration`
        :param _TaskSchedulerConfiguration: Task scheduling configuration.
        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.CreateTaskSchedulerConfiguration`
        """
        self._ProjectId = None
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskBaseAttribute(self):
        r"""The basic attributes of the task.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""Task configurations.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""Task scheduling configuration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = CreateTaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = CreateTaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = CreateTaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    r"""CreateTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task ID
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task ID
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTaskResult(AbstractModel):
    r"""Create task return format.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID

        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID

        :rtype: str
        """
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
        


class CreateTaskSchedulerConfiguration(AbstractModel):
    r"""Creates task scheduling configuration info.

    """

    def __init__(self):
        r"""
        :param _CycleType: Period type: defaults to DAY_CYCLE.

Supported types. 

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type.
        :type CycleType: str
        :param _ScheduleTimeZone: Time zone, defaults to UTC+8.
        :type ScheduleTimeZone: str
        :param _CrontabExpression: Cron expression, defaults to 0 0 0 * * ? *.
        :type CrontabExpression: str
        :param _StartTime: Effective date, defaults to 00:00:00 of the current date.
        :type StartTime: str
        :param _EndTime: End date, defaults to 2099-12-31 23:59:59.
        :type EndTime: str
        :param _ExecutionStartTime: Execution time: the left-closed interval. Default: 00:00.
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: Execution time: the right closed interval. Default: 23:59.
        :type ExecutionEndTime: str
        :param _ScheduleRunType: Scheduling type: 0 for normal scheduling, 1 for dry-run scheduling. Default is 0.
        :type ScheduleRunType: str
        :param _CalendarOpen: Calendar scheduling value: 0 or 1, where 1 means ON and 0 means OFF. Default is 0.
        :type CalendarOpen: str
        :param _CalendarId: Calendar scheduling:  the calendar ID.
        :type CalendarId: str
        :param _SelfDepend: Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :type SelfDepend: str
        :param _UpstreamDependencyConfigList: Specifies the upstream dependency list.
        :type UpstreamDependencyConfigList: list of DependencyTaskBrief
        :param _EventListenerList: List of Events
        :type EventListenerList: list of EventListener
        :param _RunPriority: Task scheduling priority. Valid values: 4 (high), 5 (medium), 6 (low). Default: 6.
        :type RunPriority: str
        :param _RetryWait: Retry Policy: Retry Wait Time (in minutes): Default 5
        :type RetryWait: str
        :param _MaxRetryAttempts: Retry Policy: maximum attempts. Default: 4.
        :type MaxRetryAttempts: str
        :param _ExecutionTTL: Timeout Handling Policy: Execution Timeout (in minutes), default: -1
        :type ExecutionTTL: str
        :param _WaitExecutionTotalTTL: Timeout Handling Policy: Wait Duration Timeout  (in minutes), default: -1
        :type WaitExecutionTotalTTL: str
        :param _AllowRedoType: Rerun & Refill Configuration: Default: ALL;

* ALL: Rerun or refill is allowed regardless of whether the task succeeds or fails.

* FAILURE: Rerun or refill is allowed only if the task fails; not allowed if the task succeeds.

* NONE: Rerun or refill is not allowed regardless of success or failure.
        :type AllowRedoType: str
        :param _ParamTaskOutList: Output parameter list.
        :type ParamTaskOutList: list of OutTaskParameter
        :param _ParamTaskInList: Input parameter list.
        :type ParamTaskInList: list of InTaskParameter
        :param _TaskOutputRegistryList: Output registration.
        :type TaskOutputRegistryList: list of TaskDataRegistry
        :param _InitStrategy: **Instance generation policy**.
T_PLUS_0: specifies t+0 generation. default policy.
T_PLUS_1: specifies t+1 generation.
        :type InitStrategy: str
        """
        self._CycleType = None
        self._ScheduleTimeZone = None
        self._CrontabExpression = None
        self._StartTime = None
        self._EndTime = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._ScheduleRunType = None
        self._CalendarOpen = None
        self._CalendarId = None
        self._SelfDepend = None
        self._UpstreamDependencyConfigList = None
        self._EventListenerList = None
        self._RunPriority = None
        self._RetryWait = None
        self._MaxRetryAttempts = None
        self._ExecutionTTL = None
        self._WaitExecutionTotalTTL = None
        self._AllowRedoType = None
        self._ParamTaskOutList = None
        self._ParamTaskInList = None
        self._TaskOutputRegistryList = None
        self._InitStrategy = None

    @property
    def CycleType(self):
        r"""Period type: defaults to DAY_CYCLE.

Supported types. 

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type.
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ScheduleTimeZone(self):
        r"""Time zone, defaults to UTC+8.
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CrontabExpression(self):
        r"""Cron expression, defaults to 0 0 0 * * ? *.
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def StartTime(self):
        r"""Effective date, defaults to 00:00:00 of the current date.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End date, defaults to 2099-12-31 23:59:59.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionStartTime(self):
        r"""Execution time: the left-closed interval. Default: 00:00.
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""Execution time: the right closed interval. Default: 23:59.
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def ScheduleRunType(self):
        r"""Scheduling type: 0 for normal scheduling, 1 for dry-run scheduling. Default is 0.
        :rtype: str
        """
        return self._ScheduleRunType

    @ScheduleRunType.setter
    def ScheduleRunType(self, ScheduleRunType):
        self._ScheduleRunType = ScheduleRunType

    @property
    def CalendarOpen(self):
        r"""Calendar scheduling value: 0 or 1, where 1 means ON and 0 means OFF. Default is 0.
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""Calendar scheduling:  the calendar ID.
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId

    @property
    def SelfDepend(self):
        r"""Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def UpstreamDependencyConfigList(self):
        r"""Specifies the upstream dependency list.
        :rtype: list of DependencyTaskBrief
        """
        return self._UpstreamDependencyConfigList

    @UpstreamDependencyConfigList.setter
    def UpstreamDependencyConfigList(self, UpstreamDependencyConfigList):
        self._UpstreamDependencyConfigList = UpstreamDependencyConfigList

    @property
    def EventListenerList(self):
        r"""List of Events
        :rtype: list of EventListener
        """
        return self._EventListenerList

    @EventListenerList.setter
    def EventListenerList(self, EventListenerList):
        self._EventListenerList = EventListenerList

    @property
    def RunPriority(self):
        r"""Task scheduling priority. Valid values: 4 (high), 5 (medium), 6 (low). Default: 6.
        :rtype: str
        """
        return self._RunPriority

    @RunPriority.setter
    def RunPriority(self, RunPriority):
        self._RunPriority = RunPriority

    @property
    def RetryWait(self):
        r"""Retry Policy: Retry Wait Time (in minutes): Default 5
        :rtype: str
        """
        return self._RetryWait

    @RetryWait.setter
    def RetryWait(self, RetryWait):
        self._RetryWait = RetryWait

    @property
    def MaxRetryAttempts(self):
        r"""Retry Policy: maximum attempts. Default: 4.
        :rtype: str
        """
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def ExecutionTTL(self):
        r"""Timeout Handling Policy: Execution Timeout (in minutes), default: -1
        :rtype: str
        """
        return self._ExecutionTTL

    @ExecutionTTL.setter
    def ExecutionTTL(self, ExecutionTTL):
        self._ExecutionTTL = ExecutionTTL

    @property
    def WaitExecutionTotalTTL(self):
        r"""Timeout Handling Policy: Wait Duration Timeout  (in minutes), default: -1
        :rtype: str
        """
        return self._WaitExecutionTotalTTL

    @WaitExecutionTotalTTL.setter
    def WaitExecutionTotalTTL(self, WaitExecutionTotalTTL):
        self._WaitExecutionTotalTTL = WaitExecutionTotalTTL

    @property
    def AllowRedoType(self):
        r"""Rerun & Refill Configuration: Default: ALL;

* ALL: Rerun or refill is allowed regardless of whether the task succeeds or fails.

* FAILURE: Rerun or refill is allowed only if the task fails; not allowed if the task succeeds.

* NONE: Rerun or refill is not allowed regardless of success or failure.
        :rtype: str
        """
        return self._AllowRedoType

    @AllowRedoType.setter
    def AllowRedoType(self, AllowRedoType):
        self._AllowRedoType = AllowRedoType

    @property
    def ParamTaskOutList(self):
        r"""Output parameter list.
        :rtype: list of OutTaskParameter
        """
        return self._ParamTaskOutList

    @ParamTaskOutList.setter
    def ParamTaskOutList(self, ParamTaskOutList):
        self._ParamTaskOutList = ParamTaskOutList

    @property
    def ParamTaskInList(self):
        r"""Input parameter list.
        :rtype: list of InTaskParameter
        """
        return self._ParamTaskInList

    @ParamTaskInList.setter
    def ParamTaskInList(self, ParamTaskInList):
        self._ParamTaskInList = ParamTaskInList

    @property
    def TaskOutputRegistryList(self):
        r"""Output registration.
        :rtype: list of TaskDataRegistry
        """
        return self._TaskOutputRegistryList

    @TaskOutputRegistryList.setter
    def TaskOutputRegistryList(self, TaskOutputRegistryList):
        self._TaskOutputRegistryList = TaskOutputRegistryList

    @property
    def InitStrategy(self):
        r"""**Instance generation policy**.
T_PLUS_0: specifies t+0 generation. default policy.
T_PLUS_1: specifies t+1 generation.
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy


    def _deserialize(self, params):
        self._CycleType = params.get("CycleType")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CrontabExpression = params.get("CrontabExpression")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._ScheduleRunType = params.get("ScheduleRunType")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        self._SelfDepend = params.get("SelfDepend")
        if params.get("UpstreamDependencyConfigList") is not None:
            self._UpstreamDependencyConfigList = []
            for item in params.get("UpstreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._UpstreamDependencyConfigList.append(obj)
        if params.get("EventListenerList") is not None:
            self._EventListenerList = []
            for item in params.get("EventListenerList"):
                obj = EventListener()
                obj._deserialize(item)
                self._EventListenerList.append(obj)
        self._RunPriority = params.get("RunPriority")
        self._RetryWait = params.get("RetryWait")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        self._ExecutionTTL = params.get("ExecutionTTL")
        self._WaitExecutionTotalTTL = params.get("WaitExecutionTotalTTL")
        self._AllowRedoType = params.get("AllowRedoType")
        if params.get("ParamTaskOutList") is not None:
            self._ParamTaskOutList = []
            for item in params.get("ParamTaskOutList"):
                obj = OutTaskParameter()
                obj._deserialize(item)
                self._ParamTaskOutList.append(obj)
        if params.get("ParamTaskInList") is not None:
            self._ParamTaskInList = []
            for item in params.get("ParamTaskInList"):
                obj = InTaskParameter()
                obj._deserialize(item)
                self._ParamTaskInList.append(obj)
        if params.get("TaskOutputRegistryList") is not None:
            self._TaskOutputRegistryList = []
            for item in params.get("TaskOutputRegistryList"):
                obj = TaskDataRegistry()
                obj._deserialize(item)
                self._TaskOutputRegistryList.append(obj)
        self._InitStrategy = params.get("InitStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowFolderRequest(AbstractModel):
    r"""CreateWorkflowFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Parent folder absolute path, such as /abc/de. if it is the root directory, pass /.
        :type ParentFolderPath: str
        :param _FolderName: Specifies the folder name to be created.
        :type FolderName: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder absolute path, such as /abc/de. if it is the root directory, pass /.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def FolderName(self):
        r"""Specifies the folder name to be created.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowFolderResponse(AbstractModel):
    r"""CreateWorkflowFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Folder creation result. error will be reported if creation failed.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Folder creation result. error will be reported if creation failed.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    r"""CreateWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _ParentFolderPath: Specifies the folder path.
        :type ParentFolderPath: str
        :param _WorkflowType: Workflow type. value examples: cycle for periodic workflow; manual for manual workflow. default input: cycle.
        :type WorkflowType: str
        :param _WorkflowDesc: Workflow description.
        :type WorkflowDesc: str
        :param _OwnerUin: Workflow owner ID.
        :type OwnerUin: str
        :param _WorkflowParams: Workflow parameter.
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: Specifies unified scheduling info.
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        :param _BundleId: BundleId item.
        :type BundleId: str
        :param _BundleInfo: Bundle info.
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._WorkflowName = None
        self._ParentFolderPath = None
        self._WorkflowType = None
        self._WorkflowDesc = None
        self._OwnerUin = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowName(self):
        r"""Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ParentFolderPath(self):
        r"""Specifies the folder path.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def WorkflowType(self):
        r"""Workflow type. value examples: cycle for periodic workflow; manual for manual workflow. default input: cycle.
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowDesc(self):
        r"""Workflow description.
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def OwnerUin(self):
        r"""Workflow owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowParams(self):
        r"""Workflow parameter.
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""Specifies unified scheduling info.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def BundleId(self):
        r"""BundleId item.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle info.
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowName = params.get("WorkflowName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._WorkflowType = params.get("WorkflowType")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._OwnerUin = params.get("OwnerUin")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfigurationInfo()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    r"""CreateWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returns the workflow ID.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returns the workflow ID.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CreateWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkflowResult(AbstractModel):
    r"""Create workflow result.

    """

    def __init__(self):
        r"""
        :param _WorkflowId: Workflow id after successful creation.
        :type WorkflowId: str
        """
        self._WorkflowId = None

    @property
    def WorkflowId(self):
        r"""Workflow id after successful creation.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataBackfillRange(AbstractModel):
    r"""Backfill plan date range.

    """

    def __init__(self):
        r"""
        :param _StartDate: Start date in yyyy-MM-dd format. indicates the start from 00:00:00 on the specified date.

        :type StartDate: str
        :param _EndDate: End date in the format yyyy-MM-dd, indicates ending at 23:59:59 of the specified date.

        :type EndDate: str
        :param _ExecutionStartTime: Start time of each day between [StartDate, EndDate] in HH:mm format. effective for tasks with a period of hours or less.

        :type ExecutionStartTime: str
        :param _ExecutionEndTime: End time point between [StartDate, EndDate] in HH:mm format. effective for tasks with a period of hours or less.

        :type ExecutionEndTime: str
        """
        self._StartDate = None
        self._EndDate = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None

    @property
    def StartDate(self):
        r"""Start date in yyyy-MM-dd format. indicates the start from 00:00:00 on the specified date.

        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""End date in the format yyyy-MM-dd, indicates ending at 23:59:59 of the specified date.

        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ExecutionStartTime(self):
        r"""Start time of each day between [StartDate, EndDate] in HH:mm format. effective for tasks with a period of hours or less.

        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""End time point between [StartDate, EndDate] in HH:mm format. effective for tasks with a period of hours or less.

        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmRuleResult(AbstractModel):
    r"""Describes the response result of deleting an Alarm rule.

    """

    def __init__(self):
        r"""
        :param _Status: Whether deletion succeeded.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Whether deletion succeeded.
        :rtype: bool
        """
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
        


class DeleteCodeFileRequest(AbstractModel):
    r"""DeleteCodeFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _CodeFileId: Code file ID. the parameter value comes from the CreateCodeFile API.
        :type CodeFileId: str
        """
        self._ProjectId = None
        self._CodeFileId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""Code file ID. the parameter value comes from the CreateCodeFile API.
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeFileResponse(AbstractModel):
    r"""DeleteCodeFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Execution result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFileActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Execution result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFileActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFileActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteCodeFolderRequest(AbstractModel):
    r"""DeleteCodeFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. the parameter value comes from the CreateCodeFolder API response.
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. the parameter value comes from the CreateCodeFolder API response.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCodeFolderResponse(AbstractModel):
    r"""DeleteCodeFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Execution result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Execution result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteFolderResult(AbstractModel):
    r"""Delete resource folder result.

    """

    def __init__(self):
        r"""
        :param _Status: Deletion status. true indicates success, false indicates failure.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Deletion status. true indicates success, false indicates failure.
        :rtype: bool
        """
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
        


class DeleteOpsAlarmRuleRequest(AbstractModel):
    r"""DeleteOpsAlarmRule request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AlarmRuleId: Alarm Rule Unique ID. Obtained from the response of the CreateAlarmRule API. Either this field or AlarmRuleName must be provided.
        :type AlarmRuleId: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""Alarm Rule Unique ID. Obtained from the response of the CreateAlarmRule API. Either this field or AlarmRuleName must be provided.
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOpsAlarmRuleResponse(AbstractModel):
    r"""DeleteOpsAlarmRule response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Whether deletion succeeded.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteAlarmRuleResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Whether deletion succeeded.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteAlarmRuleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteAlarmRuleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteResourceFileRequest(AbstractModel):
    r"""DeleteResourceFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ResourceId: Resource ID. obtain through the API ListResourceFiles.
        :type ResourceId: str
        """
        self._ProjectId = None
        self._ResourceId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""Resource ID. obtain through the API ListResourceFiles.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceFileResponse(AbstractModel):
    r"""DeleteResourceFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the resource deletion result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the resource deletion result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteResourceFileResult(AbstractModel):
    r"""Delete resource file result.

    """

    def __init__(self):
        r"""
        :param _Status: true
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""true
        :rtype: bool
        """
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
        


class DeleteResourceFolderRequest(AbstractModel):
    r"""DeleteResourceFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. obtain through the ListResourceFolders API.
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. obtain through the ListResourceFolders API.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceFolderResponse(AbstractModel):
    r"""DeleteResourceFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: true represents successful deletion. false represents failure.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""true represents successful deletion. false represents failure.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteSQLFolderRequest(AbstractModel):
    r"""DeleteSQLFolder request structure.

    """

    def __init__(self):
        r"""
        :param _FolderId: Folder ID
        :type FolderId: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        """
        self._FolderId = None
        self._ProjectId = None

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSQLFolderResponse(AbstractModel):
    r"""DeleteSQLFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Operation result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Operation result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteSQLScriptRequest(AbstractModel):
    r"""DeleteSQLScript request structure.

    """

    def __init__(self):
        r"""
        :param _ScriptId: Script Id.
        :type ScriptId: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        """
        self._ScriptId = None
        self._ProjectId = None

    @property
    def ScriptId(self):
        r"""Script Id.
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSQLScriptResponse(AbstractModel):
    r"""DeleteSQLScript response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Execution result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Execution result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    r"""DeleteTask request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _TaskId: Either Task ID or VirtualTaskId must be provided (optional, choose one).
        :type TaskId: str
        :param _OperateInform: Whether to send a notification to downstream task owners when performing task operations.
true: Send notification
false: Do not send notification
default: false.
        :type OperateInform: bool
        :param _DeleteMode: Task Deletion Mode.
true: Do not force downstream task instances to fail
false: Force downstream task instances to fail
default: false 

        :type DeleteMode: bool
        """
        self._ProjectId = None
        self._TaskId = None
        self._OperateInform = None
        self._DeleteMode = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Either Task ID or VirtualTaskId must be provided (optional, choose one).
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperateInform(self):
        r"""Whether to send a notification to downstream task owners when performing task operations.
true: Send notification
false: Do not send notification
default: false.
        :rtype: bool
        """
        return self._OperateInform

    @OperateInform.setter
    def OperateInform(self, OperateInform):
        self._OperateInform = OperateInform

    @property
    def DeleteMode(self):
        r"""Task Deletion Mode.
true: Do not force downstream task instances to fail
false: Force downstream task instances to fail
default: false 

        :rtype: bool
        """
        return self._DeleteMode

    @DeleteMode.setter
    def DeleteMode(self, DeleteMode):
        self._DeleteMode = DeleteMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._OperateInform = params.get("OperateInform")
        self._DeleteMode = params.get("DeleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    r"""DeleteTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Whether deletion succeeded.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Whether deletion succeeded.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteTaskResult(AbstractModel):
    r"""Deletion result of a data development task.

    """

    def __init__(self):
        r"""
        :param _Status: Deletion status. true indicates success. false indicates failure.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Deletion status. true indicates success. false indicates failure.
        :rtype: bool
        """
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
        


class DeleteWorkflowFolderRequest(AbstractModel):
    r"""DeleteWorkflowFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. Obtain through the ListWorkflowFolders API.
        :type FolderId: str
        """
        self._ProjectId = None
        self._FolderId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. Obtain through the ListWorkflowFolders API.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowFolderResponse(AbstractModel):
    r"""DeleteWorkflowFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Deletion result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Deletion result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    r"""DeleteWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _WorkflowId: Workflow id.
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""Workflow id.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    r"""DeleteWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returns the count of successfully deleted workflow tasks, number of failures, and total number of tasks.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returns the count of successfully deleted workflow tasks, number of failures, and total number of tasks.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DeleteWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteWorkflowResult(AbstractModel):
    r"""Delete workflow result.

    """

    def __init__(self):
        r"""
        :param _Status: Indicates whether the workflow deletion was successful
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Indicates whether the workflow deletion was successful
        :rtype: bool
        """
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
        


class DependencyConfigPage(AbstractModel):
    r"""Paginated Query of Upstream Task Dependency Details

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records matching the query conditions.
        :type TotalCount: int
        :param _TotalPageNumber: Total number of pages matching the query conditions.
        :type TotalPageNumber: int
        :param _PageNumber: The page number of the current request.
        :type PageNumber: int
        :param _PageSize: The number of entries in the current request data page.
        :type PageSize: int
        :param _Items: Paginated Data
        :type Items: list of TaskDependDto
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""Total number of records matching the query conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total number of pages matching the query conditions.
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""The page number of the current request.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""The number of entries in the current request data page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""Paginated Data
        :rtype: list of TaskDependDto
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskDependDto()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyStrategyTask(AbstractModel):
    r"""Dependency configuration policy.

    """

    def __init__(self):
        r"""
        :param _PollingNullStrategy: Wait upstream task instance policy: EXECUTING (execute); WAITING (wait).

        :type PollingNullStrategy: str
        :param _TaskDependencyExecutingStrategies: This field is required only when PollingNullStrategy is set to EXECUTING.
Type: List

NOT_EXIST (default) - In cases where minute depends on minute / hour depends on hour, the parent instance does not fall within the scheduling time range of the downstream instance.

PARENT_EXPIRED - The parent instance failed.

PARENT_TIMEOUT - The parent instance timed out.

If any of the above conditions are met, the dependency check for that parent task instance is considered satisfied. In all other cases, the system must wait for the parent instance.
        :type TaskDependencyExecutingStrategies: list of str
        :param _TaskDependencyExecutingTimeoutValue: This field is required only when TaskDependencyExecutingStrategies includes PARENT_TIMEOUT.
Specifies the timeout duration (in minutes) for the downstream task's dependency on the parent instance execution.
        :type TaskDependencyExecutingTimeoutValue: int
        """
        self._PollingNullStrategy = None
        self._TaskDependencyExecutingStrategies = None
        self._TaskDependencyExecutingTimeoutValue = None

    @property
    def PollingNullStrategy(self):
        r"""Wait upstream task instance policy: EXECUTING (execute); WAITING (wait).

        :rtype: str
        """
        return self._PollingNullStrategy

    @PollingNullStrategy.setter
    def PollingNullStrategy(self, PollingNullStrategy):
        self._PollingNullStrategy = PollingNullStrategy

    @property
    def TaskDependencyExecutingStrategies(self):
        r"""This field is required only when PollingNullStrategy is set to EXECUTING.
Type: List

NOT_EXIST (default) - In cases where minute depends on minute / hour depends on hour, the parent instance does not fall within the scheduling time range of the downstream instance.

PARENT_EXPIRED - The parent instance failed.

PARENT_TIMEOUT - The parent instance timed out.

If any of the above conditions are met, the dependency check for that parent task instance is considered satisfied. In all other cases, the system must wait for the parent instance.
        :rtype: list of str
        """
        return self._TaskDependencyExecutingStrategies

    @TaskDependencyExecutingStrategies.setter
    def TaskDependencyExecutingStrategies(self, TaskDependencyExecutingStrategies):
        self._TaskDependencyExecutingStrategies = TaskDependencyExecutingStrategies

    @property
    def TaskDependencyExecutingTimeoutValue(self):
        r"""This field is required only when TaskDependencyExecutingStrategies includes PARENT_TIMEOUT.
Specifies the timeout duration (in minutes) for the downstream task's dependency on the parent instance execution.
        :rtype: int
        """
        return self._TaskDependencyExecutingTimeoutValue

    @TaskDependencyExecutingTimeoutValue.setter
    def TaskDependencyExecutingTimeoutValue(self, TaskDependencyExecutingTimeoutValue):
        self._TaskDependencyExecutingTimeoutValue = TaskDependencyExecutingTimeoutValue


    def _deserialize(self, params):
        self._PollingNullStrategy = params.get("PollingNullStrategy")
        self._TaskDependencyExecutingStrategies = params.get("TaskDependencyExecutingStrategies")
        self._TaskDependencyExecutingTimeoutValue = params.get("TaskDependencyExecutingTimeoutValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyTaskBrief(AbstractModel):
    r"""Dependency Task Information - Value Reference Table:

    Value description table:
    | Current Task Cycle Type | Upstream Task Cycle Type | Configuration Mode | MainCyclicConfig Value | Time Dimension / Instance Scope        | SubordinateCyclicConfig Value     | offset Value                         |
    | ----------------------- | ------------------------ | ------------------ | ---------------------- | -------------------------------------- | --------------------------------- | ------------------------------------ |
    | HOUR_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | DAY_CYCLE               | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Latest Instance              | CURRENT_HOUR                      | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Previous Cycle               | PREVIOUS_HOUR_CYCLE               | None                                 |
    | HOUR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Friday              | PREVIOUS_FRIDAY                   | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Sunday              | PREVIOUS_WEEKEND                  | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | WEEK_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Previous Hour (-60,0]        | PREVIOUS_HOUR_LATER_OFFSET_MINUTE | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Previous Hour                | PREVIOUS_HOUR                     | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Current Hour                 | CURRENT_HOUR                      | None                                 |
    | YEAR_CYCLE              | WEEK_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | WEEK_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Current Hour                 | CURRENT_HOUR                      | None                                 |
    | HOUR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | ONEOFF_CYCLE             | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | MONTH_CYCLE             | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | ONEOFF_CYCLE            | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Recommended Policy | MINUTE                 | By Minute / Current Minute             | CURRENT_MINUTE                    | None                                 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Recommended Policy | MINUTE                 | By Minute / Previous Cycle             | PREVIOUS_MINUTE_CYCLE             | None                                 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | ONEOFF_CYCLE            | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Previous Day (-24 * 60,0]     | PREVIOUS_DAY_LATER_OFFSET_MINUTE  | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | WEEK_CYCLE              | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | YEAR_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | ONEOFF_CYCLE            | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | HOUR_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Previous Day (-24,0]          | PREVIOUS_DAY_LATER_OFFSET_HOUR    | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Previous Day [-24,0)          | PREVIOUS_DAY                      | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / All Months of Current Year  | ALL_MONTH_OF_YEAR                 | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / End of Previous Month       | PREVIOUS_END_OF_MONTH             | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Beginning of Previous Month | PREVIOUS_BEGIN_OF_MONTH           | None                                 |
    | ONEOFF_CYCLE            | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | DAY_CYCLE               | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | ONEOFF_CYCLE            | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | DAY_CYCLE               | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MINUTE_CYCLE            | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | WEEK_CYCLE              | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / End of Previous Month       | PREVIOUS_END_OF_MONTH             | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / All Days of Current Year      | ALL_DAY_OF_YEAR                   | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | HOUR_CYCLE              | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MONTH_CYCLE             | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | DAY_CYCLE               | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | DAY_CYCLE               | YEAR_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | ONEOFF_CYCLE            | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | ONEOFF_CYCLE            | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | CRONTAB_CYCLE           | CRONTAB_CYCLE            | Recommended Policy | CRONTAB                | None                                   | CURRENT                           | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID

        :type TaskId: str
        :param _MainCyclicConfig: Main dependency configuration. Valid values:

* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR
        :type MainCyclicConfig: str
        :param _SubordinateCyclicConfig: Configures secondary dependencies.  Valid values:
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE
        :type SubordinateCyclicConfig: str
        :param _Offset: Offset in Range/List Mode
        :type Offset: str
        :param _DependencyStrategy: Dependency Execution Policy
        :type DependencyStrategy: :class:`tencentcloud.wedata.v20250806.models.DependencyStrategyTask`
        """
        self._TaskId = None
        self._MainCyclicConfig = None
        self._SubordinateCyclicConfig = None
        self._Offset = None
        self._DependencyStrategy = None

    @property
    def TaskId(self):
        r"""Task ID

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MainCyclicConfig(self):
        r"""Main dependency configuration. Valid values:

* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR
        :rtype: str
        """
        return self._MainCyclicConfig

    @MainCyclicConfig.setter
    def MainCyclicConfig(self, MainCyclicConfig):
        self._MainCyclicConfig = MainCyclicConfig

    @property
    def SubordinateCyclicConfig(self):
        r"""Configures secondary dependencies.  Valid values:
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE
        :rtype: str
        """
        return self._SubordinateCyclicConfig

    @SubordinateCyclicConfig.setter
    def SubordinateCyclicConfig(self, SubordinateCyclicConfig):
        self._SubordinateCyclicConfig = SubordinateCyclicConfig

    @property
    def Offset(self):
        r"""Offset in Range/List Mode
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def DependencyStrategy(self):
        r"""Dependency Execution Policy
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyStrategyTask`
        """
        return self._DependencyStrategy

    @DependencyStrategy.setter
    def DependencyStrategy(self, DependencyStrategy):
        self._DependencyStrategy = DependencyStrategy


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._MainCyclicConfig = params.get("MainCyclicConfig")
        self._SubordinateCyclicConfig = params.get("SubordinateCyclicConfig")
        self._Offset = params.get("Offset")
        if params.get("DependencyStrategy") is not None:
            self._DependencyStrategy = DependencyStrategyTask()
            self._DependencyStrategy._deserialize(params.get("DependencyStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventListener(AbstractModel):
    r"""Event listener.

    """

    def __init__(self):
        r"""
        :param _EventName: Event name

        :type EventName: str
        :param _EventSubType: Event cycle. valid values: SECOND, MIN, HOUR, DAY.

        :type EventSubType: str
        :param _EventBroadcastType: Event BROADCAST type: SINGLE, BROADCAST.

        :type EventBroadcastType: str
        :param _PropertiesList: Extension Information


        :type PropertiesList: list of ParamInfo
        """
        self._EventName = None
        self._EventSubType = None
        self._EventBroadcastType = None
        self._PropertiesList = None

    @property
    def EventName(self):
        r"""Event name

        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventSubType(self):
        r"""Event cycle. valid values: SECOND, MIN, HOUR, DAY.

        :rtype: str
        """
        return self._EventSubType

    @EventSubType.setter
    def EventSubType(self, EventSubType):
        self._EventSubType = EventSubType

    @property
    def EventBroadcastType(self):
        r"""Event BROADCAST type: SINGLE, BROADCAST.

        :rtype: str
        """
        return self._EventBroadcastType

    @EventBroadcastType.setter
    def EventBroadcastType(self, EventBroadcastType):
        self._EventBroadcastType = EventBroadcastType

    @property
    def PropertiesList(self):
        r"""Extension Information


        :rtype: list of ParamInfo
        """
        return self._PropertiesList

    @PropertiesList.setter
    def PropertiesList(self, PropertiesList):
        self._PropertiesList = PropertiesList


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._EventSubType = params.get("EventSubType")
        self._EventBroadcastType = params.get("EventBroadcastType")
        if params.get("PropertiesList") is not None:
            self._PropertiesList = []
            for item in params.get("PropertiesList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._PropertiesList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmMessageRequest(AbstractModel):
    r"""GetAlarmMessage request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _AlarmMessageId: Alarm message Id.
        :type AlarmMessageId: str
        :param _TimeZone: Specifies the time zone of the return date. default UTC+8.
        :type TimeZone: str
        """
        self._ProjectId = None
        self._AlarmMessageId = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmMessageId(self):
        r"""Alarm message Id.
        :rtype: str
        """
        return self._AlarmMessageId

    @AlarmMessageId.setter
    def AlarmMessageId(self, AlarmMessageId):
        self._AlarmMessageId = AlarmMessageId

    @property
    def TimeZone(self):
        r"""Specifies the time zone of the return date. default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmMessageId = params.get("AlarmMessageId")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmMessageResponse(AbstractModel):
    r"""GetAlarmMessage response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Alarm information.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.AlarmMessage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Alarm information.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmMessage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AlarmMessage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetCodeFileRequest(AbstractModel):
    r"""GetCodeFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _CodeFileId: Code file ID. the parameter value comes from the CreateCodeFile API response.
        :type CodeFileId: str
        :param _IncludeContent: true: return file content and configuration. false: only return configuration message. default false.
        :type IncludeContent: bool
        """
        self._ProjectId = None
        self._CodeFileId = None
        self._IncludeContent = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""Code file ID. the parameter value comes from the CreateCodeFile API response.
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def IncludeContent(self):
        r"""true: return file content and configuration. false: only return configuration message. default false.
        :rtype: bool
        """
        return self._IncludeContent

    @IncludeContent.setter
    def IncludeContent(self, IncludeContent):
        self._IncludeContent = IncludeContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        self._IncludeContent = params.get("IncludeContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCodeFileResponse(AbstractModel):
    r"""GetCodeFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the code file detail.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the code file detail.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsAlarmRuleRequest(AbstractModel):
    r"""GetOpsAlarmRule request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AlarmRuleId: Specifies the unique id of the Alarm rule.
        :type AlarmRuleId: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""Specifies the unique id of the Alarm rule.
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsAlarmRuleResponse(AbstractModel):
    r"""GetOpsAlarmRule response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the Alarm rule details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the Alarm rule details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AlarmRuleData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsAsyncJobRequest(AbstractModel):
    r"""GetOpsAsyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AsyncId: Asynchronous operation id.
        :type AsyncId: str
        """
        self._ProjectId = None
        self._AsyncId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AsyncId(self):
        r"""Asynchronous operation id.
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AsyncId = params.get("AsyncId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsAsyncJobResponse(AbstractModel):
    r"""GetOpsAsyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Asynchronous operation result.

        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncJobDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Asynchronous operation result.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncJobDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncJobDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsTaskCodeRequest(AbstractModel):
    r"""GetOpsTaskCode request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsTaskCodeResponse(AbstractModel):
    r"""GetOpsTaskCode response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Retrieves the task code result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskCode`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Retrieves the task code result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskCode`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskCode()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsTaskRequest(AbstractModel):
    r"""GetOpsTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID		
        :type TaskId: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        """
        self._TaskId = None
        self._ProjectId = None

    @property
    def TaskId(self):
        r"""Task ID		
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsTaskResponse(AbstractModel):
    r"""GetOpsTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetOpsWorkflowRequest(AbstractModel):
    r"""GetOpsWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _WorkflowId: Workflow Id, can be obtained through the ListOpsWorkflows api.
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""Workflow Id, can be obtained through the ListOpsWorkflows api.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpsWorkflowResponse(AbstractModel):
    r"""GetOpsWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Workflow scheduling details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflowDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Workflow scheduling details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflowDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsWorkflowDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetResourceFileRequest(AbstractModel):
    r"""GetResourceFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ResourceId: Resource file ID. obtain through the API ListResourceFiles.
        :type ResourceId: str
        """
        self._ProjectId = None
        self._ResourceId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""Resource file ID. obtain through the API ListResourceFiles.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourceFileResponse(AbstractModel):
    r"""GetResourceFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Describes the resource file details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFile`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Describes the resource file details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetSQLScriptRequest(AbstractModel):
    r"""GetSQLScript request structure.

    """

    def __init__(self):
        r"""
        :param _ScriptId: Script Id.
        :type ScriptId: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        """
        self._ScriptId = None
        self._ProjectId = None

    @property
    def ScriptId(self):
        r"""Script Id.
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSQLScriptResponse(AbstractModel):
    r"""GetSQLScript response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Script details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Script details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskCodeRequest(AbstractModel):
    r"""GetTaskCode request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: The project id.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""The project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskCodeResponse(AbstractModel):
    r"""GetTaskCode response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Retrieves the task code result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskCodeResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Retrieves the task code result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskCodeResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskCodeResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskInstanceLogRequest(AbstractModel):
    r"""GetTaskInstanceLog request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: **Project ID**. specifies the project ID.
        :type ProjectId: str
        :param _InstanceKey: **Instance unique id**.
        :type InstanceKey: str
        :param _LifeRoundNum: **Instance Lifecycle Number** - Identifies a specific execution of an instance.
For example: the first run of a cyclic instance has a lifecycle number of 0. If the user reruns that instance later, the second execution will have a lifecycle number of 1;
By default, the latest execution is used.
        :type LifeRoundNum: int
        :param _LogLevel: **Log level** default All - Info - Debug - Warn - Error - All.
        :type LogLevel: str
        :param _NextCursor: **Used when performing paginated log queries; has no specific business meaning.**

For the first query, the value is null.

For subsequent queries, use the value of the NextCursor field returned from the previous query.
        :type NextCursor: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._LifeRoundNum = None
        self._LogLevel = None
        self._NextCursor = None

    @property
    def ProjectId(self):
        r"""**Project ID**. specifies the project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**Instance unique id**.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def LifeRoundNum(self):
        r"""**Instance Lifecycle Number** - Identifies a specific execution of an instance.
For example: the first run of a cyclic instance has a lifecycle number of 0. If the user reruns that instance later, the second execution will have a lifecycle number of 1;
By default, the latest execution is used.
        :rtype: int
        """
        return self._LifeRoundNum

    @LifeRoundNum.setter
    def LifeRoundNum(self, LifeRoundNum):
        self._LifeRoundNum = LifeRoundNum

    @property
    def LogLevel(self):
        r"""**Log level** default All - Info - Debug - Warn - Error - All.
        :rtype: str
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def NextCursor(self):
        r"""**Used when performing paginated log queries; has no specific business meaning.**

For the first query, the value is null.

For subsequent queries, use the value of the NextCursor field returned from the previous query.
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._LifeRoundNum = params.get("LifeRoundNum")
        self._LogLevel = params.get("LogLevel")
        self._NextCursor = params.get("NextCursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskInstanceLogResponse(AbstractModel):
    r"""GetTaskInstanceLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Details of a scheduled instance.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.InstanceLog`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Details of a scheduled instance.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.InstanceLog`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = InstanceLog()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskInstanceRequest(AbstractModel):
    r"""GetTaskInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _InstanceKey: Instance unique id, can be obtained through ListInstances.
        :type InstanceKey: str
        :param _TimeZone: **Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :type TimeZone: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""Instance unique id, can be obtained through ListInstances.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskInstanceResponse(AbstractModel):
    r"""GetTaskInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Details of an instance.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Details of an instance.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstanceDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskRequest(AbstractModel):
    r"""GetTask request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._ProjectId = None
        self._TaskId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskResponse(AbstractModel):
    r"""GetTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetTaskVersionRequest(AbstractModel):
    r"""GetTaskVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _VersionId: Submit version ID. If not specified, the latest submit version will be used by default.
        :type VersionId: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._VersionId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VersionId(self):
        r"""Submit version ID. If not specified, the latest submit version will be used by default.
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskVersionResponse(AbstractModel):
    r"""GetTaskVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Version detail.

        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskVersionDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Version detail.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskVersionDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskVersionDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetWorkflowRequest(AbstractModel):
    r"""GetWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _WorkflowId: Workflow ID. Obtained through the  ListWorkflows API.
        :type WorkflowId: str
        """
        self._ProjectId = None
        self._WorkflowId = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""Workflow ID. Obtained through the  ListWorkflows API.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWorkflowResponse(AbstractModel):
    r"""GetWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Describes workflow details.

        :type Data: :class:`tencentcloud.wedata.v20250806.models.WorkflowDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Describes workflow details.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = WorkflowDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class InTaskParameter(AbstractModel):
    r"""Parameter passing - reference parameter.

    """

    def __init__(self):
        r"""
        :param _ParamKey: Parameter name.

        :type ParamKey: str
        :param _ParamDesc: Parameter Description: The format is ProjectIdentifier.TaskName.ParameterName
Example: project_wedata_1.sh_250820_104107.pp_out
        :type ParamDesc: str
        :param _FromTaskId: Parent Task ID

        :type FromTaskId: str
        :param _FromParamKey: Parent task parameter key.

        :type FromParamKey: str
        """
        self._ParamKey = None
        self._ParamDesc = None
        self._FromTaskId = None
        self._FromParamKey = None

    @property
    def ParamKey(self):
        r"""Parameter name.

        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamDesc(self):
        r"""Parameter Description: The format is ProjectIdentifier.TaskName.ParameterName
Example: project_wedata_1.sh_250820_104107.pp_out
        :rtype: str
        """
        return self._ParamDesc

    @ParamDesc.setter
    def ParamDesc(self, ParamDesc):
        self._ParamDesc = ParamDesc

    @property
    def FromTaskId(self):
        r"""Parent Task ID

        :rtype: str
        """
        return self._FromTaskId

    @FromTaskId.setter
    def FromTaskId(self, FromTaskId):
        self._FromTaskId = FromTaskId

    @property
    def FromParamKey(self):
        r"""Parent task parameter key.

        :rtype: str
        """
        return self._FromParamKey

    @FromParamKey.setter
    def FromParamKey(self, FromParamKey):
        self._FromParamKey = FromParamKey


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamDesc = params.get("ParamDesc")
        self._FromTaskId = params.get("FromTaskId")
        self._FromParamKey = params.get("FromParamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExecution(AbstractModel):
    r"""Describes the details of an instance.

    """

    def __init__(self):
        r"""
        :param _InstanceKey: Instance unique identifier.

        :type InstanceKey: str
        :param _LifeRoundNum: **Instance lifecycle number, identifies one-time execution of the instance.**.

For example, the first run of a periodic instance is numbered 0. if the user reruns the instance subsequently, the second execution is numbered 1.

        :type LifeRoundNum: int
        :param _InstanceState: **Instance status**.
-WAIT_EVENT: specifies the wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
- RUNNING: indicates the instance is RUNNING.
- SKIP_RUNNING: SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
- EXPIRED: failed.
-COMPLETED: success.

        :type InstanceState: str
        :param _RunType: **Trigger type for instance running**.

-RERUN indicates a rerun.
-ADDITION indicates supplementary recording.
-PERIODIC indicates a period.
-APERIODIC indicates non-periodic.
-RERUN_SKIP_RUN indicates rerun - empty run.
-ADDITION_SKIP_RUN indicates a supplementary empty run.
-PERIODIC_SKIP_RUN indicates cycle - empty run.
-APERIODIC_SKIP_RUN indicates non-periodic empty run.
-MANUAL_TRIGGER indicates manual triggering.
-RERUN_MANUAL_TRIGGER indicates manual triggering - rerun.
        :type RunType: str
        :param _Tries: Specifies the number of retry attempts on failure.

        :type Tries: int
        :param _ExecutionPhaseList: **Specifies the lifecycle list for instance execution.**.

        :type ExecutionPhaseList: list of InstanceExecutionPhase
        :param _CostTime: Time spent, in milliseconds.

        :type CostTime: int
        """
        self._InstanceKey = None
        self._LifeRoundNum = None
        self._InstanceState = None
        self._RunType = None
        self._Tries = None
        self._ExecutionPhaseList = None
        self._CostTime = None

    @property
    def InstanceKey(self):
        r"""Instance unique identifier.

        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def LifeRoundNum(self):
        r"""**Instance lifecycle number, identifies one-time execution of the instance.**.

For example, the first run of a periodic instance is numbered 0. if the user reruns the instance subsequently, the second execution is numbered 1.

        :rtype: int
        """
        return self._LifeRoundNum

    @LifeRoundNum.setter
    def LifeRoundNum(self, LifeRoundNum):
        self._LifeRoundNum = LifeRoundNum

    @property
    def InstanceState(self):
        r"""**Instance status**.
-WAIT_EVENT: specifies the wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
- RUNNING: indicates the instance is RUNNING.
- SKIP_RUNNING: SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
- EXPIRED: failed.
-COMPLETED: success.

        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def RunType(self):
        r"""**Trigger type for instance running**.

-RERUN indicates a rerun.
-ADDITION indicates supplementary recording.
-PERIODIC indicates a period.
-APERIODIC indicates non-periodic.
-RERUN_SKIP_RUN indicates rerun - empty run.
-ADDITION_SKIP_RUN indicates a supplementary empty run.
-PERIODIC_SKIP_RUN indicates cycle - empty run.
-APERIODIC_SKIP_RUN indicates non-periodic empty run.
-MANUAL_TRIGGER indicates manual triggering.
-RERUN_MANUAL_TRIGGER indicates manual triggering - rerun.
        :rtype: str
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def Tries(self):
        r"""Specifies the number of retry attempts on failure.

        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def ExecutionPhaseList(self):
        r"""**Specifies the lifecycle list for instance execution.**.

        :rtype: list of InstanceExecutionPhase
        """
        return self._ExecutionPhaseList

    @ExecutionPhaseList.setter
    def ExecutionPhaseList(self, ExecutionPhaseList):
        self._ExecutionPhaseList = ExecutionPhaseList

    @property
    def CostTime(self):
        r"""Time spent, in milliseconds.

        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._LifeRoundNum = params.get("LifeRoundNum")
        self._InstanceState = params.get("InstanceState")
        self._RunType = params.get("RunType")
        self._Tries = params.get("Tries")
        if params.get("ExecutionPhaseList") is not None:
            self._ExecutionPhaseList = []
            for item in params.get("ExecutionPhaseList"):
                obj = InstanceExecutionPhase()
                obj._deserialize(item)
                self._ExecutionPhaseList.append(obj)
        self._CostTime = params.get("CostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExecutionPhase(AbstractModel):
    r"""Describes the details of each stage in instance execution.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the state.
        :type StartTime: str
        :param _DetailState: **Instance lifecycle phase status**.

-WAIT_UPSTREAM indicates the wait event/upstream status.
-WAIT_RUN indicates the waiting for running status.
-RUNNING indicates the running state.
-COMPLETE indicates the final state of completion.
- FAILED indicates the final state - retry on failure.
-EXPIRED indicates the final state - failure.
-SKIP_RUNNING indicates the branch skipped by the upstream branch node in the final state.
-HISTORY indicates compatibility with historical instances before 2024-03-30. no need to pay attention to this enum afterward.
        :type DetailState: str
        :param _EndTime: End time of the state.
        :type EndTime: str
        """
        self._StartTime = None
        self._DetailState = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""Start time of the state.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def DetailState(self):
        r"""**Instance lifecycle phase status**.

-WAIT_UPSTREAM indicates the wait event/upstream status.
-WAIT_RUN indicates the waiting for running status.
-RUNNING indicates the running state.
-COMPLETE indicates the final state of completion.
- FAILED indicates the final state - retry on failure.
-EXPIRED indicates the final state - failure.
-SKIP_RUNNING indicates the branch skipped by the upstream branch node in the final state.
-HISTORY indicates compatibility with historical instances before 2024-03-30. no need to pay attention to this enum afterward.
        :rtype: str
        """
        return self._DetailState

    @DetailState.setter
    def DetailState(self, DetailState):
        self._DetailState = DetailState

    @property
    def EndTime(self):
        r"""End time of the state.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._DetailState = params.get("DetailState")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    r"""Instance log content.

    """

    def __init__(self):
        r"""
        :param _InstanceKey: Instance unique id.

        :type InstanceKey: str
        :param _ProjectId: Project ID.


        :type ProjectId: str
        :param _CodeContent: Specifies the code content to run.

        :type CodeContent: str
        :param _LogInfo: log information

        :type LogInfo: str
        :param _NextCursor: Used for paginated log queries; has no specific business meaning.

For the first query, set the value to null.

For subsequent queries, use the NextCursor value returned from the previous query.
        :type NextCursor: str
        """
        self._InstanceKey = None
        self._ProjectId = None
        self._CodeContent = None
        self._LogInfo = None
        self._NextCursor = None

    @property
    def InstanceKey(self):
        r"""Instance unique id.

        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ProjectId(self):
        r"""Project ID.


        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeContent(self):
        r"""Specifies the code content to run.

        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def LogInfo(self):
        r"""log information

        :rtype: str
        """
        return self._LogInfo

    @LogInfo.setter
    def LogInfo(self, LogInfo):
        self._LogInfo = LogInfo

    @property
    def NextCursor(self):
        r"""Used for paginated log queries; has no specific business meaning.

For the first query, set the value to null.

For subsequent queries, use the NextCursor value returned from the previous query.
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ProjectId = params.get("ProjectId")
        self._CodeContent = params.get("CodeContent")
        self._LogInfo = params.get("LogInfo")
        self._NextCursor = params.get("NextCursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobDto(AbstractModel):
    r"""Data exploration JOB.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID of the data exploration.

        :type JobId: str
        :param _JobName: Task name.
        :type JobName: str
        :param _JobType: Task type
        :type JobType: str
        :param _ScriptId: Script ID
        :type ScriptId: str
        :param _JobExecutionList: Subtask List
        :type JobExecutionList: list of JobExecutionDto
        :param _ScriptContent: Specifies the script content.
        :type ScriptContent: str
        :param _Status: State of a task.
        :type Status: str
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _EndTime: End time.

        :type EndTime: str
        :param _OwnerUin: Root account UIN.
        :type OwnerUin: str
        :param _UserUin: Account UIN.
        :type UserUin: str
        :param _TimeCost: Duration. specifies the time taken.

        :type TimeCost: int
        :param _ScriptContentTruncate: Specifies whether the script content is truncated.

        :type ScriptContentTruncate: bool
        """
        self._JobId = None
        self._JobName = None
        self._JobType = None
        self._ScriptId = None
        self._JobExecutionList = None
        self._ScriptContent = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._EndTime = None
        self._OwnerUin = None
        self._UserUin = None
        self._TimeCost = None
        self._ScriptContentTruncate = None

    @property
    def JobId(self):
        r"""Task ID of the data exploration.

        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        r"""Task name.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobType(self):
        r"""Task type
        :rtype: str
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def ScriptId(self):
        r"""Script ID
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def JobExecutionList(self):
        r"""Subtask List
        :rtype: list of JobExecutionDto
        """
        return self._JobExecutionList

    @JobExecutionList.setter
    def JobExecutionList(self, JobExecutionList):
        self._JobExecutionList = JobExecutionList

    @property
    def ScriptContent(self):
        r"""Specifies the script content.
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Status(self):
        r"""State of a task.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""Task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def EndTime(self):
        r"""End time.

        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OwnerUin(self):
        r"""Root account UIN.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def UserUin(self):
        r"""Account UIN.
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def TimeCost(self):
        r"""Duration. specifies the time taken.

        :rtype: int
        """
        return self._TimeCost

    @TimeCost.setter
    def TimeCost(self, TimeCost):
        self._TimeCost = TimeCost

    @property
    def ScriptContentTruncate(self):
        r"""Specifies whether the script content is truncated.

        :rtype: bool
        """
        return self._ScriptContentTruncate

    @ScriptContentTruncate.setter
    def ScriptContentTruncate(self, ScriptContentTruncate):
        self._ScriptContentTruncate = ScriptContentTruncate


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobType = params.get("JobType")
        self._ScriptId = params.get("ScriptId")
        if params.get("JobExecutionList") is not None:
            self._JobExecutionList = []
            for item in params.get("JobExecutionList"):
                obj = JobExecutionDto()
                obj._deserialize(item)
                self._JobExecutionList.append(obj)
        self._ScriptContent = params.get("ScriptContent")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._EndTime = params.get("EndTime")
        self._OwnerUin = params.get("OwnerUin")
        self._UserUin = params.get("UserUin")
        self._TimeCost = params.get("TimeCost")
        self._ScriptContentTruncate = params.get("ScriptContentTruncate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobExecutionDto(AbstractModel):
    r"""Describes the subtask of a business submission JOB.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID of the data exploration.

        :type JobId: str
        :param _JobExecutionId: Query job ID.

        :type JobExecutionId: str
        :param _JobExecutionName: Specifies the subquery name.

        :type JobExecutionName: str
        :param _ScriptContent: Specifies the subquery sql content.

        :type ScriptContent: str
        :param _Status: Subquery status.

        :type Status: str
        :param _CreateTime: Creation time.

        :type CreateTime: str
        :param _ExecuteStageInfo: Execution phase.

        :type ExecuteStageInfo: str
        :param _LogFilePath: Log path

        :type LogFilePath: str
        :param _ResultFilePath: Result path for download.

        :type ResultFilePath: str
        :param _ResultPreviewFilePath: Preview result path.

        :type ResultPreviewFilePath: str
        :param _ResultTotalCount: Total number of lines in the task execution result.

        :type ResultTotalCount: int
        :param _UpdateTime: Update time.

        :type UpdateTime: str
        :param _EndTime: End time.


        :type EndTime: str
        :param _TimeCost: Duration. specifies the time taken.

        :type TimeCost: int
        :param _ContextScriptContent: SQL content in the context.

        :type ContextScriptContent: list of str
        :param _ResultPreviewCount: Specifies the preview row count for task execution results.

        :type ResultPreviewCount: int
        :param _ResultEffectCount: Specifies the number of affected rows in task execution.

        :type ResultEffectCount: int
        :param _CollectingTotalResult: Whether the full result is being collected: default false. true indicates the full result is being collected, for the frontend to determine whether to continue to poll.

        :type CollectingTotalResult: bool
        :param _ScriptContentTruncate: Specifies whether to truncate the script content.

        :type ScriptContentTruncate: bool
        """
        self._JobId = None
        self._JobExecutionId = None
        self._JobExecutionName = None
        self._ScriptContent = None
        self._Status = None
        self._CreateTime = None
        self._ExecuteStageInfo = None
        self._LogFilePath = None
        self._ResultFilePath = None
        self._ResultPreviewFilePath = None
        self._ResultTotalCount = None
        self._UpdateTime = None
        self._EndTime = None
        self._TimeCost = None
        self._ContextScriptContent = None
        self._ResultPreviewCount = None
        self._ResultEffectCount = None
        self._CollectingTotalResult = None
        self._ScriptContentTruncate = None

    @property
    def JobId(self):
        r"""Job ID of the data exploration.

        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobExecutionId(self):
        r"""Query job ID.

        :rtype: str
        """
        return self._JobExecutionId

    @JobExecutionId.setter
    def JobExecutionId(self, JobExecutionId):
        self._JobExecutionId = JobExecutionId

    @property
    def JobExecutionName(self):
        r"""Specifies the subquery name.

        :rtype: str
        """
        return self._JobExecutionName

    @JobExecutionName.setter
    def JobExecutionName(self, JobExecutionName):
        self._JobExecutionName = JobExecutionName

    @property
    def ScriptContent(self):
        r"""Specifies the subquery sql content.

        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Status(self):
        r"""Subquery status.

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""Creation time.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExecuteStageInfo(self):
        r"""Execution phase.

        :rtype: str
        """
        return self._ExecuteStageInfo

    @ExecuteStageInfo.setter
    def ExecuteStageInfo(self, ExecuteStageInfo):
        self._ExecuteStageInfo = ExecuteStageInfo

    @property
    def LogFilePath(self):
        r"""Log path

        :rtype: str
        """
        return self._LogFilePath

    @LogFilePath.setter
    def LogFilePath(self, LogFilePath):
        self._LogFilePath = LogFilePath

    @property
    def ResultFilePath(self):
        r"""Result path for download.

        :rtype: str
        """
        return self._ResultFilePath

    @ResultFilePath.setter
    def ResultFilePath(self, ResultFilePath):
        self._ResultFilePath = ResultFilePath

    @property
    def ResultPreviewFilePath(self):
        r"""Preview result path.

        :rtype: str
        """
        return self._ResultPreviewFilePath

    @ResultPreviewFilePath.setter
    def ResultPreviewFilePath(self, ResultPreviewFilePath):
        self._ResultPreviewFilePath = ResultPreviewFilePath

    @property
    def ResultTotalCount(self):
        r"""Total number of lines in the task execution result.

        :rtype: int
        """
        return self._ResultTotalCount

    @ResultTotalCount.setter
    def ResultTotalCount(self, ResultTotalCount):
        self._ResultTotalCount = ResultTotalCount

    @property
    def UpdateTime(self):
        r"""Update time.

        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def EndTime(self):
        r"""End time.


        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeCost(self):
        r"""Duration. specifies the time taken.

        :rtype: int
        """
        return self._TimeCost

    @TimeCost.setter
    def TimeCost(self, TimeCost):
        self._TimeCost = TimeCost

    @property
    def ContextScriptContent(self):
        r"""SQL content in the context.

        :rtype: list of str
        """
        return self._ContextScriptContent

    @ContextScriptContent.setter
    def ContextScriptContent(self, ContextScriptContent):
        self._ContextScriptContent = ContextScriptContent

    @property
    def ResultPreviewCount(self):
        r"""Specifies the preview row count for task execution results.

        :rtype: int
        """
        return self._ResultPreviewCount

    @ResultPreviewCount.setter
    def ResultPreviewCount(self, ResultPreviewCount):
        self._ResultPreviewCount = ResultPreviewCount

    @property
    def ResultEffectCount(self):
        r"""Specifies the number of affected rows in task execution.

        :rtype: int
        """
        return self._ResultEffectCount

    @ResultEffectCount.setter
    def ResultEffectCount(self, ResultEffectCount):
        self._ResultEffectCount = ResultEffectCount

    @property
    def CollectingTotalResult(self):
        r"""Whether the full result is being collected: default false. true indicates the full result is being collected, for the frontend to determine whether to continue to poll.

        :rtype: bool
        """
        return self._CollectingTotalResult

    @CollectingTotalResult.setter
    def CollectingTotalResult(self, CollectingTotalResult):
        self._CollectingTotalResult = CollectingTotalResult

    @property
    def ScriptContentTruncate(self):
        r"""Specifies whether to truncate the script content.

        :rtype: bool
        """
        return self._ScriptContentTruncate

    @ScriptContentTruncate.setter
    def ScriptContentTruncate(self, ScriptContentTruncate):
        self._ScriptContentTruncate = ScriptContentTruncate


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobExecutionId = params.get("JobExecutionId")
        self._JobExecutionName = params.get("JobExecutionName")
        self._ScriptContent = params.get("ScriptContent")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ExecuteStageInfo = params.get("ExecuteStageInfo")
        self._LogFilePath = params.get("LogFilePath")
        self._ResultFilePath = params.get("ResultFilePath")
        self._ResultPreviewFilePath = params.get("ResultPreviewFilePath")
        self._ResultTotalCount = params.get("ResultTotalCount")
        self._UpdateTime = params.get("UpdateTime")
        self._EndTime = params.get("EndTime")
        self._TimeCost = params.get("TimeCost")
        self._ContextScriptContent = params.get("ContextScriptContent")
        self._ResultPreviewCount = params.get("ResultPreviewCount")
        self._ResultEffectCount = params.get("ResultEffectCount")
        self._CollectingTotalResult = params.get("CollectingTotalResult")
        self._ScriptContentTruncate = params.get("ScriptContentTruncate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVMap(AbstractModel):
    r"""map

    """

    def __init__(self):
        r"""
        :param _K: k
        :type K: str
        :param _V: v
        :type V: str
        """
        self._K = None
        self._V = None

    @property
    def K(self):
        r"""k
        :rtype: str
        """
        return self._K

    @K.setter
    def K(self, K):
        self._K = K

    @property
    def V(self):
        r"""v
        :rtype: str
        """
        return self._V

    @V.setter
    def V(self, V):
        self._V = V


    def _deserialize(self, params):
        self._K = params.get("K")
        self._V = params.get("V")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    r"""Key-value pair

    """

    def __init__(self):
        r"""
        :param _K: Key name


        :type K: str
        :param _V: The value. do not pass SQL (the request will be deemed as an attack on the api). if needed, transcode the SQL with Base64 and decode it.

        :type V: str
        """
        self._K = None
        self._V = None

    @property
    def K(self):
        r"""Key name


        :rtype: str
        """
        return self._K

    @K.setter
    def K(self, K):
        self._K = K

    @property
    def V(self):
        r"""The value. do not pass SQL (the request will be deemed as an attack on the api). if needed, transcode the SQL with Base64 and decode it.

        :rtype: str
        """
        return self._V

    @V.setter
    def V(self, V):
        self._V = V


    def _deserialize(self, params):
        self._K = params.get("K")
        self._V = params.get("V")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillTaskInstancesAsyncRequest(AbstractModel):
    r"""KillTaskInstancesAsync request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _InstanceKeyList: Instance id list, can be obtained from ListInstances API.
        :type InstanceKeyList: list of str
        """
        self._ProjectId = None
        self._InstanceKeyList = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""Instance id list, can be obtained from ListInstances API.
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillTaskInstancesAsyncResponse(AbstractModel):
    r"""KillTaskInstancesAsync response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Async id of the batch termination operation. can be used in the GetAsyncJob API to query execution detail.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Async id of the batch termination operation. can be used in the GetAsyncJob API to query execution detail.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListAlarmMessages(AbstractModel):
    r"""Alarm information list.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _TotalPageNumber: Total pages
        :type TotalPageNumber: int
        :param _Items: Alarm information list.
        :type Items: list of AlarmMessage
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""Alarm information list.
        :rtype: list of AlarmMessage
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AlarmMessage()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlarmMessagesRequest(AbstractModel):
    r"""ListAlarmMessages request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _PageNumber: Page number for pagination, minimum value is 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of items displayed per page. maximum value: 100.
        :type PageSize: int
        :param _StartTime: Starting Alarm time. format: yyyy-MM-dd HH:MM:ss.
        :type StartTime: str
        :param _EndTime: Specifies the Alarm end time in the format yyyy-MM-dd HH:MM:ss.
        :type EndTime: str
        :param _AlarmLevel: Alarm level.
        :type AlarmLevel: int
        :param _AlarmRecipientId: Alert recipient Id.
        :type AlarmRecipientId: str
        :param _TimeZone: For incoming and returned filter time zone, default UTC+8.
        :type TimeZone: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._StartTime = None
        self._EndTime = None
        self._AlarmLevel = None
        self._AlarmRecipientId = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Page number for pagination, minimum value is 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of items displayed per page. maximum value: 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartTime(self):
        r"""Starting Alarm time. format: yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Specifies the Alarm end time in the format yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AlarmLevel(self):
        r"""Alarm level.
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRecipientId(self):
        r"""Alert recipient Id.
        :rtype: str
        """
        return self._AlarmRecipientId

    @AlarmRecipientId.setter
    def AlarmRecipientId(self, AlarmRecipientId):
        self._AlarmRecipientId = AlarmRecipientId

    @property
    def TimeZone(self):
        r"""For incoming and returned filter time zone, default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRecipientId = params.get("AlarmRecipientId")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlarmMessagesResponse(AbstractModel):
    r"""ListAlarmMessages response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Alarm information list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessages`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Alarm information list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmMessages`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListAlarmMessages()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListAlarmRulesResult(AbstractModel):
    r"""Query Alarm rule list.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number for pagination. current page number.
        :type PageNumber: int
        :param _PageSize: Specifies the number of items to display per page.
        :type PageSize: int
        :param _TotalPageNumber: Total number of pages.
        :type TotalPageNumber: int
        :param _TotalCount: Count of all Alarm rules.
        :type TotalCount: int
        :param _Items: Alert rule information list.
        :type Items: list of AlarmRuleData
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""Page number for pagination. current page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of items to display per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPageNumber(self):
        r"""Total number of pages.
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""Count of all Alarm rules.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Alert rule information list.
        :rtype: list of AlarmRuleData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AlarmRuleData()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCodeFolderContentsRequest(AbstractModel):
    r"""ListCodeFolderContents request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Parent folder path, such as /aaa/bbb/ccc. path header must include a slash. pass / for the root directory.
        :type ParentFolderPath: str
        :param _Keyword: Folder name or code file name.
        :type Keyword: str
        :param _OnlyFolderNode: Queries folder only.
        :type OnlyFolderNode: bool
        :param _OnlyUserSelfScript: Specifies whether to query only code script created by user themselves.
        :type OnlyUserSelfScript: bool
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._Keyword = None
        self._OnlyFolderNode = None
        self._OnlyUserSelfScript = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, such as /aaa/bbb/ccc. path header must include a slash. pass / for the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def Keyword(self):
        r"""Folder name or code file name.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def OnlyFolderNode(self):
        r"""Queries folder only.
        :rtype: bool
        """
        return self._OnlyFolderNode

    @OnlyFolderNode.setter
    def OnlyFolderNode(self, OnlyFolderNode):
        self._OnlyFolderNode = OnlyFolderNode

    @property
    def OnlyUserSelfScript(self):
        r"""Specifies whether to query only code script created by user themselves.
        :rtype: bool
        """
        return self._OnlyUserSelfScript

    @OnlyUserSelfScript.setter
    def OnlyUserSelfScript(self, OnlyUserSelfScript):
        self._OnlyUserSelfScript = OnlyUserSelfScript


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._Keyword = params.get("Keyword")
        self._OnlyFolderNode = params.get("OnlyFolderNode")
        self._OnlyUserSelfScript = params.get("OnlyUserSelfScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCodeFolderContentsResponse(AbstractModel):
    r"""ListCodeFolderContents response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result

        :type Data: list of CodeFolderNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result

        :rtype: list of CodeFolderNode
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CodeFolderNode()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListDataBackfillInstancesRequest(AbstractModel):
    r"""ListDataBackfillInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _DataBackfillPlanId: Backfill plan Id.
        :type DataBackfillPlanId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        """
        self._ProjectId = None
        self._DataBackfillPlanId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DataBackfillPlanId(self):
        r"""Backfill plan Id.
        :rtype: str
        """
        return self._DataBackfillPlanId

    @DataBackfillPlanId.setter
    def DataBackfillPlanId(self, DataBackfillPlanId):
        self._DataBackfillPlanId = DataBackfillPlanId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DataBackfillPlanId = params.get("DataBackfillPlanId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDataBackfillInstancesResponse(AbstractModel):
    r"""ListDataBackfillInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Data: All backfill  instances under one backfill  plan.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.BackfillInstanceCollection`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""All backfill  instances under one backfill  plan.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.BackfillInstanceCollection`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = BackfillInstanceCollection()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamOpsTasksRequest(AbstractModel):
    r"""ListDownstreamOpsTasks request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID		
        :type TaskId: str
        :param _ProjectId: Project ID.
		
        :type ProjectId: str
        :param _PageNumber: Page number
        :type PageNumber: str
        :param _PageSize: Pagination size.
        :type PageSize: str
        """
        self._TaskId = None
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TaskId(self):
        r"""Task ID		
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ProjectId(self):
        r"""Project ID.
		
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamOpsTasksResponse(AbstractModel):
    r"""ListDownstreamOpsTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Downstream dependency description.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ChildDependencyConfigPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Downstream dependency description.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ChildDependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ChildDependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamTaskInstancesRequest(AbstractModel):
    r"""ListDownstreamTaskInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _InstanceKey: **Instance unique id**.
        :type InstanceKey: str
        :param _TimeZone: **Time zone** timeZone, default UTC+8.
        :type TimeZone: str
        :param _PageNumber: **Page number, int** used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of items to display per page. default: 10. value range: 1-100.
        :type PageSize: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**Instance unique id**.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**Time zone** timeZone, default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageNumber(self):
        r"""**Page number, int** used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of items to display per page. default: 10. value range: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamTaskInstancesResponse(AbstractModel):
    r"""ListDownstreamTaskInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Direct downstream instance list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Direct downstream instance list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDownstreamTasksRequest(AbstractModel):
    r"""ListDownstreamTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _PageNumber: Page number
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDownstreamTasksResponse(AbstractModel):
    r"""ListDownstreamTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Describes the downstream dependency details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Describes the downstream dependency details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsAlarmRulesRequest(AbstractModel):
    r"""ListOpsAlarmRules request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageNumber: Page number for pagination. defaults to 1.
        :type PageNumber: int
        :param _PageSize: Number of items to display per page, defaults to 20, minimum value 1, maximum value 200.
        :type PageSize: int
        :param _MonitorObjectType: Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :type MonitorObjectType: int
        :param _TaskId: Based on task id, queries Alarm rules.
        :type TaskId: str
        :param _AlarmType: Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :type AlarmType: str
        :param _AlarmLevel: Queries Alarm rules configured with corresponding Alarm levels.
Valid values: 1. ordinary, 2. important, 3. critical.
        :type AlarmLevel: int
        :param _AlarmRecipientId: Query the alarm rules associated with the configured alarm recipients.
        :type AlarmRecipientId: str
        :param _Keyword: Queries the corresponding Alarm rule based on Alarm rule id or rule name.
        :type Keyword: str
        :param _CreateUserUin: Specifies the creator filter for Alarm rule creation.
        :type CreateUserUin: str
        :param _CreateTimeFrom: Start time of the Alarm rule create time range, in the format of 2025-08-17 00:00:00.
        :type CreateTimeFrom: str
        :param _CreateTimeTo: End time of the Alarm rule creation time range, in the format of "2025-08-26 23:59:59".

        :type CreateTimeTo: str
        :param _UpdateTimeFrom: Filters Alarm rules by last update time, in the format of "2025-08-26 00:00:00".

        :type UpdateTimeFrom: str
        :param _UpdateTimeTo: Filters Alarm rules by last update time in the format of "2025-08-26 23:59:59".

        :type UpdateTimeTo: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._MonitorObjectType = None
        self._TaskId = None
        self._AlarmType = None
        self._AlarmLevel = None
        self._AlarmRecipientId = None
        self._Keyword = None
        self._CreateUserUin = None
        self._CreateTimeFrom = None
        self._CreateTimeTo = None
        self._UpdateTimeFrom = None
        self._UpdateTimeTo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Page number for pagination. defaults to 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of items to display per page, defaults to 20, minimum value 1, maximum value 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MonitorObjectType(self):
        r"""Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def TaskId(self):
        r"""Based on task id, queries Alarm rules.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AlarmType(self):
        r"""Alarm Rule Monitoring Types:

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

reconciliationFailure: Alarm when an offline reconciliation task fails

reconciliationOvertime: Alarm when an offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :rtype: str
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmLevel(self):
        r"""Queries Alarm rules configured with corresponding Alarm levels.
Valid values: 1. ordinary, 2. important, 3. critical.
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmRecipientId(self):
        r"""Query the alarm rules associated with the configured alarm recipients.
        :rtype: str
        """
        return self._AlarmRecipientId

    @AlarmRecipientId.setter
    def AlarmRecipientId(self, AlarmRecipientId):
        self._AlarmRecipientId = AlarmRecipientId

    @property
    def Keyword(self):
        r"""Queries the corresponding Alarm rule based on Alarm rule id or rule name.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def CreateUserUin(self):
        r"""Specifies the creator filter for Alarm rule creation.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateTimeFrom(self):
        r"""Start time of the Alarm rule create time range, in the format of 2025-08-17 00:00:00.
        :rtype: str
        """
        return self._CreateTimeFrom

    @CreateTimeFrom.setter
    def CreateTimeFrom(self, CreateTimeFrom):
        self._CreateTimeFrom = CreateTimeFrom

    @property
    def CreateTimeTo(self):
        r"""End time of the Alarm rule creation time range, in the format of "2025-08-26 23:59:59".

        :rtype: str
        """
        return self._CreateTimeTo

    @CreateTimeTo.setter
    def CreateTimeTo(self, CreateTimeTo):
        self._CreateTimeTo = CreateTimeTo

    @property
    def UpdateTimeFrom(self):
        r"""Filters Alarm rules by last update time, in the format of "2025-08-26 00:00:00".

        :rtype: str
        """
        return self._UpdateTimeFrom

    @UpdateTimeFrom.setter
    def UpdateTimeFrom(self, UpdateTimeFrom):
        self._UpdateTimeFrom = UpdateTimeFrom

    @property
    def UpdateTimeTo(self):
        r"""Filters Alarm rules by last update time in the format of "2025-08-26 23:59:59".

        :rtype: str
        """
        return self._UpdateTimeTo

    @UpdateTimeTo.setter
    def UpdateTimeTo(self, UpdateTimeTo):
        self._UpdateTimeTo = UpdateTimeTo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._TaskId = params.get("TaskId")
        self._AlarmType = params.get("AlarmType")
        self._AlarmLevel = params.get("AlarmLevel")
        self._AlarmRecipientId = params.get("AlarmRecipientId")
        self._Keyword = params.get("Keyword")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateTimeFrom = params.get("CreateTimeFrom")
        self._CreateTimeTo = params.get("CreateTimeTo")
        self._UpdateTimeFrom = params.get("UpdateTimeFrom")
        self._UpdateTimeTo = params.get("UpdateTimeTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsAlarmRulesResponse(AbstractModel):
    r"""ListOpsAlarmRules response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Alarm information response.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListAlarmRulesResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Alarm information response.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListAlarmRulesResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListAlarmRulesResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsTasksPage(AbstractModel):
    r"""Task list pagination.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results

        :type TotalCount: int
        :param _TotalPageNumber: Total pages

        :type TotalPageNumber: int
        :param _Items: Record list	
	

        :type Items: list of TaskOpsInfo
        :param _PageNumber: Page number.

        :type PageNumber: int
        :param _PageSize: Pagination size.

        :type PageSize: int
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TotalCount(self):
        r"""Total number of results

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""Record list	
	

        :rtype: list of TaskOpsInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""Page number.

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskOpsInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsTasksRequest(AbstractModel):
    r"""ListOpsTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
		
        :type ProjectId: str
        :param _PageSize: Pagination size.
        :type PageSize: str
        :param _PageNumber: Page number
        :type PageNumber: str
        :param _TaskTypeId: Task type Id. 
-20: common data sync.
 - 25:ETLTaskType
 - 26:ETLTaskType
 - 30:python
 - 31:pyspark
 - 34:HiveSQLTaskType
 - 35:shell
 - 36:SparkSQLTaskType
 - 21:JDBCSQLTaskType
 - 32:DLCTaskType
 - 33:ImpalaTaskType
 - 40:CDWTaskType
 - 41:kettle
 - 46:DLCSparkTaskType
-47: TiOne machine learning.
 - 48:TrinoTaskType
 - 50:DLCPyspark39:spark
 - 92:mr
-38: shell script.
-70: hivesql script.
-1000: common custom business.
        :type TaskTypeId: str
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _OwnerUin: Owner id.
        :type OwnerUin: str
        :param _FolderId: Folder ID
        :type FolderId: str
        :param _SourceServiceId: Data source ID.
        :type SourceServiceId: str
        :param _TargetServiceId: Target data source id.
        :type TargetServiceId: str
        :param _ExecutorGroupId: Executor Group ID
        :type ExecutorGroupId: str
        :param _CycleType: Task Cycle Type:

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _Status: Task Status

-Y: Running

-F: Stopped

-O: Frozen

-T: Stopping

-INVALID: Invalid
        :type Status: str
        :param _TimeZone: Time zone. defaults to UTC+8.
        :type TimeZone: str
        """
        self._ProjectId = None
        self._PageSize = None
        self._PageNumber = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._OwnerUin = None
        self._FolderId = None
        self._SourceServiceId = None
        self._TargetServiceId = None
        self._ExecutorGroupId = None
        self._CycleType = None
        self._Status = None
        self._TimeZone = None

    @property
    def ProjectId(self):
        r"""Project ID.
		
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TaskTypeId(self):
        r"""Task type Id. 
-20: common data sync.
 - 25:ETLTaskType
 - 26:ETLTaskType
 - 30:python
 - 31:pyspark
 - 34:HiveSQLTaskType
 - 35:shell
 - 36:SparkSQLTaskType
 - 21:JDBCSQLTaskType
 - 32:DLCTaskType
 - 33:ImpalaTaskType
 - 40:CDWTaskType
 - 41:kettle
 - 46:DLCSparkTaskType
-47: TiOne machine learning.
 - 48:TrinoTaskType
 - 50:DLCPyspark39:spark
 - 92:mr
-38: shell script.
-70: hivesql script.
-1000: common custom business.
        :rtype: str
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""Owner id.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def SourceServiceId(self):
        r"""Data source ID.
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def TargetServiceId(self):
        r"""Target data source id.
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def ExecutorGroupId(self):
        r"""Executor Group ID
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def CycleType(self):
        r"""Task Cycle Type:

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def Status(self):
        r"""Task Status

-Y: Running

-F: Stopped

-O: Frozen

-T: Stopping

-INVALID: Invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TimeZone(self):
        r"""Time zone. defaults to UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._FolderId = params.get("FolderId")
        self._SourceServiceId = params.get("SourceServiceId")
        self._TargetServiceId = params.get("TargetServiceId")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._CycleType = params.get("CycleType")
        self._Status = params.get("Status")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsTasksResponse(AbstractModel):
    r"""ListOpsTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListOpsTasksPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListOpsTasksPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOpsWorkflowsRequest(AbstractModel):
    r"""ListOpsWorkflows request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _PageNumber: Page number
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        :param _FolderId: Folder ID
        :type FolderId: str
        :param _Status: Workflow Status Filter

* ALL_RUNNING: All workflows are running (scheduled)

* ALL_FREEZED: All workflows are paused

* ALL_STOPPED: All workflows are offline

* PART_RUNNING: Some workflows are running (partially scheduled)

* ALL_NO_RUNNING: No workflows are running (unscheduled)

* ALL_INVALID: All workflows are invalid
        :type Status: str
        :param _OwnerUin: Owner ID
        :type OwnerUin: str
        :param _WorkflowType: Workflow type filter criteria. supported values: Cycle or Manual. default: Cycle.
        :type WorkflowType: str
        :param _KeyWord: Workflow keyword-based filtering supports fuzzy matching of workflow Id/name.
        :type KeyWord: str
        :param _SortItem: Sort item. Options: CreateTime, TaskCount.
        :type SortItem: str
        :param _SortType: Sorting method, DESC or ASC, uppercase.
        :type SortType: str
        :param _CreateUserUin: CreatorId. specifies the id of the creator.
        :type CreateUserUin: str
        :param _ModifyTime: Update time. format: yyyy-MM-dd HH:MM:ss.
        :type ModifyTime: str
        :param _CreateTime: Creation time. format: yyyy-MM-dd HH:MM:ss.
        :type CreateTime: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._FolderId = None
        self._Status = None
        self._OwnerUin = None
        self._WorkflowType = None
        self._KeyWord = None
        self._SortItem = None
        self._SortType = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def Status(self):
        r"""Workflow Status Filter

* ALL_RUNNING: All workflows are running (scheduled)

* ALL_FREEZED: All workflows are paused

* ALL_STOPPED: All workflows are offline

* PART_RUNNING: Some workflows are running (partially scheduled)

* ALL_NO_RUNNING: No workflows are running (unscheduled)

* ALL_INVALID: All workflows are invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        r"""Owner ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowType(self):
        r"""Workflow type filter criteria. supported values: Cycle or Manual. default: Cycle.
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def KeyWord(self):
        r"""Workflow keyword-based filtering supports fuzzy matching of workflow Id/name.
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def SortItem(self):
        r"""Sort item. Options: CreateTime, TaskCount.
        :rtype: str
        """
        return self._SortItem

    @SortItem.setter
    def SortItem(self, SortItem):
        self._SortItem = SortItem

    @property
    def SortType(self):
        r"""Sorting method, DESC or ASC, uppercase.
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def CreateUserUin(self):
        r"""CreatorId. specifies the id of the creator.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""Update time. format: yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""Creation time. format: yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._FolderId = params.get("FolderId")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowType = params.get("WorkflowType")
        self._KeyWord = params.get("KeyWord")
        self._SortItem = params.get("SortItem")
        self._SortType = params.get("SortType")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOpsWorkflowsResponse(AbstractModel):
    r"""ListOpsWorkflows response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Workflow list
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflows`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Workflow list
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsWorkflows`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsWorkflows()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListResourceFilesRequest(AbstractModel):
    r"""ListResourceFiles request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageNumber: Data page number, equal to or greater than 1. default 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :type PageSize: int
        :param _ResourceName: Resource file name (fuzzy search keyword).
        :type ResourceName: str
        :param _ParentFolderPath: Specifies the path of the file's parent folder (for example /a/b/c, querying resource files under the folder c).
        :type ParentFolderPath: str
        :param _CreateUserUin: Creator ID. obtain through the DescribeCurrentUserInfo API.
        :type CreateUserUin: str
        :param _ModifyTimeStart: Update time range. specifies the start time in yyyy-MM-dd HH:MM:ss format.
        :type ModifyTimeStart: str
        :param _ModifyTimeEnd: Update time range. specifies the end time in yyyy-MM-dd HH:MM:ss format.
        :type ModifyTimeEnd: str
        :param _CreateTimeStart: Create time range. specifies the start time in yyyy-MM-dd HH:MM:ss format.
        :type CreateTimeStart: str
        :param _CreateTimeEnd: Create time range. specifies the termination time in yyyy-MM-dd HH:MM:ss format.
        :type CreateTimeEnd: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._ResourceName = None
        self._ParentFolderPath = None
        self._CreateUserUin = None
        self._ModifyTimeStart = None
        self._ModifyTimeEnd = None
        self._CreateTimeStart = None
        self._CreateTimeEnd = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Data page number, equal to or greater than 1. default 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ResourceName(self):
        r"""Resource file name (fuzzy search keyword).
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ParentFolderPath(self):
        r"""Specifies the path of the file's parent folder (for example /a/b/c, querying resource files under the folder c).
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def CreateUserUin(self):
        r"""Creator ID. obtain through the DescribeCurrentUserInfo API.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTimeStart(self):
        r"""Update time range. specifies the start time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._ModifyTimeStart

    @ModifyTimeStart.setter
    def ModifyTimeStart(self, ModifyTimeStart):
        self._ModifyTimeStart = ModifyTimeStart

    @property
    def ModifyTimeEnd(self):
        r"""Update time range. specifies the end time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._ModifyTimeEnd

    @ModifyTimeEnd.setter
    def ModifyTimeEnd(self, ModifyTimeEnd):
        self._ModifyTimeEnd = ModifyTimeEnd

    @property
    def CreateTimeStart(self):
        r"""Create time range. specifies the start time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._CreateTimeStart

    @CreateTimeStart.setter
    def CreateTimeStart(self, CreateTimeStart):
        self._CreateTimeStart = CreateTimeStart

    @property
    def CreateTimeEnd(self):
        r"""Create time range. specifies the termination time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._CreateTimeEnd

    @CreateTimeEnd.setter
    def CreateTimeEnd(self, CreateTimeEnd):
        self._CreateTimeEnd = CreateTimeEnd


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ResourceName = params.get("ResourceName")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTimeStart = params.get("ModifyTimeStart")
        self._ModifyTimeEnd = params.get("ModifyTimeEnd")
        self._CreateTimeStart = params.get("CreateTimeStart")
        self._CreateTimeEnd = params.get("CreateTimeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListResourceFilesResponse(AbstractModel):
    r"""ListResourceFiles response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Retrieve the resource file list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFilePage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Retrieve the resource file list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFilePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFilePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListResourceFoldersRequest(AbstractModel):
    r"""ListResourceFolders request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Resource folder absolute path. value example.
/wedata/test
        :type ParentFolderPath: str
        :param _PageNumber: Data page number, equal to or greater than 1. default 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :type PageSize: int
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Resource folder absolute path. value example.
/wedata/test
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def PageNumber(self):
        r"""Data page number, equal to or greater than 1. default 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListResourceFoldersResponse(AbstractModel):
    r"""ListResourceFolders response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Paginated resource folder query result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ResourceFolderPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Paginated resource folder query result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ResourceFolderPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResourceFolderPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListSQLFolderContentsRequest(AbstractModel):
    r"""ListSQLFolderContents request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _ParentFolderPath: Parent folder path, /aaa/bbb/ccc. path header must include a slash. pass / to query the root directory.
        :type ParentFolderPath: str
        :param _Keyword: Folder name or script name search.
        :type Keyword: str
        :param _OnlyFolderNode: Queries only the folder.
        :type OnlyFolderNode: bool
        :param _OnlyUserSelfScript: Specifies whether to query only scripts created by the user themselves.
        :type OnlyUserSelfScript: bool
        :param _AccessScope: Access permission: SHARED, PRIVATE.
        :type AccessScope: str
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._Keyword = None
        self._OnlyFolderNode = None
        self._OnlyUserSelfScript = None
        self._AccessScope = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, /aaa/bbb/ccc. path header must include a slash. pass / to query the root directory.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def Keyword(self):
        r"""Folder name or script name search.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def OnlyFolderNode(self):
        r"""Queries only the folder.
        :rtype: bool
        """
        return self._OnlyFolderNode

    @OnlyFolderNode.setter
    def OnlyFolderNode(self, OnlyFolderNode):
        self._OnlyFolderNode = OnlyFolderNode

    @property
    def OnlyUserSelfScript(self):
        r"""Specifies whether to query only scripts created by the user themselves.
        :rtype: bool
        """
        return self._OnlyUserSelfScript

    @OnlyUserSelfScript.setter
    def OnlyUserSelfScript(self, OnlyUserSelfScript):
        self._OnlyUserSelfScript = OnlyUserSelfScript

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._Keyword = params.get("Keyword")
        self._OnlyFolderNode = params.get("OnlyFolderNode")
        self._OnlyUserSelfScript = params.get("OnlyUserSelfScript")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSQLFolderContentsResponse(AbstractModel):
    r"""ListSQLFolderContents response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result list
        :type Data: list of SQLFolderNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result list
        :rtype: list of SQLFolderNode
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SQLFolderNode()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSQLScriptRunsRequest(AbstractModel):
    r"""ListSQLScriptRuns request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ScriptId: Script id.
        :type ScriptId: str
        :param _JobId: Task ID.
        :type JobId: str
        :param _SearchWord: Search keywords.
        :type SearchWord: str
        :param _ExecuteUserUin: Specifies the executor ID.
        :type ExecuteUserUin: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        """
        self._ProjectId = None
        self._ScriptId = None
        self._JobId = None
        self._SearchWord = None
        self._ExecuteUserUin = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptId(self):
        r"""Script id.
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def JobId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SearchWord(self):
        r"""Search keywords.
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def ExecuteUserUin(self):
        r"""Specifies the executor ID.
        :rtype: str
        """
        return self._ExecuteUserUin

    @ExecuteUserUin.setter
    def ExecuteUserUin(self, ExecuteUserUin):
        self._ExecuteUserUin = ExecuteUserUin

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScriptId = params.get("ScriptId")
        self._JobId = params.get("JobId")
        self._SearchWord = params.get("SearchWord")
        self._ExecuteUserUin = params.get("ExecuteUserUin")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSQLScriptRunsResponse(AbstractModel):
    r"""ListSQLScriptRuns response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data Exploration runs.
        :type Data: list of JobDto
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data Exploration runs.
        :rtype: list of JobDto
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = JobDto()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTaskInfo(AbstractModel):
    r"""Query Task Info (Paginated)

    """

    def __init__(self):
        r"""
        :param _Items: Task Array

        :type Items: list of TaskBaseAttribute
        :param _PageNumber: Current request data page number.

        :type PageNumber: int
        :param _PageSize: Number of entries in the current request.

        :type PageSize: int
        :param _TotalCount: Total number of data entries that meet the query condition.
        :type TotalCount: int
        :param _TotalPageNumber: Total number of pages that meet the query condition.

        :type TotalPageNumber: int
        """
        self._Items = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None

    @property
    def Items(self):
        r"""Task Array

        :rtype: list of TaskBaseAttribute
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""Current request data page number.

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of entries in the current request.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of data entries that meet the query condition.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total number of pages that meet the query condition.

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskBaseAttribute()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstanceExecutionsRequest(AbstractModel):
    r"""ListTaskInstanceExecutions request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _InstanceKey: Instance unique id, can be obtained through ListInstances.
        :type InstanceKey: str
        :param _TimeZone: **Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :type TimeZone: str
        :param _PageSize: Size per page. default: 10. maximum: 200.
        :type PageSize: int
        :param _PageNumber: Page number, which is 1 by default.
        :type PageNumber: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def ProjectId(self):
        r"""Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""Instance unique id, can be obtained through ListInstances.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageSize(self):
        r"""Size per page. default: 10. maximum: 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstanceExecutionsResponse(AbstractModel):
    r"""ListTaskInstanceExecutions response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Instance details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceExecutions`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Instance details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstanceExecutions`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstanceExecutions()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTaskInstancesRequest(AbstractModel):
    r"""ListTaskInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: **Project ID**. specifies the project ID.
        :type ProjectId: str
        :param _PageNumber: **Page number. integer.**.
Used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of items to display per page. default: 10. value range: 1-100.
        :type PageSize: int
        :param _Keyword: Task name or task ID.
Supports fuzzy search filtering. multiple values are separated by commas.
        :type Keyword: str
        :param _TimeZone: **Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :type TimeZone: str
        :param _InstanceType: **Instance Type**

0 - Backfill instance

1 - Cyclic (scheduled) instance

2 - Non-cyclic (non-scheduled) instance
        :type InstanceType: int
        :param _InstanceState: **Instance Status**

WAIT_EVENT: Waiting for event

WAIT_UPSTREAM: Waiting for upstream

WAIT_RUN: Waiting to run

RUNNING: Running

SKIP_RUNNING: Skipped

FAILED_RETRY: Retrying after failure

EXPIRED: Failed

COMPLETED: Succeeded
        :type InstanceState: str
        :param _TaskTypeId: Task type Id.
        :type TaskTypeId: int
        :param _CycleType: **Task Cycle Type**

ONEOFF_CYCLE: One-time

YEAR_CYCLE: Yearly

MONTH_CYCLE: Monthly

WEEK_CYCLE: Weekly

DAY_CYCLE: Daily

HOUR_CYCLE: Hourly

MINUTE_CYCLE: Minute-level

CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _OwnerUin: Task owner id.
        :type OwnerUin: str
        :param _FolderId: Folder id
        :type FolderId: str
        :param _WorkflowId: Workflow id of the task.
        :type WorkflowId: str
        :param _ExecutorGroupId: **Execution resource group Id**.
        :type ExecutorGroupId: str
        :param _ScheduleTimeFrom: **Instance Scheduled Time Filter Condition** specifies the filter start time in the time format yyyy-MM-dd HH:MM:ss.
        :type ScheduleTimeFrom: str
        :param _ScheduleTimeTo: **Instance Scheduled Time Filter Condition** specifies the cutoff time in the format of yyyy-MM-dd HH:MM:ss.
        :type ScheduleTimeTo: str
        :param _StartTimeFrom: **Instance Execution Start Time Filter Condition** specifies the start time for filtering. time format: yyyy-MM-dd HH:MM:ss.
        :type StartTimeFrom: str
        :param _StartTimeTo: **Instance Execution Start Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :type StartTimeTo: str
        :param _LastUpdateTimeFrom: **Instance Last Update Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :type LastUpdateTimeFrom: str
        :param _LastUpdateTimeTo: **Instance Last Update Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :type LastUpdateTimeTo: str
        :param _SortColumn: **Query Result Sorting Field**

SCHEDULE_DATE: Sort by scheduled execution time

START_TIME: Sort by actual execution start time

END_TIME: Sort by actual execution end time

COST_TIME: Sort by execution duration
        :type SortColumn: str
        :param _SortType: **Instance Sorting Order**

- ASC 
- DESC
        :type SortType: str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._TimeZone = None
        self._InstanceType = None
        self._InstanceState = None
        self._TaskTypeId = None
        self._CycleType = None
        self._OwnerUin = None
        self._FolderId = None
        self._WorkflowId = None
        self._ExecutorGroupId = None
        self._ScheduleTimeFrom = None
        self._ScheduleTimeTo = None
        self._StartTimeFrom = None
        self._StartTimeTo = None
        self._LastUpdateTimeFrom = None
        self._LastUpdateTimeTo = None
        self._SortColumn = None
        self._SortType = None

    @property
    def ProjectId(self):
        r"""**Project ID**. specifies the project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""**Page number. integer.**.
Used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of items to display per page. default: 10. value range: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""Task name or task ID.
Supports fuzzy search filtering. multiple values are separated by commas.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def TimeZone(self):
        r"""**Time zone** timeZone, specifies the time zone of the passed in time string. default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def InstanceType(self):
        r"""**Instance Type**

0 - Backfill instance

1 - Cyclic (scheduled) instance

2 - Non-cyclic (non-scheduled) instance
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceState(self):
        r"""**Instance Status**

WAIT_EVENT: Waiting for event

WAIT_UPSTREAM: Waiting for upstream

WAIT_RUN: Waiting to run

RUNNING: Running

SKIP_RUNNING: Skipped

FAILED_RETRY: Retrying after failure

EXPIRED: Failed

COMPLETED: Succeeded
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def TaskTypeId(self):
        r"""Task type Id.
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def CycleType(self):
        r"""**Task Cycle Type**

ONEOFF_CYCLE: One-time

YEAR_CYCLE: Yearly

MONTH_CYCLE: Monthly

WEEK_CYCLE: Weekly

DAY_CYCLE: Daily

HOUR_CYCLE: Hourly

MINUTE_CYCLE: Minute-level

CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""Task owner id.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def FolderId(self):
        r"""Folder id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkflowId(self):
        r"""Workflow id of the task.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def ExecutorGroupId(self):
        r"""**Execution resource group Id**.
        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ScheduleTimeFrom(self):
        r"""**Instance Scheduled Time Filter Condition** specifies the filter start time in the time format yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._ScheduleTimeFrom

    @ScheduleTimeFrom.setter
    def ScheduleTimeFrom(self, ScheduleTimeFrom):
        self._ScheduleTimeFrom = ScheduleTimeFrom

    @property
    def ScheduleTimeTo(self):
        r"""**Instance Scheduled Time Filter Condition** specifies the cutoff time in the format of yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._ScheduleTimeTo

    @ScheduleTimeTo.setter
    def ScheduleTimeTo(self, ScheduleTimeTo):
        self._ScheduleTimeTo = ScheduleTimeTo

    @property
    def StartTimeFrom(self):
        r"""**Instance Execution Start Time Filter Condition** specifies the start time for filtering. time format: yyyy-MM-dd HH:MM:ss.
        :rtype: str
        """
        return self._StartTimeFrom

    @StartTimeFrom.setter
    def StartTimeFrom(self, StartTimeFrom):
        self._StartTimeFrom = StartTimeFrom

    @property
    def StartTimeTo(self):
        r"""**Instance Execution Start Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._StartTimeTo

    @StartTimeTo.setter
    def StartTimeTo(self, StartTimeTo):
        self._StartTimeTo = StartTimeTo

    @property
    def LastUpdateTimeFrom(self):
        r"""**Instance Last Update Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._LastUpdateTimeFrom

    @LastUpdateTimeFrom.setter
    def LastUpdateTimeFrom(self, LastUpdateTimeFrom):
        self._LastUpdateTimeFrom = LastUpdateTimeFrom

    @property
    def LastUpdateTimeTo(self):
        r"""**Instance Last Update Time Filter Condition**.
Expiration time in yyyy-MM-dd HH:MM:ss format.
        :rtype: str
        """
        return self._LastUpdateTimeTo

    @LastUpdateTimeTo.setter
    def LastUpdateTimeTo(self, LastUpdateTimeTo):
        self._LastUpdateTimeTo = LastUpdateTimeTo

    @property
    def SortColumn(self):
        r"""**Query Result Sorting Field**

SCHEDULE_DATE: Sort by scheduled execution time

START_TIME: Sort by actual execution start time

END_TIME: Sort by actual execution end time

COST_TIME: Sort by execution duration
        :rtype: str
        """
        return self._SortColumn

    @SortColumn.setter
    def SortColumn(self, SortColumn):
        self._SortColumn = SortColumn

    @property
    def SortType(self):
        r"""**Instance Sorting Order**

- ASC 
- DESC
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._TimeZone = params.get("TimeZone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceState = params.get("InstanceState")
        self._TaskTypeId = params.get("TaskTypeId")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._FolderId = params.get("FolderId")
        self._WorkflowId = params.get("WorkflowId")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ScheduleTimeFrom = params.get("ScheduleTimeFrom")
        self._ScheduleTimeTo = params.get("ScheduleTimeTo")
        self._StartTimeFrom = params.get("StartTimeFrom")
        self._StartTimeTo = params.get("StartTimeTo")
        self._LastUpdateTimeFrom = params.get("LastUpdateTimeFrom")
        self._LastUpdateTimeTo = params.get("LastUpdateTimeTo")
        self._SortColumn = params.get("SortColumn")
        self._SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskInstancesResponse(AbstractModel):
    r"""ListTaskInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Instance result set.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Instance result set.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTaskVersions(AbstractModel):
    r"""Describes the pagination list of query task versions.

    """

    def __init__(self):
        r"""
        :param _Items: Record list	
	

        :type Items: list of TaskVersion
        :param _TotalCount: Total number of records that meet the query condition.

        :type TotalCount: int
        :param _TotalPageNumber: Total number of pages that meet the query condition.

        :type TotalPageNumber: int
        :param _PageCount: Number of records on current page.

        :type PageCount: int
        :param _PageSize: Specifies the number of entries in the current request data page.

        :type PageSize: int
        :param _PageNumber: Specifies the data page number of the current request.

        :type PageNumber: int
        """
        self._Items = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageCount = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Items(self):
        r"""Record list	
	

        :rtype: list of TaskVersion
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""Total number of records that meet the query condition.

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total number of pages that meet the query condition.

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageCount(self):
        r"""Number of records on current page.

        :rtype: int
        """
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def PageSize(self):
        r"""Specifies the number of entries in the current request data page.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Specifies the data page number of the current request.

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskVersion()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageCount = params.get("PageCount")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskVersionsRequest(AbstractModel):
    r"""ListTaskVersions request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskVersionType: SAVE version.
SUBMIT version.
Defaults to SAVE.
        :type TaskVersionType: str
        :param _PageNumber: Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._TaskVersionType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskVersionType(self):
        r"""SAVE version.
SUBMIT version.
Defaults to SAVE.
        :rtype: str
        """
        return self._TaskVersionType

    @TaskVersionType.setter
    def TaskVersionType(self, TaskVersionType):
        self._TaskVersionType = TaskVersionType

    @property
    def PageNumber(self):
        r"""Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._TaskVersionType = params.get("TaskVersionType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTaskVersionsResponse(AbstractModel):
    r"""ListTaskVersions response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task version list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersions`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task version list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskVersions`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListTaskVersions()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTasksRequest(AbstractModel):
    r"""ListTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageNumber: Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :type PageSize: int
        :param _TaskName: Task name.
        :type TaskName: str
        :param _WorkflowId: Workflow ID
        :type WorkflowId: str
        :param _OwnerUin: Owner ID.
        :type OwnerUin: str
        :param _TaskTypeId: Task type
        :type TaskTypeId: int
        :param _Status: Task Status:
* N: New
* Y: Scheduling
* F: Offline
* O: Paused
* T: Offlining
* INVALID: Invalid
        :type Status: str
        :param _Submit: Submission status.
        :type Submit: bool
        :param _BundleId: Bundle id.
        :type BundleId: str
        :param _CreateUserUin: Creator ID.
        :type CreateUserUin: str
        :param _ModifyTime: Modification time range (yyyy-MM-dd HH:mm:ss). Two time values must be provided in the array.
        :type ModifyTime: list of str
        :param _CreateTime: Creation time range (yyyy-MM-dd HH:MM:ss). Two time values must be provided in the array.
        :type CreateTime: list of str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._TaskName = None
        self._WorkflowId = None
        self._OwnerUin = None
        self._TaskTypeId = None
        self._Status = None
        self._Submit = None
        self._BundleId = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""Workflow ID
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def OwnerUin(self):
        r"""Owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskTypeId(self):
        r"""Task type
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def Status(self):
        r"""Task Status:
* N: New
* Y: Scheduling
* F: Offline
* O: Paused
* T: Offlining
* INVALID: Invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Submit(self):
        r"""Submission status.
        :rtype: bool
        """
        return self._Submit

    @Submit.setter
    def Submit(self, Submit):
        self._Submit = Submit

    @property
    def BundleId(self):
        r"""Bundle id.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def CreateUserUin(self):
        r"""Creator ID.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""Modification time range (yyyy-MM-dd HH:mm:ss). Two time values must be provided in the array.
        :rtype: list of str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""Creation time range (yyyy-MM-dd HH:MM:ss). Two time values must be provided in the array.
        :rtype: list of str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskTypeId = params.get("TaskTypeId")
        self._Status = params.get("Status")
        self._Submit = params.get("Submit")
        self._BundleId = params.get("BundleId")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksResponse(AbstractModel):
    r"""ListTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Describes the task pagination information.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListTaskInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Describes the task pagination information.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListTaskInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListTaskInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamOpsTasksRequest(AbstractModel):
    r"""ListUpstreamOpsTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _PageNumber: Page number
        :type PageNumber: str
        :param _PageSize: Pagination size.
        :type PageSize: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: str
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamOpsTasksResponse(AbstractModel):
    r"""ListUpstreamOpsTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Upstream task details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ParentDependencyConfigPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Upstream task details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ParentDependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ParentDependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamTaskInstancesRequest(AbstractModel):
    r"""ListUpstreamTaskInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _InstanceKey: **Instance unique id**.
        :type InstanceKey: str
        :param _TimeZone: **Time zone** timeZone, default UTC+8.
        :type TimeZone: str
        :param _PageNumber: **Page number, int** used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of items to display per page. default: 10. value range: 1-100.
        :type PageSize: int
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._TimeZone = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**Instance unique id**.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def TimeZone(self):
        r"""**Time zone** timeZone, default UTC+8.
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def PageNumber(self):
        r"""**Page number, int** used in conjunction with pageSize and cannot be less than 1. default value: 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of items to display per page. default: 10. value range: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._TimeZone = params.get("TimeZone")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamTaskInstancesResponse(AbstractModel):
    r"""ListUpstreamTaskInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Upstream instance list.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Upstream instance list.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskInstancePage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskInstancePage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListUpstreamTasksRequest(AbstractModel):
    r"""ListUpstreamTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _PageNumber: Specifies the data page number of the request. Default value is 1. Valid values: equal to or greater than 1.
        :type PageNumber: int
        :param _PageSize: Specifies the data page number of the request. Default value is 1. Valid values: equal to or greater than 1.
        :type PageSize: int
        """
        self._ProjectId = None
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""Specifies the data page number of the request. Default value is 1. Valid values: equal to or greater than 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the data page number of the request. Default value is 1. Valid values: equal to or greater than 1.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUpstreamTasksResponse(AbstractModel):
    r"""ListUpstreamTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Upstream task details.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Upstream task details.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.DependencyConfigPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DependencyConfigPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowFoldersRequest(AbstractModel):
    r"""ListWorkflowFolders request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ParentFolderPath: Parent folder absolute path, for example /abc/de, if it is root directory, pass /.
        :type ParentFolderPath: str
        :param _PageNumber: Data page number, equal to or greater than 1. default 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :type PageSize: int
        """
        self._ProjectId = None
        self._ParentFolderPath = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ParentFolderPath(self):
        r"""Parent folder absolute path, for example /abc/de, if it is root directory, pass /.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def PageNumber(self):
        r"""Data page number, equal to or greater than 1. default 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. valid values: 10 to 200. default: 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowFoldersResponse(AbstractModel):
    r"""ListWorkflowFolders response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Paginated folder query result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.WorkflowFolderPage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Paginated folder query result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowFolderPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = WorkflowFolderPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListWorkflowInfo(AbstractModel):
    r"""Query workflow pagination list.

    """

    def __init__(self):
        r"""
        :param _Items: List items.
        :type Items: list of WorkflowInfo
        :param _TotalPageNumber: Total number of pages that meet the query condition.

        :type TotalPageNumber: int
        :param _PageNumber: Current request data page number.

        :type PageNumber: int
        :param _PageSize: Number of entries in the current request.

        :type PageSize: int
        :param _TotalCount: Total number of data entries that meet the query condition.

        :type TotalCount: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None

    @property
    def Items(self):
        r"""List items.
        :rtype: list of WorkflowInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""Total number of pages that meet the query condition.

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""Current request data page number.

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of entries in the current request.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of data entries that meet the query condition.

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsRequest(AbstractModel):
    r"""ListWorkflows request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _PageNumber: Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :type PageSize: int
        :param _Keyword: Search keywords.
        :type Keyword: str
        :param _ParentFolderPath: Workflow folder.
        :type ParentFolderPath: str
        :param _WorkflowType: Workflow type. valid values: cycle and manual.
        :type WorkflowType: str
        :param _BundleId: bundleId item.
        :type BundleId: str
        :param _OwnerUin: Owner ID
        :type OwnerUin: str
        :param _CreateUserUin: Creator ID.
        :type CreateUserUin: str
        :param _ModifyTime: Modification time interval yyyy-MM-dd HH:MM:ss. fill in two times in the array.
        :type ModifyTime: list of str
        :param _CreateTime: Creation time range yyyy-MM-dd HH:MM:ss. two times must be filled in the array.
        :type CreateTime: list of str
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._ParentFolderPath = None
        self._WorkflowType = None
        self._BundleId = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._ModifyTime = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""Specifies the data page number of the request. default value is 1. valid values: equal to or greater than 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. default: 10. value range: 10 to 200.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        r"""Search keywords.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ParentFolderPath(self):
        r"""Workflow folder.
        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def WorkflowType(self):
        r"""Workflow type. valid values: cycle and manual.
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def BundleId(self):
        r"""bundleId item.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def OwnerUin(self):
        r"""Owner ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""Creator ID.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def ModifyTime(self):
        r"""Modification time interval yyyy-MM-dd HH:MM:ss. fill in two times in the array.
        :rtype: list of str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        r"""Creation time range yyyy-MM-dd HH:MM:ss. two times must be filled in the array.
        :rtype: list of str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._WorkflowType = params.get("WorkflowType")
        self._BundleId = params.get("BundleId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWorkflowsResponse(AbstractModel):
    r"""ListWorkflows response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Describes workflow pagination information.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Describes workflow pagination information.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ListWorkflowInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListWorkflowInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyAlarmRuleResult(AbstractModel):
    r"""Describes the response of updating an Alarm rule.

    """

    def __init__(self):
        r"""
        :param _Status: Whether update succeeded
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Whether update succeeded
        :rtype: bool
        """
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
        


class NotebookSessionInfo(AbstractModel):
    r"""notebook kernel session information.

    """

    def __init__(self):
        r"""
        :param _NotebookSessionId: Specifies the session ID.
        :type NotebookSessionId: str
        :param _NotebookSessionName: Session Name
        :type NotebookSessionName: str
        """
        self._NotebookSessionId = None
        self._NotebookSessionName = None

    @property
    def NotebookSessionId(self):
        r"""Specifies the session ID.
        :rtype: str
        """
        return self._NotebookSessionId

    @NotebookSessionId.setter
    def NotebookSessionId(self, NotebookSessionId):
        self._NotebookSessionId = NotebookSessionId

    @property
    def NotebookSessionName(self):
        r"""Session Name
        :rtype: str
        """
        return self._NotebookSessionName

    @NotebookSessionName.setter
    def NotebookSessionName(self, NotebookSessionName):
        self._NotebookSessionName = NotebookSessionName


    def _deserialize(self, params):
        self._NotebookSessionId = params.get("NotebookSessionId")
        self._NotebookSessionName = params.get("NotebookSessionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotificationFatigue(AbstractModel):
    r"""Alarm fatigue Alarm configuration.

    """

    def __init__(self):
        r"""
        :param _NotifyCount: Number of alarms.
        :type NotifyCount: int
        :param _NotifyInterval: Alarm interval, in minutes.
        :type NotifyInterval: int
        :param _QuietIntervals: Do not disturb period, such as example value.
[{DaysOfWeek: [1, 2], StartTime: "00:00:00", EndTime: "09:00:00"}]	
Specifies notification muting from 00:00 to 09:00 every monday and tuesday.
        :type QuietIntervals: list of AlarmQuietInterval
        """
        self._NotifyCount = None
        self._NotifyInterval = None
        self._QuietIntervals = None

    @property
    def NotifyCount(self):
        r"""Number of alarms.
        :rtype: int
        """
        return self._NotifyCount

    @NotifyCount.setter
    def NotifyCount(self, NotifyCount):
        self._NotifyCount = NotifyCount

    @property
    def NotifyInterval(self):
        r"""Alarm interval, in minutes.
        :rtype: int
        """
        return self._NotifyInterval

    @NotifyInterval.setter
    def NotifyInterval(self, NotifyInterval):
        self._NotifyInterval = NotifyInterval

    @property
    def QuietIntervals(self):
        r"""Do not disturb period, such as example value.
[{DaysOfWeek: [1, 2], StartTime: "00:00:00", EndTime: "09:00:00"}]	
Specifies notification muting from 00:00 to 09:00 every monday and tuesday.
        :rtype: list of AlarmQuietInterval
        """
        return self._QuietIntervals

    @QuietIntervals.setter
    def QuietIntervals(self, QuietIntervals):
        self._QuietIntervals = QuietIntervals


    def _deserialize(self, params):
        self._NotifyCount = params.get("NotifyCount")
        self._NotifyInterval = params.get("NotifyInterval")
        if params.get("QuietIntervals") is not None:
            self._QuietIntervals = []
            for item in params.get("QuietIntervals"):
                obj = AlarmQuietInterval()
                obj._deserialize(item)
                self._QuietIntervals.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsAsyncJobDetail(AbstractModel):
    r"""Asynchronous operation details.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AsyncId: Operation ID
        :type AsyncId: str
        :param _AsyncType: Asynchronous operation type.
        :type AsyncType: str
        :param _Status: Asynchronous operation status: initial status: INIT; Running: RUNNING; Success: SUCCESS; failure: FAIL; partially successful: PART_SUCCESS.
        :type Status: str
        :param _ErrorDesc: Error message.


        :type ErrorDesc: str
        :param _TotalSubProcessCount: Total sub-processes.
        :type TotalSubProcessCount: int
        :param _FinishedSubProcessCount: Number of completed sub-processes.

        :type FinishedSubProcessCount: int
        :param _SuccessSubProcessCount: Count of successful sub-processes.

        :type SuccessSubProcessCount: int
        :param _CreateUserUin: Operator id.
        :type CreateUserUin: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        """
        self._ProjectId = None
        self._AsyncId = None
        self._AsyncType = None
        self._Status = None
        self._ErrorDesc = None
        self._TotalSubProcessCount = None
        self._FinishedSubProcessCount = None
        self._SuccessSubProcessCount = None
        self._CreateUserUin = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AsyncId(self):
        r"""Operation ID
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId

    @property
    def AsyncType(self):
        r"""Asynchronous operation type.
        :rtype: str
        """
        return self._AsyncType

    @AsyncType.setter
    def AsyncType(self, AsyncType):
        self._AsyncType = AsyncType

    @property
    def Status(self):
        r"""Asynchronous operation status: initial status: INIT; Running: RUNNING; Success: SUCCESS; failure: FAIL; partially successful: PART_SUCCESS.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorDesc(self):
        r"""Error message.


        :rtype: str
        """
        return self._ErrorDesc

    @ErrorDesc.setter
    def ErrorDesc(self, ErrorDesc):
        self._ErrorDesc = ErrorDesc

    @property
    def TotalSubProcessCount(self):
        r"""Total sub-processes.
        :rtype: int
        """
        return self._TotalSubProcessCount

    @TotalSubProcessCount.setter
    def TotalSubProcessCount(self, TotalSubProcessCount):
        self._TotalSubProcessCount = TotalSubProcessCount

    @property
    def FinishedSubProcessCount(self):
        r"""Number of completed sub-processes.

        :rtype: int
        """
        return self._FinishedSubProcessCount

    @FinishedSubProcessCount.setter
    def FinishedSubProcessCount(self, FinishedSubProcessCount):
        self._FinishedSubProcessCount = FinishedSubProcessCount

    @property
    def SuccessSubProcessCount(self):
        r"""Count of successful sub-processes.

        :rtype: int
        """
        return self._SuccessSubProcessCount

    @SuccessSubProcessCount.setter
    def SuccessSubProcessCount(self, SuccessSubProcessCount):
        self._SuccessSubProcessCount = SuccessSubProcessCount

    @property
    def CreateUserUin(self):
        r"""Operator id.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AsyncId = params.get("AsyncId")
        self._AsyncType = params.get("AsyncType")
        self._Status = params.get("Status")
        self._ErrorDesc = params.get("ErrorDesc")
        self._TotalSubProcessCount = params.get("TotalSubProcessCount")
        self._FinishedSubProcessCount = params.get("FinishedSubProcessCount")
        self._SuccessSubProcessCount = params.get("SuccessSubProcessCount")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsAsyncResponse(AbstractModel):
    r"""Asynchronous operation return structure.

    """

    def __init__(self):
        r"""
        :param _AsyncId: Asynchronous execution record Id.
        :type AsyncId: str
        """
        self._AsyncId = None

    @property
    def AsyncId(self):
        r"""Asynchronous execution record Id.
        :rtype: str
        """
        return self._AsyncId

    @AsyncId.setter
    def AsyncId(self, AsyncId):
        self._AsyncId = AsyncId


    def _deserialize(self, params):
        self._AsyncId = params.get("AsyncId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsTaskDepend(AbstractModel):
    r"""Dependent task information.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID


        :type TaskId: str
        :param _TaskName: Task name.


        :type TaskName: str
        :param _WorkflowId: Workflow id.

        :type WorkflowId: str
        :param _WorkflowName: Workflow name.


        :type WorkflowName: str
        :param _ProjectId: Project ID.


        :type ProjectId: str
        :param _ProjectName: Project name.


        :type ProjectName: str
        :param _Status: Task Status

-N: New

-Y: Scheduling

-F: Offline

-O: Paused

-T: Offlining

-INVALID: Invalid
        :type Status: str
        :param _TaskTypeId: Task type Id.
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskTypeId: int
        :param _TaskTypeDesc: Task type description.
-20 : universal data synchronization.
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
-130: specifies the branch.
-131: specifies the merge.
-132: specifies the Notebook explore.
-133: specifies the SSH node.
 - 134 :  StarRocks
 - 137 :  For-each
-10000: common custom business.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskTypeDesc: str
        :param _FolderName: Folder name.

        :type FolderName: str
        :param _FolderId: Folder ID

        :type FolderId: str
        :param _FirstSubmitTime: Latest submission time.

        :type FirstSubmitTime: str
        :param _FirstRunTime: First running time


        :type FirstRunTime: str
        :param _ScheduleDesc: Describes the scheduling plan display description information.

        :type ScheduleDesc: str
        :param _CycleType: Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _OwnerUin: Specifies the person in charge.
        :type OwnerUin: str
        :param _ExecutionStartTime: Execution start time. format: HH:mm, for example 00:00.

        :type ExecutionStartTime: str
        :param _ExecutionEndTime: Execution end time. format: HH:mm, for example 23:59.

        :type ExecutionEndTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._FolderName = None
        self._FolderId = None
        self._FirstSubmitTime = None
        self._FirstRunTime = None
        self._ScheduleDesc = None
        self._CycleType = None
        self._OwnerUin = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None

    @property
    def TaskId(self):
        r"""Task ID


        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.


        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""Workflow id.

        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.


        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""Project ID.


        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name.


        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Status(self):
        r"""Task Status

-N: New

-Y: Scheduling

-F: Offline

-O: Paused

-T: Offlining

-INVALID: Invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskTypeId(self):
        r"""Task type Id.
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""Task type description.
-20 : universal data synchronization.
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
-130: specifies the branch.
-131: specifies the merge.
-132: specifies the Notebook explore.
-133: specifies the SSH node.
 - 134 :  StarRocks
 - 137 :  For-each
-10000: common custom business.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def FolderName(self):
        r"""Folder name.

        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderId(self):
        r"""Folder ID

        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FirstSubmitTime(self):
        r"""Latest submission time.

        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def FirstRunTime(self):
        r"""First running time


        :rtype: str
        """
        return self._FirstRunTime

    @FirstRunTime.setter
    def FirstRunTime(self, FirstRunTime):
        self._FirstRunTime = FirstRunTime

    @property
    def ScheduleDesc(self):
        r"""Describes the scheduling plan display description information.

        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def CycleType(self):
        r"""Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""Specifies the person in charge.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ExecutionStartTime(self):
        r"""Execution start time. format: HH:mm, for example 00:00.

        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""Execution end time. format: HH:mm, for example 23:59.

        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._FolderName = params.get("FolderName")
        self._FolderId = params.get("FolderId")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._FirstRunTime = params.get("FirstRunTime")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflow(AbstractModel):
    r"""Workflow list pagination details.

    """

    def __init__(self):
        r"""
        :param _TaskCount: Number of Tasks
        :type TaskCount: int
        :param _FolderName: folder name.

        :type FolderName: str
        :param _FolderId: Workflow folder id.
        :type FolderId: str
        :param _WorkflowId: Workflow id.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.

Note: This field may return null, indicating that no valid values can be obtained.
        :type WorkflowName: str
        :param _WorkflowType: Specifies the workflow type.
-cycle period.
-manual.
        :type WorkflowType: str
        :param _WorkflowDesc: Workflow description.

        :type WorkflowDesc: str
        :param _OwnerUin: Responsible user id, multiple ';' separators.

        :type OwnerUin: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ProjectName: Project name.


        :type ProjectName: str
        :param _Status: Workflow Status

* ALL_RUNNING: All running (all workflows are in scheduling state)

* ALL_FREEZED: All paused

* ALL_STOPPTED: All stopped

* PART_RUNNING: Partially running (some workflows are running, others not)

* ALL_NO_RUNNING: All not scheduled

* ALL_INVALID: All invalid
        :type Status: str
        :param _CreateTime: Workflow creation time.

        :type CreateTime: str
        :param _UpdateTime: Latest update time. specifies development and production updates.
        :type UpdateTime: str
        :param _UpdateUserUin: Last updated by, including development and production updates.
        :type UpdateUserUin: str
        """
        self._TaskCount = None
        self._FolderName = None
        self._FolderId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowType = None
        self._WorkflowDesc = None
        self._OwnerUin = None
        self._ProjectId = None
        self._ProjectName = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._UpdateUserUin = None

    @property
    def TaskCount(self):
        r"""Number of Tasks
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def FolderName(self):
        r"""folder name.

        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderId(self):
        r"""Workflow folder id.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkflowId(self):
        r"""Workflow id.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowType(self):
        r"""Specifies the workflow type.
-cycle period.
-manual.
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowDesc(self):
        r"""Workflow description.

        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def OwnerUin(self):
        r"""Responsible user id, multiple ';' separators.

        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name.


        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Status(self):
        r"""Workflow Status

* ALL_RUNNING: All running (all workflows are in scheduling state)

* ALL_FREEZED: All paused

* ALL_STOPPTED: All stopped

* PART_RUNNING: Partially running (some workflows are running, others not)

* ALL_NO_RUNNING: All not scheduled

* ALL_INVALID: All invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""Workflow creation time.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Latest update time. specifies development and production updates.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UpdateUserUin(self):
        r"""Last updated by, including development and production updates.
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin


    def _deserialize(self, params):
        self._TaskCount = params.get("TaskCount")
        self._FolderName = params.get("FolderName")
        self._FolderId = params.get("FolderId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowType = params.get("WorkflowType")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._UpdateUserUin = params.get("UpdateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflowDetail(AbstractModel):
    r"""Workflow scheduling details.

    """

    def __init__(self):
        r"""
        :param _WorkflowId: Workflow ID.

        :type WorkflowId: str
        :param _WorkflowDesc: Workflow description.

        :type WorkflowDesc: str
        :param _WorkflowType: Specifies the workflow type.
-cycle.
-manual.
        :type WorkflowType: str
        :param _CreateTime: Creation time.

        :type CreateTime: str
        :param _CreateUserUin: Creator

        :type CreateUserUin: str
        :param _UpdateTime: Modification time.

        :type UpdateTime: str
        :param _StartupTime: Delayed execution time. unit: minute.

        :type StartupTime: int
        :param _StartTime: Effective date. specifies the start date.

        :type StartTime: str
        :param _EndTime: Configure end date end date.

        :type EndTime: str
        :param _CycleType: Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _FolderId: Folder ID


        :type FolderId: str
        :param _InstanceInitStrategy: Task instance initialization strategy.
-T_PLUS_1 (t+1): initializes with a one-day delay.
-T_PLUS_0 (t+0): initialize on the day.
-T_MINUS_1 (t-1): initialize one day in advance.

        :type InstanceInitStrategy: str
        :param _SchedulerDesc: Specifies the scheduling plan interpretation.

        :type SchedulerDesc: str
        :param _FirstSubmitTime: First submission time of workflow.

        :type FirstSubmitTime: str
        :param _LatestSubmitTime: Latest submission time of workflow.

        :type LatestSubmitTime: str
        :param _Status: Workflow Status

* ALL_RUNNING: All running (all workflows are in scheduling state)

* ALL_FREEZED: All paused

* ALL_STOPPTED: All stopped

* PART_RUNNING: Partially running (some workflows are running, others not)

* ALL_NO_RUNNING: All not scheduled

* ALL_INVALID: All invalid
        :type Status: str
        :param _OwnerUin: Person in charge. multiple values are separated by a ";" separator.
        :type OwnerUin: str
        :param _WorkflowName: Workflow name.

        :type WorkflowName: str
        """
        self._WorkflowId = None
        self._WorkflowDesc = None
        self._WorkflowType = None
        self._CreateTime = None
        self._CreateUserUin = None
        self._UpdateTime = None
        self._StartupTime = None
        self._StartTime = None
        self._EndTime = None
        self._CycleType = None
        self._FolderId = None
        self._InstanceInitStrategy = None
        self._SchedulerDesc = None
        self._FirstSubmitTime = None
        self._LatestSubmitTime = None
        self._Status = None
        self._OwnerUin = None
        self._WorkflowName = None

    @property
    def WorkflowId(self):
        r"""Workflow ID.

        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowDesc(self):
        r"""Workflow description.

        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def WorkflowType(self):
        r"""Specifies the workflow type.
-cycle.
-manual.
        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def CreateTime(self):
        r"""Creation time.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateUserUin(self):
        r"""Creator

        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def UpdateTime(self):
        r"""Modification time.

        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartupTime(self):
        r"""Delayed execution time. unit: minute.

        :rtype: int
        """
        return self._StartupTime

    @StartupTime.setter
    def StartupTime(self, StartupTime):
        self._StartupTime = StartupTime

    @property
    def StartTime(self):
        r"""Effective date. specifies the start date.

        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Configure end date end date.

        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CycleType(self):
        r"""Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def FolderId(self):
        r"""Folder ID


        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def InstanceInitStrategy(self):
        r"""Task instance initialization strategy.
-T_PLUS_1 (t+1): initializes with a one-day delay.
-T_PLUS_0 (t+0): initialize on the day.
-T_MINUS_1 (t-1): initialize one day in advance.

        :rtype: str
        """
        return self._InstanceInitStrategy

    @InstanceInitStrategy.setter
    def InstanceInitStrategy(self, InstanceInitStrategy):
        self._InstanceInitStrategy = InstanceInitStrategy

    @property
    def SchedulerDesc(self):
        r"""Specifies the scheduling plan interpretation.

        :rtype: str
        """
        return self._SchedulerDesc

    @SchedulerDesc.setter
    def SchedulerDesc(self, SchedulerDesc):
        self._SchedulerDesc = SchedulerDesc

    @property
    def FirstSubmitTime(self):
        r"""First submission time of workflow.

        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def LatestSubmitTime(self):
        r"""Latest submission time of workflow.

        :rtype: str
        """
        return self._LatestSubmitTime

    @LatestSubmitTime.setter
    def LatestSubmitTime(self, LatestSubmitTime):
        self._LatestSubmitTime = LatestSubmitTime

    @property
    def Status(self):
        r"""Workflow Status

* ALL_RUNNING: All running (all workflows are in scheduling state)

* ALL_FREEZED: All paused

* ALL_STOPPTED: All stopped

* PART_RUNNING: Partially running (some workflows are running, others not)

* ALL_NO_RUNNING: All not scheduled

* ALL_INVALID: All invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        r"""Person in charge. multiple values are separated by a ";" separator.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowName(self):
        r"""Workflow name.

        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._WorkflowType = params.get("WorkflowType")
        self._CreateTime = params.get("CreateTime")
        self._CreateUserUin = params.get("CreateUserUin")
        self._UpdateTime = params.get("UpdateTime")
        self._StartupTime = params.get("StartupTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CycleType = params.get("CycleType")
        self._FolderId = params.get("FolderId")
        self._InstanceInitStrategy = params.get("InstanceInitStrategy")
        self._SchedulerDesc = params.get("SchedulerDesc")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._LatestSubmitTime = params.get("LatestSubmitTime")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowName = params.get("WorkflowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpsWorkflows(AbstractModel):
    r"""Query workflow pagination list.

    """

    def __init__(self):
        r"""
        :param _Items: Record list	
	

        :type Items: list of OpsWorkflow
        :param _TotalCount: Total number of results


        :type TotalCount: int
        :param _TotalPageNumber: Total pages


        :type TotalPageNumber: int
        :param _PageSize: Pagination size.

        :type PageSize: int
        :param _PageNumber: Page number


        :type PageNumber: int
        """
        self._Items = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Items(self):
        r"""Record list	
	

        :rtype: list of OpsWorkflow
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""Total number of results


        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages


        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageSize(self):
        r"""Pagination size.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Page number


        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsWorkflow()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutTaskParameter(AbstractModel):
    r"""Parameter passing - output parameter.

    """

    def __init__(self):
        r"""
        :param _ParamKey: Parameter name.

        :type ParamKey: str
        :param _ParamValue: Parameter definition.
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""Parameter name.

        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""Parameter definition.
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    r"""Parameters

    """

    def __init__(self):
        r"""
        :param _ParamKey: Parameter name.
        :type ParamKey: str
        :param _ParamValue: Parameter value.
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""Parameter value.
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParentDependencyConfigPage(AbstractModel):
    r"""Query job upstream dependency details pagination.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results


        :type TotalCount: int
        :param _TotalPageNumber: Total pages


        :type TotalPageNumber: int
        :param _PageNumber: Page number.


        :type PageNumber: int
        :param _PageSize: Pagination size.


        :type PageSize: int
        :param _Items: Paging data

        :type Items: list of OpsTaskDepend
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""Total number of results


        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages


        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""Page number.


        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.


        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""Paging data

        :rtype: list of OpsTaskDepend
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OpsTaskDepend()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOpsTasksAsyncRequest(AbstractModel):
    r"""PauseOpsTasksAsync request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _TaskIds: Task Id list. specifies the list of task ids.
        :type TaskIds: list of str
        :param _KillInstance: Whether required to terminate the generated instance.
        :type KillInstance: bool
        """
        self._ProjectId = None
        self._TaskIds = None
        self._KillInstance = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""Task Id list. specifies the list of task ids.
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def KillInstance(self):
        r"""Whether required to terminate the generated instance.
        :rtype: bool
        """
        return self._KillInstance

    @KillInstance.setter
    def KillInstance(self, KillInstance):
        self._KillInstance = KillInstance


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._KillInstance = params.get("KillInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOpsTasksAsyncResponse(AbstractModel):
    r"""PauseOpsTasksAsync response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Asynchronous operation result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Asynchronous operation result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ProjectInstanceStatisticsAlarmInfo(AbstractModel):
    r"""Alarm rule project fluctuation rate Alarm configuration information.

    """

    def __init__(self):
        r"""
        :param _AlarmType: Alarm type

projectFailureInstanceUpwardFluctuationAlarm: specifies the upward fluctuation alert for failed instances.

projectSuccessInstanceDownwardFluctuationAlarm: specifies the downward fluctuation alert for successful instances.
        :type AlarmType: str
        :param _InstanceThresholdCountPercent: Alarm threshold for the downward fluctuation ratio of the number of successful instances.
Alarm threshold for the upward fluctuation ratio of the number of failed instances.
        :type InstanceThresholdCountPercent: int
        :param _InstanceThresholdCount: Cumulative instance number fluctuation threshold.
        :type InstanceThresholdCount: int
        :param _StabilizeThreshold: Stability threshold count (debounce configuration statistical cycle count).
        :type StabilizeThreshold: int
        :param _StabilizeStatisticsCycle: Stability statistical cycle (anti-shake configuration statistical cycle count).
        :type StabilizeStatisticsCycle: int
        :param _IsCumulant: Specifies whether to use cumulative calculation. valid values: false (consecutive), true (cumulative).
        :type IsCumulant: bool
        :param _InstanceCount: Cumulative number of instances for the current day.
Specifies the downward fluctuation of failed instance count on the day.
        :type InstanceCount: int
        """
        self._AlarmType = None
        self._InstanceThresholdCountPercent = None
        self._InstanceThresholdCount = None
        self._StabilizeThreshold = None
        self._StabilizeStatisticsCycle = None
        self._IsCumulant = None
        self._InstanceCount = None

    @property
    def AlarmType(self):
        r"""Alarm type

projectFailureInstanceUpwardFluctuationAlarm: specifies the upward fluctuation alert for failed instances.

projectSuccessInstanceDownwardFluctuationAlarm: specifies the downward fluctuation alert for successful instances.
        :rtype: str
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def InstanceThresholdCountPercent(self):
        r"""Alarm threshold for the downward fluctuation ratio of the number of successful instances.
Alarm threshold for the upward fluctuation ratio of the number of failed instances.
        :rtype: int
        """
        return self._InstanceThresholdCountPercent

    @InstanceThresholdCountPercent.setter
    def InstanceThresholdCountPercent(self, InstanceThresholdCountPercent):
        self._InstanceThresholdCountPercent = InstanceThresholdCountPercent

    @property
    def InstanceThresholdCount(self):
        r"""Cumulative instance number fluctuation threshold.
        :rtype: int
        """
        return self._InstanceThresholdCount

    @InstanceThresholdCount.setter
    def InstanceThresholdCount(self, InstanceThresholdCount):
        self._InstanceThresholdCount = InstanceThresholdCount

    @property
    def StabilizeThreshold(self):
        r"""Stability threshold count (debounce configuration statistical cycle count).
        :rtype: int
        """
        return self._StabilizeThreshold

    @StabilizeThreshold.setter
    def StabilizeThreshold(self, StabilizeThreshold):
        self._StabilizeThreshold = StabilizeThreshold

    @property
    def StabilizeStatisticsCycle(self):
        r"""Stability statistical cycle (anti-shake configuration statistical cycle count).
        :rtype: int
        """
        return self._StabilizeStatisticsCycle

    @StabilizeStatisticsCycle.setter
    def StabilizeStatisticsCycle(self, StabilizeStatisticsCycle):
        self._StabilizeStatisticsCycle = StabilizeStatisticsCycle

    @property
    def IsCumulant(self):
        r"""Specifies whether to use cumulative calculation. valid values: false (consecutive), true (cumulative).
        :rtype: bool
        """
        return self._IsCumulant

    @IsCumulant.setter
    def IsCumulant(self, IsCumulant):
        self._IsCumulant = IsCumulant

    @property
    def InstanceCount(self):
        r"""Cumulative number of instances for the current day.
Specifies the downward fluctuation of failed instance count on the day.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._InstanceThresholdCountPercent = params.get("InstanceThresholdCountPercent")
        self._InstanceThresholdCount = params.get("InstanceThresholdCount")
        self._StabilizeThreshold = params.get("StabilizeThreshold")
        self._StabilizeStatisticsCycle = params.get("StabilizeStatisticsCycle")
        self._IsCumulant = params.get("IsCumulant")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconciliationStrategyInfo(AbstractModel):
    r"""Offline integration reconciliation Alarm rule.

    """

    def __init__(self):
        r"""
        :param _RuleType: Offline Integration Task Reconciliation Alarms

reconciliationFailure: Alarm when offline reconciliation task fails

reconciliationOvertime: Alarm when offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :type RuleType: str
        :param _MismatchCount: Reconciliation Mismatch Threshold - Required when RuleType = reconciliationMismatch. Specifies the threshold for the number of mismatched records in reconciliation. No default value.
        :type MismatchCount: int
        :param _Hour: Task run timeout threshold for reconciliation: hr, defaults to 0.
        :type Hour: int
        :param _Min: Reconciliation task timeout threshold: minutes, defaults to 1.
        :type Min: int
        """
        self._RuleType = None
        self._MismatchCount = None
        self._Hour = None
        self._Min = None

    @property
    def RuleType(self):
        r"""Offline Integration Task Reconciliation Alarms

reconciliationFailure: Alarm when offline reconciliation task fails

reconciliationOvertime: Alarm when offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def MismatchCount(self):
        r"""Reconciliation Mismatch Threshold - Required when RuleType = reconciliationMismatch. Specifies the threshold for the number of mismatched records in reconciliation. No default value.
        :rtype: int
        """
        return self._MismatchCount

    @MismatchCount.setter
    def MismatchCount(self, MismatchCount):
        self._MismatchCount = MismatchCount

    @property
    def Hour(self):
        r"""Task run timeout threshold for reconciliation: hr, defaults to 0.
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Min(self):
        r"""Reconciliation task timeout threshold: minutes, defaults to 1.
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._MismatchCount = params.get("MismatchCount")
        self._Hour = params.get("Hour")
        self._Min = params.get("Min")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunTaskInstancesAsyncRequest(AbstractModel):
    r"""RerunTaskInstancesAsync request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _InstanceKeyList: Instance id list. obtain from ListInstances.
        :type InstanceKeyList: list of str
        :param _RerunType: Rerun type. valid values: 1 (self), 3 (child), 2 (self and child). default: 1.
        :type RerunType: str
        :param _CheckParentType: Whether to check upstream tasks: ALL (ALL), MAKE_SCOPE (select), NONE (do not check). default is NONE.
        :type CheckParentType: str
        :param _SonRangeType: Downstream Instance Scope

* WORKFLOW: Within the current workflow (default)

* PROJECT: Within the current project

* ALL: Across all projects with cross-workflow dependencies
        :type SonRangeType: str
        :param _SkipEventListening: Specifies whether to ignore event monitoring when rerunning.
        :type SkipEventListening: bool
        :param _RedefineParallelNum: Specifies the degree of concurrency for a custom instance run. if not configured, use the existing self-dependent task.
        :type RedefineParallelNum: int
        :param _RedefineSelfWorkflowDependency: Custom workflow self-dependency. valid values: yes (enable), no (disable). if not configured, use the existing workflow self-dependency.
        :type RedefineSelfWorkflowDependency: str
        :param _RedefineParamList: Rerun instance custom parameter.
        :type RedefineParamList: :class:`tencentcloud.wedata.v20250806.models.KVMap`
        """
        self._ProjectId = None
        self._InstanceKeyList = None
        self._RerunType = None
        self._CheckParentType = None
        self._SonRangeType = None
        self._SkipEventListening = None
        self._RedefineParallelNum = None
        self._RedefineSelfWorkflowDependency = None
        self._RedefineParamList = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""Instance id list. obtain from ListInstances.
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList

    @property
    def RerunType(self):
        r"""Rerun type. valid values: 1 (self), 3 (child), 2 (self and child). default: 1.
        :rtype: str
        """
        return self._RerunType

    @RerunType.setter
    def RerunType(self, RerunType):
        self._RerunType = RerunType

    @property
    def CheckParentType(self):
        r"""Whether to check upstream tasks: ALL (ALL), MAKE_SCOPE (select), NONE (do not check). default is NONE.
        :rtype: str
        """
        return self._CheckParentType

    @CheckParentType.setter
    def CheckParentType(self, CheckParentType):
        self._CheckParentType = CheckParentType

    @property
    def SonRangeType(self):
        r"""Downstream Instance Scope

* WORKFLOW: Within the current workflow (default)

* PROJECT: Within the current project

* ALL: Across all projects with cross-workflow dependencies
        :rtype: str
        """
        return self._SonRangeType

    @SonRangeType.setter
    def SonRangeType(self, SonRangeType):
        self._SonRangeType = SonRangeType

    @property
    def SkipEventListening(self):
        r"""Specifies whether to ignore event monitoring when rerunning.
        :rtype: bool
        """
        return self._SkipEventListening

    @SkipEventListening.setter
    def SkipEventListening(self, SkipEventListening):
        self._SkipEventListening = SkipEventListening

    @property
    def RedefineParallelNum(self):
        r"""Specifies the degree of concurrency for a custom instance run. if not configured, use the existing self-dependent task.
        :rtype: int
        """
        return self._RedefineParallelNum

    @RedefineParallelNum.setter
    def RedefineParallelNum(self, RedefineParallelNum):
        self._RedefineParallelNum = RedefineParallelNum

    @property
    def RedefineSelfWorkflowDependency(self):
        r"""Custom workflow self-dependency. valid values: yes (enable), no (disable). if not configured, use the existing workflow self-dependency.
        :rtype: str
        """
        return self._RedefineSelfWorkflowDependency

    @RedefineSelfWorkflowDependency.setter
    def RedefineSelfWorkflowDependency(self, RedefineSelfWorkflowDependency):
        self._RedefineSelfWorkflowDependency = RedefineSelfWorkflowDependency

    @property
    def RedefineParamList(self):
        r"""Rerun instance custom parameter.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.KVMap`
        """
        return self._RedefineParamList

    @RedefineParamList.setter
    def RedefineParamList(self, RedefineParamList):
        self._RedefineParamList = RedefineParamList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        self._RerunType = params.get("RerunType")
        self._CheckParentType = params.get("CheckParentType")
        self._SonRangeType = params.get("SonRangeType")
        self._SkipEventListening = params.get("SkipEventListening")
        self._RedefineParallelNum = params.get("RedefineParallelNum")
        self._RedefineSelfWorkflowDependency = params.get("RedefineSelfWorkflowDependency")
        if params.get("RedefineParamList") is not None:
            self._RedefineParamList = KVMap()
            self._RedefineParamList._deserialize(params.get("RedefineParamList"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerunTaskInstancesAsyncResponse(AbstractModel):
    r"""RerunTaskInstancesAsync response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Asynchronous ID returned by the batch rerun operation. You can use the GetAsyncJob API to retrieve detailed execution information.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Asynchronous ID returned by the batch rerun operation. You can use the GetAsyncJob API to retrieve detailed execution information.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ResourceFile(AbstractModel):
    r"""Resource file details.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ResourceId: Resource file ID.
        :type ResourceId: str
        :param _ResourceName: Resource file name.
        :type ResourceName: str
        :param _LocalPath: Source file path.
        :type LocalPath: str
        :param _RemotePath: Specifies the COS storage path of the resource object.
        :type RemotePath: str
        :param _FileExtensionType: Specifies the resource file type.

        :type FileExtensionType: str
        :param _Size: Resource size
        :type Size: str
        :param _CreatorUserUin: Creator user ID 
        :type CreatorUserUin: str
        :param _CreatorUserName: Creator name
        :type CreatorUserName: str
        :param _UpdateUserName: Last updated username.

        :type UpdateUserName: str
        :param _UpdateUserUin: Last updated user ID.

        :type UpdateUserUin: str
        :param _BucketName: COS bucket.
        :type BucketName: str
        :param _CosRegion: COS region
        :type CosRegion: str
        :param _ResourceSourceMode: Specifies the resource source mode.
        :type ResourceSourceMode: str
        :param _BundleId: Local project ID.

        :type BundleId: str
        :param _BundleInfo: Local project information.

        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceId = None
        self._ResourceName = None
        self._LocalPath = None
        self._RemotePath = None
        self._FileExtensionType = None
        self._Size = None
        self._CreatorUserUin = None
        self._CreatorUserName = None
        self._UpdateUserName = None
        self._UpdateUserUin = None
        self._BucketName = None
        self._CosRegion = None
        self._ResourceSourceMode = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""Resource file ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Resource file name.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def LocalPath(self):
        r"""Source file path.
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        r"""Specifies the COS storage path of the resource object.
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def FileExtensionType(self):
        r"""Specifies the resource file type.

        :rtype: str
        """
        return self._FileExtensionType

    @FileExtensionType.setter
    def FileExtensionType(self, FileExtensionType):
        self._FileExtensionType = FileExtensionType

    @property
    def Size(self):
        r"""Resource size
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def CreatorUserUin(self):
        r"""Creator user ID 
        :rtype: str
        """
        return self._CreatorUserUin

    @CreatorUserUin.setter
    def CreatorUserUin(self, CreatorUserUin):
        self._CreatorUserUin = CreatorUserUin

    @property
    def CreatorUserName(self):
        r"""Creator name
        :rtype: str
        """
        return self._CreatorUserName

    @CreatorUserName.setter
    def CreatorUserName(self, CreatorUserName):
        self._CreatorUserName = CreatorUserName

    @property
    def UpdateUserName(self):
        r"""Last updated username.

        :rtype: str
        """
        return self._UpdateUserName

    @UpdateUserName.setter
    def UpdateUserName(self, UpdateUserName):
        self._UpdateUserName = UpdateUserName

    @property
    def UpdateUserUin(self):
        r"""Last updated user ID.

        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def BucketName(self):
        r"""COS bucket.
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def CosRegion(self):
        r"""COS region
        :rtype: str
        """
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def ResourceSourceMode(self):
        r"""Specifies the resource source mode.
        :rtype: str
        """
        return self._ResourceSourceMode

    @ResourceSourceMode.setter
    def ResourceSourceMode(self, ResourceSourceMode):
        self._ResourceSourceMode = ResourceSourceMode

    @property
    def BundleId(self):
        r"""Local project ID.

        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Local project information.

        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._FileExtensionType = params.get("FileExtensionType")
        self._Size = params.get("Size")
        self._CreatorUserUin = params.get("CreatorUserUin")
        self._CreatorUserName = params.get("CreatorUserName")
        self._UpdateUserName = params.get("UpdateUserName")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._BucketName = params.get("BucketName")
        self._CosRegion = params.get("CosRegion")
        self._ResourceSourceMode = params.get("ResourceSourceMode")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFileItem(AbstractModel):
    r"""Retrieve the resource file list item.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Resource file ID.
        :type ResourceId: str
        :param _ResourceName: Resource file name.
        :type ResourceName: str
        :param _FileExtensionType: Specifies the resource file type.
        :type FileExtensionType: str
        :param _LocalPath: Resource path
        :type LocalPath: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._FileExtensionType = None
        self._LocalPath = None

    @property
    def ResourceId(self):
        r"""Resource file ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        r"""Resource file name.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def FileExtensionType(self):
        r"""Specifies the resource file type.
        :rtype: str
        """
        return self._FileExtensionType

    @FileExtensionType.setter
    def FileExtensionType(self, FileExtensionType):
        self._FileExtensionType = FileExtensionType

    @property
    def LocalPath(self):
        r"""Resource path
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._FileExtensionType = params.get("FileExtensionType")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFilePage(AbstractModel):
    r"""Resource file pagination.

    """

    def __init__(self):
        r"""
        :param _Items: Task collection information.
        :type Items: list of ResourceFileItem
        :param _TotalPageNumber: Total page number
        :type TotalPageNumber: int
        :param _TotalCount: Total file count.
        :type TotalCount: int
        :param _PageNumber: Current Page number

        :type PageNumber: int
        :param _PageSize: Items per Page
        :type PageSize: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Items(self):
        r"""Task collection information.
        :rtype: list of ResourceFileItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""Total page number
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""Total file count.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        r"""Current Page number

        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Items per Page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceFileItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFolder(AbstractModel):
    r"""Resource folder details.

    """

    def __init__(self):
        r"""
        :param _FolderId: Resource folder ID.
        :type FolderId: str
        :param _CreateUserUin: Creator ID.
        :type CreateUserUin: str
        :param _CreateUserName: Creator's name.
        :type CreateUserName: str
        :param _FolderPath: Specifies the folder path.
        :type FolderPath: str
        :param _FolderName: Folder name.
        :type FolderName: str
        """
        self._FolderId = None
        self._CreateUserUin = None
        self._CreateUserName = None
        self._FolderPath = None
        self._FolderName = None

    @property
    def FolderId(self):
        r"""Resource folder ID.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def CreateUserUin(self):
        r"""Creator ID.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def CreateUserName(self):
        r"""Creator's name.
        :rtype: str
        """
        return self._CreateUserName

    @CreateUserName.setter
    def CreateUserName(self, CreateUserName):
        self._CreateUserName = CreateUserName

    @property
    def FolderPath(self):
        r"""Specifies the folder path.
        :rtype: str
        """
        return self._FolderPath

    @FolderPath.setter
    def FolderPath(self, FolderPath):
        self._FolderPath = FolderPath

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._CreateUserUin = params.get("CreateUserUin")
        self._CreateUserName = params.get("CreateUserName")
        self._FolderPath = params.get("FolderPath")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFolderPage(AbstractModel):
    r"""Paginate resource folders.

    """

    def __init__(self):
        r"""
        :param _Items: Resource folder collection information.
        :type Items: list of ResourceFolder
        :param _TotalPageNumber: Total page number.
        :type TotalPageNumber: int
        :param _TotalCount: Total resource folder count
        :type TotalCount: int
        :param _PageNumber: Current Page number
        :type PageNumber: int
        :param _PageSize: Items per Page
        :type PageSize: int
        """
        self._Items = None
        self._TotalPageNumber = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Items(self):
        r"""Resource folder collection information.
        :rtype: list of ResourceFolder
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalPageNumber(self):
        r"""Total page number.
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def TotalCount(self):
        r"""Total resource folder count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        r"""Current Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Items per Page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceFolder()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSQLScriptRequest(AbstractModel):
    r"""RunSQLScript request structure.

    """

    def __init__(self):
        r"""
        :param _ScriptId: Script id.
        :type ScriptId: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ScriptContent: Script content. executed by default if not transmitted. requires Base64 encoding if transmitted.
        :type ScriptContent: str
        :param _Params: Advanced running parameter, JSON format base64 encode.
        :type Params: str
        """
        self._ScriptId = None
        self._ProjectId = None
        self._ScriptContent = None
        self._Params = None

    @property
    def ScriptId(self):
        r"""Script id.
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptContent(self):
        r"""Script content. executed by default if not transmitted. requires Base64 encoding if transmitted.
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def Params(self):
        r"""Advanced running parameter, JSON format base64 encode.
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        self._ScriptContent = params.get("ScriptContent")
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSQLScriptResponse(AbstractModel):
    r"""RunSQLScript response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Explores data tasks.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.JobDto`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Explores data tasks.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.JobDto`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = JobDto()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SQLContentActionResult(AbstractModel):
    r"""SQL exploration file/folder operation result.

    """

    def __init__(self):
        r"""
        :param _Status: Whether the operation is successful


        :type Status: bool
        :param _FolderId: Folder ID.


        :type FolderId: str
        """
        self._Status = None
        self._FolderId = None

    @property
    def Status(self):
        r"""Whether the operation is successful


        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""Folder ID.


        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLFolderNode(AbstractModel):
    r"""SQL script file tree node.

    """

    def __init__(self):
        r"""
        :param _Id: Unique identifier


        :type Id: str
        :param _Name: Name

        :type Name: str
        :param _Type: folder type, script type.

        :type Type: str
        :param _ParentFolderPath: Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.

        :type ParentFolderPath: str
        :param _IsLeaf: Whether it is a leaf node.


        :type IsLeaf: bool
        :param _Params: Business parameters	

        :type Params: str
        :param _AccessScope: Permission scope: SHARED, PRIVATE.

        :type AccessScope: str
        :param _Path: Node path.

        :type Path: str
        :param _CreateUserUin: Creator

        :type CreateUserUin: str
        :param _NodePermission: Specifies the permission of the current user for nodes.	

        :type NodePermission: str
        :param _Children: Sub-node list

        :type Children: list of SQLFolderNode
        :param _OwnerUin: Owner of the file.

        :type OwnerUin: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._ParentFolderPath = None
        self._IsLeaf = None
        self._Params = None
        self._AccessScope = None
        self._Path = None
        self._CreateUserUin = None
        self._NodePermission = None
        self._Children = None
        self._OwnerUin = None

    @property
    def Id(self):
        r"""Unique identifier


        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Name

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""folder type, script type.

        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, such as /aaa/bbb/ccc. the path must start with a slash. use / for the root directory.

        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def IsLeaf(self):
        r"""Whether it is a leaf node.


        :rtype: bool
        """
        return self._IsLeaf

    @IsLeaf.setter
    def IsLeaf(self, IsLeaf):
        self._IsLeaf = IsLeaf

    @property
    def Params(self):
        r"""Business parameters	

        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AccessScope(self):
        r"""Permission scope: SHARED, PRIVATE.

        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""Node path.

        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def CreateUserUin(self):
        r"""Creator

        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def NodePermission(self):
        r"""Specifies the permission of the current user for nodes.	

        :rtype: str
        """
        return self._NodePermission

    @NodePermission.setter
    def NodePermission(self, NodePermission):
        self._NodePermission = NodePermission

    @property
    def Children(self):
        r"""Sub-node list

        :rtype: list of SQLFolderNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def OwnerUin(self):
        r"""Owner of the file.

        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ParentFolderPath = params.get("ParentFolderPath")
        self._IsLeaf = params.get("IsLeaf")
        self._Params = params.get("Params")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        self._CreateUserUin = params.get("CreateUserUin")
        self._NodePermission = params.get("NodePermission")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = SQLFolderNode()
                obj._deserialize(item)
                self._Children.append(obj)
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLScript(AbstractModel):
    r"""Explore data script business processing entity.

    """

    def __init__(self):
        r"""
        :param _ScriptId: Script id.

        :type ScriptId: str
        :param _ScriptName: Script name.

        :type ScriptName: str
        :param _OwnerUin: Specifies the script owner uin.

        :type OwnerUin: str
        :param _ParentFolderPath: Parent folder path, /aaa/bbb/ccc.

        :type ParentFolderPath: str
        :param _ScriptConfig: Specifies the script configuration.

        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: Specifies the script content.

        :type ScriptContent: str
        :param _UpdateUserUin: Latest operator.

        :type UpdateUserUin: str
        :param _ProjectId: Project ID.


        :type ProjectId: str
        :param _UpdateTime: Update time. format: yyyy-MM-dd hh:MM:ss.

        :type UpdateTime: str
        :param _CreateTime: Creation time. format: yyyy-MM-dd hh:MM:ss.

        :type CreateTime: str
        :param _AccessScope: Access permission: SHARED, PRIVATE.

        :type AccessScope: str
        :param _Path: Full path of the node, /aaa/bbb/ccc.ipynb, consists of the name of each node.

        :type Path: str
        """
        self._ScriptId = None
        self._ScriptName = None
        self._OwnerUin = None
        self._ParentFolderPath = None
        self._ScriptConfig = None
        self._ScriptContent = None
        self._UpdateUserUin = None
        self._ProjectId = None
        self._UpdateTime = None
        self._CreateTime = None
        self._AccessScope = None
        self._Path = None

    @property
    def ScriptId(self):
        r"""Script id.

        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ScriptName(self):
        r"""Script name.

        :rtype: str
        """
        return self._ScriptName

    @ScriptName.setter
    def ScriptName(self, ScriptName):
        self._ScriptName = ScriptName

    @property
    def OwnerUin(self):
        r"""Specifies the script owner uin.

        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ParentFolderPath(self):
        r"""Parent folder path, /aaa/bbb/ccc.

        :rtype: str
        """
        return self._ParentFolderPath

    @ParentFolderPath.setter
    def ParentFolderPath(self, ParentFolderPath):
        self._ParentFolderPath = ParentFolderPath

    @property
    def ScriptConfig(self):
        r"""Specifies the script configuration.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""Specifies the script content.

        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent

    @property
    def UpdateUserUin(self):
        r"""Latest operator.

        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def ProjectId(self):
        r"""Project ID.


        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UpdateTime(self):
        r"""Update time. format: yyyy-MM-dd hh:MM:ss.

        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""Creation time. format: yyyy-MM-dd hh:MM:ss.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.

        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope

    @property
    def Path(self):
        r"""Full path of the node, /aaa/bbb/ccc.ipynb, consists of the name of each node.

        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ScriptName = params.get("ScriptName")
        self._OwnerUin = params.get("OwnerUin")
        self._ParentFolderPath = params.get("ParentFolderPath")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._ProjectId = params.get("ProjectId")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._AccessScope = params.get("AccessScope")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLScriptConfig(AbstractModel):
    r"""Data exploration script configuration.

    """

    def __init__(self):
        r"""
        :param _DatasourceId: Data source Id.

        :type DatasourceId: str
        :param _DatasourceEnv: Specifies the data source environment.

        :type DatasourceEnv: str
        :param _ComputeResource: Computational resource.

        :type ComputeResource: str
        :param _ExecutorGroupId: Specifies the execution resource group.

        :type ExecutorGroupId: str
        :param _Params: Advanced running parameter variable replacement map-json String,String.

        :type Params: str
        :param _AdvanceConfig: Advanced setting. executes configuration parameters. map-json String,String. use Base64 encode.

        :type AdvanceConfig: str
        """
        self._DatasourceId = None
        self._DatasourceEnv = None
        self._ComputeResource = None
        self._ExecutorGroupId = None
        self._Params = None
        self._AdvanceConfig = None

    @property
    def DatasourceId(self):
        r"""Data source Id.

        :rtype: str
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def DatasourceEnv(self):
        r"""Specifies the data source environment.

        :rtype: str
        """
        return self._DatasourceEnv

    @DatasourceEnv.setter
    def DatasourceEnv(self, DatasourceEnv):
        self._DatasourceEnv = DatasourceEnv

    @property
    def ComputeResource(self):
        r"""Computational resource.

        :rtype: str
        """
        return self._ComputeResource

    @ComputeResource.setter
    def ComputeResource(self, ComputeResource):
        self._ComputeResource = ComputeResource

    @property
    def ExecutorGroupId(self):
        r"""Specifies the execution resource group.

        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def Params(self):
        r"""Advanced running parameter variable replacement map-json String,String.

        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def AdvanceConfig(self):
        r"""Advanced setting. executes configuration parameters. map-json String,String. use Base64 encode.

        :rtype: str
        """
        return self._AdvanceConfig

    @AdvanceConfig.setter
    def AdvanceConfig(self, AdvanceConfig):
        self._AdvanceConfig = AdvanceConfig


    def _deserialize(self, params):
        self._DatasourceId = params.get("DatasourceId")
        self._DatasourceEnv = params.get("DatasourceEnv")
        self._ComputeResource = params.get("ComputeResource")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._Params = params.get("Params")
        self._AdvanceConfig = params.get("AdvanceConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SQLStopResult(AbstractModel):
    r"""Disable sql execution result.

    """

    def __init__(self):
        r"""
        :param _Status: Success status


        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Success status


        :rtype: bool
        """
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
        


class SetSuccessTaskInstancesAsyncRequest(AbstractModel):
    r"""SetSuccessTaskInstancesAsync request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _InstanceKeyList: Instance id list, can be obtained from ListInstances API.
        :type InstanceKeyList: list of str
        """
        self._ProjectId = None
        self._InstanceKeyList = None

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKeyList(self):
        r"""Instance id list, can be obtained from ListInstances API.
        :rtype: list of str
        """
        return self._InstanceKeyList

    @InstanceKeyList.setter
    def InstanceKeyList(self, InstanceKeyList):
        self._InstanceKeyList = InstanceKeyList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKeyList = params.get("InstanceKeyList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSuccessTaskInstancesAsyncResponse(AbstractModel):
    r"""SetSuccessTaskInstancesAsync response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Async id of the batch successful operation. can be used in the GetAsyncJob API to query execution detail.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Async id of the batch successful operation. can be used in the GetAsyncJob API to query execution detail.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SqlCreateResult(AbstractModel):
    r"""Describes the return type of creating a data exploration script folder.

    """

    def __init__(self):
        r"""
        :param _FolderId: Folder ID
        :type FolderId: str
        """
        self._FolderId = None

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOpsTasksAsyncRequest(AbstractModel):
    r"""StopOpsTasksAsync request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _TaskIds: Task Id list. specifies the list of task ids.
        :type TaskIds: list of str
        :param _KillInstance: Specifies whether to terminate the generated instance. default value: false.
        :type KillInstance: bool
        """
        self._ProjectId = None
        self._TaskIds = None
        self._KillInstance = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""Task Id list. specifies the list of task ids.
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def KillInstance(self):
        r"""Specifies whether to terminate the generated instance. default value: false.
        :rtype: bool
        """
        return self._KillInstance

    @KillInstance.setter
    def KillInstance(self, KillInstance):
        self._KillInstance = KillInstance


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._KillInstance = params.get("KillInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOpsTasksAsyncResponse(AbstractModel):
    r"""StopOpsTasksAsync response structure.

    """

    def __init__(self):
        r"""
        :param _Data: AsyncId
        :type Data: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""AsyncId
        :rtype: :class:`tencentcloud.wedata.v20250806.models.OpsAsyncResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = OpsAsyncResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class StopSQLScriptRunRequest(AbstractModel):
    r"""StopSQLScriptRun request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Specifies the query id.
        :type JobId: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        """
        self._JobId = None
        self._ProjectId = None

    @property
    def JobId(self):
        r"""Specifies the query id.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSQLScriptRunResponse(AbstractModel):
    r"""StopSQLScriptRun response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Execution result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLStopResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Execution result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLStopResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLStopResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SubmitTaskRequest(AbstractModel):
    r"""SubmitTask request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _VersionRemark: Version remarks.
        :type VersionRemark: str
        """
        self._ProjectId = None
        self._TaskId = None
        self._VersionRemark = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def VersionRemark(self):
        r"""Version remarks.
        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        self._VersionRemark = params.get("VersionRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTaskResponse(AbstractModel):
    r"""SubmitTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Success or failure.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Success or failure.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SubmitTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SubmitTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SubmitTaskResult(AbstractModel):
    r"""Submits the result of a data development task.

    """

    def __init__(self):
        r"""
        :param _VersionId: Generated task version ID.

        :type VersionId: str
        :param _Status: Submission status.
        :type Status: bool
        """
        self._VersionId = None
        self._Status = None

    @property
    def VersionId(self):
        r"""Generated task version ID.

        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Status(self):
        r"""Submission status.
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    r"""Task object.

    """

    def __init__(self):
        r"""
        :param _TaskBaseAttribute: Describes the basic attributes of the task.
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.TaskBaseAttribute`
        :param _TaskConfiguration: Task configurations.

        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        :param _TaskSchedulerConfiguration: Specifies task scheduling configuration.

        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def TaskBaseAttribute(self):
        r"""Describes the basic attributes of the task.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""Task configurations.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""Specifies task scheduling configuration.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = TaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = TaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = TaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskBaseAttribute(AbstractModel):
    r"""Describes the basic attribute information of the task.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID

        :type TaskId: str
        :param _TaskTypeId: Specifies the task type ID.

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :type TaskTypeId: int
        :param _WorkflowId: Workflow ID.

        :type WorkflowId: str
        :param _TaskName: Task name.

        :type TaskName: str
        :param _TaskLatestVersionNo: Last save version number.

        :type TaskLatestVersionNo: str
        :param _TaskLatestSubmitVersionNo: Last submit version number.

        :type TaskLatestSubmitVersionNo: str
        :param _WorkflowName: Workflow name.


        :type WorkflowName: str
        :param _Status: Task Status:

* N: New
* Y: Scheduling
* F: Offline
* O: Paused
* T: Offlining (in the process of being taken offline)
* INVALID: Invalid

        :type Status: str
        :param _Submit: Latest submission status of the task. Specifies whether it has been submitted: true/false.
        :type Submit: bool
        :param _CreateTime: Task creation time. example: 2022-02-12 11:13:41.

        :type CreateTime: str
        :param _LastUpdateTime: Last update time. example: 2025-08-13 16:34:06.
        :type LastUpdateTime: str
        :param _LastUpdateUserName: Last Updated By (Name).
        :type LastUpdateUserName: str
        :param _LastOpsTime: Last operation time.

        :type LastOpsTime: str
        :param _LastOpsUserName: Last operator name.
        :type LastOpsUserName: str
        :param _OwnerUin: Task owner ID.
        :type OwnerUin: str
        :param _TaskDescription: Task description

        :type TaskDescription: str
        :param _UpdateUserUin: Last Updated User ID

        :type UpdateUserUin: str
        :param _CreateUserUin: Created By User ID

        :type CreateUserUin: str
        """
        self._TaskId = None
        self._TaskTypeId = None
        self._WorkflowId = None
        self._TaskName = None
        self._TaskLatestVersionNo = None
        self._TaskLatestSubmitVersionNo = None
        self._WorkflowName = None
        self._Status = None
        self._Submit = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._LastUpdateUserName = None
        self._LastOpsTime = None
        self._LastOpsUserName = None
        self._OwnerUin = None
        self._TaskDescription = None
        self._UpdateUserUin = None
        self._CreateUserUin = None

    @property
    def TaskId(self):
        r"""Task ID

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskTypeId(self):
        r"""Specifies the task type ID.

* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def WorkflowId(self):
        r"""Workflow ID.

        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def TaskName(self):
        r"""Task name.

        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskLatestVersionNo(self):
        r"""Last save version number.

        :rtype: str
        """
        return self._TaskLatestVersionNo

    @TaskLatestVersionNo.setter
    def TaskLatestVersionNo(self, TaskLatestVersionNo):
        self._TaskLatestVersionNo = TaskLatestVersionNo

    @property
    def TaskLatestSubmitVersionNo(self):
        r"""Last submit version number.

        :rtype: str
        """
        return self._TaskLatestSubmitVersionNo

    @TaskLatestSubmitVersionNo.setter
    def TaskLatestSubmitVersionNo(self, TaskLatestSubmitVersionNo):
        self._TaskLatestSubmitVersionNo = TaskLatestSubmitVersionNo

    @property
    def WorkflowName(self):
        r"""Workflow name.


        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Status(self):
        r"""Task Status:

* N: New
* Y: Scheduling
* F: Offline
* O: Paused
* T: Offlining (in the process of being taken offline)
* INVALID: Invalid

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Submit(self):
        r"""Latest submission status of the task. Specifies whether it has been submitted: true/false.
        :rtype: bool
        """
        return self._Submit

    @Submit.setter
    def Submit(self, Submit):
        self._Submit = Submit

    @property
    def CreateTime(self):
        r"""Task creation time. example: 2022-02-12 11:13:41.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""Last update time. example: 2025-08-13 16:34:06.
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def LastUpdateUserName(self):
        r"""Last Updated By (Name).
        :rtype: str
        """
        return self._LastUpdateUserName

    @LastUpdateUserName.setter
    def LastUpdateUserName(self, LastUpdateUserName):
        self._LastUpdateUserName = LastUpdateUserName

    @property
    def LastOpsTime(self):
        r"""Last operation time.

        :rtype: str
        """
        return self._LastOpsTime

    @LastOpsTime.setter
    def LastOpsTime(self, LastOpsTime):
        self._LastOpsTime = LastOpsTime

    @property
    def LastOpsUserName(self):
        r"""Last operator name.
        :rtype: str
        """
        return self._LastOpsUserName

    @LastOpsUserName.setter
    def LastOpsUserName(self, LastOpsUserName):
        self._LastOpsUserName = LastOpsUserName

    @property
    def OwnerUin(self):
        r"""Task owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""Task description

        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

    @property
    def UpdateUserUin(self):
        r"""Last Updated User ID

        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def CreateUserUin(self):
        r"""Created By User ID

        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskTypeId = params.get("TaskTypeId")
        self._WorkflowId = params.get("WorkflowId")
        self._TaskName = params.get("TaskName")
        self._TaskLatestVersionNo = params.get("TaskLatestVersionNo")
        self._TaskLatestSubmitVersionNo = params.get("TaskLatestSubmitVersionNo")
        self._WorkflowName = params.get("WorkflowName")
        self._Status = params.get("Status")
        self._Submit = params.get("Submit")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._LastUpdateUserName = params.get("LastUpdateUserName")
        self._LastOpsTime = params.get("LastOpsTime")
        self._LastOpsUserName = params.get("LastOpsUserName")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCode(AbstractModel):
    r"""Task code.

    """

    def __init__(self):
        r"""
        :param _CodeContent: Specifies the code content.
        :type CodeContent: str
        :param _CodeFileSize: Specifies the size of the code file in bytes.
        :type CodeFileSize: int
        """
        self._CodeContent = None
        self._CodeFileSize = None

    @property
    def CodeContent(self):
        r"""Specifies the code content.
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def CodeFileSize(self):
        r"""Specifies the size of the code file in bytes.
        :rtype: int
        """
        return self._CodeFileSize

    @CodeFileSize.setter
    def CodeFileSize(self, CodeFileSize):
        self._CodeFileSize = CodeFileSize


    def _deserialize(self, params):
        self._CodeContent = params.get("CodeContent")
        self._CodeFileSize = params.get("CodeFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCodeResult(AbstractModel):
    r"""Task code.

    """

    def __init__(self):
        r"""
        :param _CodeInfo: Code content.
        :type CodeInfo: str
        :param _CodeFileSize: Code file size. unit: KB.
        :type CodeFileSize: str
        """
        self._CodeInfo = None
        self._CodeFileSize = None

    @property
    def CodeInfo(self):
        r"""Code content.
        :rtype: str
        """
        return self._CodeInfo

    @CodeInfo.setter
    def CodeInfo(self, CodeInfo):
        self._CodeInfo = CodeInfo

    @property
    def CodeFileSize(self):
        r"""Code file size. unit: KB.
        :rtype: str
        """
        return self._CodeFileSize

    @CodeFileSize.setter
    def CodeFileSize(self, CodeFileSize):
        self._CodeFileSize = CodeFileSize


    def _deserialize(self, params):
        self._CodeInfo = params.get("CodeInfo")
        self._CodeFileSize = params.get("CodeFileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskConfiguration(AbstractModel):
    r"""Task configuration information.

    """

    def __init__(self):
        r"""
        :param _CodeContent: Base64 encoding of the code content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CodeContent: str
        :param _TaskExtConfigurationList: Extended attribute configuration list of the task.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskExtConfigurationList: list of TaskExtParameter
        :param _DataCluster: Cluster ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type DataCluster: str
        :param _BrokerIp: Specifies the specified running node.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BrokerIp: str
        :param _YarnQueue: Resource pool queue name. need to pass through DescribeProjectClusterQueues to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type YarnQueue: str
        :param _SourceServiceId: Source data source ID, separated by;, obtained through DescribeDataSourceWithoutInfo.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceServiceId: str
        :param _SourceServiceType: Data source type. use semicolon to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceServiceType: str
        :param _SourceServiceName: Data source name. use semicolons to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceServiceName: str
        :param _TargetServiceId: TargetTarget data source ID, separated by semicolons. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetServiceId: str
        :param _TargetServiceType: Target data source type. uses ; for separation. needs to pass through DescribeDataSourceWithoutInfo for retrieval.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetServiceType: str
        :param _TargetServiceName: Target data source name. use semicolon to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetServiceName: str
        :param _ResourceGroup: Resource group ID: need to pass through DescribeNormalSchedulerExecutorGroups to obtain ExecutorGroupId.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceGroup: str
        :param _ResourceGroupName: Resource group name: need to pass through DescribeNormalSchedulerExecutorGroups to obtain ExecutorGroupName.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceGroupName: str
        :param _TaskSchedulingParameterList: Specifies the scheduling parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskSchedulingParameterList: list of TaskSchedulingParameter
        :param _BundleId: ID used by the Bundle.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BundleId: str
        :param _BundleInfo: Bundle info.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BundleInfo: str
        """
        self._CodeContent = None
        self._TaskExtConfigurationList = None
        self._DataCluster = None
        self._BrokerIp = None
        self._YarnQueue = None
        self._SourceServiceId = None
        self._SourceServiceType = None
        self._SourceServiceName = None
        self._TargetServiceId = None
        self._TargetServiceType = None
        self._TargetServiceName = None
        self._ResourceGroup = None
        self._ResourceGroupName = None
        self._TaskSchedulingParameterList = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def CodeContent(self):
        r"""Base64 encoding of the code content.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CodeContent

    @CodeContent.setter
    def CodeContent(self, CodeContent):
        self._CodeContent = CodeContent

    @property
    def TaskExtConfigurationList(self):
        r"""Extended attribute configuration list of the task.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TaskExtParameter
        """
        return self._TaskExtConfigurationList

    @TaskExtConfigurationList.setter
    def TaskExtConfigurationList(self, TaskExtConfigurationList):
        self._TaskExtConfigurationList = TaskExtConfigurationList

    @property
    def DataCluster(self):
        r"""Cluster ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataCluster

    @DataCluster.setter
    def DataCluster(self, DataCluster):
        self._DataCluster = DataCluster

    @property
    def BrokerIp(self):
        r"""Specifies the specified running node.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BrokerIp

    @BrokerIp.setter
    def BrokerIp(self, BrokerIp):
        self._BrokerIp = BrokerIp

    @property
    def YarnQueue(self):
        r"""Resource pool queue name. need to pass through DescribeProjectClusterQueues to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._YarnQueue

    @YarnQueue.setter
    def YarnQueue(self, YarnQueue):
        self._YarnQueue = YarnQueue

    @property
    def SourceServiceId(self):
        r"""Source data source ID, separated by;, obtained through DescribeDataSourceWithoutInfo.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceServiceId

    @SourceServiceId.setter
    def SourceServiceId(self, SourceServiceId):
        self._SourceServiceId = SourceServiceId

    @property
    def SourceServiceType(self):
        r"""Data source type. use semicolon to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceServiceType

    @SourceServiceType.setter
    def SourceServiceType(self, SourceServiceType):
        self._SourceServiceType = SourceServiceType

    @property
    def SourceServiceName(self):
        r"""Data source name. use semicolons to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceServiceName

    @SourceServiceName.setter
    def SourceServiceName(self, SourceServiceName):
        self._SourceServiceName = SourceServiceName

    @property
    def TargetServiceId(self):
        r"""TargetTarget data source ID, separated by semicolons. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetServiceId

    @TargetServiceId.setter
    def TargetServiceId(self, TargetServiceId):
        self._TargetServiceId = TargetServiceId

    @property
    def TargetServiceType(self):
        r"""Target data source type. uses ; for separation. needs to pass through DescribeDataSourceWithoutInfo for retrieval.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetServiceType

    @TargetServiceType.setter
    def TargetServiceType(self, TargetServiceType):
        self._TargetServiceType = TargetServiceType

    @property
    def TargetServiceName(self):
        r"""Target data source name. use semicolon to separate. need to pass through DescribeDataSourceWithoutInfo to obtain.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetServiceName

    @TargetServiceName.setter
    def TargetServiceName(self, TargetServiceName):
        self._TargetServiceName = TargetServiceName

    @property
    def ResourceGroup(self):
        r"""Resource group ID: need to pass through DescribeNormalSchedulerExecutorGroups to obtain ExecutorGroupId.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceGroup

    @ResourceGroup.setter
    def ResourceGroup(self, ResourceGroup):
        self._ResourceGroup = ResourceGroup

    @property
    def ResourceGroupName(self):
        r"""Resource group name: need to pass through DescribeNormalSchedulerExecutorGroups to obtain ExecutorGroupName.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def TaskSchedulingParameterList(self):
        r"""Specifies the scheduling parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TaskSchedulingParameter
        """
        return self._TaskSchedulingParameterList

    @TaskSchedulingParameterList.setter
    def TaskSchedulingParameterList(self, TaskSchedulingParameterList):
        self._TaskSchedulingParameterList = TaskSchedulingParameterList

    @property
    def BundleId(self):
        r"""ID used by the Bundle.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle info.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._CodeContent = params.get("CodeContent")
        if params.get("TaskExtConfigurationList") is not None:
            self._TaskExtConfigurationList = []
            for item in params.get("TaskExtConfigurationList"):
                obj = TaskExtParameter()
                obj._deserialize(item)
                self._TaskExtConfigurationList.append(obj)
        self._DataCluster = params.get("DataCluster")
        self._BrokerIp = params.get("BrokerIp")
        self._YarnQueue = params.get("YarnQueue")
        self._SourceServiceId = params.get("SourceServiceId")
        self._SourceServiceType = params.get("SourceServiceType")
        self._SourceServiceName = params.get("SourceServiceName")
        self._TargetServiceId = params.get("TargetServiceId")
        self._TargetServiceType = params.get("TargetServiceType")
        self._TargetServiceName = params.get("TargetServiceName")
        self._ResourceGroup = params.get("ResourceGroup")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("TaskSchedulingParameterList") is not None:
            self._TaskSchedulingParameterList = []
            for item in params.get("TaskSchedulingParameterList"):
                obj = TaskSchedulingParameter()
                obj._deserialize(item)
                self._TaskSchedulingParameterList.append(obj)
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDataRegistry(AbstractModel):
    r"""Task data registration item.

    """

    def __init__(self):
        r"""
        :param _DatasourceId: Data source ID.
        :type DatasourceId: str
        :param _DatabaseName: Database name.

        :type DatabaseName: str
        :param _TableName: Table name

        :type TableName: str
        :param _PartitionName: Partition name

        :type PartitionName: str
        :param _DataFlowType: Input output table data type.
Input stream:
 UPSTREAM,
Output stream:
  DOWNSTREAM;.
        :type DataFlowType: str
        :param _TablePhysicalId: Physical unique ID..
        :type TablePhysicalId: str
        :param _DbGuid: Database unique id..
        :type DbGuid: str
        :param _TableGuid: Unique id of the table.
        :type TableGuid: str
        """
        self._DatasourceId = None
        self._DatabaseName = None
        self._TableName = None
        self._PartitionName = None
        self._DataFlowType = None
        self._TablePhysicalId = None
        self._DbGuid = None
        self._TableGuid = None

    @property
    def DatasourceId(self):
        r"""Data source ID.
        :rtype: str
        """
        return self._DatasourceId

    @DatasourceId.setter
    def DatasourceId(self, DatasourceId):
        self._DatasourceId = DatasourceId

    @property
    def DatabaseName(self):
        r"""Database name.

        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableName(self):
        r"""Table name

        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def PartitionName(self):
        r"""Partition name

        :rtype: str
        """
        return self._PartitionName

    @PartitionName.setter
    def PartitionName(self, PartitionName):
        self._PartitionName = PartitionName

    @property
    def DataFlowType(self):
        r"""Input output table data type.
Input stream:
 UPSTREAM,
Output stream:
  DOWNSTREAM;.
        :rtype: str
        """
        return self._DataFlowType

    @DataFlowType.setter
    def DataFlowType(self, DataFlowType):
        self._DataFlowType = DataFlowType

    @property
    def TablePhysicalId(self):
        r"""Physical unique ID..
        :rtype: str
        """
        return self._TablePhysicalId

    @TablePhysicalId.setter
    def TablePhysicalId(self, TablePhysicalId):
        self._TablePhysicalId = TablePhysicalId

    @property
    def DbGuid(self):
        r"""Database unique id..
        :rtype: str
        """
        return self._DbGuid

    @DbGuid.setter
    def DbGuid(self, DbGuid):
        self._DbGuid = DbGuid

    @property
    def TableGuid(self):
        r"""Unique id of the table.
        :rtype: str
        """
        return self._TableGuid

    @TableGuid.setter
    def TableGuid(self, TableGuid):
        self._TableGuid = TableGuid


    def _deserialize(self, params):
        self._DatasourceId = params.get("DatasourceId")
        self._DatabaseName = params.get("DatabaseName")
        self._TableName = params.get("TableName")
        self._PartitionName = params.get("PartitionName")
        self._DataFlowType = params.get("DataFlowType")
        self._TablePhysicalId = params.get("TablePhysicalId")
        self._DbGuid = params.get("DbGuid")
        self._TableGuid = params.get("TableGuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDependDto(AbstractModel):
    r"""Describes the dependency task information.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID

        :type TaskId: str
        :param _TaskName: Task name.

        :type TaskName: str
        :param _WorkflowId: Workflow id.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.

        :type WorkflowName: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _Status: Task Status:

* N: New

* Y: Scheduling

* F: Offline

* O: Paused

* T: Offlining (in the process of being taken offline)

I* NVALID: Invalid
        :type Status: str
        :param _TaskTypeId: Task type id.
        :type TaskTypeId: int
        :param _TaskTypeDesc: Task type description.
-20 : universal data synchronization.
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
-130: branch.
-131: merge.
-132: Notebook 
-133: SSH node.
 - 134 :  StarRocks
 - 137 :  For-each
-10000 : custom business common.
        :type TaskTypeDesc: str
        :param _ScheduleDesc: Specifies scheduling plan display description information.

        :type ScheduleDesc: str
        :param _StartTime: Task start time.
        :type StartTime: str
        :param _EndTime: Task end time.
        :type EndTime: str
        :param _DelayTime: Delay time.
        :type DelayTime: int
        :param _CycleType: Cycle Type, Default: D
Supported types:
* O: One-time

* Y: Yearly

* M: Monthly

* W: Weekly

* D: Daily

* H: Hourly

* I: Minute

* C: Crontab expression type
        :type CycleType: str
        :param _OwnerUin: Owner ID
        :type OwnerUin: str
        :param _TaskAction: Elastic cycle configuration.
        :type TaskAction: str
        :param _InitStrategy: Initialization strategy for scheduling.
        :type InitStrategy: str
        :param _CrontabExpression: crontab expression.
        :type CrontabExpression: str
        """
        self._TaskId = None
        self._TaskName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._Status = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._ScheduleDesc = None
        self._StartTime = None
        self._EndTime = None
        self._DelayTime = None
        self._CycleType = None
        self._OwnerUin = None
        self._TaskAction = None
        self._InitStrategy = None
        self._CrontabExpression = None

    @property
    def TaskId(self):
        r"""Task ID

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.

        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WorkflowId(self):
        r"""Workflow id.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.

        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""Task Status:

* N: New

* Y: Scheduling

* F: Offline

* O: Paused

* T: Offlining (in the process of being taken offline)

I* NVALID: Invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskTypeId(self):
        r"""Task type id.
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""Task type description.
-20 : universal data synchronization.
 - 25 :  ETLTaskType
 - 26 :  ETLTaskType
 - 30 :  python
 - 31 :  pyspark
 - 34 :  hivesql
 - 35 :  shell
 - 36 :  sparksql
 - 21 :  jdbcsql
 - 32 :  dlc
 - 33 :  ImpalaTaskType
 - 40 :  CDWTaskType
 - 41 :  kettle
 - 42 :  TCHouse-X
 - 43 :  TCHouse-X SQL
 - 46 :  dlcsparkTaskType
 - 47 :  TiOneMachineLearningTaskType
 - 48 :  Trino
 - 50 :  DLCPyspark
 - 23 :  TencentDistributedSQL
 - 39 :  spark
 - 92 :  MRTaskType
 - 38 :  ShellScript
 - 70 :  HiveSQLScrip
-130: branch.
-131: merge.
-132: Notebook 
-133: SSH node.
 - 134 :  StarRocks
 - 137 :  For-each
-10000 : custom business common.
        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def ScheduleDesc(self):
        r"""Specifies scheduling plan display description information.

        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def StartTime(self):
        r"""Task start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Task end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DelayTime(self):
        r"""Delay time.
        :rtype: int
        """
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def CycleType(self):
        r"""Cycle Type, Default: D
Supported types:
* O: One-time

* Y: Yearly

* M: Monthly

* W: Weekly

* D: Daily

* H: Hourly

* I: Minute

* C: Crontab expression type
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def OwnerUin(self):
        r"""Owner ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskAction(self):
        r"""Elastic cycle configuration.
        :rtype: str
        """
        return self._TaskAction

    @TaskAction.setter
    def TaskAction(self, TaskAction):
        self._TaskAction = TaskAction

    @property
    def InitStrategy(self):
        r"""Initialization strategy for scheduling.
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy

    @property
    def CrontabExpression(self):
        r"""crontab expression.
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DelayTime = params.get("DelayTime")
        self._CycleType = params.get("CycleType")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskAction = params.get("TaskAction")
        self._InitStrategy = params.get("InitStrategy")
        self._CrontabExpression = params.get("CrontabExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskExtParameter(AbstractModel):
    r"""Task extension information parameter.

    """

    def __init__(self):
        r"""
        :param _ParamKey: Parameter name.


        :type ParamKey: str
        :param _ParamValue: Parameter value.


        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""Parameter name.


        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""Parameter value.


        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstance(AbstractModel):
    r"""Scheduling task instance entity.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project id.
        :type ProjectId: str
        :param _InstanceKey: **Instance unique id**.
        :type InstanceKey: str
        :param _FolderId: Folder ID.

        :type FolderId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.

        :type WorkflowName: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskName: Task name.

        :type TaskName: str
        :param _CurRunDate: Instance data time.
        :type CurRunDate: str
        :param _InstanceState: **Instance status**.
-WAIT_EVENT: specifies the wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
- RUNNING: indicates the instance is RUNNING.
- SKIP_RUNNING: SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
- EXPIRED: failed.
-COMPLETED: success.
        :type InstanceState: str
        :param _InstanceType: Specifies the instance type.

-0 indicates the supplementary entry type.
-Indicates a periodic instance.
-2 indicates a non-periodic instance.
        :type InstanceType: int
        :param _OwnerUinList: Owner Uin list.
        :type OwnerUinList: list of str
        :param _TotalRunNum: Cumulative running times.

        :type TotalRunNum: int
        :param _TaskType: Task type description.
        :type TaskType: str
        :param _TaskTypeId: Task type id.

        :type TaskTypeId: int
        :param _CycleType: Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _TryLimit: Retry count limit when execution fails each time.

        :type TryLimit: int
        :param _Tries: Specifies the number of retry attempts on failure.
When triggered by manual rerun, supplementary entry instance, or other methods, the count will be reset to 0 and start again.
        :type Tries: int
        :param _StartTime: Operation start time.
        :type StartTime: str
        :param _EndTime: Operation completion time.
        :type EndTime: str
        :param _CostTime: Time spent, in milliseconds.

        :type CostTime: int
        :param _SchedulerTime: Scheduled dispatch time.

        :type SchedulerTime: str
        :param _LastUpdateTime: Latest update time of the instance. specifies the time format as yyyy-MM-dd HH:MM:ss.

        :type LastUpdateTime: str
        :param _ExecutorGroupId: Execution resource group ID.

        :type ExecutorGroupId: str
        :param _ExecutorGroupName: Resource group name.

        :type ExecutorGroupName: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._TaskId = None
        self._TaskName = None
        self._CurRunDate = None
        self._InstanceState = None
        self._InstanceType = None
        self._OwnerUinList = None
        self._TotalRunNum = None
        self._TaskType = None
        self._TaskTypeId = None
        self._CycleType = None
        self._TryLimit = None
        self._Tries = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._SchedulerTime = None
        self._LastUpdateTime = None
        self._ExecutorGroupId = None
        self._ExecutorGroupName = None

    @property
    def ProjectId(self):
        r"""Project id.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**Instance unique id**.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def FolderId(self):
        r"""Folder ID.

        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.

        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.

        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def CurRunDate(self):
        r"""Instance data time.
        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def InstanceState(self):
        r"""**Instance status**.
-WAIT_EVENT: specifies the wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
- RUNNING: indicates the instance is RUNNING.
- SKIP_RUNNING: SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
- EXPIRED: failed.
-COMPLETED: success.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def InstanceType(self):
        r"""Specifies the instance type.

-0 indicates the supplementary entry type.
-Indicates a periodic instance.
-2 indicates a non-periodic instance.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OwnerUinList(self):
        r"""Owner Uin list.
        :rtype: list of str
        """
        return self._OwnerUinList

    @OwnerUinList.setter
    def OwnerUinList(self, OwnerUinList):
        self._OwnerUinList = OwnerUinList

    @property
    def TotalRunNum(self):
        r"""Cumulative running times.

        :rtype: int
        """
        return self._TotalRunNum

    @TotalRunNum.setter
    def TotalRunNum(self, TotalRunNum):
        self._TotalRunNum = TotalRunNum

    @property
    def TaskType(self):
        r"""Task type description.
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskTypeId(self):
        r"""Task type id.

        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def CycleType(self):
        r"""Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def TryLimit(self):
        r"""Retry count limit when execution fails each time.

        :rtype: int
        """
        return self._TryLimit

    @TryLimit.setter
    def TryLimit(self, TryLimit):
        self._TryLimit = TryLimit

    @property
    def Tries(self):
        r"""Specifies the number of retry attempts on failure.
When triggered by manual rerun, supplementary entry instance, or other methods, the count will be reset to 0 and start again.
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def StartTime(self):
        r"""Operation start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Operation completion time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CostTime(self):
        r"""Time spent, in milliseconds.

        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def SchedulerTime(self):
        r"""Scheduled dispatch time.

        :rtype: str
        """
        return self._SchedulerTime

    @SchedulerTime.setter
    def SchedulerTime(self, SchedulerTime):
        self._SchedulerTime = SchedulerTime

    @property
    def LastUpdateTime(self):
        r"""Latest update time of the instance. specifies the time format as yyyy-MM-dd HH:MM:ss.

        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def ExecutorGroupId(self):
        r"""Execution resource group ID.

        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ExecutorGroupName(self):
        r"""Resource group name.

        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._CurRunDate = params.get("CurRunDate")
        self._InstanceState = params.get("InstanceState")
        self._InstanceType = params.get("InstanceType")
        self._OwnerUinList = params.get("OwnerUinList")
        self._TotalRunNum = params.get("TotalRunNum")
        self._TaskType = params.get("TaskType")
        self._TaskTypeId = params.get("TaskTypeId")
        self._CycleType = params.get("CycleType")
        self._TryLimit = params.get("TryLimit")
        self._Tries = params.get("Tries")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._SchedulerTime = params.get("SchedulerTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceDetail(AbstractModel):
    r"""Scheduling task instance details.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Specifies the project id.

        :type ProjectId: str
        :param _InstanceKey: **Instance unique id**.

        :type InstanceKey: str
        :param _FolderId: Folder ID.


        :type FolderId: str
        :param _FolderName: Specifies the folder name.

        :type FolderName: str
        :param _WorkflowId: Workflow ID.

        :type WorkflowId: str
        :param _WorkflowName: Workflow name.


        :type WorkflowName: str
        :param _TaskId: Task ID


        :type TaskId: str
        :param _TaskName: Task name.


        :type TaskName: str
        :param _TaskTypeId: Specifies the id corresponding to taskType.
        :type TaskTypeId: int
        :param _TaskType: Task type


        :type TaskType: str
        :param _CycleType: Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _CurRunDate: Specifies the instance data time.

        :type CurRunDate: str
        :param _InstanceState: Instance status.
-WAIT_EVENT: wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
-RUNNING. specifies the running status.
- SKIP_RUNNING: specifies whether to SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
-EXPIRED: indicates a failure.
-COMPLETED: success.

        :type InstanceState: str
        :param _InstanceType: Specifies the instance type.

-0 indicates the replenishment type.
-Indicates a periodic instance.
-2 indicates a non-periodic instance.

        :type InstanceType: int
        :param _OwnerUinList: owner uin list.


        :type OwnerUinList: list of str
        :param _TotalRunNum: Cumulative running times.

        :type TotalRunNum: int
        :param _TryLimit: Retry count limit when execution fails each time.

        :type TryLimit: int
        :param _Tries: **Failure Retry Count** - The number of retry attempts after a failure. When the instance is triggered again through methods such as manual rerun or backfill, this counter is reset to 0 and starts counting again.
        :type Tries: int
        :param _CostTime: Time spent, in milliseconds.

        :type CostTime: int
        :param _StartTime: Start time.

        :type StartTime: str
        :param _EndTime: Operation completion time.

        :type EndTime: str
        :param _SchedulerTime: Scheduled dispatch time.

        :type SchedulerTime: str
        :param _LastUpdateTime: Latest update time of the instance. format: yyyy-MM-dd HH:MM:ss.

        :type LastUpdateTime: str
        :param _ExecutorGroupId: Execution resource group ID.

        :type ExecutorGroupId: str
        :param _ExecutorGroupName: Resource group name.

        :type ExecutorGroupName: str
        :param _JobErrorMsg: Brief task failure information.

        :type JobErrorMsg: str
        """
        self._ProjectId = None
        self._InstanceKey = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._TaskId = None
        self._TaskName = None
        self._TaskTypeId = None
        self._TaskType = None
        self._CycleType = None
        self._CurRunDate = None
        self._InstanceState = None
        self._InstanceType = None
        self._OwnerUinList = None
        self._TotalRunNum = None
        self._TryLimit = None
        self._Tries = None
        self._CostTime = None
        self._StartTime = None
        self._EndTime = None
        self._SchedulerTime = None
        self._LastUpdateTime = None
        self._ExecutorGroupId = None
        self._ExecutorGroupName = None
        self._JobErrorMsg = None

    @property
    def ProjectId(self):
        r"""Specifies the project id.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceKey(self):
        r"""**Instance unique id**.

        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def FolderId(self):
        r"""Folder ID.


        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Specifies the folder name.

        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""Workflow ID.

        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.


        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def TaskId(self):
        r"""Task ID


        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.


        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskTypeId(self):
        r"""Specifies the id corresponding to taskType.
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskType(self):
        r"""Task type


        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def CycleType(self):
        r"""Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def CurRunDate(self):
        r"""Specifies the instance data time.

        :rtype: str
        """
        return self._CurRunDate

    @CurRunDate.setter
    def CurRunDate(self, CurRunDate):
        self._CurRunDate = CurRunDate

    @property
    def InstanceState(self):
        r"""Instance status.
-WAIT_EVENT: wait for event.
-WAIT_UPSTREAM: waiting for upstream.
- WAIT_RUN: awaiting execution.
-RUNNING. specifies the running status.
- SKIP_RUNNING: specifies whether to SKIP RUNNING.
- FAILED_RETRY: RETRY on failure.
-EXPIRED: indicates a failure.
-COMPLETED: success.

        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def InstanceType(self):
        r"""Specifies the instance type.

-0 indicates the replenishment type.
-Indicates a periodic instance.
-2 indicates a non-periodic instance.

        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OwnerUinList(self):
        r"""owner uin list.


        :rtype: list of str
        """
        return self._OwnerUinList

    @OwnerUinList.setter
    def OwnerUinList(self, OwnerUinList):
        self._OwnerUinList = OwnerUinList

    @property
    def TotalRunNum(self):
        r"""Cumulative running times.

        :rtype: int
        """
        return self._TotalRunNum

    @TotalRunNum.setter
    def TotalRunNum(self, TotalRunNum):
        self._TotalRunNum = TotalRunNum

    @property
    def TryLimit(self):
        r"""Retry count limit when execution fails each time.

        :rtype: int
        """
        return self._TryLimit

    @TryLimit.setter
    def TryLimit(self, TryLimit):
        self._TryLimit = TryLimit

    @property
    def Tries(self):
        r"""**Failure Retry Count** - The number of retry attempts after a failure. When the instance is triggered again through methods such as manual rerun or backfill, this counter is reset to 0 and starts counting again.
        :rtype: int
        """
        return self._Tries

    @Tries.setter
    def Tries(self, Tries):
        self._Tries = Tries

    @property
    def CostTime(self):
        r"""Time spent, in milliseconds.

        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def StartTime(self):
        r"""Start time.

        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Operation completion time.

        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SchedulerTime(self):
        r"""Scheduled dispatch time.

        :rtype: str
        """
        return self._SchedulerTime

    @SchedulerTime.setter
    def SchedulerTime(self, SchedulerTime):
        self._SchedulerTime = SchedulerTime

    @property
    def LastUpdateTime(self):
        r"""Latest update time of the instance. format: yyyy-MM-dd HH:MM:ss.

        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def ExecutorGroupId(self):
        r"""Execution resource group ID.

        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ExecutorGroupName(self):
        r"""Resource group name.

        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName

    @property
    def JobErrorMsg(self):
        r"""Brief task failure information.

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceKey = params.get("InstanceKey")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskType = params.get("TaskType")
        self._CycleType = params.get("CycleType")
        self._CurRunDate = params.get("CurRunDate")
        self._InstanceState = params.get("InstanceState")
        self._InstanceType = params.get("InstanceType")
        self._OwnerUinList = params.get("OwnerUinList")
        self._TotalRunNum = params.get("TotalRunNum")
        self._TryLimit = params.get("TryLimit")
        self._Tries = params.get("Tries")
        self._CostTime = params.get("CostTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SchedulerTime = params.get("SchedulerTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        self._JobErrorMsg = params.get("JobErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceExecutions(AbstractModel):
    r"""Instance execution list.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _TotalPageNumber: Total pages
        :type TotalPageNumber: int
        :param _Items: Record list
        :type Items: list of InstanceExecution
        :param _PageNumber: Page number.
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""Record list
        :rtype: list of InstanceExecution
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PageNumber(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceExecution()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstancePage(AbstractModel):
    r"""Instance list pagination entity.

    """

    def __init__(self):
        r"""
        :param _TotalCount: **Total number of entries**.

        :type TotalCount: int
        :param _TotalPageNumber: **Total number of pages.**

        :type TotalPageNumber: int
        :param _PageNumber: Page number.


        :type PageNumber: int
        :param _PageSize: Specifies the number of entries per page.

        :type PageSize: int
        :param _Items: Data List


        :type Items: list of TaskInstance
        """
        self._TotalCount = None
        self._TotalPageNumber = None
        self._PageNumber = None
        self._PageSize = None
        self._Items = None

    @property
    def TotalCount(self):
        r"""**Total number of entries**.

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""**Total number of pages.**

        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def PageNumber(self):
        r"""Page number.


        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of entries per page.

        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Items(self):
        r"""Data List


        :rtype: list of TaskInstance
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TaskInstance()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOpsInfo(AbstractModel):
    r"""Describes the list details of the task operation and maintenance workflow.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _TaskName: Task name.
        :type TaskName: str
        :param _OwnerUin: Owner id

        :type OwnerUin: str
        :param _Status: Task Status

-N: New

-Y: Scheduling

-F: Offline

-O: Paused

-T: Offlining

-INVALID: Invalid
        :type Status: str
        :param _FolderId: Folder ID
        :type FolderId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        :param _WorkflowId: Workflow id.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ProjectName: Project name.
        :type ProjectName: str
        :param _UpdateUserUin: Specifies the name of the updater.
        :type UpdateUserUin: str
        :param _TaskTypeId: Task type Id.
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :type TaskTypeId: int
        :param _TaskTypeDesc: Task type description.
-Universal data synchronization.
 - ETLTaskType
 - ETLTaskType
 - python
 - pyspark
 - HiveSQLTaskType
 - shell
 - SparkSQLTaskType
 - JDBCSQLTaskType
 - DLCTaskType
 - ImpalaTaskType
 - CDWTaskType
 - kettle
 - DLCSparkTaskType
-TiOne machine learning.
 - TrinoTaskType
 - DLCPyspark
 - spark
 - mr
-Specifies the shell script.
-hivesql script.
-Specifies common custom business.

        :type TaskTypeDesc: str
        :param _CycleType: Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :type CycleType: str
        :param _ExecutorGroupId: Resource group ID

        :type ExecutorGroupId: str
        :param _ScheduleDesc: Scheduling description.

        :type ScheduleDesc: str
        :param _ExecutorGroupName: Resource group name.
        :type ExecutorGroupName: str
        :param _LastSchedulerCommitTime: Latest scheduling submission time.

        :type LastSchedulerCommitTime: str
        :param _FirstRunTime: First execution time.

        :type FirstRunTime: str
        :param _FirstSubmitTime: Most recent submission time.
        :type FirstSubmitTime: str
        :param _CreateTime: Creation time.


        :type CreateTime: str
        :param _LastUpdateTime: Latest update time.

        :type LastUpdateTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._OwnerUin = None
        self._Status = None
        self._FolderId = None
        self._FolderName = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._ProjectId = None
        self._ProjectName = None
        self._UpdateUserUin = None
        self._TaskTypeId = None
        self._TaskTypeDesc = None
        self._CycleType = None
        self._ExecutorGroupId = None
        self._ScheduleDesc = None
        self._ExecutorGroupName = None
        self._LastSchedulerCommitTime = None
        self._FirstRunTime = None
        self._FirstSubmitTime = None
        self._CreateTime = None
        self._LastUpdateTime = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def OwnerUin(self):
        r"""Owner id

        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Status(self):
        r"""Task Status

-N: New

-Y: Scheduling

-F: Offline

-O: Paused

-T: Offlining

-INVALID: Invalid
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def WorkflowId(self):
        r"""Workflow id.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""Project name.
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def UpdateUserUin(self):
        r"""Specifies the name of the updater.
        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def TaskTypeId(self):
        r"""Task type Id.
* 21:JDBC SQL
* 23:TDSQL-PostgreSQL
* 26:OfflineSynchronization
* 30:Python
* 31:PySpark
* 33:Impala
* 34:Hive SQL
* 35:Shell
* 36:Spark SQL
* 38:Shell Form Mode
* 39:Spark
* 40:TCHouse-P
* 41:Kettle
* 42:Tchouse-X
* 43:TCHouse-X SQL
* 46:DLC Spark
* 47:TiOne
* 48:Trino
* 50:DLC PySpark
* 92:MapReduce
* 130:Branch Node
* 131:Merged Node
* 132:Notebook
* 133:SSH
* 134:StarRocks
* 137:For-each
* 138:Setats SQL
        :rtype: int
        """
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeDesc(self):
        r"""Task type description.
-Universal data synchronization.
 - ETLTaskType
 - ETLTaskType
 - python
 - pyspark
 - HiveSQLTaskType
 - shell
 - SparkSQLTaskType
 - JDBCSQLTaskType
 - DLCTaskType
 - ImpalaTaskType
 - CDWTaskType
 - kettle
 - DLCSparkTaskType
-TiOne machine learning.
 - TrinoTaskType
 - DLCPyspark
 - spark
 - mr
-Specifies the shell script.
-hivesql script.
-Specifies common custom business.

        :rtype: str
        """
        return self._TaskTypeDesc

    @TaskTypeDesc.setter
    def TaskTypeDesc(self, TaskTypeDesc):
        self._TaskTypeDesc = TaskTypeDesc

    @property
    def CycleType(self):
        r"""Task Cycle Type

* ONEOFF_CYCLE: One-time

* YEAR_CYCLE: Yearly

* MONTH_CYCLE: Monthly

* WEEK_CYCLE: Weekly

* DAY_CYCLE: Daily

* HOUR_CYCLE: Hourly

* MINUTE_CYCLE: Minute-level

* CRONTAB_CYCLE: Crontab expression-based
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ExecutorGroupId(self):
        r"""Resource group ID

        :rtype: str
        """
        return self._ExecutorGroupId

    @ExecutorGroupId.setter
    def ExecutorGroupId(self, ExecutorGroupId):
        self._ExecutorGroupId = ExecutorGroupId

    @property
    def ScheduleDesc(self):
        r"""Scheduling description.

        :rtype: str
        """
        return self._ScheduleDesc

    @ScheduleDesc.setter
    def ScheduleDesc(self, ScheduleDesc):
        self._ScheduleDesc = ScheduleDesc

    @property
    def ExecutorGroupName(self):
        r"""Resource group name.
        :rtype: str
        """
        return self._ExecutorGroupName

    @ExecutorGroupName.setter
    def ExecutorGroupName(self, ExecutorGroupName):
        self._ExecutorGroupName = ExecutorGroupName

    @property
    def LastSchedulerCommitTime(self):
        r"""Latest scheduling submission time.

        :rtype: str
        """
        return self._LastSchedulerCommitTime

    @LastSchedulerCommitTime.setter
    def LastSchedulerCommitTime(self, LastSchedulerCommitTime):
        self._LastSchedulerCommitTime = LastSchedulerCommitTime

    @property
    def FirstRunTime(self):
        r"""First execution time.

        :rtype: str
        """
        return self._FirstRunTime

    @FirstRunTime.setter
    def FirstRunTime(self, FirstRunTime):
        self._FirstRunTime = FirstRunTime

    @property
    def FirstSubmitTime(self):
        r"""Most recent submission time.
        :rtype: str
        """
        return self._FirstSubmitTime

    @FirstSubmitTime.setter
    def FirstSubmitTime(self, FirstSubmitTime):
        self._FirstSubmitTime = FirstSubmitTime

    @property
    def CreateTime(self):
        r"""Creation time.


        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""Latest update time.

        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._OwnerUin = params.get("OwnerUin")
        self._Status = params.get("Status")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeDesc = params.get("TaskTypeDesc")
        self._CycleType = params.get("CycleType")
        self._ExecutorGroupId = params.get("ExecutorGroupId")
        self._ScheduleDesc = params.get("ScheduleDesc")
        self._ExecutorGroupName = params.get("ExecutorGroupName")
        self._LastSchedulerCommitTime = params.get("LastSchedulerCommitTime")
        self._FirstRunTime = params.get("FirstRunTime")
        self._FirstSubmitTime = params.get("FirstSubmitTime")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSchedulerConfiguration(AbstractModel):
    r"""Specifies task scheduling configuration info.

    """

    def __init__(self):
        r"""
        :param _CycleType: Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :type CycleType: str
        :param _ScheduleTimeZone: Time zone.
        :type ScheduleTimeZone: str
        :param _CrontabExpression: 0 2 3 1,L,2 * ?	

        :type CrontabExpression: str
        :param _StartTime: Effective date.

        :type StartTime: str
        :param _EndTime: End date

        :type EndTime: str
        :param _ExecutionStartTime: Execution time. the left-closed interval.

        :type ExecutionStartTime: str
        :param _ExecutionEndTime: Execution time. right closed interval.

        :type ExecutionEndTime: str
        :param _ScheduleRunType: Scheduling type: 0 for normal scheduling, 1 for dry-run scheduling.

        :type ScheduleRunType: int
        :param _CalendarOpen: Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :type CalendarOpen: str
        :param _CalendarId: Calendar id.
        :type CalendarId: str
        :param _CalendarName: Calendar name, which needs to be obtained from DescribeScheduleCalendarPageList API.
        :type CalendarName: str
        :param _SelfDepend: Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :type SelfDepend: str
        :param _UpstreamDependencyConfigList: Specifies the upstream dependency array.
        :type UpstreamDependencyConfigList: list of DependencyTaskBrief
        :param _DownStreamDependencyConfigList: SpecSpecifies the downstream dependency array.

        :type DownStreamDependencyConfigList: list of DependencyTaskBrief
        :param _EventListenerList: Array of Events

        :type EventListenerList: list of EventListener
        :param _RunPriority: Task scheduling priority. valid values: 4 (high), 5 (medium), 6 (low). default: 6.

        :type RunPriority: int
        :param _RetryWait: Retry policy. retry wait time in minutes. default: 5.

        :type RetryWait: int
        :param _MaxRetryAttempts: Specifies the maximum attempts of the retry policy. default: 4.

        :type MaxRetryAttempts: int
        :param _ExecutionTTL: Timeout Handling Policy: Execution Timeout (in minutes), default: -1

        :type ExecutionTTL: int
        :param _WaitExecutionTotalTTL: Timeout Handling Policy: Wait Duration Timeout  (in minutes), default: -1
        :type WaitExecutionTotalTTL: str
        :param _AllowRedoType: Rerun & Refill Configuration: Default: ALL;

* ALL: Rerun or refill is allowed regardless of whether the task succeeds or fails.

* FAILURE: Rerun or refill is allowed only if the task fails; not allowed if the task succeeds.

* NONE: Rerun or refill is not allowed regardless of success or failure.
        :type AllowRedoType: str
        :param _ParamTaskOutList: Output parameter list.
        :type ParamTaskOutList: list of OutTaskParameter
        :param _ParamTaskInList: Input parameter list.
        :type ParamTaskInList: list of InTaskParameter
        :param _TaskOutputRegistryList: Output registration.
        :type TaskOutputRegistryList: list of TaskDataRegistry
        :param _InitStrategy: **Instance generation policy**.
T_PLUS_0: specifies t+0 generation. default policy.
T_PLUS_1: specifies t+1 generation.
        :type InitStrategy: str
        """
        self._CycleType = None
        self._ScheduleTimeZone = None
        self._CrontabExpression = None
        self._StartTime = None
        self._EndTime = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._ScheduleRunType = None
        self._CalendarOpen = None
        self._CalendarId = None
        self._CalendarName = None
        self._SelfDepend = None
        self._UpstreamDependencyConfigList = None
        self._DownStreamDependencyConfigList = None
        self._EventListenerList = None
        self._RunPriority = None
        self._RetryWait = None
        self._MaxRetryAttempts = None
        self._ExecutionTTL = None
        self._WaitExecutionTotalTTL = None
        self._AllowRedoType = None
        self._ParamTaskOutList = None
        self._ParamTaskInList = None
        self._TaskOutputRegistryList = None
        self._InitStrategy = None

    @property
    def CycleType(self):
        r"""Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def ScheduleTimeZone(self):
        r"""Time zone.
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CrontabExpression(self):
        r"""0 2 3 1,L,2 * ?	

        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def StartTime(self):
        r"""Effective date.

        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End date

        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecutionStartTime(self):
        r"""Execution time. the left-closed interval.

        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""Execution time. right closed interval.

        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def ScheduleRunType(self):
        r"""Scheduling type: 0 for normal scheduling, 1 for dry-run scheduling.

        :rtype: int
        """
        return self._ScheduleRunType

    @ScheduleRunType.setter
    def ScheduleRunType(self, ScheduleRunType):
        self._ScheduleRunType = ScheduleRunType

    @property
    def CalendarOpen(self):
        r"""Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""Calendar id.
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId

    @property
    def CalendarName(self):
        r"""Calendar name, which needs to be obtained from DescribeScheduleCalendarPageList API.
        :rtype: str
        """
        return self._CalendarName

    @CalendarName.setter
    def CalendarName(self, CalendarName):
        self._CalendarName = CalendarName

    @property
    def SelfDepend(self):
        r"""Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def UpstreamDependencyConfigList(self):
        r"""Specifies the upstream dependency array.
        :rtype: list of DependencyTaskBrief
        """
        return self._UpstreamDependencyConfigList

    @UpstreamDependencyConfigList.setter
    def UpstreamDependencyConfigList(self, UpstreamDependencyConfigList):
        self._UpstreamDependencyConfigList = UpstreamDependencyConfigList

    @property
    def DownStreamDependencyConfigList(self):
        r"""SpecSpecifies the downstream dependency array.

        :rtype: list of DependencyTaskBrief
        """
        return self._DownStreamDependencyConfigList

    @DownStreamDependencyConfigList.setter
    def DownStreamDependencyConfigList(self, DownStreamDependencyConfigList):
        self._DownStreamDependencyConfigList = DownStreamDependencyConfigList

    @property
    def EventListenerList(self):
        r"""Array of Events

        :rtype: list of EventListener
        """
        return self._EventListenerList

    @EventListenerList.setter
    def EventListenerList(self, EventListenerList):
        self._EventListenerList = EventListenerList

    @property
    def RunPriority(self):
        r"""Task scheduling priority. valid values: 4 (high), 5 (medium), 6 (low). default: 6.

        :rtype: int
        """
        return self._RunPriority

    @RunPriority.setter
    def RunPriority(self, RunPriority):
        self._RunPriority = RunPriority

    @property
    def RetryWait(self):
        r"""Retry policy. retry wait time in minutes. default: 5.

        :rtype: int
        """
        return self._RetryWait

    @RetryWait.setter
    def RetryWait(self, RetryWait):
        self._RetryWait = RetryWait

    @property
    def MaxRetryAttempts(self):
        r"""Specifies the maximum attempts of the retry policy. default: 4.

        :rtype: int
        """
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts

    @property
    def ExecutionTTL(self):
        r"""Timeout Handling Policy: Execution Timeout (in minutes), default: -1

        :rtype: int
        """
        return self._ExecutionTTL

    @ExecutionTTL.setter
    def ExecutionTTL(self, ExecutionTTL):
        self._ExecutionTTL = ExecutionTTL

    @property
    def WaitExecutionTotalTTL(self):
        r"""Timeout Handling Policy: Wait Duration Timeout  (in minutes), default: -1
        :rtype: str
        """
        return self._WaitExecutionTotalTTL

    @WaitExecutionTotalTTL.setter
    def WaitExecutionTotalTTL(self, WaitExecutionTotalTTL):
        self._WaitExecutionTotalTTL = WaitExecutionTotalTTL

    @property
    def AllowRedoType(self):
        r"""Rerun & Refill Configuration: Default: ALL;

* ALL: Rerun or refill is allowed regardless of whether the task succeeds or fails.

* FAILURE: Rerun or refill is allowed only if the task fails; not allowed if the task succeeds.

* NONE: Rerun or refill is not allowed regardless of success or failure.
        :rtype: str
        """
        return self._AllowRedoType

    @AllowRedoType.setter
    def AllowRedoType(self, AllowRedoType):
        self._AllowRedoType = AllowRedoType

    @property
    def ParamTaskOutList(self):
        r"""Output parameter list.
        :rtype: list of OutTaskParameter
        """
        return self._ParamTaskOutList

    @ParamTaskOutList.setter
    def ParamTaskOutList(self, ParamTaskOutList):
        self._ParamTaskOutList = ParamTaskOutList

    @property
    def ParamTaskInList(self):
        r"""Input parameter list.
        :rtype: list of InTaskParameter
        """
        return self._ParamTaskInList

    @ParamTaskInList.setter
    def ParamTaskInList(self, ParamTaskInList):
        self._ParamTaskInList = ParamTaskInList

    @property
    def TaskOutputRegistryList(self):
        r"""Output registration.
        :rtype: list of TaskDataRegistry
        """
        return self._TaskOutputRegistryList

    @TaskOutputRegistryList.setter
    def TaskOutputRegistryList(self, TaskOutputRegistryList):
        self._TaskOutputRegistryList = TaskOutputRegistryList

    @property
    def InitStrategy(self):
        r"""**Instance generation policy**.
T_PLUS_0: specifies t+0 generation. default policy.
T_PLUS_1: specifies t+1 generation.
        :rtype: str
        """
        return self._InitStrategy

    @InitStrategy.setter
    def InitStrategy(self, InitStrategy):
        self._InitStrategy = InitStrategy


    def _deserialize(self, params):
        self._CycleType = params.get("CycleType")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CrontabExpression = params.get("CrontabExpression")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._ScheduleRunType = params.get("ScheduleRunType")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        self._CalendarName = params.get("CalendarName")
        self._SelfDepend = params.get("SelfDepend")
        if params.get("UpstreamDependencyConfigList") is not None:
            self._UpstreamDependencyConfigList = []
            for item in params.get("UpstreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._UpstreamDependencyConfigList.append(obj)
        if params.get("DownStreamDependencyConfigList") is not None:
            self._DownStreamDependencyConfigList = []
            for item in params.get("DownStreamDependencyConfigList"):
                obj = DependencyTaskBrief()
                obj._deserialize(item)
                self._DownStreamDependencyConfigList.append(obj)
        if params.get("EventListenerList") is not None:
            self._EventListenerList = []
            for item in params.get("EventListenerList"):
                obj = EventListener()
                obj._deserialize(item)
                self._EventListenerList.append(obj)
        self._RunPriority = params.get("RunPriority")
        self._RetryWait = params.get("RetryWait")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        self._ExecutionTTL = params.get("ExecutionTTL")
        self._WaitExecutionTotalTTL = params.get("WaitExecutionTotalTTL")
        self._AllowRedoType = params.get("AllowRedoType")
        if params.get("ParamTaskOutList") is not None:
            self._ParamTaskOutList = []
            for item in params.get("ParamTaskOutList"):
                obj = OutTaskParameter()
                obj._deserialize(item)
                self._ParamTaskOutList.append(obj)
        if params.get("ParamTaskInList") is not None:
            self._ParamTaskInList = []
            for item in params.get("ParamTaskInList"):
                obj = InTaskParameter()
                obj._deserialize(item)
                self._ParamTaskInList.append(obj)
        if params.get("TaskOutputRegistryList") is not None:
            self._TaskOutputRegistryList = []
            for item in params.get("TaskOutputRegistryList"):
                obj = TaskDataRegistry()
                obj._deserialize(item)
                self._TaskOutputRegistryList.append(obj)
        self._InitStrategy = params.get("InitStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSchedulingParameter(AbstractModel):
    r"""Scheduling variable parameter.

    """

    def __init__(self):
        r"""
        :param _ParamKey: Parameter name.

        :type ParamKey: str
        :param _ParamValue: Parameter value.
        :type ParamValue: str
        """
        self._ParamKey = None
        self._ParamValue = None

    @property
    def ParamKey(self):
        r"""Parameter name.

        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamValue(self):
        r"""Parameter value.
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskVersion(AbstractModel):
    r"""Describes the version list information of the task.

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _VersionNum: Version number

        :type VersionNum: str
        :param _CreateUserUin: Creator ID
        :type CreateUserUin: str
        :param _VersionId: Saved version ID
        :type VersionId: str
        :param _VersionRemark: Version description

        :type VersionRemark: str
        :param _ApproveStatus: Approval status (only for submit version).

        :type ApproveStatus: str
        :param _Status: Production status (only for submit version).

        :type Status: str
        :param _ApproveUserUin: Approver (only for submit version).

        :type ApproveUserUin: str
        """
        self._CreateTime = None
        self._VersionNum = None
        self._CreateUserUin = None
        self._VersionId = None
        self._VersionRemark = None
        self._ApproveStatus = None
        self._Status = None
        self._ApproveUserUin = None

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VersionNum(self):
        r"""Version number

        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def CreateUserUin(self):
        r"""Creator ID
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def VersionId(self):
        r"""Saved version ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionRemark(self):
        r"""Version description

        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def ApproveStatus(self):
        r"""Approval status (only for submit version).

        :rtype: str
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def Status(self):
        r"""Production status (only for submit version).

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApproveUserUin(self):
        r"""Approver (only for submit version).

        :rtype: str
        """
        return self._ApproveUserUin

    @ApproveUserUin.setter
    def ApproveUserUin(self, ApproveUserUin):
        self._ApproveUserUin = ApproveUserUin


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._VersionNum = params.get("VersionNum")
        self._CreateUserUin = params.get("CreateUserUin")
        self._VersionId = params.get("VersionId")
        self._VersionRemark = params.get("VersionRemark")
        self._ApproveStatus = params.get("ApproveStatus")
        self._Status = params.get("Status")
        self._ApproveUserUin = params.get("ApproveUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskVersionDetail(AbstractModel):
    r"""Describes the version list information of the task.

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _VersionNum: Version number


        :type VersionNum: str
        :param _CreateUserUin: Specifies the version creator.

        :type CreateUserUin: str
        :param _VersionId: Specifies the version Id to save.

        :type VersionId: str
        :param _VersionRemark: Version description

        :type VersionRemark: str
        :param _ApproveStatus: Approval status (only for submit version).

        :type ApproveStatus: str
        :param _ApproveTime: Production status  (only for submit version).
        :type ApproveTime: str
        :param _Task: Describes the task detail of the version.

        :type Task: :class:`tencentcloud.wedata.v20250806.models.Task`
        :param _ApproveUserUin: Approver Id.
        :type ApproveUserUin: str
        """
        self._CreateTime = None
        self._VersionNum = None
        self._CreateUserUin = None
        self._VersionId = None
        self._VersionRemark = None
        self._ApproveStatus = None
        self._ApproveTime = None
        self._Task = None
        self._ApproveUserUin = None

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VersionNum(self):
        r"""Version number


        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def CreateUserUin(self):
        r"""Specifies the version creator.

        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def VersionId(self):
        r"""Specifies the version Id to save.

        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionRemark(self):
        r"""Version description

        :rtype: str
        """
        return self._VersionRemark

    @VersionRemark.setter
    def VersionRemark(self, VersionRemark):
        self._VersionRemark = VersionRemark

    @property
    def ApproveStatus(self):
        r"""Approval status (only for submit version).

        :rtype: str
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def ApproveTime(self):
        r"""Production status  (only for submit version).
        :rtype: str
        """
        return self._ApproveTime

    @ApproveTime.setter
    def ApproveTime(self, ApproveTime):
        self._ApproveTime = ApproveTime

    @property
    def Task(self):
        r"""Describes the task detail of the version.

        :rtype: :class:`tencentcloud.wedata.v20250806.models.Task`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def ApproveUserUin(self):
        r"""Approver Id.
        :rtype: str
        """
        return self._ApproveUserUin

    @ApproveUserUin.setter
    def ApproveUserUin(self, ApproveUserUin):
        self._ApproveUserUin = ApproveUserUin


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._VersionNum = params.get("VersionNum")
        self._CreateUserUin = params.get("CreateUserUin")
        self._VersionId = params.get("VersionId")
        self._VersionRemark = params.get("VersionRemark")
        self._ApproveStatus = params.get("ApproveStatus")
        self._ApproveTime = params.get("ApproveTime")
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._ApproveUserUin = params.get("ApproveUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeOutStrategyInfo(AbstractModel):
    r"""Alarm timeout configuration rule information.

    """

    def __init__(self):
        r"""
        :param _RuleType: Timeout Alarm Configuration

Expected Execution Duration Timeout - The actual runtime exceeds the estimated execution duration.

Expected Completion Time Timeout - The task has not completed by the estimated completion time.

Expected Scheduling Wait Timeout - The waiting time in the scheduling queue exceeds the estimated wait time.

Cycle-Incomplete Timeout - The task was expected to complete within its scheduled cycle but did not.
        :type RuleType: int
        :param _Type: Timeout Value Configuration Type

1: Fixed value (specified manually)

2: Average value (calculated automatically)
        :type Type: int
        :param _Hour: Timeout Specified Value (hours) - The timeout threshold in hours. Default is 1.
        :type Hour: int
        :param _Min: Timeout Specified Value (minutes) - The timeout threshold in minutes. Default is 1.
        :type Min: int
        :param _ScheduleTimeZone: The time zone configuration corresponding to the timeout, such as UTC+7, defaults to UTC+8.

        :type ScheduleTimeZone: str
        """
        self._RuleType = None
        self._Type = None
        self._Hour = None
        self._Min = None
        self._ScheduleTimeZone = None

    @property
    def RuleType(self):
        r"""Timeout Alarm Configuration

Expected Execution Duration Timeout - The actual runtime exceeds the estimated execution duration.

Expected Completion Time Timeout - The task has not completed by the estimated completion time.

Expected Scheduling Wait Timeout - The waiting time in the scheduling queue exceeds the estimated wait time.

Cycle-Incomplete Timeout - The task was expected to complete within its scheduled cycle but did not.
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Type(self):
        r"""Timeout Value Configuration Type

1: Fixed value (specified manually)

2: Average value (calculated automatically)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Hour(self):
        r"""Timeout Specified Value (hours) - The timeout threshold in hours. Default is 1.
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Min(self):
        r"""Timeout Specified Value (minutes) - The timeout threshold in minutes. Default is 1.
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ScheduleTimeZone(self):
        r"""The time zone configuration corresponding to the timeout, such as UTC+7, defaults to UTC+8.

        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._Type = params.get("Type")
        self._Hour = params.get("Hour")
        self._Min = params.get("Min")
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFileRequest(AbstractModel):
    r"""UpdateCodeFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _CodeFileId: Code file ID. the parameter value comes from the CreateCodeFile API response.
        :type CodeFileId: str
        :param _CodeFileConfig: Specifies the code file configuration.
        :type CodeFileConfig: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        :param _CodeFileContent: Specifies the content of the code file.
        :type CodeFileContent: str
        """
        self._ProjectId = None
        self._CodeFileId = None
        self._CodeFileConfig = None
        self._CodeFileContent = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CodeFileId(self):
        r"""Code file ID. the parameter value comes from the CreateCodeFile API response.
        :rtype: str
        """
        return self._CodeFileId

    @CodeFileId.setter
    def CodeFileId(self, CodeFileId):
        self._CodeFileId = CodeFileId

    @property
    def CodeFileConfig(self):
        r"""Specifies the code file configuration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFileConfig`
        """
        return self._CodeFileConfig

    @CodeFileConfig.setter
    def CodeFileConfig(self, CodeFileConfig):
        self._CodeFileConfig = CodeFileConfig

    @property
    def CodeFileContent(self):
        r"""Specifies the content of the code file.
        :rtype: str
        """
        return self._CodeFileContent

    @CodeFileContent.setter
    def CodeFileContent(self, CodeFileContent):
        self._CodeFileContent = CodeFileContent


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CodeFileId = params.get("CodeFileId")
        if params.get("CodeFileConfig") is not None:
            self._CodeFileConfig = CodeFileConfig()
            self._CodeFileConfig._deserialize(params.get("CodeFileConfig"))
        self._CodeFileContent = params.get("CodeFileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFileResponse(AbstractModel):
    r"""UpdateCodeFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeFile`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeFile()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateCodeFolderRequest(AbstractModel):
    r"""UpdateCodeFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. The parameter value can be obtained from the response of the CreateCodeFolder API.
        :type FolderId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. The parameter value can be obtained from the response of the CreateCodeFolder API.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCodeFolderResponse(AbstractModel):
    r"""UpdateCodeFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Execution result
        :type Data: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Execution result
        :rtype: :class:`tencentcloud.wedata.v20250806.models.CodeStudioFolderActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CodeStudioFolderActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateFolderResult(AbstractModel):
    r"""Specifies the update folder result.

    """

    def __init__(self):
        r"""
        :param _Status: Update status. true indicates update succeeded. false indicates update failed.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Update status. true indicates update succeeded. false indicates update failed.
        :rtype: bool
        """
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
        


class UpdateOpsAlarmRuleRequest(AbstractModel):
    r"""UpdateOpsAlarmRule request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AlarmRuleId: Specifies the unique id of the Alarm rule, obtained through the GetAlarmRule/ListAlarmRule api.
        :type AlarmRuleId: str
        :param _AlarmRuleName: Specifies the new rule name of the Alarm rule.
        :type AlarmRuleName: str
        :param _MonitorObjectType: Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :type MonitorObjectType: int
        :param _MonitorObjectIds: Pass different business IDs based on the MonitorType setting:

1 (Task): MonitorObjectIds should be a list of task IDs.

2 (Workflow): MonitorObjectIds should be a list of workflow IDs (workflow IDs can be obtained via the ListWorkflows API).

3 (Project): MonitorObjectIds should be a list of project IDs.
        :type MonitorObjectIds: list of str
        :param _AlarmTypes: Alarm Rule Monitoring Types

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectFailureInstanceUpwardVolatilityAlarm: Alarm when the upward fluctuation count of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

projectSuccessInstanceDownwardVolatilityAlarm: Alarm when the downward fluctuation count of successful instances for the day exceeds the threshold

projectFailureInstanceCountAlarm: Alarm when the number of failed instances for the day exceeds the threshold

projectFailureInstanceProportionAlarm: Alarm when the proportion of failed instances for the day exceeds the threshold

reconciliationFailure: Alarm when offline reconciliation task fails

reconciliationOvertime: Alarm when offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :type AlarmTypes: list of str
        :param _AlarmRuleDetail: Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :type AlarmRuleDetail: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        :param _Status: Enable status of the Alarm rule. valid values: 0 (disabled), 1 (enabled).
        :type Status: int
        :param _AlarmLevel: Alarm level. 1. ordinary, 2. important, 3. critical.
        :type AlarmLevel: int
        :param _AlarmGroups: Describes the Alarm recipient configuration message.
        :type AlarmGroups: list of AlarmGroup
        :param _Description: Alarm description.
        :type Description: str
        """
        self._ProjectId = None
        self._AlarmRuleId = None
        self._AlarmRuleName = None
        self._MonitorObjectType = None
        self._MonitorObjectIds = None
        self._AlarmTypes = None
        self._AlarmRuleDetail = None
        self._Status = None
        self._AlarmLevel = None
        self._AlarmGroups = None
        self._Description = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AlarmRuleId(self):
        r"""Specifies the unique id of the Alarm rule, obtained through the GetAlarmRule/ListAlarmRule api.
        :rtype: str
        """
        return self._AlarmRuleId

    @AlarmRuleId.setter
    def AlarmRuleId(self, AlarmRuleId):
        self._AlarmRuleId = AlarmRuleId

    @property
    def AlarmRuleName(self):
        r"""Specifies the new rule name of the Alarm rule.
        :rtype: str
        """
        return self._AlarmRuleName

    @AlarmRuleName.setter
    def AlarmRuleName(self, AlarmRuleName):
        self._AlarmRuleName = AlarmRuleName

    @property
    def MonitorObjectType(self):
        r"""Monitoring Object Type

Task-level Monitoring - Can be configured by Task / Workflow / Project:
1 = Task (default)
2 = Workflow
3 = Project

Project-level Monitoring - Monitors overall task fluctuations within a project:
7 = Project fluctuation monitoring alarm
        :rtype: int
        """
        return self._MonitorObjectType

    @MonitorObjectType.setter
    def MonitorObjectType(self, MonitorObjectType):
        self._MonitorObjectType = MonitorObjectType

    @property
    def MonitorObjectIds(self):
        r"""Pass different business IDs based on the MonitorType setting:

1 (Task): MonitorObjectIds should be a list of task IDs.

2 (Workflow): MonitorObjectIds should be a list of workflow IDs (workflow IDs can be obtained via the ListWorkflows API).

3 (Project): MonitorObjectIds should be a list of project IDs.
        :rtype: list of str
        """
        return self._MonitorObjectIds

    @MonitorObjectIds.setter
    def MonitorObjectIds(self, MonitorObjectIds):
        self._MonitorObjectIds = MonitorObjectIds

    @property
    def AlarmTypes(self):
        r"""Alarm Rule Monitoring Types

failure: Failure alarm

overtime: Timeout alarm

success: Success alarm

backTrackingOrRerunSuccess: Alarm when backfill/rerun succeeds

backTrackingOrRerunFailure: Alarm when backfill/rerun fails

projectFailureInstanceUpwardFluctuationAlarm: Alarm when the upward fluctuation rate of failed instances for the day exceeds the threshold

projectFailureInstanceUpwardVolatilityAlarm: Alarm when the upward fluctuation count of failed instances for the day exceeds the threshold

projectSuccessInstanceDownwardFluctuationAlarm: Alarm when the downward fluctuation rate of successful instances for the day exceeds the threshold

projectSuccessInstanceDownwardVolatilityAlarm: Alarm when the downward fluctuation count of successful instances for the day exceeds the threshold

projectFailureInstanceCountAlarm: Alarm when the number of failed instances for the day exceeds the threshold

projectFailureInstanceProportionAlarm: Alarm when the proportion of failed instances for the day exceeds the threshold

reconciliationFailure: Alarm when offline reconciliation task fails

reconciliationOvertime: Alarm when offline reconciliation task runs overtime

reconciliationMismatch: Alarm when the number of mismatched records in reconciliation exceeds the threshold
        :rtype: list of str
        """
        return self._AlarmTypes

    @AlarmTypes.setter
    def AlarmTypes(self, AlarmTypes):
        self._AlarmTypes = AlarmTypes

    @property
    def AlarmRuleDetail(self):
        r"""Alarm Rule Configuration Information

Success Alarms - No configuration required;

Failure Alarms - Can be configured to trigger on the first failure or on all retry failures;

Timeout Alarms - Require configuration of the timeout type and timeout threshold;

Project Fluctuation Alarms - Require configuration of the fluctuation rate and the debounce cycle.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.AlarmRuleDetail`
        """
        return self._AlarmRuleDetail

    @AlarmRuleDetail.setter
    def AlarmRuleDetail(self, AlarmRuleDetail):
        self._AlarmRuleDetail = AlarmRuleDetail

    @property
    def Status(self):
        r"""Enable status of the Alarm rule. valid values: 0 (disabled), 1 (enabled).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AlarmLevel(self):
        r"""Alarm level. 1. ordinary, 2. important, 3. critical.
        :rtype: int
        """
        return self._AlarmLevel

    @AlarmLevel.setter
    def AlarmLevel(self, AlarmLevel):
        self._AlarmLevel = AlarmLevel

    @property
    def AlarmGroups(self):
        r"""Describes the Alarm recipient configuration message.
        :rtype: list of AlarmGroup
        """
        return self._AlarmGroups

    @AlarmGroups.setter
    def AlarmGroups(self, AlarmGroups):
        self._AlarmGroups = AlarmGroups

    @property
    def Description(self):
        r"""Alarm description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AlarmRuleId = params.get("AlarmRuleId")
        self._AlarmRuleName = params.get("AlarmRuleName")
        self._MonitorObjectType = params.get("MonitorObjectType")
        self._MonitorObjectIds = params.get("MonitorObjectIds")
        self._AlarmTypes = params.get("AlarmTypes")
        if params.get("AlarmRuleDetail") is not None:
            self._AlarmRuleDetail = AlarmRuleDetail()
            self._AlarmRuleDetail._deserialize(params.get("AlarmRuleDetail"))
        self._Status = params.get("Status")
        self._AlarmLevel = params.get("AlarmLevel")
        if params.get("AlarmGroups") is not None:
            self._AlarmGroups = []
            for item in params.get("AlarmGroups"):
                obj = AlarmGroup()
                obj._deserialize(item)
                self._AlarmGroups.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOpsAlarmRuleResponse(AbstractModel):
    r"""UpdateOpsAlarmRule response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Indicates whether the update is successful.
true: update successful. false: failed to update.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.ModifyAlarmRuleResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Indicates whether the update is successful.
true: update successful. false: failed to update.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.ModifyAlarmRuleResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ModifyAlarmRuleResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateOpsTasksOwnerRequest(AbstractModel):
    r"""UpdateOpsTasksOwner request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _TaskIds: Task Id list. specifies the list of task ids.
        :type TaskIds: list of str
        :param _OwnerUin: Task owner Id.
        :type OwnerUin: str
        """
        self._ProjectId = None
        self._TaskIds = None
        self._OwnerUin = None

    @property
    def ProjectId(self):
        r"""Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskIds(self):
        r"""Task Id list. specifies the list of task ids.
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def OwnerUin(self):
        r"""Task owner Id.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskIds = params.get("TaskIds")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOpsTasksOwnerResponse(AbstractModel):
    r"""UpdateOpsTasksOwner response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Operation result.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateTasksOwner`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Operation result.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTasksOwner`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateTasksOwner()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateResourceFileRequest(AbstractModel):
    r"""UpdateResourceFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ResourceId: Resource file ID. Can be obtained through the ListResourceFiles API.
        :type ResourceId: str
        :param _ResourceFile: -Upload file and manual entry are two methods, choose one. if both are provided, the sequence is file > manual entry.
-The hand-filled value must be an existing cos path. /datastudio/resource/ is the fixed prefix. projectId is the project ID and requires a specific value. parentFolderPath is the parent folder path. name is the file name. 
Hand-filled value example:.
   /datastudio/resource/projectId/parentFolderPath/name 

        :type ResourceFile: str
        :param _ResourceName: Resource name, preferably kept consistent with the file name.
        :type ResourceName: str
        :param _BundleId: Bundle Client ID.
        :type BundleId: str
        :param _BundleInfo: Bundle Client Name
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._ResourceId = None
        self._ResourceFile = None
        self._ResourceName = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceId(self):
        r"""Resource file ID. Can be obtained through the ListResourceFiles API.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceFile(self):
        r"""-Upload file and manual entry are two methods, choose one. if both are provided, the sequence is file > manual entry.
-The hand-filled value must be an existing cos path. /datastudio/resource/ is the fixed prefix. projectId is the project ID and requires a specific value. parentFolderPath is the parent folder path. name is the file name. 
Hand-filled value example:.
   /datastudio/resource/projectId/parentFolderPath/name 

        :rtype: str
        """
        return self._ResourceFile

    @ResourceFile.setter
    def ResourceFile(self, ResourceFile):
        self._ResourceFile = ResourceFile

    @property
    def ResourceName(self):
        r"""Resource name, preferably kept consistent with the file name.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def BundleId(self):
        r"""Bundle Client ID.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle Client Name
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ResourceId = params.get("ResourceId")
        self._ResourceFile = params.get("ResourceFile")
        self._ResourceName = params.get("ResourceName")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceFileResponse(AbstractModel):
    r"""UpdateResourceFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Update status.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Update status.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateResourceFileResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateResourceFileResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateResourceFileResult(AbstractModel):
    r"""Update resource file result.

    """

    def __init__(self):
        r"""
        :param _Status: true
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""true
        :rtype: bool
        """
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
        


class UpdateResourceFolderRequest(AbstractModel):
    r"""UpdateResourceFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. obtain through the  ListResourceFolders API.
        :type FolderId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. obtain through the  ListResourceFolders API.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceFolderResponse(AbstractModel):
    r"""UpdateResourceFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the update folder result. if the update fails, an error will be reported.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the update folder result. if the update fails, an error will be reported.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateSQLFolderRequest(AbstractModel):
    r"""UpdateSQLFolder request structure.

    """

    def __init__(self):
        r"""
        :param _FolderId: Folder ID
        :type FolderId: str
        :param _FolderName: Folder name.
        :type FolderName: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _AccessScope: Access permission: SHARED, PRIVATE.
        :type AccessScope: str
        """
        self._FolderId = None
        self._FolderName = None
        self._ProjectId = None
        self._AccessScope = None

    @property
    def FolderId(self):
        r"""Folder ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Folder name.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AccessScope(self):
        r"""Access permission: SHARED, PRIVATE.
        :rtype: str
        """
        return self._AccessScope

    @AccessScope.setter
    def AccessScope(self, AccessScope):
        self._AccessScope = AccessScope


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._ProjectId = params.get("ProjectId")
        self._AccessScope = params.get("AccessScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSQLFolderResponse(AbstractModel):
    r"""UpdateSQLFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).
        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Indicates whether the operation is successful. valid values: true (successful), false (unsuccessful).
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLContentActionResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLContentActionResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateSQLScriptRequest(AbstractModel):
    r"""UpdateSQLScript request structure.

    """

    def __init__(self):
        r"""
        :param _ScriptId: Script Id.
        :type ScriptId: str
        :param _ProjectId: Project ID.

        :type ProjectId: str
        :param _ScriptConfig: Specifies the script configuration for data exploration.
        :type ScriptConfig: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        :param _ScriptContent: Specifies the script content, needs to be Base64 encoded.
        :type ScriptContent: str
        """
        self._ScriptId = None
        self._ProjectId = None
        self._ScriptConfig = None
        self._ScriptContent = None

    @property
    def ScriptId(self):
        r"""Script Id.
        :rtype: str
        """
        return self._ScriptId

    @ScriptId.setter
    def ScriptId(self, ScriptId):
        self._ScriptId = ScriptId

    @property
    def ProjectId(self):
        r"""Project ID.

        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScriptConfig(self):
        r"""Specifies the script configuration for data exploration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScriptConfig`
        """
        return self._ScriptConfig

    @ScriptConfig.setter
    def ScriptConfig(self, ScriptConfig):
        self._ScriptConfig = ScriptConfig

    @property
    def ScriptContent(self):
        r"""Specifies the script content, needs to be Base64 encoded.
        :rtype: str
        """
        return self._ScriptContent

    @ScriptContent.setter
    def ScriptContent(self, ScriptContent):
        self._ScriptContent = ScriptContent


    def _deserialize(self, params):
        self._ScriptId = params.get("ScriptId")
        self._ProjectId = params.get("ProjectId")
        if params.get("ScriptConfig") is not None:
            self._ScriptConfig = SQLScriptConfig()
            self._ScriptConfig._deserialize(params.get("ScriptConfig"))
        self._ScriptContent = params.get("ScriptContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSQLScriptResponse(AbstractModel):
    r"""UpdateSQLScript response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result


        :type Data: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result


        :rtype: :class:`tencentcloud.wedata.v20250806.models.SQLScript`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SQLScript()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateTaskBaseAttribute(AbstractModel):
    r"""Updates the basic attribute information of the task.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name.
        :type TaskName: str
        :param _OwnerUin: Task owner ID.
        :type OwnerUin: str
        :param _TaskDescription: Task description
        :type TaskDescription: str
        """
        self._TaskName = None
        self._OwnerUin = None
        self._TaskDescription = None

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def OwnerUin(self):
        r"""Task owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def TaskDescription(self):
        r"""Task description
        :rtype: str
        """
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._OwnerUin = params.get("OwnerUin")
        self._TaskDescription = params.get("TaskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskBrief(AbstractModel):
    r"""Update task object input parameters.

    """

    def __init__(self):
        r"""
        :param _TaskBaseAttribute: Describes the basic attributes of the task.
        :type TaskBaseAttribute: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBaseAttribute`
        :param _TaskConfiguration: Task configurations.
        :type TaskConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        :param _TaskSchedulerConfiguration: Task scheduling configuration.
        :type TaskSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        self._TaskBaseAttribute = None
        self._TaskConfiguration = None
        self._TaskSchedulerConfiguration = None

    @property
    def TaskBaseAttribute(self):
        r"""Describes the basic attributes of the task.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBaseAttribute`
        """
        return self._TaskBaseAttribute

    @TaskBaseAttribute.setter
    def TaskBaseAttribute(self, TaskBaseAttribute):
        self._TaskBaseAttribute = TaskBaseAttribute

    @property
    def TaskConfiguration(self):
        r"""Task configurations.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskConfiguration`
        """
        return self._TaskConfiguration

    @TaskConfiguration.setter
    def TaskConfiguration(self, TaskConfiguration):
        self._TaskConfiguration = TaskConfiguration

    @property
    def TaskSchedulerConfiguration(self):
        r"""Task scheduling configuration.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.TaskSchedulerConfiguration`
        """
        return self._TaskSchedulerConfiguration

    @TaskSchedulerConfiguration.setter
    def TaskSchedulerConfiguration(self, TaskSchedulerConfiguration):
        self._TaskSchedulerConfiguration = TaskSchedulerConfiguration


    def _deserialize(self, params):
        if params.get("TaskBaseAttribute") is not None:
            self._TaskBaseAttribute = UpdateTaskBaseAttribute()
            self._TaskBaseAttribute._deserialize(params.get("TaskBaseAttribute"))
        if params.get("TaskConfiguration") is not None:
            self._TaskConfiguration = TaskConfiguration()
            self._TaskConfiguration._deserialize(params.get("TaskConfiguration"))
        if params.get("TaskSchedulerConfiguration") is not None:
            self._TaskSchedulerConfiguration = TaskSchedulerConfiguration()
            self._TaskSchedulerConfiguration._deserialize(params.get("TaskSchedulerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskRequest(AbstractModel):
    r"""UpdateTask request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _TaskId: Task ID
        :type TaskId: str
        :param _Task: Describes the basic attributes of the task.
        :type Task: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBrief`
        """
        self._ProjectId = None
        self._TaskId = None
        self._Task = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Task(self):
        r"""Describes the basic attributes of the task.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskBrief`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TaskId = params.get("TaskId")
        if params.get("Task") is not None:
            self._Task = UpdateTaskBrief()
            self._Task._deserialize(params.get("Task"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTaskResponse(AbstractModel):
    r"""UpdateTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task ID
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task ID
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateTaskResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateTaskResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateTaskResult(AbstractModel):
    r"""Update task response parameters structure.

    """

    def __init__(self):
        r"""
        :param _Status: Processing result. returns true on success. returns false on failure.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Processing result. returns true on success. returns false on failure.
        :rtype: bool
        """
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
        


class UpdateTasksOwner(AbstractModel):
    r"""Describes the result of batch modifying the task owner.

    """

    def __init__(self):
        r"""
        :param _Status: Describes the result of modifying the task owner.
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Describes the result of modifying the task owner.
        :rtype: bool
        """
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
        


class UpdateWorkflowFolderRequest(AbstractModel):
    r"""UpdateWorkflowFolder request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID. obtain through the ListWorkflowFolders API.
        :type FolderId: str
        :param _FolderName: Specifies the folder name after update.
        :type FolderName: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderName = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID. obtain through the ListWorkflowFolders API.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        r"""Specifies the folder name after update.
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowFolderResponse(AbstractModel):
    r"""UpdateWorkflowFolder response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Specifies the update folder result. if the update fails, an error will be reported.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Specifies the update folder result. if the update fails, an error will be reported.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateFolderResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateFolderResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkflowRequest(AbstractModel):
    r"""UpdateWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.
        :type WorkflowName: str
        :param _OwnerUin: Owner ID.
        :type OwnerUin: str
        :param _WorkflowDesc: Remarks.
        :type WorkflowDesc: str
        :param _WorkflowParams: Workflow parameter list.
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: Specifies unified scheduling parameters.
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        :param _BundleId: BundleId item.
        :type BundleId: str
        :param _BundleInfo: Bundle info.
        :type BundleInfo: str
        """
        self._ProjectId = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._OwnerUin = None
        self._WorkflowDesc = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def WorkflowId(self):
        r"""Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""Owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def WorkflowDesc(self):
        r"""Remarks.
        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def WorkflowParams(self):
        r"""Workflow parameter list.
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""Specifies unified scheduling parameters.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfigurationInfo`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def BundleId(self):
        r"""BundleId item.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""Bundle info.
        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._WorkflowDesc = params.get("WorkflowDesc")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfigurationInfo()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkflowResponse(AbstractModel):
    r"""UpdateWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _Data: true represents success. false represents failure.
        :type Data: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""true represents success. false represents failure.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.UpdateWorkflowResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateWorkflowResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateWorkflowResult(AbstractModel):
    r"""Update workflow result.

    """

    def __init__(self):
        r"""
        :param _Status: Update Workflow Result
        :type Status: bool
        """
        self._Status = None

    @property
    def Status(self):
        r"""Update Workflow Result
        :rtype: bool
        """
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
        


class WorkflowDetail(AbstractModel):
    r"""Describes the workflow details.

    """

    def __init__(self):
        r"""
        :param _WorkflowName: Workflow name.

        :type WorkflowName: str
        :param _OwnerUin: Owner ID.
        :type OwnerUin: str
        :param _CreateUserUin: Creator ID.
        :type CreateUserUin: str
        :param _WorkflowType: Workflow type. Valid values: cycle or manual.

        :type WorkflowType: str
        :param _WorkflowParams: Workflow parameter array.
        :type WorkflowParams: list of ParamInfo
        :param _WorkflowSchedulerConfiguration: Unified scheduling parameter.
.
        :type WorkflowSchedulerConfiguration: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfiguration`
        :param _WorkflowDesc: Workflow description.

        :type WorkflowDesc: str
        :param _Path: Workflow path.
        :type Path: str
        :param _BundleId: BundleId item.
        :type BundleId: str
        :param _BundleInfo: BundleInfo item. specifies the bundle information.

        :type BundleInfo: str
        """
        self._WorkflowName = None
        self._OwnerUin = None
        self._CreateUserUin = None
        self._WorkflowType = None
        self._WorkflowParams = None
        self._WorkflowSchedulerConfiguration = None
        self._WorkflowDesc = None
        self._Path = None
        self._BundleId = None
        self._BundleInfo = None

    @property
    def WorkflowName(self):
        r"""Workflow name.

        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def OwnerUin(self):
        r"""Owner ID.
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUserUin(self):
        r"""Creator ID.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin

    @property
    def WorkflowType(self):
        r"""Workflow type. Valid values: cycle or manual.

        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def WorkflowParams(self):
        r"""Workflow parameter array.
        :rtype: list of ParamInfo
        """
        return self._WorkflowParams

    @WorkflowParams.setter
    def WorkflowParams(self, WorkflowParams):
        self._WorkflowParams = WorkflowParams

    @property
    def WorkflowSchedulerConfiguration(self):
        r"""Unified scheduling parameter.
.
        :rtype: :class:`tencentcloud.wedata.v20250806.models.WorkflowSchedulerConfiguration`
        """
        return self._WorkflowSchedulerConfiguration

    @WorkflowSchedulerConfiguration.setter
    def WorkflowSchedulerConfiguration(self, WorkflowSchedulerConfiguration):
        self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration

    @property
    def WorkflowDesc(self):
        r"""Workflow description.

        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def Path(self):
        r"""Workflow path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def BundleId(self):
        r"""BundleId item.
        :rtype: str
        """
        return self._BundleId

    @BundleId.setter
    def BundleId(self, BundleId):
        self._BundleId = BundleId

    @property
    def BundleInfo(self):
        r"""BundleInfo item. specifies the bundle information.

        :rtype: str
        """
        return self._BundleInfo

    @BundleInfo.setter
    def BundleInfo(self, BundleInfo):
        self._BundleInfo = BundleInfo


    def _deserialize(self, params):
        self._WorkflowName = params.get("WorkflowName")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUserUin = params.get("CreateUserUin")
        self._WorkflowType = params.get("WorkflowType")
        if params.get("WorkflowParams") is not None:
            self._WorkflowParams = []
            for item in params.get("WorkflowParams"):
                obj = ParamInfo()
                obj._deserialize(item)
                self._WorkflowParams.append(obj)
        if params.get("WorkflowSchedulerConfiguration") is not None:
            self._WorkflowSchedulerConfiguration = WorkflowSchedulerConfiguration()
            self._WorkflowSchedulerConfiguration._deserialize(params.get("WorkflowSchedulerConfiguration"))
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._Path = params.get("Path")
        self._BundleId = params.get("BundleId")
        self._BundleInfo = params.get("BundleInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowFolder(AbstractModel):
    r"""Folder information.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _FolderId: Folder ID.
        :type FolderId: str
        :param _FolderPath: Specifies the absolute path of the folder.
        :type FolderPath: str
        :param _CreateUserUin: Creator ID.
        :type CreateUserUin: str
        """
        self._ProjectId = None
        self._FolderId = None
        self._FolderPath = None
        self._CreateUserUin = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FolderId(self):
        r"""Folder ID.
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderPath(self):
        r"""Specifies the absolute path of the folder.
        :rtype: str
        """
        return self._FolderPath

    @FolderPath.setter
    def FolderPath(self, FolderPath):
        self._FolderPath = FolderPath

    @property
    def CreateUserUin(self):
        r"""Creator ID.
        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FolderId = params.get("FolderId")
        self._FolderPath = params.get("FolderPath")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowFolderPage(AbstractModel):
    r"""Paginate resource files.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Data page number, equal to or greater than 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageNumber: int
        :param _PageSize: Specifies the number of data records displayed per page. value range: 10 to 200.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PageSize: int
        :param _TotalCount: Total number of folders.
        :type TotalCount: int
        :param _TotalPageNumber: Total pages
        :type TotalPageNumber: int
        :param _Items: Folder list.
        :type Items: list of WorkflowFolder
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TotalPageNumber = None
        self._Items = None

    @property
    def PageNumber(self):
        r"""Data page number, equal to or greater than 1.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Specifies the number of data records displayed per page. value range: 10 to 200.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of folders.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalPageNumber(self):
        r"""Total pages
        :rtype: int
        """
        return self._TotalPageNumber

    @TotalPageNumber.setter
    def TotalPageNumber(self, TotalPageNumber):
        self._TotalPageNumber = TotalPageNumber

    @property
    def Items(self):
        r"""Folder list.
        :rtype: list of WorkflowFolder
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalPageNumber = params.get("TotalPageNumber")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = WorkflowFolder()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    r"""Retrieves workflow list information item.

    """

    def __init__(self):
        r"""
        :param _WorkflowId: Workflow ID.
        :type WorkflowId: str
        :param _WorkflowName: Workflow name.

        :type WorkflowName: str
        :param _WorkflowType: Workflow type: cycle or manual.

        :type WorkflowType: str
        :param _OwnerUin: Owner ID


        :type OwnerUin: str
        :param _CreateTime: Creation time.

        :type CreateTime: str
        :param _ModifyTime: Last Modification Time

        :type ModifyTime: str
        :param _UpdateUserUin: Last updated user ID.

        :type UpdateUserUin: str
        :param _WorkflowDesc: Workflow description.

        :type WorkflowDesc: str
        :param _CreateUserUin: Creator ID.

        :type CreateUserUin: str
        """
        self._WorkflowId = None
        self._WorkflowName = None
        self._WorkflowType = None
        self._OwnerUin = None
        self._CreateTime = None
        self._ModifyTime = None
        self._UpdateUserUin = None
        self._WorkflowDesc = None
        self._CreateUserUin = None

    @property
    def WorkflowId(self):
        r"""Workflow ID.
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""Workflow name.

        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def WorkflowType(self):
        r"""Workflow type: cycle or manual.

        :rtype: str
        """
        return self._WorkflowType

    @WorkflowType.setter
    def WorkflowType(self, WorkflowType):
        self._WorkflowType = WorkflowType

    @property
    def OwnerUin(self):
        r"""Owner ID


        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateTime(self):
        r"""Creation time.

        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        r"""Last Modification Time

        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def UpdateUserUin(self):
        r"""Last updated user ID.

        :rtype: str
        """
        return self._UpdateUserUin

    @UpdateUserUin.setter
    def UpdateUserUin(self, UpdateUserUin):
        self._UpdateUserUin = UpdateUserUin

    @property
    def WorkflowDesc(self):
        r"""Workflow description.

        :rtype: str
        """
        return self._WorkflowDesc

    @WorkflowDesc.setter
    def WorkflowDesc(self, WorkflowDesc):
        self._WorkflowDesc = WorkflowDesc

    @property
    def CreateUserUin(self):
        r"""Creator ID.

        :rtype: str
        """
        return self._CreateUserUin

    @CreateUserUin.setter
    def CreateUserUin(self, CreateUserUin):
        self._CreateUserUin = CreateUserUin


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._WorkflowType = params.get("WorkflowType")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._UpdateUserUin = params.get("UpdateUserUin")
        self._WorkflowDesc = params.get("WorkflowDesc")
        self._CreateUserUin = params.get("CreateUserUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowSchedulerConfiguration(AbstractModel):
    r"""Unified workflow scheduling response parameters structure.

    """

    def __init__(self):
        r"""
        :param _ScheduleTimeZone: Specifies the time zone.
        :type ScheduleTimeZone: str
        :param _CycleType: Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :type CycleType: str
        :param _SelfDepend: Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :type SelfDepend: str
        :param _StartTime: Effective Start Time
        :type StartTime: str
        :param _EndTime: Effective End Time.
        :type EndTime: str
        :param _DependencyWorkflow: Workflow dependency. Valid values: yes or no.
        :type DependencyWorkflow: str
        :param _ExecutionStartTime: Execution time. specifies the left-closed interval. example: 00:00.
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: Execution time right closed interval, for example: 23:59.

        :type ExecutionEndTime: str
        :param _CrontabExpression: Cron expression


        :type CrontabExpression: str
        :param _CalendarOpen: Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :type CalendarOpen: str
        :param _CalendarName: Calendar name.
        :type CalendarName: str
        :param _CalendarId: Calendar id.
        :type CalendarId: str
        """
        self._ScheduleTimeZone = None
        self._CycleType = None
        self._SelfDepend = None
        self._StartTime = None
        self._EndTime = None
        self._DependencyWorkflow = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._CrontabExpression = None
        self._CalendarOpen = None
        self._CalendarName = None
        self._CalendarId = None

    @property
    def ScheduleTimeZone(self):
        r"""Specifies the time zone.
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CycleType(self):
        r"""Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def SelfDepend(self):
        r"""Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def StartTime(self):
        r"""Effective Start Time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Effective End Time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DependencyWorkflow(self):
        r"""Workflow dependency. Valid values: yes or no.
        :rtype: str
        """
        return self._DependencyWorkflow

    @DependencyWorkflow.setter
    def DependencyWorkflow(self, DependencyWorkflow):
        self._DependencyWorkflow = DependencyWorkflow

    @property
    def ExecutionStartTime(self):
        r"""Execution time. specifies the left-closed interval. example: 00:00.
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""Execution time right closed interval, for example: 23:59.

        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def CrontabExpression(self):
        r"""Cron expression


        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def CalendarOpen(self):
        r"""Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarName(self):
        r"""Calendar name.
        :rtype: str
        """
        return self._CalendarName

    @CalendarName.setter
    def CalendarName(self, CalendarName):
        self._CalendarName = CalendarName

    @property
    def CalendarId(self):
        r"""Calendar id.
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId


    def _deserialize(self, params):
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CycleType = params.get("CycleType")
        self._SelfDepend = params.get("SelfDepend")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DependencyWorkflow = params.get("DependencyWorkflow")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._CrontabExpression = params.get("CrontabExpression")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarName = params.get("CalendarName")
        self._CalendarId = params.get("CalendarId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowSchedulerConfigurationInfo(AbstractModel):
    r"""Workflow Unified Scheduling Parameter Input - Dependency Task Value Reference:

    Value description table:
    | Current Task Cycle Type | Upstream Task Cycle Type | Configuration Mode | MainCyclicConfig Value | Time Dimension / Instance Scope        | SubordinateCyclicConfig Value     | offset Value                         |
    | ----------------------- | ------------------------ | ------------------ | ---------------------- | -------------------------------------- | --------------------------------- | ------------------------------------ |
    | HOUR_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | DAY_CYCLE               | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Latest Instance              | CURRENT_HOUR                      | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Previous Cycle               | PREVIOUS_HOUR_CYCLE               | None                                 |
    | HOUR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Friday              | PREVIOUS_FRIDAY                   | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Previous Sunday              | PREVIOUS_WEEKEND                  | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | WEEK_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Previous Hour (-60,0]        | PREVIOUS_HOUR_LATER_OFFSET_MINUTE | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Previous Hour                | PREVIOUS_HOUR                     | None                                 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | HOUR                   | By Hour / Current Hour                 | CURRENT_HOUR                      | None                                 |
    | YEAR_CYCLE              | WEEK_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | WEEK_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Recommended Policy | HOUR                   | By Hour / Current Hour                 | CURRENT_HOUR                      | None                                 |
    | HOUR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | ONEOFF_CYCLE             | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | DAY_CYCLE               | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | MONTH_CYCLE             | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | ONEOFF_CYCLE            | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Recommended Policy | MINUTE                 | By Minute / Current Minute             | CURRENT_MINUTE                    | None                                 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Recommended Policy | MINUTE                 | By Minute / Previous Cycle             | PREVIOUS_MINUTE_CYCLE             | None                                 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | ONEOFF_CYCLE            | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Previous Day (-24 * 60,0]     | PREVIOUS_DAY_LATER_OFFSET_MINUTE  | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | WEEK_CYCLE              | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | YEAR_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MINUTE_CYCLE            | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | ONEOFF_CYCLE            | MINUTE_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | HOUR_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Recommended Policy | WEEK                   | By Week / Previous Week                | PREVIOUS_WEEK                     | None                                 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Previous Day (-24,0]          | PREVIOUS_DAY_LATER_OFFSET_HOUR    | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Previous Day [-24,0)          | PREVIOUS_DAY                      | None                                 |
    | DAY_CYCLE               | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / All Months of Current Year  | ALL_MONTH_OF_YEAR                 | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / End of Previous Month       | PREVIOUS_END_OF_MONTH             | None                                 |
    | YEAR_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Beginning of Previous Month | PREVIOUS_BEGIN_OF_MONTH           | None                                 |
    | ONEOFF_CYCLE            | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | DAY_CYCLE               | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | ONEOFF_CYCLE            | HOUR_CYCLE               | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | DAY_CYCLE               | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MINUTE_CYCLE            | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | WEEK_CYCLE              | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | WEEK_CYCLE              | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | YEAR_CYCLE              | ONEOFF_CYCLE             | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / End of Previous Month       | PREVIOUS_END_OF_MONTH             | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | MONTH_CYCLE             | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / All Days of Current Year      | ALL_DAY_OF_YEAR                   | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | YEAR_CYCLE              | DAY_CYCLE                | Recommended Policy | DAY                    | By Day / Previous Day                  | PREVIOUS_DAY                      | None                                 |
    | HOUR_CYCLE              | WEEK_CYCLE               | Recommended Policy | WEEK                   | By Week / Current Week                 | CURRENT_WEEK                      | None                                 |
    | MONTH_CYCLE             | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | MONTH_CYCLE              | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | MONTH                  | By Month / Previous Month              | PREVIOUS_MONTH                    | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | MONTH_CYCLE             | WEEK_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | DAY_CYCLE               | YEAR_CYCLE               | Recommended Policy | YEAR                   | By Year / Current Year                 | CURRENT_YEAR                      | None                                 |
    | DAY_CYCLE               | YEAR_CYCLE               | Recommended Policy | DAY                    | By Day / Instance of Latest Data Time  | RECENT_DATE                       | None                                 |
    | ONEOFF_CYCLE            | ONEOFF_CYCLE             | Recommended Policy | DAY                    | By Day / Current Day                   | CURRENT_DAY                       | None                                 |
    | ONEOFF_CYCLE            | MONTH_CYCLE              | Recommended Policy | MONTH                  | By Month / Current Month               | CURRENT_MONTH                     | None                                 |
    | CRONTAB_CYCLE           | CRONTAB_CYCLE            | Recommended Policy | CRONTAB                | None                                   | CURRENT                           | None                                 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | HOUR_CYCLE               | Custom             | RANGE_HOUR             | Range (hours)                          | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | DAY_CYCLE                | Custom             | RANGE_DAY              | Range (days)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Custom             | RANGE_MINUTE           | Range (minutes)                        | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | HOUR_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | MINUTE_CYCLE            | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | WEEK_CYCLE              | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | HOUR_CYCLE               | Custom             | LIST_HOUR              | List (hours)                           | None                              | Comma-separated integers, e.g., -1,0 |
    | DAY_CYCLE               | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | YEAR_CYCLE              | DAY_CYCLE                | Custom             | LIST_DAY               | List (days)                            | None                              | Comma-separated integers, e.g., -1,0 |
    | MONTH_CYCLE             | MINUTE_CYCLE             | Custom             | LIST_MINUTE            | List (minutes)                         | None                              | Comma-separated integers, e.g., -1,0 |

    """

    def __init__(self):
        r"""
        :param _ScheduleTimeZone: Specifies the time zone.
        :type ScheduleTimeZone: str
        :param _CycleType: Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :type CycleType: str
        :param _SelfDepend: Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :type SelfDepend: str
        :param _StartTime: Effective Start Time
        :type StartTime: str
        :param _EndTime: Effective End Time
        :type EndTime: str
        :param _CrontabExpression: Cron expression
        :type CrontabExpression: str
        :param _DependencyWorkflow: Workflow dependency. Valid values: yes or no.
        :type DependencyWorkflow: str
        :param _ModifyCycleValue: 0: Do not modify
1: Reset the task's upstream dependency configuration to the default value
        :type ModifyCycleValue: str
        :param _ClearLink: The workflow contains cross-workflow dependencies and uses a cron expression for scheduling. If unified scheduling is saved, unsupported dependencies will be disconnected.
        :type ClearLink: bool
        :param _MainCyclicConfig: Takes effect when ModifyCycleValue = 1. Indicates the default modification of the upstream dependency time dimension. Valid values are:
* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :type MainCyclicConfig: str
        :param _SubordinateCyclicConfig: Takes effect when ModifyCycleValue = 1. Indicates the default modification of the upstream dependency - instance scope. Valid values are:
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :type SubordinateCyclicConfig: str
        :param _ExecutionStartTime: Execution time left closed interval, for example: 00:00. only required when the CycleType is MINUTE_CYCLE.
        :type ExecutionStartTime: str
        :param _ExecutionEndTime: Execution time right closed interval, for example: 23:59. only required when the CycleType is MINUTE_CYCLE.
        :type ExecutionEndTime: str
        :param _CalendarOpen: Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :type CalendarOpen: str
        :param _CalendarId: Calendar id.
        :type CalendarId: str
        """
        self._ScheduleTimeZone = None
        self._CycleType = None
        self._SelfDepend = None
        self._StartTime = None
        self._EndTime = None
        self._CrontabExpression = None
        self._DependencyWorkflow = None
        self._ModifyCycleValue = None
        self._ClearLink = None
        self._MainCyclicConfig = None
        self._SubordinateCyclicConfig = None
        self._ExecutionStartTime = None
        self._ExecutionEndTime = None
        self._CalendarOpen = None
        self._CalendarId = None

    @property
    def ScheduleTimeZone(self):
        r"""Specifies the time zone.
        :rtype: str
        """
        return self._ScheduleTimeZone

    @ScheduleTimeZone.setter
    def ScheduleTimeZone(self, ScheduleTimeZone):
        self._ScheduleTimeZone = ScheduleTimeZone

    @property
    def CycleType(self):
        r"""Period type. Supported types:

ONEOFF_CYCLE: specifies a one-time cycle.
YEAR_CYCLE: specifies the year cycle.
MONTH_CYCLE: specifies the monthly cycle.
WEEK_CYCLE: specifies the week cycle.
DAY_CYCLE: specifies the day cycle.
HOUR_CYCLE: specifies the hour cycle.
MINUTE_CYCLE: specifies the minute cycle.
CRONTAB_CYCLE: specifies the crontab expression type
        :rtype: str
        """
        return self._CycleType

    @CycleType.setter
    def CycleType(self, CycleType):
        self._CycleType = CycleType

    @property
    def SelfDepend(self):
        r"""Self-Dependent. Valid values: parallel, serial, orderly. Default value: serial. 
        :rtype: str
        """
        return self._SelfDepend

    @SelfDepend.setter
    def SelfDepend(self, SelfDepend):
        self._SelfDepend = SelfDepend

    @property
    def StartTime(self):
        r"""Effective Start Time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Effective End Time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CrontabExpression(self):
        r"""Cron expression
        :rtype: str
        """
        return self._CrontabExpression

    @CrontabExpression.setter
    def CrontabExpression(self, CrontabExpression):
        self._CrontabExpression = CrontabExpression

    @property
    def DependencyWorkflow(self):
        r"""Workflow dependency. Valid values: yes or no.
        :rtype: str
        """
        return self._DependencyWorkflow

    @DependencyWorkflow.setter
    def DependencyWorkflow(self, DependencyWorkflow):
        self._DependencyWorkflow = DependencyWorkflow

    @property
    def ModifyCycleValue(self):
        r"""0: Do not modify
1: Reset the task's upstream dependency configuration to the default value
        :rtype: str
        """
        return self._ModifyCycleValue

    @ModifyCycleValue.setter
    def ModifyCycleValue(self, ModifyCycleValue):
        self._ModifyCycleValue = ModifyCycleValue

    @property
    def ClearLink(self):
        r"""The workflow contains cross-workflow dependencies and uses a cron expression for scheduling. If unified scheduling is saved, unsupported dependencies will be disconnected.
        :rtype: bool
        """
        return self._ClearLink

    @ClearLink.setter
    def ClearLink(self, ClearLink):
        self._ClearLink = ClearLink

    @property
    def MainCyclicConfig(self):
        r"""Takes effect when ModifyCycleValue = 1. Indicates the default modification of the upstream dependency time dimension. Valid values are:
* CRONTAB
* DAY
* HOUR
* LIST_DAY
* LIST_HOUR
* LIST_MINUTE
* MINUTE
* MONTH
* RANGE_DAY
* RANGE_HOUR
* RANGE_MINUTE
* WEEK
* YEAR

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :rtype: str
        """
        return self._MainCyclicConfig

    @MainCyclicConfig.setter
    def MainCyclicConfig(self, MainCyclicConfig):
        self._MainCyclicConfig = MainCyclicConfig

    @property
    def SubordinateCyclicConfig(self):
        r"""Takes effect when ModifyCycleValue = 1. Indicates the default modification of the upstream dependency - instance scope. Valid values are:
* ALL_DAY_OF_YEAR
* ALL_MONTH_OF_YEAR
* CURRENT
* CURRENT_DAY
* CURRENT_HOUR
* CURRENT_MINUTE
* CURRENT_MONTH
* CURRENT_WEEK
* CURRENT_YEAR
* PREVIOUS_BEGIN_OF_MONTH
* PREVIOUS_DAY
* PREVIOUS_DAY_LATER_OFFSET_HOUR
* PREVIOUS_DAY_LATER_OFFSET_MINUTE
* PREVIOUS_END_OF_MONTH
* PREVIOUS_FRIDAY
* PREVIOUS_HOUR
* PREVIOUS_HOUR_CYCLE
* PREVIOUS_HOUR_LATER_OFFSET_MINUTE
* PREVIOUS_MINUTE_CYCLE
* PREVIOUS_MONTH
* PREVIOUS_WEEK
* PREVIOUS_WEEKEND
* RECENT_DATE

https://capi.woa.com/object/detail?product=wedata&env=api_dev&version=2025-08-06&name=WorkflowSchedulerConfigurationInfo
        :rtype: str
        """
        return self._SubordinateCyclicConfig

    @SubordinateCyclicConfig.setter
    def SubordinateCyclicConfig(self, SubordinateCyclicConfig):
        self._SubordinateCyclicConfig = SubordinateCyclicConfig

    @property
    def ExecutionStartTime(self):
        r"""Execution time left closed interval, for example: 00:00. only required when the CycleType is MINUTE_CYCLE.
        :rtype: str
        """
        return self._ExecutionStartTime

    @ExecutionStartTime.setter
    def ExecutionStartTime(self, ExecutionStartTime):
        self._ExecutionStartTime = ExecutionStartTime

    @property
    def ExecutionEndTime(self):
        r"""Execution time right closed interval, for example: 23:59. only required when the CycleType is MINUTE_CYCLE.
        :rtype: str
        """
        return self._ExecutionEndTime

    @ExecutionEndTime.setter
    def ExecutionEndTime(self, ExecutionEndTime):
        self._ExecutionEndTime = ExecutionEndTime

    @property
    def CalendarOpen(self):
        r"""Whether calendar scheduling is enabled. Valid values: 1 (enabled), 0 (disabled).
        :rtype: str
        """
        return self._CalendarOpen

    @CalendarOpen.setter
    def CalendarOpen(self, CalendarOpen):
        self._CalendarOpen = CalendarOpen

    @property
    def CalendarId(self):
        r"""Calendar id.
        :rtype: str
        """
        return self._CalendarId

    @CalendarId.setter
    def CalendarId(self, CalendarId):
        self._CalendarId = CalendarId


    def _deserialize(self, params):
        self._ScheduleTimeZone = params.get("ScheduleTimeZone")
        self._CycleType = params.get("CycleType")
        self._SelfDepend = params.get("SelfDepend")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CrontabExpression = params.get("CrontabExpression")
        self._DependencyWorkflow = params.get("DependencyWorkflow")
        self._ModifyCycleValue = params.get("ModifyCycleValue")
        self._ClearLink = params.get("ClearLink")
        self._MainCyclicConfig = params.get("MainCyclicConfig")
        self._SubordinateCyclicConfig = params.get("SubordinateCyclicConfig")
        self._ExecutionStartTime = params.get("ExecutionStartTime")
        self._ExecutionEndTime = params.get("ExecutionEndTime")
        self._CalendarOpen = params.get("CalendarOpen")
        self._CalendarId = params.get("CalendarId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        