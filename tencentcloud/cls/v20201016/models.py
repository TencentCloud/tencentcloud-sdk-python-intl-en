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


class AlarmInfo(AbstractModel):
    """Alarm policy description

    """

    def __init__(self):
        r"""
        :param Name: Alarm policy name
        :type Name: str
        :param AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTargetInfo
        :param MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: Trigger condition
        :type Condition: str
        :param TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param Status: Enablement status
        :type Status: bool
        :param AlarmId: Alarm policy ID
        :type AlarmId: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Last update time
        :type UpdateTime: str
        :param MessageTemplate: Custom notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MessageTemplate: str
        :param CallBack: Custom callback template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param Analysis: Multi-Dimensional analysis settings
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Analysis: list of AnalysisDimensional
        """
        self.Name = None
        self.AlarmTargets = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.Status = None
        self.AlarmId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MessageTemplate = None
        self.CallBack = None
        self.Analysis = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTargetInfo()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        self.Status = params.get("Status")
        self.AlarmId = params.get("AlarmId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmNotice(AbstractModel):
    """Alarm notification template type

    """

    def __init__(self):
        r"""
        :param Name: Alarm notification template name
        :type Name: str
        :param Type: Alarm template type. Valid values:
<br><li> `Trigger`: alarm triggered
<br><li> `Recovery`: alarm cleared
<br><li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param NoticeReceivers: Information of the recipient in alarm notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: Callback information of alarm notification template
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebCallbacks: list of WebCallback
        :param AlarmNoticeId: Alarm notification template ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNoticeId: str
        :param CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Last update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None
        self.AlarmNoticeId = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTarget(AbstractModel):
    """Monitoring object

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Query: Query statement
        :type Query: str
        :param Number: Monitoring object number, which is incremental from 1.
        :type Number: int
        :param StartTimeOffset: Offset of the query start time from the alarm execution time in minutes. The value cannot be positive. Value range: -1440–0.
        :type StartTimeOffset: int
        :param EndTimeOffset: Offset of the query end time from the alarm execution time in minutes. The value cannot be positive and must be greater than `StartTimeOffset`. Value range: -1440–0.
        :type EndTimeOffset: int
        :param LogsetId: Logset ID
        :type LogsetId: str
        """
        self.TopicId = None
        self.Query = None
        self.Number = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.LogsetId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Query = params.get("Query")
        self.Number = params.get("Number")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTargetInfo(AbstractModel):
    """Alarm object

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param LogsetName: Logset name
        :type LogsetName: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param TopicName: Log topic name
        :type TopicName: str
        :param Query: Query statement
        :type Query: str
        :param Number: Monitoring object number
        :type Number: int
        :param StartTimeOffset: Offset of the query start time from the alarm execution time in minutes. The value cannot be positive. Value range: -1440–0.
        :type StartTimeOffset: int
        :param EndTimeOffset: Offset of the query end time from the alarm execution time in minutes. The value cannot be positive and must be greater than `StartTimeOffset`. Value range: -1440–0.
        :type EndTimeOffset: int
        """
        self.LogsetId = None
        self.LogsetName = None
        self.TopicId = None
        self.TopicName = None
        self.Query = None
        self.Number = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Query = params.get("Query")
        self.Number = params.get("Number")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisDimensional(AbstractModel):
    """Multi-Dimensional analysis dimension

    """

    def __init__(self):
        r"""
        :param Name: Analysis name
        :type Name: str
        :param Type: Analysis type. Valid values: `query`, `field`
        :type Type: str
        :param Content: Analysis content
        :type Content: str
        """
        self.Name = None
        self.Type = None
        self.Content = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupRequest(AbstractModel):
    """ApplyConfigToMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection configuration ID
        :type ConfigId: str
        :param GroupId: Machine group ID
        :type GroupId: str
        """
        self.ConfigId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConfigToMachineGroupResponse(AbstractModel):
    """ApplyConfigToMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallBackInfo(AbstractModel):
    """Callback configuration

    """

    def __init__(self):
        r"""
        :param Body: `Body` during callback
        :type Body: str
        :param Headers: `Headers` during callback
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Headers: list of str
        """
        self.Body = None
        self.Headers = None


    def _deserialize(self, params):
        self.Body = params.get("Body")
        self.Headers = params.get("Headers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ckafka(AbstractModel):
    """Information of the CKafka instance to ship to

    """

    def __init__(self):
        r"""
        :param Vip: CKafka VIP
        :type Vip: str
        :param Vport: CKafka Vport
        :type Vport: str
        :param InstanceId: CKafka instance ID
        :type InstanceId: str
        :param InstanceName: CKafka instance name
        :type InstanceName: str
        :param TopicId: CKafka topic ID
        :type TopicId: str
        :param TopicName: CKafka topic name
        :type TopicName: str
        """
        self.Vip = None
        self.Vport = None
        self.InstanceId = None
        self.InstanceName = None
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerRequest(AbstractModel):
    """CloseKafkaConsumer request structure.

    """

    def __init__(self):
        r"""
        :param FromTopicId: CLS topic identifier
        :type FromTopicId: str
        """
        self.FromTopicId = None


    def _deserialize(self, params):
        self.FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseKafkaConsumerResponse(AbstractModel):
    """CloseKafkaConsumer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Column(AbstractModel):
    """Column attribute of log analysis

    """

    def __init__(self):
        r"""
        :param Name: Column name
        :type Name: str
        :param Type: Column attribute
        :type Type: str
        """
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressInfo(AbstractModel):
    """Compression configuration of shipped log

    """

    def __init__(self):
        r"""
        :param Format: Compression format. Valid values: `gzip`, `lzop`, `none` (no compression)
        :type Format: str
        """
        self.Format = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigInfo(AbstractModel):
    """Collection rule configuration information

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection rule configuration ID
        :type ConfigId: str
        :param LogFormat: Log formatting method
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogFormat: str
        :param Path: Log collection path
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogType: str
        :param ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: Collection path blocklist
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExcludePaths: list of ExcludePathInfo
        :param Output: Log topic ID (TopicId) of collection configuration
        :type Output: str
        :param UpdateTime: Update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UserDefineRule: Custom parsing string
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UserDefineRule: str
        """
        self.ConfigId = None
        self.LogFormat = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None
        self.Output = None
        self.UpdateTime = None
        self.CreateTime = None
        self.UserDefineRule = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.LogFormat = params.get("LogFormat")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        self.Output = params.get("Output")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerContent(AbstractModel):
    """Shipping content

    """

    def __init__(self):
        r"""
        :param EnableTag: Whether to ship tag information
Note: This field may return `null`, indicating that no valid value was found.
        :type EnableTag: bool
        :param MetaFields: List of metadata to ship. Only \_\_SOURCE\_\_, \_\_FILENAME\_\_, and \_\_TIMESTAMP\_\_ are supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetaFields: list of str
        :param TagJsonNotTiled: This parameter is required if `EnableTag` is `true`, and is used to specify whether the tag information is JSON tiled. Valid values: `true` (not tiled); `false` (tiled)
Note: This field may return `null`, indicating that no valid value was found.
        :type TagJsonNotTiled: bool
        :param TimestampAccuracy: Shipping timestamp precision in seconds (default) or milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimestampAccuracy: int
        """
        self.EnableTag = None
        self.MetaFields = None
        self.TagJsonNotTiled = None
        self.TimestampAccuracy = None


    def _deserialize(self, params):
        self.EnableTag = params.get("EnableTag")
        self.MetaFields = params.get("MetaFields")
        self.TagJsonNotTiled = params.get("TagJsonNotTiled")
        self.TimestampAccuracy = params.get("TimestampAccuracy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentInfo(AbstractModel):
    """Format configuration of shipped log content

    """

    def __init__(self):
        r"""
        :param Format: Content format. Valid values: `json`, `csv`
        :type Format: str
        :param Csv: CSV format content description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Csv: :class:`tencentcloud.cls.v20201016.models.CsvInfo`
        :param Json: JSON format content description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Json: :class:`tencentcloud.cls.v20201016.models.JsonInfo`
        :param Parquet: `Parquet` format description
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Parquet: :class:`tencentcloud.cls.v20201016.models.ParquetInfo`
        """
        self.Format = None
        self.Csv = None
        self.Json = None
        self.Parquet = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("Csv") is not None:
            self.Csv = CsvInfo()
            self.Csv._deserialize(params.get("Csv"))
        if params.get("Json") is not None:
            self.Json = JsonInfo()
            self.Json._deserialize(params.get("Json"))
        if params.get("Parquet") is not None:
            self.Parquet = ParquetInfo()
            self.Parquet._deserialize(params.get("Parquet"))
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
        :param Name: Notification group name
        :type Name: str
        :param Type: Notification type. Valid values:
<li> `Trigger`: alarm triggered
<li> `Recovery`: alarm cleared
<li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param NoticeReceivers: Notification recipient
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: API callback information (including WeCom)
        :type WebCallbacks: list of WebCallback
        """
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
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
        :param AlarmNoticeId: Alarm template ID
        :type AlarmNoticeId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AlarmNoticeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.RequestId = params.get("RequestId")


class CreateAlarmRequest(AbstractModel):
    """CreateAlarm request structure.

    """

    def __init__(self):
        r"""
        :param Name: Alarm policy name
        :type Name: str
        :param AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTarget
        :param MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: Trigger condition
        :type Condition: str
        :param TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param Status: Whether to enable the alarm policy. Default value: true
        :type Status: bool
        :param MessageTemplate: Custom alarm content
        :type MessageTemplate: str
        :param CallBack: Custom callback
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param Analysis: Multi-Dimensional analysis
        :type Analysis: list of AnalysisDimensional
        """
        self.Name = None
        self.AlarmTargets = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.Status = None
        self.MessageTemplate = None
        self.CallBack = None
        self.Analysis = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        self.Status = params.get("Status")
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlarmResponse(AbstractModel):
    """CreateAlarm response structure.

    """

    def __init__(self):
        r"""
        :param AlarmId: Alarm policy ID.
        :type AlarmId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AlarmId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig request structure.

    """

    def __init__(self):
        r"""
        :param Name: Collection configuration name
        :type Name: str
        :param Output: Log topic ID (TopicId) of collection configuration
        :type Output: str
        :param Path: Log collection path containing the filename
        :type Path: str
        :param LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
        :type LogType: str
        :param ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: Collection path blocklist
        :type ExcludePaths: list of ExcludePathInfo
        :param UserDefineRule: Custom collection rule, which is a serialized JSON string
        :type UserDefineRule: str
        """
        self.Name = None
        self.Output = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None
        self.UserDefineRule = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Output = params.get("Output")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        self.UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig response structure.

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection configuration ID
        :type ConfigId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class CreateConsumerRequest(AbstractModel):
    """CreateConsumer request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID to bind
        :type TopicId: str
        :param NeedContent: Whether to ship log metadata. Default value: `true`
        :type NeedContent: bool
        :param Content: Metadata to ship if `NeedContent` is `true`
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        """
        self.TopicId = None
        self.NeedContent = None
        self.Content = None
        self.Ckafka = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self.Content = ConsumerContent()
            self.Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self.Ckafka = Ckafka()
            self.Ckafka._deserialize(params.get("Ckafka"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerResponse(AbstractModel):
    """CreateConsumer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateExportRequest(AbstractModel):
    """CreateExport request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Count: Number of logs to be exported. Maximum value: 50 million
        :type Count: int
        :param Query: Search statements for log export. <a href="https://intl.cloud.tencent.com/document/product/614/44061?from_cn_redirect=1" target="_blank">[SQL statements]</a> are not supported.
        :type Query: str
        :param From: Start time of the log to be exported, which is a timestamp in milliseconds
        :type From: int
        :param To: End time of the log to be exported, which is a timestamp in milliseconds
        :type To: int
        :param Order: Exported log sorting order by time. Valid values: `asc`: ascending; `desc`: descending. Default value: `desc`
        :type Order: str
        :param Format: Exported log data format. Valid values: `json`, `csv`. Default value: `json`
        :type Format: str
        """
        self.TopicId = None
        self.Count = None
        self.Query = None
        self.From = None
        self.To = None
        self.Order = None
        self.Format = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Count = params.get("Count")
        self.Query = params.get("Query")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExportResponse(AbstractModel):
    """CreateExport response structure.

    """

    def __init__(self):
        r"""
        :param ExportId: Log export ID.
        :type ExportId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ExportId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        self.RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Rule: Index rule
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param Status: Whether to take effect. Default value: true
        :type Status: bool
        :param IncludeInternalFields: Internal field marker of full-text index. Default value: `false`. Valid value: `false`: excluding internal fields; `true`: including internal fields
        :type IncludeInternalFields: bool
        :param MetadataFlag: Metadata flag. Default value: `0`. Valid value: `0`: full-text index (including the metadata field with key-value index enabled); `1`: full-text index (including all metadata fields); `2`: full-text index (excluding metadata fields).
        :type MetadataFlag: int
        """
        self.TopicId = None
        self.Rule = None
        self.Status = None
        self.IncludeInternalFields = None
        self.MetadataFlag = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.Status = params.get("Status")
        self.IncludeInternalFields = params.get("IncludeInternalFields")
        self.MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLogsetRequest(AbstractModel):
    """CreateLogset request structure.

    """

    def __init__(self):
        r"""
        :param LogsetName: Logset name, which must be unique
        :type LogsetName: str
        :param Tags: Tag description list. Up to 10 tag key-value pairs are supported and must be unique.
        :type Tags: list of Tag
        """
        self.LogsetName = None
        self.Tags = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
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
        


class CreateLogsetResponse(AbstractModel):
    """CreateLogset response structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogsetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.RequestId = params.get("RequestId")


class CreateMachineGroupRequest(AbstractModel):
    """CreateMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupName: Machine group name, which must be unique
        :type GroupName: str
        :param MachineGroupType: Type of the machine group to be created. Valid values: `ip`: use the IP string list in `Values` to create a machine group; `label`: use the tag string list in `Values` to create a machine group
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param Tags: Tag description list. This parameter is used to bind a tag to a machine group. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key.
        :type Tags: list of Tag
        :param AutoUpdate: Whether to enable automatic update for the machine group
        :type AutoUpdate: bool
        :param UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
        :type UpdateStartTime: str
        :param UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
        :type UpdateEndTime: str
        :param ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees
        :type ServiceLogging: bool
        """
        self.GroupName = None
        self.MachineGroupType = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMachineGroupResponse(AbstractModel):
    """CreateMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateShipperRequest(AbstractModel):
    """CreateShipper request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the log topic to which the shipping rule to be created belongs
        :type TopicId: str
        :param Bucket: Destination bucket in the shipping rule to be created
        :type Bucket: str
        :param Prefix: Prefix of the shipping directory in the shipping rule to be created
        :type Prefix: str
        :param ShipperName: Shipping rule name
        :type ShipperName: str
        :param Interval: Interval between shipping tasks (in sec). Default value: 300. Value range: 300-900
        :type Interval: int
        :param MaxSize: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100-256
        :type MaxSize: int
        :param FilterRules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :type FilterRules: list of FilterRuleInfo
        :param Partition: Rules for partitioning logs to be shipped. `strftime` can be used to define the presentation of time format.
        :type Partition: str
        :param Compress: Compression configuration of shipped log
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: Format configuration of shipped log content
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        self.TopicId = None
        self.Bucket = None
        self.Prefix = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShipperResponse(AbstractModel):
    """CreateShipper response structure.

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ShipperId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicName: Log topic name
        :type TopicName: str
        :param PartitionCount: Number of log topic partitions. Default value: 1. Maximum value: 10
        :type PartitionCount: int
        :param Tags: Tag description list. This parameter is used to bind a tag to a log topic. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key.
        :type Tags: list of Tag
        :param AutoSplit: Whether to enable automatic split. Default value: true
        :type AutoSplit: bool
        :param MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled. Default value: 50
        :type MaxSplitPartitions: int
        :param StorageType: Log topic storage type. Valid values: `hot` (STANDARD storage); `cold` (IA storage). Default value: `hot`.
        :type StorageType: str
        :param Period: Lifecycle in days. Value range: 1-3600 (3640 indicates permanent retention)
        :type Period: int
        """
        self.LogsetId = None
        self.TopicName = None
        self.PartitionCount = None
        self.Tags = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.StorageType = None
        self.Period = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        self.StorageType = params.get("StorageType")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CsvInfo(AbstractModel):
    """CSV content description

    """

    def __init__(self):
        r"""
        :param PrintKey: Whether to print `key` on the first row of the CSV file
        :type PrintKey: bool
        :param Keys: Names of keys
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Keys: list of str
        :param Delimiter: Field delimiter
        :type Delimiter: str
        :param EscapeChar: Escape character used to enclose any field delimiter in field content. You can enter only a single quotation mark, double quotation mark, or an empty string.
        :type EscapeChar: str
        :param NonExistingField: Content used to populate non-existing fields
        :type NonExistingField: str
        """
        self.PrintKey = None
        self.Keys = None
        self.Delimiter = None
        self.EscapeChar = None
        self.NonExistingField = None


    def _deserialize(self, params):
        self.PrintKey = params.get("PrintKey")
        self.Keys = params.get("Keys")
        self.Delimiter = params.get("Delimiter")
        self.EscapeChar = params.get("EscapeChar")
        self.NonExistingField = params.get("NonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeRequest(AbstractModel):
    """DeleteAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param AlarmNoticeId: Notification group ID
        :type AlarmNoticeId: str
        """
        self.AlarmNoticeId = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmNoticeResponse(AbstractModel):
    """DeleteAlarmNotice response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAlarmRequest(AbstractModel):
    """DeleteAlarm request structure.

    """

    def __init__(self):
        r"""
        :param AlarmId: Alarm policy ID.
        :type AlarmId: str
        """
        self.AlarmId = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlarmResponse(AbstractModel):
    """DeleteAlarm response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConfigFromMachineGroupRequest(AbstractModel):
    """DeleteConfigFromMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        :param ConfigId: Collection configuration ID
        :type ConfigId: str
        """
        self.GroupId = None
        self.ConfigId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFromMachineGroupResponse(AbstractModel):
    """DeleteConfigFromMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig request structure.

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection rule configuration ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConsumerRequest(AbstractModel):
    """DeleteConsumer request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID bound to the task
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerResponse(AbstractModel):
    """DeleteConsumer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteExportRequest(AbstractModel):
    """DeleteExport request structure.

    """

    def __init__(self):
        r"""
        :param ExportId: Log export ID
        :type ExportId: str
        """
        self.ExportId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteExportResponse(AbstractModel):
    """DeleteExport response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogsetRequest(AbstractModel):
    """DeleteLogset request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        """
        self.LogsetId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogsetResponse(AbstractModel):
    """DeleteLogset response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineGroupRequest(AbstractModel):
    """DeleteMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineGroupResponse(AbstractModel):
    """DeleteMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteShipperRequest(AbstractModel):
    """DeleteShipper request structure.

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        """
        self.ShipperId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShipperResponse(AbstractModel):
    """DeleteShipper response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAlarmNoticesRequest(AbstractModel):
    """DescribeAlarmNotices request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <li> name
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
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
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
        


class DescribeAlarmNoticesResponse(AbstractModel):
    """DescribeAlarmNotices response structure.

    """

    def __init__(self):
        r"""
        :param AlarmNotices: Alarm notification template list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AlarmNotices: list of AlarmNotice
        :param TotalCount: Total number of eligible alarm notification templates
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AlarmNotices = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmNotices") is not None:
            self.AlarmNotices = []
            for item in params.get("AlarmNotices"):
                obj = AlarmNotice()
                obj._deserialize(item)
                self.AlarmNotices.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> name

Filter by **alarm policy name**
Type: string

Required: no

<br><li> alarmId

Filter by **alarm policy ID**
Type: string

Required: no

<br><li> topicId

Filter by **log topic ID**

Type: string

Required: no

<br><li> enable

Filter by **enablement status**

Type: string

Note: The valid values of `enable` include `1`, `t`, `T`, `TRUE`, `true`, `True`, `0`, `f`, `F`, `FALSE`, `false`, and `False`. If other values are entered, an “invalid parameter” error will be returned.

Required: no

Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
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
        


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms response structure.

    """

    def __init__(self):
        r"""
        :param Alarms: Alarm policy list
        :type Alarms: list of AlarmInfo
        :param TotalCount: Number of eligible alarm policies
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Alarms = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeConfigMachineGroupsRequest(AbstractModel):
    """DescribeConfigMachineGroups request structure.

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection configuration ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMachineGroupsResponse(AbstractModel):
    """DescribeConfigMachineGroups response structure.

    """

    def __init__(self):
        r"""
        :param MachineGroups: List of machine groups bound to the collection rule configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MachineGroups: list of MachineGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MachineGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self.MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self.MachineGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> configName

Filter by fuzzy match of **collection configuration name**
Type: String

Required: no

<br><li> configId

Filter by **collection configuration ID**.
Type: String

Required: no

<br><li> topicId

Filter by **log topic**.

Type: String

Required: no

Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
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
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs response structure.

    """

    def __init__(self):
        r"""
        :param Configs: Collection configuration list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Configs: list of ConfigInfo
        :param TotalCount: Total number of filtered items
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Configs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeConsumerRequest(AbstractModel):
    """DescribeConsumer request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID bound to the task
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerResponse(AbstractModel):
    """DescribeConsumer response structure.

    """

    def __init__(self):
        r"""
        :param Effective: Whether the shipping task is effective
        :type Effective: bool
        :param NeedContent: Whether log metadata is shipped
        :type NeedContent: bool
        :param Content: Metadata shipped if `NeedContent` is `true`
Note: This field may return `null`, indicating that no valid value was found.
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Effective = None
        self.NeedContent = None
        self.Content = None
        self.Ckafka = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Effective = params.get("Effective")
        self.NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self.Content = ConsumerContent()
            self.Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self.Ckafka = Ckafka()
            self.Ckafka._deserialize(params.get("Ckafka"))
        self.RequestId = params.get("RequestId")


class DescribeExportsRequest(AbstractModel):
    """DescribeExports request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
        :type Limit: int
        """
        self.TopicId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportsResponse(AbstractModel):
    """DescribeExports response structure.

    """

    def __init__(self):
        r"""
        :param Exports: List of exported logs
        :type Exports: list of ExportInfo
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Exports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Exports") is not None:
            self.Exports = []
            for item in params.get("Exports"):
                obj = ExportInfo()
                obj._deserialize(item)
                self.Exports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIndexRequest(AbstractModel):
    """DescribeIndex request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexResponse(AbstractModel):
    """DescribeIndex response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Status: Whether it takes effect
        :type Status: bool
        :param Rule: Index configuration information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param ModifyTime: Index modification time. The default value is the index creation time.
        :type ModifyTime: str
        :param IncludeInternalFields: Internal field marker of full-text index. Default value: `false`. Valid value: `false`: excluding internal fields; `true`: including internal fields
Note: This field may return `null`, indicating that no valid value was found.
        :type IncludeInternalFields: bool
        :param MetadataFlag: Metadata flag. Default value: `0`. Valid value: `0`: full-text index (including the metadata field with key-value index enabled); `1`: full-text index (including all metadata fields); `2`: full-text index (excluding metadata fields).
Note: This field may return `null`, indicating that no valid value was found.
        :type MetadataFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.Status = None
        self.Rule = None
        self.ModifyTime = None
        self.IncludeInternalFields = None
        self.MetadataFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Status = params.get("Status")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.ModifyTime = params.get("ModifyTime")
        self.IncludeInternalFields = params.get("IncludeInternalFields")
        self.MetadataFlag = params.get("MetadataFlag")
        self.RequestId = params.get("RequestId")


class DescribeLogContextRequest(AbstractModel):
    """DescribeLogContext request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID to be queried
        :type TopicId: str
        :param BTime: Log time in the format of YYYY-mm-dd HH:MM:SS.FFF
        :type BTime: str
        :param PkgId: Log package number
        :type PkgId: str
        :param PkgLogId: Log number in log package
        :type PkgLogId: int
        :param PrevLogs: Number of previous logs. Default value: 10
        :type PrevLogs: int
        :param NextLogs: Number of next logs. Default value: 10
        :type NextLogs: int
        """
        self.TopicId = None
        self.BTime = None
        self.PkgId = None
        self.PkgLogId = None
        self.PrevLogs = None
        self.NextLogs = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.BTime = params.get("BTime")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.PrevLogs = params.get("PrevLogs")
        self.NextLogs = params.get("NextLogs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogContextResponse(AbstractModel):
    """DescribeLogContext response structure.

    """

    def __init__(self):
        r"""
        :param LogContextInfos: Log context information set
        :type LogContextInfos: list of LogContextInfo
        :param PrevOver: Whether the previous logs have been returned
        :type PrevOver: bool
        :param NextOver: Whether the next logs have been returned
        :type NextOver: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogContextInfos = None
        self.PrevOver = None
        self.NextOver = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogContextInfos") is not None:
            self.LogContextInfos = []
            for item in params.get("LogContextInfos"):
                obj = LogContextInfo()
                obj._deserialize(item)
                self.LogContextInfos.append(obj)
        self.PrevOver = params.get("PrevOver")
        self.NextOver = params.get("NextOver")
        self.RequestId = params.get("RequestId")


class DescribeLogHistogramRequest(AbstractModel):
    """DescribeLogHistogram request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the log topic to be queried
        :type TopicId: str
        :param From: Start time of the log to be queried, which is a Unix timestamp in milliseconds
        :type From: int
        :param To: End time of the log to be queried, which is a Unix timestamp in milliseconds
        :type To: int
        :param Query: Query statement
        :type Query: str
        :param Interval: Time interval in milliseconds
        :type Interval: int
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Interval = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogHistogramResponse(AbstractModel):
    """DescribeLogHistogram response structure.

    """

    def __init__(self):
        r"""
        :param Interval: Statistical period in milliseconds
        :type Interval: int
        :param TotalCount: The number of logs that hit the keywords
        :type TotalCount: int
        :param HistogramInfos: Statistical result details within the period
        :type HistogramInfos: list of HistogramInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.TotalCount = None
        self.HistogramInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        self.TotalCount = params.get("TotalCount")
        if params.get("HistogramInfos") is not None:
            self.HistogramInfos = []
            for item in params.get("HistogramInfos"):
                obj = HistogramInfo()
                obj._deserialize(item)
                self.HistogramInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogsetsRequest(AbstractModel):
    """DescribeLogsets request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> logsetName

Filter by **logset name**.
Type: String

Required: no

<br><li> logsetId

Filter by **logset ID**.
Type: String

Required: no

<br><li> tagKey

Filter by **tag key**.

Type: String

Required: no

<br><li> tag:tagKey

Filter by **tag key-value pair**. The `tagKey` should be replaced with a specified tag key.
Type: String

Required: no


Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
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
        


class DescribeLogsetsResponse(AbstractModel):
    """DescribeLogsets response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of pages
        :type TotalCount: int
        :param Logsets: Logset list
        :type Logsets: list of LogsetInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logsets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logsets") is not None:
            self.Logsets = []
            for item in params.get("Logsets"):
                obj = LogsetInfo()
                obj._deserialize(item)
                self.Logsets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineGroupConfigsRequest(AbstractModel):
    """DescribeMachineGroupConfigs request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineGroupConfigsResponse(AbstractModel):
    """DescribeMachineGroupConfigs response structure.

    """

    def __init__(self):
        r"""
        :param Configs: Collection rule configuration list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Configs: list of ConfigInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Configs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = ConfigInfo()
                obj._deserialize(item)
                self.Configs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineGroupsRequest(AbstractModel):
    """DescribeMachineGroups request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> machineGroupName

Filter by **machine group name**.
Type: String

Required: no

<br><li> machineGroupId

Filter by **machine group ID**.
Type: String

Required: no

<br><li> tagKey

Filter by **tag key**.

Type: String

Required: no

<br><li> tag:tagKey

Filter by **tag key-value pair**. The `tagKey` should be replaced with a specified tag key.
Type: String

Required: no


Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
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
        


class DescribeMachineGroupsResponse(AbstractModel):
    """DescribeMachineGroups response structure.

    """

    def __init__(self):
        r"""
        :param MachineGroups: Machine group information list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MachineGroups: list of MachineGroupInfo
        :param TotalCount: Total number of pages
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MachineGroups = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MachineGroups") is not None:
            self.MachineGroups = []
            for item in params.get("MachineGroups"):
                obj = MachineGroupInfo()
                obj._deserialize(item)
                self.MachineGroups.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: ID of the machine group to be queried
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines response structure.

    """

    def __init__(self):
        r"""
        :param Machines: Group of machine status information
        :type Machines: list of MachineInfo
        :param AutoUpdate: Whether to enable the automatic update feature for the machine group
        :type AutoUpdate: int
        :param UpdateStartTime: Preset start time of automatic update of machine group
        :type UpdateStartTime: str
        :param UpdateEndTime: Preset end time of automatic update of machine group
        :type UpdateEndTime: str
        :param LatestAgentVersion: Latest LogListener version available to the current user
        :type LatestAgentVersion: str
        :param ServiceLogging: Whether to enable the service log
        :type ServiceLogging: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Machines = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.LatestAgentVersion = None
        self.ServiceLogging = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = MachineInfo()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.LatestAgentVersion = params.get("LatestAgentVersion")
        self.ServiceLogging = params.get("ServiceLogging")
        self.RequestId = params.get("RequestId")


class DescribePartitionsRequest(AbstractModel):
    """DescribePartitions request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePartitionsResponse(AbstractModel):
    """DescribePartitions response structure.

    """

    def __init__(self):
        r"""
        :param Partitions: Partition list
        :type Partitions: list of PartitionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShipperTasksRequest(AbstractModel):
    """DescribeShipperTasks request structure.

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        :param StartTime: Query start timestamp in milliseconds, which can be within the last three days
        :type StartTime: int
        :param EndTime: Query end timestamp in milliseconds
        :type EndTime: int
        """
        self.ShipperId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShipperTasksResponse(AbstractModel):
    """DescribeShipperTasks response structure.

    """

    def __init__(self):
        r"""
        :param Tasks: Shipping task list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tasks: list of ShipperTaskInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ShipperTaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShippersRequest(AbstractModel):
    """DescribeShippers request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> shipperName

Filter by **shipping rule name**.
Type: String

Required: no

<br><li> shipperId

Filter by **shipping rule ID**.
Type: String

Required: no

<br><li> topicId

Filter by **log topic**.

Type: String

Required: no

Each request can contain up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100
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
        


class DescribeShippersResponse(AbstractModel):
    """DescribeShippers response structure.

    """

    def __init__(self):
        r"""
        :param Shippers: Shipping rule list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Shippers: list of ShipperInfo
        :param TotalCount: Total number of results obtained in this query
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Shippers = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Shippers") is not None:
            self.Shippers = []
            for item in params.get("Shippers"):
                obj = ShipperInfo()
                obj._deserialize(item)
                self.Shippers.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <br><li> `topicName` filters by **log topic name**. Type: String. Required: No<br><li> `logsetName` filters by **logset name**. Type: String. Required: No<br><li> `topicId` filters by **log topic ID**. Type: String. Required: No<br><li> `logsetId` filters by **logset ID**. You can call the `DescribeLogsets` API to query the list of created logsets or log in to the console to view them. You can also call the `CreateLogset` API to create a logset. Type: String. Required: No<br><li> `tagKey` filters by **tag key**. Type: String. Required: No<br><li> `tag:tagKey` filters by **tag key-value pair**. The tagKey should be replaced with a specified tag key, such as “tag:exampleKey”. Type: String. Required: No<br><li> `storageType` filters by **log topic storage type**. Valid values: `hot` (STANDARD storage); `cold`: (IA storage). Type: String. Required: No. Each request can contain up to 10 `Filters` and 100 `Filter.Values`.
        :type Filters: list of Filter
        :param Offset: Page offset. Default value: 0.
        :type Offset: int
        :param Limit: Maximum number of entries per page. Default value: 20. Maximum value: 100.
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
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics response structure.

    """

    def __init__(self):
        r"""
        :param Topics: Log topic list
        :type Topics: list of TopicInfo
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Topics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ExcludePathInfo(AbstractModel):
    """Blocklist path information

    """

    def __init__(self):
        r"""
        :param Type: Type. Valid values: `File`, `Path`
        :type Type: str
        :param Value: Specific content corresponding to `Type`
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInfo(AbstractModel):
    """Log export information

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param ExportId: Log export task ID
        :type ExportId: str
        :param Query: Log export query statement
        :type Query: str
        :param FileName: Log export filename
        :type FileName: str
        :param FileSize: Log file size
        :type FileSize: int
        :param Order: Log export time sorting
        :type Order: str
        :param Format: Log export format
        :type Format: str
        :param Count: Number of logs to be exported
        :type Count: int
        :param Status: Log download status. Valid values: `Processing`: exporting; `Complete`: completed; `Failed`: failed; `Expired`: expired (3-day validity period).
        :type Status: str
        :param From: Log export start time
        :type From: int
        :param To: Log export end time
        :type To: int
        :param CosPath: Log export path
        :type CosPath: str
        :param CreateTime: Log export creation time
        :type CreateTime: str
        """
        self.TopicId = None
        self.ExportId = None
        self.Query = None
        self.FileName = None
        self.FileSize = None
        self.Order = None
        self.Format = None
        self.Count = None
        self.Status = None
        self.From = None
        self.To = None
        self.CosPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ExportId = params.get("ExportId")
        self.Query = params.get("Query")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        self.Count = params.get("Count")
        self.Status = params.get("Status")
        self.From = params.get("From")
        self.To = params.get("To")
        self.CosPath = params.get("CosPath")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtractRuleInfo(AbstractModel):
    """Log extraction rule

    """

    def __init__(self):
        r"""
        :param TimeKey: Time field key name. `time_key` and `time_format` must appear in pairs
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeKey: str
        :param TimeFormat: Time field format. For more information, please see the output parameters of the time format description of the `strftime` function in C language
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeFormat: str
        :param Delimiter: Delimiter for delimited log, which is valid only if `log_type` is `delimiter_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Delimiter: str
        :param LogRegex: Full log matching rule, which is valid only if `log_type` is `fullregex_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogRegex: str
        :param BeginRegex: First-Line matching rule, which is valid only if `log_type` is `multiline_log` or `fullregex_log`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BeginRegex: str
        :param Keys: Key name of each extracted field. An empty key indicates to discard the field. This parameter is valid only if `log_type` is `delimiter_log`. `json_log` logs use the key of JSON itself
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Keys: list of str
        :param FilterKeyRegex: Log keys to be filtered and the corresponding regex
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FilterKeyRegex: list of KeyRegexInfo
        :param UnMatchUpLoadSwitch: Whether to upload the logs that failed to be parsed. Valid values: `true`: yes; `false`: no
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnMatchUpLoadSwitch: bool
        :param UnMatchLogKey: Unmatched log key
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnMatchLogKey: str
        :param Backtracking: Size of the data to be rewound in incremental collection mode. Default value: -1 (full collection)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Backtracking: int
        """
        self.TimeKey = None
        self.TimeFormat = None
        self.Delimiter = None
        self.LogRegex = None
        self.BeginRegex = None
        self.Keys = None
        self.FilterKeyRegex = None
        self.UnMatchUpLoadSwitch = None
        self.UnMatchLogKey = None
        self.Backtracking = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.TimeFormat = params.get("TimeFormat")
        self.Delimiter = params.get("Delimiter")
        self.LogRegex = params.get("LogRegex")
        self.BeginRegex = params.get("BeginRegex")
        self.Keys = params.get("Keys")
        if params.get("FilterKeyRegex") is not None:
            self.FilterKeyRegex = []
            for item in params.get("FilterKeyRegex"):
                obj = KeyRegexInfo()
                obj._deserialize(item)
                self.FilterKeyRegex.append(obj)
        self.UnMatchUpLoadSwitch = params.get("UnMatchUpLoadSwitch")
        self.UnMatchLogKey = params.get("UnMatchLogKey")
        self.Backtracking = params.get("Backtracking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filter

    """

    def __init__(self):
        r"""
        :param Key: Field to be filtered
        :type Key: str
        :param Values: Value to be filtered
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterRuleInfo(AbstractModel):
    """Filter rule for shipped log

    """

    def __init__(self):
        r"""
        :param Key: Filter rule key
        :type Key: str
        :param Regex: Filter rule
        :type Regex: str
        :param Value: Filter rule value
        :type Value: str
        """
        self.Key = None
        self.Regex = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Regex = params.get("Regex")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FullTextInfo(AbstractModel):
    """Full-Text index configuration

    """

    def __init__(self):
        r"""
        :param CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param Tokenizer: Separator of the full-text index. Each character represents a separator;
Supports only English punctuation marks and (\n\t\r);
We recommend you use (@&?|#()='",;:<>[]{}/ \n\t\r\) as separators;
        :type Tokenizer: str
        :param ContainZH: Whether Chinese characters are contained
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ContainZH: bool
        """
        self.CaseSensitive = None
        self.Tokenizer = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        self.Tokenizer = params.get("Tokenizer")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogRequest(AbstractModel):
    """GetAlarmLog request structure.

    """

    def __init__(self):
        r"""
        :param From: Start time of the log to be queried, which is a Unix timestamp in milliseconds
        :type From: int
        :param To: End time of the log to be queried, which is a Unix timestamp in milliseconds
        :type To: int
        :param Query: Query statement. Maximum length: 1024
        :type Query: str
        :param Limit: Number of logs returned in a single query. Maximum value: 1000
        :type Limit: int
        :param Context: This field is used to load more logs. Pass through the last `Context` value returned to get more log content.
        :type Context: str
        :param Sort: Order of the logs sorted by time returned by the log API. Valid values: `asc`: ascending; `desc`: descending. Default value: `desc`
        :type Sort: str
        :param UseNewAnalysis: If the value is `true`, the new search method will be used, and the response parameters `AnalysisRecords` and `Columns` will be valid. If the value is `false`, the old search method will be used, and `AnalysisResults` and `ColNames` will be valid.
        :type UseNewAnalysis: bool
        """
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None
        self.UseNewAnalysis = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        self.UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmLogResponse(AbstractModel):
    """GetAlarmLog response structure.

    """

    def __init__(self):
        r"""
        :param Context: `Context` for loading subsequent content
        :type Context: str
        :param ListOver: Whether all log query results are returned
        :type ListOver: bool
        :param Analysis: Whether the return is the analysis result
        :type Analysis: bool
        :param ColNames: If `Analysis` is `true`, column name of the analysis result will be returned; otherwise, empty content will be returned.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ColNames: list of str
        :param Results: Log query result. If `Analysis` is `True`, `null` may be returned
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Results: list of LogInfo
        :param AnalysisResults: Log analysis result. If `Analysis` is `False`, `null` may be returned
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AnalysisResults: list of LogItems
        :param AnalysisRecords: New log analysis result, which will be valid if `UseNewAnalysis` is `true`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AnalysisRecords: list of str
        :param Columns: Column attribute of log analysis, which will be valid if `UseNewAnalysis` is `true`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Columns: list of Column
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.ColNames = None
        self.Results = None
        self.AnalysisResults = None
        self.AnalysisRecords = None
        self.Columns = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        self.Analysis = params.get("Analysis")
        self.ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self.AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self.AnalysisResults.append(obj)
        self.AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.RequestId = params.get("RequestId")


class HistogramInfo(AbstractModel):
    """Histogram details

    """

    def __init__(self):
        r"""
        :param Count: The number of logs within the statistical period
        :type Count: int
        :param BTime: Unix timestamp rounded by `period`, in milliseconds
        :type BTime: int
        """
        self.Count = None
        self.BTime = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.BTime = params.get("BTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JsonInfo(AbstractModel):
    """JSON type description

    """

    def __init__(self):
        r"""
        :param EnableTag: Enablement flag
        :type EnableTag: bool
        :param MetaFields: Metadata information list. Valid values: __SOURCE__; __FILENAME__; __TIMESTAMP__
Note: This field may return `null`, indicating that no valid value was found.
        :type MetaFields: list of str
        """
        self.EnableTag = None
        self.MetaFields = None


    def _deserialize(self, params):
        self.EnableTag = params.get("EnableTag")
        self.MetaFields = params.get("MetaFields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRegexInfo(AbstractModel):
    """Log keys to be filtered and the corresponding regex

    """

    def __init__(self):
        r"""
        :param Key: Log key to be filtered
        :type Key: str
        :param Regex: Filter rule regex corresponding to key
        :type Regex: str
        """
        self.Key = None
        self.Regex = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueInfo(AbstractModel):
    """Field information of key value or metafield index

    """

    def __init__(self):
        r"""
        :param Key: When a key value or metafield index needs to be configured for a field, the metafield `Key` does not need to be prefixed with `__TAG__.` and is consistent with the one when logs are uploaded. `__TAG__.` will be prefixed automatically for display in the console.
        :type Key: str
        :param Value: Field index description information
        :type Value: :class:`tencentcloud.cls.v20201016.models.ValueInfo`
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = ValueInfo()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContextInfo(AbstractModel):
    """Log context information

    """

    def __init__(self):
        r"""
        :param Source: Log source device
        :type Source: str
        :param Filename: Collection path
        :type Filename: str
        :param Content: Log content
        :type Content: str
        :param PkgId: Log package number
        :type PkgId: str
        :param PkgLogId: Log number in log package
        :type PkgLogId: int
        :param BTime: Log timestamp
        :type BTime: int
        :param HostName: Source host name of logs
Note: This field may return `null`, indicating that no valid value was found.
        :type HostName: str
        """
        self.Source = None
        self.Filename = None
        self.Content = None
        self.PkgId = None
        self.PkgLogId = None
        self.BTime = None
        self.HostName = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Filename = params.get("Filename")
        self.Content = params.get("Content")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.BTime = params.get("BTime")
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """Log result information

    """

    def __init__(self):
        r"""
        :param Time: Log time in milliseconds
        :type Time: int
        :param TopicId: Log topic ID
        :type TopicId: str
        :param TopicName: Log topic name
        :type TopicName: str
        :param Source: Log source IP
        :type Source: str
        :param FileName: Log filename
        :type FileName: str
        :param PkgId: ID of the request package for log reporting
        :type PkgId: str
        :param PkgLogId: Log ID in request package
        :type PkgLogId: str
        :param LogJson: Serialized JSON string of log content
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LogJson: str
        :param HostName: Source host name of logs
Note: This field may return `null`, indicating that no valid value was found.
        :type HostName: str
        """
        self.Time = None
        self.TopicId = None
        self.TopicName = None
        self.Source = None
        self.FileName = None
        self.PkgId = None
        self.PkgLogId = None
        self.LogJson = None
        self.HostName = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Source = params.get("Source")
        self.FileName = params.get("FileName")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.LogJson = params.get("LogJson")
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """Key-Value pair in log

    """

    def __init__(self):
        r"""
        :param Key: Log key
        :type Key: str
        :param Value: Log value
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
        


class LogItems(AbstractModel):
    """`LogItem` array

    """

    def __init__(self):
        r"""
        :param Data: Key-Value pair returned in analysis result
        :type Data: list of LogItem
        """
        self.Data = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogsetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param LogsetName: Logset name
        :type LogsetName: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Tags: Tag bound to logset
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param TopicCount: Number of log topics in logset
        :type TopicCount: int
        :param RoleName: If `AssumerUin` is not empty, it indicates the service provider who creates the logset
        :type RoleName: str
        """
        self.LogsetId = None
        self.LogsetName = None
        self.CreateTime = None
        self.Tags = None
        self.TopicCount = None
        self.RoleName = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TopicCount = params.get("TopicCount")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupInfo(AbstractModel):
    """Machine group information

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        :param GroupName: Machine group name
        :type GroupName: str
        :param MachineGroupType: Machine group type
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Tags: List of tags bound to machine group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param AutoUpdate: Whether to enable automatic update for the machine group
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoUpdate: str
        :param UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateStartTime: str
        :param UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateEndTime: str
        :param ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServiceLogging: bool
        """
        self.GroupId = None
        self.GroupName = None
        self.MachineGroupType = None
        self.CreateTime = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        self.CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineGroupTypeInfo(AbstractModel):
    """Machine group type description

    """

    def __init__(self):
        r"""
        :param Type: Machine group type. Valid values: `ip`: the IP addresses of collection machines are stored in `Values` of the machine group; `label`: the tags of the machines are stored in `Values` of the machine group
        :type Type: str
        :param Values: Machine description list
        :type Values: list of str
        """
        self.Type = None
        self.Values = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineInfo(AbstractModel):
    """Machine status information

    """

    def __init__(self):
        r"""
        :param Ip: Machine IP
        :type Ip: str
        :param Status: Machine status. Valid values: `0`: exceptional; `1`: normal
        :type Status: int
        :param OfflineTime: Machine disconnection time. If the value is empty, the machine is normal. If the machine is exceptional, a specific value will be returned.
        :type OfflineTime: str
        :param AutoUpdate: Whether to enable automatic update for the machine. Valid values: `0`: no; `1`: yes
        :type AutoUpdate: int
        :param Version: Current machine version number
        :type Version: str
        :param UpdateStatus: Machine update feature status
        :type UpdateStatus: int
        :param ErrCode: Machine update result flag
        :type ErrCode: int
        :param ErrMsg: Machine update result information
        :type ErrMsg: str
        """
        self.Ip = None
        self.Status = None
        self.OfflineTime = None
        self.AutoUpdate = None
        self.Version = None
        self.UpdateStatus = None
        self.ErrCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Status = params.get("Status")
        self.OfflineTime = params.get("OfflineTime")
        self.AutoUpdate = params.get("AutoUpdate")
        self.Version = params.get("Version")
        self.UpdateStatus = params.get("UpdateStatus")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionRequest(AbstractModel):
    """MergePartition request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param PartitionId: Merged `PartitionId`
        :type PartitionId: int
        """
        self.TopicId = None
        self.PartitionId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergePartitionResponse(AbstractModel):
    """MergePartition response structure.

    """

    def __init__(self):
        r"""
        :param Partitions: Merge result set
        :type Partitions: list of PartitionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyAlarmNoticeRequest(AbstractModel):
    """ModifyAlarmNotice request structure.

    """

    def __init__(self):
        r"""
        :param AlarmNoticeId: Notification group ID
        :type AlarmNoticeId: str
        :param Name: Notification group name
        :type Name: str
        :param Type: Notification type. Valid values:
<li> `Trigger`: alarm triggered
<li> `Recovery`: alarm cleared
<li> `All`: alarm triggered and alarm cleared
        :type Type: str
        :param NoticeReceivers: Notification recipient
        :type NoticeReceivers: list of NoticeReceiver
        :param WebCallbacks: API callback information (including WeCom)
        :type WebCallbacks: list of WebCallback
        """
        self.AlarmNoticeId = None
        self.Name = None
        self.Type = None
        self.NoticeReceivers = None
        self.WebCallbacks = None


    def _deserialize(self, params):
        self.AlarmNoticeId = params.get("AlarmNoticeId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("NoticeReceivers") is not None:
            self.NoticeReceivers = []
            for item in params.get("NoticeReceivers"):
                obj = NoticeReceiver()
                obj._deserialize(item)
                self.NoticeReceivers.append(obj)
        if params.get("WebCallbacks") is not None:
            self.WebCallbacks = []
            for item in params.get("WebCallbacks"):
                obj = WebCallback()
                obj._deserialize(item)
                self.WebCallbacks.append(obj)
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


class ModifyAlarmRequest(AbstractModel):
    """ModifyAlarm request structure.

    """

    def __init__(self):
        r"""
        :param AlarmId: Alarm policy ID
        :type AlarmId: str
        :param Name: Alarm policy name
        :type Name: str
        :param MonitorTime: Monitoring task running time point
        :type MonitorTime: :class:`tencentcloud.cls.v20201016.models.MonitorTime`
        :param Condition: Trigger condition
        :type Condition: str
        :param TriggerCount: Alarm persistence cycle. An alarm will be triggered only after the corresponding trigger condition is met for the number of times specified by `TriggerCount`. Value range: 1–10.
        :type TriggerCount: int
        :param AlarmPeriod: Repeated alarm interval in minutes. Value range: 0–1440.
        :type AlarmPeriod: int
        :param AlarmNoticeIds: List of associated alarm notification templates
        :type AlarmNoticeIds: list of str
        :param AlarmTargets: Monitoring object list
        :type AlarmTargets: list of AlarmTarget
        :param Status: Whether to enable the alarm policy
        :type Status: bool
        :param MessageTemplate: Custom alarm content
        :type MessageTemplate: str
        :param CallBack: Custom callback
        :type CallBack: :class:`tencentcloud.cls.v20201016.models.CallBackInfo`
        :param Analysis: Multi-Dimensional analysis
        :type Analysis: list of AnalysisDimensional
        """
        self.AlarmId = None
        self.Name = None
        self.MonitorTime = None
        self.Condition = None
        self.TriggerCount = None
        self.AlarmPeriod = None
        self.AlarmNoticeIds = None
        self.AlarmTargets = None
        self.Status = None
        self.MessageTemplate = None
        self.CallBack = None
        self.Analysis = None


    def _deserialize(self, params):
        self.AlarmId = params.get("AlarmId")
        self.Name = params.get("Name")
        if params.get("MonitorTime") is not None:
            self.MonitorTime = MonitorTime()
            self.MonitorTime._deserialize(params.get("MonitorTime"))
        self.Condition = params.get("Condition")
        self.TriggerCount = params.get("TriggerCount")
        self.AlarmPeriod = params.get("AlarmPeriod")
        self.AlarmNoticeIds = params.get("AlarmNoticeIds")
        if params.get("AlarmTargets") is not None:
            self.AlarmTargets = []
            for item in params.get("AlarmTargets"):
                obj = AlarmTarget()
                obj._deserialize(item)
                self.AlarmTargets.append(obj)
        self.Status = params.get("Status")
        self.MessageTemplate = params.get("MessageTemplate")
        if params.get("CallBack") is not None:
            self.CallBack = CallBackInfo()
            self.CallBack._deserialize(params.get("CallBack"))
        if params.get("Analysis") is not None:
            self.Analysis = []
            for item in params.get("Analysis"):
                obj = AnalysisDimensional()
                obj._deserialize(item)
                self.Analysis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmResponse(AbstractModel):
    """ModifyAlarm response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyConfigRequest(AbstractModel):
    """ModifyConfig request structure.

    """

    def __init__(self):
        r"""
        :param ConfigId: Collection rule configuration ID
        :type ConfigId: str
        :param Name: Collection rule configuration name
        :type Name: str
        :param Path: Log collection path containing the filename
        :type Path: str
        :param LogType: Type of the log to be collected. Valid values: `json_log`: log in JSON format; `delimiter_log`: log in delimited format; `minimalist_log`: minimalist log; `multiline_log`: log in multi-line format; `fullregex_log`: log in full regex format. Default value: `minimalist_log`
        :type LogType: str
        :param ExtractRule: Extraction rule. If `ExtractRule` is set, `LogType` must be set.
        :type ExtractRule: :class:`tencentcloud.cls.v20201016.models.ExtractRuleInfo`
        :param ExcludePaths: Collection path blocklist
        :type ExcludePaths: list of ExcludePathInfo
        :param Output: Log topic (TopicId) associated with collection configuration
        :type Output: str
        :param UserDefineRule: Custom parsing string, which is a serialized JSON string
        :type UserDefineRule: str
        """
        self.ConfigId = None
        self.Name = None
        self.Path = None
        self.LogType = None
        self.ExtractRule = None
        self.ExcludePaths = None
        self.Output = None
        self.UserDefineRule = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.Name = params.get("Name")
        self.Path = params.get("Path")
        self.LogType = params.get("LogType")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = ExtractRuleInfo()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        if params.get("ExcludePaths") is not None:
            self.ExcludePaths = []
            for item in params.get("ExcludePaths"):
                obj = ExcludePathInfo()
                obj._deserialize(item)
                self.ExcludePaths.append(obj)
        self.Output = params.get("Output")
        self.UserDefineRule = params.get("UserDefineRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigResponse(AbstractModel):
    """ModifyConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyConsumerRequest(AbstractModel):
    """ModifyConsumer request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID bound to the task
        :type TopicId: str
        :param Effective: Whether the shipping task takes effect (default: no)
        :type Effective: bool
        :param NeedContent: Whether to ship metadata. Default value: `false`
        :type NeedContent: bool
        :param Content: Metadata to ship if `NeedContent` is `true`
        :type Content: :class:`tencentcloud.cls.v20201016.models.ConsumerContent`
        :param Ckafka: CKafka information
        :type Ckafka: :class:`tencentcloud.cls.v20201016.models.Ckafka`
        """
        self.TopicId = None
        self.Effective = None
        self.NeedContent = None
        self.Content = None
        self.Ckafka = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Effective = params.get("Effective")
        self.NeedContent = params.get("NeedContent")
        if params.get("Content") is not None:
            self.Content = ConsumerContent()
            self.Content._deserialize(params.get("Content"))
        if params.get("Ckafka") is not None:
            self.Ckafka = Ckafka()
            self.Ckafka._deserialize(params.get("Ckafka"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerResponse(AbstractModel):
    """ModifyConsumer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIndexRequest(AbstractModel):
    """ModifyIndex request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Status: It does not take effect by default
        :type Status: bool
        :param Rule: Index rule
        :type Rule: :class:`tencentcloud.cls.v20201016.models.RuleInfo`
        :param IncludeInternalFields: Internal field marker of full-text index. Default value: `false`. Valid value: `false`: excluding internal fields; `true`: including internal fields
        :type IncludeInternalFields: bool
        :param MetadataFlag: Metadata flag. Default value: `0`. Valid value: `0`: full-text index (including the metadata field with key-value index enabled); `1`: full-text index (including all metadata fields); `2`: full-text index (excluding metadata fields).
        :type MetadataFlag: int
        """
        self.TopicId = None
        self.Status = None
        self.Rule = None
        self.IncludeInternalFields = None
        self.MetadataFlag = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Status = params.get("Status")
        if params.get("Rule") is not None:
            self.Rule = RuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.IncludeInternalFields = params.get("IncludeInternalFields")
        self.MetadataFlag = params.get("MetadataFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIndexResponse(AbstractModel):
    """ModifyIndex response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLogsetRequest(AbstractModel):
    """ModifyLogset request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param LogsetName: Logset name
        :type LogsetName: str
        :param Tags: Tag key-value pair bound to logset. Up to 10 tag key-value pairs are supported, and a resource can be bound to only one tag key at any time.
        :type Tags: list of Tag
        """
        self.LogsetId = None
        self.LogsetName = None
        self.Tags = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
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
        


class ModifyLogsetResponse(AbstractModel):
    """ModifyLogset response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMachineGroupRequest(AbstractModel):
    """ModifyMachineGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Machine group ID
        :type GroupId: str
        :param GroupName: Machine group name
        :type GroupName: str
        :param MachineGroupType: Machine group type
        :type MachineGroupType: :class:`tencentcloud.cls.v20201016.models.MachineGroupTypeInfo`
        :param Tags: Tag list
        :type Tags: list of Tag
        :param AutoUpdate: Whether to enable automatic update for the machine group
        :type AutoUpdate: bool
        :param UpdateStartTime: Update start time. We recommend you update LogListener during off-peak hours.
        :type UpdateStartTime: str
        :param UpdateEndTime: Update end time. We recommend you update LogListener during off-peak hours.
        :type UpdateEndTime: str
        :param ServiceLogging: Whether to enable the service log to record the logs generated by the LogListener service itself. After it is enabled, the internal logset `cls_service_logging` and the `loglistener_status`, `loglistener_alarm`, and `loglistener_business` log topics will be created, which will not incur fees.
        :type ServiceLogging: bool
        """
        self.GroupId = None
        self.GroupName = None
        self.MachineGroupType = None
        self.Tags = None
        self.AutoUpdate = None
        self.UpdateStartTime = None
        self.UpdateEndTime = None
        self.ServiceLogging = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("MachineGroupType") is not None:
            self.MachineGroupType = MachineGroupTypeInfo()
            self.MachineGroupType._deserialize(params.get("MachineGroupType"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoUpdate = params.get("AutoUpdate")
        self.UpdateStartTime = params.get("UpdateStartTime")
        self.UpdateEndTime = params.get("UpdateEndTime")
        self.ServiceLogging = params.get("ServiceLogging")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMachineGroupResponse(AbstractModel):
    """ModifyMachineGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyShipperRequest(AbstractModel):
    """ModifyShipper request structure.

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        :param Bucket: New destination bucket in shipping rule
        :type Bucket: str
        :param Prefix: New destination directory prefix in shipping rule
        :type Prefix: str
        :param Status: Shipping rule status
        :type Status: bool
        :param ShipperName: Shipping rule name
        :type ShipperName: str
        :param Interval: Shipping time interval in seconds. Default value: 300. Value range: 300–900
        :type Interval: int
        :param MaxSize: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100–256
        :type MaxSize: int
        :param FilterRules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :type FilterRules: list of FilterRuleInfo
        :param Partition: Partition rule of shipped log, which can be represented in `strftime` time format
        :type Partition: str
        :param Compress: Compression configuration of shipped log
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: Format configuration of shipped log content
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        """
        self.ShipperId = None
        self.Bucket = None
        self.Prefix = None
        self.Status = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.Status = params.get("Status")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyShipperResponse(AbstractModel):
    """ModifyShipper response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param TopicName: Log topic name
        :type TopicName: str
        :param Tags: Tag description list. This parameter is used to bind a tag to a log topic. Up to 10 tag key-value pairs are supported, and they must be unique.
        :type Tags: list of Tag
        :param Status: Whether to start collection for this log topic
        :type Status: bool
        :param AutoSplit: Whether to enable automatic split
        :type AutoSplit: bool
        :param MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled
        :type MaxSplitPartitions: int
        :param Period: Lifecycle in days. Value range: 1-3600 (3640 indicates permanent retention)
        :type Period: int
        """
        self.TopicId = None
        self.TopicName = None
        self.Tags = None
        self.Status = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.Period = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Status = params.get("Status")
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorTime(AbstractModel):
    """Monitoring task execution time point in alarm policy

    """

    def __init__(self):
        r"""
        :param Type: Valid values:
<br><li> `Period`: periodic execution
<br><li> `Fixed`: scheduled execution
        :type Type: str
        :param Time: Execution interval or scheduled time point in minutes. Value range: 1–1440.
        :type Time: int
        """
        self.Type = None
        self.Time = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeReceiver(AbstractModel):
    """Alarm notification recipient information

    """

    def __init__(self):
        r"""
        :param ReceiverType: Recipient type. Valid values:
<br><li> `Uin`: user ID
<br><li> `Group`: user group ID
Currently, other recipient types are not supported.
        :type ReceiverType: str
        :param ReceiverIds: Recipient
        :type ReceiverIds: list of int
        :param ReceiverChannels: Notification method
<br><li> `Email`: email
<br><li> `Sms`: SMS
<br><li> `WeChat`: WeChat
<br><li> `Phone`: phone
        :type ReceiverChannels: list of str
        :param StartTime: Start time for allowed message receipt
        :type StartTime: str
        :param EndTime: End time for allowed message receipt
        :type EndTime: str
        :param Index: Index
        :type Index: int
        """
        self.ReceiverType = None
        self.ReceiverIds = None
        self.ReceiverChannels = None
        self.StartTime = None
        self.EndTime = None
        self.Index = None


    def _deserialize(self, params):
        self.ReceiverType = params.get("ReceiverType")
        self.ReceiverIds = params.get("ReceiverIds")
        self.ReceiverChannels = params.get("ReceiverChannels")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerRequest(AbstractModel):
    """OpenKafkaConsumer request structure.

    """

    def __init__(self):
        r"""
        :param FromTopicId: `TopicId` created by the CLS console
        :type FromTopicId: str
        """
        self.FromTopicId = None


    def _deserialize(self, params):
        self.FromTopicId = params.get("FromTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenKafkaConsumerResponse(AbstractModel):
    """OpenKafkaConsumer response structure.

    """

    def __init__(self):
        r"""
        :param TopicID: `TopicId` to be consumed
        :type TopicID: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicID = params.get("TopicID")
        self.RequestId = params.get("RequestId")


class ParquetInfo(AbstractModel):
    """`Parquet` contents

    """

    def __init__(self):
        r"""
        :param ParquetKeyInfo: `ParquetKeyInfo` array
        :type ParquetKeyInfo: list of ParquetKeyInfo
        """
        self.ParquetKeyInfo = None


    def _deserialize(self, params):
        if params.get("ParquetKeyInfo") is not None:
            self.ParquetKeyInfo = []
            for item in params.get("ParquetKeyInfo"):
                obj = ParquetKeyInfo()
                obj._deserialize(item)
                self.ParquetKeyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParquetKeyInfo(AbstractModel):
    """`Parquet` content description

    """

    def __init__(self):
        r"""
        :param KeyName: Key name
        :type KeyName: str
        :param KeyType: Supported data types: string, boolean, int32, int64, float, and double
        :type KeyType: str
        :param KeyNonExistingField: Assignment information returned upon resolution failure
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type KeyNonExistingField: str
        """
        self.KeyName = None
        self.KeyType = None
        self.KeyNonExistingField = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.KeyType = params.get("KeyType")
        self.KeyNonExistingField = params.get("KeyNonExistingField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """Log topic partition information

    """

    def __init__(self):
        r"""
        :param PartitionId: Partition ID
        :type PartitionId: int
        :param Status: Partition status. Valid values: `readwrite`, `readonly`
        :type Status: str
        :param InclusiveBeginKey: Partition hash start key
        :type InclusiveBeginKey: str
        :param ExclusiveEndKey: Partition hash end key
        :type ExclusiveEndKey: str
        :param CreateTime: Partition creation time
        :type CreateTime: str
        :param LastWriteTime: Last modified of read-only partition
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LastWriteTime: str
        """
        self.PartitionId = None
        self.Status = None
        self.InclusiveBeginKey = None
        self.ExclusiveEndKey = None
        self.CreateTime = None
        self.LastWriteTime = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")
        self.Status = params.get("Status")
        self.InclusiveBeginKey = params.get("InclusiveBeginKey")
        self.ExclusiveEndKey = params.get("ExclusiveEndKey")
        self.CreateTime = params.get("CreateTime")
        self.LastWriteTime = params.get("LastWriteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskRequest(AbstractModel):
    """RetryShipperTask request structure.

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        :param TaskId: Shipping task ID
        :type TaskId: str
        """
        self.ShipperId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryShipperTaskResponse(AbstractModel):
    """RetryShipperTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """Index rule. At least one of the `FullText`, `KeyValue`, and `Tag` parameters must be valid.

    """

    def __init__(self):
        r"""
        :param FullText: Full-Text index configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FullText: :class:`tencentcloud.cls.v20201016.models.FullTextInfo`
        :param KeyValue: Key-Value index configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type KeyValue: :class:`tencentcloud.cls.v20201016.models.RuleKeyValueInfo`
        :param Tag: Metafield index configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tag: :class:`tencentcloud.cls.v20201016.models.RuleTagInfo`
        """
        self.FullText = None
        self.KeyValue = None
        self.Tag = None


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self.FullText = FullTextInfo()
            self.FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self.KeyValue = RuleKeyValueInfo()
            self.KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self.Tag = RuleTagInfo()
            self.Tag._deserialize(params.get("Tag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleKeyValueInfo(AbstractModel):
    """Key-Value index configuration

    """

    def __init__(self):
        r"""
        :param CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param KeyValues: Key-Value pair information of the index to be created. Up to 100 key-value pairs can be configured.
        :type KeyValues: list of KeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleTagInfo(AbstractModel):
    """Metafield index configuration

    """

    def __init__(self):
        r"""
        :param CaseSensitive: Case sensitivity
        :type CaseSensitive: bool
        :param KeyValues: Field information in the metafield index configuration
        :type KeyValues: list of KeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = KeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the log topic to be searched
        :type TopicId: str
        :param From: Start time of the log to be searched, which is a Unix timestamp in milliseconds
        :type From: int
        :param To: End time of the log to be searched, which is a Unix timestamp in milliseconds
        :type To: int
        :param Query: Statement for search and analysis. Maximum length: 12 KB
A statement is in the format of <a href="https://intl.cloud.tencent.com/document/product/614/47044?from_cn_redirect=1" target="_blank">[search rule]</a> | <a href="https://intl.cloud.tencent.com/document/product/614/44061?from_cn_redirect=1" target="_blank">[SQL statement]</a>. You can omit the pipe symbol <code> | </code> and SQL statement when log analysis is not required.
        :type Query: str
        :param Limit: The number of raw logs returned by a single query. Maximum value: 1000. You need to use `Context` to continue to get logs.
Notes:
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To limit the number of analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58977?from_cn_redirect=1" target="_blank">SQL LIMIT Syntax</a>.
        :type Limit: int
        :param Context: You can pass through the `Context` value (validity: 1 hour) returned by the last API to continue to get logs, which can get up to 10,000 raw logs.
Notes:
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To continue to get analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58977?from_cn_redirect=1" target="_blank">SQL LIMIT Syntax</a>.
        :type Context: str
        :param Sort: Time order of the logs returned. Valid values: `asc` (ascending); `desc`: (descending). Default value: `desc`
Notes:
* This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
* To sort the analysis results, see <a href="https://intl.cloud.tencent.com/document/product/614/58978?from_cn_redirect=1" target="_blank">SQL ORDER BY Syntax</a>.
        :type Sort: str
        :param UseNewAnalysis: If the value is `true`, the new response method will be used, and the output parameters `AnalysisRecords` and `Columns` will be valid.
If the value is `false`, the old response method will be used, and the output parameters `AnalysisResults` and `ColNames` will be valid.
The two response methods differ slightly in terms of encoding format. You are advised to use the new method (`true`).
        :type UseNewAnalysis: bool
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None
        self.UseNewAnalysis = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        self.UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog response structure.

    """

    def __init__(self):
        r"""
        :param Context: You can pass through the `Context` value (validity: 1 hour) returned by this API to continue to get more logs.
        :type Context: str
        :param ListOver: Whether to return all raw log query results. If not, you can use `Context` to continue to get logs.
Note: This parameter is valid only when the query statement (`Query`) does not contain an SQL statement.
        :type ListOver: bool
        :param Analysis: Whether the returned data is the analysis (SQL) result
        :type Analysis: bool
        :param Results: Raw logs that meet the search conditions
Note: This field may return `null`, indicating that no valid value was found.
        :type Results: list of LogInfo
        :param ColNames: Column names of log analysis
This parameter is valid only when `UseNewAnalysis` is `false`.
Note: This field may return `null`, indicating that no valid value was found.
        :type ColNames: list of str
        :param AnalysisResults: Log analysis result
This parameter is valid only when `UseNewAnalysis` is `false`.
Note: This field may return `null`, indicating that no valid value was found.
        :type AnalysisResults: list of LogItems
        :param AnalysisRecords: Log analysis result
This parameter is valid only when `UseNewAnalysis` is `true`.
Note: This field may return `null`, indicating that no valid value was found.
        :type AnalysisRecords: list of str
        :param Columns: Column attributes of log analysis
This parameter is valid only when `UseNewAnalysis` is `true`.
Note: This field may return `null`, indicating that no valid value was found.
        :type Columns: list of Column
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.Results = None
        self.ColNames = None
        self.AnalysisResults = None
        self.AnalysisRecords = None
        self.Columns = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        self.Analysis = params.get("Analysis")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        self.ColNames = params.get("ColNames")
        if params.get("AnalysisResults") is not None:
            self.AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self.AnalysisResults.append(obj)
        self.AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self.Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self.Columns.append(obj)
        self.RequestId = params.get("RequestId")


class ShipperInfo(AbstractModel):
    """Shipping rule

    """

    def __init__(self):
        r"""
        :param ShipperId: Shipping rule ID
        :type ShipperId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Bucket: Bucket address shipped to
        :type Bucket: str
        :param Prefix: Shipping prefix directory
        :type Prefix: str
        :param ShipperName: Shipping rule name
        :type ShipperName: str
        :param Interval: Shipping time interval in seconds
        :type Interval: int
        :param MaxSize: Maximum size of shipped file in MB
        :type MaxSize: int
        :param Status: Whether it takes effect
        :type Status: bool
        :param FilterRules: Filter rule for shipped log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FilterRules: list of FilterRuleInfo
        :param Partition: Partition rule of shipped log, which can be represented in `strftime` time format
        :type Partition: str
        :param Compress: Compression configuration of shipped log
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Compress: :class:`tencentcloud.cls.v20201016.models.CompressInfo`
        :param Content: Format configuration of shipped log content
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Content: :class:`tencentcloud.cls.v20201016.models.ContentInfo`
        :param CreateTime: Creation time of shipped log
        :type CreateTime: str
        """
        self.ShipperId = None
        self.TopicId = None
        self.Bucket = None
        self.Prefix = None
        self.ShipperName = None
        self.Interval = None
        self.MaxSize = None
        self.Status = None
        self.FilterRules = None
        self.Partition = None
        self.Compress = None
        self.Content = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ShipperId = params.get("ShipperId")
        self.TopicId = params.get("TopicId")
        self.Bucket = params.get("Bucket")
        self.Prefix = params.get("Prefix")
        self.ShipperName = params.get("ShipperName")
        self.Interval = params.get("Interval")
        self.MaxSize = params.get("MaxSize")
        self.Status = params.get("Status")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = FilterRuleInfo()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        self.Partition = params.get("Partition")
        if params.get("Compress") is not None:
            self.Compress = CompressInfo()
            self.Compress._deserialize(params.get("Compress"))
        if params.get("Content") is not None:
            self.Content = ContentInfo()
            self.Content._deserialize(params.get("Content"))
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipperTaskInfo(AbstractModel):
    """Shipping task information

    """

    def __init__(self):
        r"""
        :param TaskId: Shipping task ID
        :type TaskId: str
        :param ShipperId: Shipping information ID
        :type ShipperId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param RangeStart: Start timestamp of the current batch of shipped logs in milliseconds
        :type RangeStart: int
        :param RangeEnd: End timestamp of the current batch of shipped logs in milliseconds
        :type RangeEnd: int
        :param StartTime: Start timestamp of the current shipping task in milliseconds
        :type StartTime: int
        :param EndTime: End timestamp of the current shipping task in milliseconds
        :type EndTime: int
        :param Status: Result of the current shipping task. Valid values: `success`, `running`, `failed`
        :type Status: str
        :param Message: Result details
        :type Message: str
        """
        self.TaskId = None
        self.ShipperId = None
        self.TopicId = None
        self.RangeStart = None
        self.RangeEnd = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Message = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ShipperId = params.get("ShipperId")
        self.TopicId = params.get("TopicId")
        self.RangeStart = params.get("RangeStart")
        self.RangeEnd = params.get("RangeEnd")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionRequest(AbstractModel):
    """SplitPartition request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param PartitionId: ID of the partition to be split
        :type PartitionId: int
        :param SplitKey: Partition split hash key position, which is meaningful only if `Number=2` is set
        :type SplitKey: str
        :param Number: Number of partitions to split into, which is optional. Default value: 2
        :type Number: int
        """
        self.TopicId = None
        self.PartitionId = None
        self.SplitKey = None
        self.Number = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.PartitionId = params.get("PartitionId")
        self.SplitKey = params.get("SplitKey")
        self.Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitPartitionResponse(AbstractModel):
    """SplitPartition response structure.

    """

    def __init__(self):
        r"""
        :param Partitions: Split result set
        :type Partitions: list of PartitionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Partitions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.Partitions.append(obj)
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Description of the tag pair bound to a resource instance when it is created

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
        


class TopicInfo(AbstractModel):
    """Log topic information

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param TopicName: Log topic name
        :type TopicName: str
        :param PartitionCount: Number of topic partitions
        :type PartitionCount: int
        :param Index: Whether index is enabled
        :type Index: bool
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Status: Whether collection is enabled in the log topic
        :type Status: bool
        :param Tags: Information of tags bound to log topic
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param AutoSplit: Whether automatic split is enabled for this topic
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoSplit: bool
        :param MaxSplitPartitions: Maximum number of partitions to split into for this topic if automatic split is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxSplitPartitions: int
        :param StorageType: Log topic storage class
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageType: str
        :param Period: Lifecycle in days. Value range: 1-3600 (3640 indicates permanent retention)
Note: This field may return `null`, indicating that no valid value was found.
        :type Period: int
        """
        self.LogsetId = None
        self.TopicId = None
        self.TopicName = None
        self.PartitionCount = None
        self.Index = None
        self.CreateTime = None
        self.Status = None
        self.Tags = None
        self.AutoSplit = None
        self.MaxSplitPartitions = None
        self.StorageType = None
        self.Period = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.PartitionCount = params.get("PartitionCount")
        self.Index = params.get("Index")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoSplit = params.get("AutoSplit")
        self.MaxSplitPartitions = params.get("MaxSplitPartitions")
        self.StorageType = params.get("StorageType")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogRequest(AbstractModel):
    """UploadLog request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID
        :type TopicId: str
        :param HashKey: Topic partition where data will be written into by `HashKey` 
        :type HashKey: str
        :param CompressType: Compression type
        :type CompressType: str
        """
        self.TopicId = None
        self.HashKey = None
        self.CompressType = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.HashKey = params.get("HashKey")
        self.CompressType = params.get("CompressType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadLogResponse(AbstractModel):
    """UploadLog response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ValueInfo(AbstractModel):
    """Index description information of the field for which key-value index needs to be enabled

    """

    def __init__(self):
        r"""
        :param Type: Field type. Valid values: `long`, `text`, `double`
        :type Type: str
        :param Tokenizer: Separator of fields. Each character represents a separator;
Supports only English punctuation marks and (\n\t\r);
`long` and `double` fields need to be null;
We recommend you use (@&?|#()='",;:<>[]{}/ \n\t\r\\) as separators for `text` fields;
        :type Tokenizer: str
        :param SqlFlag: Whether the analysis feature is enabled for the field
        :type SqlFlag: bool
        :param ContainZH: Whether Chinese characters are contained
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ContainZH: bool
        """
        self.Type = None
        self.Tokenizer = None
        self.SqlFlag = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tokenizer = params.get("Tokenizer")
        self.SqlFlag = params.get("SqlFlag")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebCallback(AbstractModel):
    """Callback address

    """

    def __init__(self):
        r"""
        :param Url: Callback address
        :type Url: str
        :param CallbackType: Callback type. Valid values:
<li> WeCom
<li> Http
        :type CallbackType: str
        :param Method: Callback method. Valid values:
<li> POST
<li> PUT
Default value: `POST`. This parameter is required if `CallbackType` is `Http`.
Note: This field may return `null`, indicating that no valid value was found.
        :type Method: str
        :param Headers: Request header
Note: This parameter is disused. To specify request headers, see `CallBack` in <a href="https://intl.cloud.tencent.com/document/product/614/56466?from_cn_redirect=1">CreateAlarmNotice</a>.
Note: This field may return `null`, indicating that no valid value was found.
        :type Headers: list of str
        :param Body: Request content
Note: This parameter is disused. To specify request content, see `CallBack` in <a href="https://intl.cloud.tencent.com/document/product/614/56466?from_cn_redirect=1">CreateAlarmNotice</a>.
Note: This field may return `null`, indicating that no valid value was found.
        :type Body: str
        :param Index: Number
        :type Index: int
        """
        self.Url = None
        self.CallbackType = None
        self.Method = None
        self.Headers = None
        self.Body = None
        self.Index = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CallbackType = params.get("CallbackType")
        self.Method = params.get("Method")
        self.Headers = params.get("Headers")
        self.Body = params.get("Body")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        