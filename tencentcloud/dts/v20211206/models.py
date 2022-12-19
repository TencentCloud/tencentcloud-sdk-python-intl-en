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


class CheckStep(AbstractModel):
    """Check step

    """

    def __init__(self):
        r"""
        :param StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param StepId: Step ID such as `ConnectDBCheck`, `VersionCheck`, and `SrcPrivilegeCheck`. The specific check items are subject to source and target instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param StepStatus: Result of this check step. Valid values: `pass`, `failed`, `notStarted`, `blocked`, `warning`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepStatus: str
        :param StepMessage: Error message in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepMessage: str
        :param DetailCheckItems: Specific check item in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailCheckItems: list of DetailCheckItem
        :param HasSkipped: Whether this step was skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasSkipped: bool
        """
        self.StepNo = None
        self.StepId = None
        self.StepName = None
        self.StepStatus = None
        self.StepMessage = None
        self.DetailCheckItems = None
        self.HasSkipped = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepId = params.get("StepId")
        self.StepName = params.get("StepName")
        self.StepStatus = params.get("StepStatus")
        self.StepMessage = params.get("StepMessage")
        if params.get("DetailCheckItems") is not None:
            self.DetailCheckItems = []
            for item in params.get("DetailCheckItems"):
                obj = DetailCheckItem()
                obj._deserialize(item)
                self.DetailCheckItems.append(obj)
        self.HasSkipped = params.get("HasSkipped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStepInfo(AbstractModel):
    """Check task running details

    """

    def __init__(self):
        r"""
        :param StartAt: Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartAt: str
        :param EndAt: Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndAt: str
        :param Progress: Task step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        self.StartAt = None
        self.EndAt = None
        self.Progress = None


    def _deserialize(self, params):
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        if params.get("Progress") is not None:
            self.Progress = ProcessProgress()
            self.Progress._deserialize(params.get("Progress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareAbstractInfo(AbstractModel):
    """Summary information of data consistency check

    """

    def __init__(self):
        r"""
        :param Conclusion: Comparison conclusion. Valid values: `same`, `different`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conclusion: str
        :param Status: Task status. Valid values: `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param TotalTables: Total number of tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalTables: int
        :param CheckedTables: Number of checked tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckedTables: int
        :param DifferentTables: Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type DifferentTables: int
        :param SkippedTables: Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkippedTables: int
        :param DifferentRows: Number of inconsistent data rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type DifferentRows: int
        """
        self.Conclusion = None
        self.Status = None
        self.TotalTables = None
        self.CheckedTables = None
        self.DifferentTables = None
        self.SkippedTables = None
        self.DifferentRows = None


    def _deserialize(self, params):
        self.Conclusion = params.get("Conclusion")
        self.Status = params.get("Status")
        self.TotalTables = params.get("TotalTables")
        self.CheckedTables = params.get("CheckedTables")
        self.DifferentTables = params.get("DifferentTables")
        self.SkippedTables = params.get("SkippedTables")
        self.DifferentRows = params.get("DifferentRows")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareDetailInfo(AbstractModel):
    """Data consistency check details

    """

    def __init__(self):
        r"""
        :param Difference: Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Difference: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        :param Skipped: Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Skipped: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        self.Difference = None
        self.Skipped = None


    def _deserialize(self, params):
        if params.get("Difference") is not None:
            self.Difference = DifferenceDetail()
            self.Difference._deserialize(params.get("Difference"))
        if params.get("Skipped") is not None:
            self.Skipped = SkippedDetail()
            self.Skipped._deserialize(params.get("Skipped"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObject(AbstractModel):
    """Configuration of the data consistency check object

    """

    def __init__(self):
        r"""
        :param ObjectMode: Object migration mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectMode: str
        :param ObjectItems: Migration database/table configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectItems: list of CompareObjectItem
        """
        self.ObjectMode = None
        self.ObjectItems = None


    def _deserialize(self, params):
        self.ObjectMode = params.get("ObjectMode")
        if params.get("ObjectItems") is not None:
            self.ObjectItems = []
            for item in params.get("ObjectItems"):
                obj = CompareObjectItem()
                obj._deserialize(item)
                self.ObjectItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObjectItem(AbstractModel):
    """Database/Table objects for data consistency check

    """

    def __init__(self):
        r"""
        :param DbName: The database to be migrated
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param DbMode: Database selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param SchemaName: The schema to be migrated
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param TableMode: Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param Tables: Table configuration for data consistency check, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of CompareTableItem
        :param ViewMode: View selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param Views: View configuration for data consistency check, which is required if `ViewMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of CompareViewItem
        """
        self.DbName = None
        self.DbMode = None
        self.SchemaName = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.DbMode = params.get("DbMode")
        self.SchemaName = params.get("SchemaName")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = CompareTableItem()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = CompareViewItem()
                obj._deserialize(item)
                self.Views.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTableItem(AbstractModel):
    """Table configuration for data consistency check

    """

    def __init__(self):
        r"""
        :param TableName: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskInfo(AbstractModel):
    """Data consistency check result

    """

    def __init__(self):
        r"""
        :param CompareTaskId: Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param Status: Data consistency check result. Valid values: `unstart` (the task is not started); `running` (the task is running); `canceled` (the task is stopped); `failed` (the task failed); `inconsistent` (the data is inconsistent); `consistent` (the data is consistent); `notexist` (the task does not exist).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self.CompareTaskId = None
        self.Status = None


    def _deserialize(self, params):
        self.CompareTaskId = params.get("CompareTaskId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskItem(AbstractModel):
    """Information of the data consistency check object

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param TaskName: Data consistency check task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param Status: Data consistency check task status. Valid values: `created`, `readyRun`, `running`, `success`, `stopping`, `failed`, `canceled`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Config: Data consistency check task configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param CheckProcess: Check details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param CompareProcess: Running details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param Conclusion: Comparison result. Valid values: `same`, `different`, `skipAll`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conclusion: str
        :param CreatedAt: Task creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param StartedAt: Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartedAt: str
        :param FinishedAt: Comparison end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinishedAt: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None
        self.Status = None
        self.Config = None
        self.CheckProcess = None
        self.CompareProcess = None
        self.Conclusion = None
        self.CreatedAt = None
        self.StartedAt = None
        self.FinishedAt = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        self.Status = params.get("Status")
        if params.get("Config") is not None:
            self.Config = CompareObject()
            self.Config._deserialize(params.get("Config"))
        if params.get("CheckProcess") is not None:
            self.CheckProcess = ProcessProgress()
            self.CheckProcess._deserialize(params.get("CheckProcess"))
        if params.get("CompareProcess") is not None:
            self.CompareProcess = ProcessProgress()
            self.CompareProcess._deserialize(params.get("CompareProcess"))
        self.Conclusion = params.get("Conclusion")
        self.CreatedAt = params.get("CreatedAt")
        self.StartedAt = params.get("StartedAt")
        self.FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareViewItem(AbstractModel):
    """View configuration for data consistency check

    """

    def __init__(self):
        r"""
        :param ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        """
        self.ViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        :param CompleteMode: The way to complete the task, which is supported only for legacy MySQL migration tasks. Valid values: `waitForSync` (wait for the source-replica lag to become 0 before stopping); `immediately` (complete immediately without waiting for source-replica sync). Default value: `waitForSync`.
        :type CompleteMode: str
        """
        self.JobId = None
        self.CompleteMode = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfigureSyncJobRequest(AbstractModel):
    """ConfigureSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :type JobId: str
        :param SrcAccessType: Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet); `noProxy`. Note that the valid values are subject to the current link.
        :type SrcAccessType: str
        :param SrcInfo: Source database information
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param DstAccessType: Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet); `noProxy`. Note that the valid values are subject to the current link.
        :type DstAccessType: str
        :param DstInfo: Target database information
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param Options: Sync task options
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param Objects: Information of synced database/table objects
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param JobName: Sync task name
        :type JobName: str
        :param RunMode: Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
        :type RunMode: str
        :param ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `Timed`.
        :type ExpectRunTime: str
        """
        self.JobId = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstInfo = None
        self.Options = None
        self.Objects = None
        self.JobName = None
        self.RunMode = None
        self.ExpectRunTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = Endpoint()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = Endpoint()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("Options") is not None:
            self.Options = Options()
            self.Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self.Objects = Objects()
            self.Objects._deserialize(params.get("Objects"))
        self.JobName = params.get("JobName")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureSyncJobResponse(AbstractModel):
    """ConfigureSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConflictHandleOption(AbstractModel):
    """Detailed description of conflict processing

    """

    def __init__(self):
        r"""
        :param ConditionColumn: Conditionally overwritten column
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionColumn: str
        :param ConditionOperator: Conditional overwrite operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionOperator: str
        :param ConditionOrderInSrcAndDst: Conditional overwrite priority configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionOrderInSrcAndDst: str
        """
        self.ConditionColumn = None
        self.ConditionOperator = None
        self.ConditionOrderInSrcAndDst = None


    def _deserialize(self, params):
        self.ConditionColumn = params.get("ConditionColumn")
        self.ConditionOperator = params.get("ConditionOperator")
        self.ConditionOrderInSrcAndDst = params.get("ConditionOrderInSrcAndDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsistencyOption(AbstractModel):
    """Data consistency check option. Data consistency check is disabled by default.

    """

    def __init__(self):
        r"""
        :param Mode: Data consistency check type. Valid values: `full`, `noCheck`, `notConfigured`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckSyncJobRequest(AbstractModel):
    """CreateCheckSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckSyncJobResponse(AbstractModel):
    """CreateCheckSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCompareTaskRequest(AbstractModel):
    """CreateCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param TaskName: Data consistency check task name. If this parameter is left empty, the value of `CompareTaskId` will be assigned to it.
        :type TaskName: str
        :param ObjectMode: Data comparison object mode. Valid values: `sameAsMigrate` (all migration objects); `custom` (custom mode). Default value: `sameAsMigrate`.
        :type ObjectMode: str
        :param Objects: Configuration of the data consistency check object
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        self.JobId = None
        self.TaskName = None
        self.ObjectMode = None
        self.Objects = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self.Objects = CompareObject()
            self.Objects._deserialize(params.get("Objects"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCompareTaskResponse(AbstractModel):
    """CreateCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CompareTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompareTaskId = params.get("CompareTaskId")
        self.RequestId = params.get("RequestId")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrationServiceRequest(AbstractModel):
    """CreateMigrationService request structure.

    """

    def __init__(self):
        r"""
        :param SrcDatabaseType: Source database type. Valid values: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`.
        :type SrcDatabaseType: str
        :param DstDatabaseType: Target database type. Valid values: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`.
        :type DstDatabaseType: str
        :param SrcRegion: Source instance region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param DstRegion: Target instance region, such as `ap-guangzhou`. Note that it must be the same as the API request region.
        :type DstRegion: str
        :param InstanceClass: Instance specification. Valid values: `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :type InstanceClass: str
        :param Count: Quantity. Value range: [1,15]. Default value: `1`.
        :type Count: int
        :param JobName: Migration task name, which can contain up to 128 characters.
        :type JobName: str
        :param Tags: Tag information
        :type Tags: list of TagItem
        """
        self.SrcDatabaseType = None
        self.DstDatabaseType = None
        self.SrcRegion = None
        self.DstRegion = None
        self.InstanceClass = None
        self.Count = None
        self.JobName = None
        self.Tags = None


    def _deserialize(self, params):
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.SrcRegion = params.get("SrcRegion")
        self.DstRegion = params.get("DstRegion")
        self.InstanceClass = params.get("InstanceClass")
        self.Count = params.get("Count")
        self.JobName = params.get("JobName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationServiceResponse(AbstractModel):
    """CreateMigrationService response structure.

    """

    def __init__(self):
        r"""
        :param JobIds: The list of migration task IDs randomly generated in the format of `dts-c1f6rs21` after a successful order placement
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param PayMode: Billing mode. Valid values: `PrePay` (monthly subscription); `PostPay` (pay-as-you-go). Currently, DTS at Tencent Cloud International is free of charge.
        :type PayMode: str
        :param SrcDatabaseType: Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
        :type SrcDatabaseType: str
        :param SrcRegion: Source database region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param DstDatabaseType: Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
        :type DstDatabaseType: str
        :param DstRegion: Target database region, such as `ap-guangzhou`.
        :type DstRegion: str
        :param Specification: Sync task specification, such as `Standard`.
        :type Specification: str
        :param Tags: Tag information
        :type Tags: list of TagItem
        :param Count: The number of sync tasks purchased at a time. Value range: [1, 10]. Default value: `1`.
        :type Count: int
        :param AutoRenew: Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled). Default value: `0`.
        :type AutoRenew: int
        :param InstanceClass: Sync link specification, such as `micro`, `small`, `medium`, and `large`. Default value: `medium`.
        :type InstanceClass: str
        :param JobName: Sync task name
        :type JobName: str
        :param ExistedJobId: ID of the existing task used to create a similar task
        :type ExistedJobId: str
        """
        self.PayMode = None
        self.SrcDatabaseType = None
        self.SrcRegion = None
        self.DstDatabaseType = None
        self.DstRegion = None
        self.Specification = None
        self.Tags = None
        self.Count = None
        self.AutoRenew = None
        self.InstanceClass = None
        self.JobName = None
        self.ExistedJobId = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcRegion = params.get("SrcRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstRegion = params.get("DstRegion")
        self.Specification = params.get("Specification")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Count = params.get("Count")
        self.AutoRenew = params.get("AutoRenew")
        self.InstanceClass = params.get("InstanceClass")
        self.JobName = params.get("JobName")
        self.ExistedJobId = params.get("ExistedJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param JobIds: Sync task IDs
        :type JobIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        self.RequestId = params.get("RequestId")


class DBEndpointInfo(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param Region: Instance region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param AccessType: Instances network access type. Valid values: `extranet` (public network); `ipv6` (public IPv6); `cvm` (self-build on CVM); `dcg` (Direct Connect); `vpncloud` (VPN access); `cdb` (database); `ccn` (CCN); `intranet` (intranet); `vpc` (VPC). Note that the valid values are subject to the current link.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessType: str
        :param DatabaseType: Database type, such as `mysql`, `redis`, `mongodb`, `postgresql`, `mariadb`, and `percona`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseType: str
        :param NodeType: Node type. Valid values: empty or `simple` (general node); `cluster` (cluster node).
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeType: str
        :param Info: Database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Info: list of DBInfo
        :param Supplier: Instance service provider, such as "aliyun" and "others".
Note: This field may return null, indicating that no valid values can be obtained.
        :type Supplier: str
        :param ExtraAttr: For MongoDB, you can define the following parameters: 	['AuthDatabase':'admin', 
'AuthFlag': "1",	'AuthMechanism':"SCRAM-SHA-1"]
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        """
        self.Region = None
        self.AccessType = None
        self.DatabaseType = None
        self.NodeType = None
        self.Info = None
        self.Supplier = None
        self.ExtraAttr = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.AccessType = params.get("AccessType")
        self.DatabaseType = params.get("DatabaseType")
        self.NodeType = params.get("NodeType")
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = DBInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        self.Supplier = params.get("Supplier")
        if params.get("ExtraAttr") is not None:
            self.ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self.ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInfo(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param Role: Node role in a distributed database, such as the mongos node in MongoDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Role: str
        :param DbKernel: Kernel version, such as the different kernel versions of MariaDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbKernel: str
        :param Host: Instance IP address, which is required for the following access types: public network, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param Port: Instance port, which is required for the following access types: public network, self-build on CVM, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param User: Instance username
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param Password: Instance password
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param UniqVpnGwId: VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpnGwId: str
        :param UniqDcgId: Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqDcgId: str
        :param InstanceId: Database instance ID in the format of `cdb-powiqx8q`, which is required if the access type is `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param CcnGwId: CCN instance ID such as `ccn-afp6kltc`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnGwId: str
        :param VpcId: VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param SubnetId: ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param EngineVersion: Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineVersion: str
        :param Account: Instance account
Note: This field may return null, indicating that no valid values can be obtained.
        :type Account: str
        :param AccountRole: The role used for cross-account migration, which can contain [a-zA-Z0-9\-\_]+.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountRole: str
        :param AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountMode: str
        :param TmpSecretId: ID of the temporary key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretId: str
        :param TmpSecretKey: Key of the temporary key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretKey: str
        :param TmpToken: Temporary token
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpToken: str
        """
        self.Role = None
        self.DbKernel = None
        self.Host = None
        self.Port = None
        self.User = None
        self.Password = None
        self.CvmInstanceId = None
        self.UniqVpnGwId = None
        self.UniqDcgId = None
        self.InstanceId = None
        self.CcnGwId = None
        self.VpcId = None
        self.SubnetId = None
        self.EngineVersion = None
        self.Account = None
        self.AccountRole = None
        self.AccountMode = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.DbKernel = params.get("DbKernel")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.InstanceId = params.get("InstanceId")
        self.CcnGwId = params.get("CcnGwId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EngineVersion = params.get("EngineVersion")
        self.Account = params.get("Account")
        self.AccountRole = params.get("AccountRole")
        self.AccountMode = params.get("AccountMode")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBItem(AbstractModel):
    """Migration object information

    """

    def __init__(self):
        r"""
        :param DbName: Name of the database to be migrated or synced, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param NewDbName: Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewDbName: str
        :param SchemaName: The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param NewSchemaName: Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewSchemaName: str
        :param DBMode: Database selection mode, which is required if `ObjectMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBMode: str
        :param SchemaMode: Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaMode: str
        :param TableMode: Table selection mode, which is required if `DBMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param Tables: The set of table objects, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of TableItem
        :param ViewMode: View selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param Views: The set of view objects, which is required if `ViewMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of ViewItem
        :param RoleMode: Role selection mode, which is exclusive to PostgreSQL. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleMode: str
        :param Roles: Role, which is exclusive to PostgreSQL and required if `RoleMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Roles: list of RoleItem
        :param FunctionMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FunctionMode: str
        :param TriggerMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TriggerMode: str
        :param EventMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventMode: str
        :param ProcedureMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcedureMode: str
        :param Functions: This parameter is required if `FunctionMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Functions: list of str
        :param Procedures: This parameter is required if `ProcedureMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procedures: list of str
        :param Events: This parameter is required if `EventMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of str
        :param Triggers: This parameter is required if `TriggerMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Triggers: list of str
        """
        self.DbName = None
        self.NewDbName = None
        self.SchemaName = None
        self.NewSchemaName = None
        self.DBMode = None
        self.SchemaMode = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None
        self.RoleMode = None
        self.Roles = None
        self.FunctionMode = None
        self.TriggerMode = None
        self.EventMode = None
        self.ProcedureMode = None
        self.Functions = None
        self.Procedures = None
        self.Events = None
        self.Triggers = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.NewDbName = params.get("NewDbName")
        self.SchemaName = params.get("SchemaName")
        self.NewSchemaName = params.get("NewSchemaName")
        self.DBMode = params.get("DBMode")
        self.SchemaMode = params.get("SchemaMode")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = TableItem()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = ViewItem()
                obj._deserialize(item)
                self.Views.append(obj)
        self.RoleMode = params.get("RoleMode")
        if params.get("Roles") is not None:
            self.Roles = []
            for item in params.get("Roles"):
                obj = RoleItem()
                obj._deserialize(item)
                self.Roles.append(obj)
        self.FunctionMode = params.get("FunctionMode")
        self.TriggerMode = params.get("TriggerMode")
        self.EventMode = params.get("EventMode")
        self.ProcedureMode = params.get("ProcedureMode")
        self.Functions = params.get("Functions")
        self.Procedures = params.get("Procedures")
        self.Events = params.get("Events")
        self.Triggers = params.get("Triggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """The database/table objects to be synced

    """

    def __init__(self):
        r"""
        :param DbName: Name of the database to be migrated or synced, which is required if `ObjectMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param NewDbName: Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewDbName: str
        :param DbMode: Database selection mode, which is required if `Mode` is `Partial`. Valid values: `All`, `Partial`. Note that the sync of advanced objects does not depend on this parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param SchemaName: The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param NewSchemaName: Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewSchemaName: str
        :param TableMode: Table selection mode, which is required if `DBMode` is `Partial`. Valid values: `All`, `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param Tables: The set of table objects, which is required if `TableMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of Table
        :param ViewMode: View selection mode. Valid values: `All`, `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param Views: The set of view objects, which is required if `ViewMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of View
        :param FunctionMode: Sync mode. Valid values: `Partial`, `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FunctionMode: str
        :param Functions: This parameter is required if `FunctionMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Functions: list of str
        :param ProcedureMode: Sync mode. Valid values: `Partial`, `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcedureMode: str
        :param Procedures: This parameter is required if `ProcedureMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procedures: list of str
        """
        self.DbName = None
        self.NewDbName = None
        self.DbMode = None
        self.SchemaName = None
        self.NewSchemaName = None
        self.TableMode = None
        self.Tables = None
        self.ViewMode = None
        self.Views = None
        self.FunctionMode = None
        self.Functions = None
        self.ProcedureMode = None
        self.Procedures = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        self.NewDbName = params.get("NewDbName")
        self.DbMode = params.get("DbMode")
        self.SchemaName = params.get("SchemaName")
        self.NewSchemaName = params.get("NewSchemaName")
        self.TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = View()
                obj._deserialize(item)
                self.Views.append(obj)
        self.FunctionMode = params.get("FunctionMode")
        self.Functions = params.get("Functions")
        self.ProcedureMode = params.get("ProcedureMode")
        self.Procedures = params.get("Procedures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTableObject(AbstractModel):
    """Migration object options, which tell DTS which database/table objects should be migrated.

    """

    def __init__(self):
        r"""
        :param ObjectMode: Migration object type. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectMode: str
        :param Databases: Migration object, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Databases: list of DBItem
        :param AdvancedObjects: Advanced object type, such as trigger, function, procedure, and event.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedObjects: list of str
        """
        self.ObjectMode = None
        self.Databases = None
        self.AdvancedObjects = None


    def _deserialize(self, params):
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = DBItem()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdlOption(AbstractModel):
    """DDL statement sync processing during data sync

    """

    def __init__(self):
        r"""
        :param DdlObject: DDL type, such as database, table, view, and index.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlObject: str
        :param DdlValue: DDL value. Valid values: [Create,Drop,Alter] for database <br>[Create,Drop,Alter,Truncate,Rename] for table <br/>[Create,Drop] for view <br/>[Create,Drop] for index
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlValue: list of str
        """
        self.DdlObject = None
        self.DdlValue = None


    def _deserialize(self, params):
        self.DdlObject = params.get("DdlObject")
        self.DdlValue = params.get("DdlValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskRequest(AbstractModel):
    """DeleteCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskResponse(AbstractModel):
    """DeleteCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCheckSyncJobResultRequest(AbstractModel):
    """DescribeCheckSyncJobResult request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSyncJobResultResponse(AbstractModel):
    """DescribeCheckSyncJobResult response structure.

    """

    def __init__(self):
        r"""
        :param Status: Check result
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param StepCount: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCount: int
        :param StepCur: The current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCur: int
        :param Progress: Overall progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param StepInfos: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfos: list of StepInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.StepCount = None
        self.StepCur = None
        self.Progress = None
        self.StepInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StepCount = params.get("StepCount")
        self.StepCur = params.get("StepCur")
        self.Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self.StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self.StepInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCompareReportRequest(AbstractModel):
    """DescribeCompareReport request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Check task ID
        :type CompareTaskId: str
        :param DifferenceLimit: Number of inconsistent objects to be returned
        :type DifferenceLimit: int
        :param DifferenceOffset: Offset of inconsistent objects
        :type DifferenceOffset: int
        :param DifferenceDB: Search criterion: Inconsistent database name
        :type DifferenceDB: str
        :param DifferenceTable: Search criterion: Inconsistent table name
        :type DifferenceTable: str
        :param SkippedLimit: Number of unchecked objects to be returned
        :type SkippedLimit: int
        :param SkippedOffset: Offset of unchecked objects
        :type SkippedOffset: int
        :param SkippedDB: Search criterion: Unchecked database name
        :type SkippedDB: str
        :param SkippedTable: Search criterion: Unchecked table name
        :type SkippedTable: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.DifferenceLimit = None
        self.DifferenceOffset = None
        self.DifferenceDB = None
        self.DifferenceTable = None
        self.SkippedLimit = None
        self.SkippedOffset = None
        self.SkippedDB = None
        self.SkippedTable = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.DifferenceLimit = params.get("DifferenceLimit")
        self.DifferenceOffset = params.get("DifferenceOffset")
        self.DifferenceDB = params.get("DifferenceDB")
        self.DifferenceTable = params.get("DifferenceTable")
        self.SkippedLimit = params.get("SkippedLimit")
        self.SkippedOffset = params.get("SkippedOffset")
        self.SkippedDB = params.get("SkippedDB")
        self.SkippedTable = params.get("SkippedTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareReportResponse(AbstractModel):
    """DescribeCompareReport response structure.

    """

    def __init__(self):
        r"""
        :param Abstract: Summary information of data consistency check
Note: This field may return null, indicating that no valid values can be obtained.
        :type Abstract: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        :param Detail: Data consistency check details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Abstract = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Abstract") is not None:
            self.Abstract = CompareAbstractInfo()
            self.Abstract._deserialize(params.get("Abstract"))
        if params.get("Detail") is not None:
            self.Detail = CompareDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeCompareTasksRequest(AbstractModel):
    """DescribeCompareTasks request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param Limit: Number of tasks to be displayed per page. Default value: `20`.
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareTasksResponse(AbstractModel):
    """DescribeCompareTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Items: List of data consistency check tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of CompareTaskItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CompareTaskItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrateDBInstancesRequest(AbstractModel):
    """DescribeMigrateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param DatabaseType: Database type, such as `mysql`.
        :type DatabaseType: str
        :param MigrateRole: Specifies whether the instance is the migration source or target. Valid values: `src` (source); `dts` (target).
        :type MigrateRole: str
        :param InstanceId: Database instance ID
        :type InstanceId: str
        :param InstanceName: Database instance name
        :type InstanceName: str
        :param Limit: Number of results to be returned
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        :param AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
        :type AccountMode: str
        :param TmpSecretId: ID of the temporary key, which is required if the operation is performed across accounts.
        :type TmpSecretId: str
        :param TmpSecretKey: Key of the temporary key, which is required if the operation is performed across accounts.
        :type TmpSecretKey: str
        :param TmpToken: Temporary token, which is required if the operation is performed across accounts.
        :type TmpToken: str
        """
        self.DatabaseType = None
        self.MigrateRole = None
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.AccountMode = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None


    def _deserialize(self, params):
        self.DatabaseType = params.get("DatabaseType")
        self.MigrateRole = params.get("MigrateRole")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.AccountMode = params.get("AccountMode")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateDBInstancesResponse(AbstractModel):
    """DescribeMigrateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Instances: Instance list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Instances: list of MigrateDBItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = MigrateDBItem()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationCheckJobRequest(AbstractModel):
    """DescribeMigrationCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationCheckJobResponse(AbstractModel):
    """DescribeMigrationCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param Status: Check task execution status. Valid values: `notStarted`, `running`, `failed`, `success`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param BriefMsg: Check task result message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param StepInfo: Check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: list of CheckStep
        :param CheckFlag: Check result. Valid values: `checkPass`, `checkNotPass`.
        :type CheckFlag: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.BriefMsg = None
        self.StepInfo = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.BriefMsg = params.get("BriefMsg")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = CheckStep()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param JobName: Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param CreateTime: Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param StartTime: Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param EndTime: Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param BriefMsg: Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param Status: Task status. Valid values: `created`, `checking`, `checkPass`, `checkNotPass`, `readyRun`, `running`, `readyComplete`, `success`, `failed`, `stopping`, `completing`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Action: Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param StepInfo: Information of the migration task execution process. The check and migration step information will be displayed in the check and migration stages respectively.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param SrcInfo: Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param CompareTask: Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param RunMode: Running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param MigrateOption: Migration options, which describe how the task performs migration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param CheckStepInfo: Check task running details
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckStepInfo: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        :param TradeInfo: Billing information
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param ErrorInfo: Task error information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: list of ErrorInfoItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.BriefMsg = None
        self.Status = None
        self.Action = None
        self.StepInfo = None
        self.SrcInfo = None
        self.DstInfo = None
        self.CompareTask = None
        self.Tags = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.MigrateOption = None
        self.CheckStepInfo = None
        self.TradeInfo = None
        self.ErrorInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BriefMsg = params.get("BriefMsg")
        self.Status = params.get("Status")
        if params.get("Action") is not None:
            self.Action = MigrateAction()
            self.Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self.StepInfo = MigrateDetailInfo()
            self.StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self.CompareTask = CompareTaskInfo()
            self.CompareTask._deserialize(params.get("CompareTask"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("CheckStepInfo") is not None:
            self.CheckStepInfo = CheckStepInfo()
            self.CheckStepInfo._deserialize(params.get("CheckStepInfo"))
        if params.get("TradeInfo") is not None:
            self.TradeInfo = TradeInfo()
            self.TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("ErrorInfo") is not None:
            self.ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfoItem()
                obj._deserialize(item)
                self.ErrorInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationJobsRequest(AbstractModel):
    """DescribeMigrationJobs request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID such as `dts-amm1jw5q`
        :type JobId: str
        :param JobName: Data migration task name
        :type JobName: str
        :param Status: Data migration task status. Valid values: `created`, `checking`, `checkPass`, `checkNotPass`, `readyRun`, `running`, `readyComplete`, `success`, `failed`, `stopping`, `completing`.
        :type Status: list of str
        :param SrcInstanceId: Source instance ID in the format of `cdb-c1nl9rpv`
        :type SrcInstanceId: str
        :param SrcRegion: Source instance region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param SrcDatabaseType: Source database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :type SrcDatabaseType: list of str
        :param SrcAccessType: Source instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :type SrcAccessType: list of str
        :param DstInstanceId: Target instance ID in the format of `cdb-c1nl9rpv`
        :type DstInstanceId: str
        :param DstRegion: Target instance region, such as `ap-guangzhou`.
        :type DstRegion: str
        :param DstDatabaseType: Target database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :type DstDatabaseType: list of str
        :param DstAccessType: Target instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :type DstAccessType: list of str
        :param RunMode: Task running mode. Valid values: `immediate`, `timed`.
        :type RunMode: str
        :param OrderSeq: Sorting order. Valid values: `asc`, `desc`. Default value: `desc` by creation time.
        :type OrderSeq: str
        :param Limit: Number of instances to be returned. Value range: [1,100]. Default value: `20`.
        :type Limit: int
        :param Offset: Offset. Default value: `0`.
        :type Offset: int
        :param TagFilters: Tag filter
        :type TagFilters: list of TagFilter
        """
        self.JobId = None
        self.JobName = None
        self.Status = None
        self.SrcInstanceId = None
        self.SrcRegion = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.DstInstanceId = None
        self.DstRegion = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.RunMode = None
        self.OrderSeq = None
        self.Limit = None
        self.Offset = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Status = params.get("Status")
        self.SrcInstanceId = params.get("SrcInstanceId")
        self.SrcRegion = params.get("SrcRegion")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        self.DstInstanceId = params.get("DstInstanceId")
        self.DstRegion = params.get("DstRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        self.RunMode = params.get("RunMode")
        self.OrderSeq = params.get("OrderSeq")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationJobsResponse(AbstractModel):
    """DescribeMigrationJobs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of migration tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param JobList: Migration task list
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobList: list of JobItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = JobItem()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID, such as `sync-werwfs23`.
        :type JobId: str
        :param JobName: Sync task name
        :type JobName: str
        :param Order: Sort by field, such as `CreateTime`.
        :type Order: str
        :param OrderSeq: Sorting order. Valid values: `ASC`, `DESC`. Default value: `DESC` by `CreateTime`.
        :type OrderSeq: str
        :param Offset: Offset. Default value: `0`.
        :type Offset: int
        :param Limit: Number of sync task instances to be returned. Value range: [1,100]. Default value: `20`.
        :type Limit: int
        :param Status: The set of status values, such as `Initialized,CheckPass,Running,ResumableErr,Stopped`.
        :type Status: list of str
        :param RunMode: Running mode. Valid values: `Immediate`, `Timed`.
        :type RunMode: str
        :param JobType: Task type, such as `mysql2mysql` (sync from MySQL to MySQL).
        :type JobType: str
        :param PayMode: Billing mode. Valid values: `PrePay` (prepaid); `PostPay` (postpaid).
        :type PayMode: str
        :param TagFilters: tag
        :type TagFilters: list of TagFilter
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.RunMode = None
        self.JobType = None
        self.PayMode = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.RunMode = params.get("RunMode")
        self.JobType = params.get("JobType")
        self.PayMode = params.get("PayMode")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param JobList: Array of task details
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobList: list of SyncJobInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyMigrateJobRequest(AbstractModel):
    """DestroyMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyMigrateJobResponse(AbstractModel):
    """DestroyMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroySyncJobRequest(AbstractModel):
    """DestroySyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySyncJobResponse(AbstractModel):
    """DestroySyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetailCheckItem(AbstractModel):
    """Specific check item in this check step

    """

    def __init__(self):
        r"""
        :param CheckItemName: Check item name, such as source database permission check.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckItemName: str
        :param Description: Check item details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param CheckResult: Check item result. Valid values: `pass` (pass); `failed` (failure); `warning` (pass with warning).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckResult: str
        :param FailureReason: The cause of the check item failure
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailureReason: str
        :param Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param ErrorLog: Execution error log
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLog: list of str
        :param HelpDoc: URL of the detailed help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: list of str
        :param SkipInfo: Prompt text for ignoring a risk
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkipInfo: str
        """
        self.CheckItemName = None
        self.Description = None
        self.CheckResult = None
        self.FailureReason = None
        self.Solution = None
        self.ErrorLog = None
        self.HelpDoc = None
        self.SkipInfo = None


    def _deserialize(self, params):
        self.CheckItemName = params.get("CheckItemName")
        self.Description = params.get("Description")
        self.CheckResult = params.get("CheckResult")
        self.FailureReason = params.get("FailureReason")
        self.Solution = params.get("Solution")
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        self.SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceDetail(AbstractModel):
    """Details of inconsistent tables

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Items: Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of DifferenceItem
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DifferenceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceItem(AbstractModel):
    """Details of inconsistent tables

    """

    def __init__(self):
        r"""
        :param Db: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Db: str
        :param Table: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param Chunk: Chunk ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Chunk: int
        :param SrcItem: Source database value
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcItem: str
        :param DstItem: Target database value
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstItem: str
        :param IndexName: Index name
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexName: str
        :param LowerBoundary: First index key
Note: This field may return null, indicating that no valid values can be obtained.
        :type LowerBoundary: str
        :param UpperBoundary: Last index key
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpperBoundary: str
        :param CostTime: Comparison time in ms
Note: This field may return null, indicating that no valid values can be obtained.
        :type CostTime: float
        :param FinishedAt: Completion time
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinishedAt: str
        """
        self.Db = None
        self.Table = None
        self.Chunk = None
        self.SrcItem = None
        self.DstItem = None
        self.IndexName = None
        self.LowerBoundary = None
        self.UpperBoundary = None
        self.CostTime = None
        self.FinishedAt = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        self.Chunk = params.get("Chunk")
        self.SrcItem = params.get("SrcItem")
        self.DstItem = params.get("DstItem")
        self.IndexName = params.get("IndexName")
        self.LowerBoundary = params.get("LowerBoundary")
        self.UpperBoundary = params.get("UpperBoundary")
        self.CostTime = params.get("CostTime")
        self.FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endpoint(AbstractModel):
    """Information of the source and target databases in data sync

    """

    def __init__(self):
        r"""
        :param Region: Region name, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param DbKernel: Database kernel type, which is used to distinguish between different kernels in TDSQL. Valid values: `percona`, `mariadb`, `mysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbKernel: str
        :param InstanceId: Database instance ID in the format of `cdb-powiqx8q`
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param Ip: Instance IP address, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param Port: Instance port, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param User: Username, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param Password: Password, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param DbName: Database name, which is required if the database type is `cdwpg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param VpcId: VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param SubnetId: ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param UniqDcgId: Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqDcgId: str
        :param UniqVpnGwId: VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpnGwId: str
        :param CcnId: CCN instance ID in the format of `ccn-afp6kltc`, which is required if the access type is `ccn`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnId: str
        :param Supplier: Cloud vendor type. For Alibaba Cloud ApsaraDB for RDS instances, enter `aliyun`; otherwise, enter `others`. Default value: `others`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Supplier: str
        :param EngineVersion: Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineVersion: str
        :param AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountMode: str
        :param Account: Instance account, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Account: str
        :param AccountRole: The role used for cross-account sync, which can contain [a-zA-Z0-9\-\_]+ and is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountRole: str
        :param TmpSecretId: ID of the temporary key, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretId: str
        :param TmpSecretKey: Key of the temporary key, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretKey: str
        :param TmpToken: Temporary token, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpToken: str
        :param RoleExternalId: External role ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleExternalId: str
        """
        self.Region = None
        self.DbKernel = None
        self.InstanceId = None
        self.Ip = None
        self.Port = None
        self.User = None
        self.Password = None
        self.DbName = None
        self.VpcId = None
        self.SubnetId = None
        self.CvmInstanceId = None
        self.UniqDcgId = None
        self.UniqVpnGwId = None
        self.CcnId = None
        self.Supplier = None
        self.EngineVersion = None
        self.AccountMode = None
        self.Account = None
        self.AccountRole = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.TmpToken = None
        self.RoleExternalId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.DbKernel = params.get("DbKernel")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.CcnId = params.get("CcnId")
        self.Supplier = params.get("Supplier")
        self.EngineVersion = params.get("EngineVersion")
        self.AccountMode = params.get("AccountMode")
        self.Account = params.get("Account")
        self.AccountRole = params.get("AccountRole")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.TmpToken = params.get("TmpToken")
        self.RoleExternalId = params.get("RoleExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfoItem(AbstractModel):
    """Task error information

    """

    def __init__(self):
        r"""
        :param Code: Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param ErrorLog: Error log
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLog: str
        :param HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        """
        self.Code = None
        self.Solution = None
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Solution = params.get("Solution")
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobRequest(AbstractModel):
    """IsolateMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobResponse(AbstractModel):
    """IsolateMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IsolateSyncJobRequest(AbstractModel):
    """IsolateSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSyncJobResponse(AbstractModel):
    """IsolateSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class JobItem(AbstractModel):
    """Migration task list

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param JobName: Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param CreateTime: Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param StartTime: Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param EndTime: Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param BriefMsg: Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param Status: Task status. Valid values: `creating`, `created`, `checking`, `checkPass`, `checkNotPass`, `readyRun`, `running`, `readyComplete`, `success`, `failed`, `stopping`, `completing`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param RunMode: Task running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param ExpectRunTime: Expected start time in the format of "2022-07-11 16:20:49", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param Action: Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param StepInfo: Information of the migration task execution process
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param SrcInfo: Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param CompareTask: Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param TradeInfo: Billing status information
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        """
        self.JobId = None
        self.JobName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.BriefMsg = None
        self.Status = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.Action = None
        self.StepInfo = None
        self.SrcInfo = None
        self.DstInfo = None
        self.CompareTask = None
        self.TradeInfo = None
        self.Tags = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BriefMsg = params.get("BriefMsg")
        self.Status = params.get("Status")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Action") is not None:
            self.Action = MigrateAction()
            self.Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self.StepInfo = MigrateDetailInfo()
            self.StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self.CompareTask = CompareTaskInfo()
            self.CompareTask._deserialize(params.get("CompareTask"))
        if params.get("TradeInfo") is not None:
            self.TradeInfo = TradeInfo()
            self.TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePairOption(AbstractModel):
    """Additional configuration information

    """

    def __init__(self):
        r"""
        :param Key: Option key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param Value: Option value
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
        


class MigrateAction(AbstractModel):
    """Task operation information, which contains the list of all operations in the migration task as well as the list of allowed operations under the current status.

    """

    def __init__(self):
        r"""
        :param AllAction: List of all operations in the task
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllAction: list of str
        :param AllowedAction: List of allowed operations in the task under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllowedAction: list of str
        """
        self.AllAction = None
        self.AllowedAction = None


    def _deserialize(self, params):
        self.AllAction = params.get("AllAction")
        self.AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDBItem(AbstractModel):
    """Object in the migration task instance list

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Vip: Instance VIP
        :type Vip: str
        :param Vport: Instance Vport
        :type Vport: int
        :param Usable: Whether the instance can be migrated. Valid values: `1 (yes); `0` (no).
        :type Usable: int
        :param Hint: The cause why the instance cannot be migrated
        :type Hint: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.Usable = None
        self.Hint = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Usable = params.get("Usable")
        self.Hint = params.get("Hint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetailInfo(AbstractModel):
    """Information of the migration task execution process

    """

    def __init__(self):
        r"""
        :param StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param MasterSlaveDistance: Source-replica lag in MB. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: Source-replica lag in seconds. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecondsBehindMaster: int
        :param StepInfo: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: list of StepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """Migration options, which describe how the task performs migration.

    """

    def __init__(self):
        r"""
        :param DatabaseTable: Migration object options, which tell DTS which database/table objects should be migrated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseTable: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        :param MigrateType: Migration type. Valid values: `full`, `structure`, `fullAndIncrement`. Default value: `fullAndIncrement`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrateType: str
        :param Consistency: Data consistency check option. Data consistency check is disabled by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Consistency: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        :param IsMigrateAccount: Whether to migrate accounts. Valid values: `yes`, `no`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMigrateAccount: bool
        :param IsOverrideRoot: Whether to use the `Root` account in the source database to overwrite that in the target database. Valid values: `false`, `true`. For database/table or structural migration, you should specify `false`. Note that this parameter takes effect only for OldDTS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsOverrideRoot: bool
        :param IsDstReadOnly: Whether to set the target database to read-only during migration, which takes effect only for MySQL databases. Valid values: `true`, `false`. Default value: `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDstReadOnly: bool
        :param ExtraAttr: Additional information. You can set additional parameters for certain database types. For Redis, you can define the following parameters: 
["ClientOutputBufferHardLimit":512, 	Hard limit of the replica buffer zone capacity in MB	"ClientOutputBufferSoftLimit":512, 	Soft limit of the replica buffer zone capacity in MB	"ClientOutputBufferPersistTime":60, Soft limit duration of the replica buffer zone in seconds	"ReplBacklogSize":512, 	Limit of the circular buffer zone capacity in MB	"ReplTimeout":120, 		Replication timeout period in seconds]
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        """
        self.DatabaseTable = None
        self.MigrateType = None
        self.Consistency = None
        self.IsMigrateAccount = None
        self.IsOverrideRoot = None
        self.IsDstReadOnly = None
        self.ExtraAttr = None


    def _deserialize(self, params):
        if params.get("DatabaseTable") is not None:
            self.DatabaseTable = DatabaseTableObject()
            self.DatabaseTable._deserialize(params.get("DatabaseTable"))
        self.MigrateType = params.get("MigrateType")
        if params.get("Consistency") is not None:
            self.Consistency = ConsistencyOption()
            self.Consistency._deserialize(params.get("Consistency"))
        self.IsMigrateAccount = params.get("IsMigrateAccount")
        self.IsOverrideRoot = params.get("IsOverrideRoot")
        self.IsDstReadOnly = params.get("IsDstReadOnly")
        if params.get("ExtraAttr") is not None:
            self.ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self.ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameRequest(AbstractModel):
    """ModifyCompareTaskName request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        :param TaskName: Data consistency check task name
        :type TaskName: str
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameResponse(AbstractModel):
    """ModifyCompareTaskName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCompareTaskRequest(AbstractModel):
    """ModifyCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        :param TaskName: Task name
        :type TaskName: str
        :param ObjectMode: Data comparison object mode. Valid values: `sameAsMigrate` (all migration objects); `custom` (custom mode). Default value: `sameAsMigrate`.
        :type ObjectMode: str
        :param Objects: Compared object, which is required if `CompareObjectMode` is `custom`.
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        self.JobId = None
        self.CompareTaskId = None
        self.TaskName = None
        self.ObjectMode = None
        self.Objects = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        self.TaskName = params.get("TaskName")
        self.ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self.Objects = CompareObject()
            self.Objects._deserialize(params.get("Objects"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskResponse(AbstractModel):
    """ModifyCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrateJobSpecRequest(AbstractModel):
    """ModifyMigrateJobSpec request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param NewInstanceClass: New instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :type NewInstanceClass: str
        """
        self.JobId = None
        self.NewInstanceClass = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobSpecResponse(AbstractModel):
    """ModifyMigrateJobSpec response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrateNameRequest(AbstractModel):
    """ModifyMigrateName request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param JobName: New migration task name
        :type JobName: str
        """
        self.JobId = None
        self.JobName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateNameResponse(AbstractModel):
    """ModifyMigrateName response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationJobRequest(AbstractModel):
    """ModifyMigrationJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param RunMode: Running mode. Valid values: `immediate`, `timed`.
        :type RunMode: str
        :param MigrateOption: Migration task configuration options, which describe how the task performs migration.
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param SrcInfo: Source instance information
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param DstInfo: Target instance information
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param JobName: Migration task name, which can contain up to 128 characters.
        :type JobName: str
        :param ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
        :type ExpectRunTime: str
        :param Tags: Tag information
        :type Tags: list of TagItem
        """
        self.JobId = None
        self.RunMode = None
        self.MigrateOption = None
        self.SrcInfo = None
        self.DstInfo = None
        self.JobName = None
        self.ExpectRunTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RunMode = params.get("RunMode")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DBEndpointInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DBEndpointInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.JobName = params.get("JobName")
        self.ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationJobResponse(AbstractModel):
    """ModifyMigrationJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Objects(AbstractModel):
    """Description of synced database objects

    """

    def __init__(self):
        r"""
        :param Mode: Migration object type, such as `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        :param Databases: Sync object, which is required if `Mode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Databases: list of Database
        :param AdvancedObjects: Advanced object type, such as function and procedure. If you need to sync advanced objects, the initialization type must include structure initialization; that is, `Options.InitType` must be `Structure` or `Full`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedObjects: list of str
        """
        self.Mode = None
        self.Databases = None
        self.AdvancedObjects = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Options(AbstractModel):
    """Data sync options

    """

    def __init__(self):
        r"""
        :param InitType: Sync initialization option. Valid values: `data` (full data initialization); `Structure` (structure initialization); `Full` (full data and structure initialization); `None` (incremental data only). Default value: `Full`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitType: str
        :param DealOfExistSameTable: Processing method for duplicate tables. Valid values: `ReportErrorAfterCheck`, `InitializeAfterDelete`, `ExecuteAfterIgnore`. Default value: `ReportErrorAfterCheck`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealOfExistSameTable: str
        :param ConflictHandleType: Conflict processing option. Valid values: `ReportError` (report an error); `Ignore` (ignore); `Cover` (overwrite); `ConditionCover` (conditionally overwrite). Default value: `ReportError`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleType: str
        :param AddAdditionalColumn: Whether to add the additional column
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddAdditionalColumn: bool
        :param OpTypes: DML and DDL options to be synced. Valid values: `Insert` (INSERT operations); `Update` (UPDATE operations); `Delete` (DELETE operations); `DDL` (structure sync); `PartialDDL` (custom option, which is used together with `DdlOptions`). You can also leave this parameter empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpTypes: list of str
        :param ConflictHandleOption: Detailed option for conflict processing, such as condition rows and operations in conditional overwrite.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param DdlOptions: DDL statements to be synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlOptions: list of DdlOption
        """
        self.InitType = None
        self.DealOfExistSameTable = None
        self.ConflictHandleType = None
        self.AddAdditionalColumn = None
        self.OpTypes = None
        self.ConflictHandleOption = None
        self.DdlOptions = None


    def _deserialize(self, params):
        self.InitType = params.get("InitType")
        self.DealOfExistSameTable = params.get("DealOfExistSameTable")
        self.ConflictHandleType = params.get("ConflictHandleType")
        self.AddAdditionalColumn = params.get("AddAdditionalColumn")
        self.OpTypes = params.get("OpTypes")
        if params.get("ConflictHandleOption") is not None:
            self.ConflictHandleOption = ConflictHandleOption()
            self.ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        if params.get("DdlOptions") is not None:
            self.DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self.DdlOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessProgress(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
        :param Status: Step status. Valid values: `notStarted`, `running`, `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Percent: Progress information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param Message: The prompt output in the current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Steps: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Steps: list of StepDetailInfo
        """
        self.Status = None
        self.Percent = None
        self.StepAll = None
        self.StepNow = None
        self.Message = None
        self.Steps = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Message = params.get("Message")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self.Steps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStepTip(AbstractModel):
    """Object of the error or warning information

    """

    def __init__(self):
        r"""
        :param Message: Prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        """
        self.Message = None
        self.Solution = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Solution = params.get("Solution")
        self.HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobRequest(AbstractModel):
    """RecoverMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobResponse(AbstractModel):
    """RecoverMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecoverSyncJobRequest(AbstractModel):
    """RecoverSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverSyncJobResponse(AbstractModel):
    """RecoverSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeSyncJobRequest(AbstractModel):
    """ResizeSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        :param NewInstanceClass: Task specification
        :type NewInstanceClass: str
        """
        self.JobId = None
        self.NewInstanceClass = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeSyncJobResponse(AbstractModel):
    """ResizeSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeMigrateJobRequest(AbstractModel):
    """ResumeMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        :param ResumeOption: Task resumption mode. Valid values: `clearData` (clear the target instance data); `overwrite` (execute the task in overwrite mode); `normal` (follow the normal process without performing additional operations).
        :type ResumeOption: str
        """
        self.JobId = None
        self.ResumeOption = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.ResumeOption = params.get("ResumeOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeMigrateJobResponse(AbstractModel):
    """ResumeMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeSyncJobRequest(AbstractModel):
    """ResumeSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSyncJobResponse(AbstractModel):
    """ResumeSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleItem(AbstractModel):
    """Role object, which is exclusive to PostgreSQL.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleName: str
        :param NewRoleName: Role name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewRoleName: str
        """
        self.RoleName = None
        self.NewRoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.NewRoleName = params.get("NewRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkippedDetail(AbstractModel):
    """Details of skipped tables

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Items: Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of SkippedItem
        """
        self.TotalCount = None
        self.Items = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SkippedItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkippedItem(AbstractModel):
    """Details of skipped tables

    """

    def __init__(self):
        r"""
        :param Db: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Db: str
        :param Table: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param Reason: The cause why check is not initiated
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self.Db = None
        self.Table = None
        self.Reason = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareRequest(AbstractModel):
    """StartCompare request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareResponse(AbstractModel):
    """StartCompare response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StepDetailInfo(AbstractModel):
    """Step information

    """

    def __init__(self):
        r"""
        :param StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param StepId: Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param Status: Step status. Valid values: `success`, `failed`, `running`, `notStarted`. Default value: `notStarted`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param StartTime: Start time of the current step in the format of "yyyy-mm-dd hh:mm:ss". If this field does not exist or is empty, it is meaningless.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param StepMessage: Step error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepMessage: str
        :param Percent: Execution progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param Errors: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of ProcessStepTip
        :param Warnings: Warning
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warnings: list of ProcessStepTip
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None
        self.StepMessage = None
        self.Percent = None
        self.Errors = None
        self.Warnings = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.StepMessage = params.get("StepMessage")
        self.Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self.Errors = []
            for item in params.get("Errors"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self.Errors.append(obj)
        if params.get("Warnings") is not None:
            self.Warnings = []
            for item in params.get("Warnings"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self.Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepInfo(AbstractModel):
    """Step details

    """

    def __init__(self):
        r"""
        :param StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param StepId: Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param Status: Current status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param StartTime: Step start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param Errors: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of StepTip
        :param Warnings: Warning message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warnings: list of StepTip
        :param Progress: Progress of the current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None
        self.Errors = None
        self.Warnings = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        if params.get("Errors") is not None:
            self.Errors = []
            for item in params.get("Errors"):
                obj = StepTip()
                obj._deserialize(item)
                self.Errors.append(obj)
        if params.get("Warnings") is not None:
            self.Warnings = []
            for item in params.get("Warnings"):
                obj = StepTip()
                obj._deserialize(item)
                self.Warnings.append(obj)
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepTip(AbstractModel):
    """Error or warning information in the current step

    """

    def __init__(self):
        r"""
        :param Code: Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        :param SkipInfo: Whether the current step is skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkipInfo: str
        """
        self.Code = None
        self.Message = None
        self.Solution = None
        self.HelpDoc = None
        self.SkipInfo = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.Solution = params.get("Solution")
        self.HelpDoc = params.get("HelpDoc")
        self.SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareRequest(AbstractModel):
    """StopCompare request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Migration task ID
        :type JobId: str
        :param CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self.JobId = None
        self.CompareTaskId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareResponse(AbstractModel):
    """StopCompare response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Data migration task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopSyncJobRequest(AbstractModel):
    """StopSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSyncJobResponse(AbstractModel):
    """StopSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncDetailInfo(AbstractModel):
    """Step information of the sync task

    """

    def __init__(self):
        r"""
        :param StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param Progress: Overall progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param CurrentStepProgress: Progress of the current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentStepProgress: int
        :param MasterSlaveDistance: Data volume difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: Time difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecondsBehindMaster: int
        :param Message: Overall description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param StepInfos: Step details
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfos: list of StepInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.Message = None
        self.StepInfos = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        self.Message = params.get("Message")
        if params.get("StepInfos") is not None:
            self.StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self.StepInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncJobInfo(AbstractModel):
    """Sync task information

    """

    def __init__(self):
        r"""
        :param JobId: Sync task ID, such as `sync-btso140`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param JobName: Sync task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param PayMode: Billing mode. Valid values: `PostPay` (pay-as-you-go); `PrePay` (monthly subscription).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param RunMode: Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param ExpectRunTime: Expected execution time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param AllActions: All supported operations
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllActions: list of str
        :param Actions: Operations that can be performed under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Actions: list of str
        :param Options: Sync options
Note: This field may return null, indicating that no valid values can be obtained.
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param Objects: Sync database/table objects
Note: This field may return null, indicating that no valid values can be obtained.
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param Specification: Task specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type Specification: str
        :param ExpireTime: Expiration time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param SrcRegion: Source database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcRegion: str
        :param SrcDatabaseType: Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcDatabaseType: str
        :param SrcAccessType: Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcAccessType: str
        :param SrcInfo: Source database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param DstRegion: Target database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstRegion: str
        :param DstDatabaseType: Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstDatabaseType: str
        :param DstAccessType: Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstAccessType: str
        :param DstInfo: Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param CreateTime: Creation time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param StartTime: Start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param Status: Task status. Valid values: `UnInitialized`, `Initialized`, `Checking`, `CheckPass`, `CheckNotPass`, `ReadyRunning`, `Running`, `Pausing`, `Paused`, `Stopping`, `Stopped`, `ResumableErr`, `Resuming`, `Failed`, `Released`, `Resetting`, `Unknown`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param EndTime: End time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param Detail: Step information of the sync task
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        :param TradeStatus: Billing status. Valid values: `Normal`, `Resizing`, `Renewing`, `Isolating`, `Isolated`, `Offlining`, `Offlined`, `NotBilled`, `Recovering`, `PostPay2Prepaying`, `PrePay2Postpaying`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeStatus: str
        :param InstanceClass: Sync link specification, such as `micro`, `small`, `medium`, and `large`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceClass: str
        :param AutoRenew: Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenew: int
        :param OfflineTime: Deletion time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        """
        self.JobId = None
        self.JobName = None
        self.PayMode = None
        self.RunMode = None
        self.ExpectRunTime = None
        self.AllActions = None
        self.Actions = None
        self.Options = None
        self.Objects = None
        self.Specification = None
        self.ExpireTime = None
        self.SrcRegion = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstRegion = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.Status = None
        self.EndTime = None
        self.Tags = None
        self.Detail = None
        self.TradeStatus = None
        self.InstanceClass = None
        self.AutoRenew = None
        self.OfflineTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.PayMode = params.get("PayMode")
        self.RunMode = params.get("RunMode")
        self.ExpectRunTime = params.get("ExpectRunTime")
        self.AllActions = params.get("AllActions")
        self.Actions = params.get("Actions")
        if params.get("Options") is not None:
            self.Options = Options()
            self.Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self.Objects = Objects()
            self.Objects._deserialize(params.get("Objects"))
        self.Specification = params.get("Specification")
        self.ExpireTime = params.get("ExpireTime")
        self.SrcRegion = params.get("SrcRegion")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = Endpoint()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstRegion = params.get("DstRegion")
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = Endpoint()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.Status = params.get("Status")
        self.EndTime = params.get("EndTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Detail") is not None:
            self.Detail = SyncDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.TradeStatus = params.get("TradeStatus")
        self.InstanceClass = params.get("InstanceClass")
        self.AutoRenew = params.get("AutoRenew")
        self.OfflineTime = params.get("OfflineTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """Synced table description

    """

    def __init__(self):
        r"""
        :param TableName: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param NewTableName: New table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        :param FilterCondition: Filter condition
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilterCondition: str
        """
        self.TableName = None
        self.NewTableName = None
        self.FilterCondition = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        self.FilterCondition = params.get("FilterCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableItem(AbstractModel):
    """The set of table objects, which is required if `TableMode` is `partial`.

    """

    def __init__(self):
        r"""
        :param TableName: Name of the table to be migrated
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param NewTableName: Name of the table after migration, which is required if `TableEditMode` is `rename`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        :param TmpTables: Temp table to be migrated, which is required if `TableEditMode` is `pt`. To sync temp tables that may be generated during migration by tools such as pt-online-schema-change, you can use this parameter to configure the temp table names.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpTables: list of str
        :param TableEditMode: Table editing type. Valid values: `rename` (table mapping); `pt` (additional table sync).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableEditMode: str
        """
        self.TableName = None
        self.NewTableName = None
        self.TmpTables = None
        self.TableEditMode = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        self.TmpTables = params.get("TmpTables")
        self.TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filter

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeInfo(AbstractModel):
    """Billing status information

    """

    def __init__(self):
        r"""
        :param DealName: Order number
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param LastDealName: Last order number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastDealName: str
        :param InstanceClass: Instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceClass: str
        :param TradeStatus: Task billing status. Valid values: `normal` (billed or to be billed); `resizing` (adjusting configuration); `reversing` (topping up, which is a short status); `isolating` (isolating, which is a short status); `isolated` (isolated); `offlining` (deleting); `offlined` (deleted); `notBilled` (not billed).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeStatus: str
        :param ExpireTime: Expiration time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param OfflineTime: Deletion time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        :param IsolateTime: Isolation time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateTime: str
        :param OfflineReason: The cause of deletion
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineReason: str
        :param IsolateReason: The cause of isolation
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateReason: str
        :param PayType: Billing mode. Valid values: `postpay` (postpaid); `prepay` (prepaid).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayType: str
        :param BillingType: Task billing type. Valid values: `billing` (billed); `notBilling` (free); `promotions` (in promotion).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingType: str
        """
        self.DealName = None
        self.LastDealName = None
        self.InstanceClass = None
        self.TradeStatus = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.IsolateTime = None
        self.OfflineReason = None
        self.IsolateReason = None
        self.PayType = None
        self.BillingType = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.LastDealName = params.get("LastDealName")
        self.InstanceClass = params.get("InstanceClass")
        self.TradeStatus = params.get("TradeStatus")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.IsolateTime = params.get("IsolateTime")
        self.OfflineReason = params.get("OfflineReason")
        self.IsolateReason = params.get("IsolateReason")
        self.PayType = params.get("PayType")
        self.BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class View(AbstractModel):
    """Synced view description

    """

    def __init__(self):
        r"""
        :param ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        :param NewViewName: New view name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewViewName: str
        """
        self.ViewName = None
        self.NewViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        self.NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewItem(AbstractModel):
    """View object

    """

    def __init__(self):
        r"""
        :param ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        :param NewViewName: View name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewViewName: str
        """
        self.ViewName = None
        self.NewViewName = None


    def _deserialize(self, params):
        self.ViewName = params.get("ViewName")
        self.NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        