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
        :param _InstanceKey: <p>Instance ID</p>
        :type InstanceKey: str
        :param _ServiceName: <p>Service name</p>
        :type ServiceName: str
        :param _UrlConvergenceSwitch: <p>URL convergence switch</p>
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: <p>URL convergence threshold</p>
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: <p>URL regular convergence</p>
        :type UrlConvergence: str
        :param _ExceptionFilter: <p>Exception filter regular</p>
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: <p>Error code filtering</p>
        :type ErrorCodeFilter: str
        :param _Components: <p>Service component type</p>
        :type Components: str
        :param _UrlExclude: <p>URL exclusion regular</p>
        :type UrlExclude: str
        :param _LogSource: <p>Log source</p>
        :type LogSource: str
        :param _LogRegion: <p>Log region</p>
        :type LogRegion: str
        :param _IsRelatedLog: <p>Whether logging is enabled 0 Disabled 1 Enabled</p>
        :type IsRelatedLog: int
        :param _LogTopicID: <p>Log topic ID</p>
        :type LogTopicID: str
        :param _IgnoreOperationName: <p>Interface Names to Filter</p>
        :type IgnoreOperationName: str
        :param _LogSet: <p>CLS logset | ES cluster ID</p>
        :type LogSet: str
        :param _TraceRateLimit: <p>Number of traces reported by the probe per second</p>
        :type TraceRateLimit: int
        :param _EnableSnapshot: <p>Whether thread profiling is enabled</p>
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: <p>Timeout threshold for thread profiling</p>
        :type SnapshotTimeout: int
        :param _AgentEnable: <p>Whether to enable agent</p>
        :type AgentEnable: bool
        :param _InstrumentList: <p>Component list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstrumentList: list of Instrument
        :param _TraceSquash: <p>Whether to enable link compression</p>
        :type TraceSquash: bool
        :param _EventEnable: <p>Whether the application diagnosis switch is enabled</p>
        :type EventEnable: bool
        :param _AgentOperationConfigView: <p>probe API related configuration</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: <p>Whether the application log configuration is enabled</p>
        :type EnableLogConfig: bool
        :param _ServiceID: <p>Application ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceID: str
        :param _EnableDashboardConfig: <p>Whether the dashboard configuration is enabled: false (disabled, consistent with the business system)/true (enabled, hierarchical configuration)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: <p>Whether dashboard is associated: 0 Disabled 1 Enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: <p>dashboard ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DashboardTopicID: str
        :param _EnableSecurityConfig: <p>Whether the application-level configuration is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableSecurityConfig: bool
        :param _IsInstrumentationVulnerabilityScan: <p>Whether the component vulnerability detection is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: <p>Whether SQL injection analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSqlInjectionAnalysis: int
        :param _IsRemoteCommandExecutionAnalysis: <p>Whether remote command execution analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: <p>Whether Java Webshell detection and analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: <p>CLS index type (0=full-text index, 1=key-value index)</p>
        :type LogIndexType: int
        :param _LogTraceIdKey: <p>Index key of traceId: This parameter is valid only when the CLS index type is key-value index.</p>
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: <p>Whether to enable file deletion detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: <p>Whether to enable arbitrary file read detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: <p>Whether to enable arbitrary file upload detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: <p>Whether to enable detection of arbitrary files (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: <p>Whether path traversal detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: <p>Whether to enable template engine injection detection (0-disable, 1-enable)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: <p>Whether script engine injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: <p>Whether expression injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: <p>Whether JNDI injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: <p>Whether JNI injection detection is enabled (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: <p>Whether to enable Webshell backdoor detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: <p>Whether deserialization detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: <p>API name auto convergence switch (0-off, 1-on)</p>
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: <p>URL long segment convergence threshold</p>
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: <p>URL digit segment convergence threshold</p>
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: <p>Fuse memory threshold of the probe</p>
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: <p>Probe fuse CPU threshold</p>
        :type DisableCpuUsed: int
        :param _DbStatementParametersEnabled: <p>Whether SQL parameter access is enabled</p>
        :type DbStatementParametersEnabled: bool
        :param _SlowSQLThresholds: <p>Slow SQL threshold</p>
        :type SlowSQLThresholds: list of ApmTag
        :param _EnableDesensitizationRule: <p>Whether the masking rule is enabled</p>
        :type EnableDesensitizationRule: int
        :param _DesensitizationRule: <p>Masking rule</p>
        :type DesensitizationRule: str
        :param _LogSpanIdKey: <p>Index key of spanId: This parameter is valid only when the CLS index type is key-value index.</p>
        :type LogSpanIdKey: str
        :param _AutoProfilingConfig: <p>Automated performance analysis configuration</p>
        :type AutoProfilingConfig: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        :param _EnableThresholdConfig: <p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
        :type EnableThresholdConfig: bool
        :param _ErrRateThreshold: <p>Error rate threshold (%) used to judge the application health status as "red".</p>
        :type ErrRateThreshold: int
        :param _ResponseDurationWarningThreshold: <p>Alert threshold for response time (ms), used to judge the application health status as "yellow".</p>
        :type ResponseDurationWarningThreshold: int
        :param _UseDefaultFuseConfig: <p>Whether to use the built-in fuse threshold of the probe by default</p>
        :type UseDefaultFuseConfig: bool
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
        self._DbStatementParametersEnabled = None
        self._SlowSQLThresholds = None
        self._EnableDesensitizationRule = None
        self._DesensitizationRule = None
        self._LogSpanIdKey = None
        self._AutoProfilingConfig = None
        self._EnableThresholdConfig = None
        self._ErrRateThreshold = None
        self._ResponseDurationWarningThreshold = None
        self._UseDefaultFuseConfig = None

    @property
    def InstanceKey(self):
        r"""<p>Instance ID</p>
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""<p>Service name</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""<p>URL convergence switch</p>
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""<p>URL convergence threshold</p>
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""<p>URL regular convergence</p>
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ExceptionFilter(self):
        r"""<p>Exception filter regular</p>
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""<p>Error code filtering</p>
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def Components(self):
        r"""<p>Service component type</p>
        :rtype: str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def UrlExclude(self):
        r"""<p>URL exclusion regular</p>
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def LogSource(self):
        r"""<p>Log source</p>
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogRegion(self):
        r"""<p>Log region</p>
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def IsRelatedLog(self):
        r"""<p>Whether logging is enabled 0 Disabled 1 Enabled</p>
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        r"""<p>Log topic ID</p>
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def IgnoreOperationName(self):
        r"""<p>Interface Names to Filter</p>
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def LogSet(self):
        r"""<p>CLS logset | ES cluster ID</p>
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def TraceRateLimit(self):
        r"""<p>Number of traces reported by the probe per second</p>
        :rtype: int
        """
        return self._TraceRateLimit

    @TraceRateLimit.setter
    def TraceRateLimit(self, TraceRateLimit):
        self._TraceRateLimit = TraceRateLimit

    @property
    def EnableSnapshot(self):
        r"""<p>Whether thread profiling is enabled</p>
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""<p>Timeout threshold for thread profiling</p>
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""<p>Whether to enable agent</p>
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""<p>Component list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""<p>Whether to enable link compression</p>
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""<p>Whether the application diagnosis switch is enabled</p>
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def AgentOperationConfigView(self):
        r"""<p>probe API related configuration</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""<p>Whether the application log configuration is enabled</p>
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def ServiceID(self):
        r"""<p>Application ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def EnableDashboardConfig(self):
        r"""<p>Whether the dashboard configuration is enabled: false (disabled, consistent with the business system)/true (enabled, hierarchical configuration)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""<p>Whether dashboard is associated: 0 Disabled 1 Enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""<p>dashboard ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def EnableSecurityConfig(self):
        r"""<p>Whether the application-level configuration is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""<p>Whether the component vulnerability detection is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        r"""<p>Whether SQL injection analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""<p>Whether remote command execution analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""<p>Whether Java Webshell detection and analysis is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""<p>CLS index type (0=full-text index, 1=key-value index)</p>
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""<p>Index key of traceId: This parameter is valid only when the CLS index type is key-value index.</p>
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""<p>Whether to enable file deletion detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file read detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file upload detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""<p>Whether to enable detection of arbitrary files (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""<p>Whether path traversal detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""<p>Whether to enable template engine injection detection (0-disable, 1-enable)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""<p>Whether script engine injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""<p>Whether expression injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""<p>Whether JNDI injection detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""<p>Whether JNI injection detection is enabled (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""<p>Whether to enable Webshell backdoor detection (0 - disabled, 1 - enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""<p>Whether deserialization detection is enabled (0-disabled, 1-enabled)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""<p>API name auto convergence switch (0-off, 1-on)</p>
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""<p>URL long segment convergence threshold</p>
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""<p>URL digit segment convergence threshold</p>
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""<p>Fuse memory threshold of the probe</p>
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""<p>Probe fuse CPU threshold</p>
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed

    @property
    def DbStatementParametersEnabled(self):
        r"""<p>Whether SQL parameter access is enabled</p>
        :rtype: bool
        """
        return self._DbStatementParametersEnabled

    @DbStatementParametersEnabled.setter
    def DbStatementParametersEnabled(self, DbStatementParametersEnabled):
        self._DbStatementParametersEnabled = DbStatementParametersEnabled

    @property
    def SlowSQLThresholds(self):
        r"""<p>Slow SQL threshold</p>
        :rtype: list of ApmTag
        """
        return self._SlowSQLThresholds

    @SlowSQLThresholds.setter
    def SlowSQLThresholds(self, SlowSQLThresholds):
        self._SlowSQLThresholds = SlowSQLThresholds

    @property
    def EnableDesensitizationRule(self):
        r"""<p>Whether the masking rule is enabled</p>
        :rtype: int
        """
        return self._EnableDesensitizationRule

    @EnableDesensitizationRule.setter
    def EnableDesensitizationRule(self, EnableDesensitizationRule):
        self._EnableDesensitizationRule = EnableDesensitizationRule

    @property
    def DesensitizationRule(self):
        r"""<p>Masking rule</p>
        :rtype: str
        """
        return self._DesensitizationRule

    @DesensitizationRule.setter
    def DesensitizationRule(self, DesensitizationRule):
        self._DesensitizationRule = DesensitizationRule

    @property
    def LogSpanIdKey(self):
        r"""<p>Index key of spanId: This parameter is valid only when the CLS index type is key-value index.</p>
        :rtype: str
        """
        return self._LogSpanIdKey

    @LogSpanIdKey.setter
    def LogSpanIdKey(self, LogSpanIdKey):
        self._LogSpanIdKey = LogSpanIdKey

    @property
    def AutoProfilingConfig(self):
        r"""<p>Automated performance analysis configuration</p>
        :rtype: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        """
        return self._AutoProfilingConfig

    @AutoProfilingConfig.setter
    def AutoProfilingConfig(self, AutoProfilingConfig):
        self._AutoProfilingConfig = AutoProfilingConfig

    @property
    def EnableThresholdConfig(self):
        r"""<p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
        :rtype: bool
        """
        return self._EnableThresholdConfig

    @EnableThresholdConfig.setter
    def EnableThresholdConfig(self, EnableThresholdConfig):
        self._EnableThresholdConfig = EnableThresholdConfig

    @property
    def ErrRateThreshold(self):
        r"""<p>Error rate threshold (%) used to judge the application health status as "red".</p>
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def ResponseDurationWarningThreshold(self):
        r"""<p>Alert threshold for response time (ms), used to judge the application health status as "yellow".</p>
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def UseDefaultFuseConfig(self):
        r"""<p>Whether to use the built-in fuse threshold of the probe by default</p>
        :rtype: bool
        """
        return self._UseDefaultFuseConfig

    @UseDefaultFuseConfig.setter
    def UseDefaultFuseConfig(self, UseDefaultFuseConfig):
        self._UseDefaultFuseConfig = UseDefaultFuseConfig


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
        self._DbStatementParametersEnabled = params.get("DbStatementParametersEnabled")
        if params.get("SlowSQLThresholds") is not None:
            self._SlowSQLThresholds = []
            for item in params.get("SlowSQLThresholds"):
                obj = ApmTag()
                obj._deserialize(item)
                self._SlowSQLThresholds.append(obj)
        self._EnableDesensitizationRule = params.get("EnableDesensitizationRule")
        self._DesensitizationRule = params.get("DesensitizationRule")
        self._LogSpanIdKey = params.get("LogSpanIdKey")
        if params.get("AutoProfilingConfig") is not None:
            self._AutoProfilingConfig = AutoProfilingConfig()
            self._AutoProfilingConfig._deserialize(params.get("AutoProfilingConfig"))
        self._EnableThresholdConfig = params.get("EnableThresholdConfig")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._UseDefaultFuseConfig = params.get("UseDefaultFuseConfig")
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
        :param _InstanceKey: <p>Business system ID</p>
        :type InstanceKey: str
        :param _ServiceName: <p>Application name</p>
        :type ServiceName: str
        :param _OperationNameFilter: <p>Interface Filtering</p>
        :type OperationNameFilter: str
        :param _ExceptionFilter: <p>Error type filtering</p>
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: <p>HTTP status code filtering</p>
        :type ErrorCodeFilter: str
        :param _EventEnable: <p>Application diagnosis switch (abandoned)</p>
        :type EventEnable: bool
        :param _UrlConvergenceSwitch: <p>URL convergence switch 0 Off 1 On</p>
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: <p>URL convergence threshold</p>
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: <p>URL regular convergence rules</p>
        :type UrlConvergence: str
        :param _UrlExclude: <p>URL exclusion rule regex</p>
        :type UrlExclude: str
        :param _IsRelatedLog: <p>Whether logging is enabled 0 Disabled 1 Enabled</p>
        :type IsRelatedLog: int
        :param _LogSource: <p>Log source</p>
        :type LogSource: str
        :param _LogSet: <p>Logset</p>
        :type LogSet: str
        :param _LogTopicID: <p>Log topic</p>
        :type LogTopicID: str
        :param _SnapshotEnable: <p>Method stack snapshot switch. Enabled indicates true. false indicates disabled.</p>
        :type SnapshotEnable: bool
        :param _SnapshotTimeout: <p>Slow call monitoring trigger threshold</p>
        :type SnapshotTimeout: int
        :param _AgentEnable: <p>Master switch for probes</p>
        :type AgentEnable: bool
        :param _InstrumentList: <p>Component list toggle (abandoned)</p>
        :type InstrumentList: list of Instrument
        :param _TraceSquash: <p>Link compression switch (abandoned)</p>
        :type TraceSquash: bool
        :param _AgentIgnoreOperation: <p>Link filtering configuration</p>
        :type AgentIgnoreOperation: str
        :param _EnableSecurityConfig: <p>Enable the application security switch</p>
        :type EnableSecurityConfig: bool
        :param _IsSqlInjectionAnalysis: <p>Whether SQL injection detection is enabled</p>
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: <p>Whether component vulnerability detection is enabled</p>
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: <p>Whether remote command execution detection is enabled</p>
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: <p>Whether memory leakage detection is enabled</p>
        :type IsMemoryHijackingAnalysis: int
        :param _IsDeleteAnyFileAnalysis: <p>Whether to enable detection of any file deletion</p>
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: <p>Whether to enable arbitrary file read detection</p>
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: <p>Whether to enable arbitrary file upload detection</p>
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: <p>Whether to enable detection of arbitrary files</p>
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: <p>Whether path traversal detection is enabled</p>
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: <p>Whether to enable template engine injection detection</p>
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: <p>Whether script engine injection detection is enabled</p>
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: <p>Whether expression injection detection is enabled</p>
        :type IsExpressionInjectionAnalysis: int
        :param _IsJndiInjectionAnalysis: <p>Whether JNDI injection detection is enabled</p>
        :type IsJndiInjectionAnalysis: int
        :param _IsJniInjectionAnalysis: <p>Whether JNI injection detection is enabled</p>
        :type IsJniInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: <p>Whether Webshell backdoor detection is enabled</p>
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: <p>Whether deserialization detection is enabled</p>
        :type IsDeserializationAnalysis: int
        :param _EnableDashboardConfig: <p>Whether the console switch is enabled</p>
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: <p>Whether to associate with Dashboard</p>
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: <p>Dashboard topic</p>
        :type DashboardTopicID: str
        :param _DisableMemoryUsed: <p>Fuse memory threshold of the probe</p>
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: <p>Probe fuse CPU threshold</p>
        :type DisableCpuUsed: int
        :param _DbStatementParametersEnabled: <p>Whether SQL parameter access is enabled</p>
        :type DbStatementParametersEnabled: bool
        :param _SlowSQLThresholds: <p>Slow SQL threshold</p>
        :type SlowSQLThresholds: list of ApmTag
        :param _EnableDesensitizationRule: <p>Whether the masking rule is enabled</p>
        :type EnableDesensitizationRule: int
        :param _DesensitizationRule: <p>Masking rule</p>
        :type DesensitizationRule: str
        :param _AutoProfilingConfig: <p>Automated performance analysis task configuration</p>
        :type AutoProfilingConfig: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        :param _EnableThresholdConfig: <p>Threshold configuration switch</p>
        :type EnableThresholdConfig: bool
        :param _ErrRateThreshold: <p>Error rate threshold</p><p>Unit: %</p>
        :type ErrRateThreshold: int
        :param _ResponseDurationWarningThreshold: <p>Alert threshold of response time</p><p>Unit: ms</p>
        :type ResponseDurationWarningThreshold: int
        :param _UseDefaultFuseConfig: <p>Whether to use the default fuse threshold of the probe</p>
        :type UseDefaultFuseConfig: bool
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
        self._AgentIgnoreOperation = None
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
        self._IsJndiInjectionAnalysis = None
        self._IsJniInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._EnableDashboardConfig = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None
        self._DbStatementParametersEnabled = None
        self._SlowSQLThresholds = None
        self._EnableDesensitizationRule = None
        self._DesensitizationRule = None
        self._AutoProfilingConfig = None
        self._EnableThresholdConfig = None
        self._ErrRateThreshold = None
        self._ResponseDurationWarningThreshold = None
        self._UseDefaultFuseConfig = None

    @property
    def InstanceKey(self):
        r"""<p>Business system ID</p>
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""<p>Application name</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationNameFilter(self):
        r"""<p>Interface Filtering</p>
        :rtype: str
        """
        return self._OperationNameFilter

    @OperationNameFilter.setter
    def OperationNameFilter(self, OperationNameFilter):
        self._OperationNameFilter = OperationNameFilter

    @property
    def ExceptionFilter(self):
        r"""<p>Error type filtering</p>
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""<p>HTTP status code filtering</p>
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def EventEnable(self):
        r"""<p>Application diagnosis switch (abandoned)</p>
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def UrlConvergenceSwitch(self):
        r"""<p>URL convergence switch 0 Off 1 On</p>
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""<p>URL convergence threshold</p>
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""<p>URL regular convergence rules</p>
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def UrlExclude(self):
        r"""<p>URL exclusion rule regex</p>
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""<p>Whether logging is enabled 0 Disabled 1 Enabled</p>
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogSource(self):
        r"""<p>Log source</p>
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogSet(self):
        r"""<p>Logset</p>
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogTopicID(self):
        r"""<p>Log topic</p>
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def SnapshotEnable(self):
        r"""<p>Method stack snapshot switch. Enabled indicates true. false indicates disabled.</p>
        :rtype: bool
        """
        return self._SnapshotEnable

    @SnapshotEnable.setter
    def SnapshotEnable(self, SnapshotEnable):
        self._SnapshotEnable = SnapshotEnable

    @property
    def SnapshotTimeout(self):
        r"""<p>Slow call monitoring trigger threshold</p>
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""<p>Master switch for probes</p>
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""<p>Component list toggle (abandoned)</p>
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""<p>Link compression switch (abandoned)</p>
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def AgentIgnoreOperation(self):
        r"""<p>Link filtering configuration</p>
        :rtype: str
        """
        return self._AgentIgnoreOperation

    @AgentIgnoreOperation.setter
    def AgentIgnoreOperation(self, AgentIgnoreOperation):
        self._AgentIgnoreOperation = AgentIgnoreOperation

    @property
    def EnableSecurityConfig(self):
        r"""<p>Enable the application security switch</p>
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsSqlInjectionAnalysis(self):
        r"""<p>Whether SQL injection detection is enabled</p>
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""<p>Whether component vulnerability detection is enabled</p>
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""<p>Whether remote command execution detection is enabled</p>
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""<p>Whether memory leakage detection is enabled</p>
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""<p>Whether to enable detection of any file deletion</p>
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file read detection</p>
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file upload detection</p>
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""<p>Whether to enable detection of arbitrary files</p>
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""<p>Whether path traversal detection is enabled</p>
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""<p>Whether to enable template engine injection detection</p>
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""<p>Whether script engine injection detection is enabled</p>
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""<p>Whether expression injection detection is enabled</p>
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJndiInjectionAnalysis(self):
        r"""<p>Whether JNDI injection detection is enabled</p>
        :rtype: int
        """
        return self._IsJndiInjectionAnalysis

    @IsJndiInjectionAnalysis.setter
    def IsJndiInjectionAnalysis(self, IsJndiInjectionAnalysis):
        self._IsJndiInjectionAnalysis = IsJndiInjectionAnalysis

    @property
    def IsJniInjectionAnalysis(self):
        r"""<p>Whether JNI injection detection is enabled</p>
        :rtype: int
        """
        return self._IsJniInjectionAnalysis

    @IsJniInjectionAnalysis.setter
    def IsJniInjectionAnalysis(self, IsJniInjectionAnalysis):
        self._IsJniInjectionAnalysis = IsJniInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""<p>Whether Webshell backdoor detection is enabled</p>
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""<p>Whether deserialization detection is enabled</p>
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def EnableDashboardConfig(self):
        r"""<p>Whether the console switch is enabled</p>
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""<p>Whether to associate with Dashboard</p>
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""<p>Dashboard topic</p>
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def DisableMemoryUsed(self):
        r"""<p>Fuse memory threshold of the probe</p>
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""<p>Probe fuse CPU threshold</p>
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed

    @property
    def DbStatementParametersEnabled(self):
        r"""<p>Whether SQL parameter access is enabled</p>
        :rtype: bool
        """
        return self._DbStatementParametersEnabled

    @DbStatementParametersEnabled.setter
    def DbStatementParametersEnabled(self, DbStatementParametersEnabled):
        self._DbStatementParametersEnabled = DbStatementParametersEnabled

    @property
    def SlowSQLThresholds(self):
        r"""<p>Slow SQL threshold</p>
        :rtype: list of ApmTag
        """
        return self._SlowSQLThresholds

    @SlowSQLThresholds.setter
    def SlowSQLThresholds(self, SlowSQLThresholds):
        self._SlowSQLThresholds = SlowSQLThresholds

    @property
    def EnableDesensitizationRule(self):
        r"""<p>Whether the masking rule is enabled</p>
        :rtype: int
        """
        return self._EnableDesensitizationRule

    @EnableDesensitizationRule.setter
    def EnableDesensitizationRule(self, EnableDesensitizationRule):
        self._EnableDesensitizationRule = EnableDesensitizationRule

    @property
    def DesensitizationRule(self):
        r"""<p>Masking rule</p>
        :rtype: str
        """
        return self._DesensitizationRule

    @DesensitizationRule.setter
    def DesensitizationRule(self, DesensitizationRule):
        self._DesensitizationRule = DesensitizationRule

    @property
    def AutoProfilingConfig(self):
        r"""<p>Automated performance analysis task configuration</p>
        :rtype: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        """
        return self._AutoProfilingConfig

    @AutoProfilingConfig.setter
    def AutoProfilingConfig(self, AutoProfilingConfig):
        self._AutoProfilingConfig = AutoProfilingConfig

    @property
    def EnableThresholdConfig(self):
        r"""<p>Threshold configuration switch</p>
        :rtype: bool
        """
        return self._EnableThresholdConfig

    @EnableThresholdConfig.setter
    def EnableThresholdConfig(self, EnableThresholdConfig):
        self._EnableThresholdConfig = EnableThresholdConfig

    @property
    def ErrRateThreshold(self):
        r"""<p>Error rate threshold</p><p>Unit: %</p>
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def ResponseDurationWarningThreshold(self):
        r"""<p>Alert threshold of response time</p><p>Unit: ms</p>
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def UseDefaultFuseConfig(self):
        r"""<p>Whether to use the default fuse threshold of the probe</p>
        :rtype: bool
        """
        return self._UseDefaultFuseConfig

    @UseDefaultFuseConfig.setter
    def UseDefaultFuseConfig(self, UseDefaultFuseConfig):
        self._UseDefaultFuseConfig = UseDefaultFuseConfig


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
        self._AgentIgnoreOperation = params.get("AgentIgnoreOperation")
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
        self._IsJndiInjectionAnalysis = params.get("IsJndiInjectionAnalysis")
        self._IsJniInjectionAnalysis = params.get("IsJniInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._EnableDashboardConfig = params.get("EnableDashboardConfig")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        self._DbStatementParametersEnabled = params.get("DbStatementParametersEnabled")
        if params.get("SlowSQLThresholds") is not None:
            self._SlowSQLThresholds = []
            for item in params.get("SlowSQLThresholds"):
                obj = ApmTag()
                obj._deserialize(item)
                self._SlowSQLThresholds.append(obj)
        self._EnableDesensitizationRule = params.get("EnableDesensitizationRule")
        self._DesensitizationRule = params.get("DesensitizationRule")
        if params.get("AutoProfilingConfig") is not None:
            self._AutoProfilingConfig = AutoProfilingConfig()
            self._AutoProfilingConfig._deserialize(params.get("AutoProfilingConfig"))
        self._EnableThresholdConfig = params.get("EnableThresholdConfig")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._UseDefaultFuseConfig = params.get("UseDefaultFuseConfig")
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
        :param _PeerId: <p>Instance ID of the associated product</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        :param _Status: <p>Association status: 1 (enabled), 2 (not enabled), 3 (invalid)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Topic: <p>CKafka message topic</p>
        :type Topic: str
        :param _MetricTopic: <p>Ckafka consumption topic</p><p>Used for Kafka metric delivery</p>
        :type MetricTopic: str
        """
        self._PeerId = None
        self._Status = None
        self._Topic = None
        self._MetricTopic = None

    @property
    def PeerId(self):
        r"""<p>Instance ID of the associated product</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Status(self):
        r"""<p>Association status: 1 (enabled), 2 (not enabled), 3 (invalid)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Topic(self):
        r"""<p>CKafka message topic</p>
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def MetricTopic(self):
        r"""<p>Ckafka consumption topic</p><p>Used for Kafka metric delivery</p>
        :rtype: str
        """
        return self._MetricTopic

    @MetricTopic.setter
    def MetricTopic(self, MetricTopic):
        self._MetricTopic = MetricTopic


    def _deserialize(self, params):
        self._PeerId = params.get("PeerId")
        self._Status = params.get("Status")
        self._Topic = params.get("Topic")
        self._MetricTopic = params.get("MetricTopic")
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
        :param _LogSpanIdKey: Index key of spanId: This parameter is valid only when the CLS index type is key-value index
        :type LogSpanIdKey: str
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
        self._LogSpanIdKey = None

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

    @property
    def LogSpanIdKey(self):
        r"""Index key of spanId: This parameter is valid only when the CLS index type is key-value index
        :rtype: str
        """
        return self._LogSpanIdKey

    @LogSpanIdKey.setter
    def LogSpanIdKey(self, LogSpanIdKey):
        self._LogSpanIdKey = LogSpanIdKey


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
        self._LogSpanIdKey = params.get("LogSpanIdKey")
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
        


class ApmVulnerabilityServiceDetail(AbstractModel):
    r"""Vulnerability-related information of APM application instance

    """

    def __init__(self):
        r"""
        :param _ServiceInstance: Application instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceInstance: str
        :param _Path: Path of the jar package with the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _LastOccurTime: Last occurrence time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastOccurTime: int
        """
        self._ServiceInstance = None
        self._Path = None
        self._LastOccurTime = None

    @property
    def ServiceInstance(self):
        r"""Application instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceInstance

    @ServiceInstance.setter
    def ServiceInstance(self, ServiceInstance):
        self._ServiceInstance = ServiceInstance

    @property
    def Path(self):
        r"""Path of the jar package with the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def LastOccurTime(self):
        r"""Last occurrence time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LastOccurTime

    @LastOccurTime.setter
    def LastOccurTime(self, LastOccurTime):
        self._LastOccurTime = LastOccurTime


    def _deserialize(self, params):
        self._ServiceInstance = params.get("ServiceInstance")
        self._Path = params.get("Path")
        self._LastOccurTime = params.get("LastOccurTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoProfilingConfig(AbstractModel):
    r"""Automated performance analysis configuration

    """

    def __init__(self):
        r"""
        :param _CpuProfilingEnable: Auto CPU profiling task switch
        :type CpuProfilingEnable: bool
        :param _MemoryProfilingEnable: Auto memory profiling task switch
        :type MemoryProfilingEnable: bool
        :param _CpuProfilingThreshold: Auto CPU profiling task threshold
        :type CpuProfilingThreshold: int
        :param _MemoryProfilingThreshold: Automated memory profiling task threshold
        :type MemoryProfilingThreshold: int
        :param _CpuProfilingDuration: CPU auto profiling task duration
        :type CpuProfilingDuration: int
        :param _MemoryProfilingDuration: Memory auto profiling task duration
        :type MemoryProfilingDuration: int
        """
        self._CpuProfilingEnable = None
        self._MemoryProfilingEnable = None
        self._CpuProfilingThreshold = None
        self._MemoryProfilingThreshold = None
        self._CpuProfilingDuration = None
        self._MemoryProfilingDuration = None

    @property
    def CpuProfilingEnable(self):
        r"""Auto CPU profiling task switch
        :rtype: bool
        """
        return self._CpuProfilingEnable

    @CpuProfilingEnable.setter
    def CpuProfilingEnable(self, CpuProfilingEnable):
        self._CpuProfilingEnable = CpuProfilingEnable

    @property
    def MemoryProfilingEnable(self):
        r"""Auto memory profiling task switch
        :rtype: bool
        """
        return self._MemoryProfilingEnable

    @MemoryProfilingEnable.setter
    def MemoryProfilingEnable(self, MemoryProfilingEnable):
        self._MemoryProfilingEnable = MemoryProfilingEnable

    @property
    def CpuProfilingThreshold(self):
        r"""Auto CPU profiling task threshold
        :rtype: int
        """
        return self._CpuProfilingThreshold

    @CpuProfilingThreshold.setter
    def CpuProfilingThreshold(self, CpuProfilingThreshold):
        self._CpuProfilingThreshold = CpuProfilingThreshold

    @property
    def MemoryProfilingThreshold(self):
        r"""Automated memory profiling task threshold
        :rtype: int
        """
        return self._MemoryProfilingThreshold

    @MemoryProfilingThreshold.setter
    def MemoryProfilingThreshold(self, MemoryProfilingThreshold):
        self._MemoryProfilingThreshold = MemoryProfilingThreshold

    @property
    def CpuProfilingDuration(self):
        r"""CPU auto profiling task duration
        :rtype: int
        """
        return self._CpuProfilingDuration

    @CpuProfilingDuration.setter
    def CpuProfilingDuration(self, CpuProfilingDuration):
        self._CpuProfilingDuration = CpuProfilingDuration

    @property
    def MemoryProfilingDuration(self):
        r"""Memory auto profiling task duration
        :rtype: int
        """
        return self._MemoryProfilingDuration

    @MemoryProfilingDuration.setter
    def MemoryProfilingDuration(self, MemoryProfilingDuration):
        self._MemoryProfilingDuration = MemoryProfilingDuration


    def _deserialize(self, params):
        self._CpuProfilingEnable = params.get("CpuProfilingEnable")
        self._MemoryProfilingEnable = params.get("MemoryProfilingEnable")
        self._CpuProfilingThreshold = params.get("CpuProfilingThreshold")
        self._MemoryProfilingThreshold = params.get("MemoryProfilingThreshold")
        self._CpuProfilingDuration = params.get("CpuProfilingDuration")
        self._MemoryProfilingDuration = params.get("MemoryProfilingDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMMeta(AbstractModel):
    r"""CVM metadata.

    """

    def __init__(self):
        r"""
        :param _Region: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _InstanceID: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceID: str
        """
        self._Region = None
        self._InstanceID = None

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
    def InstanceID(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentTopologyView(AbstractModel):
    r"""Contains the quantity of node component types in the view.

    """

    def __init__(self):
        r"""
        :param _Service: Number of nodes at the service level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Service: int
        :param _Database: Node count of the database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: int
        :param _MQ: Node count of the message queue.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MQ: int
        """
        self._Service = None
        self._Database = None
        self._MQ = None

    @property
    def Service(self):
        r"""Number of nodes at the service level.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Database(self):
        r"""Node count of the database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def MQ(self):
        r"""Node count of the message queue.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MQ

    @MQ.setter
    def MQ(self, MQ):
        self._MQ = MQ


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Database = params.get("Database")
        self._MQ = params.get("MQ")
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
        :param _RuleId: ID of the metric match rule
        :type RuleId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        r"""ID of the metric match rule
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
        self._RuleId = params.get("RuleId")
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


class DescribeApmAllVulCountRequest(AbstractModel):
    r"""DescribeApmAllVulCount request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: unix second-level timestamp
        :type StartTime: int
        :param _EndTime: unix second-level timestamp
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAllVulCountResponse(AbstractModel):
    r"""DescribeApmAllVulCount response structure.

    """

    def __init__(self):
        r"""
        :param _VulnerabilityList: Vulnerability metrics as well as number of business systems	
        :type VulnerabilityList: list of ApmMetricRecord
        :param _VulnerabilityCount: Total number of vulnerabilities
        :type VulnerabilityCount: int
        :param _ImportantVulnerabilityCount: Number of critical vulnerabilities
        :type ImportantVulnerabilityCount: int
        :param _CriticalVulnerabilityCount: High-risk vulnerability count
        :type CriticalVulnerabilityCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VulnerabilityList = None
        self._VulnerabilityCount = None
        self._ImportantVulnerabilityCount = None
        self._CriticalVulnerabilityCount = None
        self._RequestId = None

    @property
    def VulnerabilityList(self):
        r"""Vulnerability metrics as well as number of business systems	
        :rtype: list of ApmMetricRecord
        """
        return self._VulnerabilityList

    @VulnerabilityList.setter
    def VulnerabilityList(self, VulnerabilityList):
        self._VulnerabilityList = VulnerabilityList

    @property
    def VulnerabilityCount(self):
        r"""Total number of vulnerabilities
        :rtype: int
        """
        return self._VulnerabilityCount

    @VulnerabilityCount.setter
    def VulnerabilityCount(self, VulnerabilityCount):
        self._VulnerabilityCount = VulnerabilityCount

    @property
    def ImportantVulnerabilityCount(self):
        r"""Number of critical vulnerabilities
        :rtype: int
        """
        return self._ImportantVulnerabilityCount

    @ImportantVulnerabilityCount.setter
    def ImportantVulnerabilityCount(self, ImportantVulnerabilityCount):
        self._ImportantVulnerabilityCount = ImportantVulnerabilityCount

    @property
    def CriticalVulnerabilityCount(self):
        r"""High-risk vulnerability count
        :rtype: int
        """
        return self._CriticalVulnerabilityCount

    @CriticalVulnerabilityCount.setter
    def CriticalVulnerabilityCount(self, CriticalVulnerabilityCount):
        self._CriticalVulnerabilityCount = CriticalVulnerabilityCount

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
        if params.get("VulnerabilityList") is not None:
            self._VulnerabilityList = []
            for item in params.get("VulnerabilityList"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._VulnerabilityList.append(obj)
        self._VulnerabilityCount = params.get("VulnerabilityCount")
        self._ImportantVulnerabilityCount = params.get("ImportantVulnerabilityCount")
        self._CriticalVulnerabilityCount = params.get("CriticalVulnerabilityCount")
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


class DescribeApmSQLInjectionDetailRequest(AbstractModel):
    r"""DescribeApmSQLInjectionDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _Limit: Limit
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _StartTime: unix second-level timestamp
        :type StartTime: int
        :param _EndTime: unix second-level timestamp
        :type EndTime: int
        :param _OrderBy: Order.
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _Filters: Query filter criteria.
        :type Filters: list of Filter
        :param _GroupBy: Aggregation dimension
        :type GroupBy: list of str
        :param _Metrics: Metric list
        :type Metrics: list of QueryMetricItem
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._OrderBy = None
        self._Filters = None
        self._GroupBy = None
        self._Metrics = None

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
    def Limit(self):
        r"""Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""unix second-level timestamp
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
    def Filters(self):
        r"""Query filter criteria.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        r"""Aggregation dimension
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Metrics(self):
        r"""Metric list
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._GroupBy = params.get("GroupBy")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmSQLInjectionDetailResponse(AbstractModel):
    r"""DescribeApmSQLInjectionDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Tags: SQL dimension information
        :type Tags: list of ApmTag
        :param _Records: Link information
        :type Records: list of ApmMetricRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tags = None
        self._Records = None
        self._RequestId = None

    @property
    def Tags(self):
        r"""SQL dimension information
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Records(self):
        r"""Link information
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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
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


class DescribeApmVulnerabilityCountRequest(AbstractModel):
    r"""DescribeApmVulnerabilityCount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: APM business system ID
        :type InstanceId: str
        :param _ServiceName: app name
        :type ServiceName: str
        :param _StartTime: unix second-level timestamp
        :type StartTime: int
        :param _EndTime: unix second-level timestamp
        :type EndTime: int
        :param _Type: Data type of queried data. Attack detection is "attack_detect".
        :type Type: str
        """
        self._InstanceId = None
        self._ServiceName = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None

    @property
    def InstanceId(self):
        r"""APM business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""app name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def StartTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""Data type of queried data. Attack detection is "attack_detect".
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmVulnerabilityCountResponse(AbstractModel):
    r"""DescribeApmVulnerabilityCount response structure.

    """

    def __init__(self):
        r"""
        :param _VulnerabilityList: Vulnerability metrics as well as number of business systems
        :type VulnerabilityList: list of ApmMetricRecord
        :param _VulnerabilityCount: Total number of vulnerabilities
        :type VulnerabilityCount: int
        :param _ImportantVulnerabilityCount: Number of critical vulnerabilities
        :type ImportantVulnerabilityCount: int
        :param _CriticalVulnerabilityCount: High-risk vulnerability count
        :type CriticalVulnerabilityCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VulnerabilityList = None
        self._VulnerabilityCount = None
        self._ImportantVulnerabilityCount = None
        self._CriticalVulnerabilityCount = None
        self._RequestId = None

    @property
    def VulnerabilityList(self):
        r"""Vulnerability metrics as well as number of business systems
        :rtype: list of ApmMetricRecord
        """
        return self._VulnerabilityList

    @VulnerabilityList.setter
    def VulnerabilityList(self, VulnerabilityList):
        self._VulnerabilityList = VulnerabilityList

    @property
    def VulnerabilityCount(self):
        r"""Total number of vulnerabilities
        :rtype: int
        """
        return self._VulnerabilityCount

    @VulnerabilityCount.setter
    def VulnerabilityCount(self, VulnerabilityCount):
        self._VulnerabilityCount = VulnerabilityCount

    @property
    def ImportantVulnerabilityCount(self):
        r"""Number of critical vulnerabilities
        :rtype: int
        """
        return self._ImportantVulnerabilityCount

    @ImportantVulnerabilityCount.setter
    def ImportantVulnerabilityCount(self, ImportantVulnerabilityCount):
        self._ImportantVulnerabilityCount = ImportantVulnerabilityCount

    @property
    def CriticalVulnerabilityCount(self):
        r"""High-risk vulnerability count
        :rtype: int
        """
        return self._CriticalVulnerabilityCount

    @CriticalVulnerabilityCount.setter
    def CriticalVulnerabilityCount(self, CriticalVulnerabilityCount):
        self._CriticalVulnerabilityCount = CriticalVulnerabilityCount

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
        if params.get("VulnerabilityList") is not None:
            self._VulnerabilityList = []
            for item in params.get("VulnerabilityList"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._VulnerabilityList.append(obj)
        self._VulnerabilityCount = params.get("VulnerabilityCount")
        self._ImportantVulnerabilityCount = params.get("ImportantVulnerabilityCount")
        self._CriticalVulnerabilityCount = params.get("CriticalVulnerabilityCount")
        self._RequestId = params.get("RequestId")


class DescribeApmVulnerabilityDetailRequest(AbstractModel):
    r"""DescribeApmVulnerabilityDetail request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: unix second-level timestamp
        :type StartTime: int
        :param _EndTime: unix second-level timestamp
        :type EndTime: int
        :param _InstanceId: APM business system ID
        :type InstanceId: str
        :param _Filters: Conditional filtering, required service.name, instrumentation.name, version, vul.id
        :type Filters: list of Filter
        """
        self._StartTime = None
        self._EndTime = None
        self._InstanceId = None
        self._Filters = None

    @property
    def StartTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        r"""APM business system ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        r"""Conditional filtering, required service.name, instrumentation.name, version, vul.id
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceId = params.get("InstanceId")
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
        


class DescribeApmVulnerabilityDetailResponse(AbstractModel):
    r"""DescribeApmVulnerabilityDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Tags: Vulnerability details
        :type Tags: list of ApmTag
        :param _ServiceInstanceList: List of business systems related to vulnerabilities
        :type ServiceInstanceList: list of ApmVulnerabilityServiceDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tags = None
        self._ServiceInstanceList = None
        self._RequestId = None

    @property
    def Tags(self):
        r"""Vulnerability details
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceInstanceList(self):
        r"""List of business systems related to vulnerabilities
        :rtype: list of ApmVulnerabilityServiceDetail
        """
        return self._ServiceInstanceList

    @ServiceInstanceList.setter
    def ServiceInstanceList(self, ServiceInstanceList):
        self._ServiceInstanceList = ServiceInstanceList

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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceInstanceList") is not None:
            self._ServiceInstanceList = []
            for item in params.get("ServiceInstanceList"):
                obj = ApmVulnerabilityServiceDetail()
                obj._deserialize(item)
                self._ServiceInstanceList.append(obj)
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
 -If the time span is (48, +inf) hours, it is aggregated at an hourly granularity.
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
 -If the time span is (48, +inf) hours, it is aggregated at an hourly granularity.
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
        :param _InstanceId: <p>Business system ID</p>
        :type InstanceId: str
        :param _StartTime: <p>Span query start timestamp (unit: seconds)</p>
        :type StartTime: int
        :param _EndTime: <p>Span query end timestamp (unit: s)</p>
        :type EndTime: int
        :param _Filters: <p>Universal filter parameters supported filter key such as service.name</p>
        :type Filters: list of Filter
        :param _OrderBy: <p>Sort<br>Keys now supported:</p><ul><li>startTime</li><li>endTime</li><li>duration</li></ul><p>Values now supported:</p><ul><li>desc (sort in descending order)</li><li>asc (ascending order)</li></ul>
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: <p>Business service name. Console users please enter taw</p>
        :type BusinessName: str
        :param _Limit: <p>Count of single-page projects. Defaults to 10000. Valid value range is 0–10000.</p>
        :type Limit: int
        :param _Offset: <p>Page</p>
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
        r"""<p>Business system ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""<p>Span query start timestamp (unit: seconds)</p>
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>Span query end timestamp (unit: s)</p>
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>Universal filter parameters supported filter key such as service.name</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""<p>Sort<br>Keys now supported:</p><ul><li>startTime</li><li>endTime</li><li>duration</li></ul><p>Values now supported:</p><ul><li>desc (sort in descending order)</li><li>asc (ascending order)</li></ul>
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""<p>Business service name. Console users please enter taw</p>
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""<p>Count of single-page projects. Defaults to 10000. Valid value range is 0–10000.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Page</p>
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
        :param _TotalCount: <p>Total number</p>
        :type TotalCount: int
        :param _Spans: <p>The Spans field contains all content of the link data. Since the data is compressed, perform the following three steps to restore the original text.</p><ol><li>Decode the text in the Spans field with Base64 to get the compressed byte[].</li><li>Decompress the compressed byte[] with gzip to get the byte array before compression.</li><li>Convert the byte array before compression to text using the UTF-8 character set.</li></ol>
        :type Spans: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total number</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""<p>The Spans field contains all content of the link data. Since the data is compressed, perform the following three steps to restore the original text.</p><ol><li>Decode the text in the Spans field with Base64 to get the compressed byte[].</li><li>Decompress the compressed byte[] with gzip to get the byte array before compression.</li><li>Convert the byte array before compression to text using the UTF-8 character set.</li></ol>
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
        :param _InstanceId: <p>Business system ID</p>
        :type InstanceId: str
        :param _StartTime: <p>Span query start timestamp (unit: seconds)</p>
        :type StartTime: int
        :param _EndTime: <p>Span query end timestamp (unit: s)</p>
        :type EndTime: int
        :param _Filters: <p>Universal filter parameters supported filter key such as service.name</p>
        :type Filters: list of Filter
        :param _OrderBy: <p>Sort<br>Keys now supported:</p><ul><li>startTime</li><li>endTime</li><li>duration</li></ul><p>Values now supported:</p><ul><li>desc (sort in descending order)</li><li>asc (ascending order)</li></ul>
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: <p>Business service name. Console users please enter taw</p>
        :type BusinessName: str
        :param _Limit: <p>Count of single-page projects. Defaults to 1000. Valid value range is 1–1000.</p>
        :type Limit: int
        :param _Offset: <p>Page</p>
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
        r"""<p>Business system ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""<p>Span query start timestamp (unit: seconds)</p>
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>Span query end timestamp (unit: s)</p>
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>Universal filter parameters supported filter key such as service.name</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""<p>Sort<br>Keys now supported:</p><ul><li>startTime</li><li>endTime</li><li>duration</li></ul><p>Values now supported:</p><ul><li>desc (sort in descending order)</li><li>asc (ascending order)</li></ul>
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""<p>Business service name. Console users please enter taw</p>
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""<p>Count of single-page projects. Defaults to 1000. Valid value range is 1–1000.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Page</p>
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
        :param _TotalCount: <p>Total number</p>
        :type TotalCount: int
        :param _Spans: <p>Span pagination list</p>
        :type Spans: list of Span
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total number</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""<p>Span pagination list</p>
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


class DescribeOPRAllVulCountRequest(AbstractModel):
    r"""DescribeOPRAllVulCount request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: unix second-level timestamp
        :type StartTime: int
        :param _EndTime: unix second-level timestamp
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""unix second-level timestamp
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOPRAllVulCountResponse(AbstractModel):
    r"""DescribeOPRAllVulCount response structure.

    """

    def __init__(self):
        r"""
        :param _VulnerabilityList: Vulnerability metrics as well as number of business systems	
        :type VulnerabilityList: list of ApmMetricRecord
        :param _VulnerabilityCount: Total number of vulnerabilities
        :type VulnerabilityCount: int
        :param _ImportantVulnerabilityCount: Number of critical vulnerabilities
        :type ImportantVulnerabilityCount: int
        :param _CriticalVulnerabilityCount: High-risk vulnerability count
        :type CriticalVulnerabilityCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VulnerabilityList = None
        self._VulnerabilityCount = None
        self._ImportantVulnerabilityCount = None
        self._CriticalVulnerabilityCount = None
        self._RequestId = None

    @property
    def VulnerabilityList(self):
        r"""Vulnerability metrics as well as number of business systems	
        :rtype: list of ApmMetricRecord
        """
        return self._VulnerabilityList

    @VulnerabilityList.setter
    def VulnerabilityList(self, VulnerabilityList):
        self._VulnerabilityList = VulnerabilityList

    @property
    def VulnerabilityCount(self):
        r"""Total number of vulnerabilities
        :rtype: int
        """
        return self._VulnerabilityCount

    @VulnerabilityCount.setter
    def VulnerabilityCount(self, VulnerabilityCount):
        self._VulnerabilityCount = VulnerabilityCount

    @property
    def ImportantVulnerabilityCount(self):
        r"""Number of critical vulnerabilities
        :rtype: int
        """
        return self._ImportantVulnerabilityCount

    @ImportantVulnerabilityCount.setter
    def ImportantVulnerabilityCount(self, ImportantVulnerabilityCount):
        self._ImportantVulnerabilityCount = ImportantVulnerabilityCount

    @property
    def CriticalVulnerabilityCount(self):
        r"""High-risk vulnerability count
        :rtype: int
        """
        return self._CriticalVulnerabilityCount

    @CriticalVulnerabilityCount.setter
    def CriticalVulnerabilityCount(self, CriticalVulnerabilityCount):
        self._CriticalVulnerabilityCount = CriticalVulnerabilityCount

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
        if params.get("VulnerabilityList") is not None:
            self._VulnerabilityList = []
            for item in params.get("VulnerabilityList"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._VulnerabilityList.append(obj)
        self._VulnerabilityCount = params.get("VulnerabilityCount")
        self._ImportantVulnerabilityCount = params.get("ImportantVulnerabilityCount")
        self._CriticalVulnerabilityCount = params.get("CriticalVulnerabilityCount")
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


class DescribeTopologyNewRequest(AbstractModel):
    r"""DescribeTopologyNew request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Business system ID
        :type InstanceId: str
        :param _StartTime: Querying start time.
        :type StartTime: int
        :param _EndTime: Query end time
        :type EndTime: int
        :param _ServiceName: Application name
        :type ServiceName: str
        :param _UpLevel: Upstream level.
        :type UpLevel: int
        :param _ServiceInstance: Application instance information.
        :type ServiceInstance: str
        :param _DownLevel: downstream hierarchy
        :type DownLevel: int
        :param _View: perspective
        :type View: str
        :param _Filters: Filter.
        :type Filters: list of Filter
        :param _Topic: Represents topic (for MQ topology)
        :type Topic: str
        :param _Selectors: View filtering list.
        :type Selectors: :class:`tencentcloud.apm.v20210622.models.Selectors`
        :param _Id: View ID
        :type Id: str
        :param _TraceID: TraceID
        :type TraceID: str
        :param _IsSlowTopFive: Specifies the top 5 slow response nodes query.
        :type IsSlowTopFive: bool
        :param _GetResource: Whether the resource layer information is obtained.
        :type GetResource: bool
        :param _Tags: Filters by application tag.
        :type Tags: list of ApmTag
        :param _Hidden: Node type not displayed.
        :type Hidden: :class:`tencentcloud.apm.v20210622.models.Selectors`
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._ServiceName = None
        self._UpLevel = None
        self._ServiceInstance = None
        self._DownLevel = None
        self._View = None
        self._Filters = None
        self._Topic = None
        self._Selectors = None
        self._Id = None
        self._TraceID = None
        self._IsSlowTopFive = None
        self._GetResource = None
        self._Tags = None
        self._Hidden = None

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
    def StartTime(self):
        r"""Querying start time.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Query end time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def UpLevel(self):
        r"""Upstream level.
        :rtype: int
        """
        return self._UpLevel

    @UpLevel.setter
    def UpLevel(self, UpLevel):
        self._UpLevel = UpLevel

    @property
    def ServiceInstance(self):
        r"""Application instance information.
        :rtype: str
        """
        return self._ServiceInstance

    @ServiceInstance.setter
    def ServiceInstance(self, ServiceInstance):
        self._ServiceInstance = ServiceInstance

    @property
    def DownLevel(self):
        r"""downstream hierarchy
        :rtype: int
        """
        return self._DownLevel

    @DownLevel.setter
    def DownLevel(self, DownLevel):
        self._DownLevel = DownLevel

    @property
    def View(self):
        r"""perspective
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View

    @property
    def Filters(self):
        r"""Filter.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Topic(self):
        r"""Represents topic (for MQ topology)
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Selectors(self):
        r"""View filtering list.
        :rtype: :class:`tencentcloud.apm.v20210622.models.Selectors`
        """
        return self._Selectors

    @Selectors.setter
    def Selectors(self, Selectors):
        self._Selectors = Selectors

    @property
    def Id(self):
        r"""View ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TraceID(self):
        r"""TraceID
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID

    @property
    def IsSlowTopFive(self):
        r"""Specifies the top 5 slow response nodes query.
        :rtype: bool
        """
        return self._IsSlowTopFive

    @IsSlowTopFive.setter
    def IsSlowTopFive(self, IsSlowTopFive):
        self._IsSlowTopFive = IsSlowTopFive

    @property
    def GetResource(self):
        r"""Whether the resource layer information is obtained.
        :rtype: bool
        """
        return self._GetResource

    @GetResource.setter
    def GetResource(self, GetResource):
        self._GetResource = GetResource

    @property
    def Tags(self):
        r"""Filters by application tag.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Hidden(self):
        r"""Node type not displayed.
        :rtype: :class:`tencentcloud.apm.v20210622.models.Selectors`
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ServiceName = params.get("ServiceName")
        self._UpLevel = params.get("UpLevel")
        self._ServiceInstance = params.get("ServiceInstance")
        self._DownLevel = params.get("DownLevel")
        self._View = params.get("View")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Topic = params.get("Topic")
        if params.get("Selectors") is not None:
            self._Selectors = Selectors()
            self._Selectors._deserialize(params.get("Selectors"))
        self._Id = params.get("Id")
        self._TraceID = params.get("TraceID")
        self._IsSlowTopFive = params.get("IsSlowTopFive")
        self._GetResource = params.get("GetResource")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Hidden") is not None:
            self._Hidden = Selectors()
            self._Hidden._deserialize(params.get("Hidden"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopologyNewResponse(AbstractModel):
    r"""DescribeTopologyNew response structure.

    """

    def __init__(self):
        r"""
        :param _Nodes: Node collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nodes: list of TopologyNode
        :param _Edges: Edge set.
        :type Edges: list of TopologyEdgeNew
        :param _TopologyModifyFlag: Whether the topology map is modified
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopologyModifyFlag: int
        :param _Selectors: Number of nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Selectors: :class:`tencentcloud.apm.v20210622.models.SelectorView`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Nodes = None
        self._Edges = None
        self._TopologyModifyFlag = None
        self._Selectors = None
        self._RequestId = None

    @property
    def Nodes(self):
        r"""Node collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TopologyNode
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Edges(self):
        r"""Edge set.
        :rtype: list of TopologyEdgeNew
        """
        return self._Edges

    @Edges.setter
    def Edges(self, Edges):
        self._Edges = Edges

    @property
    def TopologyModifyFlag(self):
        r"""Whether the topology map is modified
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TopologyModifyFlag

    @TopologyModifyFlag.setter
    def TopologyModifyFlag(self, TopologyModifyFlag):
        self._TopologyModifyFlag = TopologyModifyFlag

    @property
    def Selectors(self):
        r"""Number of nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.SelectorView`
        """
        return self._Selectors

    @Selectors.setter
    def Selectors(self, Selectors):
        self._Selectors = Selectors

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
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = TopologyNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("Edges") is not None:
            self._Edges = []
            for item in params.get("Edges"):
                obj = TopologyEdgeNew()
                obj._deserialize(item)
                self._Edges.append(obj)
        self._TopologyModifyFlag = params.get("TopologyModifyFlag")
        if params.get("Selectors") is not None:
            self._Selectors = SelectorView()
            self._Selectors._deserialize(params.get("Selectors"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Queries filter parameters.

    """

    def __init__(self):
        r"""
        :param _Type: <p>Filter method (=, !=, in)</p>
        :type Type: str
        :param _Key: <p>Filter dimension name</p><p>For details, see the actual interface field description</p>
        :type Key: str
        :param _Value: <p>Filter value. Use comma-separated multiple values for in filtering method.</p>
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        r"""<p>Filter method (=, !=, in)</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""<p>Filter dimension name</p><p>For details, see the actual interface field description</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Filter value. Use comma-separated multiple values for in filtering method.</p>
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
        :param _InstanceId: <p>Business system ID</p>
        :type InstanceId: str
        :param _ServiceName: <p>Application name</p>
        :type ServiceName: str
        :param _UrlConvergenceSwitch: <p>URL convergence switch, 0 Off | 1 On</p>
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: <p>URL convergence threshold</p>
        :type UrlConvergenceThreshold: int
        :param _ExceptionFilter: <p>Exception filtering regex rules, comma-separated</p>
        :type ExceptionFilter: str
        :param _UrlConvergence: <p>URL convergence regex rules, comma-separated</p>
        :type UrlConvergence: str
        :param _ErrorCodeFilter: <p>Error code filtering, comma-separated</p>
        :type ErrorCodeFilter: str
        :param _UrlExclude: <p>URL exclusion regex rule, comma-separated</p>
        :type UrlExclude: str
        :param _IsRelatedLog: <p>Log switch 0 Disabled 1 Enabled</p>
        :type IsRelatedLog: int
        :param _LogRegion: <p>Log region</p>
        :type LogRegion: str
        :param _LogTopicID: <p>Log topic ID</p>
        :type LogTopicID: str
        :param _LogSet: <p>CLS logset | ES cluster ID</p>
        :type LogSet: str
        :param _LogSource: <p>Log source CLS | ES</p>
        :type LogSource: str
        :param _IgnoreOperationName: <p>Interfaces to Filter</p>
        :type IgnoreOperationName: str
        :param _EnableSnapshot: <p>Whether thread profiling is enabled</p>
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: <p>Timeout threshold for thread profiling</p>
        :type SnapshotTimeout: int
        :param _AgentEnable: <p>Whether to enable agent</p>
        :type AgentEnable: bool
        :param _TraceSquash: <p>Whether to enable link compression</p>
        :type TraceSquash: bool
        :param _EventEnable: <p>Whether the switch for enabling application diagnosis is enabled</p>
        :type EventEnable: bool
        :param _InstrumentList: <p>Component list</p>
        :type InstrumentList: list of Instrument
        :param _AgentOperationConfigView: <p>probe API related configuration</p>
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: <p>Whether the application log configuration is enabled</p>
        :type EnableLogConfig: bool
        :param _EnableDashboardConfig: <p>Whether the dashboard configuration is enabled: false (disabled, consistent with the business system)/true (enabled, application-level configuration)</p>
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: <p>Whether to associate with dashboard: 0 off 1 on</p>
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: <p>dashboard ID</p>
        :type DashboardTopicID: str
        :param _LogIndexType: <p>CLS index type (0=full-text index, 1=key-value index)</p>
        :type LogIndexType: int
        :param _LogTraceIdKey: <p>Index key of traceId: This parameter is valid only when the CLS index type is key-value index.</p>
        :type LogTraceIdKey: str
        :param _EnableSecurityConfig: <p>Whether application security configuration is enabled</p>
        :type EnableSecurityConfig: bool
        :param _IsSqlInjectionAnalysis: <p>Whether SQL injection analysis is enabled</p>
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: <p>Whether component vulnerability detection is enabled</p>
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: <p>Whether remote command detection is enabled</p>
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: <p>Whether Java Webshell detection is enabled</p>
        :type IsMemoryHijackingAnalysis: int
        :param _IsDeleteAnyFileAnalysis: <p>Whether to enable detection of any file deletion (0 - turn off, 1 - turn on)</p>
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: <p>Whether to enable arbitrary file read detection (0 - disabled, 1 - enabled)</p>
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: <p>Whether to enable arbitrary file upload detection (0-disable, 1-enable)</p>
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: <p>Whether to enable detection of arbitrary files (0 - disabled, 1 - enabled)</p>
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: <p>Whether path traversal detection is enabled (0-disabled, 1-enabled)</p>
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: <p>Whether to enable template engine injection detection (0-disable, 1-enable)</p>
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: <p>Whether to enable script engine injection detection (0-disable, 1-enable)</p>
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: <p>Whether expression injection detection is enabled (0-disabled, 1-enabled)</p>
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: <p>Whether JNDI injection detection is enabled (0 - disabled, 1 - enabled)</p>
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: <p>Whether JNI injection detection is enabled (0-disabled, 1-enabled)</p>
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: <p>Whether to enable Webshell backdoor detection (0 - disabled, 1 - enabled)</p>
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: <p>Whether deserialization detection is enabled (0-disabled, 1-enabled)</p>
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: <p>API auto convergence switch, 0-off | 1-on</p>
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: <p>URL long segment convergence threshold</p>
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: <p>URL digit segment convergence threshold</p>
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: <p>Fuse memory threshold of the probe</p>
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: <p>Probe fuse CPU threshold</p>
        :type DisableCpuUsed: int
        :param _DbStatementParametersEnabled: <p>Whether SQL parameter access is enabled</p>
        :type DbStatementParametersEnabled: bool
        :param _SlowSQLThresholds: <p>Slow SQL threshold</p>
        :type SlowSQLThresholds: list of ApmTag
        :param _EnableDesensitizationRule: <p>Whether the masking rule is enabled</p>
        :type EnableDesensitizationRule: int
        :param _DesensitizationRule: <p>Masking rule</p>
        :type DesensitizationRule: str
        :param _LogSpanIdKey: <p>Index key of spanId: This parameter is valid only when the CLS index type is key-value index.</p>
        :type LogSpanIdKey: str
        :param _AutoProfilingConfig: <p>Automated performance analysis task configuration</p>
        :type AutoProfilingConfig: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        :param _EnableThresholdConfig: <p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
        :type EnableThresholdConfig: bool
        :param _ErrRateThreshold: <p>Error rate threshold (%) used to judge the application health status as "red".</p>
        :type ErrRateThreshold: int
        :param _ResponseDurationWarningThreshold: <p>Alert threshold for response time (ms), used to judge the application health status as "yellow".</p>
        :type ResponseDurationWarningThreshold: int
        :param _UseDefaultFuseConfig: <p>Whether to use the default fuse threshold of the probe</p>
        :type UseDefaultFuseConfig: bool
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
        self._DbStatementParametersEnabled = None
        self._SlowSQLThresholds = None
        self._EnableDesensitizationRule = None
        self._DesensitizationRule = None
        self._LogSpanIdKey = None
        self._AutoProfilingConfig = None
        self._EnableThresholdConfig = None
        self._ErrRateThreshold = None
        self._ResponseDurationWarningThreshold = None
        self._UseDefaultFuseConfig = None

    @property
    def InstanceId(self):
        r"""<p>Business system ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""<p>Application name</p>
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""<p>URL convergence switch, 0 Off | 1 On</p>
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""<p>URL convergence threshold</p>
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def ExceptionFilter(self):
        r"""<p>Exception filtering regex rules, comma-separated</p>
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def UrlConvergence(self):
        r"""<p>URL convergence regex rules, comma-separated</p>
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ErrorCodeFilter(self):
        r"""<p>Error code filtering, comma-separated</p>
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def UrlExclude(self):
        r"""<p>URL exclusion regex rule, comma-separated</p>
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""<p>Log switch 0 Disabled 1 Enabled</p>
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        r"""<p>Log region</p>
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        r"""<p>Log topic ID</p>
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        r"""<p>CLS logset | ES cluster ID</p>
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        r"""<p>Log source CLS | ES</p>
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IgnoreOperationName(self):
        r"""<p>Interfaces to Filter</p>
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def EnableSnapshot(self):
        r"""<p>Whether thread profiling is enabled</p>
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""<p>Timeout threshold for thread profiling</p>
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""<p>Whether to enable agent</p>
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def TraceSquash(self):
        r"""<p>Whether to enable link compression</p>
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""<p>Whether the switch for enabling application diagnosis is enabled</p>
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def InstrumentList(self):
        r"""<p>Component list</p>
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def AgentOperationConfigView(self):
        r"""<p>probe API related configuration</p>
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""<p>Whether the application log configuration is enabled</p>
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def EnableDashboardConfig(self):
        r"""<p>Whether the dashboard configuration is enabled: false (disabled, consistent with the business system)/true (enabled, application-level configuration)</p>
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""<p>Whether to associate with dashboard: 0 off 1 on</p>
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""<p>dashboard ID</p>
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def LogIndexType(self):
        r"""<p>CLS index type (0=full-text index, 1=key-value index)</p>
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""<p>Index key of traceId: This parameter is valid only when the CLS index type is key-value index.</p>
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def EnableSecurityConfig(self):
        r"""<p>Whether application security configuration is enabled</p>
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsSqlInjectionAnalysis(self):
        r"""<p>Whether SQL injection analysis is enabled</p>
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""<p>Whether component vulnerability detection is enabled</p>
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""<p>Whether remote command detection is enabled</p>
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""<p>Whether Java Webshell detection is enabled</p>
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""<p>Whether to enable detection of any file deletion (0 - turn off, 1 - turn on)</p>
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file read detection (0 - disabled, 1 - enabled)</p>
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""<p>Whether to enable arbitrary file upload detection (0-disable, 1-enable)</p>
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""<p>Whether to enable detection of arbitrary files (0 - disabled, 1 - enabled)</p>
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""<p>Whether path traversal detection is enabled (0-disabled, 1-enabled)</p>
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""<p>Whether to enable template engine injection detection (0-disable, 1-enable)</p>
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""<p>Whether to enable script engine injection detection (0-disable, 1-enable)</p>
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""<p>Whether expression injection detection is enabled (0-disabled, 1-enabled)</p>
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""<p>Whether JNDI injection detection is enabled (0 - disabled, 1 - enabled)</p>
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""<p>Whether JNI injection detection is enabled (0-disabled, 1-enabled)</p>
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""<p>Whether to enable Webshell backdoor detection (0 - disabled, 1 - enabled)</p>
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""<p>Whether deserialization detection is enabled (0-disabled, 1-enabled)</p>
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""<p>API auto convergence switch, 0-off | 1-on</p>
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""<p>URL long segment convergence threshold</p>
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""<p>URL digit segment convergence threshold</p>
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""<p>Fuse memory threshold of the probe</p>
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""<p>Probe fuse CPU threshold</p>
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed

    @property
    def DbStatementParametersEnabled(self):
        r"""<p>Whether SQL parameter access is enabled</p>
        :rtype: bool
        """
        return self._DbStatementParametersEnabled

    @DbStatementParametersEnabled.setter
    def DbStatementParametersEnabled(self, DbStatementParametersEnabled):
        self._DbStatementParametersEnabled = DbStatementParametersEnabled

    @property
    def SlowSQLThresholds(self):
        r"""<p>Slow SQL threshold</p>
        :rtype: list of ApmTag
        """
        return self._SlowSQLThresholds

    @SlowSQLThresholds.setter
    def SlowSQLThresholds(self, SlowSQLThresholds):
        self._SlowSQLThresholds = SlowSQLThresholds

    @property
    def EnableDesensitizationRule(self):
        r"""<p>Whether the masking rule is enabled</p>
        :rtype: int
        """
        return self._EnableDesensitizationRule

    @EnableDesensitizationRule.setter
    def EnableDesensitizationRule(self, EnableDesensitizationRule):
        self._EnableDesensitizationRule = EnableDesensitizationRule

    @property
    def DesensitizationRule(self):
        r"""<p>Masking rule</p>
        :rtype: str
        """
        return self._DesensitizationRule

    @DesensitizationRule.setter
    def DesensitizationRule(self, DesensitizationRule):
        self._DesensitizationRule = DesensitizationRule

    @property
    def LogSpanIdKey(self):
        r"""<p>Index key of spanId: This parameter is valid only when the CLS index type is key-value index.</p>
        :rtype: str
        """
        return self._LogSpanIdKey

    @LogSpanIdKey.setter
    def LogSpanIdKey(self, LogSpanIdKey):
        self._LogSpanIdKey = LogSpanIdKey

    @property
    def AutoProfilingConfig(self):
        r"""<p>Automated performance analysis task configuration</p>
        :rtype: :class:`tencentcloud.apm.v20210622.models.AutoProfilingConfig`
        """
        return self._AutoProfilingConfig

    @AutoProfilingConfig.setter
    def AutoProfilingConfig(self, AutoProfilingConfig):
        self._AutoProfilingConfig = AutoProfilingConfig

    @property
    def EnableThresholdConfig(self):
        r"""<p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
        :rtype: bool
        """
        return self._EnableThresholdConfig

    @EnableThresholdConfig.setter
    def EnableThresholdConfig(self, EnableThresholdConfig):
        self._EnableThresholdConfig = EnableThresholdConfig

    @property
    def ErrRateThreshold(self):
        r"""<p>Error rate threshold (%) used to judge the application health status as "red".</p>
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def ResponseDurationWarningThreshold(self):
        r"""<p>Alert threshold for response time (ms), used to judge the application health status as "yellow".</p>
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def UseDefaultFuseConfig(self):
        r"""<p>Whether to use the default fuse threshold of the probe</p>
        :rtype: bool
        """
        return self._UseDefaultFuseConfig

    @UseDefaultFuseConfig.setter
    def UseDefaultFuseConfig(self, UseDefaultFuseConfig):
        self._UseDefaultFuseConfig = UseDefaultFuseConfig


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
        self._DbStatementParametersEnabled = params.get("DbStatementParametersEnabled")
        if params.get("SlowSQLThresholds") is not None:
            self._SlowSQLThresholds = []
            for item in params.get("SlowSQLThresholds"):
                obj = ApmTag()
                obj._deserialize(item)
                self._SlowSQLThresholds.append(obj)
        self._EnableDesensitizationRule = params.get("EnableDesensitizationRule")
        self._DesensitizationRule = params.get("DesensitizationRule")
        self._LogSpanIdKey = params.get("LogSpanIdKey")
        if params.get("AutoProfilingConfig") is not None:
            self._AutoProfilingConfig = AutoProfilingConfig()
            self._AutoProfilingConfig._deserialize(params.get("AutoProfilingConfig"))
        self._EnableThresholdConfig = params.get("EnableThresholdConfig")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._UseDefaultFuseConfig = params.get("UseDefaultFuseConfig")
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
        :param _ProductName: <p>Associated product name, currently only support Prometheus, CKafka</p>
        :type ProductName: str
        :param _Status: <p>Status of the association relationship: // Association relationship status: 1 (enabled), 2 (disabled)</p>
        :type Status: int
        :param _InstanceId: <p>Business system ID</p>
        :type InstanceId: str
        :param _PeerId: <p>ID of the associated product instance</p>
        :type PeerId: str
        :param _Topic: <p>CKafka message topic</p>
        :type Topic: str
        :param _MetricTopic: <p>Ckafka message topic</p>
        :type MetricTopic: str
        """
        self._ProductName = None
        self._Status = None
        self._InstanceId = None
        self._PeerId = None
        self._Topic = None
        self._MetricTopic = None

    @property
    def ProductName(self):
        r"""<p>Associated product name, currently only support Prometheus, CKafka</p>
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Status(self):
        r"""<p>Status of the association relationship: // Association relationship status: 1 (enabled), 2 (disabled)</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""<p>Business system ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PeerId(self):
        r"""<p>ID of the associated product instance</p>
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Topic(self):
        r"""<p>CKafka message topic</p>
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def MetricTopic(self):
        r"""<p>Ckafka message topic</p>
        :rtype: str
        """
        return self._MetricTopic

    @MetricTopic.setter
    def MetricTopic(self, MetricTopic):
        self._MetricTopic = MetricTopic


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._PeerId = params.get("PeerId")
        self._Topic = params.get("Topic")
        self._MetricTopic = params.get("MetricTopic")
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
        :param _LogSpanIdKey: Index key of spanId: This parameter is valid only when the CLS index type is key-value index
        :type LogSpanIdKey: str
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
        self._LogSpanIdKey = None

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

    @property
    def LogSpanIdKey(self):
        r"""Index key of spanId: This parameter is valid only when the CLS index type is key-value index
        :rtype: str
        """
        return self._LogSpanIdKey

    @LogSpanIdKey.setter
    def LogSpanIdKey(self, LogSpanIdKey):
        self._LogSpanIdKey = LogSpanIdKey


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
        self._LogSpanIdKey = params.get("LogSpanIdKey")
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


class ModifyApmServiceRequest(AbstractModel):
    r"""ModifyApmService request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceID: Application ID
        :type ServiceID: str
        :param _ServiceDescription: Application description
        :type ServiceDescription: str
        :param _Tags: Tag list
        :type Tags: list of ApmTag
        """
        self._ServiceID = None
        self._ServiceDescription = None
        self._Tags = None

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
    def ServiceDescription(self):
        r"""Application description
        :rtype: str
        """
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def Tags(self):
        r"""Tag list
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ServiceID = params.get("ServiceID")
        self._ServiceDescription = params.get("ServiceDescription")
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
        


class ModifyApmServiceResponse(AbstractModel):
    r"""ModifyApmService response structure.

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
        


class Position(AbstractModel):
    r"""Node location information

    """

    def __init__(self):
        r"""
        :param _X: Node horizontal coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :type X: float
        :param _Y: Node vertical coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :type Y: float
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""Node horizontal coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Node vertical coordinate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
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
        


class Resource(AbstractModel):
    r"""Resource layer information.

    """

    def __init__(self):
        r"""
        :param _Type: Resource type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: list of str
        :param _TKEMeta: TKE resource layer information.
        :type TKEMeta: list of TkeMeta
        :param _CVMMeta: CVM resource information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CVMMeta: list of CVMMeta
        """
        self._Type = None
        self._TKEMeta = None
        self._CVMMeta = None

    @property
    def Type(self):
        r"""Resource type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TKEMeta(self):
        r"""TKE resource layer information.
        :rtype: list of TkeMeta
        """
        return self._TKEMeta

    @TKEMeta.setter
    def TKEMeta(self, TKEMeta):
        self._TKEMeta = TKEMeta

    @property
    def CVMMeta(self):
        r"""CVM resource information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CVMMeta
        """
        return self._CVMMeta

    @CVMMeta.setter
    def CVMMeta(self, CVMMeta):
        self._CVMMeta = CVMMeta


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("TKEMeta") is not None:
            self._TKEMeta = []
            for item in params.get("TKEMeta"):
                obj = TkeMeta()
                obj._deserialize(item)
                self._TKEMeta.append(obj)
        if params.get("CVMMeta") is not None:
            self._CVMMeta = []
            for item in params.get("CVMMeta"):
                obj = CVMMeta()
                obj._deserialize(item)
                self._CVMMeta.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectorView(AbstractModel):
    r"""Contains the quantities of components and healthy nodes in the nodes.

    """

    def __init__(self):
        r"""
        :param _Component: Component Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type Component: :class:`tencentcloud.apm.v20210622.models.ComponentTopologyView`
        """
        self._Component = None

    @property
    def Component(self):
        r"""Component Count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.ComponentTopologyView`
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component


    def _deserialize(self, params):
        if params.get("Component") is not None:
            self._Component = ComponentTopologyView()
            self._Component._deserialize(params.get("Component"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Selectors(AbstractModel):
    r"""Selection status of the topology view.

    """

    def __init__(self):
        r"""
        :param _Component: Selection status of the component.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Component: list of str
        """
        self._Component = None

    @property
    def Component(self):
        r"""Selection status of the component.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component


    def _deserialize(self, params):
        self._Component = params.get("Component")
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
        :param _ServiceID: <p>Application ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceID: str
        :param _InstanceKey: <p>Business system ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceKey: str
        :param _AppID: <p>User appid</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppID: int
        :param _CreateUIN: <p>main account uin</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateUIN: str
        :param _ServiceName: <p>Application name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _ServiceDescription: <p>Application description</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDescription: str
        :param _Region: <p>Region</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Tags: <p>Tag</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of ApmTag
        :param _InstanceName: <p>Business system name</p>
        :type InstanceName: str
        :param _EnableThresholdConfig: <p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableThresholdConfig: bool
        :param _ErrRateThreshold: <p>Error rate threshold (%) used to judge the application health status as "red".</p><p>Unit: %</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrRateThreshold: int
        :param _ResponseDurationWarningThreshold: <p>Alert threshold for response time (ms), used to judge application health status as "yellow".</p><p>Unit: ms</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResponseDurationWarningThreshold: int
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
        self._EnableThresholdConfig = None
        self._ErrRateThreshold = None
        self._ResponseDurationWarningThreshold = None

    @property
    def ServiceID(self):
        r"""<p>Application ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def InstanceKey(self):
        r"""<p>Business system ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def AppID(self):
        r"""<p>User appid</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CreateUIN(self):
        r"""<p>main account uin</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateUIN

    @CreateUIN.setter
    def CreateUIN(self, CreateUIN):
        self._CreateUIN = CreateUIN

    @property
    def ServiceName(self):
        r"""<p>Application name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDescription(self):
        r"""<p>Application description</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def Region(self):
        r"""<p>Region</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""<p>Tag</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        r"""<p>Business system name</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def EnableThresholdConfig(self):
        r"""<p>Threshold configuration switch. true means use application level threshold; false means use business system level threshold.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableThresholdConfig

    @EnableThresholdConfig.setter
    def EnableThresholdConfig(self, EnableThresholdConfig):
        self._EnableThresholdConfig = EnableThresholdConfig

    @property
    def ErrRateThreshold(self):
        r"""<p>Error rate threshold (%) used to judge the application health status as "red".</p><p>Unit: %</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def ResponseDurationWarningThreshold(self):
        r"""<p>Alert threshold for response time (ms), used to judge application health status as "yellow".</p><p>Unit: ms</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold


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
        self._EnableThresholdConfig = params.get("EnableThresholdConfig")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
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


class TkeMeta(AbstractModel):
    r"""TKE resource metadata.

    """

    def __init__(self):
        r"""
        :param _Region: Region.
        :type Region: str
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _PodName: pod name
        :type PodName: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Deployment: workload
        :type Deployment: str
        :param _PodIP: pod ip
        :type PodIP: str
        :param _NodeIP: node ip
        :type NodeIP: str
        """
        self._Region = None
        self._ClusterID = None
        self._PodName = None
        self._Namespace = None
        self._Deployment = None
        self._PodIP = None
        self._NodeIP = None

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterID(self):
        r"""Cluster ID
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def PodName(self):
        r"""pod name
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Namespace(self):
        r"""Namespace
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Deployment(self):
        r"""workload
        :rtype: str
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

    @property
    def PodIP(self):
        r"""pod ip
        :rtype: str
        """
        return self._PodIP

    @PodIP.setter
    def PodIP(self, PodIP):
        self._PodIP = PodIP

    @property
    def NodeIP(self):
        r"""node ip
        :rtype: str
        """
        return self._NodeIP

    @NodeIP.setter
    def NodeIP(self, NodeIP):
        self._NodeIP = NodeIP


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._ClusterID = params.get("ClusterID")
        self._PodName = params.get("PodName")
        self._Namespace = params.get("Namespace")
        self._Deployment = params.get("Deployment")
        self._PodIP = params.get("PodIP")
        self._NodeIP = params.get("NodeIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopologyEdgeNew(AbstractModel):
    r"""Topology edge definition

    """

    def __init__(self):
        r"""
        :param _Source: Source node
        :type Source: str
        :param _Id: Edge ID
        :type Id: str
        :param _Weight: Edge weight
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: float
        :param _Target: Target node
        :type Target: str
        :param _Duration: response time
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: float
        :param _ErrRate: Error rate
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrRate: float
        :param _Qps: throughput
Note: This field may return null, indicating that no valid values can be obtained.
        :type Qps: float
        :param _Type: Edge type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Color: Edge color
Note: This field may return null, indicating that no valid values can be obtained.
        :type Color: str
        :param _SqlRequestCount: SQL call count
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlRequestCount: float
        :param _SqlErrorRequestCount: SQL call error count
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlErrorRequestCount: float
        :param _SourceComp: Source node type on the edge of the topology diagram. Application/MQ/DB.
        :type SourceComp: str
        :param _TargetComp: Target node type on the edge of the topology diagram. Application/MQ/DB.
        :type TargetComp: str
        """
        self._Source = None
        self._Id = None
        self._Weight = None
        self._Target = None
        self._Duration = None
        self._ErrRate = None
        self._Qps = None
        self._Type = None
        self._Color = None
        self._SqlRequestCount = None
        self._SqlErrorRequestCount = None
        self._SourceComp = None
        self._TargetComp = None

    @property
    def Source(self):
        r"""Source node
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Id(self):
        r"""Edge ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Weight(self):
        r"""Edge weight
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Target(self):
        r"""Target node
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Duration(self):
        r"""response time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ErrRate(self):
        r"""Error rate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._ErrRate

    @ErrRate.setter
    def ErrRate(self, ErrRate):
        self._ErrRate = ErrRate

    @property
    def Qps(self):
        r"""throughput
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Type(self):
        r"""Edge type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Color(self):
        r"""Edge color
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def SqlRequestCount(self):
        r"""SQL call count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._SqlRequestCount

    @SqlRequestCount.setter
    def SqlRequestCount(self, SqlRequestCount):
        self._SqlRequestCount = SqlRequestCount

    @property
    def SqlErrorRequestCount(self):
        r"""SQL call error count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._SqlErrorRequestCount

    @SqlErrorRequestCount.setter
    def SqlErrorRequestCount(self, SqlErrorRequestCount):
        self._SqlErrorRequestCount = SqlErrorRequestCount

    @property
    def SourceComp(self):
        r"""Source node type on the edge of the topology diagram. Application/MQ/DB.
        :rtype: str
        """
        return self._SourceComp

    @SourceComp.setter
    def SourceComp(self, SourceComp):
        self._SourceComp = SourceComp

    @property
    def TargetComp(self):
        r"""Target node type on the edge of the topology diagram. Application/MQ/DB.
        :rtype: str
        """
        return self._TargetComp

    @TargetComp.setter
    def TargetComp(self, TargetComp):
        self._TargetComp = TargetComp


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Id = params.get("Id")
        self._Weight = params.get("Weight")
        self._Target = params.get("Target")
        self._Duration = params.get("Duration")
        self._ErrRate = params.get("ErrRate")
        self._Qps = params.get("Qps")
        self._Type = params.get("Type")
        self._Color = params.get("Color")
        self._SqlRequestCount = params.get("SqlRequestCount")
        self._SqlErrorRequestCount = params.get("SqlErrorRequestCount")
        self._SourceComp = params.get("SourceComp")
        self._TargetComp = params.get("TargetComp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopologyNode(AbstractModel):
    r"""Topology graph edge node

    """

    def __init__(self):
        r"""
        :param _ErrRate: Error rate
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrRate: float
        :param _Kind: Node type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Kind: str
        :param _Name: Node name
        :type Name: str
        :param _Weight: Node weight
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: float
        :param _Color: Node color
Note: This field may return null, indicating that no valid values can be obtained.
        :type Color: str
        :param _Duration: response time
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: float
        :param _Qps: throughput
Note: This field may return null, indicating that no valid values can be obtained.
        :type Qps: float
        :param _Type: Node type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Id: Node ID
        :type Id: str
        :param _Size: Node size
Note: This field may return null, indicating that no valid values can be obtained.
        :type Size: str
        :param _IsModule: Indicate whether the node is a component
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsModule: bool
        :param _Position: Node location information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Position: :class:`tencentcloud.apm.v20210622.models.Position`
        :param _Tags: Node tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of ApmTag
        :param _CanDrillDown: Whether the node supports drill-down.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CanDrillDown: bool
        :param _Resource: Resource layer information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resource: :class:`tencentcloud.apm.v20210622.models.Resource`
        :param _NodeView: Name of the topology node view.
        :type NodeView: str
        :param _ConsumerDuration: Message consumption time of the MQ consumer, in ms.
        :type ConsumerDuration: float
        :param _ConsumerErrRate: Error rate of the MQ consumers, in %.
        :type ConsumerErrRate: float
        :param _ConsumerQps: Throughput of the message queue (MQ) consumer.
        :type ConsumerQps: float
        :param _ServiceId: Application ID.
        :type ServiceId: str
        """
        self._ErrRate = None
        self._Kind = None
        self._Name = None
        self._Weight = None
        self._Color = None
        self._Duration = None
        self._Qps = None
        self._Type = None
        self._Id = None
        self._Size = None
        self._IsModule = None
        self._Position = None
        self._Tags = None
        self._CanDrillDown = None
        self._Resource = None
        self._NodeView = None
        self._ConsumerDuration = None
        self._ConsumerErrRate = None
        self._ConsumerQps = None
        self._ServiceId = None

    @property
    def ErrRate(self):
        r"""Error rate
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._ErrRate

    @ErrRate.setter
    def ErrRate(self, ErrRate):
        self._ErrRate = ErrRate

    @property
    def Kind(self):
        r"""Node type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        r"""Node name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Weight(self):
        r"""Node weight
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Color(self):
        r"""Node color
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Duration(self):
        r"""response time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Qps(self):
        r"""throughput
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Type(self):
        r"""Node type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        r"""Node ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Size(self):
        r"""Node size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def IsModule(self):
        r"""Indicate whether the node is a component
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsModule

    @IsModule.setter
    def IsModule(self, IsModule):
        self._IsModule = IsModule

    @property
    def Position(self):
        r"""Node location information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.Position`
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Tags(self):
        r"""Node tags
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CanDrillDown(self):
        r"""Whether the node supports drill-down.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CanDrillDown

    @CanDrillDown.setter
    def CanDrillDown(self, CanDrillDown):
        self._CanDrillDown = CanDrillDown

    @property
    def Resource(self):
        r"""Resource layer information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.apm.v20210622.models.Resource`
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def NodeView(self):
        r"""Name of the topology node view.
        :rtype: str
        """
        return self._NodeView

    @NodeView.setter
    def NodeView(self, NodeView):
        self._NodeView = NodeView

    @property
    def ConsumerDuration(self):
        r"""Message consumption time of the MQ consumer, in ms.
        :rtype: float
        """
        return self._ConsumerDuration

    @ConsumerDuration.setter
    def ConsumerDuration(self, ConsumerDuration):
        self._ConsumerDuration = ConsumerDuration

    @property
    def ConsumerErrRate(self):
        r"""Error rate of the MQ consumers, in %.
        :rtype: float
        """
        return self._ConsumerErrRate

    @ConsumerErrRate.setter
    def ConsumerErrRate(self, ConsumerErrRate):
        self._ConsumerErrRate = ConsumerErrRate

    @property
    def ConsumerQps(self):
        r"""Throughput of the message queue (MQ) consumer.
        :rtype: float
        """
        return self._ConsumerQps

    @ConsumerQps.setter
    def ConsumerQps(self, ConsumerQps):
        self._ConsumerQps = ConsumerQps

    @property
    def ServiceId(self):
        r"""Application ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ErrRate = params.get("ErrRate")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Weight = params.get("Weight")
        self._Color = params.get("Color")
        self._Duration = params.get("Duration")
        self._Qps = params.get("Qps")
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        self._Size = params.get("Size")
        self._IsModule = params.get("IsModule")
        if params.get("Position") is not None:
            self._Position = Position()
            self._Position._deserialize(params.get("Position"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CanDrillDown = params.get("CanDrillDown")
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        self._NodeView = params.get("NodeView")
        self._ConsumerDuration = params.get("ConsumerDuration")
        self._ConsumerErrRate = params.get("ConsumerErrRate")
        self._ConsumerQps = params.get("ConsumerQps")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        