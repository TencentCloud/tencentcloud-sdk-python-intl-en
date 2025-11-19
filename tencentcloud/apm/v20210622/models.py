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


class APMKV(AbstractModel):
    r"""APM floating-point number type key-value pair.

    """

    def __init__(self):
        r"""
        :param _Key: Key value definition.
        :type Key: str
        :param _Value: Value definition.
        :type Value: float
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key value definition.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value definition.
        :rtype: float
        """
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
        


class APMKVItem(AbstractModel):
    r"""Common kv structure of apm.

    """

    def __init__(self):
        r"""
        :param _Key: Key value definition.
        :type Key: str
        :param _Value: Value definition.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key value definition.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value definition.
        :rtype: str
        """
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
        


class AgentOperationConfigView(AbstractModel):
    r"""Related configurations of the probe APIs.

    """

    def __init__(self):
        r"""
        :param _RetentionValid: Whether allowlist configuration is enabled for the current API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionValid: bool
        :param _IgnoreOperation: Effective when RetentionValid is false. It indicates blocklist configuration in API settings. The APIs specified in the configuration do not support collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreOperation: str
        :param _RetentionOperation: Effective when RetentionValid is true. It indicates allowlist configuration in API settings. Only the APIs specified in the configuration support collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionOperation: str
        """
        self._RetentionValid = None
        self._IgnoreOperation = None
        self._RetentionOperation = None

    @property
    def RetentionValid(self):
        r"""Whether allowlist configuration is enabled for the current API.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RetentionValid

    @RetentionValid.setter
    def RetentionValid(self, RetentionValid):
        self._RetentionValid = RetentionValid

    @property
    def IgnoreOperation(self):
        r"""Effective when RetentionValid is false. It indicates blocklist configuration in API settings. The APIs specified in the configuration do not support collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IgnoreOperation

    @IgnoreOperation.setter
    def IgnoreOperation(self, IgnoreOperation):
        self._IgnoreOperation = IgnoreOperation

    @property
    def RetentionOperation(self):
        r"""Effective when RetentionValid is true. It indicates allowlist configuration in API settings. Only the APIs specified in the configuration support collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RetentionOperation

    @RetentionOperation.setter
    def RetentionOperation(self, RetentionOperation):
        self._RetentionOperation = RetentionOperation


    def _deserialize(self, params):
        self._RetentionValid = params.get("RetentionValid")
        self._IgnoreOperation = params.get("IgnoreOperation")
        self._RetentionOperation = params.get("RetentionOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmAgentInfo(AbstractModel):
    r"""APM agent information.

    """

    def __init__(self):
        r"""
        :param _AgentDownloadURL: Agent download address.
        :type AgentDownloadURL: str
        :param _CollectorURL: Collector reporting address.
        :type CollectorURL: str
        :param _Token: Token information.
        :type Token: str
        :param _PublicCollectorURL: Public network reporting address.
        :type PublicCollectorURL: str
        :param _InnerCollectorURL: Self-Developed vpc report address.
        :type InnerCollectorURL: str
        :param _PrivateLinkCollectorURL: Private link reporting address.
        :type PrivateLinkCollectorURL: str
        """
        self._AgentDownloadURL = None
        self._CollectorURL = None
        self._Token = None
        self._PublicCollectorURL = None
        self._InnerCollectorURL = None
        self._PrivateLinkCollectorURL = None

    @property
    def AgentDownloadURL(self):
        r"""Agent download address.
        :rtype: str
        """
        return self._AgentDownloadURL

    @AgentDownloadURL.setter
    def AgentDownloadURL(self, AgentDownloadURL):
        self._AgentDownloadURL = AgentDownloadURL

    @property
    def CollectorURL(self):
        r"""Collector reporting address.
        :rtype: str
        """
        return self._CollectorURL

    @CollectorURL.setter
    def CollectorURL(self, CollectorURL):
        self._CollectorURL = CollectorURL

    @property
    def Token(self):
        r"""Token information.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def PublicCollectorURL(self):
        r"""Public network reporting address.
        :rtype: str
        """
        return self._PublicCollectorURL

    @PublicCollectorURL.setter
    def PublicCollectorURL(self, PublicCollectorURL):
        self._PublicCollectorURL = PublicCollectorURL

    @property
    def InnerCollectorURL(self):
        r"""Self-Developed vpc report address.
        :rtype: str
        """
        return self._InnerCollectorURL

    @InnerCollectorURL.setter
    def InnerCollectorURL(self, InnerCollectorURL):
        self._InnerCollectorURL = InnerCollectorURL

    @property
    def PrivateLinkCollectorURL(self):
        r"""Private link reporting address.
        :rtype: str
        """
        return self._PrivateLinkCollectorURL

    @PrivateLinkCollectorURL.setter
    def PrivateLinkCollectorURL(self, PrivateLinkCollectorURL):
        self._PrivateLinkCollectorURL = PrivateLinkCollectorURL


    def _deserialize(self, params):
        self._AgentDownloadURL = params.get("AgentDownloadURL")
        self._CollectorURL = params.get("CollectorURL")
        self._Token = params.get("Token")
        self._PublicCollectorURL = params.get("PublicCollectorURL")
        self._InnerCollectorURL = params.get("InnerCollectorURL")
        self._PrivateLinkCollectorURL = params.get("PrivateLinkCollectorURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmAppConfig(AbstractModel):
    r"""Querying application configuration response parameters structure.

    """

    def __init__(self):
        r"""
        :param _InstanceKey: Instance ID.
        :type InstanceKey: str
        :param _ServiceName: Service name.
        :type ServiceName: str
        :param _UrlConvergenceSwitch: URL convergence switch.
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL convergence threshold
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: URL convergence regular expression.
        :type UrlConvergence: str
        :param _ExceptionFilter: Exception filtering regular expression.
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: Error code filtering.
        :type ErrorCodeFilter: str
        :param _Components: Service component type.
        :type Components: str
        :param _UrlExclude: URL exclusion regular.
        :type UrlExclude: str
        :param _LogSource: Specifies the log source.
        :type LogSource: str
        :param _LogRegion: Log region.
        :type LogRegion: str
        :param _IsRelatedLog: Whether logging is enabled. valid values: 0 (disabled), 1 (enabled).
        :type IsRelatedLog: int
        :param _LogTopicID: Log topic ID
        :type LogTopicID: str
        :param _IgnoreOperationName: API names to filter
        :type IgnoreOperationName: str
        :param _LogSet: CLS log set/ES cluster ID
        :type LogSet: str
        :param _TraceRateLimit: Number of traces reported by the probe per second.
        :type TraceRateLimit: int
        :param _EnableSnapshot: Whether thread profiling is enabled.
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: Timeout threshold for thread profiling.
        :type SnapshotTimeout: int
        :param _AgentEnable: Whether agent is enabled.
        :type AgentEnable: bool
        :param _InstrumentList: Component List
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstrumentList: list of Instrument
        :param _TraceSquash: Whether link compression is enabled.
        :type TraceSquash: bool
        :param _EventEnable: Whether application diagnosis is enabled.
        :type EventEnable: bool
        :param _AgentOperationConfigView: Related configurations of the probe APIs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: Whether to enable application log configuration.
        :type EnableLogConfig: bool
        :param _ServiceID: Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceID: str
        :param _EnableDashboardConfig: Whether to enable the dashboard configuration for applications. false: disabled (consistent with the business system configuration); true: enabled (application-level configuration).
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: Whether to associate with Dashboard. 0: disabled; 1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DashboardTopicID: str
        :param _EnableSecurityConfig: Whether to enable the application-level configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableSecurityConfig: bool
        :param _IsInstrumentationVulnerabilityScan: Whether to enable detection of component vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: Whether to enable SQL injection analysis.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSqlInjectionAnalysis: int
        :param _IsRemoteCommandExecutionAnalysis: Whether to enable execution analysis of remote command.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: Whether to enable detection analysis of Java webshell.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS index type. (0 = full-text index; 1 = key-value index).
        :type LogIndexType: int
        :param _LogTraceIdKey: Index key of traceId. It is valid when the CLS index type is key-value index.
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: API name automatic convergence switch (0 - disabled; 1 - enabled)
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: Convergence threshold for URL long segments.
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: Convergence threshold for URL numerical segments.
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: Specifies the memory threshold for probe fusing.
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: Specifies the CPU threshold for probe fusing.
        :type DisableCpuUsed: int
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._UrlConvergence = None
        self._ExceptionFilter = None
        self._ErrorCodeFilter = None
        self._Components = None
        self._UrlExclude = None
        self._LogSource = None
        self._LogRegion = None
        self._IsRelatedLog = None
        self._LogTopicID = None
        self._IgnoreOperationName = None
        self._LogSet = None
        self._TraceRateLimit = None
        self._EnableSnapshot = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._InstrumentList = None
        self._TraceSquash = None
        self._EventEnable = None
        self._AgentOperationConfigView = None
        self._EnableLogConfig = None
        self._ServiceID = None
        self._EnableDashboardConfig = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._EnableSecurityConfig = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsSqlInjectionAnalysis = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlAutoConvergenceEnable = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceKey(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""Service name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""URL convergence switch.
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL convergence threshold
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""URL convergence regular expression.
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ExceptionFilter(self):
        r"""Exception filtering regular expression.
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""Error code filtering.
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def Components(self):
        r"""Service component type.
        :rtype: str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def UrlExclude(self):
        r"""URL exclusion regular.
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def LogSource(self):
        r"""Specifies the log source.
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogRegion(self):
        r"""Log region.
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def IsRelatedLog(self):
        r"""Whether logging is enabled. valid values: 0 (disabled), 1 (enabled).
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        r"""Log topic ID
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def IgnoreOperationName(self):
        r"""API names to filter
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def LogSet(self):
        r"""CLS log set/ES cluster ID
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def TraceRateLimit(self):
        r"""Number of traces reported by the probe per second.
        :rtype: int
        """
        return self._TraceRateLimit

    @TraceRateLimit.setter
    def TraceRateLimit(self, TraceRateLimit):
        self._TraceRateLimit = TraceRateLimit

    @property
    def EnableSnapshot(self):
        r"""Whether thread profiling is enabled.
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""Timeout threshold for thread profiling.
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""Whether agent is enabled.
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""Component List
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""Whether link compression is enabled.
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""Whether application diagnosis is enabled.
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def AgentOperationConfigView(self):
        r"""Related configurations of the probe APIs.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""Whether to enable application log configuration.
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def ServiceID(self):
        r"""Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def EnableDashboardConfig(self):
        r"""Whether to enable the dashboard configuration for applications. false: disabled (consistent with the business system configuration); true: enabled (application-level configuration).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""Whether to associate with Dashboard. 0: disabled; 1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""dashboard ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def EnableSecurityConfig(self):
        r"""Whether to enable the application-level configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""Whether to enable detection of component vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        r"""Whether to enable SQL injection analysis.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""Whether to enable execution analysis of remote command.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""Whether to enable detection analysis of Java webshell.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS index type. (0 = full-text index; 1 = key-value index).
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""Index key of traceId. It is valid when the CLS index type is key-value index.
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""API name automatic convergence switch (0 - disabled; 1 - enabled)
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""Convergence threshold for URL long segments.
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""Convergence threshold for URL numerical segments.
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""Specifies the memory threshold for probe fusing.
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""Specifies the CPU threshold for probe fusing.
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._UrlConvergence = params.get("UrlConvergence")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._Components = params.get("Components")
        self._UrlExclude = params.get("UrlExclude")
        self._LogSource = params.get("LogSource")
        self._LogRegion = params.get("LogRegion")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogTopicID = params.get("LogTopicID")
        self._IgnoreOperationName = params.get("IgnoreOperationName")
        self._LogSet = params.get("LogSet")
        self._TraceRateLimit = params.get("TraceRateLimit")
        self._EnableSnapshot = params.get("EnableSnapshot")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        self._TraceSquash = params.get("TraceSquash")
        self._EventEnable = params.get("EventEnable")
        if params.get("AgentOperationConfigView") is not None:
            self._AgentOperationConfigView = AgentOperationConfigView()
            self._AgentOperationConfigView._deserialize(params.get("AgentOperationConfigView"))
        self._EnableLogConfig = params.get("EnableLogConfig")
        self._ServiceID = params.get("ServiceID")
        self._EnableDashboardConfig = params.get("EnableDashboardConfig")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._EnableSecurityConfig = params.get("EnableSecurityConfig")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlAutoConvergenceEnable = params.get("UrlAutoConvergenceEnable")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmApplicationConfigView(AbstractModel):
    r"""Application-Related configuration list items.

    """

    def __init__(self):
        r"""
        :param _InstanceKey: Business system id.
        :type InstanceKey: str
        :param _ServiceName: Application name	.	
        :type ServiceName: str
        :param _OperationNameFilter: API filtering.
        :type OperationNameFilter: str
        :param _ExceptionFilter: Error type filtering.
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: HTTP status code filtering.
        :type ErrorCodeFilter: str
        :param _EventEnable: Application diagnosis switch (deprecated).
        :type EventEnable: bool
        :param _UrlConvergenceSwitch: URL convergence switch. 0: off; 1: on.
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL convergence threshold.	
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: URL convergence rule in the form of a regular expression.	
        :type UrlConvergence: str
        :param _UrlExclude: URL exclusion rule in the form of a regular expression.
        :type UrlExclude: str
        :param _IsRelatedLog: Log feature switch. 0: off; 1: on.
        :type IsRelatedLog: int
        :param _LogSource: Log source.	
        :type LogSource: str
        :param _LogSet: Log set. 
        :type LogSet: str
        :param _LogTopicID: Log topic.
        :type LogTopicID: str
        :param _SnapshotEnable: Method stack snapshot switch: true to enable, false to disable.
        :type SnapshotEnable: bool
        :param _SnapshotTimeout: Slow call listening trigger threshold.
        :type SnapshotTimeout: int
        :param _AgentEnable: Probe master switch.
        :type AgentEnable: bool
        :param _InstrumentList: Component list switch (deprecated).
        :type InstrumentList: list of Instrument
        :param _TraceSquash: Link compression switch (deprecated).
        :type TraceSquash: bool
        :param _DisableMemoryUsed: Specifies the memory threshold for probe fusing.
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: Specifies the CPU threshold for probe fusing.
        :type DisableCpuUsed: int
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._OperationNameFilter = None
        self._ExceptionFilter = None
        self._ErrorCodeFilter = None
        self._EventEnable = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._UrlConvergence = None
        self._UrlExclude = None
        self._IsRelatedLog = None
        self._LogSource = None
        self._LogSet = None
        self._LogTopicID = None
        self._SnapshotEnable = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._InstrumentList = None
        self._TraceSquash = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceKey(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""Application name	.	
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationNameFilter(self):
        r"""API filtering.
        :rtype: str
        """
        return self._OperationNameFilter

    @OperationNameFilter.setter
    def OperationNameFilter(self, OperationNameFilter):
        self._OperationNameFilter = OperationNameFilter

    @property
    def ExceptionFilter(self):
        r"""Error type filtering.
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""HTTP status code filtering.
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def EventEnable(self):
        r"""Application diagnosis switch (deprecated).
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def UrlConvergenceSwitch(self):
        r"""URL convergence switch. 0: off; 1: on.
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL convergence threshold.	
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""URL convergence rule in the form of a regular expression.	
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def UrlExclude(self):
        r"""URL exclusion rule in the form of a regular expression.
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""Log feature switch. 0: off; 1: on.
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogSource(self):
        r"""Log source.	
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogSet(self):
        r"""Log set. 
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogTopicID(self):
        r"""Log topic.
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def SnapshotEnable(self):
        r"""Method stack snapshot switch: true to enable, false to disable.
        :rtype: bool
        """
        return self._SnapshotEnable

    @SnapshotEnable.setter
    def SnapshotEnable(self, SnapshotEnable):
        self._SnapshotEnable = SnapshotEnable

    @property
    def SnapshotTimeout(self):
        r"""Slow call listening trigger threshold.
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""Probe master switch.
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""Component list switch (deprecated).
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""Link compression switch (deprecated).
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def DisableMemoryUsed(self):
        r"""Specifies the memory threshold for probe fusing.
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""Specifies the CPU threshold for probe fusing.
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._OperationNameFilter = params.get("OperationNameFilter")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._EventEnable = params.get("EventEnable")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._UrlConvergence = params.get("UrlConvergence")
        self._UrlExclude = params.get("UrlExclude")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogSource = params.get("LogSource")
        self._LogSet = params.get("LogSet")
        self._LogTopicID = params.get("LogTopicID")
        self._SnapshotEnable = params.get("SnapshotEnable")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        self._TraceSquash = params.get("TraceSquash")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmAssociation(AbstractModel):
    r"""Shows the association between the apm business system and other cloud products in the return format.

    """

    def __init__(self):
        r"""
        :param _PeerId: Associated product instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        :param _Status: Association status: 1 (enabled), 2 (disabled), 3 (invalid).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Topic: Specifies the CKafka message topic.
        :type Topic: str
        """
        self._PeerId = None
        self._Status = None
        self._Topic = None

    @property
    def PeerId(self):
        r"""Associated product instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Status(self):
        r"""Association status: 1 (enabled), 2 (disabled), 3 (invalid).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Topic(self):
        r"""Specifies the CKafka message topic.
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._PeerId = params.get("PeerId")
        self._Status = params.get("Status")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmField(AbstractModel):
    r"""Metric dimension information.

    """

    def __init__(self):
        r"""
        :param _Key: Metric name.
        :type Key: str
        :param _Value: Indicator numerical value.
        :type Value: float
        :param _Unit: Units corresponding to the metric.
        :type Unit: str
        :param _CompareVals: Year-Over-Year result array, recommended to use.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CompareVals: list of APMKVItem
        :param _LastPeriodValue: Indicator numerical value of the previous period in year-over-year comparison.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastPeriodValue: list of APMKV
        :param _CompareVal: Year-On-Year metric value. deprecated, not recommended for use.
        :type CompareVal: str
        :param _NameCN: Metric Chinese Name
        :type NameCN: str
        :param _NameEN: Metric English name
        :type NameEN: str
        """
        self._Key = None
        self._Value = None
        self._Unit = None
        self._CompareVals = None
        self._LastPeriodValue = None
        self._CompareVal = None
        self._NameCN = None
        self._NameEN = None

    @property
    def Key(self):
        r"""Metric name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Indicator numerical value.
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""Units corresponding to the metric.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def CompareVals(self):
        r"""Year-Over-Year result array, recommended to use.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of APMKVItem
        """
        return self._CompareVals

    @CompareVals.setter
    def CompareVals(self, CompareVals):
        self._CompareVals = CompareVals

    @property
    def LastPeriodValue(self):
        r"""Indicator numerical value of the previous period in year-over-year comparison.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of APMKV
        """
        return self._LastPeriodValue

    @LastPeriodValue.setter
    def LastPeriodValue(self, LastPeriodValue):
        self._LastPeriodValue = LastPeriodValue

    @property
    def CompareVal(self):
        r"""Year-On-Year metric value. deprecated, not recommended for use.
        :rtype: str
        """
        return self._CompareVal

    @CompareVal.setter
    def CompareVal(self, CompareVal):
        self._CompareVal = CompareVal

    @property
    def NameCN(self):
        r"""Metric Chinese Name
        :rtype: str
        """
        return self._NameCN

    @NameCN.setter
    def NameCN(self, NameCN):
        self._NameCN = NameCN

    @property
    def NameEN(self):
        r"""Metric English name
        :rtype: str
        """
        return self._NameEN

    @NameEN.setter
    def NameEN(self, NameEN):
        self._NameEN = NameEN


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        if params.get("CompareVals") is not None:
            self._CompareVals = []
            for item in params.get("CompareVals"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._CompareVals.append(obj)
        if params.get("LastPeriodValue") is not None:
            self._LastPeriodValue = []
            for item in params.get("LastPeriodValue"):
                obj = APMKV()
                obj._deserialize(item)
                self._LastPeriodValue.append(obj)
        self._CompareVal = params.get("CompareVal")
        self._NameCN = params.get("NameCN")
        self._NameEN = params.get("NameEN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmInstanceDetail(AbstractModel):
    r"""APM business system information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _Name: Business system name.
        :type Name: str
        :param _Description: Business system description information.
        :type Description: str
        :param _Status: Status of the business system.
{Initializing; running; throttling}.
        :type Status: int
        :param _Region: Region where the business system belongs.
        :type Region: str
        :param _Tags: Business system tag list.
        :type Tags: list of ApmTag
        :param _AppId: AppID information.
        :type AppId: int
        :param _CreateUin: Creator uin.
        :type CreateUin: str
        :param _AmountOfUsedStorage: Storage used (unit: mb).
        :type AmountOfUsedStorage: float
        :param _ServiceCount: Quantity of server applications of the business system.
        :type ServiceCount: int
        :param _CountOfReportSpanPerDay: Average daily reported span count.
        :type CountOfReportSpanPerDay: int
        :param _TraceDuration: Retention period of trace data (unit: days).
        :type TraceDuration: int
        :param _SpanDailyCounters: Business system report limit.
        :type SpanDailyCounters: int
        :param _BillingInstance: Whether the business system billing is Activated (0 = not activated, 1 = activated).
        :type BillingInstance: int
        :param _ErrRateThreshold: Error warning line (unit: %).
        :type ErrRateThreshold: int
        :param _SampleRate: Sampling rate (unit: %).
        :type SampleRate: int
        :param _ErrorSample: Error sampling switch (0: off, 1: on).
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: Sampling slow call saving threshold (unit: ms).
        :type SlowRequestSavedThreshold: int
        :param _LogRegion: CLS log region.
        :type LogRegion: str
        :param _LogSource: Log source.
        :type LogSource: str
        :param _IsRelatedLog: Log feature switch (0: off; 1: on).
        :type IsRelatedLog: int
        :param _LogTopicID: Log topic id.
        :type LogTopicID: str
        :param _ClientCount: Quantity of client applications of the business system.
        :type ClientCount: int
        :param _TotalCount: The quantity of active applications in this business system in the last two days.
        :type TotalCount: int
        :param _LogSet: CLS log set.
        :type LogSet: str
        :param _MetricDuration: Retention period of metric data (unit: days).
        :type MetricDuration: int
        :param _CustomShowTags: List of custom display tags.
        :type CustomShowTags: list of str
        :param _PayMode: Business system billing mode (1: prepaid, 0: pay-as-you-go).
        :type PayMode: int
        :param _PayModeEffective: Indicates whether the billing mode of the business system takes effect.
        :type PayModeEffective: bool
        :param _ResponseDurationWarningThreshold: Response time warning line (unit: ms).
        :type ResponseDurationWarningThreshold: int
        :param _Free: Whether it is free (0 = no; 1 = limited free; 2 = completely free), default 0.
        :type Free: int
        :param _DefaultTSF: Indicates whether it is the default business system of tsf (0 = no, 1 = yes).
        :type DefaultTSF: int
        :param _IsRelatedDashboard: Whether to associate the dashboard (0 = off, 1 = on).
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: Associated dashboard id.
        :type DashboardTopicID: str
        :param _IsInstrumentationVulnerabilityScan: Whether to enable component vulnerability detection (0 = no, 1 = yes).
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: Whether to enable sql injection analysis (0: off, 1: on).
        :type IsSqlInjectionAnalysis: int
        :param _StopReason: Reasons for traffic throttling.
Official version quota;.
Trial version quota.
Trial version expiration;.
Account in arrears.
}.
        :type StopReason: int
        :param _IsRemoteCommandExecutionAnalysis: Whether to enable detection of remote command execution (0 = disabled; 1 = enabled).
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: Whether to enable detection of Java webshell execution (0 = disabled; 1 = enabled).
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS index type. (0 = full-text index; 1 = key-value index).
        :type LogIndexType: int
        :param _LogTraceIdKey: Index key of traceId. It is valid when the CLS index type is key-value index.
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :type IsDeserializationAnalysis: int
        :param _Token: Business system authentication token.
        :type Token: str
        :param _UrlLongSegmentThreshold: Convergence threshold for URL long segments.
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: Convergence threshold for URL numerical segments.
        :type UrlNumberSegmentThreshold: int
        """
        self._InstanceId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Region = None
        self._Tags = None
        self._AppId = None
        self._CreateUin = None
        self._AmountOfUsedStorage = None
        self._ServiceCount = None
        self._CountOfReportSpanPerDay = None
        self._TraceDuration = None
        self._SpanDailyCounters = None
        self._BillingInstance = None
        self._ErrRateThreshold = None
        self._SampleRate = None
        self._ErrorSample = None
        self._SlowRequestSavedThreshold = None
        self._LogRegion = None
        self._LogSource = None
        self._IsRelatedLog = None
        self._LogTopicID = None
        self._ClientCount = None
        self._TotalCount = None
        self._LogSet = None
        self._MetricDuration = None
        self._CustomShowTags = None
        self._PayMode = None
        self._PayModeEffective = None
        self._ResponseDurationWarningThreshold = None
        self._Free = None
        self._DefaultTSF = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsSqlInjectionAnalysis = None
        self._StopReason = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._Token = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Business system name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Business system description information.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""Status of the business system.
{Initializing; running; throttling}.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""Region where the business system belongs.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""Business system tag list.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AppId(self):
        r"""AppID information.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreateUin(self):
        r"""Creator uin.
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def AmountOfUsedStorage(self):
        r"""Storage used (unit: mb).
        :rtype: float
        """
        return self._AmountOfUsedStorage

    @AmountOfUsedStorage.setter
    def AmountOfUsedStorage(self, AmountOfUsedStorage):
        self._AmountOfUsedStorage = AmountOfUsedStorage

    @property
    def ServiceCount(self):
        r"""Quantity of server applications of the business system.
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def CountOfReportSpanPerDay(self):
        r"""Average daily reported span count.
        :rtype: int
        """
        return self._CountOfReportSpanPerDay

    @CountOfReportSpanPerDay.setter
    def CountOfReportSpanPerDay(self, CountOfReportSpanPerDay):
        self._CountOfReportSpanPerDay = CountOfReportSpanPerDay

    @property
    def TraceDuration(self):
        r"""Retention period of trace data (unit: days).
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def SpanDailyCounters(self):
        r"""Business system report limit.
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def BillingInstance(self):
        r"""Whether the business system billing is Activated (0 = not activated, 1 = activated).
        :rtype: int
        """
        return self._BillingInstance

    @BillingInstance.setter
    def BillingInstance(self, BillingInstance):
        self._BillingInstance = BillingInstance

    @property
    def ErrRateThreshold(self):
        r"""Error warning line (unit: %).
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        r"""Sampling rate (unit: %).
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        r"""Error sampling switch (0: off, 1: on).
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        r"""Sampling slow call saving threshold (unit: ms).
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def LogRegion(self):
        r"""CLS log region.
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogSource(self):
        r"""Log source.
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IsRelatedLog(self):
        r"""Log feature switch (0: off; 1: on).
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        r"""Log topic id.
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def ClientCount(self):
        r"""Quantity of client applications of the business system.
        :rtype: int
        """
        return self._ClientCount

    @ClientCount.setter
    def ClientCount(self, ClientCount):
        self._ClientCount = ClientCount

    @property
    def TotalCount(self):
        r"""The quantity of active applications in this business system in the last two days.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogSet(self):
        r"""CLS log set.
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def MetricDuration(self):
        r"""Retention period of metric data (unit: days).
        :rtype: int
        """
        return self._MetricDuration

    @MetricDuration.setter
    def MetricDuration(self, MetricDuration):
        self._MetricDuration = MetricDuration

    @property
    def CustomShowTags(self):
        r"""List of custom display tags.
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        r"""Business system billing mode (1: prepaid, 0: pay-as-you-go).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeEffective(self):
        r"""Indicates whether the billing mode of the business system takes effect.
        :rtype: bool
        """
        return self._PayModeEffective

    @PayModeEffective.setter
    def PayModeEffective(self, PayModeEffective):
        self._PayModeEffective = PayModeEffective

    @property
    def ResponseDurationWarningThreshold(self):
        r"""Response time warning line (unit: ms).
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        r"""Whether it is free (0 = no; 1 = limited free; 2 = completely free), default 0.
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def DefaultTSF(self):
        r"""Indicates whether it is the default business system of tsf (0 = no, 1 = yes).
        :rtype: int
        """
        return self._DefaultTSF

    @DefaultTSF.setter
    def DefaultTSF(self, DefaultTSF):
        self._DefaultTSF = DefaultTSF

    @property
    def IsRelatedDashboard(self):
        r"""Whether to associate the dashboard (0 = off, 1 = on).
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""Associated dashboard id.
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""Whether to enable component vulnerability detection (0 = no, 1 = yes).
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        r"""Whether to enable sql injection analysis (0: off, 1: on).
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def StopReason(self):
        r"""Reasons for traffic throttling.
Official version quota;.
Trial version quota.
Trial version expiration;.
Account in arrears.
}.
        :rtype: int
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""Whether to enable detection of remote command execution (0 = disabled; 1 = enabled).
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""Whether to enable detection of Java webshell execution (0 = disabled; 1 = enabled).
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS index type. (0 = full-text index; 1 = key-value index).
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""Index key of traceId. It is valid when the CLS index type is key-value index.
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def Token(self):
        r"""Business system authentication token.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def UrlLongSegmentThreshold(self):
        r"""Convergence threshold for URL long segments.
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""Convergence threshold for URL numerical segments.
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AppId = params.get("AppId")
        self._CreateUin = params.get("CreateUin")
        self._AmountOfUsedStorage = params.get("AmountOfUsedStorage")
        self._ServiceCount = params.get("ServiceCount")
        self._CountOfReportSpanPerDay = params.get("CountOfReportSpanPerDay")
        self._TraceDuration = params.get("TraceDuration")
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        self._BillingInstance = params.get("BillingInstance")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._SampleRate = params.get("SampleRate")
        self._ErrorSample = params.get("ErrorSample")
        self._SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        self._LogRegion = params.get("LogRegion")
        self._LogSource = params.get("LogSource")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogTopicID = params.get("LogTopicID")
        self._ClientCount = params.get("ClientCount")
        self._TotalCount = params.get("TotalCount")
        self._LogSet = params.get("LogSet")
        self._MetricDuration = params.get("MetricDuration")
        self._CustomShowTags = params.get("CustomShowTags")
        self._PayMode = params.get("PayMode")
        self._PayModeEffective = params.get("PayModeEffective")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._Free = params.get("Free")
        self._DefaultTSF = params.get("DefaultTSF")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._StopReason = params.get("StopReason")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._Token = params.get("Token")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmMetricRecord(AbstractModel):
    r"""Metric list cell.

    """

    def __init__(self):
        r"""
        :param _Fields: Field array, used for the query result of indicators.
        :type Fields: list of ApmField
        :param _Tags: Tag array, used to distinguish the objects of groupby.
        :type Tags: list of ApmTag
        """
        self._Fields = None
        self._Tags = None

    @property
    def Fields(self):
        r"""Field array, used for the query result of indicators.
        :rtype: list of ApmField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        r"""Tag array, used to distinguish the objects of groupby.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = ApmField()
                obj._deserialize(item)
                self._Fields.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmPrometheusRules(AbstractModel):
    r"""Shows the association between the apm business system and prometheus in the return format.

    """

    def __init__(self):
        r"""
        :param _Id: Metric match rule ID.
        :type Id: int
        :param _Name: Metric match rule name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ServiceName: Applications where the rule takes effect. input an empty string for all applications.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _Status: Specifies the metric match rule status: 1 (enabled), 2 (disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _MetricNameRule: Specifies the metric match rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricNameRule: str
        :param _MetricMatchType: Match type: 0 - precision match, 1 - prefix match, 2 - suffix match.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MetricMatchType: int
        """
        self._Id = None
        self._Name = None
        self._ServiceName = None
        self._Status = None
        self._MetricNameRule = None
        self._MetricMatchType = None

    @property
    def Id(self):
        r"""Metric match rule ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Metric match rule name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServiceName(self):
        r"""Applications where the rule takes effect. input an empty string for all applications.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Status(self):
        r"""Specifies the metric match rule status: 1 (enabled), 2 (disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MetricNameRule(self):
        r"""Specifies the metric match rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule

    @property
    def MetricMatchType(self):
        r"""Match type: 0 - precision match, 1 - prefix match, 2 - suffix match.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ServiceName = params.get("ServiceName")
        self._Status = params.get("Status")
        self._MetricNameRule = params.get("MetricNameRule")
        self._MetricMatchType = params.get("MetricMatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmSampleConfig(AbstractModel):
    r"""Sampling configuration

    """

    def __init__(self):
        r"""
        :param _InstanceKey: Instance ID.
        :type InstanceKey: str
        :param _ServiceName: Service name.
        :type ServiceName: str
        :param _SampleName: Sampling name
        :type SampleName: str
        :param _OperationName: API name.
        :type OperationName: str
        :param _SpanNum: Number of spans sampled
        :type SpanNum: int
        :param _Status: Sampling configuration switch. 0: Off; 1: On
        :type Status: int
        :param _Tags: Tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of APMKVItem
        :param _SampleRate: Sampling rate.
        :type SampleRate: int
        :param _OperationType: Specifies the matching method. 0: exact match (default); 1: prefix match; 2: suffix match.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperationType: int
        :param _Id: Configuration ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._SampleName = None
        self._OperationName = None
        self._SpanNum = None
        self._Status = None
        self._Tags = None
        self._SampleRate = None
        self._OperationType = None
        self._Id = None

    @property
    def InstanceKey(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""Service name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SampleName(self):
        r"""Sampling name
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def OperationName(self):
        r"""API name.
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def SpanNum(self):
        r"""Number of spans sampled
        :rtype: int
        """
        return self._SpanNum

    @SpanNum.setter
    def SpanNum(self, SpanNum):
        self._SpanNum = SpanNum

    @property
    def Status(self):
        r"""Sampling configuration switch. 0: Off; 1: On
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""Tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SampleRate(self):
        r"""Sampling rate.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def OperationType(self):
        r"""Specifies the matching method. 0: exact match (default); 1: prefix match; 2: suffix match.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def Id(self):
        r"""Configuration ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._SampleName = params.get("SampleName")
        self._OperationName = params.get("OperationName")
        self._SpanNum = params.get("SpanNum")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SampleRate = params.get("SampleRate")
        self._OperationType = params.get("OperationType")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmServiceMetric(AbstractModel):
    r"""APM application metric information.

    """

    def __init__(self):
        r"""
        :param _Fields: Field array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fields: list of ApmField
        :param _Tags: Tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of ApmTag
        :param _ServiceDetail: Application information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDetail: :class:`tencentcloud.apm.v20210622.models.ServiceDetail`
        """
        self._Fields = None
        self._Tags = None
        self._ServiceDetail = None

    @property
    def Fields(self):
        r"""Field array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        r"""Tag array
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceDetail(self):
        r"""Application information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ServiceDetail`
        """
        return self._ServiceDetail

    @ServiceDetail.setter
    def ServiceDetail(self, ServiceDetail):
        self._ServiceDetail = ServiceDetail


    def _deserialize(self, params):
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = ApmField()
                obj._deserialize(item)
                self._Fields.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceDetail") is not None:
            self._ServiceDetail = ServiceDetail()
            self._ServiceDetail._deserialize(params.get("ServiceDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmTag(AbstractModel):
    r"""Dimension (tag) object.

    """

    def __init__(self):
        r"""
        :param _Key: Dimension key (column name, Tag key).
        :type Key: str
        :param _Value: Dimension value (tag value).
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Dimension key (column name, Tag key).
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Dimension value (tag value).
        :rtype: str
        """
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
        


class CreateApmInstanceRequest(AbstractModel):
    r"""CreateApmInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Business system name.
        :type Name: str
        :param _Description: Business system description information.
        :type Description: str
        :param _TraceDuration: Retention period of trace data (unit: days, the default storage duration is 3 days).
        :type TraceDuration: int
        :param _Tags: Business system tag list.
        :type Tags: list of ApmTag
        :param _SpanDailyCounters: The report quota value of the business system. the default value is 0, indicating no limit on the report quota. (obsolete).
        :type SpanDailyCounters: int
        :param _PayMode: Billing model of the business system (0: pay-as-you-go, 1: prepaid).
        :type PayMode: int
        :param _Free: Whether it is a free edition business system (0 = paid edition; 1 = tsf restricted free edition; 2 = free edition).
        :type Free: int
        """
        self._Name = None
        self._Description = None
        self._TraceDuration = None
        self._Tags = None
        self._SpanDailyCounters = None
        self._PayMode = None
        self._Free = None

    @property
    def Name(self):
        r"""Business system name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Business system description information.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        r"""Retention period of trace data (unit: days, the default storage duration is 3 days).
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Tags(self):
        r"""Business system tag list.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SpanDailyCounters(self):
        r"""The report quota value of the business system. the default value is 0, indicating no limit on the report quota. (obsolete).
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def PayMode(self):
        r"""Billing model of the business system (0: pay-as-you-go, 1: prepaid).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Free(self):
        r"""Whether it is a free edition business system (0 = paid edition; 1 = tsf restricted free edition; 2 = free edition).
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._TraceDuration = params.get("TraceDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        self._PayMode = params.get("PayMode")
        self._Free = params.get("Free")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmInstanceResponse(AbstractModel):
    r"""CreateApmInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateApmPrometheusRuleRequest(AbstractModel):
    r"""CreateApmPrometheusRule request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Metric match rule name.
        :type Name: str
        :param _ServiceName: Applications where the rule takes effect. input an empty string for all applications.
        :type ServiceName: str
        :param _MetricMatchType: Match type: 0 - precision match, 1 - prefix match, 2 - suffix match.
        :type MetricMatchType: int
        :param _MetricNameRule: Specifies the rule for customer-defined metric names with cache hit.
        :type MetricNameRule: str
        :param _InstanceId: Business system ID
        :type InstanceId: str
        """
        self._Name = None
        self._ServiceName = None
        self._MetricMatchType = None
        self._MetricNameRule = None
        self._InstanceId = None

    @property
    def Name(self):
        r"""Metric match rule name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServiceName(self):
        r"""Applications where the rule takes effect. input an empty string for all applications.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def MetricMatchType(self):
        r"""Match type: 0 - precision match, 1 - prefix match, 2 - suffix match.
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType

    @property
    def MetricNameRule(self):
        r"""Specifies the rule for customer-defined metric names with cache hit.
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ServiceName = params.get("ServiceName")
        self._MetricMatchType = params.get("MetricMatchType")
        self._MetricNameRule = params.get("MetricNameRule")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmPrometheusRuleResponse(AbstractModel):
    r"""CreateApmPrometheusRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateApmSampleConfigRequest(AbstractModel):
    r"""CreateApmSampleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _SampleRate: Sampling rate.
        :type SampleRate: int
        :param _ServiceName: Application name
        :type ServiceName: str
        :param _SampleName: Sampling rule name.
        :type SampleName: str
        :param _Tags: Sampling tags
        :type Tags: list of APMKVItem
        :param _OperationName: API name.
        :type OperationName: str
        :param _OperationType: 0: exact match (default); 1: prefix match; 2: suffix match.
        :type OperationType: int
        """
        self._InstanceId = None
        self._SampleRate = None
        self._ServiceName = None
        self._SampleName = None
        self._Tags = None
        self._OperationName = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleRate(self):
        r"""Sampling rate.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ServiceName(self):
        r"""Application name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SampleName(self):
        r"""Sampling rule name.
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def Tags(self):
        r"""Sampling tags
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OperationName(self):
        r"""API name.
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def OperationType(self):
        r"""0: exact match (default); 1: prefix match; 2: suffix match.
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleRate = params.get("SampleRate")
        self._ServiceName = params.get("ServiceName")
        self._SampleName = params.get("SampleName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OperationName = params.get("OperationName")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmSampleConfigResponse(AbstractModel):
    r"""CreateApmSampleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ApmSampleConfig: Sampling configuration parameter
        :type ApmSampleConfig: :class:`tencentcloud.apm.v20210622.models.ApmSampleConfig`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmSampleConfig = None
        self._RequestId = None

    @property
    def ApmSampleConfig(self):
        r"""Sampling configuration parameter
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmSampleConfig`
        """
        return self._ApmSampleConfig

    @ApmSampleConfig.setter
    def ApmSampleConfig(self, ApmSampleConfig):
        self._ApmSampleConfig = ApmSampleConfig

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
        if params.get("ApmSampleConfig") is not None:
            self._ApmSampleConfig = ApmSampleConfig()
            self._ApmSampleConfig._deserialize(params.get("ApmSampleConfig"))
        self._RequestId = params.get("RequestId")


class CreateProfileTaskRequest(AbstractModel):
    r"""CreateProfileTask request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Application name
        :type ServiceName: str
        :param _InstanceId: APM business system ID.
        :type InstanceId: str
        :param _ServiceInstance: Application instance (online).
        :type ServiceInstance: str
        :param _Event: Event type (cpu, alloc).
        :type Event: str
        :param _Duration: Specifies the task duration in milliseconds (ms). value range: 5 to 180 seconds.
        :type Duration: int
        :param _AllTimes: Number of execution. value range: 1-100.
        :type AllTimes: int
        :param _StartTime: Start timestamp. 0 indicates start from the current time (unit: seconds).
        :type StartTime: int
        :param _TaskInterval: Specifies the task execution interval in milliseconds (ms). value range: 10 to 600 seconds. cannot be less than 1.5 times the Duration.
        :type TaskInterval: int
        """
        self._ServiceName = None
        self._InstanceId = None
        self._ServiceInstance = None
        self._Event = None
        self._Duration = None
        self._AllTimes = None
        self._StartTime = None
        self._TaskInterval = None

    @property
    def ServiceName(self):
        r"""Application name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        r"""APM business system ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceInstance(self):
        r"""Application instance (online).
        :rtype: str
        """
        return self._ServiceInstance

    @ServiceInstance.setter
    def ServiceInstance(self, ServiceInstance):
        self._ServiceInstance = ServiceInstance

    @property
    def Event(self):
        r"""Event type (cpu, alloc).
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def Duration(self):
        r"""Specifies the task duration in milliseconds (ms). value range: 5 to 180 seconds.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AllTimes(self):
        r"""Number of execution. value range: 1-100.
        :rtype: int
        """
        return self._AllTimes

    @AllTimes.setter
    def AllTimes(self, AllTimes):
        self._AllTimes = AllTimes

    @property
    def StartTime(self):
        r"""Start timestamp. 0 indicates start from the current time (unit: seconds).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskInterval(self):
        r"""Specifies the task execution interval in milliseconds (ms). value range: 10 to 600 seconds. cannot be less than 1.5 times the Duration.
        :rtype: int
        """
        return self._TaskInterval

    @TaskInterval.setter
    def TaskInterval(self, TaskInterval):
        self._TaskInterval = TaskInterval


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        self._ServiceInstance = params.get("ServiceInstance")
        self._Event = params.get("Event")
        self._Duration = params.get("Duration")
        self._AllTimes = params.get("AllTimes")
        self._StartTime = params.get("StartTime")
        self._TaskInterval = params.get("TaskInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProfileTaskResponse(AbstractModel):
    r"""CreateProfileTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteApmSampleConfigRequest(AbstractModel):
    r"""DeleteApmSampleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _SampleName: Sampling rule name.
        :type SampleName: str
        """
        self._InstanceId = None
        self._SampleName = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""Sampling rule name.
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApmSampleConfigResponse(AbstractModel):
    r"""DeleteApmSampleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeApmAgentRequest(AbstractModel):
    r"""DescribeApmAgent request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _AgentType: Access method: currently supports access and reporting via skywalking, ot, and ebpf methods. if not specified, ot is used by default.
        :type AgentType: str
        :param _NetworkMode: Reporting environment: currently supports pl (private network reporting), public (public network), and inner (self-developed vpc) environment reporting. if not specified, the default is public.
        :type NetworkMode: str
        :param _LanguageEnvironment: Language reporting is now supported for java, golang, php, python, dotnet, nodejs. if not specified, golang is used by default.
        :type LanguageEnvironment: str
        :param _ReportMethod: Reporting method, deprecated.
        :type ReportMethod: str
        """
        self._InstanceId = None
        self._AgentType = None
        self._NetworkMode = None
        self._LanguageEnvironment = None
        self._ReportMethod = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentType(self):
        r"""Access method: currently supports access and reporting via skywalking, ot, and ebpf methods. if not specified, ot is used by default.
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def NetworkMode(self):
        r"""Reporting environment: currently supports pl (private network reporting), public (public network), and inner (self-developed vpc) environment reporting. if not specified, the default is public.
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def LanguageEnvironment(self):
        r"""Language reporting is now supported for java, golang, php, python, dotnet, nodejs. if not specified, golang is used by default.
        :rtype: str
        """
        return self._LanguageEnvironment

    @LanguageEnvironment.setter
    def LanguageEnvironment(self, LanguageEnvironment):
        self._LanguageEnvironment = LanguageEnvironment

    @property
    def ReportMethod(self):
        r"""Reporting method, deprecated.
        :rtype: str
        """
        return self._ReportMethod

    @ReportMethod.setter
    def ReportMethod(self, ReportMethod):
        self._ReportMethod = ReportMethod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentType = params.get("AgentType")
        self._NetworkMode = params.get("NetworkMode")
        self._LanguageEnvironment = params.get("LanguageEnvironment")
        self._ReportMethod = params.get("ReportMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAgentResponse(AbstractModel):
    r"""DescribeApmAgent response structure.

    """

    def __init__(self):
        r"""
        :param _ApmAgent: Agent information.
        :type ApmAgent: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmAgent = None
        self._RequestId = None

    @property
    def ApmAgent(self):
        r"""Agent information.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        """
        return self._ApmAgent

    @ApmAgent.setter
    def ApmAgent(self, ApmAgent):
        self._ApmAgent = ApmAgent

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
        if params.get("ApmAgent") is not None:
            self._ApmAgent = ApmAgentInfo()
            self._ApmAgent._deserialize(params.get("ApmAgent"))
        self._RequestId = params.get("RequestId")


class DescribeApmApplicationConfigRequest(AbstractModel):
    r"""DescribeApmApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ServiceName: Service name
        :type ServiceName: str
        """
        self._InstanceId = None
        self._ServiceName = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""Service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmApplicationConfigResponse(AbstractModel):
    r"""DescribeApmApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ApmAppConfig: Apm application configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmAppConfig: :class:`tencentcloud.apm.v20210622.models.ApmAppConfig`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmAppConfig = None
        self._RequestId = None

    @property
    def ApmAppConfig(self):
        r"""Apm application configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAppConfig`
        """
        return self._ApmAppConfig

    @ApmAppConfig.setter
    def ApmAppConfig(self, ApmAppConfig):
        self._ApmAppConfig = ApmAppConfig

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
        if params.get("ApmAppConfig") is not None:
            self._ApmAppConfig = ApmAppConfig()
            self._ApmAppConfig._deserialize(params.get("ApmAppConfig"))
        self._RequestId = params.get("RequestId")


class DescribeApmAssociationRequest(AbstractModel):
    r"""DescribeApmAssociation request structure.

    """

    def __init__(self):
        r"""
        :param _ProductName: Associated product name. currently only supports Prometheus.
        :type ProductName: str
        :param _InstanceId: Business System Name
        :type InstanceId: str
        """
        self._ProductName = None
        self._InstanceId = None

    @property
    def ProductName(self):
        r"""Associated product name. currently only supports Prometheus.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def InstanceId(self):
        r"""Business System Name
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAssociationResponse(AbstractModel):
    r"""DescribeApmAssociation response structure.

    """

    def __init__(self):
        r"""
        :param _ApmAssociation: Associated product instance ID.
        :type ApmAssociation: :class:`tencentcloud.apm.v20210622.models.ApmAssociation`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmAssociation = None
        self._RequestId = None

    @property
    def ApmAssociation(self):
        r"""Associated product instance ID.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAssociation`
        """
        return self._ApmAssociation

    @ApmAssociation.setter
    def ApmAssociation(self, ApmAssociation):
        self._ApmAssociation = ApmAssociation

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
        if params.get("ApmAssociation") is not None:
            self._ApmAssociation = ApmAssociation()
            self._ApmAssociation._deserialize(params.get("ApmAssociation"))
        self._RequestId = params.get("RequestId")


class DescribeApmInstancesRequest(AbstractModel):
    r"""DescribeApmInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Tags: Tag list.
        :type Tags: list of ApmTag
        :param _InstanceName: Filters by business system name, and fuzzy search is supported.
        :type InstanceName: str
        :param _InstanceId: Filters by business system ID, and fuzzy search is supported.
        :type InstanceId: str
        :param _InstanceIds: Filter by business system id.
        :type InstanceIds: list of str
        :param _DemoInstanceFlag: Whether to query the official demo business system (0 = non-demo business system, 1 = demo business system, default is 0).
        :type DemoInstanceFlag: int
        :param _AllRegionsFlag: Whether to query all regional business systems (0 = do not query all regions, 1 = query all regions, default is 0).
        :type AllRegionsFlag: int
        """
        self._Tags = None
        self._InstanceName = None
        self._InstanceId = None
        self._InstanceIds = None
        self._DemoInstanceFlag = None
        self._AllRegionsFlag = None

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        r"""Filters by business system name, and fuzzy search is supported.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""Filters by business system ID, and fuzzy search is supported.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceIds(self):
        r"""Filter by business system id.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DemoInstanceFlag(self):
        r"""Whether to query the official demo business system (0 = non-demo business system, 1 = demo business system, default is 0).
        :rtype: int
        """
        return self._DemoInstanceFlag

    @DemoInstanceFlag.setter
    def DemoInstanceFlag(self, DemoInstanceFlag):
        self._DemoInstanceFlag = DemoInstanceFlag

    @property
    def AllRegionsFlag(self):
        r"""Whether to query all regional business systems (0 = do not query all regions, 1 = query all regions, default is 0).
        :rtype: int
        """
        return self._AllRegionsFlag

    @AllRegionsFlag.setter
    def AllRegionsFlag(self, AllRegionsFlag):
        self._AllRegionsFlag = AllRegionsFlag


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceIds = params.get("InstanceIds")
        self._DemoInstanceFlag = params.get("DemoInstanceFlag")
        self._AllRegionsFlag = params.get("AllRegionsFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmInstancesResponse(AbstractModel):
    r"""DescribeApmInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: APM business system list.
        :type Instances: list of ApmInstanceDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""APM business system list.
        :rtype: list of ApmInstanceDetail
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmPrometheusRuleRequest(AbstractModel):
    r"""DescribeApmPrometheusRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
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
        


class DescribeApmPrometheusRuleResponse(AbstractModel):
    r"""DescribeApmPrometheusRule response structure.

    """

    def __init__(self):
        r"""
        :param _ApmPrometheusRules: Specifies the metric match rule.
        :type ApmPrometheusRules: list of ApmPrometheusRules
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmPrometheusRules = None
        self._RequestId = None

    @property
    def ApmPrometheusRules(self):
        r"""Specifies the metric match rule.
        :rtype: list of ApmPrometheusRules
        """
        return self._ApmPrometheusRules

    @ApmPrometheusRules.setter
    def ApmPrometheusRules(self, ApmPrometheusRules):
        self._ApmPrometheusRules = ApmPrometheusRules

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
        if params.get("ApmPrometheusRules") is not None:
            self._ApmPrometheusRules = []
            for item in params.get("ApmPrometheusRules"):
                obj = ApmPrometheusRules()
                obj._deserialize(item)
                self._ApmPrometheusRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmSampleConfigRequest(AbstractModel):
    r"""DescribeApmSampleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _SampleName: Sampling rule name.
        :type SampleName: str
        """
        self._InstanceId = None
        self._SampleName = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""Sampling rule name.
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmSampleConfigResponse(AbstractModel):
    r"""DescribeApmSampleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ApmSampleConfigs: Sampling configuration list
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmSampleConfigs: list of ApmSampleConfig
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmSampleConfigs = None
        self._RequestId = None

    @property
    def ApmSampleConfigs(self):
        r"""Sampling configuration list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmSampleConfig
        """
        return self._ApmSampleConfigs

    @ApmSampleConfigs.setter
    def ApmSampleConfigs(self, ApmSampleConfigs):
        self._ApmSampleConfigs = ApmSampleConfigs

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
        if params.get("ApmSampleConfigs") is not None:
            self._ApmSampleConfigs = []
            for item in params.get("ApmSampleConfigs"):
                obj = ApmSampleConfig()
                obj._deserialize(item)
                self._ApmSampleConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmServiceMetricRequest(AbstractModel):
    r"""DescribeApmServiceMetric request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _ServiceName: Application name
        :type ServiceName: str
        :param _ServiceID: Application ID
        :type ServiceID: str
        :param _StartTime: Start time.
        :type StartTime: int
        :param _EndTime: End time.
        :type EndTime: int
        :param _OrderBy: Order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _Demo: Whether to use the demo mode.
        :type Demo: bool
        :param _ServiceStatus: Application status filter criteria. valid values: health, warning, error. if multiple statuses are selected, separate them by commas, for example: "warning,error".
        :type ServiceStatus: str
        :param _Tags: Tag list
        :type Tags: list of ApmTag
        :param _Page: Page number.
        :type Page: int
        :param _PageSize: Page size.
        :type PageSize: int
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._ServiceName = None
        self._ServiceID = None
        self._StartTime = None
        self._EndTime = None
        self._OrderBy = None
        self._Demo = None
        self._ServiceStatus = None
        self._Tags = None
        self._Page = None
        self._PageSize = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""Application name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceID(self):
        r"""Application ID
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OrderBy(self):
        r"""Order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Demo(self):
        r"""Whether to use the demo mode.
        :rtype: bool
        """
        return self._Demo

    @Demo.setter
    def Demo(self, Demo):
        self._Demo = Demo

    @property
    def ServiceStatus(self):
        r"""Application status filter criteria. valid values: health, warning, error. if multiple statuses are selected, separate them by commas, for example: "warning,error".
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def Tags(self):
        r"""Tag list
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Page(self):
        r"""Page number.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""Page size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""Filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceID = params.get("ServiceID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._Demo = params.get("Demo")
        self._ServiceStatus = params.get("ServiceStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
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
        


class DescribeApmServiceMetricResponse(AbstractModel):
    r"""DescribeApmServiceMetric response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceMetricList: List of application metrics.
        :type ServiceMetricList: list of ApmServiceMetric
        :param _TotalCount: Number of applications meeting the filtering conditions.
        :type TotalCount: int
        :param _WarningErrorCount: Warning of the abnormal number of applications.
        :type WarningErrorCount: int
        :param _ApplicationCount: Total number of applications.
        :type ApplicationCount: int
        :param _Page: Page number.
        :type Page: int
        :param _PageSize: Page size.
        :type PageSize: int
        :param _ErrorCount: Indicates the number of abnormal applications.
        :type ErrorCount: int
        :param _WarningCount: Warning of the number of applications.
        :type WarningCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceMetricList = None
        self._TotalCount = None
        self._WarningErrorCount = None
        self._ApplicationCount = None
        self._Page = None
        self._PageSize = None
        self._ErrorCount = None
        self._WarningCount = None
        self._RequestId = None

    @property
    def ServiceMetricList(self):
        r"""List of application metrics.
        :rtype: list of ApmServiceMetric
        """
        return self._ServiceMetricList

    @ServiceMetricList.setter
    def ServiceMetricList(self, ServiceMetricList):
        self._ServiceMetricList = ServiceMetricList

    @property
    def TotalCount(self):
        r"""Number of applications meeting the filtering conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WarningErrorCount(self):
        r"""Warning of the abnormal number of applications.
        :rtype: int
        """
        return self._WarningErrorCount

    @WarningErrorCount.setter
    def WarningErrorCount(self, WarningErrorCount):
        self._WarningErrorCount = WarningErrorCount

    @property
    def ApplicationCount(self):
        r"""Total number of applications.
        :rtype: int
        """
        return self._ApplicationCount

    @ApplicationCount.setter
    def ApplicationCount(self, ApplicationCount):
        self._ApplicationCount = ApplicationCount

    @property
    def Page(self):
        r"""Page number.
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""Page size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ErrorCount(self):
        r"""Indicates the number of abnormal applications.
        :rtype: int
        """
        return self._ErrorCount

    @ErrorCount.setter
    def ErrorCount(self, ErrorCount):
        self._ErrorCount = ErrorCount

    @property
    def WarningCount(self):
        r"""Warning of the number of applications.
        :rtype: int
        """
        return self._WarningCount

    @WarningCount.setter
    def WarningCount(self, WarningCount):
        self._WarningCount = WarningCount

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
        if params.get("ServiceMetricList") is not None:
            self._ServiceMetricList = []
            for item in params.get("ServiceMetricList"):
                obj = ApmServiceMetric()
                obj._deserialize(item)
                self._ServiceMetricList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._WarningErrorCount = params.get("WarningErrorCount")
        self._ApplicationCount = params.get("ApplicationCount")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._ErrorCount = params.get("ErrorCount")
        self._WarningCount = params.get("WarningCount")
        self._RequestId = params.get("RequestId")


class DescribeGeneralApmApplicationConfigRequest(AbstractModel):
    r"""DescribeGeneralApmApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Application name.
        :type ServiceName: str
        :param _InstanceId: Business system id.
        :type InstanceId: str
        """
        self._ServiceName = None
        self._InstanceId = None

    @property
    def ServiceName(self):
        r"""Application name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralApmApplicationConfigResponse(AbstractModel):
    r"""DescribeGeneralApmApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ApmApplicationConfigView: Application configuration item.
        :type ApmApplicationConfigView: :class:`tencentcloud.apm.v20210622.models.ApmApplicationConfigView`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApmApplicationConfigView = None
        self._RequestId = None

    @property
    def ApmApplicationConfigView(self):
        r"""Application configuration item.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmApplicationConfigView`
        """
        return self._ApmApplicationConfigView

    @ApmApplicationConfigView.setter
    def ApmApplicationConfigView(self, ApmApplicationConfigView):
        self._ApmApplicationConfigView = ApmApplicationConfigView

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
        if params.get("ApmApplicationConfigView") is not None:
            self._ApmApplicationConfigView = ApmApplicationConfigView()
            self._ApmApplicationConfigView._deserialize(params.get("ApmApplicationConfigView"))
        self._RequestId = params.get("RequestId")


class DescribeGeneralMetricDataRequest(AbstractModel):
    r"""DescribeGeneralMetricData request structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: Metric name to be queried, which cannot be customized. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :type Metrics: list of str
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _ViewName: View name. the input cannot be customized. [for details, see.](https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1).
        :type ViewName: str
        :param _Filters: The dimension information to be filtered; different views have corresponding metric dimensions. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :type Filters: list of GeneralFilter
        :param _GroupBy: Aggregated dimension; different views have corresponding metric dimensions. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :type GroupBy: list of str
        :param _StartTime: The timestamp of the start time, supporting the query of metric data within 30 days. (unit: seconds).
        :type StartTime: int
        :param _EndTime: The timestamp of the end time, supporting the query of metric data within 30 days. (unit: seconds).
        :type EndTime: int
        :param _Period: Whether to aggregate by a fixed time span: enter 1 for values of 1 and greater, and 0 if not filled in.
-If 0 is filled in, it calculates the metric data from the start time to the cutoff time.
- if 1 is filled in, the aggregation granularity will be selected according to the time span from the start time to the deadline:.
 -If the time span is (0,12) hours, it is aggregated by one-minute granularity.
 -If the time span is [12,48] hours, it is aggregated at a five-minute granularity.
 -If the time span is (48, +∞) hours, it is aggregated at an hourly granularity.
        :type Period: int
        :param _OrderBy: Sort query metrics.
Key: enter the tencentcloud api metric name. [for details, see](https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1) .
Value: specify the sorting method:.     
-Asc: sorts query metrics in ascending order.
- desc: sort query metrics in descending order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _PageSize: Maximum number of queried metrics. currently, up to 50 data entries can be displayed. the value range for pagesize is 1-50. submit pagesize to show the limited number based on the value of pagesize.
        :type PageSize: int
        """
        self._Metrics = None
        self._InstanceId = None
        self._ViewName = None
        self._Filters = None
        self._GroupBy = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._OrderBy = None
        self._PageSize = None

    @property
    def Metrics(self):
        r"""Metric name to be queried, which cannot be customized. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ViewName(self):
        r"""View name. the input cannot be customized. [for details, see.](https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1).
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Filters(self):
        r"""The dimension information to be filtered; different views have corresponding metric dimensions. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :rtype: list of GeneralFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        r"""Aggregated dimension; different views have corresponding metric dimensions. (for details, see <https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1>.).
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def StartTime(self):
        r"""The timestamp of the start time, supporting the query of metric data within 30 days. (unit: seconds).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""The timestamp of the end time, supporting the query of metric data within 30 days. (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""Whether to aggregate by a fixed time span: enter 1 for values of 1 and greater, and 0 if not filled in.
-If 0 is filled in, it calculates the metric data from the start time to the cutoff time.
- if 1 is filled in, the aggregation granularity will be selected according to the time span from the start time to the deadline:.
 -If the time span is (0,12) hours, it is aggregated by one-minute granularity.
 -If the time span is [12,48] hours, it is aggregated at a five-minute granularity.
 -If the time span is (48, +∞) hours, it is aggregated at an hourly granularity.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OrderBy(self):
        r"""Sort query metrics.
Key: enter the tencentcloud api metric name. [for details, see](https://intl.cloud.tencent.com/document/product/248/101681?from_cn_redirect=1) .
Value: specify the sorting method:.     
-Asc: sorts query metrics in ascending order.
- desc: sort query metrics in descending order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def PageSize(self):
        r"""Maximum number of queried metrics. currently, up to 50 data entries can be displayed. the value range for pagesize is 1-50. submit pagesize to show the limited number based on the value of pagesize.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Metrics = params.get("Metrics")
        self._InstanceId = params.get("InstanceId")
        self._ViewName = params.get("ViewName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = GeneralFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._GroupBy = params.get("GroupBy")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralMetricDataResponse(AbstractModel):
    r"""DescribeGeneralMetricData response structure.

    """

    def __init__(self):
        r"""
        :param _Records: Indicator result set.
        :type Records: list of Line
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        r"""Indicator result set.
        :rtype: list of Line
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = Line()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralOTSpanListRequest(AbstractModel):
    r"""DescribeGeneralOTSpanList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _StartTime: Span query start timestamp (unit: seconds).
        :type StartTime: int
        :param _EndTime: Span query end timestamp (unit: seconds).
        :type EndTime: int
        :param _Filters: Universal filter parameters.
        :type Filters: list of Filter
        :param _OrderBy: Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: The service name of the business itself. console users should fill in taw.
        :type BusinessName: str
        :param _Limit: Number of items per page, defaults to 10,000, valid value range is 0 – 10,000.
        :type Limit: int
        :param _Offset: Pagination.
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Span query start timestamp (unit: seconds).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Span query end timestamp (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""Universal filter parameters.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""The service name of the business itself. console users should fill in taw.
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""Number of items per page, defaults to 10,000, valid value range is 0 – 10,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralOTSpanListResponse(AbstractModel):
    r"""DescribeGeneralOTSpanList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _Spans: The Spans field contains the entire content of the link data. since the data is compressed, perform the following three steps to switch back to the original text.
Decode the text in the Spans field with Base64 to get the compressed byte[].
Use gzip to decompress the compressed byte array and get the byte array before compression.
Uses UTF-8 character set to convert byte[] before compression to text.

        :type Spans: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""The Spans field contains the entire content of the link data. since the data is compressed, perform the following three steps to switch back to the original text.
Decode the text in the Spans field with Base64 to get the compressed byte[].
Use gzip to decompress the compressed byte array and get the byte array before compression.
Uses UTF-8 character set to convert byte[] before compression to text.

        :rtype: str
        """
        return self._Spans

    @Spans.setter
    def Spans(self, Spans):
        self._Spans = Spans

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
        self._TotalCount = params.get("TotalCount")
        self._Spans = params.get("Spans")
        self._RequestId = params.get("RequestId")


class DescribeGeneralSpanListRequest(AbstractModel):
    r"""DescribeGeneralSpanList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _StartTime: Span query start timestamp (unit: seconds).
        :type StartTime: int
        :param _EndTime: Span query end timestamp (unit: seconds).
        :type EndTime: int
        :param _Filters: Universal filter parameters.
        :type Filters: list of Filter
        :param _OrderBy: Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: The service name of the business itself. console users should fill in taw.
        :type BusinessName: str
        :param _Limit: Number of items per page, defaults to 10,000, valid values are 0 to 10,000.
        :type Limit: int
        :param _Offset: Pagination.
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Span query start timestamp (unit: seconds).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Span query end timestamp (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""Universal filter parameters.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""The service name of the business itself. console users should fill in taw.
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""Number of items per page, defaults to 10,000, valid values are 0 to 10,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralSpanListResponse(AbstractModel):
    r"""DescribeGeneralSpanList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _Spans: Span pagination list.
        :type Spans: list of Span
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""Span pagination list.
        :rtype: list of Span
        """
        return self._Spans

    @Spans.setter
    def Spans(self, Spans):
        self._Spans = Spans

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Spans") is not None:
            self._Spans = []
            for item in params.get("Spans"):
                obj = Span()
                obj._deserialize(item)
                self._Spans.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMetricRecordsRequest(AbstractModel):
    r"""DescribeMetricRecords request structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: Metric list.
        :type Metrics: list of QueryMetricItem
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _StartTime: Start time (unit: sec).
        :type StartTime: int
        :param _EndTime: End time (unit: seconds).
        :type EndTime: int
        :param _GroupBy: Aggregation dimension.
        :type GroupBy: list of str
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        :param _OrFilters: Or filter criteria.
        :type OrFilters: list of Filter
        :param _OrderBy: Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: The service name of the business itself. console users should fill in taw.
        :type BusinessName: str
        :param _Type: Special handling of query results.
        :type Type: str
        :param _Limit: Size per page, defaults to 1,000, valid value range is 0 – 1,000.
        :type Limit: int
        :param _Offset: Paging starting point.
        :type Offset: int
        :param _PageIndex: Page number.
        :type PageIndex: int
        :param _PageSize: Page length.
        :type PageSize: int
        """
        self._Metrics = None
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._GroupBy = None
        self._Filters = None
        self._OrFilters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._PageIndex = None
        self._PageSize = None

    @property
    def Metrics(self):
        r"""Metric list.
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time (unit: sec).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def GroupBy(self):
        r"""Aggregation dimension.
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Filters(self):
        r"""Filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrFilters(self):
        r"""Or filter criteria.
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def OrderBy(self):
        r"""Sort
.
The currently supported keys are:.

-StartTime (start time).
-EndTime (end time).
-Duration (response time).

The currently supported values are:.

- desc: sort in descending order.
-Asc - ascending order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""The service name of the business itself. console users should fill in taw.
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Type(self):
        r"""Special handling of query results.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        r"""Size per page, defaults to 1,000, valid value range is 0 – 1,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Paging starting point.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PageIndex(self):
        r"""Page number.
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""Page length.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GroupBy = params.get("GroupBy")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrFilters") is not None:
            self._OrFilters = []
            for item in params.get("OrFilters"):
                obj = Filter()
                obj._deserialize(item)
                self._OrFilters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricRecordsResponse(AbstractModel):
    r"""DescribeMetricRecords response structure.

    """

    def __init__(self):
        r"""
        :param _Records: Indicator result set.
        :type Records: list of ApmMetricRecord
        :param _TotalCount: Number of metric query result sets.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        r"""Indicator result set.
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def TotalCount(self):
        r"""Number of metric query result sets.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServiceOverviewRequest(AbstractModel):
    r"""DescribeServiceOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Metrics: Metric list.
        :type Metrics: list of QueryMetricItem
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _GroupBy: Aggregation dimension.
        :type GroupBy: list of str
        :param _StartTime: Start time (unit: sec).
        :type StartTime: int
        :param _EndTime: End time (unit: seconds).
        :type EndTime: int
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        :param _OrderBy: Sorting method
.
Value: fill in.
-Asc: sorts query metrics in ascending order.
- desc: sort query metrics in descending order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _Limit: Page size.
        :type Limit: int
        :param _Offset: Paging starting point.
        :type Offset: int
        """
        self._Metrics = None
        self._InstanceId = None
        self._GroupBy = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def Metrics(self):
        r"""Metric list.
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupBy(self):
        r"""Aggregation dimension.
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def StartTime(self):
        r"""Start time (unit: sec).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""Filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""Sorting method
.
Value: fill in.
-Asc: sorts query metrics in ascending order.
- desc: sort query metrics in descending order.
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""Page size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Paging starting point.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._GroupBy = params.get("GroupBy")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceOverviewResponse(AbstractModel):
    r"""DescribeServiceOverview response structure.

    """

    def __init__(self):
        r"""
        :param _Records: Indicator result set.
        :type Records: list of ApmMetricRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        r"""Indicator result set.
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    r"""DescribeTagValues request structure.

    """

    def __init__(self):
        r"""
        :param _TagKey: Dimension name.
        :type TagKey: str
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _StartTime: Start time (unit: sec).
        :type StartTime: int
        :param _EndTime: End time (unit: seconds).
        :type EndTime: int
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        :param _OrFilters: Or filter criteria.
        :type OrFilters: list of Filter
        :param _Type: Usage type.
        :type Type: str
        """
        self._TagKey = None
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrFilters = None
        self._Type = None

    @property
    def TagKey(self):
        r"""Dimension name.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time (unit: sec).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time (unit: seconds).
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""Filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrFilters(self):
        r"""Or filter criteria.
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def Type(self):
        r"""Usage type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrFilters") is not None:
            self._OrFilters = []
            for item in params.get("OrFilters"):
                obj = Filter()
                obj._deserialize(item)
                self._OrFilters.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    r"""DescribeTagValues response structure.

    """

    def __init__(self):
        r"""
        :param _Values: Dimension value list.
        :type Values: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Values = None
        self._RequestId = None

    @property
    def Values(self):
        r"""Dimension value list.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

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
        self._Values = params.get("Values")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Queries filter parameters.

    """

    def __init__(self):
        r"""
        :param _Type: Filtering method (=, !=, in).
        :type Type: str
        :param _Key: Filter dimension name.
        :type Key: str
        :param _Value: Filter value. uses commas to separate multiple values in in filtering method.
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        r"""Filtering method (=, !=, in).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""Filter dimension name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Filter value. uses commas to separate multiple values in in filtering method.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralFilter(AbstractModel):
    r"""Queries filter parameters.

    """

    def __init__(self):
        r"""
        :param _Key: Filter dimension name.
        :type Key: str
        :param _Value: Values after filtering.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Filter dimension name.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Values after filtering.
        :rtype: str
        """
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
        


class Instrument(AbstractModel):
    r"""Component.

    """

    def __init__(self):
        r"""
        :param _Name: Component name.
        :type Name: str
        :param _Enable: Component switch.
        :type Enable: bool
        """
        self._Name = None
        self._Enable = None

    @property
    def Name(self):
        r"""Component name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        r"""Component switch.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Line(AbstractModel):
    r"""Metric curve data.

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name.
        :type MetricName: str
        :param _MetricNameCN: Metric chinese name.
        :type MetricNameCN: str
        :param _TimeSerial: Time series.
        :type TimeSerial: list of int
        :param _DataSerial: Data sequence.
        :type DataSerial: list of float
        :param _Tags: Dimension list.
        :type Tags: list of ApmTag
        :param _MetricUnit: Metric data unit
        :type MetricUnit: str
        """
        self._MetricName = None
        self._MetricNameCN = None
        self._TimeSerial = None
        self._DataSerial = None
        self._Tags = None
        self._MetricUnit = None

    @property
    def MetricName(self):
        r"""Metric name.
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricNameCN(self):
        r"""Metric chinese name.
        :rtype: str
        """
        return self._MetricNameCN

    @MetricNameCN.setter
    def MetricNameCN(self, MetricNameCN):
        self._MetricNameCN = MetricNameCN

    @property
    def TimeSerial(self):
        r"""Time series.
        :rtype: list of int
        """
        return self._TimeSerial

    @TimeSerial.setter
    def TimeSerial(self, TimeSerial):
        self._TimeSerial = TimeSerial

    @property
    def DataSerial(self):
        r"""Data sequence.
        :rtype: list of float
        """
        return self._DataSerial

    @DataSerial.setter
    def DataSerial(self, DataSerial):
        self._DataSerial = DataSerial

    @property
    def Tags(self):
        r"""Dimension list.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MetricUnit(self):
        r"""Metric data unit
        :rtype: str
        """
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._MetricNameCN = params.get("MetricNameCN")
        self._TimeSerial = params.get("TimeSerial")
        self._DataSerial = params.get("DataSerial")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmApplicationConfigRequest(AbstractModel):
    r"""ModifyApmApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID.
        :type InstanceId: str
        :param _ServiceName: Application name
        :type ServiceName: str
        :param _UrlConvergenceSwitch: URL convergence switch. 0: Off; 1: On
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL convergence threshold
        :type UrlConvergenceThreshold: int
        :param _ExceptionFilter: Regex rules for exception filtering, separated by commas
        :type ExceptionFilter: str
        :param _UrlConvergence: Regex rules for URL convergence, separated by commas
        :type UrlConvergence: str
        :param _ErrorCodeFilter: Error code filtering, separated by commas
        :type ErrorCodeFilter: str
        :param _UrlExclude: Regex rules for URL exclusion, separated by commas
        :type UrlExclude: str
        :param _IsRelatedLog: Log switch. 0: Off; 1: On
        :type IsRelatedLog: int
        :param _LogRegion: Log region.
        :type LogRegion: str
        :param _LogTopicID: Log topic ID
        :type LogTopicID: str
        :param _LogSet: CLS log set/ES cluster ID
        :type LogSet: str
        :param _LogSource: Log source: CLS or ES
        :type LogSource: str
        :param _IgnoreOperationName: APIs to be filtered
        :type IgnoreOperationName: str
        :param _EnableSnapshot: Whether thread profiling is enabled.
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: Timeout threshold for thread profiling.
        :type SnapshotTimeout: int
        :param _AgentEnable: Whether agent is enabled.
        :type AgentEnable: bool
        :param _TraceSquash: Whether link compression is enabled.
        :type TraceSquash: bool
        :param _EventEnable: Switch for enabling application diagnosis.
        :type EventEnable: bool
        :param _InstrumentList: Component List
        :type InstrumentList: list of Instrument
        :param _AgentOperationConfigView: Related configurations of the probe APIs.
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: Whether to enable application log configuration.
        :type EnableLogConfig: bool
        :param _EnableDashboardConfig: Whether to enable the dashboard configuration for applications. false: disabled (consistent with the business system configuration); true: enabled (application-level configuration).
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: Whether to associate with Dashboard. 0: disabled; 1: enabled.
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
        :type DashboardTopicID: str
        :param _LogIndexType: CLS index type. (0 = full-text index; 1 = key-value index).
        :type LogIndexType: int
        :param _LogTraceIdKey: Index key of traceId. It is valid when the CLS index type is key-value index.
        :type LogTraceIdKey: str
        :param _EnableSecurityConfig: Whether to enable the application security configuration.
        :type EnableSecurityConfig: bool
        :param _IsSqlInjectionAnalysis: Whether to enable SQL injection analysis.
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: Whether to enable detection of component vulnerability.
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: Whether remote command detection is enabled.
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: Whether to enable detection of Java webshell.
        :type IsMemoryHijackingAnalysis: int
        :param _IsDeleteAnyFileAnalysis: Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: Automatic convergence switch for APIs. 0: disabled | 1: enabled.
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: Convergence threshold for URL long segments.
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: Convergence threshold for URL numerical segments.
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: Specifies the memory threshold for probe fusing.
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: Specifies the CPU threshold for probe fusing.
        :type DisableCpuUsed: int
        """
        self._InstanceId = None
        self._ServiceName = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._ExceptionFilter = None
        self._UrlConvergence = None
        self._ErrorCodeFilter = None
        self._UrlExclude = None
        self._IsRelatedLog = None
        self._LogRegion = None
        self._LogTopicID = None
        self._LogSet = None
        self._LogSource = None
        self._IgnoreOperationName = None
        self._EnableSnapshot = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._TraceSquash = None
        self._EventEnable = None
        self._InstrumentList = None
        self._AgentOperationConfigView = None
        self._EnableLogConfig = None
        self._EnableDashboardConfig = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._EnableSecurityConfig = None
        self._IsSqlInjectionAnalysis = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlAutoConvergenceEnable = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceId(self):
        r"""Business system ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""Application name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""URL convergence switch. 0: Off; 1: On
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL convergence threshold
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def ExceptionFilter(self):
        r"""Regex rules for exception filtering, separated by commas
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def UrlConvergence(self):
        r"""Regex rules for URL convergence, separated by commas
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ErrorCodeFilter(self):
        r"""Error code filtering, separated by commas
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def UrlExclude(self):
        r"""Regex rules for URL exclusion, separated by commas
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""Log switch. 0: Off; 1: On
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        r"""Log region.
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        r"""Log topic ID
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        r"""CLS log set/ES cluster ID
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        r"""Log source: CLS or ES
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IgnoreOperationName(self):
        r"""APIs to be filtered
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def EnableSnapshot(self):
        r"""Whether thread profiling is enabled.
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""Timeout threshold for thread profiling.
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""Whether agent is enabled.
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def TraceSquash(self):
        r"""Whether link compression is enabled.
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""Switch for enabling application diagnosis.
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def InstrumentList(self):
        r"""Component List
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def AgentOperationConfigView(self):
        r"""Related configurations of the probe APIs.
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""Whether to enable application log configuration.
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def EnableDashboardConfig(self):
        r"""Whether to enable the dashboard configuration for applications. false: disabled (consistent with the business system configuration); true: enabled (application-level configuration).
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""Whether to associate with Dashboard. 0: disabled; 1: enabled.
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""dashboard ID
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def LogIndexType(self):
        r"""CLS index type. (0 = full-text index; 1 = key-value index).
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""Index key of traceId. It is valid when the CLS index type is key-value index.
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def EnableSecurityConfig(self):
        r"""Whether to enable the application security configuration.
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsSqlInjectionAnalysis(self):
        r"""Whether to enable SQL injection analysis.
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""Whether to enable detection of component vulnerability.
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""Whether remote command detection is enabled.
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""Whether to enable detection of Java webshell.
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""Automatic convergence switch for APIs. 0: disabled | 1: enabled.
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""Convergence threshold for URL long segments.
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""Convergence threshold for URL numerical segments.
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""Specifies the memory threshold for probe fusing.
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""Specifies the CPU threshold for probe fusing.
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._UrlConvergence = params.get("UrlConvergence")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._UrlExclude = params.get("UrlExclude")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogRegion = params.get("LogRegion")
        self._LogTopicID = params.get("LogTopicID")
        self._LogSet = params.get("LogSet")
        self._LogSource = params.get("LogSource")
        self._IgnoreOperationName = params.get("IgnoreOperationName")
        self._EnableSnapshot = params.get("EnableSnapshot")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        self._TraceSquash = params.get("TraceSquash")
        self._EventEnable = params.get("EventEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        if params.get("AgentOperationConfigView") is not None:
            self._AgentOperationConfigView = AgentOperationConfigView()
            self._AgentOperationConfigView._deserialize(params.get("AgentOperationConfigView"))
        self._EnableLogConfig = params.get("EnableLogConfig")
        self._EnableDashboardConfig = params.get("EnableDashboardConfig")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._EnableSecurityConfig = params.get("EnableSecurityConfig")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlAutoConvergenceEnable = params.get("UrlAutoConvergenceEnable")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmApplicationConfigResponse(AbstractModel):
    r"""ModifyApmApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyApmAssociationRequest(AbstractModel):
    r"""ModifyApmAssociation request structure.

    """

    def __init__(self):
        r"""
        :param _ProductName: Associated product name. currently only supports Prometheus.
        :type ProductName: str
        :param _Status: Status of the association relationship: // association status: 1 (enabled), 2 (disabled), 4 (deleted).
        :type Status: int
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _PeerId: Associated product instance ID.
        :type PeerId: str
        :param _Topic: Specifies the CKafka message topic.
        :type Topic: str
        """
        self._ProductName = None
        self._Status = None
        self._InstanceId = None
        self._PeerId = None
        self._Topic = None

    @property
    def ProductName(self):
        r"""Associated product name. currently only supports Prometheus.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Status(self):
        r"""Status of the association relationship: // association status: 1 (enabled), 2 (disabled), 4 (deleted).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PeerId(self):
        r"""Associated product instance ID.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Topic(self):
        r"""Specifies the CKafka message topic.
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._PeerId = params.get("PeerId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmAssociationResponse(AbstractModel):
    r"""ModifyApmAssociation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyApmInstanceRequest(AbstractModel):
    r"""ModifyApmInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _Name: Business system name.
        :type Name: str
        :param _Tags: Tag list.
        :type Tags: list of ApmTag
        :param _Description: Business system description.
        :type Description: str
        :param _TraceDuration: Retention period of trace data (unit: days).
        :type TraceDuration: int
        :param _OpenBilling: Billing switch.
        :type OpenBilling: bool
        :param _SpanDailyCounters: Business system report limit.
        :type SpanDailyCounters: int
        :param _ErrRateThreshold: Error rate warning line. when the average error rate of the application exceeds this threshold, the system will give an abnormal note.
        :type ErrRateThreshold: int
        :param _SampleRate: Sampling rate (unit: %).
        :type SampleRate: int
        :param _ErrorSample: Error sampling switch (0: off, 1: on).
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: Sampling slow call saving threshold (unit: ms).
        :type SlowRequestSavedThreshold: int
        :param _IsRelatedLog: Log feature switch (0: off; 1: on).
        :type IsRelatedLog: int
        :param _LogRegion: Log region, which takes effect after the log feature is enabled.
        :type LogRegion: str
        :param _LogTopicID: CLS log topic id, which takes effect after the log feature is enabled.
        :type LogTopicID: str
        :param _LogSet: Logset, which takes effect only after the log feature is enabled.
        :type LogSet: str
        :param _LogSource: Log source, which takes effect only after the log feature is enabled.
        :type LogSource: str
        :param _CustomShowTags: List of custom display tags.
        :type CustomShowTags: list of str
        :param _PayMode: Modify billing mode (1: prepaid, 0: pay-as-you-go).
        :type PayMode: int
        :param _ResponseDurationWarningThreshold: Response time warning line.
        :type ResponseDurationWarningThreshold: int
        :param _Free: Whether it is free (0 = paid edition; 1 = tsf restricted free edition; 2 = free edition), default 0.
        :type Free: int
        :param _IsRelatedDashboard: Whether to associate the dashboard (0 = off, 1 = on).
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: Associated dashboard id, which takes effect after the associated dashboard is enabled.
        :type DashboardTopicID: str
        :param _IsSqlInjectionAnalysis: SQL injection detection switch (0: off, 1: on).
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: Whether to enable component vulnerability detection (0 = no, 1 = yes).
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: Whether to enable detection of the remote command attack.
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: Whether to enable detection of Java webshell.
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS index type. (0 = full-text index; 1 = key-value index).
        :type LogIndexType: int
        :param _LogTraceIdKey: Index key of traceId. It is valid when the CLS index type is key-value index.
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :type IsDeserializationAnalysis: int
        :param _UrlLongSegmentThreshold: Convergence threshold for URL long segments.
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: Convergence threshold for URL numerical segments.
        :type UrlNumberSegmentThreshold: int
        """
        self._InstanceId = None
        self._Name = None
        self._Tags = None
        self._Description = None
        self._TraceDuration = None
        self._OpenBilling = None
        self._SpanDailyCounters = None
        self._ErrRateThreshold = None
        self._SampleRate = None
        self._ErrorSample = None
        self._SlowRequestSavedThreshold = None
        self._IsRelatedLog = None
        self._LogRegion = None
        self._LogTopicID = None
        self._LogSet = None
        self._LogSource = None
        self._CustomShowTags = None
        self._PayMode = None
        self._ResponseDurationWarningThreshold = None
        self._Free = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._IsSqlInjectionAnalysis = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Business system name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        r"""Business system description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        r"""Retention period of trace data (unit: days).
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def OpenBilling(self):
        r"""Billing switch.
        :rtype: bool
        """
        return self._OpenBilling

    @OpenBilling.setter
    def OpenBilling(self, OpenBilling):
        self._OpenBilling = OpenBilling

    @property
    def SpanDailyCounters(self):
        r"""Business system report limit.
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def ErrRateThreshold(self):
        r"""Error rate warning line. when the average error rate of the application exceeds this threshold, the system will give an abnormal note.
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        r"""Sampling rate (unit: %).
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        r"""Error sampling switch (0: off, 1: on).
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        r"""Sampling slow call saving threshold (unit: ms).
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def IsRelatedLog(self):
        r"""Log feature switch (0: off; 1: on).
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        r"""Log region, which takes effect after the log feature is enabled.
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        r"""CLS log topic id, which takes effect after the log feature is enabled.
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        r"""Logset, which takes effect only after the log feature is enabled.
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        r"""Log source, which takes effect only after the log feature is enabled.
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def CustomShowTags(self):
        r"""List of custom display tags.
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        r"""Modify billing mode (1: prepaid, 0: pay-as-you-go).
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResponseDurationWarningThreshold(self):
        r"""Response time warning line.
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        r"""Whether it is free (0 = paid edition; 1 = tsf restricted free edition; 2 = free edition), default 0.
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def IsRelatedDashboard(self):
        r"""Whether to associate the dashboard (0 = off, 1 = on).
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""Associated dashboard id, which takes effect after the associated dashboard is enabled.
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsSqlInjectionAnalysis(self):
        r"""SQL injection detection switch (0: off, 1: on).
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""Whether to enable component vulnerability detection (0 = no, 1 = yes).
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""Whether to enable detection of the remote command attack.
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""Whether to enable detection of Java webshell.
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS index type. (0 = full-text index; 1 = key-value index).
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""Index key of traceId. It is valid when the CLS index type is key-value index.
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""Whether to enable the detection of deleting arbitrary files. (0 - disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""Whether to enable the detection of reading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""Whether to enable the detection of uploading arbitrary files. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""Whether to enable the detection of the inclusion of arbitrary files. (0: disabled, 1: enabled.)
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""Whether to enable traversal detection of the directory. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""Whether to enable template engine injection detection. (0: disabled; 1: enabled.)
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""Whether to enable script engine injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""Whether to enable expression injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""Whether to enable JNDI injection detection. (0 - disabled; 1 - enabled.)
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""Whether to enable JNI injection detection. (0 - disabled, 1 - enabled).
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""Whether to enable Webshell backdoor detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""Whether to enable deserialization detection. (0 - disabled; 1 - enabled).
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlLongSegmentThreshold(self):
        r"""Convergence threshold for URL long segments.
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""Convergence threshold for URL numerical segments.
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        self._TraceDuration = params.get("TraceDuration")
        self._OpenBilling = params.get("OpenBilling")
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._SampleRate = params.get("SampleRate")
        self._ErrorSample = params.get("ErrorSample")
        self._SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogRegion = params.get("LogRegion")
        self._LogTopicID = params.get("LogTopicID")
        self._LogSet = params.get("LogSet")
        self._LogSource = params.get("LogSource")
        self._CustomShowTags = params.get("CustomShowTags")
        self._PayMode = params.get("PayMode")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._Free = params.get("Free")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmInstanceResponse(AbstractModel):
    r"""ModifyApmInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyApmPrometheusRuleRequest(AbstractModel):
    r"""ModifyApmPrometheusRule request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Rule ID
        :type Id: int
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _Name: Specifies the rule name to modify.
        :type Name: str
        :param _Status: Rule status: 1 (enabled), 2 (disabled), 3 (deleted).
        :type Status: int
        :param _ServiceName: Applications where the rule takes effect. input an empty string for all applications. if this is not modified, pass the old rule.
        :type ServiceName: str
        :param _MetricMatchType: Match type: 0 - precision match, 1 - prefix match, 2 - suffix match (if not modified, the old rule must be passed).
        :type MetricMatchType: int
        :param _MetricNameRule: Specifies the rule for customer-defined metric names with cache hit.
        :type MetricNameRule: str
        """
        self._Id = None
        self._InstanceId = None
        self._Name = None
        self._Status = None
        self._ServiceName = None
        self._MetricMatchType = None
        self._MetricNameRule = None

    @property
    def Id(self):
        r"""Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""Specifies the rule name to modify.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""Rule status: 1 (enabled), 2 (disabled), 3 (deleted).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ServiceName(self):
        r"""Applications where the rule takes effect. input an empty string for all applications. if this is not modified, pass the old rule.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def MetricMatchType(self):
        r"""Match type: 0 - precision match, 1 - prefix match, 2 - suffix match (if not modified, the old rule must be passed).
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType

    @property
    def MetricNameRule(self):
        r"""Specifies the rule for customer-defined metric names with cache hit.
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ServiceName = params.get("ServiceName")
        self._MetricMatchType = params.get("MetricMatchType")
        self._MetricNameRule = params.get("MetricNameRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmPrometheusRuleResponse(AbstractModel):
    r"""ModifyApmPrometheusRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyApmSampleConfigRequest(AbstractModel):
    r"""ModifyApmSampleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _SampleName: Sampling rule name.
        :type SampleName: str
        :param _SampleRate: Sampling rate.
        :type SampleRate: int
        :param _ServiceName: Application name. specifies the application name. fill in the blank to take effect on all applications.
        :type ServiceName: str
        :param _OperationName: API name.
        :type OperationName: str
        :param _Tags: Sampling tag
        :type Tags: list of APMKVItem
        :param _Status: Sampling switch. 0: Off; 1: On; 2: Delete
        :type Status: int
        :param _Id: Configuration ID.
        :type Id: int
        :param _OperationType: 0: exact match (default); 1: prefix match; 2: suffix match.
        :type OperationType: int
        """
        self._InstanceId = None
        self._SampleName = None
        self._SampleRate = None
        self._ServiceName = None
        self._OperationName = None
        self._Tags = None
        self._Status = None
        self._Id = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""Business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""Sampling rule name.
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def SampleRate(self):
        r"""Sampling rate.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ServiceName(self):
        r"""Application name. specifies the application name. fill in the blank to take effect on all applications.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationName(self):
        r"""API name.
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def Tags(self):
        r"""Sampling tag
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        r"""Sampling switch. 0: Off; 1: On; 2: Delete
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Configuration ID.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationType(self):
        r"""0: exact match (default); 1: prefix match; 2: suffix match.
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        self._SampleRate = params.get("SampleRate")
        self._ServiceName = params.get("ServiceName")
        self._OperationName = params.get("OperationName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmSampleConfigResponse(AbstractModel):
    r"""ModifyApmSampleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyGeneralApmApplicationConfigRequest(AbstractModel):
    r"""ModifyGeneralApmApplicationConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        :param _Tags: Fields to be modified. the key and value respectively specify the field name and field value.
.
For specific fields, please refer to.
        :type Tags: list of ApmTag
        :param _ServiceNames: Name of the application list that requires configuration modification.	
        :type ServiceNames: list of str
        """
        self._InstanceId = None
        self._Tags = None
        self._ServiceNames = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tags(self):
        r"""Fields to be modified. the key and value respectively specify the field name and field value.
.
For specific fields, please refer to.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceNames(self):
        r"""Name of the application list that requires configuration modification.	
        :rtype: list of str
        """
        return self._ServiceNames

    @ServiceNames.setter
    def ServiceNames(self, ServiceNames):
        self._ServiceNames = ServiceNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ServiceNames = params.get("ServiceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGeneralApmApplicationConfigResponse(AbstractModel):
    r"""ModifyGeneralApmApplicationConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Description of the returned value.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        r"""Description of the returned value.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class OrderBy(AbstractModel):
    r"""Sorting fields.

    """

    def __init__(self):
        r"""
        :param _Key: Sort field (starttime, endtime, duration are supported).
        :type Key: str
        :param _Value: ASC: sequential sorting / desc: reverse sorting.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Sort field (starttime, endtime, duration are supported).
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""ASC: sequential sorting / desc: reverse sorting.
        :rtype: str
        """
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
        


class QueryMetricItem(AbstractModel):
    r"""Querying.

    """

    def __init__(self):
        r"""
        :param _MetricName: Metric name.
        :type MetricName: str
        :param _Compares: Year-Over-Year comparison is now supported for comparebyyesterday (compared to yesterday) and comparebylastweek (compared to last week). 
        :type Compares: list of str
        :param _Compare: Year-On-Year, deprecated, not recommended for use.
        :type Compare: str
        """
        self._MetricName = None
        self._Compares = None
        self._Compare = None

    @property
    def MetricName(self):
        r"""Metric name.
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Compares(self):
        r"""Year-Over-Year comparison is now supported for comparebyyesterday (compared to yesterday) and comparebylastweek (compared to last week). 
        :rtype: list of str
        """
        return self._Compares

    @Compares.setter
    def Compares(self, Compares):
        self._Compares = Compares

    @property
    def Compare(self):
        r"""Year-On-Year, deprecated, not recommended for use.
        :rtype: str
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Compares = params.get("Compares")
        self._Compare = params.get("Compare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceDetail(AbstractModel):
    r"""Detailed information about applications.

    """

    def __init__(self):
        r"""
        :param _ServiceID: Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceID: str
        :param _InstanceKey: Business system ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceKey: str
        :param _AppID: User appid.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppID: int
        :param _CreateUIN: Host account UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateUIN: str
        :param _ServiceName: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _ServiceDescription: Application description
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDescription: str
        :param _Region: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Tags: Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of ApmTag
        :param _InstanceName: Business system name.
        :type InstanceName: str
        """
        self._ServiceID = None
        self._InstanceKey = None
        self._AppID = None
        self._CreateUIN = None
        self._ServiceName = None
        self._ServiceDescription = None
        self._Region = None
        self._Tags = None
        self._InstanceName = None

    @property
    def ServiceID(self):
        r"""Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def InstanceKey(self):
        r"""Business system ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def AppID(self):
        r"""User appid.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CreateUIN(self):
        r"""Host account UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateUIN

    @CreateUIN.setter
    def CreateUIN(self, CreateUIN):
        self._CreateUIN = CreateUIN

    @property
    def ServiceName(self):
        r"""Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDescription(self):
        r"""Application description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def Region(self):
        r"""Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        r"""Business system name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._ServiceID = params.get("ServiceID")
        self._InstanceKey = params.get("InstanceKey")
        self._AppID = params.get("AppID")
        self._CreateUIN = params.get("CreateUIN")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDescription = params.get("ServiceDescription")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Span(AbstractModel):
    r"""Span object.

    """

    def __init__(self):
        r"""
        :param _TraceID: Trace ID
        :type TraceID: str
        :param _Logs: Log.
        :type Logs: list of SpanLog
        :param _Tags: Tag.
        :type Tags: list of SpanTag
        :param _Process: Submit application service information.
        :type Process: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        :param _Timestamp: Generated timestamp (ms).
        :type Timestamp: int
        :param _OperationName: Span name.
        :type OperationName: str
        :param _References: Association relationship.
        :type References: list of SpanReference
        :param _StartTime: Generated timestamp (ms).
        :type StartTime: int
        :param _Duration: Duration (ms).
        :type Duration: int
        :param _SpanID: Span ID
        :type SpanID: str
        :param _StartTimeMillis: Generated timestamp (ms).
        :type StartTimeMillis: int
        :param _ParentSpanID: Parent Span ID
        :type ParentSpanID: str
        """
        self._TraceID = None
        self._Logs = None
        self._Tags = None
        self._Process = None
        self._Timestamp = None
        self._OperationName = None
        self._References = None
        self._StartTime = None
        self._Duration = None
        self._SpanID = None
        self._StartTimeMillis = None
        self._ParentSpanID = None

    @property
    def TraceID(self):
        r"""Trace ID
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID

    @property
    def Logs(self):
        r"""Log.
        :rtype: list of SpanLog
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of SpanTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Process(self):
        r"""Submit application service information.
        :rtype: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        """
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def Timestamp(self):
        r"""Generated timestamp (ms).
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def OperationName(self):
        r"""Span name.
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def References(self):
        r"""Association relationship.
        :rtype: list of SpanReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def StartTime(self):
        r"""Generated timestamp (ms).
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        r"""Duration (ms).
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SpanID(self):
        r"""Span ID
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def StartTimeMillis(self):
        r"""Generated timestamp (ms).
        :rtype: int
        """
        return self._StartTimeMillis

    @StartTimeMillis.setter
    def StartTimeMillis(self, StartTimeMillis):
        self._StartTimeMillis = StartTimeMillis

    @property
    def ParentSpanID(self):
        r"""Parent Span ID
        :rtype: str
        """
        return self._ParentSpanID

    @ParentSpanID.setter
    def ParentSpanID(self, ParentSpanID):
        self._ParentSpanID = ParentSpanID


    def _deserialize(self, params):
        self._TraceID = params.get("TraceID")
        if params.get("Logs") is not None:
            self._Logs = []
            for item in params.get("Logs"):
                obj = SpanLog()
                obj._deserialize(item)
                self._Logs.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Process") is not None:
            self._Process = SpanProcess()
            self._Process._deserialize(params.get("Process"))
        self._Timestamp = params.get("Timestamp")
        self._OperationName = params.get("OperationName")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = SpanReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._SpanID = params.get("SpanID")
        self._StartTimeMillis = params.get("StartTimeMillis")
        self._ParentSpanID = params.get("ParentSpanID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanLog(AbstractModel):
    r"""Span log section.


    """

    def __init__(self):
        r"""
        :param _Timestamp: Log timestamp.
        :type Timestamp: int
        :param _Fields: Tag.
        :type Fields: list of SpanTag
        """
        self._Timestamp = None
        self._Fields = None

    @property
    def Timestamp(self):
        r"""Log timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Fields(self):
        r"""Tag.
        :rtype: list of SpanTag
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanProcess(AbstractModel):
    r"""Service information.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Application service name.
        :type ServiceName: str
        :param _Tags: Tags Tag array.
        :type Tags: list of SpanTag
        """
        self._ServiceName = None
        self._Tags = None

    @property
    def ServiceName(self):
        r"""Application service name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Tags(self):
        r"""Tags Tag array.
        :rtype: list of SpanTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanReference(AbstractModel):
    r"""Upstream and downstream relationships of span.

    """

    def __init__(self):
        r"""
        :param _RefType: Type of association relationship.
        :type RefType: str
        :param _SpanID: Span ID
        :type SpanID: str
        :param _TraceID: Trace ID
        :type TraceID: str
        """
        self._RefType = None
        self._SpanID = None
        self._TraceID = None

    @property
    def RefType(self):
        r"""Type of association relationship.
        :rtype: str
        """
        return self._RefType

    @RefType.setter
    def RefType(self, RefType):
        self._RefType = RefType

    @property
    def SpanID(self):
        r"""Span ID
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def TraceID(self):
        r"""Trace ID
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID


    def _deserialize(self, params):
        self._RefType = params.get("RefType")
        self._SpanID = params.get("SpanID")
        self._TraceID = params.get("TraceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanTag(AbstractModel):
    r"""Tag.

    """

    def __init__(self):
        r"""
        :param _Type: Tag type.
        :type Type: str
        :param _Key: Tag key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Tag value
.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        r"""Tag type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""Tag key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value
.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateApmInstanceRequest(AbstractModel):
    r"""TerminateApmInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system id.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Business system id.
        :rtype: str
        """
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
        


class TerminateApmInstanceResponse(AbstractModel):
    r"""TerminateApmInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")