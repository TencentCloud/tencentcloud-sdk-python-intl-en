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


class CheckStep(AbstractModel):
    """Check step

    """

    def __init__(self):
        r"""
        :param _StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param _StepId: Step ID such as `ConnectDBCheck`, `VersionCheck`, and `SrcPrivilegeCheck`. The specific check items are subject to source and target instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param _StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param _StepStatus: Result of this check step. Valid values: `pass`, `failed`, `notStarted`, `blocked`, `warning`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepStatus: str
        :param _StepMessage: Error message in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepMessage: str
        :param _DetailCheckItems: Specific check item in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetailCheckItems: list of DetailCheckItem
        :param _HasSkipped: Whether this step was skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasSkipped: bool
        """
        self._StepNo = None
        self._StepId = None
        self._StepName = None
        self._StepStatus = None
        self._StepMessage = None
        self._DetailCheckItems = None
        self._HasSkipped = None

    @property
    def StepNo(self):
        """Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepId(self):
        """Step ID such as `ConnectDBCheck`, `VersionCheck`, and `SrcPrivilegeCheck`. The specific check items are subject to source and target instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def StepName(self):
        """Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepStatus(self):
        """Result of this check step. Valid values: `pass`, `failed`, `notStarted`, `blocked`, `warning`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepStatus

    @StepStatus.setter
    def StepStatus(self, StepStatus):
        self._StepStatus = StepStatus

    @property
    def StepMessage(self):
        """Error message in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def DetailCheckItems(self):
        """Specific check item in this check step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DetailCheckItem
        """
        return self._DetailCheckItems

    @DetailCheckItems.setter
    def DetailCheckItems(self, DetailCheckItems):
        self._DetailCheckItems = DetailCheckItems

    @property
    def HasSkipped(self):
        """Whether this step was skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._HasSkipped

    @HasSkipped.setter
    def HasSkipped(self, HasSkipped):
        self._HasSkipped = HasSkipped


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepId = params.get("StepId")
        self._StepName = params.get("StepName")
        self._StepStatus = params.get("StepStatus")
        self._StepMessage = params.get("StepMessage")
        if params.get("DetailCheckItems") is not None:
            self._DetailCheckItems = []
            for item in params.get("DetailCheckItems"):
                obj = DetailCheckItem()
                obj._deserialize(item)
                self._DetailCheckItems.append(obj)
        self._HasSkipped = params.get("HasSkipped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStepInfo(AbstractModel):
    """Check task running details

    """

    def __init__(self):
        r"""
        :param _StartAt: Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartAt: str
        :param _EndAt: Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndAt: str
        :param _Progress: Task step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        self._StartAt = None
        self._EndAt = None
        self._Progress = None

    @property
    def StartAt(self):
        """Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        """Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def Progress(self):
        """Task step information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        if params.get("Progress") is not None:
            self._Progress = ProcessProgress()
            self._Progress._deserialize(params.get("Progress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Column(AbstractModel):
    """Column information in data sync

    """

    def __init__(self):
        r"""
        :param _ColumnName: Column nameNote: This field may return null, indicating that no valid values can be obtained.
        :type ColumnName: str
        :param _NewColumnName: New column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewColumnName: str
        """
        self._ColumnName = None
        self._NewColumnName = None

    @property
    def ColumnName(self):
        """Column nameNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName

    @property
    def NewColumnName(self):
        """New column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewColumnName

    @NewColumnName.setter
    def NewColumnName(self, NewColumnName):
        self._NewColumnName = NewColumnName


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        self._NewColumnName = params.get("NewColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareAbstractInfo(AbstractModel):
    """Summary information of data consistency check

    """

    def __init__(self):
        r"""
        :param _Options: Configuration parameters of the check task
Note: This field may return null, indicating that no valid values can be obtained.
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Objects: Consistency check objects
Note: This field may return null, indicating that no valid values can be obtained.
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Conclusion: Comparison conclusion. Valid values: `same`, `different`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conclusion: str
        :param _Status: Task status. Valid values: `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _TotalTables: Total number of tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalTables: int
        :param _CheckedTables: Number of checked tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckedTables: int
        :param _DifferentTables: Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type DifferentTables: int
        :param _SkippedTables: Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkippedTables: int
        :param _NearlyTableCount: The estimated number of tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type NearlyTableCount: int
        :param _DifferentRows: Number of inconsistent data rows
Note: This field may return null, indicating that no valid values can be obtained.
        :type DifferentRows: int
        :param _SrcSampleRows: Source database row count, which takes effect only when the comparison type is **Row count comparison**.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcSampleRows: int
        :param _DstSampleRows: Target database row count, which takes effect only when the comparison type is **Row count comparison**.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstSampleRows: int
        :param _StartedAt: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartedAt: str
        :param _FinishedAt: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinishedAt: str
        """
        self._Options = None
        self._Objects = None
        self._Conclusion = None
        self._Status = None
        self._TotalTables = None
        self._CheckedTables = None
        self._DifferentTables = None
        self._SkippedTables = None
        self._NearlyTableCount = None
        self._DifferentRows = None
        self._SrcSampleRows = None
        self._DstSampleRows = None
        self._StartedAt = None
        self._FinishedAt = None

    @property
    def Options(self):
        """Configuration parameters of the check task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        """Consistency check objects
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Conclusion(self):
        """Comparison conclusion. Valid values: `same`, `different`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def Status(self):
        """Task status. Valid values: `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalTables(self):
        """Total number of tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalTables

    @TotalTables.setter
    def TotalTables(self, TotalTables):
        self._TotalTables = TotalTables

    @property
    def CheckedTables(self):
        """Number of checked tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CheckedTables

    @CheckedTables.setter
    def CheckedTables(self, CheckedTables):
        self._CheckedTables = CheckedTables

    @property
    def DifferentTables(self):
        """Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DifferentTables

    @DifferentTables.setter
    def DifferentTables(self, DifferentTables):
        self._DifferentTables = DifferentTables

    @property
    def SkippedTables(self):
        """Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SkippedTables

    @SkippedTables.setter
    def SkippedTables(self, SkippedTables):
        self._SkippedTables = SkippedTables

    @property
    def NearlyTableCount(self):
        """The estimated number of tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NearlyTableCount

    @NearlyTableCount.setter
    def NearlyTableCount(self, NearlyTableCount):
        self._NearlyTableCount = NearlyTableCount

    @property
    def DifferentRows(self):
        """Number of inconsistent data rows
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DifferentRows

    @DifferentRows.setter
    def DifferentRows(self, DifferentRows):
        self._DifferentRows = DifferentRows

    @property
    def SrcSampleRows(self):
        """Source database row count, which takes effect only when the comparison type is **Row count comparison**.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SrcSampleRows

    @SrcSampleRows.setter
    def SrcSampleRows(self, SrcSampleRows):
        self._SrcSampleRows = SrcSampleRows

    @property
    def DstSampleRows(self):
        """Target database row count, which takes effect only when the comparison type is **Row count comparison**.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DstSampleRows

    @DstSampleRows.setter
    def DstSampleRows(self, DstSampleRows):
        self._DstSampleRows = DstSampleRows

    @property
    def StartedAt(self):
        """Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        """End time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt


    def _deserialize(self, params):
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        self._Conclusion = params.get("Conclusion")
        self._Status = params.get("Status")
        self._TotalTables = params.get("TotalTables")
        self._CheckedTables = params.get("CheckedTables")
        self._DifferentTables = params.get("DifferentTables")
        self._SkippedTables = params.get("SkippedTables")
        self._NearlyTableCount = params.get("NearlyTableCount")
        self._DifferentRows = params.get("DifferentRows")
        self._SrcSampleRows = params.get("SrcSampleRows")
        self._DstSampleRows = params.get("DstSampleRows")
        self._StartedAt = params.get("StartedAt")
        self._FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareColumnItem(AbstractModel):
    """Column options

    """

    def __init__(self):
        r"""
        :param _ColumnName: Column nameNote: This field may return null, indicating that no valid values can be obtained.
        :type ColumnName: str
        """
        self._ColumnName = None

    @property
    def ColumnName(self):
        """Column nameNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareDetailInfo(AbstractModel):
    """Data consistency check details

    """

    def __init__(self):
        r"""
        :param _Difference: Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Difference: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        :param _Skipped: Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Skipped: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        self._Difference = None
        self._Skipped = None

    @property
    def Difference(self):
        """Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DifferenceDetail`
        """
        return self._Difference

    @Difference.setter
    def Difference(self, Difference):
        self._Difference = Difference

    @property
    def Skipped(self):
        """Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkippedDetail`
        """
        return self._Skipped

    @Skipped.setter
    def Skipped(self, Skipped):
        self._Skipped = Skipped


    def _deserialize(self, params):
        if params.get("Difference") is not None:
            self._Difference = DifferenceDetail()
            self._Difference._deserialize(params.get("Difference"))
        if params.get("Skipped") is not None:
            self._Skipped = SkippedDetail()
            self._Skipped._deserialize(params.get("Skipped"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObject(AbstractModel):
    """Configuration of the data consistency check object

    """

    def __init__(self):
        r"""
        :param _ObjectMode: Data comparison object mode (`all`: Entire instance; `partial`: Some objects)
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectMode: str
        :param _ObjectItems: Object list
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectItems: list of CompareObjectItem
        :param _AdvancedObjects: Advanced object types, such as account, index, shardkey, schema.Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._ObjectItems = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        """Data comparison object mode (`all`: Entire instance; `partial`: Some objects)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def ObjectItems(self):
        """Object list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CompareObjectItem
        """
        return self._ObjectItems

    @ObjectItems.setter
    def ObjectItems(self, ObjectItems):
        self._ObjectItems = ObjectItems

    @property
    def AdvancedObjects(self):
        """Advanced object types, such as account, index, shardkey, schema.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects


    def _deserialize(self, params):
        self._ObjectMode = params.get("ObjectMode")
        if params.get("ObjectItems") is not None:
            self._ObjectItems = []
            for item in params.get("ObjectItems"):
                obj = CompareObjectItem()
                obj._deserialize(item)
                self._ObjectItems.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareObjectItem(AbstractModel):
    """Database/Table objects for data consistency check

    """

    def __init__(self):
        r"""
        :param _DbName: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _DbMode: Database selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param _SchemaName: Schema name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param _TableMode: Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param _Tables: Table configuration for data consistency check, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of CompareTableItem
        :param _ViewMode: View selection mode: all refers to all view objects under the current object, partial refers to partial view objects (consistency check does not check views, and the current parameters are disabled).Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param _Views: View configuration used for consistency check. When ViewMode is partial, it needs to be filled in (consistency check does not check views, and the current parameters are disabled).Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of CompareViewItem
        """
        self._DbName = None
        self._DbMode = None
        self._SchemaName = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None

    @property
    def DbName(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def DbMode(self):
        """Database selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        """Schema name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def TableMode(self):
        """Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """Table configuration for data consistency check, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CompareTableItem
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """View selection mode: all refers to all view objects under the current object, partial refers to partial view objects (consistency check does not check views, and the current parameters are disabled).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """View configuration used for consistency check. When ViewMode is partial, it needs to be filled in (consistency check does not check views, and the current parameters are disabled).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CompareViewItem
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._DbMode = params.get("DbMode")
        self._SchemaName = params.get("SchemaName")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = CompareTableItem()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = CompareViewItem()
                obj._deserialize(item)
                self._Views.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareOptions(AbstractModel):
    """Consistency check options

    """

    def __init__(self):
        r"""
        :param _Method: Comparative Method: dataCheck (Complete Data Comparison), sampleDataCheck (Sampling Data Comparison), rowsCount (Row Count Comparison)Note: This field may return null, indicating that no valid value can be obtained.
        :type Method: str
        :param _SampleRate: Sampling rate. Value range: 0-100%.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SampleRate: int
        :param _ThreadCount: The number of threads, which defaults to 1. Value range: 1-5.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ThreadCount: int
        """
        self._Method = None
        self._SampleRate = None
        self._ThreadCount = None

    @property
    def Method(self):
        """Comparative Method: dataCheck (Complete Data Comparison), sampleDataCheck (Sampling Data Comparison), rowsCount (Row Count Comparison)Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def SampleRate(self):
        """Sampling rate. Value range: 0-100%.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ThreadCount(self):
        """The number of threads, which defaults to 1. Value range: 1-5.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ThreadCount

    @ThreadCount.setter
    def ThreadCount(self, ThreadCount):
        self._ThreadCount = ThreadCount


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._SampleRate = params.get("SampleRate")
        self._ThreadCount = params.get("ThreadCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTableItem(AbstractModel):
    """Table configuration for data consistency check

    """

    def __init__(self):
        r"""
        :param _TableName: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _ColumnMode: In column mode, all refers to all data, while partial refers to part of the data (this parameter is only valid for data sync tasks).Note: This field may return null, indicating that no valid values can be obtained.
        :type ColumnMode: str
        :param _Columns: This field is required when ColumnMode is set to partial (this parameter is only valid for data sync tasks).Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of CompareColumnItem
        """
        self._TableName = None
        self._ColumnMode = None
        self._Columns = None

    @property
    def TableName(self):
        """Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def ColumnMode(self):
        """In column mode, all refers to all data, while partial refers to part of the data (this parameter is only valid for data sync tasks).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColumnMode

    @ColumnMode.setter
    def ColumnMode(self, ColumnMode):
        self._ColumnMode = ColumnMode

    @property
    def Columns(self):
        """This field is required when ColumnMode is set to partial (this parameter is only valid for data sync tasks).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CompareColumnItem
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._ColumnMode = params.get("ColumnMode")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = CompareColumnItem()
                obj._deserialize(item)
                self._Columns.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskInfo(AbstractModel):
    """Data consistency check result

    """

    def __init__(self):
        r"""
        :param _CompareTaskId: Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param _Status: Data consistency check result. Valid values: `unstart` (the task is not started); `running` (the task is running); `canceled` (the task is stopped); `failed` (the task failed); `inconsistent` (the data is inconsistent); `consistent` (the data is consistent); `notexist` (the task does not exist).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._CompareTaskId = None
        self._Status = None

    @property
    def CompareTaskId(self):
        """Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        """Data consistency check result. Valid values: `unstart` (the task is not started); `running` (the task is running); `canceled` (the task is stopped); `failed` (the task failed); `inconsistent` (the data is inconsistent); `consistent` (the data is consistent); `notexist` (the task does not exist).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CompareTaskId = params.get("CompareTaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareTaskItem(AbstractModel):
    """Information of the data consistency check object

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param _TaskName: Data consistency check task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _Status: Data consistency check task status. Valid values: `created`, `readyRun`, `running`, `success`, `stopping`, `failed`, `canceled`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Config: Data consistency check task configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _CheckProcess: Check details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _CompareProcess: Running details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareProcess: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        :param _Conclusion: Comparison result. Valid values: `same`, `different`, `skipAll`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conclusion: str
        :param _CreatedAt: Task creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _StartedAt: Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartedAt: str
        :param _FinishedAt: Comparison end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinishedAt: str
        :param _Method: Comparison type: (`dataCheck`: Full data comparison; `sampleDataCheck`: Sampling data comparison; `rowsCount`: Row count comparison)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Method: str
        :param _Options: Configuration information of the comparison task
Note: This field may return null, indicating that no valid values can be obtained.
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        :param _Message: Consistency check prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None
        self._Status = None
        self._Config = None
        self._CheckProcess = None
        self._CompareProcess = None
        self._Conclusion = None
        self._CreatedAt = None
        self._StartedAt = None
        self._FinishedAt = None
        self._Method = None
        self._Options = None
        self._Message = None

    @property
    def JobId(self):
        """Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """Data consistency check task name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        """Data consistency check task status. Valid values: `created`, `readyRun`, `running`, `success`, `stopping`, `failed`, `canceled`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Config(self):
        """Data consistency check task configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CheckProcess(self):
        """Check details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        return self._CheckProcess

    @CheckProcess.setter
    def CheckProcess(self, CheckProcess):
        self._CheckProcess = CheckProcess

    @property
    def CompareProcess(self):
        """Running details of the data consistency check task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ProcessProgress`
        """
        return self._CompareProcess

    @CompareProcess.setter
    def CompareProcess(self, CompareProcess):
        self._CompareProcess = CompareProcess

    @property
    def Conclusion(self):
        """Comparison result. Valid values: `same`, `different`, `skipAll`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Conclusion

    @Conclusion.setter
    def Conclusion(self, Conclusion):
        self._Conclusion = Conclusion

    @property
    def CreatedAt(self):
        """Task creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def StartedAt(self):
        """Task start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def FinishedAt(self):
        """Comparison end time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt

    @property
    def Method(self):
        """Comparison type: (`dataCheck`: Full data comparison; `sampleDataCheck`: Sampling data comparison; `rowsCount`: Row count comparison)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Options(self):
        """Configuration information of the comparison task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Message(self):
        """Consistency check prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        if params.get("Config") is not None:
            self._Config = CompareObject()
            self._Config._deserialize(params.get("Config"))
        if params.get("CheckProcess") is not None:
            self._CheckProcess = ProcessProgress()
            self._CheckProcess._deserialize(params.get("CheckProcess"))
        if params.get("CompareProcess") is not None:
            self._CompareProcess = ProcessProgress()
            self._CompareProcess._deserialize(params.get("CompareProcess"))
        self._Conclusion = params.get("Conclusion")
        self._CreatedAt = params.get("CreatedAt")
        self._StartedAt = params.get("StartedAt")
        self._FinishedAt = params.get("FinishedAt")
        self._Method = params.get("Method")
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareViewItem(AbstractModel):
    """View configuration for data consistency check

    """

    def __init__(self):
        r"""
        :param _ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        """
        self._ViewName = None

    @property
    def ViewName(self):
        """View name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _CompleteMode: The way to complete the task, which is supported only for legacy MySQL migration tasks. Valid values: `waitForSync` (wait for the source-replica lag to become 0 before stopping); `immediately` (complete immediately without waiting for source-replica sync). Default value: `waitForSync`.
        :type CompleteMode: str
        """
        self._JobId = None
        self._CompleteMode = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompleteMode(self):
        """The way to complete the task, which is supported only for legacy MySQL migration tasks. Valid values: `waitForSync` (wait for the source-replica lag to become 0 before stopping); `immediately` (complete immediately without waiting for source-replica sync). Default value: `waitForSync`.
        :rtype: str
        """
        return self._CompleteMode

    @CompleteMode.setter
    def CompleteMode(self, CompleteMode):
        self._CompleteMode = CompleteMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompleteMode = params.get("CompleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConfigureSubscribeJobRequest(AbstractModel):
    """ConfigureSubscribeJob request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeMode: Data subscription type. Valid values for non-mongo DatabaseType: all (full instance update); dml (data update); ddl (structure update); dmlAndDdl (data + structure update). Valid values for mongo DatabaseType: all (full instance update); database (subscribe to a table); collection (subscribe to a collection).
        :type SubscribeMode: str
        :param _AccessType: Source database access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC). Note: The specific optional values depend on the current link support capabilities.
        :type AccessType: str
        :param _Endpoints: Database node information
        :type Endpoints: list of EndpointItem
        :param _KafkaConfig: Kafka configuration
        :type KafkaConfig: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        :param _SubscribeObjects: Subscription database table information. When SubscribeMode is not all or ddl, SubscribeObjects is a required parameter.
        :type SubscribeObjects: list of SubscribeObject
        :param _Protocol: Subscription data format, such as: protobuf, json, avro. Note: The specific optional values depend on the current link support capabilities. For details on the data format, please refer to the consumption demo documentation on the official website.
        :type Protocol: str
        :param _PipelineInfo: mongo optional parameter: output aggregation settings.
        :type PipelineInfo: list of PipelineInfo
        :param _ExtraAttr: Additional information added for the business. The parameter name is called key, and the parameter value is called value.Optional parameters for mysql: ProcessXA. If true is filled in, it will be processed. If it is left blank or filled with other values, it will not be processed.Optional parameters for mongo: SubscribeType. Currently only changeStream is supported. If not filled in, the default is changeStream.Other businesses currently have no optional parameters.
        :type ExtraAttr: list of KeyValuePairOption
        """
        self._SubscribeId = None
        self._SubscribeMode = None
        self._AccessType = None
        self._Endpoints = None
        self._KafkaConfig = None
        self._SubscribeObjects = None
        self._Protocol = None
        self._PipelineInfo = None
        self._ExtraAttr = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeMode(self):
        """Data subscription type. Valid values for non-mongo DatabaseType: all (full instance update); dml (data update); ddl (structure update); dmlAndDdl (data + structure update). Valid values for mongo DatabaseType: all (full instance update); database (subscribe to a table); collection (subscribe to a collection).
        :rtype: str
        """
        return self._SubscribeMode

    @SubscribeMode.setter
    def SubscribeMode(self, SubscribeMode):
        self._SubscribeMode = SubscribeMode

    @property
    def AccessType(self):
        """Source database access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC). Note: The specific optional values depend on the current link support capabilities.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """Database node information
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def KafkaConfig(self):
        """Kafka configuration
        :rtype: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        """
        return self._KafkaConfig

    @KafkaConfig.setter
    def KafkaConfig(self, KafkaConfig):
        self._KafkaConfig = KafkaConfig

    @property
    def SubscribeObjects(self):
        """Subscription database table information. When SubscribeMode is not all or ddl, SubscribeObjects is a required parameter.
        :rtype: list of SubscribeObject
        """
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

    @property
    def Protocol(self):
        """Subscription data format, such as: protobuf, json, avro. Note: The specific optional values depend on the current link support capabilities. For details on the data format, please refer to the consumption demo documentation on the official website.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PipelineInfo(self):
        """mongo optional parameter: output aggregation settings.
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo

    @property
    def ExtraAttr(self):
        """Additional information added for the business. The parameter name is called key, and the parameter value is called value.Optional parameters for mysql: ProcessXA. If true is filled in, it will be processed. If it is left blank or filled with other values, it will not be processed.Optional parameters for mongo: SubscribeType. Currently only changeStream is supported. If not filled in, the default is changeStream.Other businesses currently have no optional parameters.
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeMode = params.get("SubscribeMode")
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        if params.get("KafkaConfig") is not None:
            self._KafkaConfig = SubscribeKafkaConfig()
            self._KafkaConfig._deserialize(params.get("KafkaConfig"))
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        self._Protocol = params.get("Protocol")
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureSubscribeJobResponse(AbstractModel):
    """ConfigureSubscribeJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConfigureSyncJobRequest(AbstractModel):
    """ConfigureSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :type JobId: str
        :param _SrcAccessType: Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet). Note that the valid values are subject to the current link.
        :type SrcAccessType: str
        :param _DstAccessType: Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet); `ckafka` (CKafka instance). Note that the valid values are subject to the current link.
        :type DstAccessType: str
        :param _Objects: Information of synced database/table objects
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _JobName: Sync task name
        :type JobName: str
        :param _JobMode: Enumerated values: `liteMode`: Lite mode; `fullMode`: Standard mode
        :type JobMode: str
        :param _RunMode: Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
        :type RunMode: str
        :param _ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `Timed`.
        :type ExpectRunTime: str
        :param _SrcInfo: Source database information. This parameter only applies to single-node databases, and `SrcNodeType` must be `single`.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _SrcInfos: Source database information. This parameter is valid for multi-node databases, and the value of `SrcNodeType` must be `cluster`.
        :type SrcInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _SrcNodeType: Enumerated values: `single` (for single-node source database), `cluster` (for multi-node source database).
        :type SrcNodeType: str
        :param _DstInfo: Target database information. This parameter is used by single-node databases.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstInfos: Target database information. This parameter is valid for multi-node databases, and the value of `DstNodeType` must be `cluster`.
        :type DstInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _DstNodeType: Enumerated values: `single` (for single-node target database), `cluster` (for multi-node target database).
        :type DstNodeType: str
        :param _Options: Sync task options. The `RateLimitOption` option cannot take effect currently. To modify the speed limit settings, use the `ModifySyncRateLimit` API.
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param _AutoRetryTimeRangeMinutes: Automatic retry time, which can be set to 5-720 minutes. 0 indicates that retry is disabled.
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._SrcAccessType = None
        self._DstAccessType = None
        self._Objects = None
        self._JobName = None
        self._JobMode = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._SrcInfo = None
        self._SrcInfos = None
        self._SrcNodeType = None
        self._DstInfo = None
        self._DstInfos = None
        self._DstNodeType = None
        self._Options = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        """Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SrcAccessType(self):
        """Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet). Note that the valid values are subject to the current link.
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstAccessType(self):
        """Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet); `ckafka` (CKafka instance). Note that the valid values are subject to the current link.
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def Objects(self):
        """Information of synced database/table objects
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def JobName(self):
        """Sync task name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobMode(self):
        """Enumerated values: `liteMode`: Lite mode; `fullMode`: Standard mode
        :rtype: str
        """
        return self._JobMode

    @JobMode.setter
    def JobMode(self, JobMode):
        self._JobMode = JobMode

    @property
    def RunMode(self):
        """Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `Timed`.
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def SrcInfo(self):
        """Source database information. This parameter only applies to single-node databases, and `SrcNodeType` must be `single`.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def SrcInfos(self):
        """Source database information. This parameter is valid for multi-node databases, and the value of `SrcNodeType` must be `cluster`.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._SrcInfos

    @SrcInfos.setter
    def SrcInfos(self, SrcInfos):
        self._SrcInfos = SrcInfos

    @property
    def SrcNodeType(self):
        """Enumerated values: `single` (for single-node source database), `cluster` (for multi-node source database).
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def DstInfo(self):
        """Target database information. This parameter is used by single-node databases.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DstInfos(self):
        """Target database information. This parameter is valid for multi-node databases, and the value of `DstNodeType` must be `cluster`.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._DstInfos

    @DstInfos.setter
    def DstInfos(self, DstInfos):
        self._DstInfos = DstInfos

    @property
    def DstNodeType(self):
        """Enumerated values: `single` (for single-node target database), `cluster` (for multi-node target database).
        :rtype: str
        """
        return self._DstNodeType

    @DstNodeType.setter
    def DstNodeType(self, DstNodeType):
        self._DstNodeType = DstNodeType

    @property
    def Options(self):
        """Sync task options. The `RateLimitOption` option cannot take effect currently. To modify the speed limit settings, use the `ModifySyncRateLimit` API.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Options`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def AutoRetryTimeRangeMinutes(self):
        """Automatic retry time, which can be set to 5-720 minutes. 0 indicates that retry is disabled.
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._SrcAccessType = params.get("SrcAccessType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("Objects") is not None:
            self._Objects = Objects()
            self._Objects._deserialize(params.get("Objects"))
        self._JobName = params.get("JobName")
        self._JobMode = params.get("JobMode")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = Endpoint()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("SrcInfos") is not None:
            self._SrcInfos = SyncDBEndpointInfos()
            self._SrcInfos._deserialize(params.get("SrcInfos"))
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("DstInfo") is not None:
            self._DstInfo = Endpoint()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("DstInfos") is not None:
            self._DstInfos = SyncDBEndpointInfos()
            self._DstInfos._deserialize(params.get("DstInfos"))
        self._DstNodeType = params.get("DstNodeType")
        if params.get("Options") is not None:
            self._Options = Options()
            self._Options._deserialize(params.get("Options"))
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureSyncJobResponse(AbstractModel):
    """ConfigureSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ConflictHandleOption(AbstractModel):
    """Detailed description of conflict processing

    """

    def __init__(self):
        r"""
        :param _ConditionColumn: Conditionally overwritten column
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionColumn: str
        :param _ConditionOperator: Conditional overwrite operation
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionOperator: str
        :param _ConditionOrderInSrcAndDst: Conditional overwrite priority configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionOrderInSrcAndDst: str
        """
        self._ConditionColumn = None
        self._ConditionOperator = None
        self._ConditionOrderInSrcAndDst = None

    @property
    def ConditionColumn(self):
        """Conditionally overwritten column
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConditionColumn

    @ConditionColumn.setter
    def ConditionColumn(self, ConditionColumn):
        self._ConditionColumn = ConditionColumn

    @property
    def ConditionOperator(self):
        """Conditional overwrite operation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConditionOperator

    @ConditionOperator.setter
    def ConditionOperator(self, ConditionOperator):
        self._ConditionOperator = ConditionOperator

    @property
    def ConditionOrderInSrcAndDst(self):
        """Conditional overwrite priority configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConditionOrderInSrcAndDst

    @ConditionOrderInSrcAndDst.setter
    def ConditionOrderInSrcAndDst(self, ConditionOrderInSrcAndDst):
        self._ConditionOrderInSrcAndDst = ConditionOrderInSrcAndDst


    def _deserialize(self, params):
        self._ConditionColumn = params.get("ConditionColumn")
        self._ConditionOperator = params.get("ConditionOperator")
        self._ConditionOrderInSrcAndDst = params.get("ConditionOrderInSrcAndDst")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsistencyOption(AbstractModel):
    """Data consistency check option. Data consistency check is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Mode: Data consistency check type. Valid values: `full`, `noCheck`, `notConfigured`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        """Data consistency check type. Valid values: `full`, `noCheck`, `notConfigured`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobRequest(AbstractModel):
    """ContinueMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueMigrateJobResponse(AbstractModel):
    """ContinueMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ContinueSyncJobRequest(AbstractModel):
    """ContinueSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueSyncJobResponse(AbstractModel):
    """ContinueSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCheckSyncJobRequest(AbstractModel):
    """CreateCheckSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCheckSyncJobResponse(AbstractModel):
    """CreateCheckSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCompareTaskRequest(AbstractModel):
    """CreateCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _TaskName: Data consistency check task name. If this parameter is left empty, the value of `CompareTaskId` will be assigned to it.
        :type TaskName: str
        :param _ObjectMode: Data comparison object mode. Valid values: `sameAsMigrate` (all migration objects); `custom` (custom mode). Default value: `sameAsMigrate`.
        :type ObjectMode: str
        :param _Objects: Configuration of the data consistency check object
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Options: Consistency check options
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self._JobId = None
        self._TaskName = None
        self._ObjectMode = None
        self._Objects = None
        self._Options = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """Data consistency check task name. If this parameter is left empty, the value of `CompareTaskId` will be assigned to it.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        """Data comparison object mode. Valid values: `sameAsMigrate` (all migration objects); `custom` (custom mode). Default value: `sameAsMigrate`.
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        """Configuration of the data consistency check object
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        """Consistency check options
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCompareTaskResponse(AbstractModel):
    """CreateCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CompareTaskId = None
        self._RequestId = None

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompareTaskId = params.get("CompareTaskId")
        self._RequestId = params.get("RequestId")


class CreateConsumerGroupRequest(AbstractModel):
    """CreateConsumerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _ConsumerGroupName: Consumer group name, which consists of numbers, letters (upper and lower case), or begins with _ - . Ends with numbers, letters (upper and lower case). The full name of the actually generated consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :type ConsumerGroupName: str
        :param _AccountName: Account name, which consists of numbers, letters (upper and lower case), or begins with _-.. Ends with numbers, letters (upper and lower case). The full name of the actually generated account is in the form: account-#{SubscribeId}-#{AccountName}.
        :type AccountName: str
        :param _Password: Consumer group password, which should be longer than 3 characters.
        :type Password: str
        :param _Description: Consumer group description
        :type Description: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None
        self._Password = None
        self._Description = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """Consumer group name, which consists of numbers, letters (upper and lower case), or begins with _ - . Ends with numbers, letters (upper and lower case). The full name of the actually generated consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """Account name, which consists of numbers, letters (upper and lower case), or begins with _-.. Ends with numbers, letters (upper and lower case). The full name of the actually generated account is in the form: account-#{SubscribeId}-#{AccountName}.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Password(self):
        """Consumer group password, which should be longer than 3 characters.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        """Consumer group description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerGroupResponse(AbstractModel):
    """CreateConsumerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateMigrationServiceRequest(AbstractModel):
    """CreateMigrationService request structure.

    """

    def __init__(self):
        r"""
        :param _SrcDatabaseType: Source database type. Valid values: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`, and `cynosdbmysql`.
        :type SrcDatabaseType: str
        :param _DstDatabaseType: Target database type. Valid values: `mysql`, `redis`, `percona`, `mongodb` ,`postgresql`, `sqlserver`, `mariadb`, and `cynosdbmysql`.
        :type DstDatabaseType: str
        :param _SrcRegion: Source instance region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param _DstRegion: Target instance region, such as `ap-guangzhou`. Note that it must be the same as the API request region.
        :type DstRegion: str
        :param _InstanceClass: Instance specification. Valid values: `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :type InstanceClass: str
        :param _Count: Quantity. Value range: [1,15]. Default value: `1`.
        :type Count: int
        :param _JobName: Migration task name, which can contain up to 128 characters.
        :type JobName: str
        :param _Tags: Tag information
        :type Tags: list of TagItem
        """
        self._SrcDatabaseType = None
        self._DstDatabaseType = None
        self._SrcRegion = None
        self._DstRegion = None
        self._InstanceClass = None
        self._Count = None
        self._JobName = None
        self._Tags = None

    @property
    def SrcDatabaseType(self):
        """Source database type. Valid values: `mysql`, `redis`, `percona`, `mongodb`, `postgresql`, `sqlserver`, `mariadb`, and `cynosdbmysql`.
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def DstDatabaseType(self):
        """Target database type. Valid values: `mysql`, `redis`, `percona`, `mongodb` ,`postgresql`, `sqlserver`, `mariadb`, and `cynosdbmysql`.
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def SrcRegion(self):
        """Source instance region, such as `ap-guangzhou`.
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstRegion(self):
        """Target instance region, such as `ap-guangzhou`. Note that it must be the same as the API request region.
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def InstanceClass(self):
        """Instance specification. Valid values: `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def Count(self):
        """Quantity. Value range: [1,15]. Default value: `1`.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def JobName(self):
        """Migration task name, which can contain up to 128 characters.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Tags(self):
        """Tag information
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._SrcRegion = params.get("SrcRegion")
        self._DstRegion = params.get("DstRegion")
        self._InstanceClass = params.get("InstanceClass")
        self._Count = params.get("Count")
        self._JobName = params.get("JobName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMigrationServiceResponse(AbstractModel):
    """CreateMigrationService response structure.

    """

    def __init__(self):
        r"""
        :param _JobIds: The list of migration task IDs randomly generated in the format of `dts-c1f6rs21` after a successful order placement
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        """The list of migration task IDs randomly generated in the format of `dts-c1f6rs21` after a successful order placement
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._RequestId = params.get("RequestId")


class CreateModifyCheckSyncJobRequest(AbstractModel):
    """CreateModifyCheckSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModifyCheckSyncJobResponse(AbstractModel):
    """CreateModifyCheckSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSubscribeCheckJobRequest(AbstractModel):
    """CreateSubscribeCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeCheckJobResponse(AbstractModel):
    """CreateSubscribeCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Subscription database type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, and tdsqlpercona are supported.
        :type Product: str
        :param _PayType: Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :type PayType: int
        :param _Duration: Purchase duration. This field needs to be filled in when the payType is monthly subscription. The unit is month. Value range: 1-120. Default value: 1.
        :type Duration: int
        :param _AutoRenew: Whether to renew automatically. This field needs to be filled in when the payType is monthly subscription. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled). Automatic renewal is not performed by default. This flag is invalid for pay-as-you-go.
        :type AutoRenew: int
        :param _Count: Quantity. Default value: 1. Maximum value: 10.
        :type Count: int
        :param _Tags: Instance resource tags
        :type Tags: list of TagItem
        :param _Name: Custom task name
        :type Name: str
        """
        self._Product = None
        self._PayType = None
        self._Duration = None
        self._AutoRenew = None
        self._Count = None
        self._Tags = None
        self._Name = None

    @property
    def Product(self):
        """Subscription database type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, and tdsqlpercona are supported.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def PayType(self):
        """Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Duration(self):
        """Purchase duration. This field needs to be filled in when the payType is monthly subscription. The unit is month. Value range: 1-120. Default value: 1.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AutoRenew(self):
        """Whether to renew automatically. This field needs to be filled in when the payType is monthly subscription. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled). Automatic renewal is not performed by default. This flag is invalid for pay-as-you-go.
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Count(self):
        """Quantity. Default value: 1. Maximum value: 10.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Tags(self):
        """Instance resource tags
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Name(self):
        """Custom task name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._PayType = params.get("PayType")
        self._Duration = params.get("Duration")
        self._AutoRenew = params.get("AutoRenew")
        self._Count = params.get("Count")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeIds: Array of data subscription instance IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscribeIds = None
        self._RequestId = None

    @property
    def SubscribeIds(self):
        """Array of data subscription instance IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SubscribeIds

    @SubscribeIds.setter
    def SubscribeIds(self, SubscribeIds):
        self._SubscribeIds = SubscribeIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeIds = params.get("SubscribeIds")
        self._RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _PayMode: Billing mode. Valid values: `PrePay` (monthly subscription); `PostPay` (pay-as-you-go). Currently, DTS at Tencent Cloud International is free of charge.
        :type PayMode: str
        :param _SrcDatabaseType: Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
        :type SrcDatabaseType: str
        :param _SrcRegion: Source database region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param _DstDatabaseType: Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, `tdsqlmysql`, and `kafka`.
        :type DstDatabaseType: str
        :param _DstRegion: Target database region, such as `ap-guangzhou`.
        :type DstRegion: str
        :param _Specification: Sync task specification, such as `Standard`.
        :type Specification: str
        :param _Tags: Tag information
        :type Tags: list of TagItem
        :param _Count: The number of sync tasks purchased at a time. Value range: [1, 10]. Default value: `1`.
        :type Count: int
        :param _AutoRenew: Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled). Default value: `0`.
        :type AutoRenew: int
        :param _InstanceClass: Sync link specification, such as `micro`, `small`, `medium`, and `large`. Default value: `medium`.
        :type InstanceClass: str
        :param _JobName: Sync task name
        :type JobName: str
        :param _ExistedJobId: ID of the existing task used to create a similar task
        :type ExistedJobId: str
        """
        self._PayMode = None
        self._SrcDatabaseType = None
        self._SrcRegion = None
        self._DstDatabaseType = None
        self._DstRegion = None
        self._Specification = None
        self._Tags = None
        self._Count = None
        self._AutoRenew = None
        self._InstanceClass = None
        self._JobName = None
        self._ExistedJobId = None

    @property
    def PayMode(self):
        """Billing mode. Valid values: `PrePay` (monthly subscription); `PostPay` (pay-as-you-go). Currently, DTS at Tencent Cloud International is free of charge.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SrcDatabaseType(self):
        """Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcRegion(self):
        """Source database region, such as `ap-guangzhou`.
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def DstDatabaseType(self):
        """Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, `tdsqlmysql`, and `kafka`.
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstRegion(self):
        """Target database region, such as `ap-guangzhou`.
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def Specification(self):
        """Sync task specification, such as `Standard`.
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Tags(self):
        """Tag information
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Count(self):
        """The number of sync tasks purchased at a time. Value range: [1, 10]. Default value: `1`.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AutoRenew(self):
        """Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled). Default value: `0`.
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def InstanceClass(self):
        """Sync link specification, such as `micro`, `small`, `medium`, and `large`. Default value: `medium`.
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def JobName(self):
        """Sync task name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExistedJobId(self):
        """ID of the existing task used to create a similar task
        :rtype: str
        """
        return self._ExistedJobId

    @ExistedJobId.setter
    def ExistedJobId(self, ExistedJobId):
        self._ExistedJobId = ExistedJobId


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcRegion = params.get("SrcRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstRegion = params.get("DstRegion")
        self._Specification = params.get("Specification")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Count = params.get("Count")
        self._AutoRenew = params.get("AutoRenew")
        self._InstanceClass = params.get("InstanceClass")
        self._JobName = params.get("JobName")
        self._ExistedJobId = params.get("ExistedJobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobIds: Sync task IDs
        :type JobIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobIds = None
        self._RequestId = None

    @property
    def JobIds(self):
        """Sync task IDs
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._RequestId = params.get("RequestId")


class DBEndpointInfo(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param _Region: Instance region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AccessType: Instances network access type. Valid values: `extranet` (public network); `ipv6` (public IPv6); `cvm` (self-build on CVM); `dcg` (Direct Connect); `vpncloud` (VPN access); `cdb` (database); `ccn` (CCN); `intranet` (intranet); `vpc` (VPC). Note that the valid values are subject to the current link.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessType: str
        :param _DatabaseType: Database type, such as `mysql`, `redis`, `mongodb`, `postgresql`, `mariadb`, and `percona`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseType: str
        :param _NodeType: Node type, empty or simple indicates a general node, cluster indicates a cluster node; for mongo services, valid values: replicaset (mongodb replica set), standalone (mongodb single node), cluster (mongodb cluster); for redis instances, valid values: empty or simple (single node), cluster (cluster), cluster-cache (cache cluster), cluster-proxy (proxy cluster).Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeType: str
        :param _Info: Database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Info: list of DBInfo
        :param _Supplier: Instance service provider, such as "aliyun" and "others".
Note: This field may return null, indicating that no valid values can be obtained.
        :type Supplier: str
        :param _ExtraAttr: For MongoDB, you can define the following parameters: 	['AuthDatabase':'admin', 
'AuthFlag': "1",	'AuthMechanism':"SCRAM-SHA-1"]
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        :param _DatabaseNetEnv: Network environment of the database. This parameter is required when `AccessType` is `ccn`. Valid values: `UserIDC` (user IDC), `TencentVPC` (Tencent Cloud VPC).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseNetEnv: str
        :param _ConnectType: 
        :type ConnectType: str
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._NodeType = None
        self._Info = None
        self._Supplier = None
        self._ExtraAttr = None
        self._DatabaseNetEnv = None
        self._ConnectType = None

    @property
    def Region(self):
        """Instance region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """Instances network access type. Valid values: `extranet` (public network); `ipv6` (public IPv6); `cvm` (self-build on CVM); `dcg` (Direct Connect); `vpncloud` (VPN access); `cdb` (database); `ccn` (CCN); `intranet` (intranet); `vpc` (VPC). Note that the valid values are subject to the current link.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        """Database type, such as `mysql`, `redis`, `mongodb`, `postgresql`, `mariadb`, and `percona`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def NodeType(self):
        """Node type, empty or simple indicates a general node, cluster indicates a cluster node; for mongo services, valid values: replicaset (mongodb replica set), standalone (mongodb single node), cluster (mongodb cluster); for redis instances, valid values: empty or simple (single node), cluster (cluster), cluster-cache (cache cluster), cluster-proxy (proxy cluster).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Info(self):
        """Database information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DBInfo
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Supplier(self):
        """Instance service provider, such as "aliyun" and "others".
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def ExtraAttr(self):
        """For MongoDB, you can define the following parameters: 	['AuthDatabase':'admin', 
'AuthFlag': "1",	'AuthMechanism':"SCRAM-SHA-1"]
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def DatabaseNetEnv(self):
        """Network environment of the database. This parameter is required when `AccessType` is `ccn`. Valid values: `UserIDC` (user IDC), `TencentVPC` (Tencent Cloud VPC).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def ConnectType(self):
        """
        :rtype: str
        """
        return self._ConnectType

    @ConnectType.setter
    def ConnectType(self, ConnectType):
        self._ConnectType = ConnectType


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        self._DatabaseType = params.get("DatabaseType")
        self._NodeType = params.get("NodeType")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = DBInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        self._Supplier = params.get("Supplier")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        self._ConnectType = params.get("ConnectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInfo(AbstractModel):
    """Database information

    """

    def __init__(self):
        r"""
        :param _Role: Node role in a distributed database, such as the mongos node in MongoDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Role: str
        :param _DbKernel: Kernel version, such as the different kernel versions of MariaDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbKernel: str
        :param _Host: Instance IP address, which is required for the following access types: public network, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _Port: Instance port, which is required for the following access types: public network, self-build on CVM, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _User: Instance username
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param _Password: Instance password
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param _CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param _UniqVpnGwId: VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpnGwId: str
        :param _UniqDcgId: Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqDcgId: str
        :param _InstanceId: Database instance ID in the format of `cdb-powiqx8q`, which is required if the access type is `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _CcnGwId: CCN instance ID such as `ccn-afp6kltc`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnGwId: str
        :param _VpcId: VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _EngineVersion: Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineVersion: str
        :param _Account: Instance account
Note: This field may return null, indicating that no valid values can be obtained.
        :type Account: str
        :param _AccountRole: The role used for cross-account migration, which can contain [a-zA-Z0-9\-\_]+.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountRole: str
        :param _AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountMode: str
        :param _TmpSecretId: Temporary SecretId, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary SecretKey, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretKey: str
        :param _TmpToken: Temporary token, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpToken: str
        """
        self._Role = None
        self._DbKernel = None
        self._Host = None
        self._Port = None
        self._User = None
        self._Password = None
        self._CvmInstanceId = None
        self._UniqVpnGwId = None
        self._UniqDcgId = None
        self._InstanceId = None
        self._CcnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._EngineVersion = None
        self._Account = None
        self._AccountRole = None
        self._AccountMode = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None

    @property
    def Role(self):
        """Node role in a distributed database, such as the mongos node in MongoDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        """Kernel version, such as the different kernel versions of MariaDB.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def Host(self):
        """Instance IP address, which is required for the following access types: public network, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """Instance port, which is required for the following access types: public network, self-build on CVM, Direct Connect, VPN, CCN, intranet, and VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """Instance username
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """Instance password
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CvmInstanceId(self):
        """Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqVpnGwId(self):
        """VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def UniqDcgId(self):
        """Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def InstanceId(self):
        """Database instance ID in the format of `cdb-powiqx8q`, which is required if the access type is `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CcnGwId(self):
        """CCN instance ID such as `ccn-afp6kltc`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CcnGwId

    @CcnGwId.setter
    def CcnGwId(self, CcnGwId):
        self._CcnGwId = CcnGwId

    @property
    def VpcId(self):
        """VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `vpncloud`, `ccn`, or `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EngineVersion(self):
        """Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        """Instance account
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountRole(self):
        """The role used for cross-account migration, which can contain [a-zA-Z0-9\-\_]+.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def AccountMode(self):
        """The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        """Temporary SecretId, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Temporary SecretKey, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """Temporary token, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._DbKernel = params.get("DbKernel")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._InstanceId = params.get("InstanceId")
        self._CcnGwId = params.get("CcnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EngineVersion = params.get("EngineVersion")
        self._Account = params.get("Account")
        self._AccountRole = params.get("AccountRole")
        self._AccountMode = params.get("AccountMode")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBItem(AbstractModel):
    """Migration object information, which is case-sensitive when objects such as databases, tables, and views are configured.

    """

    def __init__(self):
        r"""
        :param _DbName: Name of the database to be migrated or synced, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _NewDbName: Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewDbName: str
        :param _SchemaName: The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param _NewSchemaName: Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewSchemaName: str
        :param _DBMode: Database selection mode, which is required if `ObjectMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBMode: str
        :param _SchemaMode: Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaMode: str
        :param _TableMode: Table selection mode, which is required if `DBMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param _Tables: The set of table objects, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of TableItem
        :param _ViewMode: View selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param _Views: The set of view objects, which is required if `ViewMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of ViewItem
        :param _RoleMode: Role selection mode, which is exclusive to PostgreSQL. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleMode: str
        :param _Roles: Role, which is exclusive to PostgreSQL and required if `RoleMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Roles: list of RoleItem
        :param _FunctionMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FunctionMode: str
        :param _TriggerMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TriggerMode: str
        :param _EventMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventMode: str
        :param _ProcedureMode: Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcedureMode: str
        :param _Functions: This parameter is required if `FunctionMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Functions: list of str
        :param _Procedures: This parameter is required if `ProcedureMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procedures: list of str
        :param _Events: This parameter is required if `EventMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of str
        :param _Triggers: This parameter is required if `TriggerMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Triggers: list of str
        """
        self._DbName = None
        self._NewDbName = None
        self._SchemaName = None
        self._NewSchemaName = None
        self._DBMode = None
        self._SchemaMode = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None
        self._RoleMode = None
        self._Roles = None
        self._FunctionMode = None
        self._TriggerMode = None
        self._EventMode = None
        self._ProcedureMode = None
        self._Functions = None
        self._Procedures = None
        self._Events = None
        self._Triggers = None

    @property
    def DbName(self):
        """Name of the database to be migrated or synced, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        """Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def SchemaName(self):
        """The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        """Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def DBMode(self):
        """Database selection mode, which is required if `ObjectMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBMode

    @DBMode.setter
    def DBMode(self, DBMode):
        self._DBMode = DBMode

    @property
    def SchemaMode(self):
        """Schema selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SchemaMode

    @SchemaMode.setter
    def SchemaMode(self, SchemaMode):
        self._SchemaMode = SchemaMode

    @property
    def TableMode(self):
        """Table selection mode, which is required if `DBMode` is `partial`. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """The set of table objects, which is required if `TableMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TableItem
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """View selection mode. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """The set of view objects, which is required if `ViewMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ViewItem
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def RoleMode(self):
        """Role selection mode, which is exclusive to PostgreSQL. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RoleMode

    @RoleMode.setter
    def RoleMode(self, RoleMode):
        self._RoleMode = RoleMode

    @property
    def Roles(self):
        """Role, which is exclusive to PostgreSQL and required if `RoleMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RoleItem
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def FunctionMode(self):
        """Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def TriggerMode(self):
        """Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def EventMode(self):
        """Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def ProcedureMode(self):
        """Sync mode. Valid values: `partial`, `all`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Functions(self):
        """This parameter is required if `FunctionMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def Procedures(self):
        """This parameter is required if `ProcedureMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def Events(self):
        """This parameter is required if `EventMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Triggers(self):
        """This parameter is required if `TriggerMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._NewDbName = params.get("NewDbName")
        self._SchemaName = params.get("SchemaName")
        self._NewSchemaName = params.get("NewSchemaName")
        self._DBMode = params.get("DBMode")
        self._SchemaMode = params.get("SchemaMode")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = TableItem()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = ViewItem()
                obj._deserialize(item)
                self._Views.append(obj)
        self._RoleMode = params.get("RoleMode")
        if params.get("Roles") is not None:
            self._Roles = []
            for item in params.get("Roles"):
                obj = RoleItem()
                obj._deserialize(item)
                self._Roles.append(obj)
        self._FunctionMode = params.get("FunctionMode")
        self._TriggerMode = params.get("TriggerMode")
        self._EventMode = params.get("EventMode")
        self._ProcedureMode = params.get("ProcedureMode")
        self._Functions = params.get("Functions")
        self._Procedures = params.get("Procedures")
        self._Events = params.get("Events")
        self._Triggers = params.get("Triggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """The database/table objects to be synced

    """

    def __init__(self):
        r"""
        :param _DbName: Name of the database to be migrated or synced, which is required if `ObjectMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _NewDbName: Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewDbName: str
        :param _DbMode: Database selection mode, which is required if `Mode` is `Partial`. Valid values: `All`, `Partial`. Note that the sync of advanced objects does not depend on this parameter. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbMode: str
        :param _SchemaName: The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type SchemaName: str
        :param _NewSchemaName: Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewSchemaName: str
        :param _TableMode: Table selection mode, which is required if `DBMode` is `Partial`. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableMode: str
        :param _Tables: The set of table objects, which is required if `TableMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of Table
        :param _ViewMode: View selection mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewMode: str
        :param _Views: The set of view objects, which is required if `ViewMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of View
        :param _FunctionMode: Sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FunctionMode: str
        :param _Functions: This parameter is required if `FunctionMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Functions: list of str
        :param _ProcedureMode: Sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcedureMode: str
        :param _Procedures: This parameter is required if `ProcedureMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procedures: list of str
        :param _TriggerMode: Trigger sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`. Currently, the advanced object “trigger” is not supported for data sync.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TriggerMode: str
        :param _Triggers: This parameter is used to specify the names of the triggers to be migrated when the value of `TriggerMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Triggers: list of str
        :param _EventMode: Event sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`. Currently, the advanced object “event” is not supported for data sync.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventMode: str
        :param _Events: This parameter is used to specify the names of the events to be migrated when the value of `EventMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Events: list of str
        """
        self._DbName = None
        self._NewDbName = None
        self._DbMode = None
        self._SchemaName = None
        self._NewSchemaName = None
        self._TableMode = None
        self._Tables = None
        self._ViewMode = None
        self._Views = None
        self._FunctionMode = None
        self._Functions = None
        self._ProcedureMode = None
        self._Procedures = None
        self._TriggerMode = None
        self._Triggers = None
        self._EventMode = None
        self._Events = None

    @property
    def DbName(self):
        """Name of the database to be migrated or synced, which is required if `ObjectMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def NewDbName(self):
        """Name of the database after migration or sync, which is the same as the source database name by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewDbName

    @NewDbName.setter
    def NewDbName(self, NewDbName):
        self._NewDbName = NewDbName

    @property
    def DbMode(self):
        """Database selection mode, which is required if `Mode` is `Partial`. Valid values: `All`, `Partial`. Note that the sync of advanced objects does not depend on this parameter. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbMode

    @DbMode.setter
    def DbMode(self, DbMode):
        self._DbMode = DbMode

    @property
    def SchemaName(self):
        """The schema to be migrated or synced
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SchemaName

    @SchemaName.setter
    def SchemaName(self, SchemaName):
        self._SchemaName = SchemaName

    @property
    def NewSchemaName(self):
        """Name of the schema after migration or sync
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewSchemaName

    @NewSchemaName.setter
    def NewSchemaName(self, NewSchemaName):
        self._NewSchemaName = NewSchemaName

    @property
    def TableMode(self):
        """Table selection mode, which is required if `DBMode` is `Partial`. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableMode

    @TableMode.setter
    def TableMode(self, TableMode):
        self._TableMode = TableMode

    @property
    def Tables(self):
        """The set of table objects, which is required if `TableMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Table
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def ViewMode(self):
        """View selection mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewMode

    @ViewMode.setter
    def ViewMode(self, ViewMode):
        self._ViewMode = ViewMode

    @property
    def Views(self):
        """The set of view objects, which is required if `ViewMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of View
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def FunctionMode(self):
        """Sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FunctionMode

    @FunctionMode.setter
    def FunctionMode(self, FunctionMode):
        self._FunctionMode = FunctionMode

    @property
    def Functions(self):
        """This parameter is required if `FunctionMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def ProcedureMode(self):
        """Sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcedureMode

    @ProcedureMode.setter
    def ProcedureMode(self, ProcedureMode):
        self._ProcedureMode = ProcedureMode

    @property
    def Procedures(self):
        """This parameter is required if `ProcedureMode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures

    @property
    def TriggerMode(self):
        """Trigger sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`. Currently, the advanced object “trigger” is not supported for data sync.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TriggerMode

    @TriggerMode.setter
    def TriggerMode(self, TriggerMode):
        self._TriggerMode = TriggerMode

    @property
    def Triggers(self):
        """This parameter is used to specify the names of the triggers to be migrated when the value of `TriggerMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def EventMode(self):
        """Event sync mode. Valid values: `All`, `Partial`. To sync an entire database, set this parameter to `All`. Currently, the advanced object “event” is not supported for data sync.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventMode

    @EventMode.setter
    def EventMode(self, EventMode):
        self._EventMode = EventMode

    @property
    def Events(self):
        """This parameter is used to specify the names of the events to be migrated when the value of `EventMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        self._NewDbName = params.get("NewDbName")
        self._DbMode = params.get("DbMode")
        self._SchemaName = params.get("SchemaName")
        self._NewSchemaName = params.get("NewSchemaName")
        self._TableMode = params.get("TableMode")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._ViewMode = params.get("ViewMode")
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = View()
                obj._deserialize(item)
                self._Views.append(obj)
        self._FunctionMode = params.get("FunctionMode")
        self._Functions = params.get("Functions")
        self._ProcedureMode = params.get("ProcedureMode")
        self._Procedures = params.get("Procedures")
        self._TriggerMode = params.get("TriggerMode")
        self._Triggers = params.get("Triggers")
        self._EventMode = params.get("EventMode")
        self._Events = params.get("Events")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTableObject(AbstractModel):
    """Migration object options, which tell DTS which database/table objects should be migrated.

    """

    def __init__(self):
        r"""
        :param _ObjectMode: Migration object type. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectMode: str
        :param _Databases: Migration object, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Databases: list of DBItem
        :param _AdvancedObjects: Advanced object types, such as trigger, function, procedure, event. Note: If you want to migrate and synchronize advanced objects, the corresponding advanced object type should be included in this configuration.Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedObjects: list of str
        """
        self._ObjectMode = None
        self._Databases = None
        self._AdvancedObjects = None

    @property
    def ObjectMode(self):
        """Migration object type. Valid values: `all`, `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Databases(self):
        """Migration object, which is required if `ObjectMode` is `partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DBItem
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        """Advanced object types, such as trigger, function, procedure, event. Note: If you want to migrate and synchronize advanced objects, the corresponding advanced object type should be included in this configuration.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects


    def _deserialize(self, params):
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = DBItem()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdlOption(AbstractModel):
    """DDL statement sync processing during data sync

    """

    def __init__(self):
        r"""
        :param _DdlObject: DDL type, such as database, table, view, and index.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlObject: str
        :param _DdlValue: DDL value. Valid values: [Create,Drop,Alter] for database <br>[Create,Drop,Alter,Truncate,Rename] for table <br/>[Create,Drop] for view <br/>[Create,Drop] for index
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlValue: list of str
        """
        self._DdlObject = None
        self._DdlValue = None

    @property
    def DdlObject(self):
        """DDL type, such as database, table, view, and index.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DdlObject

    @DdlObject.setter
    def DdlObject(self, DdlObject):
        self._DdlObject = DdlObject

    @property
    def DdlValue(self):
        """DDL value. Valid values: [Create,Drop,Alter] for database <br>[Create,Drop,Alter,Truncate,Rename] for table <br/>[Create,Drop] for view <br/>[Create,Drop] for index
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DdlValue

    @DdlValue.setter
    def DdlValue(self, DdlValue):
        self._DdlValue = DdlValue


    def _deserialize(self, params):
        self._DdlObject = params.get("DdlObject")
        self._DdlValue = params.get("DdlValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskRequest(AbstractModel):
    """DeleteCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompareTaskResponse(AbstractModel):
    """DeleteCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteConsumerGroupRequest(AbstractModel):
    """DeleteConsumerGroup request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: ID of the data subscription instance
        :type SubscribeId: str
        :param _ConsumerGroupName: Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.Please make sure the consumer group name is correct.
        :type ConsumerGroupName: str
        :param _AccountName: Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.Please make sure the account name is correct.
        :type AccountName: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None

    @property
    def SubscribeId(self):
        """ID of the data subscription instance
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.Please make sure the consumer group name is correct.
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.Please make sure the account name is correct.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerGroupResponse(AbstractModel):
    """DeleteConsumerGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCheckSyncJobResultRequest(AbstractModel):
    """DescribeCheckSyncJobResult request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task. This parameter is required.
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task. This parameter is required.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSyncJobResultResponse(AbstractModel):
    """DescribeCheckSyncJobResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Execution status of the check task. Valid values: `notStarted`, `running`, `failed`, `success`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _StepCount: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCount: int
        :param _StepCur: The current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCur: int
        :param _Progress: Overall progress. Value range: 0-100.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param _StepInfos: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfos: list of StepInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._StepCount = None
        self._StepCur = None
        self._Progress = None
        self._StepInfos = None
        self._RequestId = None

    @property
    def Status(self):
        """Execution status of the check task. Valid values: `notStarted`, `running`, `failed`, `success`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        """Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        """The current step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        """Overall progress. Value range: 0-100.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        """Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StepCount = params.get("StepCount")
        self._StepCur = params.get("StepCur")
        self._Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCompareReportRequest(AbstractModel):
    """DescribeCompareReport request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _CompareTaskId: Check task ID
        :type CompareTaskId: str
        :param _DifferenceLimit: Number of inconsistent objects to be returned
        :type DifferenceLimit: int
        :param _DifferenceOffset: Offset of inconsistent objects
        :type DifferenceOffset: int
        :param _DifferenceDB: Search criterion: Inconsistent database name
        :type DifferenceDB: str
        :param _DifferenceTable: Search criterion: Inconsistent table name
        :type DifferenceTable: str
        :param _SkippedLimit: Number of unchecked objects to be returned
        :type SkippedLimit: int
        :param _SkippedOffset: Offset of unchecked objects
        :type SkippedOffset: int
        :param _SkippedDB: Search criterion: Unchecked database name
        :type SkippedDB: str
        :param _SkippedTable: Search criterion: Unchecked table name
        :type SkippedTable: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._DifferenceLimit = None
        self._DifferenceOffset = None
        self._DifferenceDB = None
        self._DifferenceTable = None
        self._SkippedLimit = None
        self._SkippedOffset = None
        self._SkippedDB = None
        self._SkippedTable = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Check task ID
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def DifferenceLimit(self):
        """Number of inconsistent objects to be returned
        :rtype: int
        """
        return self._DifferenceLimit

    @DifferenceLimit.setter
    def DifferenceLimit(self, DifferenceLimit):
        self._DifferenceLimit = DifferenceLimit

    @property
    def DifferenceOffset(self):
        """Offset of inconsistent objects
        :rtype: int
        """
        return self._DifferenceOffset

    @DifferenceOffset.setter
    def DifferenceOffset(self, DifferenceOffset):
        self._DifferenceOffset = DifferenceOffset

    @property
    def DifferenceDB(self):
        """Search criterion: Inconsistent database name
        :rtype: str
        """
        return self._DifferenceDB

    @DifferenceDB.setter
    def DifferenceDB(self, DifferenceDB):
        self._DifferenceDB = DifferenceDB

    @property
    def DifferenceTable(self):
        """Search criterion: Inconsistent table name
        :rtype: str
        """
        return self._DifferenceTable

    @DifferenceTable.setter
    def DifferenceTable(self, DifferenceTable):
        self._DifferenceTable = DifferenceTable

    @property
    def SkippedLimit(self):
        """Number of unchecked objects to be returned
        :rtype: int
        """
        return self._SkippedLimit

    @SkippedLimit.setter
    def SkippedLimit(self, SkippedLimit):
        self._SkippedLimit = SkippedLimit

    @property
    def SkippedOffset(self):
        """Offset of unchecked objects
        :rtype: int
        """
        return self._SkippedOffset

    @SkippedOffset.setter
    def SkippedOffset(self, SkippedOffset):
        self._SkippedOffset = SkippedOffset

    @property
    def SkippedDB(self):
        """Search criterion: Unchecked database name
        :rtype: str
        """
        return self._SkippedDB

    @SkippedDB.setter
    def SkippedDB(self, SkippedDB):
        self._SkippedDB = SkippedDB

    @property
    def SkippedTable(self):
        """Search criterion: Unchecked table name
        :rtype: str
        """
        return self._SkippedTable

    @SkippedTable.setter
    def SkippedTable(self, SkippedTable):
        self._SkippedTable = SkippedTable


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._DifferenceLimit = params.get("DifferenceLimit")
        self._DifferenceOffset = params.get("DifferenceOffset")
        self._DifferenceDB = params.get("DifferenceDB")
        self._DifferenceTable = params.get("DifferenceTable")
        self._SkippedLimit = params.get("SkippedLimit")
        self._SkippedOffset = params.get("SkippedOffset")
        self._SkippedDB = params.get("SkippedDB")
        self._SkippedTable = params.get("SkippedTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareReportResponse(AbstractModel):
    """DescribeCompareReport response structure.

    """

    def __init__(self):
        r"""
        :param _Abstract: Summary information of data consistency check
Note: This field may return null, indicating that no valid values can be obtained.
        :type Abstract: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        :param _Detail: Data consistency check details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Abstract = None
        self._Detail = None
        self._RequestId = None

    @property
    def Abstract(self):
        """Summary information of data consistency check
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareAbstractInfo`
        """
        return self._Abstract

    @Abstract.setter
    def Abstract(self, Abstract):
        self._Abstract = Abstract

    @property
    def Detail(self):
        """Data consistency check details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareDetailInfo`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Abstract") is not None:
            self._Abstract = CompareAbstractInfo()
            self._Abstract._deserialize(params.get("Abstract"))
        if params.get("Detail") is not None:
            self._Detail = CompareDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        self._RequestId = params.get("RequestId")


class DescribeCompareTasksRequest(AbstractModel):
    """DescribeCompareTasks request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _Limit: Number of tasks to be displayed per page. Default value: `20`.
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _CompareTaskId: Check task ID
        :type CompareTaskId: str
        :param _Status: Data consistency check task status. Valid values: `created`, `readyRun`, `running`, `success`, `stopping`, `failed`, `canceled`.
        :type Status: list of str
        """
        self._JobId = None
        self._Limit = None
        self._Offset = None
        self._CompareTaskId = None
        self._Status = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        """Number of tasks to be displayed per page. Default value: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CompareTaskId(self):
        """Check task ID
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def Status(self):
        """Data consistency check task status. Valid values: `created`, `readyRun`, `running`, `success`, `stopping`, `failed`, `canceled`.
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CompareTaskId = params.get("CompareTaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompareTasksResponse(AbstractModel):
    """DescribeCompareTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Items: List of data consistency check tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of CompareTaskItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """List of data consistency check tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CompareTaskItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CompareTaskItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConsumerGroupsRequest(AbstractModel):
    """DescribeConsumerGroups request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _Offset: Starting offset for returned results. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned at a time. Default value: 10.
        :type Limit: int
        """
        self._SubscribeId = None
        self._Offset = None
        self._Limit = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Offset(self):
        """Starting offset for returned results. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned at a time. Default value: 10.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupsResponse(AbstractModel):
    """DescribeConsumerGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of consumer groups under the specific instance
        :type TotalCount: int
        :param _Items: Consumer group list
        :type Items: list of GroupInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of consumer groups under the specific instance
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Consumer group list
        :rtype: list of GroupInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrateDBInstancesRequest(AbstractModel):
    """DescribeMigrateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _DatabaseType: Database type, such as `mysql`.
        :type DatabaseType: str
        :param _MigrateRole: Specifies whether the instance is the migration source or target. Valid values: `src` (source); `dts` (target).
        :type MigrateRole: str
        :param _InstanceId: Database instance ID
        :type InstanceId: str
        :param _InstanceName: Database instance name
        :type InstanceName: str
        :param _Limit: Number of results to be returned
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
        :type AccountMode: str
        :param _TmpSecretId: ID of the temporary key, which is required if the operation is performed across accounts.
        :type TmpSecretId: str
        :param _TmpSecretKey: Key of the temporary key, which is required if the operation is performed across accounts.
        :type TmpSecretKey: str
        :param _TmpToken: Temporary token, which is required if the operation is performed across accounts.
        :type TmpToken: str
        """
        self._DatabaseType = None
        self._MigrateRole = None
        self._InstanceId = None
        self._InstanceName = None
        self._Limit = None
        self._Offset = None
        self._AccountMode = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None

    @property
    def DatabaseType(self):
        """Database type, such as `mysql`.
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def MigrateRole(self):
        """Specifies whether the instance is the migration source or target. Valid values: `src` (source); `dts` (target).
        :rtype: str
        """
        return self._MigrateRole

    @MigrateRole.setter
    def MigrateRole(self, MigrateRole):
        self._MigrateRole = MigrateRole

    @property
    def InstanceId(self):
        """Database instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Database instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Limit(self):
        """Number of results to be returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountMode(self):
        """The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def TmpSecretId(self):
        """ID of the temporary key, which is required if the operation is performed across accounts.
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Key of the temporary key, which is required if the operation is performed across accounts.
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """Temporary token, which is required if the operation is performed across accounts.
        :rtype: str
        """
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken


    def _deserialize(self, params):
        self._DatabaseType = params.get("DatabaseType")
        self._MigrateRole = params.get("MigrateRole")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountMode = params.get("AccountMode")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrateDBInstancesResponse(AbstractModel):
    """DescribeMigrateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Instances: Instance list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Instances: list of MigrateDBItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible items
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """Instance list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MigrateDBItem
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = MigrateDBItem()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigrationCheckJobRequest(AbstractModel):
    """DescribeMigrationCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationCheckJobResponse(AbstractModel):
    """DescribeMigrationCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Check task execution status. Valid values: `notStarted`, `running`, `failed`, `success`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _BriefMsg: Check task result message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param _StepInfo: Check step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: list of CheckStep
        :param _CheckFlag: Check result. Valid values: `checkPass`, `checkNotPass`.
        :type CheckFlag: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._BriefMsg = None
        self._StepInfo = None
        self._CheckFlag = None
        self._RequestId = None

    @property
    def Status(self):
        """Check task execution status. Valid values: `notStarted`, `running`, `failed`, `success`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BriefMsg(self):
        """Check task result message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def StepInfo(self):
        """Check step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CheckStep
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def CheckFlag(self):
        """Check result. Valid values: `checkPass`, `checkNotPass`.
        :rtype: str
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._BriefMsg = params.get("BriefMsg")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = CheckStep()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _JobName: Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param _CreateTime: Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _StartTime: Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _BriefMsg: Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param _Status: Task status. Valid values: `created`(Created), `checking` (Checking), `checkPass` (Check passed), `checkNotPass` (Check not passed), `readyRun` (Ready for running), `running` (Running), `readyComplete` (Preparation completed), `success` (Successful), `failed` (Failed), `stopping` (Stopping), `completing` (Completing), `pausing` (Pausing), `manualPaused` (Paused). Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Action: Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: Information of the migration task execution process. The check and migration step information will be displayed in the check and migration stages respectively.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _RunMode: Running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param _ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param _MigrateOption: Migration options, which describe how the task performs migration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param _CheckStepInfo: Check task running details
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckStepInfo: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        :param _TradeInfo: Billing information
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _ErrorInfo: Task error information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: list of ErrorInfoItem
        :param _DumperResumeCtrl: Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
        :type DumperResumeCtrl: str
        :param _RateLimitOption: Task throttling information
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitOption: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._BriefMsg = None
        self._Status = None
        self._Action = None
        self._StepInfo = None
        self._SrcInfo = None
        self._DstInfo = None
        self._CompareTask = None
        self._Tags = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._MigrateOption = None
        self._CheckStepInfo = None
        self._TradeInfo = None
        self._ErrorInfo = None
        self._DumperResumeCtrl = None
        self._RateLimitOption = None
        self._RequestId = None

    @property
    def JobId(self):
        """Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        """Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        """Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        """Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        """Task status. Valid values: `created`(Created), `checking` (Checking), `checkPass` (Check passed), `checkNotPass` (Check not passed), `readyRun` (Ready for running), `running` (Running), `readyComplete` (Preparation completed), `success` (Successful), `failed` (Failed), `stopping` (Stopping), `completing` (Completing), `pausing` (Pausing), `manualPaused` (Paused). Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Action(self):
        """Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        """Information of the migration task execution process. The check and migration step information will be displayed in the check and migration stages respectively.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        """Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        """Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        """
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def Tags(self):
        """Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RunMode(self):
        """Running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def MigrateOption(self):
        """Migration options, which describe how the task performs migration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def CheckStepInfo(self):
        """Check task running details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CheckStepInfo`
        """
        return self._CheckStepInfo

    @CheckStepInfo.setter
    def CheckStepInfo(self, CheckStepInfo):
        self._CheckStepInfo = CheckStepInfo

    @property
    def TradeInfo(self):
        """Billing information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        """
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def ErrorInfo(self):
        """Task error information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ErrorInfoItem
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def DumperResumeCtrl(self):
        """Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl

    @property
    def RateLimitOption(self):
        """Task throttling information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        """
        return self._RateLimitOption

    @RateLimitOption.setter
    def RateLimitOption(self, RateLimitOption):
        self._RateLimitOption = RateLimitOption

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BriefMsg = params.get("BriefMsg")
        self._Status = params.get("Status")
        if params.get("Action") is not None:
            self._Action = MigrateAction()
            self._Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self._StepInfo = MigrateDetailInfo()
            self._StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self._CompareTask = CompareTaskInfo()
            self._CompareTask._deserialize(params.get("CompareTask"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("CheckStepInfo") is not None:
            self._CheckStepInfo = CheckStepInfo()
            self._CheckStepInfo._deserialize(params.get("CheckStepInfo"))
        if params.get("TradeInfo") is not None:
            self._TradeInfo = TradeInfo()
            self._TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfoItem()
                obj._deserialize(item)
                self._ErrorInfo.append(obj)
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
        if params.get("RateLimitOption") is not None:
            self._RateLimitOption = RateLimitOption()
            self._RateLimitOption._deserialize(params.get("RateLimitOption"))
        self._RequestId = params.get("RequestId")


class DescribeMigrationJobsRequest(AbstractModel):
    """DescribeMigrationJobs request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID such as `dts-amm1jw5q`
        :type JobId: str
        :param _JobName: Data migration task name
        :type JobName: str
        :param _Status: Data migration task status. Valid values: `created`, `checking`, `checkPass`, `checkNotPass`, `readyRun`, `running`, `readyComplete`, `success`, `failed`, `stopping`, `completing`.
        :type Status: list of str
        :param _SrcInstanceId: Source instance ID in the format of `cdb-c1nl9rpv`
        :type SrcInstanceId: str
        :param _SrcRegion: Source instance region, such as `ap-guangzhou`.
        :type SrcRegion: str
        :param _SrcDatabaseType: Source database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :type SrcDatabaseType: list of str
        :param _SrcAccessType: Source instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :type SrcAccessType: list of str
        :param _DstInstanceId: Target instance ID in the format of `cdb-c1nl9rpv`
        :type DstInstanceId: str
        :param _DstRegion: Target instance region, such as `ap-guangzhou`.
        :type DstRegion: str
        :param _DstDatabaseType: Target database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :type DstDatabaseType: list of str
        :param _DstAccessType: Target instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :type DstAccessType: list of str
        :param _RunMode: Task running mode. Valid values: `immediate`, `timed`.
        :type RunMode: str
        :param _OrderSeq: Sorting order. Valid values: `asc`, `desc`. Default value: `desc` by creation time.
        :type OrderSeq: str
        :param _Limit: Number of instances to be returned. Value range: [1,100]. Default value: `20`.
        :type Limit: int
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _TagFilters: Tag filter
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Status = None
        self._SrcInstanceId = None
        self._SrcRegion = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._DstInstanceId = None
        self._DstRegion = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._RunMode = None
        self._OrderSeq = None
        self._Limit = None
        self._Offset = None
        self._TagFilters = None

    @property
    def JobId(self):
        """Data migration task ID such as `dts-amm1jw5q`
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Data migration task name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        """Data migration task status. Valid values: `created`, `checking`, `checkPass`, `checkNotPass`, `readyRun`, `running`, `readyComplete`, `success`, `failed`, `stopping`, `completing`.
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcInstanceId(self):
        """Source instance ID in the format of `cdb-c1nl9rpv`
        :rtype: str
        """
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def SrcRegion(self):
        """Source instance region, such as `ap-guangzhou`.
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        """Source database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :rtype: list of str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """Source instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :rtype: list of str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def DstInstanceId(self):
        """Target instance ID in the format of `cdb-c1nl9rpv`
        :rtype: str
        """
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def DstRegion(self):
        """Target instance region, such as `ap-guangzhou`.
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        """Target database type, such as `sqlserver`, `mysql`, `mongodb`, `redis`, `tendis`, `keewidb`, `clickhouse`, `cynosdbmysql`, `percona`, `tdsqlpercona`, `mariadb`, `tdsqlmysql`, `postgresql.
        :rtype: list of str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """Target instance access type. Valid values: `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `cdb` (Database); `cvm` (self-build on CVM).
        :rtype: list of str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def RunMode(self):
        """Task running mode. Valid values: `immediate`, `timed`.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def OrderSeq(self):
        """Sorting order. Valid values: `asc`, `desc`. Default value: `desc` by creation time.
        :rtype: str
        """
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Limit(self):
        """Number of instances to be returned. Value range: [1,100]. Default value: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TagFilters(self):
        """Tag filter
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Status = params.get("Status")
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._SrcRegion = params.get("SrcRegion")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        self._DstInstanceId = params.get("DstInstanceId")
        self._DstRegion = params.get("DstRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        self._RunMode = params.get("RunMode")
        self._OrderSeq = params.get("OrderSeq")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationJobsResponse(AbstractModel):
    """DescribeMigrationJobs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of migration tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _JobList: Migration task list
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobList: list of JobItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of migration tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        """Migration task list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of JobItem
        """
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = JobItem()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModifyCheckSyncJobResultRequest(AbstractModel):
    """DescribeModifyCheckSyncJobResult request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModifyCheckSyncJobResultResponse(AbstractModel):
    """DescribeModifyCheckSyncJobResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Execution status of the check task Valid values: `notStarted` (Not started), `running` (Running), `failed` (Failed), `success` (Successful).
        :type Status: str
        :param _StepCount: Number of check steps Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCount: int
        :param _StepCur: Current step Note: This field may return null, indicating that no valid values can be obtained.
        :type StepCur: int
        :param _Progress: Overall progress. Value range: 0-100. Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param _StepInfos: Step details Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfos: list of StepInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._StepCount = None
        self._StepCur = None
        self._Progress = None
        self._StepInfos = None
        self._RequestId = None

    @property
    def Status(self):
        """Execution status of the check task Valid values: `notStarted` (Not started), `running` (Running), `failed` (Failed), `success` (Successful).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepCount(self):
        """Number of check steps Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepCount

    @StepCount.setter
    def StepCount(self, StepCount):
        self._StepCount = StepCount

    @property
    def StepCur(self):
        """Current step Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepCur

    @StepCur.setter
    def StepCur(self, StepCur):
        self._StepCur = StepCur

    @property
    def Progress(self):
        """Overall progress. Value range: 0-100. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepInfos(self):
        """Step details Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StepCount = params.get("StepCount")
        self._StepCur = params.get("StepCur")
        self._Progress = params.get("Progress")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOffsetByTimeRequest(AbstractModel):
    """DescribeOffsetByTime request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _Time: Timestamp, the format is: Y-m-d h:m:s. If the input time is much later than the current time, this is equivalent to the latest offset; if the input time is much earlier than the current time, this is equivalent to the oldest offset; if the input is empty, the default time is 0, which is the oldest offset to be queried.
        :type Time: str
        """
        self._SubscribeId = None
        self._Time = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Time(self):
        """Timestamp, the format is: Y-m-d h:m:s. If the input time is much later than the current time, this is equivalent to the latest offset; if the input time is much earlier than the current time, this is equivalent to the oldest offset; if the input is empty, the default time is 0, which is the oldest offset to be queried.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOffsetByTimeResponse(AbstractModel):
    """DescribeOffsetByTime response structure.

    """

    def __init__(self):
        r"""
        :param _Items: Time and Offset response.
        :type Items: list of OffsetTimeMap
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        """Time and Offset response.
        :rtype: list of OffsetTimeMap
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OffsetTimeMap()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeCheckJobRequest(AbstractModel):
    """DescribeSubscribeCheckJob request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeCheckJobResponse(AbstractModel):
    """DescribeSubscribeCheckJob response structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _Message: Failure or error prompts, success signals 'success'.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Status: Job running status. Valid values: running, failed, success.
        :type Status: str
        :param _Progress: Current overall progress. Value range: 0-100.
        :type Progress: int
        :param _StepAll: Total check steps
        :type StepAll: int
        :param _StepNow: Current step in execution
        :type StepNow: int
        :param _Steps: Running status of each stepNote: This field may return null, indicating that no valid values can be obtained.
        :type Steps: list of SubscribeCheckStepInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscribeId = None
        self._Message = None
        self._Status = None
        self._Progress = None
        self._StepAll = None
        self._StepNow = None
        self._Steps = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def Message(self):
        """Failure or error prompts, success signals 'success'.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """Job running status. Valid values: running, failed, success.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        """Current overall progress. Value range: 0-100.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StepAll(self):
        """Total check steps
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """Current step in execution
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Steps(self):
        """Running status of each stepNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubscribeCheckStepInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = SubscribeCheckStepInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeDetailRequest(AbstractModel):
    """DescribeSubscribeDetail request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeDetailResponse(AbstractModel):
    """DescribeSubscribeDetail response structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: The ID of the data subscription, such as subs-b6x64o31tm
        :type SubscribeId: str
        :param _SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param _Product: Subscription database type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :type Product: str
        :param _InstanceId: The subscribed cloud database instance ID. This value only makes sense if cloud database is subscribed. Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceStatus: The subscribed cloud database instance status. This value only makes sense if cloud database is subscribed. Valid values: running, isolated, offline.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStatus: str
        :param _Status: Subscription task billing status. Valid values: normal, isolating, isolated, offline, post2PrePayIng.
        :type Status: str
        :param _SubsStatus: Subscription task status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :type SubsStatus: str
        :param _ModifyTime: Modification time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _CreateTime: Creation time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _IsolateTime: Isolation time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateTime: str
        :param _ExpireTime: Expiration time for monthly subscription tasks, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _OfflineTime: Offline time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        :param _PayType: Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :type PayType: int
        :param _AutoRenewFlag: Auto-renewal flag. It is meaningful only when PayType=0. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled).
        :type AutoRenewFlag: int
        :param _Region: The region where the task is located
        :type Region: str
        :param _Topic: Kafka topic
Note: This field may return null, indicating that no valid values can be obtained.
        :type Topic: str
        :param _Broker: Broker address of Kafka serviceNote: This field may return null, indicating that no valid values can be obtained.
        :type Broker: str
        :param _SubscribeMode: Data subscription type. Valid values for non-mongo Product: all (full instance update); dml (data update); ddl (structure update); dmlAndDdl (data + structure update). Valid values for mongo Product: all (full instance update); database (subscribe to a table); collection (subscribe to a collection).Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeMode: str
        :param _Protocol: Subscription data format. If it is empty, the default format is used: mysql\cynosdbmysql\mariadb\percona\tdsqlpercona\tdpg is protobuf, mongo is json. When DatabaseType is mysql and cynosdbmysql, there are three optional protocols: protobuf\avro\json. For details on data format, please refer to the consumption demo documentation on the official website.Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _SubscribeObjects: Information of subscribed tableNote: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeObjects: list of SubscribeObject
        :param _KafkaConfig: Kafka configuration information
Note: This field may return null, indicating that no valid values can be obtained.
        :type KafkaConfig: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        :param _AccessType: Source database access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC). Note: The specific optional values depend on the current link support capabilities.Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessType: str
        :param _Endpoints: Access type information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Endpoints: list of EndpointItem
        :param _PipelineInfo: Mongo output aggregation settings
Note: This field may return null, indicating that no valid values can be obtained.
        :type PipelineInfo: list of PipelineInfo
        :param _Tags: TagNote: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _Errors: Subscription task error information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of SubsErr
        :param _ExtraAttr: Additional information added for the business. The parameter name is called key, and the parameter value is called value.Optional parameters for mysql: ProcessXA. Fill in true to process, others will not be processed.Optional parameters for mongo: SubscribeType. Currently only changeStream is supported.Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._Status = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._PayType = None
        self._AutoRenewFlag = None
        self._Region = None
        self._Topic = None
        self._Broker = None
        self._SubscribeMode = None
        self._Protocol = None
        self._SubscribeObjects = None
        self._KafkaConfig = None
        self._AccessType = None
        self._Endpoints = None
        self._PipelineInfo = None
        self._Tags = None
        self._Errors = None
        self._ExtraAttr = None
        self._RequestId = None

    @property
    def SubscribeId(self):
        """The ID of the data subscription, such as subs-b6x64o31tm
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """Data subscription instance name
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def Product(self):
        """Subscription database type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """The subscribed cloud database instance ID. This value only makes sense if cloud database is subscribed. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """The subscribed cloud database instance status. This value only makes sense if cloud database is subscribed. Valid values: running, isolated, offline.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def Status(self):
        """Subscription task billing status. Valid values: normal, isolating, isolated, offline, post2PrePayIng.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """Subscription task status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        """Modification time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        """Creation time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        """Isolation time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """Expiration time for monthly subscription tasks, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """Offline time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def PayType(self):
        """Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. It is meaningful only when PayType=0. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Region(self):
        """The region where the task is located
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Topic(self):
        """Kafka topic
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Broker(self):
        """Broker address of Kafka serviceNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Broker

    @Broker.setter
    def Broker(self, Broker):
        self._Broker = Broker

    @property
    def SubscribeMode(self):
        """Data subscription type. Valid values for non-mongo Product: all (full instance update); dml (data update); ddl (structure update); dmlAndDdl (data + structure update). Valid values for mongo Product: all (full instance update); database (subscribe to a table); collection (subscribe to a collection).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubscribeMode

    @SubscribeMode.setter
    def SubscribeMode(self, SubscribeMode):
        self._SubscribeMode = SubscribeMode

    @property
    def Protocol(self):
        """Subscription data format. If it is empty, the default format is used: mysql\cynosdbmysql\mariadb\percona\tdsqlpercona\tdpg is protobuf, mongo is json. When DatabaseType is mysql and cynosdbmysql, there are three optional protocols: protobuf\avro\json. For details on data format, please refer to the consumption demo documentation on the official website.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SubscribeObjects(self):
        """Information of subscribed tableNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubscribeObject
        """
        return self._SubscribeObjects

    @SubscribeObjects.setter
    def SubscribeObjects(self, SubscribeObjects):
        self._SubscribeObjects = SubscribeObjects

    @property
    def KafkaConfig(self):
        """Kafka configuration information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SubscribeKafkaConfig`
        """
        return self._KafkaConfig

    @KafkaConfig.setter
    def KafkaConfig(self, KafkaConfig):
        self._KafkaConfig = KafkaConfig

    @property
    def AccessType(self):
        """Source database access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC). Note: The specific optional values depend on the current link support capabilities.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """Access type information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def PipelineInfo(self):
        """Mongo output aggregation settings
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo

    @property
    def Tags(self):
        """TagNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Errors(self):
        """Subscription task error information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubsErr
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def ExtraAttr(self):
        """Additional information added for the business. The parameter name is called key, and the parameter value is called value.Optional parameters for mysql: ProcessXA. Fill in true to process, others will not be processed.Optional parameters for mongo: SubscribeType. Currently only changeStream is supported.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._PayType = params.get("PayType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Region = params.get("Region")
        self._Topic = params.get("Topic")
        self._Broker = params.get("Broker")
        self._SubscribeMode = params.get("SubscribeMode")
        self._Protocol = params.get("Protocol")
        if params.get("SubscribeObjects") is not None:
            self._SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self._SubscribeObjects.append(obj)
        if params.get("KafkaConfig") is not None:
            self._KafkaConfig = SubscribeKafkaConfig()
            self._KafkaConfig._deserialize(params.get("KafkaConfig"))
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeJobsRequest(AbstractModel):
    """DescribeSubscribeJobs request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription ID (exact match)
        :type SubscribeId: str
        :param _SubscribeName: Subscription name (prefix fuzzy match)
        :type SubscribeName: str
        :param _InstanceId: Subscribed cloud database instance ID (exact match)
        :type InstanceId: str
        :param _PayType: Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :type PayType: int
        :param _Product: Subscribed database product. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :type Product: str
        :param _Status: Data subscription lifecycle status. Valid values: normal, isolating, isolated, offline, post2PrePayIng.
        :type Status: list of str
        :param _SubsStatus: Data subscription status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :type SubsStatus: list of str
        :param _Offset: Starting offset for returned results. Default value: 0.
        :type Offset: int
        :param _Limit: Number of results to be returned at a time. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _OrderDirection: Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time.
        :type OrderDirection: str
        :param _TagFilters: Tag filter condition, the relationship between multiple TagFilters is and.
        :type TagFilters: list of TagFilter
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._InstanceId = None
        self._PayType = None
        self._Product = None
        self._Status = None
        self._SubsStatus = None
        self._Offset = None
        self._Limit = None
        self._OrderDirection = None
        self._TagFilters = None

    @property
    def SubscribeId(self):
        """Subscription ID (exact match)
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """Subscription name (prefix fuzzy match)
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def InstanceId(self):
        """Subscribed cloud database instance ID (exact match)
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PayType(self):
        """Payment method. Valid values: 0 (monthly subscription); 1 (pay-as-you-go).
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def Product(self):
        """Subscribed database product. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Status(self):
        """Data subscription lifecycle status. Valid values: normal, isolating, isolated, offline, post2PrePayIng.
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """Data subscription status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :rtype: list of str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def Offset(self):
        """Starting offset for returned results. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of results to be returned at a time. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderDirection(self):
        """Sorting order. Valid values: DESC, ASC. Default value: DESC, indicating descending by creation time.
        :rtype: str
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def TagFilters(self):
        """Tag filter condition, the relationship between multiple TagFilters is and.
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._InstanceId = params.get("InstanceId")
        self._PayType = params.get("PayType")
        self._Product = params.get("Product")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderDirection = params.get("OrderDirection")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeJobsResponse(AbstractModel):
    """DescribeSubscribeJobs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances.
        :type TotalCount: int
        :param _Items: Information list of data subscription instances
        :type Items: list of SubscribeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Information list of data subscription instances
        :rtype: list of SubscribeInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscribeReturnableRequest(AbstractModel):
    """DescribeSubscribeReturnable request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscribeReturnableResponse(AbstractModel):
    """DescribeSubscribeReturnable response structure.

    """

    def __init__(self):
        r"""
        :param _IsReturnable: Whether the instance is returnable
        :type IsReturnable: bool
        :param _ReturnFailMessage: Reason for the non-returnability
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReturnFailMessage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsReturnable = None
        self._ReturnFailMessage = None
        self._RequestId = None

    @property
    def IsReturnable(self):
        """Whether the instance is returnable
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def ReturnFailMessage(self):
        """Reason for the non-returnability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReturnFailMessage

    @ReturnFailMessage.setter
    def ReturnFailMessage(self, ReturnFailMessage):
        self._ReturnFailMessage = ReturnFailMessage

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsReturnable = params.get("IsReturnable")
        self._ReturnFailMessage = params.get("ReturnFailMessage")
        self._RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID, such as `sync-werwfs23`.
        :type JobId: str
        :param _JobName: Sync task name
        :type JobName: str
        :param _Order: Sort by field, such as `CreateTime`.
        :type Order: str
        :param _OrderSeq: Sorting order. Valid values: `ASC`, `DESC`. Default value: `DESC` by `CreateTime`.
        :type OrderSeq: str
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of sync task instances to be returned. Value range: [1,100]. Default value: `20`.
        :type Limit: int
        :param _Status: The set of status values, such as `Initialized,CheckPass,Running,ResumableErr,Stopped`.
        :type Status: list of str
        :param _RunMode: Running mode. Valid values: `Immediate`, `Timed`.
        :type RunMode: str
        :param _JobType: Task type, such as `mysql2mysql` (sync from MySQL to MySQL).
        :type JobType: str
        :param _PayMode: Billing mode. Valid values: `PrePay` (prepaid); `PostPay` (postpaid).
        :type PayMode: str
        :param _TagFilters: tag
        :type TagFilters: list of TagFilter
        """
        self._JobId = None
        self._JobName = None
        self._Order = None
        self._OrderSeq = None
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._RunMode = None
        self._JobType = None
        self._PayMode = None
        self._TagFilters = None

    @property
    def JobId(self):
        """Sync task ID, such as `sync-werwfs23`.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Sync task name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Order(self):
        """Sort by field, such as `CreateTime`.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderSeq(self):
        """Sorting order. Valid values: `ASC`, `DESC`. Default value: `DESC` by `CreateTime`.
        :rtype: str
        """
        return self._OrderSeq

    @OrderSeq.setter
    def OrderSeq(self, OrderSeq):
        self._OrderSeq = OrderSeq

    @property
    def Offset(self):
        """Offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of sync task instances to be returned. Value range: [1,100]. Default value: `20`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """The set of status values, such as `Initialized,CheckPass,Running,ResumableErr,Stopped`.
        :rtype: list of str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        """Running mode. Valid values: `Immediate`, `Timed`.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def JobType(self):
        """Task type, such as `mysql2mysql` (sync from MySQL to MySQL).
        :rtype: str
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def PayMode(self):
        """Billing mode. Valid values: `PrePay` (prepaid); `PostPay` (postpaid).
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TagFilters(self):
        """tag
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Order = params.get("Order")
        self._OrderSeq = params.get("OrderSeq")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._RunMode = params.get("RunMode")
        self._JobType = params.get("JobType")
        self._PayMode = params.get("PayMode")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _JobList: Array of task details
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobList: list of SyncJobInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobList(self):
        """Array of task details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SyncJobInfo
        """
        return self._JobList

    @JobList.setter
    def JobList(self, JobList):
        self._JobList = JobList

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self._JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self._JobList.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyIsolatedSubscribeRequest(AbstractModel):
    """DestroyIsolatedSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyIsolatedSubscribeResponse(AbstractModel):
    """DestroyIsolatedSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DestroyMigrateJobRequest(AbstractModel):
    """DestroyMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyMigrateJobResponse(AbstractModel):
    """DestroyMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DestroySyncJobRequest(AbstractModel):
    """DestroySyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySyncJobResponse(AbstractModel):
    """DestroySyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DetailCheckItem(AbstractModel):
    """Specific check item in this check step

    """

    def __init__(self):
        r"""
        :param _CheckItemName: Check item name, such as source database permission check.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckItemName: str
        :param _Description: Check item details
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _CheckResult: Check item result. Valid values: `pass` (pass); `failed` (failure); `warning` (pass with warning).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckResult: str
        :param _FailureReason: The cause of the check item failure
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailureReason: str
        :param _Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param _ErrorLog: Execution error log
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLog: list of str
        :param _HelpDoc: URL of the detailed help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: list of str
        :param _SkipInfo: Prompt text for ignoring a risk
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkipInfo: str
        """
        self._CheckItemName = None
        self._Description = None
        self._CheckResult = None
        self._FailureReason = None
        self._Solution = None
        self._ErrorLog = None
        self._HelpDoc = None
        self._SkipInfo = None

    @property
    def CheckItemName(self):
        """Check item name, such as source database permission check.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CheckItemName

    @CheckItemName.setter
    def CheckItemName(self, CheckItemName):
        self._CheckItemName = CheckItemName

    @property
    def Description(self):
        """Check item details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CheckResult(self):
        """Check item result. Valid values: `pass` (pass); `failed` (failure); `warning` (pass with warning).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def FailureReason(self):
        """The cause of the check item failure
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def Solution(self):
        """Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        """Execution error log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        """URL of the detailed help document
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        """Prompt text for ignoring a risk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SkipInfo

    @SkipInfo.setter
    def SkipInfo(self, SkipInfo):
        self._SkipInfo = SkipInfo


    def _deserialize(self, params):
        self._CheckItemName = params.get("CheckItemName")
        self._Description = params.get("Description")
        self._CheckResult = params.get("CheckResult")
        self._FailureReason = params.get("FailureReason")
        self._Solution = params.get("Solution")
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        self._SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceDetail(AbstractModel):
    """Details of inconsistent tables

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Items: Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of DifferenceItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """Number of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Details of inconsistent tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DifferenceItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DifferenceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferenceItem(AbstractModel):
    """Details of inconsistent tables

    """

    def __init__(self):
        r"""
        :param _Db: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Db: str
        :param _Table: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param _Chunk: Chunk ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Chunk: int
        :param _SrcItem: Source database value
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcItem: str
        :param _DstItem: Target database value
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstItem: str
        :param _IndexName: Index name
Note: This field may return null, indicating that no valid values can be obtained.
        :type IndexName: str
        :param _LowerBoundary: First index key
Note: This field may return null, indicating that no valid values can be obtained.
        :type LowerBoundary: str
        :param _UpperBoundary: Last index key
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpperBoundary: str
        :param _CostTime: Comparison time in ms
Note: This field may return null, indicating that no valid values can be obtained.
        :type CostTime: float
        :param _FinishedAt: Completion time
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinishedAt: str
        """
        self._Db = None
        self._Table = None
        self._Chunk = None
        self._SrcItem = None
        self._DstItem = None
        self._IndexName = None
        self._LowerBoundary = None
        self._UpperBoundary = None
        self._CostTime = None
        self._FinishedAt = None

    @property
    def Db(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Chunk(self):
        """Chunk ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Chunk

    @Chunk.setter
    def Chunk(self, Chunk):
        self._Chunk = Chunk

    @property
    def SrcItem(self):
        """Source database value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcItem

    @SrcItem.setter
    def SrcItem(self, SrcItem):
        self._SrcItem = SrcItem

    @property
    def DstItem(self):
        """Target database value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DstItem

    @DstItem.setter
    def DstItem(self, DstItem):
        self._DstItem = DstItem

    @property
    def IndexName(self):
        """Index name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def LowerBoundary(self):
        """First index key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LowerBoundary

    @LowerBoundary.setter
    def LowerBoundary(self, LowerBoundary):
        self._LowerBoundary = LowerBoundary

    @property
    def UpperBoundary(self):
        """Last index key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpperBoundary

    @UpperBoundary.setter
    def UpperBoundary(self, UpperBoundary):
        self._UpperBoundary = UpperBoundary

    @property
    def CostTime(self):
        """Comparison time in ms
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def FinishedAt(self):
        """Completion time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._Chunk = params.get("Chunk")
        self._SrcItem = params.get("SrcItem")
        self._DstItem = params.get("DstItem")
        self._IndexName = params.get("IndexName")
        self._LowerBoundary = params.get("LowerBoundary")
        self._UpperBoundary = params.get("UpperBoundary")
        self._CostTime = params.get("CostTime")
        self._FinishedAt = params.get("FinishedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeRule(AbstractModel):
    """Kafka partition rules for subscription tasks. Data that matches the regex of the database name and table name will be delivered to the Kafka partition according to the RuleType . If multiple rules are configured, the first hit rule will take effect according to the configured order.

    """

    def __init__(self):
        r"""
        :param _RuleType: Rule type. Valid values for non-mongo products: table (partitioned by table name); pk (partitioned by table name + primary key); cols (partitioned by column name). Valid values for mongo: collection (partitioned by collection name); collectionAndObjectId (partitioned by collection + primary key). Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _DbPattern: Database name matching rule, please fill in the regular expression.Note: This field may return null, indicating that no valid values can be obtained.
        :type DbPattern: str
        :param _TablePattern: Table name matching rule. If DatabaseType is mongodb, it matches the collection name.Note: This field may return null, indicating that no valid values can be obtained.
        :type TablePattern: str
        :param _Columns: Column name. This field is required if RuleType is cols. The subscription task will use the value of this column to calculate the partition. Mongo does not partition by column, so there is no need to pass this field.Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of str
        """
        self._RuleType = None
        self._DbPattern = None
        self._TablePattern = None
        self._Columns = None

    @property
    def RuleType(self):
        """Rule type. Valid values for non-mongo products: table (partitioned by table name); pk (partitioned by table name + primary key); cols (partitioned by column name). Valid values for mongo: collection (partitioned by collection name); collectionAndObjectId (partitioned by collection + primary key). Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def DbPattern(self):
        """Database name matching rule, please fill in the regular expression.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbPattern

    @DbPattern.setter
    def DbPattern(self, DbPattern):
        self._DbPattern = DbPattern

    @property
    def TablePattern(self):
        """Table name matching rule. If DatabaseType is mongodb, it matches the collection name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TablePattern

    @TablePattern.setter
    def TablePattern(self, TablePattern):
        self._TablePattern = TablePattern

    @property
    def Columns(self):
        """Column name. This field is required if RuleType is cols. The subscription task will use the value of this column to calculate the partition. Mongo does not partition by column, so there is no need to pass this field.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._DbPattern = params.get("DbPattern")
        self._TablePattern = params.get("TablePattern")
        self._Columns = params.get("Columns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicOptions(AbstractModel):
    """Data sync options

    """

    def __init__(self):
        r"""
        :param _OpTypes: DML and DDL options to be synced. Valid values: `Insert` (INSERT), `Update` (UPDATE), `Delete` (DELETE), `DDL` (structure sync), `PartialDDL` (custom option, which is used together with `DdlOptions`). This parameter is required, and its value will overwrite the previous value. Note: This field may return null, indicating that no valid values can be obtained.
        :type OpTypes: list of str
        :param _DdlOptions: DDL options to be synced. This parameter is required when `OpTypes` is `PartialDDL`, and its value will overwrite the previous value. Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlOptions: list of DdlOption
        :param _ConflictHandleType: Conflict resolution method. Valid values: `ReportError` (Report error), `Ignore` (Ignore), `Cover` (Overwrite), `ConditionCover` (Conditionally overwrite). Currently, this parameter cannot be modified if the target of the link is Kafka. Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleType: str
        :param _ConflictHandleOption: Detailed options of the conflict resolution method, such as the conditionally overwritten rows and condition operations for the “conditionally overwrite” method. The internal field of this parameter cannot be modified separately. If this parameter needs to be updated, update it fully. Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        self._OpTypes = None
        self._DdlOptions = None
        self._ConflictHandleType = None
        self._ConflictHandleOption = None

    @property
    def OpTypes(self):
        """DML and DDL options to be synced. Valid values: `Insert` (INSERT), `Update` (UPDATE), `Delete` (DELETE), `DDL` (structure sync), `PartialDDL` (custom option, which is used together with `DdlOptions`). This parameter is required, and its value will overwrite the previous value. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def DdlOptions(self):
        """DDL options to be synced. This parameter is required when `OpTypes` is `PartialDDL`, and its value will overwrite the previous value. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DdlOption
        """
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def ConflictHandleType(self):
        """Conflict resolution method. Valid values: `ReportError` (Report error), `Ignore` (Ignore), `Cover` (Overwrite), `ConditionCover` (Conditionally overwrite). Currently, this parameter cannot be modified if the target of the link is Kafka. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def ConflictHandleOption(self):
        """Detailed options of the conflict resolution method, such as the conditionally overwritten rows and condition operations for the “conditionally overwrite” method. The internal field of this parameter cannot be modified separately. If this parameter needs to be updated, update it fully. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption


    def _deserialize(self, params):
        self._OpTypes = params.get("OpTypes")
        if params.get("DdlOptions") is not None:
            self._DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self._DdlOptions.append(obj)
        self._ConflictHandleType = params.get("ConflictHandleType")
        if params.get("ConflictHandleOption") is not None:
            self._ConflictHandleOption = ConflictHandleOption()
            self._ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endpoint(AbstractModel):
    """Information of the source and target databases in data sync

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Role: Node type of TDSQL for MySQL. Enumerated values: `proxy`, `set`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Role: str
        :param _DbKernel: Database kernel type, which is used to distinguish between different kernels in TDSQL. Valid values: `percona`, `mariadb`, `mysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbKernel: str
        :param _InstanceId: Database instance ID in the format of `cdb-powiqx8q`
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Ip: Instance IP address, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Port: Instance port, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _User: Username, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param _Password: Password, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param _DbName: Database name, which is required if the database type is `cdwpg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DbName: str
        :param _VpcId: VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _CvmInstanceId: Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param _UniqDcgId: Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqDcgId: str
        :param _UniqVpnGwId: VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpnGwId: str
        :param _CcnId: CCN instance ID in the format of `ccn-afp6kltc`, which is required if the access type is `ccn`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnId: str
        :param _Supplier: Cloud vendor type. For Alibaba Cloud ApsaraDB for RDS instances, enter `aliyun`; otherwise, enter `others`. Default value: `others`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Supplier: str
        :param _EngineVersion: Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EngineVersion: str
        :param _Account: Instance account, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Account: str
        :param _AccountMode: The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountMode: str
        :param _AccountRole: The role used for cross-account sync, which can contain [a-zA-Z0-9\-\_]+ and is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountRole: str
        :param _RoleExternalId: External role ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleExternalId: str
        :param _TmpSecretId: Temporary SecretId, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance.Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary SecretKey, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance.Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpSecretKey: str
        :param _TmpToken: Temporary token, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance. Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpToken: str
        :param _EncryptConn: Whether to enable encrypted transfer (`UnEncrypted`: No; `Encrypted`: Yes). Default value: `UnEncrypted`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptConn: str
        :param _DatabaseNetEnv: Network environment of the database. This parameter is required when `AccessType` is `ccn`. Valid values: `UserIDC` (user IDC), `TencentVPC` (Tencent Cloud VPC).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseNetEnv: str
        :param _CcnOwnerUin: The root account of CCN in the scenario where the database is connected to CCN under another Tencent Cloud account
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CcnOwnerUin: str
        :param _ChildInstanceId: 
        :type ChildInstanceId: str
        :param _ChildInstanceType: 
        :type ChildInstanceType: str
        :param _SetId: 
        :type SetId: str
        """
        self._Region = None
        self._Role = None
        self._DbKernel = None
        self._InstanceId = None
        self._Ip = None
        self._Port = None
        self._User = None
        self._Password = None
        self._DbName = None
        self._VpcId = None
        self._SubnetId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._UniqVpnGwId = None
        self._CcnId = None
        self._Supplier = None
        self._EngineVersion = None
        self._Account = None
        self._AccountMode = None
        self._AccountRole = None
        self._RoleExternalId = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._TmpToken = None
        self._EncryptConn = None
        self._DatabaseNetEnv = None
        self._CcnOwnerUin = None
        self._ChildInstanceId = None
        self._ChildInstanceType = None
        self._SetId = None

    @property
    def Region(self):
        """Region name, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Role(self):
        """Node type of TDSQL for MySQL. Enumerated values: `proxy`, `set`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def DbKernel(self):
        """Database kernel type, which is used to distinguish between different kernels in TDSQL. Valid values: `percona`, `mariadb`, `mysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbKernel

    @DbKernel.setter
    def DbKernel(self, DbKernel):
        self._DbKernel = DbKernel

    @property
    def InstanceId(self):
        """Database instance ID in the format of `cdb-powiqx8q`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """Instance IP address, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Instance port, which is required if the access type is not `cdb`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def User(self):
        """Username, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """Password, which is required for an instance authenticated by username and password.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DbName(self):
        """Database name, which is required if the database type is `cdwpg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def VpcId(self):
        """VPC ID in the format of `vpc-92jblxto`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """ID of the subnet in the VPC in the format of `subnet-3paxmkdz`, which is required if the access type is `vpc`, `dcg`, or `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CvmInstanceId(self):
        """Short CVM instance ID in the format of `ins-olgl39y8`, which is required if the access type is `cvm`. It is the same as the instance ID displayed in the CVM console.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        """Direct Connect gateway ID in the format of `dcg-0rxtqqxb`, which is required if the access type is `dcg`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def UniqVpnGwId(self):
        """VPN gateway ID in the format of `vpngw-9ghexg7q`, which is required if the access type is `vpncloud`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def CcnId(self):
        """CCN instance ID in the format of `ccn-afp6kltc`, which is required if the access type is `ccn`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def Supplier(self):
        """Cloud vendor type. For Alibaba Cloud ApsaraDB for RDS instances, enter `aliyun`; otherwise, enter `others`. Default value: `others`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Supplier

    @Supplier.setter
    def Supplier(self, Supplier):
        self._Supplier = Supplier

    @property
    def EngineVersion(self):
        """Database version in the format of `5.6` or `5.7`, which takes effect only if the instance is an RDS instance. Default value: `5.6`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Account(self):
        """Instance account, which is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def AccountMode(self):
        """The account to which the resource belongs. Valid values: empty or `self` (the current account); `other` (another account).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountMode

    @AccountMode.setter
    def AccountMode(self, AccountMode):
        self._AccountMode = AccountMode

    @property
    def AccountRole(self):
        """The role used for cross-account sync, which can contain [a-zA-Z0-9\-\_]+ and is required if the operation is performed across accounts.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountRole

    @AccountRole.setter
    def AccountRole(self, AccountRole):
        self._AccountRole = AccountRole

    @property
    def RoleExternalId(self):
        """External role ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RoleExternalId

    @RoleExternalId.setter
    def RoleExternalId(self, RoleExternalId):
        self._RoleExternalId = RoleExternalId

    @property
    def TmpSecretId(self):
        """Temporary SecretId, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Temporary SecretKey, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def TmpToken(self):
        """Temporary token, you can obtain the temporary key by [GetFederationToken](https://intl.cloud.tencent.com/document/product/1312/48195?from_cn_redirect=1). This field is required if it is a cross-account instance. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TmpToken

    @TmpToken.setter
    def TmpToken(self, TmpToken):
        self._TmpToken = TmpToken

    @property
    def EncryptConn(self):
        """Whether to enable encrypted transfer (`UnEncrypted`: No; `Encrypted`: Yes). Default value: `UnEncrypted`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def DatabaseNetEnv(self):
        """Network environment of the database. This parameter is required when `AccessType` is `ccn`. Valid values: `UserIDC` (user IDC), `TencentVPC` (Tencent Cloud VPC).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def CcnOwnerUin(self):
        """The root account of CCN in the scenario where the database is connected to CCN under another Tencent Cloud account
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CcnOwnerUin

    @CcnOwnerUin.setter
    def CcnOwnerUin(self, CcnOwnerUin):
        self._CcnOwnerUin = CcnOwnerUin

    @property
    def ChildInstanceId(self):
        """
        :rtype: str
        """
        return self._ChildInstanceId

    @ChildInstanceId.setter
    def ChildInstanceId(self, ChildInstanceId):
        self._ChildInstanceId = ChildInstanceId

    @property
    def ChildInstanceType(self):
        """
        :rtype: str
        """
        return self._ChildInstanceType

    @ChildInstanceType.setter
    def ChildInstanceType(self, ChildInstanceType):
        self._ChildInstanceType = ChildInstanceType

    @property
    def SetId(self):
        """
        :rtype: str
        """
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Role = params.get("Role")
        self._DbKernel = params.get("DbKernel")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._DbName = params.get("DbName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._CcnId = params.get("CcnId")
        self._Supplier = params.get("Supplier")
        self._EngineVersion = params.get("EngineVersion")
        self._Account = params.get("Account")
        self._AccountMode = params.get("AccountMode")
        self._AccountRole = params.get("AccountRole")
        self._RoleExternalId = params.get("RoleExternalId")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._TmpToken = params.get("TmpToken")
        self._EncryptConn = params.get("EncryptConn")
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        self._CcnOwnerUin = params.get("CcnOwnerUin")
        self._ChildInstanceId = params.get("ChildInstanceId")
        self._ChildInstanceType = params.get("ChildInstanceType")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointItem(AbstractModel):
    """Instance node information of data subscription

    """

    def __init__(self):
        r"""
        :param _DatabaseRegion: Region of the source database. If AccessType is ccn, please fill in the region where vpc is located because the region of the source database is unknown. For other access methods, please fill in the region where the subscription task is located, as ensuring the subscription task and the source database are in the same region is the optimal network solution.Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseRegion: str
        :param _User: UsernameNote: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param _Password: Password. It is required when used as an input parameter and empty when used as an output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param _InstanceId: Target instance ID. This field is required when AccessType is cdb. When configuring the InstanceId, the instance information is queried and checked. The mysql query interface has been authenticated. Please ensure that the sub-user has the cdb:DescribeDBInstances interface permission.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _CvmInstanceId: Cloud Virtual Machine ID. This field is required when AccessType is cvm.Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param _UniqDcgId: Direct Connect gateway ID. This field is required when AccessType is dcg.Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqDcgId: str
        :param _CcnId: Cloud Connect Network ID. This field is required when AccessType is ccn.Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnId: str
        :param _UniqVpnGwId: VPN gateway ID. This field is required when AccessType is vpncloud.Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqVpnGwId: str
        :param _VpcId: VpcID. This field is required when AccessType is dcg\ccn\vpncloud\vpc.Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID. This field is required when AccessType is dcg\ccn\vpncloud\vpc.Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _HostName: Database address, supports domain name and IP. This field is required when AccessType is dcg\ccn\vpncloud\vpc\extranet\intranet.Note: This field may return null, indicating that no valid values can be obtained.
        :type HostName: str
        :param _Port: Database port. This field is required when AccessType is dcg\ccn\vpncloud\vpc\extranet\intranet\cvm.Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _EncryptConn: Whether to use encrypted transmission. Valid values: UnEncrypted; Encrypted. Only mysql supports it. If it is not filled in, it will not be encrypted by default. Other products do not need to fill in this.Note: This field may return null, indicating that no valid values can be obtained.
        :type EncryptConn: str
        :param _DatabaseNetEnv: Database network environment. This field is required when AccessType is ccn. Valid values: UserIDC; TencentVPC; Aws; AliYun; Others.Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseNetEnv: str
        :param _CcnOwnerUin: The UIN of the main account to which the Cloud Connect Network gateway belongs. It is required for cross-account CCN.Note: This field may return null, indicating that no valid values can be obtained.
        :type CcnOwnerUin: str
        :param _ExtraAttr: Additional information added for the business. Parameter name is called key, parameter value is called value. Mandatory parameters for tdpg: PgDatabase (subscribed database name).Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        :param _ChildInstanceId: 
        :type ChildInstanceId: str
        :param _ChildInstanceType: 
        :type ChildInstanceType: str
        """
        self._DatabaseRegion = None
        self._User = None
        self._Password = None
        self._InstanceId = None
        self._CvmInstanceId = None
        self._UniqDcgId = None
        self._CcnId = None
        self._UniqVpnGwId = None
        self._VpcId = None
        self._SubnetId = None
        self._HostName = None
        self._Port = None
        self._EncryptConn = None
        self._DatabaseNetEnv = None
        self._CcnOwnerUin = None
        self._ExtraAttr = None
        self._ChildInstanceId = None
        self._ChildInstanceType = None

    @property
    def DatabaseRegion(self):
        """Region of the source database. If AccessType is ccn, please fill in the region where vpc is located because the region of the source database is unknown. For other access methods, please fill in the region where the subscription task is located, as ensuring the subscription task and the source database are in the same region is the optimal network solution.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseRegion

    @DatabaseRegion.setter
    def DatabaseRegion(self, DatabaseRegion):
        self._DatabaseRegion = DatabaseRegion

    @property
    def User(self):
        """UsernameNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """Password. It is required when used as an input parameter and empty when used as an output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceId(self):
        """Target instance ID. This field is required when AccessType is cdb. When configuring the InstanceId, the instance information is queried and checked. The mysql query interface has been authenticated. Please ensure that the sub-user has the cdb:DescribeDBInstances interface permission.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceId(self):
        """Cloud Virtual Machine ID. This field is required when AccessType is cvm.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def UniqDcgId(self):
        """Direct Connect gateway ID. This field is required when AccessType is dcg.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqDcgId

    @UniqDcgId.setter
    def UniqDcgId(self, UniqDcgId):
        self._UniqDcgId = UniqDcgId

    @property
    def CcnId(self):
        """Cloud Connect Network ID. This field is required when AccessType is ccn.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def UniqVpnGwId(self):
        """VPN gateway ID. This field is required when AccessType is vpncloud.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpnGwId

    @UniqVpnGwId.setter
    def UniqVpnGwId(self, UniqVpnGwId):
        self._UniqVpnGwId = UniqVpnGwId

    @property
    def VpcId(self):
        """VpcID. This field is required when AccessType is dcg\ccn\vpncloud\vpc.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID. This field is required when AccessType is dcg\ccn\vpncloud\vpc.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def HostName(self):
        """Database address, supports domain name and IP. This field is required when AccessType is dcg\ccn\vpncloud\vpc\extranet\intranet.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Port(self):
        """Database port. This field is required when AccessType is dcg\ccn\vpncloud\vpc\extranet\intranet\cvm.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EncryptConn(self):
        """Whether to use encrypted transmission. Valid values: UnEncrypted; Encrypted. Only mysql supports it. If it is not filled in, it will not be encrypted by default. Other products do not need to fill in this.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EncryptConn

    @EncryptConn.setter
    def EncryptConn(self, EncryptConn):
        self._EncryptConn = EncryptConn

    @property
    def DatabaseNetEnv(self):
        """Database network environment. This field is required when AccessType is ccn. Valid values: UserIDC; TencentVPC; Aws; AliYun; Others.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseNetEnv

    @DatabaseNetEnv.setter
    def DatabaseNetEnv(self, DatabaseNetEnv):
        self._DatabaseNetEnv = DatabaseNetEnv

    @property
    def CcnOwnerUin(self):
        """The UIN of the main account to which the Cloud Connect Network gateway belongs. It is required for cross-account CCN.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CcnOwnerUin

    @CcnOwnerUin.setter
    def CcnOwnerUin(self, CcnOwnerUin):
        self._CcnOwnerUin = CcnOwnerUin

    @property
    def ExtraAttr(self):
        """Additional information added for the business. Parameter name is called key, parameter value is called value. Mandatory parameters for tdpg: PgDatabase (subscribed database name).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def ChildInstanceId(self):
        """
        :rtype: str
        """
        return self._ChildInstanceId

    @ChildInstanceId.setter
    def ChildInstanceId(self, ChildInstanceId):
        self._ChildInstanceId = ChildInstanceId

    @property
    def ChildInstanceType(self):
        """
        :rtype: str
        """
        return self._ChildInstanceType

    @ChildInstanceType.setter
    def ChildInstanceType(self, ChildInstanceType):
        self._ChildInstanceType = ChildInstanceType


    def _deserialize(self, params):
        self._DatabaseRegion = params.get("DatabaseRegion")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._UniqDcgId = params.get("UniqDcgId")
        self._CcnId = params.get("CcnId")
        self._UniqVpnGwId = params.get("UniqVpnGwId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._HostName = params.get("HostName")
        self._Port = params.get("Port")
        self._EncryptConn = params.get("EncryptConn")
        self._DatabaseNetEnv = params.get("DatabaseNetEnv")
        self._CcnOwnerUin = params.get("CcnOwnerUin")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._ChildInstanceId = params.get("ChildInstanceId")
        self._ChildInstanceType = params.get("ChildInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrInfo(AbstractModel):
    """Error information and the corresponding solution

    """

    def __init__(self):
        r"""
        :param _Reason: Cause of the error
        :type Reason: str
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        """
        self._Reason = None
        self._Message = None
        self._Solution = None

    @property
    def Reason(self):
        """Cause of the error
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfoItem(AbstractModel):
    """Task error information

    """

    def __init__(self):
        r"""
        :param _Code: Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param _Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param _ErrorLog: Error log
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorLog: str
        :param _HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        """
        self._Code = None
        self._Solution = None
        self._ErrorLog = None
        self._HelpDoc = None

    @property
    def Code(self):
        """Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Solution(self):
        """Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def ErrorLog(self):
        """Error log
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorLog

    @ErrorLog.setter
    def ErrorLog(self, ErrorLog):
        self._ErrorLog = ErrorLog

    @property
    def HelpDoc(self):
        """Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Solution = params.get("Solution")
        self._ErrorLog = params.get("ErrorLog")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """Kafka consumer group details

    """

    def __init__(self):
        r"""
        :param _Account: Consumer group account
        :type Account: str
        :param _ConsumerGroupName: Consumer group name
        :type ConsumerGroupName: str
        :param _Description: Consumer group descriptionNote: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _ConsumerGroupOffset: Consumer group offset. This field is for compatibility with the previous single partition scenario, where the value is the offset of the last partition. For the offset of each partition, please refer to the StateOfPartition field.
        :type ConsumerGroupOffset: int
        :param _ConsumerGroupLag: The amount of data that has not been consumed by the consumer group. This field is for compatibility with the previous single partition scenario, where the value is the amount of unconsumed data in the last partition. For the amount of unconsumed data in each partition, refer to the StateOfPartition field.
        :type ConsumerGroupLag: int
        :param _Latency: Consumption delay (in seconds)
        :type Latency: int
        :param _StateOfPartition: Consumption status of each partition
        :type StateOfPartition: list of MonitorInfo
        :param _CreatedAt: Consumer group creation time, the format is: YYYY-MM-DD hh:mm:ss.
        :type CreatedAt: str
        :param _UpdatedAt: Consumer group update time, the format is: YYYY-MM-DD hh:mm:ss.
        :type UpdatedAt: str
        :param _ConsumerGroupState: Consumer group states, including Dead, Empty, Stable, etc. Only Dead and Empty states can perform reset operations.
        :type ConsumerGroupState: str
        :param _PartitionAssignment: The partition is being consumed by each consumer.Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionAssignment: list of PartitionAssignment
        """
        self._Account = None
        self._ConsumerGroupName = None
        self._Description = None
        self._ConsumerGroupOffset = None
        self._ConsumerGroupLag = None
        self._Latency = None
        self._StateOfPartition = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._ConsumerGroupState = None
        self._PartitionAssignment = None

    @property
    def Account(self):
        """Consumer group account
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def ConsumerGroupName(self):
        """Consumer group name
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def Description(self):
        """Consumer group descriptionNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConsumerGroupOffset(self):
        """Consumer group offset. This field is for compatibility with the previous single partition scenario, where the value is the offset of the last partition. For the offset of each partition, please refer to the StateOfPartition field.
        :rtype: int
        """
        return self._ConsumerGroupOffset

    @ConsumerGroupOffset.setter
    def ConsumerGroupOffset(self, ConsumerGroupOffset):
        self._ConsumerGroupOffset = ConsumerGroupOffset

    @property
    def ConsumerGroupLag(self):
        """The amount of data that has not been consumed by the consumer group. This field is for compatibility with the previous single partition scenario, where the value is the amount of unconsumed data in the last partition. For the amount of unconsumed data in each partition, refer to the StateOfPartition field.
        :rtype: int
        """
        return self._ConsumerGroupLag

    @ConsumerGroupLag.setter
    def ConsumerGroupLag(self, ConsumerGroupLag):
        self._ConsumerGroupLag = ConsumerGroupLag

    @property
    def Latency(self):
        """Consumption delay (in seconds)
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def StateOfPartition(self):
        """Consumption status of each partition
        :rtype: list of MonitorInfo
        """
        return self._StateOfPartition

    @StateOfPartition.setter
    def StateOfPartition(self, StateOfPartition):
        self._StateOfPartition = StateOfPartition

    @property
    def CreatedAt(self):
        """Consumer group creation time, the format is: YYYY-MM-DD hh:mm:ss.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """Consumer group update time, the format is: YYYY-MM-DD hh:mm:ss.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ConsumerGroupState(self):
        """Consumer group states, including Dead, Empty, Stable, etc. Only Dead and Empty states can perform reset operations.
        :rtype: str
        """
        return self._ConsumerGroupState

    @ConsumerGroupState.setter
    def ConsumerGroupState(self, ConsumerGroupState):
        self._ConsumerGroupState = ConsumerGroupState

    @property
    def PartitionAssignment(self):
        """The partition is being consumed by each consumer.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PartitionAssignment
        """
        return self._PartitionAssignment

    @PartitionAssignment.setter
    def PartitionAssignment(self, PartitionAssignment):
        self._PartitionAssignment = PartitionAssignment


    def _deserialize(self, params):
        self._Account = params.get("Account")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._Description = params.get("Description")
        self._ConsumerGroupOffset = params.get("ConsumerGroupOffset")
        self._ConsumerGroupLag = params.get("ConsumerGroupLag")
        self._Latency = params.get("Latency")
        if params.get("StateOfPartition") is not None:
            self._StateOfPartition = []
            for item in params.get("StateOfPartition"):
                obj = MonitorInfo()
                obj._deserialize(item)
                self._StateOfPartition.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._ConsumerGroupState = params.get("ConsumerGroupState")
        if params.get("PartitionAssignment") is not None:
            self._PartitionAssignment = []
            for item in params.get("PartitionAssignment"):
                obj = PartitionAssignment()
                obj._deserialize(item)
                self._PartitionAssignment.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobRequest(AbstractModel):
    """IsolateMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateMigrateJobResponse(AbstractModel):
    """IsolateMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsolateSyncJobRequest(AbstractModel):
    """IsolateSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateSyncJobResponse(AbstractModel):
    """IsolateSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class JobItem(AbstractModel):
    """Migration task list

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _JobName: Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param _CreateTime: Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _StartTime: Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _BriefMsg: Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type BriefMsg: str
        :param _Status: Task status. Valid values: `creating` (Creating), `created`(Created), `checking` (Checking), `checkPass` (Check passed), `checkNotPass` (Check not passed), `readyRun` (Ready for running), `running` (Running), `readyComplete` (Preparation completed), `success` (Successful), `failed` (Failed), `stopping` (Stopping), `completing` (Completing), `pausing` (Pausing), `manualPaused` (Paused). Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _RunMode: Task running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param _ExpectRunTime: Expected start time in the format of "2022-07-11 16:20:49", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param _Action: Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        :param _StepInfo: Information of the migration task execution process
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        :param _SrcInfo: Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _CompareTask: Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompareTask: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        :param _TradeInfo: Billing status information
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeInfo: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        :param _Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _AutoRetryTimeRangeMinutes: Information of automatic retry time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRetryTimeRangeMinutes: int
        :param _DumperResumeCtrl: Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DumperResumeCtrl: str
        """
        self._JobId = None
        self._JobName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._BriefMsg = None
        self._Status = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._Action = None
        self._StepInfo = None
        self._SrcInfo = None
        self._DstInfo = None
        self._CompareTask = None
        self._TradeInfo = None
        self._Tags = None
        self._AutoRetryTimeRangeMinutes = None
        self._DumperResumeCtrl = None

    @property
    def JobId(self):
        """Data migration task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Data migration task name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def CreateTime(self):
        """Task creation (submission) time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Task update time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def StartTime(self):
        """Task start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task end time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BriefMsg(self):
        """Migration task error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BriefMsg

    @BriefMsg.setter
    def BriefMsg(self, BriefMsg):
        self._BriefMsg = BriefMsg

    @property
    def Status(self):
        """Task status. Valid values: `creating` (Creating), `created`(Created), `checking` (Checking), `checkPass` (Check passed), `checkNotPass` (Check not passed), `readyRun` (Ready for running), `running` (Running), `readyComplete` (Preparation completed), `success` (Successful), `failed` (Failed), `stopping` (Stopping), `completing` (Completing), `pausing` (Pausing), `manualPaused` (Paused). Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RunMode(self):
        """Task running mode. Valid values: `immediate`, `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """Expected start time in the format of "2022-07-11 16:20:49", which is required if `RunMode` is `timed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Action(self):
        """Task operation information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateAction`
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StepInfo(self):
        """Information of the migration task execution process
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateDetailInfo`
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo

    @property
    def SrcInfo(self):
        """Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """Target database information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def CompareTask(self):
        """Data consistency check result
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareTaskInfo`
        """
        return self._CompareTask

    @CompareTask.setter
    def CompareTask(self, CompareTask):
        self._CompareTask = CompareTask

    @property
    def TradeInfo(self):
        """Billing status information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.TradeInfo`
        """
        return self._TradeInfo

    @TradeInfo.setter
    def TradeInfo(self, TradeInfo):
        self._TradeInfo = TradeInfo

    @property
    def Tags(self):
        """Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        """Information of automatic retry time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def DumperResumeCtrl(self):
        """Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BriefMsg = params.get("BriefMsg")
        self._Status = params.get("Status")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Action") is not None:
            self._Action = MigrateAction()
            self._Action._deserialize(params.get("Action"))
        if params.get("StepInfo") is not None:
            self._StepInfo = MigrateDetailInfo()
            self._StepInfo._deserialize(params.get("StepInfo"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        if params.get("CompareTask") is not None:
            self._CompareTask = CompareTaskInfo()
            self._CompareTask._deserialize(params.get("CompareTask"))
        if params.get("TradeInfo") is not None:
            self._TradeInfo = TradeInfo()
            self._TradeInfo._deserialize(params.get("TradeInfo"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KafkaOption(AbstractModel):
    """Sync options configured when the target database is Kafka

    """

    def __init__(self):
        r"""
        :param _DataType: Data type delivered to Kafka, such as Avro, Json, canal-pb, canal-json
        :type DataType: str
        :param _TopicType: Topic sync policy, such as `Single` (deliver all data to a single topic), `Multi` (deliver data to multiple custom topics).
        :type TopicType: str
        :param _DDLTopicName: Topic for DDL storage
        :type DDLTopicName: str
        :param _TopicRules: Topic description
        :type TopicRules: list of TopicRule
        """
        self._DataType = None
        self._TopicType = None
        self._DDLTopicName = None
        self._TopicRules = None

    @property
    def DataType(self):
        """Data type delivered to Kafka, such as Avro, Json, canal-pb, canal-json
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def TopicType(self):
        """Topic sync policy, such as `Single` (deliver all data to a single topic), `Multi` (deliver data to multiple custom topics).
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def DDLTopicName(self):
        """Topic for DDL storage
        :rtype: str
        """
        return self._DDLTopicName

    @DDLTopicName.setter
    def DDLTopicName(self, DDLTopicName):
        self._DDLTopicName = DDLTopicName

    @property
    def TopicRules(self):
        """Topic description
        :rtype: list of TopicRule
        """
        return self._TopicRules

    @TopicRules.setter
    def TopicRules(self, TopicRules):
        self._TopicRules = TopicRules


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._TopicType = params.get("TopicType")
        self._DDLTopicName = params.get("DDLTopicName")
        if params.get("TopicRules") is not None:
            self._TopicRules = []
            for item in params.get("TopicRules"):
                obj = TopicRule()
                obj._deserialize(item)
                self._TopicRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePairOption(AbstractModel):
    """Additional configuration information

    """

    def __init__(self):
        r"""
        :param _Key: Option key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Option value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Option key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Option value
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class MigrateAction(AbstractModel):
    """Task operation information, which contains the list of all operations in the migration task as well as the list of allowed operations under the current status.

    """

    def __init__(self):
        r"""
        :param _AllAction: List of all operations in the task
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllAction: list of str
        :param _AllowedAction: List of allowed operations in the task under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllowedAction: list of str
        """
        self._AllAction = None
        self._AllowedAction = None

    @property
    def AllAction(self):
        """List of all operations in the task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AllAction

    @AllAction.setter
    def AllAction(self, AllAction):
        self._AllAction = AllAction

    @property
    def AllowedAction(self):
        """List of allowed operations in the task under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AllowedAction

    @AllowedAction.setter
    def AllowedAction(self, AllowedAction):
        self._AllowedAction = AllowedAction


    def _deserialize(self, params):
        self._AllAction = params.get("AllAction")
        self._AllowedAction = params.get("AllowedAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDBItem(AbstractModel):
    """Object in the migration task instance list

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Vip: Instance VIP
        :type Vip: str
        :param _Vport: Instance Vport
        :type Vport: int
        :param _Usable: Whether the instance can be migrated. Valid values: `1 (yes); `0` (no).
        :type Usable: int
        :param _Hint: The cause why the instance cannot be migrated
        :type Hint: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Vip = None
        self._Vport = None
        self._Usable = None
        self._Hint = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        """Instance VIP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        """Instance Vport
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Usable(self):
        """Whether the instance can be migrated. Valid values: `1 (yes); `0` (no).
        :rtype: int
        """
        return self._Usable

    @Usable.setter
    def Usable(self, Usable):
        self._Usable = Usable

    @property
    def Hint(self):
        """The cause why the instance cannot be migrated
        :rtype: str
        """
        return self._Hint

    @Hint.setter
    def Hint(self, Hint):
        self._Hint = Hint


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Usable = params.get("Usable")
        self._Hint = params.get("Hint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateDetailInfo(AbstractModel):
    """Information of the migration task execution process

    """

    def __init__(self):
        r"""
        :param _StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param _StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param _MasterSlaveDistance: Source-replica lag in MB. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: Source-replica lag in seconds. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecondsBehindMaster: int
        :param _StepInfo: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfo: list of StepDetailInfo
        """
        self._StepAll = None
        self._StepNow = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._StepInfo = None

    @property
    def StepAll(self):
        """Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def MasterSlaveDistance(self):
        """Source-replica lag in MB. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        """Source-replica lag in seconds. This parameter takes effect only when the task is normal and is in the last step of migration or sync (binlog sync). If it is invalid, `-1` will be returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def StepInfo(self):
        """Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepDetailInfo
        """
        return self._StepInfo

    @StepInfo.setter
    def StepInfo(self, StepInfo):
        self._StepInfo = StepInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self._StepInfo = []
            for item in params.get("StepInfo"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self._StepInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOption(AbstractModel):
    """Migration options, which describe how the task performs migration.

    """

    def __init__(self):
        r"""
        :param _DatabaseTable: Migration object options, which tell DTS which database/table objects should be migrated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseTable: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        :param _MigrateType: Migration type. Valid values: `full`, `structure`, `fullAndIncrement`. Default value: `fullAndIncrement`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MigrateType: str
        :param _Consistency: Data consistency check option. Data consistency check is disabled by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Consistency: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        :param _IsMigrateAccount: Whether to migrate accounts. Valid values: `yes`, `no`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsMigrateAccount: bool
        :param _IsOverrideRoot: Whether to use the `Root` account in the source database to overwrite that in the target database. Valid values: `false`, `true`. For database/table or structural migration, you should specify `false`. Note that this parameter takes effect only for OldDTS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsOverrideRoot: bool
        :param _IsDstReadOnly: Whether to set the target database to read-only during migration, which takes effect only for MySQL databases. Valid values: `true`, `false`. Default value: `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDstReadOnly: bool
        :param _ExtraAttr: Additional information. You can set additional parameters for certain database types. For Redis, you can define the following parameters: 
["DstWriteMode": `normal`. 	Target database write mode. Valid values: `clearData` (Clear the target instance data), overwrite` (Execute the task in overwriting mode), `normal` (Follow the normal steps) 	"IsDstReadOnly": `true`. 	Whether to set the target database to read-only for a migration task. Valid values: `true` (Yes), `false` (No) 	"ClientOutputBufferHardLimit": 512. 	Hard limit of the replica buffer zone capacity in MB. 	"ClientOutputBufferSoftLimit": 512. 	Soft limit of the replica buffer zone capacity in MB. 	"ClientOutputBufferPersistTime": 60. Soft limit duration of the replica buffer zone in seconds. 	"ReplBacklogSize": 512, 	Limit of the circular buffer zone capacity in MB. 	"ReplTimeout":120,		Replication timeout period in seconds]
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraAttr: list of KeyValuePairOption
        :param _MigrateWay: 
        :type MigrateWay: str
        """
        self._DatabaseTable = None
        self._MigrateType = None
        self._Consistency = None
        self._IsMigrateAccount = None
        self._IsOverrideRoot = None
        self._IsDstReadOnly = None
        self._ExtraAttr = None
        self._MigrateWay = None

    @property
    def DatabaseTable(self):
        """Migration object options, which tell DTS which database/table objects should be migrated.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.DatabaseTableObject`
        """
        return self._DatabaseTable

    @DatabaseTable.setter
    def DatabaseTable(self, DatabaseTable):
        self._DatabaseTable = DatabaseTable

    @property
    def MigrateType(self):
        """Migration type. Valid values: `full`, `structure`, `fullAndIncrement`. Default value: `fullAndIncrement`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MigrateType

    @MigrateType.setter
    def MigrateType(self, MigrateType):
        self._MigrateType = MigrateType

    @property
    def Consistency(self):
        """Data consistency check option. Data consistency check is disabled by default.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConsistencyOption`
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def IsMigrateAccount(self):
        """Whether to migrate accounts. Valid values: `yes`, `no`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsMigrateAccount

    @IsMigrateAccount.setter
    def IsMigrateAccount(self, IsMigrateAccount):
        self._IsMigrateAccount = IsMigrateAccount

    @property
    def IsOverrideRoot(self):
        """Whether to use the `Root` account in the source database to overwrite that in the target database. Valid values: `false`, `true`. For database/table or structural migration, you should specify `false`. Note that this parameter takes effect only for OldDTS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsOverrideRoot

    @IsOverrideRoot.setter
    def IsOverrideRoot(self, IsOverrideRoot):
        self._IsOverrideRoot = IsOverrideRoot

    @property
    def IsDstReadOnly(self):
        """Whether to set the target database to read-only during migration, which takes effect only for MySQL databases. Valid values: `true`, `false`. Default value: `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDstReadOnly

    @IsDstReadOnly.setter
    def IsDstReadOnly(self, IsDstReadOnly):
        self._IsDstReadOnly = IsDstReadOnly

    @property
    def ExtraAttr(self):
        """Additional information. You can set additional parameters for certain database types. For Redis, you can define the following parameters: 
["DstWriteMode": `normal`. 	Target database write mode. Valid values: `clearData` (Clear the target instance data), overwrite` (Execute the task in overwriting mode), `normal` (Follow the normal steps) 	"IsDstReadOnly": `true`. 	Whether to set the target database to read-only for a migration task. Valid values: `true` (Yes), `false` (No) 	"ClientOutputBufferHardLimit": 512. 	Hard limit of the replica buffer zone capacity in MB. 	"ClientOutputBufferSoftLimit": 512. 	Soft limit of the replica buffer zone capacity in MB. 	"ClientOutputBufferPersistTime": 60. Soft limit duration of the replica buffer zone in seconds. 	"ReplBacklogSize": 512, 	Limit of the circular buffer zone capacity in MB. 	"ReplTimeout":120,		Replication timeout period in seconds]
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyValuePairOption
        """
        return self._ExtraAttr

    @ExtraAttr.setter
    def ExtraAttr(self, ExtraAttr):
        self._ExtraAttr = ExtraAttr

    @property
    def MigrateWay(self):
        """
        :rtype: str
        """
        return self._MigrateWay

    @MigrateWay.setter
    def MigrateWay(self, MigrateWay):
        self._MigrateWay = MigrateWay


    def _deserialize(self, params):
        if params.get("DatabaseTable") is not None:
            self._DatabaseTable = DatabaseTableObject()
            self._DatabaseTable._deserialize(params.get("DatabaseTable"))
        self._MigrateType = params.get("MigrateType")
        if params.get("Consistency") is not None:
            self._Consistency = ConsistencyOption()
            self._Consistency._deserialize(params.get("Consistency"))
        self._IsMigrateAccount = params.get("IsMigrateAccount")
        self._IsOverrideRoot = params.get("IsOverrideRoot")
        self._IsDstReadOnly = params.get("IsDstReadOnly")
        if params.get("ExtraAttr") is not None:
            self._ExtraAttr = []
            for item in params.get("ExtraAttr"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._ExtraAttr.append(obj)
        self._MigrateWay = params.get("MigrateWay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifiedSubscribeObject(AbstractModel):
    """The object of the data subscription is used in the ModifySubscribeObjects interface. Similar to the SubscribeObject structure, only the type and parameter names differ.

    """

    def __init__(self):
        r"""
        :param _ObjectsType: Subscription object type. Valid values: 0 (database); 1 (table, for mongo tasks, this corresponds to a collection).Note: mongo only supports full instance, single database or single collection subscription, so this field should not conflict with SubscribeObjectType. For example, when SubscribeObjectType=4, it means mongo single database subscription, then 0 should be passed in this field.Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectsType: int
        :param _DatabaseName: Subscription database nameNote: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _TableNames: Name of the table (or collection) in the subscription database. If ObjectsType is 1, this field is required and not empty; 
        :type TableNames: list of str
        """
        self._ObjectsType = None
        self._DatabaseName = None
        self._TableNames = None

    @property
    def ObjectsType(self):
        """Subscription object type. Valid values: 0 (database); 1 (table, for mongo tasks, this corresponds to a collection).Note: mongo only supports full instance, single database or single collection subscription, so this field should not conflict with SubscribeObjectType. For example, when SubscribeObjectType=4, it means mongo single database subscription, then 0 should be passed in this field.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ObjectsType

    @ObjectsType.setter
    def ObjectsType(self, ObjectsType):
        self._ObjectsType = ObjectsType

    @property
    def DatabaseName(self):
        """Subscription database nameNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableNames(self):
        """Name of the table (or collection) in the subscription database. If ObjectsType is 1, this field is required and not empty; 
        :rtype: list of str
        """
        return self._TableNames

    @TableNames.setter
    def TableNames(self, TableNames):
        self._TableNames = TableNames


    def _deserialize(self, params):
        self._ObjectsType = params.get("ObjectsType")
        self._DatabaseName = params.get("DatabaseName")
        self._TableNames = params.get("TableNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameRequest(AbstractModel):
    """ModifyCompareTaskName request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        :param _TaskName: Data consistency check task name
        :type TaskName: str
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """Data consistency check task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskNameResponse(AbstractModel):
    """ModifyCompareTaskName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCompareTaskRequest(AbstractModel):
    """ModifyCompareTask request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _ObjectMode: Data comparison object mode. Valid values: `sameAsMigrate` (All migration objects), `custom` (Custom mode. The custom comparison objects must be a subset of the migration objects). Default value: `sameAsMigrate`.
        :type ObjectMode: str
        :param _Objects: Compared object, which is required if `CompareObjectMode` is `custom`.
        :type Objects: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        :param _Options: Consistency check options
        :type Options: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        self._JobId = None
        self._CompareTaskId = None
        self._TaskName = None
        self._ObjectMode = None
        self._Objects = None
        self._Options = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ObjectMode(self):
        """Data comparison object mode. Valid values: `sameAsMigrate` (All migration objects), `custom` (Custom mode. The custom comparison objects must be a subset of the migration objects). Default value: `sameAsMigrate`.
        :rtype: str
        """
        return self._ObjectMode

    @ObjectMode.setter
    def ObjectMode(self, ObjectMode):
        self._ObjectMode = ObjectMode

    @property
    def Objects(self):
        """Compared object, which is required if `CompareObjectMode` is `custom`.
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareObject`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Options(self):
        """Consistency check options
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompareOptions`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        self._TaskName = params.get("TaskName")
        self._ObjectMode = params.get("ObjectMode")
        if params.get("Objects") is not None:
            self._Objects = CompareObject()
            self._Objects._deserialize(params.get("Objects"))
        if params.get("Options") is not None:
            self._Options = CompareOptions()
            self._Options._deserialize(params.get("Options"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCompareTaskResponse(AbstractModel):
    """ModifyCompareTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsumerGroupDescriptionRequest(AbstractModel):
    """ModifyConsumerGroupDescription request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _ConsumerGroupName: Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.Please make sure the consumer group name is correct.
        :type ConsumerGroupName: str
        :param _AccountName: Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.Please make sure the account name is correct.
        :type AccountName: str
        :param _Description: Updated description of the consumer group
        :type Description: str
        """
        self._SubscribeId = None
        self._ConsumerGroupName = None
        self._AccountName = None
        self._Description = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def ConsumerGroupName(self):
        """Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.Please make sure the consumer group name is correct.
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def AccountName(self):
        """Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.Please make sure the account name is correct.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Description(self):
        """Updated description of the consumer group
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._AccountName = params.get("AccountName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupDescriptionResponse(AbstractModel):
    """ModifyConsumerGroupDescription response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyConsumerGroupPasswordRequest(AbstractModel):
    """ModifyConsumerGroupPassword request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _AccountName: Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.
        :type AccountName: str
        :param _ConsumerGroupName: Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :type ConsumerGroupName: str
        :param _OldPassword: Old Password.
        :type OldPassword: str
        :param _NewPassword: New password. The character length is no less than 3 and no more than 32.
        :type NewPassword: str
        """
        self._SubscribeId = None
        self._AccountName = None
        self._ConsumerGroupName = None
        self._OldPassword = None
        self._NewPassword = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def AccountName(self):
        """Account name. The full name of the actual account is in the form: account-#{SubscribeId}-#{AccountName}.
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def ConsumerGroupName(self):
        """Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def OldPassword(self):
        """Old Password.
        :rtype: str
        """
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def NewPassword(self):
        """New password. The character length is no less than 3 and no more than 32.
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._AccountName = params.get("AccountName")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._OldPassword = params.get("OldPassword")
        self._NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupPasswordResponse(AbstractModel):
    """ModifyConsumerGroupPassword response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateJobSpecRequest(AbstractModel):
    """ModifyMigrateJobSpec request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _NewInstanceClass: New instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :type NewInstanceClass: str
        """
        self._JobId = None
        self._NewInstanceClass = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        """New instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
        :rtype: str
        """
        return self._NewInstanceClass

    @NewInstanceClass.setter
    def NewInstanceClass(self, NewInstanceClass):
        self._NewInstanceClass = NewInstanceClass


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateJobSpecResponse(AbstractModel):
    """ModifyMigrateJobSpec response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateNameRequest(AbstractModel):
    """ModifyMigrateName request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _JobName: New migration task name
        :type JobName: str
        """
        self._JobId = None
        self._JobName = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """New migration task name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateNameResponse(AbstractModel):
    """ModifyMigrateName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateRateLimitRequest(AbstractModel):
    """ModifyMigrateRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _DumpThread: Number of full export threads for migration task. Value range: 1-16.
        :type DumpThread: int
        :param _DumpRps: The full export Rps for migration task. The value needs to be greater than 0.
        :type DumpRps: int
        :param _LoadThread: Number of full import threads for migration task. Value range: 1-16.
        :type LoadThread: int
        :param _SinkerThread: Number of incremental import threads for migration task. Value range: 1-128.
        :type SinkerThread: int
        :param _LoadRps: Limits for full import Rps.
        :type LoadRps: int
        """
        self._JobId = None
        self._DumpThread = None
        self._DumpRps = None
        self._LoadThread = None
        self._SinkerThread = None
        self._LoadRps = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DumpThread(self):
        """Number of full export threads for migration task. Value range: 1-16.
        :rtype: int
        """
        return self._DumpThread

    @DumpThread.setter
    def DumpThread(self, DumpThread):
        self._DumpThread = DumpThread

    @property
    def DumpRps(self):
        """The full export Rps for migration task. The value needs to be greater than 0.
        :rtype: int
        """
        return self._DumpRps

    @DumpRps.setter
    def DumpRps(self, DumpRps):
        self._DumpRps = DumpRps

    @property
    def LoadThread(self):
        """Number of full import threads for migration task. Value range: 1-16.
        :rtype: int
        """
        return self._LoadThread

    @LoadThread.setter
    def LoadThread(self, LoadThread):
        self._LoadThread = LoadThread

    @property
    def SinkerThread(self):
        """Number of incremental import threads for migration task. Value range: 1-128.
        :rtype: int
        """
        return self._SinkerThread

    @SinkerThread.setter
    def SinkerThread(self, SinkerThread):
        self._SinkerThread = SinkerThread

    @property
    def LoadRps(self):
        """Limits for full import Rps.
        :rtype: int
        """
        return self._LoadRps

    @LoadRps.setter
    def LoadRps(self, LoadRps):
        self._LoadRps = LoadRps


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._DumpThread = params.get("DumpThread")
        self._DumpRps = params.get("DumpRps")
        self._LoadThread = params.get("LoadThread")
        self._SinkerThread = params.get("SinkerThread")
        self._LoadRps = params.get("LoadRps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateRateLimitResponse(AbstractModel):
    """ModifyMigrateRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrateRuntimeAttributeRequest(AbstractModel):
    """ModifyMigrateRuntimeAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task id, for example: dts-2rgv0f09
        :type JobId: str
        :param _OtherOptions: Attributes that need to be modified. This structure is designed as a generic structure to separate customized attributes for multiple businesses. <br>For instance, for Redis:<br>{<br>	 "Key": "DstWriteMode",	// Target database write mode<br> 	"Value": "normal"	          // clearData (clear target instance data), overwrite (perform task in overwrite manner), normal (follow normal procedure, no additional actions, this is the default value) <br>},<br>{<br/>	 "Key": "IsDstReadOnly",	// Whether to set target database as read-only during migration<br/> 	"Value": "true"	          // true (set as read-only), false (do not set as read-only) <br/>}
        :type OtherOptions: list of KeyValuePairOption
        """
        self._JobId = None
        self._OtherOptions = None

    @property
    def JobId(self):
        """Migration task id, for example: dts-2rgv0f09
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def OtherOptions(self):
        """Attributes that need to be modified. This structure is designed as a generic structure to separate customized attributes for multiple businesses. <br>For instance, for Redis:<br>{<br>	 "Key": "DstWriteMode",	// Target database write mode<br> 	"Value": "normal"	          // clearData (clear target instance data), overwrite (perform task in overwrite manner), normal (follow normal procedure, no additional actions, this is the default value) <br>},<br>{<br/>	 "Key": "IsDstReadOnly",	// Whether to set target database as read-only during migration<br/> 	"Value": "true"	          // true (set as read-only), false (do not set as read-only) <br/>}
        :rtype: list of KeyValuePairOption
        """
        return self._OtherOptions

    @OtherOptions.setter
    def OtherOptions(self, OtherOptions):
        self._OtherOptions = OtherOptions


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("OtherOptions") is not None:
            self._OtherOptions = []
            for item in params.get("OtherOptions"):
                obj = KeyValuePairOption()
                obj._deserialize(item)
                self._OtherOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrateRuntimeAttributeResponse(AbstractModel):
    """ModifyMigrateRuntimeAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMigrationJobRequest(AbstractModel):
    """ModifyMigrationJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        :param _RunMode: Running mode. Valid values: `immediate`, `timed`.
        :type RunMode: str
        :param _MigrateOption: Migration task configuration options, which describe how the task performs migration. The `RateLimitOption` option cannot be configured. To modify the speed limit settings of the task, use the `ModifyMigrateRateLimit` API after the task starts running.
        :type MigrateOption: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        :param _SrcInfo: Source instance information
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _DstInfo: Target instance information
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        :param _JobName: Migration task name, which can contain up to 128 characters.
        :type JobName: str
        :param _ExpectRunTime: Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
        :type ExpectRunTime: str
        :param _Tags: Tag information
        :type Tags: list of TagItem
        :param _AutoRetryTimeRangeMinutes: Automatic retry time, which can be set to 5-720 minutes. 0 indicates that retry is disabled.
        :type AutoRetryTimeRangeMinutes: int
        """
        self._JobId = None
        self._RunMode = None
        self._MigrateOption = None
        self._SrcInfo = None
        self._DstInfo = None
        self._JobName = None
        self._ExpectRunTime = None
        self._Tags = None
        self._AutoRetryTimeRangeMinutes = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RunMode(self):
        """Running mode. Valid values: `immediate`, `timed`.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def MigrateOption(self):
        """Migration task configuration options, which describe how the task performs migration. The `RateLimitOption` option cannot be configured. To modify the speed limit settings of the task, use the `ModifyMigrateRateLimit` API after the task starts running.
        :rtype: :class:`tencentcloud.dts.v20211206.models.MigrateOption`
        """
        return self._MigrateOption

    @MigrateOption.setter
    def MigrateOption(self, MigrateOption):
        self._MigrateOption = MigrateOption

    @property
    def SrcInfo(self):
        """Source instance information
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        """Target instance information
        :rtype: :class:`tencentcloud.dts.v20211206.models.DBEndpointInfo`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def JobName(self):
        """Migration task name, which can contain up to 128 characters.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def ExpectRunTime(self):
        """Expected start time in the format of "2006-01-02 15:04:05", which is required if `RunMode` is `timed`.
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def Tags(self):
        """Tag information
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRetryTimeRangeMinutes(self):
        """Automatic retry time, which can be set to 5-720 minutes. 0 indicates that retry is disabled.
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RunMode = params.get("RunMode")
        if params.get("MigrateOption") is not None:
            self._MigrateOption = MigrateOption()
            self._MigrateOption._deserialize(params.get("MigrateOption"))
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DBEndpointInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DBEndpointInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._JobName = params.get("JobName")
        self._ExpectRunTime = params.get("ExpectRunTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationJobResponse(AbstractModel):
    """ModifyMigrationJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeAutoRenewFlagRequest(AbstractModel):
    """ModifySubscribeAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _AutoRenewFlag: Auto-renewal flag. Valid values: 1 (auto-renewal enabled); 0 (auto-renewal disabled).
        :type AutoRenewFlag: int
        """
        self._SubscribeId = None
        self._AutoRenewFlag = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. Valid values: 1 (auto-renewal enabled); 0 (auto-renewal disabled).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeAutoRenewFlagResponse(AbstractModel):
    """ModifySubscribeAutoRenewFlag response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Modified data subscription instance name. Value range: 1-60.
        :type SubscribeName: str
        """
        self._SubscribeId = None
        self._SubscribeName = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """Modified data subscription instance name. Value range: 1-60.
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeObjectType: Data subscription type. Valid values for non-mongo task: 0 (full instance update); 1 (data update); 2 (structure update); 3 (data + structure update). Valid values for mongo task: 0 (full instance update); 4 (subscribe to a table); 5 (subscribe to a collection).
        :type SubscribeObjectType: int
        :param _Objects: Modified subscription database table information. It will replace the original subscription object, this field is required unless SubscribeObjectType = 0 or 2.
        :type Objects: list of ModifiedSubscribeObject
        :param _DistributeRules: Kafka partitioning policy. If left blank, it will remain unchanged by default. If filled, it will replace the original policy.
        :type DistributeRules: list of DistributeRule
        :param _DefaultRuleType: Default partitioning policy. Data that does not meet the regex in DistributeRules will be partitioned according to the default partitioning policy.Default strategies supported by non-mongo products: table - partitioned by table name, pk - partitioned by table name + primary key. Mongo's default strategy only supports: collection-partitioned by collection name.This field is used in conjunction with DistributeRules. If DistributeRules is configured, this field is also required. If this field is configured, it is considered as configuring a DistributeRules, and the original partitioning policy will also be overwritten.
        :type DefaultRuleType: str
        :param _PipelineInfo: Mongo output aggregation settings, optional for Mongo tasks. If left blank, no modification will be made by default.
        :type PipelineInfo: list of PipelineInfo
        """
        self._SubscribeId = None
        self._SubscribeObjectType = None
        self._Objects = None
        self._DistributeRules = None
        self._DefaultRuleType = None
        self._PipelineInfo = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeObjectType(self):
        """Data subscription type. Valid values for non-mongo task: 0 (full instance update); 1 (data update); 2 (structure update); 3 (data + structure update). Valid values for mongo task: 0 (full instance update); 4 (subscribe to a table); 5 (subscribe to a collection).
        :rtype: int
        """
        return self._SubscribeObjectType

    @SubscribeObjectType.setter
    def SubscribeObjectType(self, SubscribeObjectType):
        self._SubscribeObjectType = SubscribeObjectType

    @property
    def Objects(self):
        """Modified subscription database table information. It will replace the original subscription object, this field is required unless SubscribeObjectType = 0 or 2.
        :rtype: list of ModifiedSubscribeObject
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def DistributeRules(self):
        """Kafka partitioning policy. If left blank, it will remain unchanged by default. If filled, it will replace the original policy.
        :rtype: list of DistributeRule
        """
        return self._DistributeRules

    @DistributeRules.setter
    def DistributeRules(self, DistributeRules):
        self._DistributeRules = DistributeRules

    @property
    def DefaultRuleType(self):
        """Default partitioning policy. Data that does not meet the regex in DistributeRules will be partitioned according to the default partitioning policy.Default strategies supported by non-mongo products: table - partitioned by table name, pk - partitioned by table name + primary key. Mongo's default strategy only supports: collection-partitioned by collection name.This field is used in conjunction with DistributeRules. If DistributeRules is configured, this field is also required. If this field is configured, it is considered as configuring a DistributeRules, and the original partitioning policy will also be overwritten.
        :rtype: str
        """
        return self._DefaultRuleType

    @DefaultRuleType.setter
    def DefaultRuleType(self, DefaultRuleType):
        self._DefaultRuleType = DefaultRuleType

    @property
    def PipelineInfo(self):
        """Mongo output aggregation settings, optional for Mongo tasks. If left blank, no modification will be made by default.
        :rtype: list of PipelineInfo
        """
        return self._PipelineInfo

    @PipelineInfo.setter
    def PipelineInfo(self, PipelineInfo):
        self._PipelineInfo = PipelineInfo


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self._Objects = []
            for item in params.get("Objects"):
                obj = ModifiedSubscribeObject()
                obj._deserialize(item)
                self._Objects.append(obj)
        if params.get("DistributeRules") is not None:
            self._DistributeRules = []
            for item in params.get("DistributeRules"):
                obj = DistributeRule()
                obj._deserialize(item)
                self._DistributeRules.append(obj)
        self._DefaultRuleType = params.get("DefaultRuleType")
        if params.get("PipelineInfo") is not None:
            self._PipelineInfo = []
            for item in params.get("PipelineInfo"):
                obj = PipelineInfo()
                obj._deserialize(item)
                self._PipelineInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySyncJobConfigRequest(AbstractModel):
    """ModifySyncJobConfig request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        :param _DynamicObjects: The modified sync objects
        :type DynamicObjects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _DynamicOptions: The modified sync task options
        :type DynamicOptions: :class:`tencentcloud.dts.v20211206.models.DynamicOptions`
        """
        self._JobId = None
        self._DynamicObjects = None
        self._DynamicOptions = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DynamicObjects(self):
        """The modified sync objects
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._DynamicObjects

    @DynamicObjects.setter
    def DynamicObjects(self, DynamicObjects):
        self._DynamicObjects = DynamicObjects

    @property
    def DynamicOptions(self):
        """The modified sync task options
        :rtype: :class:`tencentcloud.dts.v20211206.models.DynamicOptions`
        """
        return self._DynamicOptions

    @DynamicOptions.setter
    def DynamicOptions(self, DynamicOptions):
        self._DynamicOptions = DynamicOptions


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DynamicObjects") is not None:
            self._DynamicObjects = Objects()
            self._DynamicObjects._deserialize(params.get("DynamicObjects"))
        if params.get("DynamicOptions") is not None:
            self._DynamicOptions = DynamicOptions()
            self._DynamicOptions._deserialize(params.get("DynamicOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncJobConfigResponse(AbstractModel):
    """ModifySyncJobConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySyncRateLimitRequest(AbstractModel):
    """ModifySyncRateLimit request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _DumpThread: Number of full export threads for sync task. Value range: 1-16.
        :type DumpThread: int
        :param _DumpRps: The full export Rps for sync task. The value needs to be greater than 0.
        :type DumpRps: int
        :param _LoadThread: Number of full import threads for sync task. Value range: 1-16.
        :type LoadThread: int
        :param _SinkerThread: Number of incremental import threads for sync task. Value range: 1-128.
        :type SinkerThread: int
        :param _LoadRps: The full import Rps for sync task.
        :type LoadRps: int
        """
        self._JobId = None
        self._DumpThread = None
        self._DumpRps = None
        self._LoadThread = None
        self._SinkerThread = None
        self._LoadRps = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DumpThread(self):
        """Number of full export threads for sync task. Value range: 1-16.
        :rtype: int
        """
        return self._DumpThread

    @DumpThread.setter
    def DumpThread(self, DumpThread):
        self._DumpThread = DumpThread

    @property
    def DumpRps(self):
        """The full export Rps for sync task. The value needs to be greater than 0.
        :rtype: int
        """
        return self._DumpRps

    @DumpRps.setter
    def DumpRps(self, DumpRps):
        self._DumpRps = DumpRps

    @property
    def LoadThread(self):
        """Number of full import threads for sync task. Value range: 1-16.
        :rtype: int
        """
        return self._LoadThread

    @LoadThread.setter
    def LoadThread(self, LoadThread):
        self._LoadThread = LoadThread

    @property
    def SinkerThread(self):
        """Number of incremental import threads for sync task. Value range: 1-128.
        :rtype: int
        """
        return self._SinkerThread

    @SinkerThread.setter
    def SinkerThread(self, SinkerThread):
        self._SinkerThread = SinkerThread

    @property
    def LoadRps(self):
        """The full import Rps for sync task.
        :rtype: int
        """
        return self._LoadRps

    @LoadRps.setter
    def LoadRps(self, LoadRps):
        self._LoadRps = LoadRps


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._DumpThread = params.get("DumpThread")
        self._DumpRps = params.get("DumpRps")
        self._LoadThread = params.get("LoadThread")
        self._SinkerThread = params.get("SinkerThread")
        self._LoadRps = params.get("LoadRps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySyncRateLimitResponse(AbstractModel):
    """ModifySyncRateLimit response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MonitorInfo(AbstractModel):
    """Partition details of Kafka consumer group

    """

    def __init__(self):
        r"""
        :param _PartitionNo: The number of the current partition, starting from 0.
        :type PartitionNo: int
        :param _ConsumerGroupOffset: The offset of the current partition.
        :type ConsumerGroupOffset: int
        :param _ConsumerGroupLag: The amount of unconsumed data in the current partition.
        :type ConsumerGroupLag: int
        :param _Latency: The consumption delay of the current partition (in seconds).
        :type Latency: int
        """
        self._PartitionNo = None
        self._ConsumerGroupOffset = None
        self._ConsumerGroupLag = None
        self._Latency = None

    @property
    def PartitionNo(self):
        """The number of the current partition, starting from 0.
        :rtype: int
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo

    @property
    def ConsumerGroupOffset(self):
        """The offset of the current partition.
        :rtype: int
        """
        return self._ConsumerGroupOffset

    @ConsumerGroupOffset.setter
    def ConsumerGroupOffset(self, ConsumerGroupOffset):
        self._ConsumerGroupOffset = ConsumerGroupOffset

    @property
    def ConsumerGroupLag(self):
        """The amount of unconsumed data in the current partition.
        :rtype: int
        """
        return self._ConsumerGroupLag

    @ConsumerGroupLag.setter
    def ConsumerGroupLag(self, ConsumerGroupLag):
        self._ConsumerGroupLag = ConsumerGroupLag

    @property
    def Latency(self):
        """The consumption delay of the current partition (in seconds).
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency


    def _deserialize(self, params):
        self._PartitionNo = params.get("PartitionNo")
        self._ConsumerGroupOffset = params.get("ConsumerGroupOffset")
        self._ConsumerGroupLag = params.get("ConsumerGroupLag")
        self._Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Objects(AbstractModel):
    """Description of synced database objects

    """

    def __init__(self):
        r"""
        :param _Mode: Sync object type. Valid value: `Partial` (Partial objects). Note: This field may return null, indicating that no valid values can be obtained.
        :type Mode: str
        :param _Databases: Sync object, which is required if `Mode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Databases: list of Database
        :param _AdvancedObjects: Advanced object types, such as function and procedure. Note: If you want to migrate and synchronize advanced objects, the corresponding advanced object type should be included in this configuration. When advanced objects need to be synchronized, the initialization type must include the structure initialization type, that is, the Options.InitType value of the task is Structure or Full.Note: This field may return null, indicating that no valid values can be obtained.
        :type AdvancedObjects: list of str
        :param _OnlineDDL: A redundant field that specifies the online DDL type
Note: This field may return null, indicating that no valid values can be obtained.
        :type OnlineDDL: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
        self._Mode = None
        self._Databases = None
        self._AdvancedObjects = None
        self._OnlineDDL = None

    @property
    def Mode(self):
        """Sync object type. Valid value: `Partial` (Partial objects). Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Databases(self):
        """Sync object, which is required if `Mode` is `Partial`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def AdvancedObjects(self):
        """Advanced object types, such as function and procedure. Note: If you want to migrate and synchronize advanced objects, the corresponding advanced object type should be included in this configuration. When advanced objects need to be synchronized, the initialization type must include the structure initialization type, that is, the Options.InitType value of the task is Structure or Full.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AdvancedObjects

    @AdvancedObjects.setter
    def AdvancedObjects(self, AdvancedObjects):
        self._AdvancedObjects = AdvancedObjects

    @property
    def OnlineDDL(self):
        """A redundant field that specifies the online DDL type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.OnlineDDL`
        """
        return self._OnlineDDL

    @OnlineDDL.setter
    def OnlineDDL(self, OnlineDDL):
        self._OnlineDDL = OnlineDDL


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._AdvancedObjects = params.get("AdvancedObjects")
        if params.get("OnlineDDL") is not None:
            self._OnlineDDL = OnlineDDL()
            self._OnlineDDL._deserialize(params.get("OnlineDDL"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsetTimeMap(AbstractModel):
    """Checkpoint information in Kafka partition for data subscription.

    """

    def __init__(self):
        r"""
        :param _PartitionNo: Kafka partition numberNote: This field may return null, indicating that no valid values can be obtained.
        :type PartitionNo: int
        :param _Offset: Kafka offsetNote: This field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        """
        self._PartitionNo = None
        self._Offset = None

    @property
    def PartitionNo(self):
        """Kafka partition numberNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo

    @property
    def Offset(self):
        """Kafka offsetNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PartitionNo = params.get("PartitionNo")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineDDL(AbstractModel):
    """Online DDL type

    """

    def __init__(self):
        r"""
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        """Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
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
        


class Options(AbstractModel):
    """Data sync options

    """

    def __init__(self):
        r"""
        :param _InitType: Sync initialization option. Valid values: `data` (full data initialization); `Structure` (structure initialization); `Full` (full data and structure initialization); `None` (incremental data only). Default value: `Full`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitType: str
        :param _DealOfExistSameTable: Processing method for duplicate tables. Valid values: `ReportErrorAfterCheck`, `InitializeAfterDelete`, `ExecuteAfterIgnore`. Default value: `ReportErrorAfterCheck`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealOfExistSameTable: str
        :param _ConflictHandleType: Conflict processing option. Valid values: `ReportError` (report an error); `Ignore` (ignore); `Cover` (overwrite); `ConditionCover` (conditionally overwrite). Default value: `ReportError`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleType: str
        :param _AddAdditionalColumn: Whether to add the additional column
Note: This field may return null, indicating that no valid values can be obtained.
        :type AddAdditionalColumn: bool
        :param _OpTypes: DML and DDL options to be synced. Valid values: `Insert` (INSERT operations); `Update` (UPDATE operations); `Delete` (DELETE operations); `DDL` (structure sync); `PartialDDL` (custom option, which is used together with `DdlOptions`). You can also leave this parameter empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OpTypes: list of str
        :param _ConflictHandleOption: Detailed option for conflict processing, such as condition rows and operations in conditional overwrite.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConflictHandleOption: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        :param _DdlOptions: DDL statements to be synced
Note: This field may return null, indicating that no valid values can be obtained.
        :type DdlOptions: list of DdlOption
        :param _KafkaOption: Kafka sync options
Note: This field may return null, indicating that no valid values can be obtained.
        :type KafkaOption: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        :param _RateLimitOption: Task speed limit information
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitOption: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        :param _AutoRetryTimeRangeMinutes: Settings of the automatic retry time range
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRetryTimeRangeMinutes: int
        :param _FilterBeginCommit: 
        :type FilterBeginCommit: bool
        :param _FilterCheckpoint: 
        :type FilterCheckpoint: bool
        """
        self._InitType = None
        self._DealOfExistSameTable = None
        self._ConflictHandleType = None
        self._AddAdditionalColumn = None
        self._OpTypes = None
        self._ConflictHandleOption = None
        self._DdlOptions = None
        self._KafkaOption = None
        self._RateLimitOption = None
        self._AutoRetryTimeRangeMinutes = None
        self._FilterBeginCommit = None
        self._FilterCheckpoint = None

    @property
    def InitType(self):
        """Sync initialization option. Valid values: `data` (full data initialization); `Structure` (structure initialization); `Full` (full data and structure initialization); `None` (incremental data only). Default value: `Full`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InitType

    @InitType.setter
    def InitType(self, InitType):
        self._InitType = InitType

    @property
    def DealOfExistSameTable(self):
        """Processing method for duplicate tables. Valid values: `ReportErrorAfterCheck`, `InitializeAfterDelete`, `ExecuteAfterIgnore`. Default value: `ReportErrorAfterCheck`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DealOfExistSameTable

    @DealOfExistSameTable.setter
    def DealOfExistSameTable(self, DealOfExistSameTable):
        self._DealOfExistSameTable = DealOfExistSameTable

    @property
    def ConflictHandleType(self):
        """Conflict processing option. Valid values: `ReportError` (report an error); `Ignore` (ignore); `Cover` (overwrite); `ConditionCover` (conditionally overwrite). Default value: `ReportError`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ConflictHandleType

    @ConflictHandleType.setter
    def ConflictHandleType(self, ConflictHandleType):
        self._ConflictHandleType = ConflictHandleType

    @property
    def AddAdditionalColumn(self):
        """Whether to add the additional column
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AddAdditionalColumn

    @AddAdditionalColumn.setter
    def AddAdditionalColumn(self, AddAdditionalColumn):
        self._AddAdditionalColumn = AddAdditionalColumn

    @property
    def OpTypes(self):
        """DML and DDL options to be synced. Valid values: `Insert` (INSERT operations); `Update` (UPDATE operations); `Delete` (DELETE operations); `DDL` (structure sync); `PartialDDL` (custom option, which is used together with `DdlOptions`). You can also leave this parameter empty.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._OpTypes

    @OpTypes.setter
    def OpTypes(self, OpTypes):
        self._OpTypes = OpTypes

    @property
    def ConflictHandleOption(self):
        """Detailed option for conflict processing, such as condition rows and operations in conditional overwrite.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConflictHandleOption`
        """
        return self._ConflictHandleOption

    @ConflictHandleOption.setter
    def ConflictHandleOption(self, ConflictHandleOption):
        self._ConflictHandleOption = ConflictHandleOption

    @property
    def DdlOptions(self):
        """DDL statements to be synced
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DdlOption
        """
        return self._DdlOptions

    @DdlOptions.setter
    def DdlOptions(self, DdlOptions):
        self._DdlOptions = DdlOptions

    @property
    def KafkaOption(self):
        """Kafka sync options
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.KafkaOption`
        """
        return self._KafkaOption

    @KafkaOption.setter
    def KafkaOption(self, KafkaOption):
        self._KafkaOption = KafkaOption

    @property
    def RateLimitOption(self):
        """Task speed limit information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.RateLimitOption`
        """
        return self._RateLimitOption

    @RateLimitOption.setter
    def RateLimitOption(self, RateLimitOption):
        self._RateLimitOption = RateLimitOption

    @property
    def AutoRetryTimeRangeMinutes(self):
        """Settings of the automatic retry time range
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def FilterBeginCommit(self):
        """
        :rtype: bool
        """
        return self._FilterBeginCommit

    @FilterBeginCommit.setter
    def FilterBeginCommit(self, FilterBeginCommit):
        self._FilterBeginCommit = FilterBeginCommit

    @property
    def FilterCheckpoint(self):
        """
        :rtype: bool
        """
        return self._FilterCheckpoint

    @FilterCheckpoint.setter
    def FilterCheckpoint(self, FilterCheckpoint):
        self._FilterCheckpoint = FilterCheckpoint


    def _deserialize(self, params):
        self._InitType = params.get("InitType")
        self._DealOfExistSameTable = params.get("DealOfExistSameTable")
        self._ConflictHandleType = params.get("ConflictHandleType")
        self._AddAdditionalColumn = params.get("AddAdditionalColumn")
        self._OpTypes = params.get("OpTypes")
        if params.get("ConflictHandleOption") is not None:
            self._ConflictHandleOption = ConflictHandleOption()
            self._ConflictHandleOption._deserialize(params.get("ConflictHandleOption"))
        if params.get("DdlOptions") is not None:
            self._DdlOptions = []
            for item in params.get("DdlOptions"):
                obj = DdlOption()
                obj._deserialize(item)
                self._DdlOptions.append(obj)
        if params.get("KafkaOption") is not None:
            self._KafkaOption = KafkaOption()
            self._KafkaOption._deserialize(params.get("KafkaOption"))
        if params.get("RateLimitOption") is not None:
            self._RateLimitOption = RateLimitOption()
            self._RateLimitOption._deserialize(params.get("RateLimitOption"))
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        self._FilterBeginCommit = params.get("FilterBeginCommit")
        self._FilterCheckpoint = params.get("FilterCheckpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionAssignment(AbstractModel):
    """The partition allocation of Kafka consumer groups in data subscriptions. This data is queried in real time. If you need the latest data, you need to call the interface again.

    """

    def __init__(self):
        r"""
        :param _ClientId: The clientId of the consumer
        :type ClientId: str
        :param _PartitionNo: The partition is being consumed by this consumer.Note: This field may return null, indicating that no valid values can be obtained.
        :type PartitionNo: list of int non-negative
        """
        self._ClientId = None
        self._PartitionNo = None

    @property
    def ClientId(self):
        """The clientId of the consumer
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def PartitionNo(self):
        """The partition is being consumed by this consumer.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int non-negative
        """
        return self._PartitionNo

    @PartitionNo.setter
    def PartitionNo(self, PartitionNo):
        self._PartitionNo = PartitionNo


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._PartitionNo = params.get("PartitionNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobRequest(AbstractModel):
    """PauseMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseMigrateJobResponse(AbstractModel):
    """PauseMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PauseSyncJobRequest(AbstractModel):
    """PauseSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseSyncJobResponse(AbstractModel):
    """PauseSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PipelineInfo(AbstractModel):
    """Mongo output aggregation settings. Default value: Change Event.

    """

    def __init__(self):
        r"""
        :param _AggOp: Aggregation operators: $addFields, $match, $project, $replaceRoot, $redact, $replaceWith, $set, $unset. $replaceWith, $set, $unset are available options for subscription instances that are version 4.2 or higher.Note: This field may return null, indicating that no valid values can be obtained.
        :type AggOp: str
        :param _AggCmd: Aggregation expression must be in json format.Note: This field may return null, indicating that no valid values can be obtained.
        :type AggCmd: str
        """
        self._AggOp = None
        self._AggCmd = None

    @property
    def AggOp(self):
        """Aggregation operators: $addFields, $match, $project, $replaceRoot, $redact, $replaceWith, $set, $unset. $replaceWith, $set, $unset are available options for subscription instances that are version 4.2 or higher.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AggOp

    @AggOp.setter
    def AggOp(self, AggOp):
        self._AggOp = AggOp

    @property
    def AggCmd(self):
        """Aggregation expression must be in json format.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AggCmd

    @AggCmd.setter
    def AggCmd(self, AggCmd):
        self._AggCmd = AggCmd


    def _deserialize(self, params):
        self._AggOp = params.get("AggOp")
        self._AggCmd = params.get("AggCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessProgress(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
        :param _Status: Step status. Valid values: `notStarted`, `running`, `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Percent: Progress information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param _StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param _StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param _Message: The prompt output in the current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Steps: Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Steps: list of StepDetailInfo
        """
        self._Status = None
        self._Percent = None
        self._StepAll = None
        self._StepNow = None
        self._Message = None
        self._Steps = None

    @property
    def Status(self):
        """Step status. Valid values: `notStarted`, `running`, `success`, `failed`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """Progress information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def StepAll(self):
        """Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Message(self):
        """The prompt output in the current step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Steps(self):
        """Step information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepDetailInfo
        """
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Message = params.get("Message")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = StepDetailInfo()
                obj._deserialize(item)
                self._Steps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStepTip(AbstractModel):
    """Object of the error or warning information

    """

    def __init__(self):
        r"""
        :param _Message: Prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param _HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        """
        self._Message = None
        self._Solution = None
        self._HelpDoc = None

    @property
    def Message(self):
        """Prompt message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        """Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitOption(AbstractModel):
    """Speed limit details of migration and sync tasks

    """

    def __init__(self):
        r"""
        :param _CurrentDumpThread: The number of full export threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 16.Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentDumpThread: int
        :param _DefaultDumpThread: The default number of full export threads. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultDumpThread: int
        :param _CurrentDumpRps: The full export Rps currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 50,000,000.Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentDumpRps: int
        :param _DefaultDumpRps: The default full export Rps. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultDumpRps: int
        :param _CurrentLoadThread: The number of full import threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 16.Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentLoadThread: int
        :param _DefaultLoadThread: The default number of full import threads. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultLoadThread: int
        :param _CurrentLoadRps: The full import Rps currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 50,000,000.Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentLoadRps: int
        :param _DefaultLoadRps: The default full import Rps. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultLoadRps: int
        :param _CurrentSinkerThread: The number of incremental import threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 128.Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentSinkerThread: int
        :param _DefaultSinkerThread: The default number of incremental import threads. This field is only meaningful in the output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultSinkerThread: int
        :param _HasUserSetRateLimit: enum:"no"/"yes", no: the user has not set a speed limit; yes: a speed limit has been set. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :type HasUserSetRateLimit: str
        """
        self._CurrentDumpThread = None
        self._DefaultDumpThread = None
        self._CurrentDumpRps = None
        self._DefaultDumpRps = None
        self._CurrentLoadThread = None
        self._DefaultLoadThread = None
        self._CurrentLoadRps = None
        self._DefaultLoadRps = None
        self._CurrentSinkerThread = None
        self._DefaultSinkerThread = None
        self._HasUserSetRateLimit = None

    @property
    def CurrentDumpThread(self):
        """The number of full export threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 16.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentDumpThread

    @CurrentDumpThread.setter
    def CurrentDumpThread(self, CurrentDumpThread):
        self._CurrentDumpThread = CurrentDumpThread

    @property
    def DefaultDumpThread(self):
        """The default number of full export threads. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DefaultDumpThread

    @DefaultDumpThread.setter
    def DefaultDumpThread(self, DefaultDumpThread):
        self._DefaultDumpThread = DefaultDumpThread

    @property
    def CurrentDumpRps(self):
        """The full export Rps currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 50,000,000.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentDumpRps

    @CurrentDumpRps.setter
    def CurrentDumpRps(self, CurrentDumpRps):
        self._CurrentDumpRps = CurrentDumpRps

    @property
    def DefaultDumpRps(self):
        """The default full export Rps. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DefaultDumpRps

    @DefaultDumpRps.setter
    def DefaultDumpRps(self, DefaultDumpRps):
        self._DefaultDumpRps = DefaultDumpRps

    @property
    def CurrentLoadThread(self):
        """The number of full import threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 16.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentLoadThread

    @CurrentLoadThread.setter
    def CurrentLoadThread(self, CurrentLoadThread):
        self._CurrentLoadThread = CurrentLoadThread

    @property
    def DefaultLoadThread(self):
        """The default number of full import threads. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DefaultLoadThread

    @DefaultLoadThread.setter
    def DefaultLoadThread(self, DefaultLoadThread):
        self._DefaultLoadThread = DefaultLoadThread

    @property
    def CurrentLoadRps(self):
        """The full import Rps currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 50,000,000.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentLoadRps

    @CurrentLoadRps.setter
    def CurrentLoadRps(self, CurrentLoadRps):
        self._CurrentLoadRps = CurrentLoadRps

    @property
    def DefaultLoadRps(self):
        """The default full import Rps. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DefaultLoadRps

    @DefaultLoadRps.setter
    def DefaultLoadRps(self, DefaultLoadRps):
        self._DefaultLoadRps = DefaultLoadRps

    @property
    def CurrentSinkerThread(self):
        """The number of incremental import threads currently in effect. The value of this field can be adjusted when configuring the task. Note: If it is not set or set to 0, it means the current value is maintained. The maximum value is 128.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentSinkerThread

    @CurrentSinkerThread.setter
    def CurrentSinkerThread(self, CurrentSinkerThread):
        self._CurrentSinkerThread = CurrentSinkerThread

    @property
    def DefaultSinkerThread(self):
        """The default number of incremental import threads. This field is only meaningful in the output parameter.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DefaultSinkerThread

    @DefaultSinkerThread.setter
    def DefaultSinkerThread(self, DefaultSinkerThread):
        self._DefaultSinkerThread = DefaultSinkerThread

    @property
    def HasUserSetRateLimit(self):
        """enum:"no"/"yes", no: the user has not set a speed limit; yes: a speed limit has been set. This field is only meaningful in the output parameter.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HasUserSetRateLimit

    @HasUserSetRateLimit.setter
    def HasUserSetRateLimit(self, HasUserSetRateLimit):
        self._HasUserSetRateLimit = HasUserSetRateLimit


    def _deserialize(self, params):
        self._CurrentDumpThread = params.get("CurrentDumpThread")
        self._DefaultDumpThread = params.get("DefaultDumpThread")
        self._CurrentDumpRps = params.get("CurrentDumpRps")
        self._DefaultDumpRps = params.get("DefaultDumpRps")
        self._CurrentLoadThread = params.get("CurrentLoadThread")
        self._DefaultLoadThread = params.get("DefaultLoadThread")
        self._CurrentLoadRps = params.get("CurrentLoadRps")
        self._DefaultLoadRps = params.get("DefaultLoadRps")
        self._CurrentSinkerThread = params.get("CurrentSinkerThread")
        self._DefaultSinkerThread = params.get("DefaultSinkerThread")
        self._HasUserSetRateLimit = params.get("HasUserSetRateLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobRequest(AbstractModel):
    """RecoverMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMigrateJobResponse(AbstractModel):
    """RecoverMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RecoverSyncJobRequest(AbstractModel):
    """RecoverSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task instance ID in the format of `sync-werwfs23`, which is used to identify a sync task.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverSyncJobResponse(AbstractModel):
    """RecoverSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetConsumerGroupOffsetRequest(AbstractModel):
    """ResetConsumerGroupOffset request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Subscription instance ID
        :type SubscribeId: str
        :param _TopicName: Subscribed Kafka topic
        :type TopicName: str
        :param _ConsumerGroupName: Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :type ConsumerGroupName: str
        :param _PartitionNos: The partition number of offset needs to be modified.
        :type PartitionNos: list of int
        :param _ResetMode: Reset mode. Valid values: earliest (start consumption from the earliest position); latest (start consumption from the latest position); datetime (start consumption from the most recent checkpoint before the specified time).
        :type ResetMode: str
        :param _ResetDatetime: When ResetMode is datetime, this field needs to be filled in, the format is: Y-m-d h:m:s. If not filled in, the default time is 0, and the effect is the same as earliest.
        :type ResetDatetime: str
        """
        self._SubscribeId = None
        self._TopicName = None
        self._ConsumerGroupName = None
        self._PartitionNos = None
        self._ResetMode = None
        self._ResetDatetime = None

    @property
    def SubscribeId(self):
        """Subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def TopicName(self):
        """Subscribed Kafka topic
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ConsumerGroupName(self):
        """Consumer group name. The full name of the actual consumer group is in the form: consumer-grp-#{SubscribeId}-#{ConsumerGroupName}.
        :rtype: str
        """
        return self._ConsumerGroupName

    @ConsumerGroupName.setter
    def ConsumerGroupName(self, ConsumerGroupName):
        self._ConsumerGroupName = ConsumerGroupName

    @property
    def PartitionNos(self):
        """The partition number of offset needs to be modified.
        :rtype: list of int
        """
        return self._PartitionNos

    @PartitionNos.setter
    def PartitionNos(self, PartitionNos):
        self._PartitionNos = PartitionNos

    @property
    def ResetMode(self):
        """Reset mode. Valid values: earliest (start consumption from the earliest position); latest (start consumption from the latest position); datetime (start consumption from the most recent checkpoint before the specified time).
        :rtype: str
        """
        return self._ResetMode

    @ResetMode.setter
    def ResetMode(self, ResetMode):
        self._ResetMode = ResetMode

    @property
    def ResetDatetime(self):
        """When ResetMode is datetime, this field needs to be filled in, the format is: Y-m-d h:m:s. If not filled in, the default time is 0, and the effect is the same as earliest.
        :rtype: str
        """
        return self._ResetDatetime

    @ResetDatetime.setter
    def ResetDatetime(self, ResetDatetime):
        self._ResetDatetime = ResetDatetime


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._TopicName = params.get("TopicName")
        self._ConsumerGroupName = params.get("ConsumerGroupName")
        self._PartitionNos = params.get("PartitionNos")
        self._ResetMode = params.get("ResetMode")
        self._ResetDatetime = params.get("ResetDatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetConsumerGroupOffsetResponse(AbstractModel):
    """ResetConsumerGroupOffset response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResizeSyncJobRequest(AbstractModel):
    """ResizeSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        :param _NewInstanceClass: Task specification
        :type NewInstanceClass: str
        """
        self._JobId = None
        self._NewInstanceClass = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def NewInstanceClass(self):
        """Task specification
        :rtype: str
        """
        return self._NewInstanceClass

    @NewInstanceClass.setter
    def NewInstanceClass(self, NewInstanceClass):
        self._NewInstanceClass = NewInstanceClass


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._NewInstanceClass = params.get("NewInstanceClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeSyncJobResponse(AbstractModel):
    """ResizeSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeMigrateJobRequest(AbstractModel):
    """ResumeMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _ResumeOption: Task resumption mode. Valid values: `clearData` (Clearing the target instance data); `overwrite` (Executing the task in overwrite mode); `normal` (Following the normal process without additional operations). `clearData` and `overwrite` are only valid for Redis links and `normal` for non-Redis links.
        :type ResumeOption: str
        """
        self._JobId = None
        self._ResumeOption = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ResumeOption(self):
        """Task resumption mode. Valid values: `clearData` (Clearing the target instance data); `overwrite` (Executing the task in overwrite mode); `normal` (Following the normal process without additional operations). `clearData` and `overwrite` are only valid for Redis links and `normal` for non-Redis links.
        :rtype: str
        """
        return self._ResumeOption

    @ResumeOption.setter
    def ResumeOption(self, ResumeOption):
        self._ResumeOption = ResumeOption


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ResumeOption = params.get("ResumeOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeMigrateJobResponse(AbstractModel):
    """ResumeMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeSubscribeRequest(AbstractModel):
    """ResumeSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSubscribeResponse(AbstractModel):
    """ResumeSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResumeSyncJobRequest(AbstractModel):
    """ResumeSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSyncJobResponse(AbstractModel):
    """ResumeSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RoleItem(AbstractModel):
    """Role object, which is exclusive to PostgreSQL.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoleName: str
        :param _NewRoleName: Role name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewRoleName: str
        """
        self._RoleName = None
        self._NewRoleName = None

    @property
    def RoleName(self):
        """Role name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def NewRoleName(self):
        """Role name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewRoleName

    @NewRoleName.setter
    def NewRoleName(self, NewRoleName):
        self._NewRoleName = NewRoleName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._NewRoleName = params.get("NewRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemRequest(AbstractModel):
    """SkipCheckItem request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        :param _StepIds: ID of the check step to be skipped, which is obtained in the `StepInfo[i].StepId` field returned by the `DescribeMigrationCheckJob` API, such as "OptimizeCheck".
        :type StepIds: list of str
        :param _ForeignKeyFlag: When the check fails due to foreign key dependency, you can use this field to specify whether to migrate the foreign key dependency. The foreign key dependency won’t be migrated when `StepIds` contains `ConstraintCheck` and the value of this field is `shield`, and will be migrated when `StepIds` contains `ConstraintCheck` and the value of this field is `migrate`.
        :type ForeignKeyFlag: str
        """
        self._JobId = None
        self._StepIds = None
        self._ForeignKeyFlag = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        """ID of the check step to be skipped, which is obtained in the `StepInfo[i].StepId` field returned by the `DescribeMigrationCheckJob` API, such as "OptimizeCheck".
        :rtype: list of str
        """
        return self._StepIds

    @StepIds.setter
    def StepIds(self, StepIds):
        self._StepIds = StepIds

    @property
    def ForeignKeyFlag(self):
        """When the check fails due to foreign key dependency, you can use this field to specify whether to migrate the foreign key dependency. The foreign key dependency won’t be migrated when `StepIds` contains `ConstraintCheck` and the value of this field is `shield`, and will be migrated when `StepIds` contains `ConstraintCheck` and the value of this field is `migrate`.
        :rtype: str
        """
        return self._ForeignKeyFlag

    @ForeignKeyFlag.setter
    def ForeignKeyFlag(self, ForeignKeyFlag):
        self._ForeignKeyFlag = ForeignKeyFlag


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StepIds = params.get("StepIds")
        self._ForeignKeyFlag = params.get("ForeignKeyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCheckItemResponse(AbstractModel):
    """SkipCheckItem response structure.

    """

    def __init__(self):
        r"""
        :param _Message: Message prompted for skipping the check item
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """Message prompted for skipping the check item
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class SkipSyncCheckItemRequest(AbstractModel):
    """SkipSyncCheckItem request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Task ID, such as "sync-4ddgid2".
        :type JobId: str
        :param _StepIds: ID of the check step to be skipped, which is obtained in the `StepInfos[i].StepId` field returned by the `DescribeCheckSyncJobResult` API, such as "OptimizeCheck".
        :type StepIds: list of str
        """
        self._JobId = None
        self._StepIds = None

    @property
    def JobId(self):
        """Task ID, such as "sync-4ddgid2".
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StepIds(self):
        """ID of the check step to be skipped, which is obtained in the `StepInfos[i].StepId` field returned by the `DescribeCheckSyncJobResult` API, such as "OptimizeCheck".
        :rtype: list of str
        """
        return self._StepIds

    @StepIds.setter
    def StepIds(self, StepIds):
        self._StepIds = StepIds


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StepIds = params.get("StepIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipSyncCheckItemResponse(AbstractModel):
    """SkipSyncCheckItem response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SkippedDetail(AbstractModel):
    """Details of skipped tables

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Items: Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of SkippedItem
        """
        self._TotalCount = None
        self._Items = None

    @property
    def TotalCount(self):
        """Number of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        """Details of skipped tables
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SkippedItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SkippedItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkippedItem(AbstractModel):
    """Details of skipped tables

    """

    def __init__(self):
        r"""
        :param _Db: Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Db: str
        :param _Table: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param _Reason: The cause why check is not initiated
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self._Db = None
        self._Table = None
        self._Reason = None

    @property
    def Db(self):
        """Database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def Table(self):
        """Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Reason(self):
        """The cause why check is not initiated
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Db = params.get("Db")
        self._Table = params.get("Table")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareRequest(AbstractModel):
    """StartCompare request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCompareResponse(AbstractModel):
    """StartCompare response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartModifySyncJobRequest(AbstractModel):
    """StartModifySyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartModifySyncJobResponse(AbstractModel):
    """StartModifySyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartSubscribeRequest(AbstractModel):
    """StartSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        """
        self._SubscribeId = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSubscribeResponse(AbstractModel):
    """StartSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StepDetailInfo(AbstractModel):
    """Step information

    """

    def __init__(self):
        r"""
        :param _StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param _StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param _StepId: Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param _Status: Step status. Valid values: `success`, `failed`, `running`, `notStarted`. Default value: `notStarted`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _StartTime: Start time of the current step in the format of "yyyy-mm-dd hh:mm:ss". If this field does not exist or is empty, it is meaningless.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _StepMessage: Step error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepMessage: str
        :param _Percent: Execution progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param _Errors: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of ProcessStepTip
        :param _Warnings: Warning
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warnings: list of ProcessStepTip
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None
        self._StepMessage = None
        self._Percent = None
        self._Errors = None
        self._Warnings = None

    @property
    def StepNo(self):
        """Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """Step status. Valid values: `success`, `failed`, `running`, `notStarted`. Default value: `notStarted`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """Start time of the current step in the format of "yyyy-mm-dd hh:mm:ss". If this field does not exist or is empty, it is meaningless.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StepMessage(self):
        """Step error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepMessage

    @StepMessage.setter
    def StepMessage(self, StepMessage):
        self._StepMessage = StepMessage

    @property
    def Percent(self):
        """Execution progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Errors(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProcessStepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """Warning
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ProcessStepTip
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._StepMessage = params.get("StepMessage")
        self._Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = ProcessStepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepInfo(AbstractModel):
    """Step details

    """

    def __init__(self):
        r"""
        :param _StepNo: Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param _StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param _StepId: Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param _Status: Status of the current step. Valid values: `notStarted`, `running`, `failed`, `finished, `skipped`, `paused`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _StartTime: Step start time, which may be null.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _Errors: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of StepTip
        :param _Warnings: Warning message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Warnings: list of StepTip
        :param _Progress: Current step progress. Value range: 0-100. The value `-1` indicates that the progress of the current step is unavailable. Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        """
        self._StepNo = None
        self._StepName = None
        self._StepId = None
        self._Status = None
        self._StartTime = None
        self._Errors = None
        self._Warnings = None
        self._Progress = None

    @property
    def StepNo(self):
        """Step number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def StepName(self):
        """Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """Step ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def Status(self):
        """Status of the current step. Valid values: `notStarted`, `running`, `failed`, `finished, `skipped`, `paused`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """Step start time, which may be null.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Errors(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """Warning message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepTip
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings

    @property
    def Progress(self):
        """Current step progress. Value range: 0-100. The value `-1` indicates that the progress of the current step is unavailable. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress


    def _deserialize(self, params):
        self._StepNo = params.get("StepNo")
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = StepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = StepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        self._Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepTip(AbstractModel):
    """Error or warning information in the current step

    """

    def __init__(self):
        r"""
        :param _Code: Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type Code: str
        :param _Message: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Solution: Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type Solution: str
        :param _HelpDoc: Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        :param _SkipInfo: Whether the current step is skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :type SkipInfo: str
        """
        self._Code = None
        self._Message = None
        self._Solution = None
        self._HelpDoc = None
        self._SkipInfo = None

    @property
    def Code(self):
        """Error code
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Solution(self):
        """Solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def HelpDoc(self):
        """Help document
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc

    @property
    def SkipInfo(self):
        """Whether the current step is skipped
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SkipInfo

    @SkipInfo.setter
    def SkipInfo(self, SkipInfo):
        self._SkipInfo = SkipInfo


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._Solution = params.get("Solution")
        self._HelpDoc = params.get("HelpDoc")
        self._SkipInfo = params.get("SkipInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareRequest(AbstractModel):
    """StopCompare request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Migration task ID
        :type JobId: str
        :param _CompareTaskId: Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :type CompareTaskId: str
        """
        self._JobId = None
        self._CompareTaskId = None

    @property
    def JobId(self):
        """Migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CompareTaskId(self):
        """Data consistency check task ID in the format of `dts-8yv4w2i1-cmp-37skmii9`
        :rtype: str
        """
        return self._CompareTaskId

    @CompareTaskId.setter
    def CompareTaskId(self, CompareTaskId):
        self._CompareTaskId = CompareTaskId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._CompareTaskId = params.get("CompareTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCompareResponse(AbstractModel):
    """StopCompare response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Data migration task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Data migration task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopSyncJobRequest(AbstractModel):
    """StopSyncJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Sync task ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSyncJobResponse(AbstractModel):
    """StopSyncJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SubsErr(AbstractModel):
    """Subscription error message

    """

    def __init__(self):
        r"""
        :param _Message: Error message
        :type Message: str
        """
        self._Message = None

    @property
    def Message(self):
        """Error message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeCheckStepInfo(AbstractModel):
    """Information about each step of the subscription check task.

    """

    def __init__(self):
        r"""
        :param _StepName: Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepName: str
        :param _StepId: Step Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepId: str
        :param _StepNo: Step number, starting from 1
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNo: int
        :param _Status: Current step status. Valid values: notStarted, running, finished, failed.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Percent: Current step progressNote: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param _Errors: Error messageNote: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of SubscribeCheckStepTip
        :param _Warnings: Warning messageNote: This field may return null, indicating that no valid values can be obtained.
        :type Warnings: list of SubscribeCheckStepTip
        """
        self._StepName = None
        self._StepId = None
        self._StepNo = None
        self._Status = None
        self._Percent = None
        self._Errors = None
        self._Warnings = None

    @property
    def StepName(self):
        """Step name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StepId(self):
        """Step Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StepId

    @StepId.setter
    def StepId(self, StepId):
        self._StepId = StepId

    @property
    def StepNo(self):
        """Step number, starting from 1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNo

    @StepNo.setter
    def StepNo(self, StepNo):
        self._StepNo = StepNo

    @property
    def Status(self):
        """Current step status. Valid values: notStarted, running, finished, failed.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """Current step progressNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Errors(self):
        """Error messageNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubscribeCheckStepTip
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Warnings(self):
        """Warning messageNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubscribeCheckStepTip
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._StepId = params.get("StepId")
        self._StepNo = params.get("StepNo")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubscribeCheckStepTip()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = SubscribeCheckStepTip()
                obj._deserialize(item)
                self._Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeCheckStepTip(AbstractModel):
    """Prompts for subscription check tasks

    """

    def __init__(self):
        r"""
        :param _Message: Error or warning detailsNote: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _HelpDoc: Help documentation
Note: This field may return null, indicating that no valid values can be obtained.
        :type HelpDoc: str
        """
        self._Message = None
        self._HelpDoc = None

    @property
    def Message(self):
        """Error or warning detailsNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def HelpDoc(self):
        """Help documentation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HelpDoc

    @HelpDoc.setter
    def HelpDoc(self, HelpDoc):
        self._HelpDoc = HelpDoc


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._HelpDoc = params.get("HelpDoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeInfo(AbstractModel):
    """Subscription instance information

    """

    def __init__(self):
        r"""
        :param _SubscribeId: Data subscription instance ID
        :type SubscribeId: str
        :param _SubscribeName: Data subscription instance name
        :type SubscribeName: str
        :param _Topic: Kafka topic for data sent by the subscription instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type Topic: str
        :param _Product: Subscription instance type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :type Product: str
        :param _InstanceId: The subscribed database instance ID (if the subscription is a cloud database). If the instance is not on Tencent Cloud, this value is empty.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceStatus: Cloud database status: running, isolated, offline. If it is not on the cloud, this value is empty.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStatus: str
        :param _Status: Data subscription lifecycle status. Valid values: normal (normal), isolating (isolating), isolated (isolated), offlining (offlining), post2PrePayIng (changing from pay-as-you-go to monthly subscription).
        :type Status: str
        :param _SubsStatus: Data subscription status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :type SubsStatus: str
        :param _ModifyTime: Last modification time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModifyTime: str
        :param _CreateTime: Creation time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _IsolateTime: Isolation time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateTime: str
        :param _ExpireTime: Expiration time for monthly subscription tasks, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _OfflineTime: Offline time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        :param _PayType: Billing mode. 1: pay-as-you-go
        :type PayType: int
        :param _AutoRenewFlag: Auto-renewal flag. It is meaningful only when PayType=0. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled).
        :type AutoRenewFlag: int
        :param _Region: Data subscription instance region
        :type Region: str
        :param _AccessType: Access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC).Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessType: str
        :param _Endpoints: Database node information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Endpoints: list of EndpointItem
        :param _SubscribeVersion: Data subscription version, only Kafka version is currently supported.Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscribeVersion: str
        :param _Tags: TagNote: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _Errors: Task error messageNote: This field may return null, indicating that no valid values can be obtained.
        :type Errors: list of SubsErr
        """
        self._SubscribeId = None
        self._SubscribeName = None
        self._Topic = None
        self._Product = None
        self._InstanceId = None
        self._InstanceStatus = None
        self._Status = None
        self._SubsStatus = None
        self._ModifyTime = None
        self._CreateTime = None
        self._IsolateTime = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._PayType = None
        self._AutoRenewFlag = None
        self._Region = None
        self._AccessType = None
        self._Endpoints = None
        self._SubscribeVersion = None
        self._Tags = None
        self._Errors = None

    @property
    def SubscribeId(self):
        """Data subscription instance ID
        :rtype: str
        """
        return self._SubscribeId

    @SubscribeId.setter
    def SubscribeId(self, SubscribeId):
        self._SubscribeId = SubscribeId

    @property
    def SubscribeName(self):
        """Data subscription instance name
        :rtype: str
        """
        return self._SubscribeName

    @SubscribeName.setter
    def SubscribeName(self, SubscribeName):
        self._SubscribeName = SubscribeName

    @property
    def Topic(self):
        """Kafka topic for data sent by the subscription instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Product(self):
        """Subscription instance type. Currently, cynosdbmysql, mariadb, mongodb, mysql, percona, tdpg, tdsqlpercona are supported.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        """The subscribed database instance ID (if the subscription is a cloud database). If the instance is not on Tencent Cloud, this value is empty.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """Cloud database status: running, isolated, offline. If it is not on the cloud, this value is empty.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def Status(self):
        """Data subscription lifecycle status. Valid values: normal (normal), isolating (isolating), isolated (isolated), offlining (offlining), post2PrePayIng (changing from pay-as-you-go to monthly subscription).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubsStatus(self):
        """Data subscription status. Valid values: notStarted, checking, checkNotPass, checkPass, starting, running, error.
        :rtype: str
        """
        return self._SubsStatus

    @SubsStatus.setter
    def SubsStatus(self, SubsStatus):
        self._SubsStatus = SubsStatus

    @property
    def ModifyTime(self):
        """Last modification time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def CreateTime(self):
        """Creation time, the format is: Y-m-d h:m:s.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsolateTime(self):
        """Isolation time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def ExpireTime(self):
        """Expiration time for monthly subscription tasks, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """Offline time, the format is: Y-m-d h:m:s. Default time: 0000-00-00 00:00:00.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def PayType(self):
        """Billing mode. 1: pay-as-you-go
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def AutoRenewFlag(self):
        """Auto-renewal flag. It is meaningful only when PayType=0. Valid values: 0 (auto-renewal disabled); 1 (auto-renewal enabled).
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Region(self):
        """Data subscription instance region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """Access type. Valid values: extranet (public network); vpncloud (VPN access); dcg (Direct Connect); ccn (CCN); cdb (database); cvm (self-build on CVM); intranet (intranet); vpc (VPC).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Endpoints(self):
        """Database node information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def SubscribeVersion(self):
        """Data subscription version, only Kafka version is currently supported.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubscribeVersion

    @SubscribeVersion.setter
    def SubscribeVersion(self, SubscribeVersion):
        self._SubscribeVersion = SubscribeVersion

    @property
    def Tags(self):
        """TagNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Errors(self):
        """Task error messageNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SubsErr
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors


    def _deserialize(self, params):
        self._SubscribeId = params.get("SubscribeId")
        self._SubscribeName = params.get("SubscribeName")
        self._Topic = params.get("Topic")
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._Status = params.get("Status")
        self._SubsStatus = params.get("SubsStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._IsolateTime = params.get("IsolateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._PayType = params.get("PayType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._SubscribeVersion = params.get("SubscribeVersion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SubsErr()
                obj._deserialize(item)
                self._Errors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeKafkaConfig(AbstractModel):
    """Number of subscribed Kafka partitions and partition rules. mariadb, percona, tdsqlmysql, tdpg do not support custom partitions, so DistributeRules and DefaultRuleType can be left blank, but NumberOfPartitions is required.

    """

    def __init__(self):
        r"""
        :param _NumberOfPartitions: Number of Kafka partitions. Valid values: 1, 4, 8.Note: This field may return null, indicating that no valid values can be obtained.
        :type NumberOfPartitions: int
        :param _DistributeRules: Partition rules. This field is required when NumberOfPartitions > 1.Note: This field may return null, indicating that no valid values can be obtained.
        :type DistributeRules: list of DistributeRule
        :param _DefaultRuleType: Default partitioning policy. If NumberOfPartitions > 1, this field is required. Data that does not meet the regex in DistributeRules will be partitioned according to the default partitioning policy.Valid values for non-mongo products: table (partitioned by table name); pk (partitioned by table name + primary key). Valid values for mongo: collection (partitioned by collection name). This field is used in conjunction with DistributeRules. If this field is configured, it is considered as configuring a DistributeRules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultRuleType: str
        """
        self._NumberOfPartitions = None
        self._DistributeRules = None
        self._DefaultRuleType = None

    @property
    def NumberOfPartitions(self):
        """Number of Kafka partitions. Valid values: 1, 4, 8.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NumberOfPartitions

    @NumberOfPartitions.setter
    def NumberOfPartitions(self, NumberOfPartitions):
        self._NumberOfPartitions = NumberOfPartitions

    @property
    def DistributeRules(self):
        """Partition rules. This field is required when NumberOfPartitions > 1.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DistributeRule
        """
        return self._DistributeRules

    @DistributeRules.setter
    def DistributeRules(self, DistributeRules):
        self._DistributeRules = DistributeRules

    @property
    def DefaultRuleType(self):
        """Default partitioning policy. If NumberOfPartitions > 1, this field is required. Data that does not meet the regex in DistributeRules will be partitioned according to the default partitioning policy.Valid values for non-mongo products: table (partitioned by table name); pk (partitioned by table name + primary key). Valid values for mongo: collection (partitioned by collection name). This field is used in conjunction with DistributeRules. If this field is configured, it is considered as configuring a DistributeRules.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultRuleType

    @DefaultRuleType.setter
    def DefaultRuleType(self, DefaultRuleType):
        self._DefaultRuleType = DefaultRuleType


    def _deserialize(self, params):
        self._NumberOfPartitions = params.get("NumberOfPartitions")
        if params.get("DistributeRules") is not None:
            self._DistributeRules = []
            for item in params.get("DistributeRules"):
                obj = DistributeRule()
                obj._deserialize(item)
                self._DistributeRules.append(obj)
        self._DefaultRuleType = params.get("DefaultRuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeObject(AbstractModel):
    """Subscription database and table information, used to configure and query the subscription task interfaces.

    """

    def __init__(self):
        r"""
        :param _ObjectType: Subscription data type. Valid values: database; table (if DatabaseType is mongodb, it means a collection).Note: This field may return null, indicating that no valid values can be obtained.
        :type ObjectType: str
        :param _Database: Subscribed database name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _Tables: Name of the table in the subscribed database. If DatabaseType is mongodb, fill in the collection name. MongoDB only supports subscribing to a single database or a single collection.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of str
        """
        self._ObjectType = None
        self._Database = None
        self._Tables = None

    @property
    def ObjectType(self):
        """Subscription data type. Valid values: database; table (if DatabaseType is mongodb, it means a collection).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def Database(self):
        """Subscribed database name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Tables(self):
        """Name of the table in the subscribed database. If DatabaseType is mongodb, fill in the collection name. MongoDB only supports subscribing to a single database or a single collection.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables


    def _deserialize(self, params):
        self._ObjectType = params.get("ObjectType")
        self._Database = params.get("Database")
        self._Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDBEndpointInfos(AbstractModel):
    """Node information of multi-node databases configured for data sync. This data structure is valid for multi-node databases such as TDSQL for MySQL. For single-node databases such as MySQL, use `Endpoint` instead.

    """

    def __init__(self):
        r"""
        :param _Region: Region of the database
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AccessType: Instance network access type. Valid values: `extranet` (public network); `ipv6` (public IPv6); `cvm` (self-build on CVM); `dcg` (Direct Connect); `vpncloud` (VPN access); `cdb` (database); `ccn` (CCN); `intranet` (intranet); `vpc` (VPC). Note that the valid values are subject to the current link.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessType: str
        :param _DatabaseType: Database type, such as `mysql`, `redis`, `mongodb`, `postgresql`, `mariadb`, and `percona`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseType: str
        :param _Info: Database information. Note: If the data type is tdsqlmysql, the order of this Endpoint array should correspond to the set order, and the first shard (shardkey range starting from 0) must be entered first.Note: This field may return null, indicating that no valid values can be obtained.
        :type Info: list of Endpoint
        """
        self._Region = None
        self._AccessType = None
        self._DatabaseType = None
        self._Info = None

    @property
    def Region(self):
        """Region of the database
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccessType(self):
        """Instance network access type. Valid values: `extranet` (public network); `ipv6` (public IPv6); `cvm` (self-build on CVM); `dcg` (Direct Connect); `vpncloud` (VPN access); `cdb` (database); `ccn` (CCN); `intranet` (intranet); `vpc` (VPC). Note that the valid values are subject to the current link.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def DatabaseType(self):
        """Database type, such as `mysql`, `redis`, `mongodb`, `postgresql`, `mariadb`, and `percona`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType):
        self._DatabaseType = DatabaseType

    @property
    def Info(self):
        """Database information. Note: If the data type is tdsqlmysql, the order of this Endpoint array should correspond to the set order, and the first shard (shardkey range starting from 0) must be entered first.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Endpoint
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._AccessType = params.get("AccessType")
        self._DatabaseType = params.get("DatabaseType")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = Endpoint()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDetailInfo(AbstractModel):
    """Step information of the sync task

    """

    def __init__(self):
        r"""
        :param _StepAll: Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepAll: int
        :param _StepNow: Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepNow: int
        :param _Progress: Overall progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Progress: int
        :param _CurrentStepProgress: Progress of the current step. Value range: 0-100. The value of `-1` indicates that you can't check the progress of the current step.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentStepProgress: int
        :param _MasterSlaveDistance: Data volume difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterSlaveDistance: int
        :param _SecondsBehindMaster: Time difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecondsBehindMaster: int
        :param _Message: Overall description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _StepInfos: Step details
Note: This field may return null, indicating that no valid values can be obtained.
        :type StepInfos: list of StepInfo
        :param _CauseOfCompareDisable: Cause of the failure of initiating data consistency check
Note: This field may return null, indicating that no valid values can be obtained.
        :type CauseOfCompareDisable: str
        :param _ErrInfo: Task error and the corresponding solution
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrInfo: :class:`tencentcloud.dts.v20211206.models.ErrInfo`
        """
        self._StepAll = None
        self._StepNow = None
        self._Progress = None
        self._CurrentStepProgress = None
        self._MasterSlaveDistance = None
        self._SecondsBehindMaster = None
        self._Message = None
        self._StepInfos = None
        self._CauseOfCompareDisable = None
        self._ErrInfo = None

    @property
    def StepAll(self):
        """Total number of steps
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepAll

    @StepAll.setter
    def StepAll(self, StepAll):
        self._StepAll = StepAll

    @property
    def StepNow(self):
        """Current step
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StepNow

    @StepNow.setter
    def StepNow(self, StepNow):
        self._StepNow = StepNow

    @property
    def Progress(self):
        """Overall progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def CurrentStepProgress(self):
        """Progress of the current step. Value range: 0-100. The value of `-1` indicates that you can't check the progress of the current step.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CurrentStepProgress

    @CurrentStepProgress.setter
    def CurrentStepProgress(self, CurrentStepProgress):
        self._CurrentStepProgress = CurrentStepProgress

    @property
    def MasterSlaveDistance(self):
        """Data volume difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MasterSlaveDistance

    @MasterSlaveDistance.setter
    def MasterSlaveDistance(self, MasterSlaveDistance):
        self._MasterSlaveDistance = MasterSlaveDistance

    @property
    def SecondsBehindMaster(self):
        """Time difference between the sync source and target
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SecondsBehindMaster

    @SecondsBehindMaster.setter
    def SecondsBehindMaster(self, SecondsBehindMaster):
        self._SecondsBehindMaster = SecondsBehindMaster

    @property
    def Message(self):
        """Overall description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def StepInfos(self):
        """Step details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StepInfo
        """
        return self._StepInfos

    @StepInfos.setter
    def StepInfos(self, StepInfos):
        self._StepInfos = StepInfos

    @property
    def CauseOfCompareDisable(self):
        """Cause of the failure of initiating data consistency check
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CauseOfCompareDisable

    @CauseOfCompareDisable.setter
    def CauseOfCompareDisable(self, CauseOfCompareDisable):
        self._CauseOfCompareDisable = CauseOfCompareDisable

    @property
    def ErrInfo(self):
        """Task error and the corresponding solution
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.ErrInfo`
        """
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo


    def _deserialize(self, params):
        self._StepAll = params.get("StepAll")
        self._StepNow = params.get("StepNow")
        self._Progress = params.get("Progress")
        self._CurrentStepProgress = params.get("CurrentStepProgress")
        self._MasterSlaveDistance = params.get("MasterSlaveDistance")
        self._SecondsBehindMaster = params.get("SecondsBehindMaster")
        self._Message = params.get("Message")
        if params.get("StepInfos") is not None:
            self._StepInfos = []
            for item in params.get("StepInfos"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfos.append(obj)
        self._CauseOfCompareDisable = params.get("CauseOfCompareDisable")
        if params.get("ErrInfo") is not None:
            self._ErrInfo = ErrInfo()
            self._ErrInfo._deserialize(params.get("ErrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncJobInfo(AbstractModel):
    """Sync task information

    """

    def __init__(self):
        r"""
        :param _JobId: Sync task ID, such as `sync-btso140`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _JobName: Sync task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param _PayMode: Billing mode. Valid values: `PostPay` (pay-as-you-go); `PrePay` (monthly subscription).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _RunMode: Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunMode: str
        :param _ExpectRunTime: Expected execution time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectRunTime: str
        :param _AllActions: All supported operations
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllActions: list of str
        :param _Actions: Operations that can be performed under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Actions: list of str
        :param _Options: Sync options
Note: This field may return null, indicating that no valid values can be obtained.
        :type Options: :class:`tencentcloud.dts.v20211206.models.Options`
        :param _Objects: Sync database/table objects
Note: This field may return null, indicating that no valid values can be obtained.
        :type Objects: :class:`tencentcloud.dts.v20211206.models.Objects`
        :param _Specification: Task specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type Specification: str
        :param _ExpireTime: Expiration time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _SrcRegion: Source database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcRegion: str
        :param _SrcDatabaseType: Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcDatabaseType: str
        :param _SrcAccessType: Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcAccessType: str
        :param _SrcInfo: Source database information. This parameter is used by single-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _SrcNodeType: Valid values: `cluster`, `single`. `single`: For single-node source databases; `cluster`: For multi-node source databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcNodeType: str
        :param _SrcInfos: Source database information. This parameter is used for multi-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _DstRegion: Target database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstRegion: str
        :param _DstDatabaseType: Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstDatabaseType: str
        :param _DstAccessType: Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstAccessType: str
        :param _DstInfo: Target database information. This parameter is used by single-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        :param _DstNodeType: Valid values: `cluster`, `single`. `single`: For single-node target databases; `cluster`: For multi-node target databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstNodeType: str
        :param _DstInfos: Target database information. This parameter is used for multi-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfos: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        :param _CreateTime: Creation time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _StartTime: Start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _Status: Task status. Valid values: `UnInitialized`, `Initialized`, `Checking`, `CheckPass`, `CheckNotPass`, `ReadyRunning`, `Running`, `Pausing`, `Paused`, `Stopping`, `Stopped`, `ResumableErr`, `Resuming`, `Failed`, `Released`, `Resetting`, `Unknown`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _EndTime: End time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Tags: Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagItem
        :param _Detail: Step information of the sync task
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        :param _TradeStatus: Billing status. Valid values: `Normal`, `Resizing`, `Renewing`, `Isolating`, `Isolated`, `Offlining`, `Offlined`, `NotBilled`, `Recovering`, `PostPay2Prepaying`, `PrePay2Postpaying`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeStatus: str
        :param _InstanceClass: Sync link specification, such as `micro`, `small`, `medium`, and `large`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceClass: str
        :param _AutoRenew: Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRenew: int
        :param _OfflineTime: Deletion time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        :param _AutoRetryTimeRangeMinutes: Settings of automatic retry time
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoRetryTimeRangeMinutes: int
        :param _DumperResumeCtrl: Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DumperResumeCtrl: str
        """
        self._JobId = None
        self._JobName = None
        self._PayMode = None
        self._RunMode = None
        self._ExpectRunTime = None
        self._AllActions = None
        self._Actions = None
        self._Options = None
        self._Objects = None
        self._Specification = None
        self._ExpireTime = None
        self._SrcRegion = None
        self._SrcDatabaseType = None
        self._SrcAccessType = None
        self._SrcInfo = None
        self._SrcNodeType = None
        self._SrcInfos = None
        self._DstRegion = None
        self._DstDatabaseType = None
        self._DstAccessType = None
        self._DstInfo = None
        self._DstNodeType = None
        self._DstInfos = None
        self._CreateTime = None
        self._StartTime = None
        self._Status = None
        self._EndTime = None
        self._Tags = None
        self._Detail = None
        self._TradeStatus = None
        self._InstanceClass = None
        self._AutoRenew = None
        self._OfflineTime = None
        self._AutoRetryTimeRangeMinutes = None
        self._DumperResumeCtrl = None

    @property
    def JobId(self):
        """Sync task ID, such as `sync-btso140`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Sync task name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def PayMode(self):
        """Billing mode. Valid values: `PostPay` (pay-as-you-go); `PrePay` (monthly subscription).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RunMode(self):
        """Running mode. Valid values: `Immediate`, `Timed`. Default value: `Immediate`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ExpectRunTime(self):
        """Expected execution time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpectRunTime

    @ExpectRunTime.setter
    def ExpectRunTime(self, ExpectRunTime):
        self._ExpectRunTime = ExpectRunTime

    @property
    def AllActions(self):
        """All supported operations
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AllActions

    @AllActions.setter
    def AllActions(self, AllActions):
        self._AllActions = AllActions

    @property
    def Actions(self):
        """Operations that can be performed under the current status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Options(self):
        """Sync options
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Options`
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options

    @property
    def Objects(self):
        """Sync database/table objects
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Objects`
        """
        return self._Objects

    @Objects.setter
    def Objects(self, Objects):
        self._Objects = Objects

    @property
    def Specification(self):
        """Task specification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def ExpireTime(self):
        """Expiration time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SrcRegion(self):
        """Source database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def SrcDatabaseType(self):
        """Source database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcDatabaseType

    @SrcDatabaseType.setter
    def SrcDatabaseType(self, SrcDatabaseType):
        self._SrcDatabaseType = SrcDatabaseType

    @property
    def SrcAccessType(self):
        """Source database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcAccessType

    @SrcAccessType.setter
    def SrcAccessType(self, SrcAccessType):
        self._SrcAccessType = SrcAccessType

    @property
    def SrcInfo(self):
        """Source database information. This parameter is used by single-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def SrcNodeType(self):
        """Valid values: `cluster`, `single`. `single`: For single-node source databases; `cluster`: For multi-node source databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SrcNodeType

    @SrcNodeType.setter
    def SrcNodeType(self, SrcNodeType):
        self._SrcNodeType = SrcNodeType

    @property
    def SrcInfos(self):
        """Source database information. This parameter is used for multi-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._SrcInfos

    @SrcInfos.setter
    def SrcInfos(self, SrcInfos):
        self._SrcInfos = SrcInfos

    @property
    def DstRegion(self):
        """Target database region, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DstRegion

    @DstRegion.setter
    def DstRegion(self, DstRegion):
        self._DstRegion = DstRegion

    @property
    def DstDatabaseType(self):
        """Target database type, such as `mysql`, `cynosdbmysql`, `tdapg`, `tdpg`, and `tdsqlmysql`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DstDatabaseType

    @DstDatabaseType.setter
    def DstDatabaseType(self, DstDatabaseType):
        self._DstDatabaseType = DstDatabaseType

    @property
    def DstAccessType(self):
        """Target database access type. Valid values: `cdb` (database); `cvm` (self-build on CVM); `vpc` (VPC); `extranet` (public network); `vpncloud` (VPN access); `dcg` (Direct Connect); `ccn` (CCN); `intranet` (intranet).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DstAccessType

    @DstAccessType.setter
    def DstAccessType(self, DstAccessType):
        self._DstAccessType = DstAccessType

    @property
    def DstInfo(self):
        """Target database information. This parameter is used by single-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.Endpoint`
        """
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def DstNodeType(self):
        """Valid values: `cluster`, `single`. `single`: For single-node target databases; `cluster`: For multi-node target databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DstNodeType

    @DstNodeType.setter
    def DstNodeType(self, DstNodeType):
        self._DstNodeType = DstNodeType

    @property
    def DstInfos(self):
        """Target database information. This parameter is used for multi-node databases.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDBEndpointInfos`
        """
        return self._DstInfos

    @DstInfos.setter
    def DstInfos(self, DstInfos):
        self._DstInfos = DstInfos

    @property
    def CreateTime(self):
        """Creation time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """Start time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        """Task status. Valid values: `UnInitialized`, `Initialized`, `Checking`, `CheckPass`, `CheckNotPass`, `ReadyRunning`, `Running`, `Pausing`, `Paused`, `Stopping`, `Stopped`, `ResumableErr`, `Resuming`, `Failed`, `Released`, `Resetting`, `Unknown`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndTime(self):
        """End time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Tags(self):
        """Tag information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Detail(self):
        """Step information of the sync task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.dts.v20211206.models.SyncDetailInfo`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TradeStatus(self):
        """Billing status. Valid values: `Normal`, `Resizing`, `Renewing`, `Isolating`, `Isolated`, `Offlining`, `Offlined`, `NotBilled`, `Recovering`, `PostPay2Prepaying`, `PrePay2Postpaying`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def InstanceClass(self):
        """Sync link specification, such as `micro`, `small`, `medium`, and `large`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def AutoRenew(self):
        """Auto-renewal flag, which takes effect if `PayMode` is `PrePay`. Valid values: `1` (auto-renewal enabled); `0` (auto-renewal disabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def OfflineTime(self):
        """Deletion time in the format of `yyyy-mm-dd hh:mm:ss`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def AutoRetryTimeRangeMinutes(self):
        """Settings of automatic retry time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoRetryTimeRangeMinutes

    @AutoRetryTimeRangeMinutes.setter
    def AutoRetryTimeRangeMinutes(self, AutoRetryTimeRangeMinutes):
        self._AutoRetryTimeRangeMinutes = AutoRetryTimeRangeMinutes

    @property
    def DumperResumeCtrl(self):
        """Whether the task can be reentered in the full export stage. Valid values: `yes`, `no`. `yes`: The current task can be reentered. `no`: The current task is in the full export stage which cannot be reentered. If the value of this parameter is `no`, the checkpoint restart is not supported when the task is restarted in the export stage.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DumperResumeCtrl

    @DumperResumeCtrl.setter
    def DumperResumeCtrl(self, DumperResumeCtrl):
        self._DumperResumeCtrl = DumperResumeCtrl


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._PayMode = params.get("PayMode")
        self._RunMode = params.get("RunMode")
        self._ExpectRunTime = params.get("ExpectRunTime")
        self._AllActions = params.get("AllActions")
        self._Actions = params.get("Actions")
        if params.get("Options") is not None:
            self._Options = Options()
            self._Options._deserialize(params.get("Options"))
        if params.get("Objects") is not None:
            self._Objects = Objects()
            self._Objects._deserialize(params.get("Objects"))
        self._Specification = params.get("Specification")
        self._ExpireTime = params.get("ExpireTime")
        self._SrcRegion = params.get("SrcRegion")
        self._SrcDatabaseType = params.get("SrcDatabaseType")
        self._SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = Endpoint()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        self._SrcNodeType = params.get("SrcNodeType")
        if params.get("SrcInfos") is not None:
            self._SrcInfos = SyncDBEndpointInfos()
            self._SrcInfos._deserialize(params.get("SrcInfos"))
        self._DstRegion = params.get("DstRegion")
        self._DstDatabaseType = params.get("DstDatabaseType")
        self._DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self._DstInfo = Endpoint()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._DstNodeType = params.get("DstNodeType")
        if params.get("DstInfos") is not None:
            self._DstInfos = SyncDBEndpointInfos()
            self._DstInfos._deserialize(params.get("DstInfos"))
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._EndTime = params.get("EndTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Detail") is not None:
            self._Detail = SyncDetailInfo()
            self._Detail._deserialize(params.get("Detail"))
        self._TradeStatus = params.get("TradeStatus")
        self._InstanceClass = params.get("InstanceClass")
        self._AutoRenew = params.get("AutoRenew")
        self._OfflineTime = params.get("OfflineTime")
        self._AutoRetryTimeRangeMinutes = params.get("AutoRetryTimeRangeMinutes")
        self._DumperResumeCtrl = params.get("DumperResumeCtrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """Synced table description

    """

    def __init__(self):
        r"""
        :param _TableName: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _NewTableName: New table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        :param _FilterCondition: Filter condition
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilterCondition: str
        :param _ColumnMode: Whether to synchronize all columns in the table. All: all columns under the current table; Partial (the corresponding field ColumnMode in ModifySyncJobConfig interface does not support Partial at the moment): some columns under the current table, detailed table information is provided by filling the Columns field.Note: This field may return null, indicating that no valid values can be obtained.
        :type ColumnMode: str
        :param _Columns: Column information in data sync. This field is required when ColumnMode is set to Partial.Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of Column
        :param _TmpTables: The temp tables to be synced. This parameter is mutually exclusive with `NewTableName`. It is valid only when the configured sync objects are table-level ones and `TableEditMode` is `pt`. To sync temp tables generated when pt-osc or other tools are used during the sync process, you must configure this parameter first. For example, if you want to perform the pt-osc operation on a table named "t1", configure this parameter as ["\_t1\_new","\_t1\_old"]; to perform the gh-ost operation on t1, configure it as ["\_t1\_ghc","\_t1\_gho","\_t1\_del"]. Temp tables generated by pt-osc and gh-ost operations can be configured at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpTables: list of str
        :param _TableEditMode: Table editing type. Valid values: `rename` (table mapping); `pt` (additional table sync).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._FilterCondition = None
        self._ColumnMode = None
        self._Columns = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        """Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        """New table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def FilterCondition(self):
        """Filter condition
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FilterCondition

    @FilterCondition.setter
    def FilterCondition(self, FilterCondition):
        self._FilterCondition = FilterCondition

    @property
    def ColumnMode(self):
        """Whether to synchronize all columns in the table. All: all columns under the current table; Partial (the corresponding field ColumnMode in ModifySyncJobConfig interface does not support Partial at the moment): some columns under the current table, detailed table information is provided by filling the Columns field.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ColumnMode

    @ColumnMode.setter
    def ColumnMode(self, ColumnMode):
        self._ColumnMode = ColumnMode

    @property
    def Columns(self):
        """Column information in data sync. This field is required when ColumnMode is set to Partial.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def TmpTables(self):
        """The temp tables to be synced. This parameter is mutually exclusive with `NewTableName`. It is valid only when the configured sync objects are table-level ones and `TableEditMode` is `pt`. To sync temp tables generated when pt-osc or other tools are used during the sync process, you must configure this parameter first. For example, if you want to perform the pt-osc operation on a table named "t1", configure this parameter as ["\_t1\_new","\_t1\_old"]; to perform the gh-ost operation on t1, configure it as ["\_t1\_ghc","\_t1\_gho","\_t1\_del"]. Temp tables generated by pt-osc and gh-ost operations can be configured at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        """Table editing type. Valid values: `rename` (table mapping); `pt` (additional table sync).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableEditMode

    @TableEditMode.setter
    def TableEditMode(self, TableEditMode):
        self._TableEditMode = TableEditMode


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        self._FilterCondition = params.get("FilterCondition")
        self._ColumnMode = params.get("ColumnMode")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._TmpTables = params.get("TmpTables")
        self._TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableItem(AbstractModel):
    """The set of table objects, which is required if `TableMode` is `partial`.

    """

    def __init__(self):
        r"""
        :param _TableName: Name of the migrated table, which is case-sensitive
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableName: str
        :param _NewTableName: New name of the migrated table. This parameter is required when `TableEditMode` is `rename`. It is mutually exclusive with `TmpTables`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewTableName: str
        :param _TmpTables: The temp tables to be migrated. This parameter is mutually exclusive with `NewTableName`. It is valid only when the configured migration objects are table-level ones and `TableEditMode` is `pt`. To migrate temp tables generated when pt-osc or other tools are used during the migration process, you must configure this parameter first. For example, if you want to perform the pt-osc operation on a table named "t1", configure this parameter as ["_t1_new","_t1_old"]; to perform the gh-ost operation on t1, configure it as ["_t1_ghc","_t1_gho","_t1_del"]. Temp tables generated by pt-osc and gh-ost operations can be configured at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TmpTables: list of str
        :param _TableEditMode: Table editing type. Valid values: `rename` (table mapping); `pt` (additional table sync).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableEditMode: str
        """
        self._TableName = None
        self._NewTableName = None
        self._TmpTables = None
        self._TableEditMode = None

    @property
    def TableName(self):
        """Name of the migrated table, which is case-sensitive
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def NewTableName(self):
        """New name of the migrated table. This parameter is required when `TableEditMode` is `rename`. It is mutually exclusive with `TmpTables`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewTableName

    @NewTableName.setter
    def NewTableName(self, NewTableName):
        self._NewTableName = NewTableName

    @property
    def TmpTables(self):
        """The temp tables to be migrated. This parameter is mutually exclusive with `NewTableName`. It is valid only when the configured migration objects are table-level ones and `TableEditMode` is `pt`. To migrate temp tables generated when pt-osc or other tools are used during the migration process, you must configure this parameter first. For example, if you want to perform the pt-osc operation on a table named "t1", configure this parameter as ["_t1_new","_t1_old"]; to perform the gh-ost operation on t1, configure it as ["_t1_ghc","_t1_gho","_t1_del"]. Temp tables generated by pt-osc and gh-ost operations can be configured at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TmpTables

    @TmpTables.setter
    def TmpTables(self, TmpTables):
        self._TmpTables = TmpTables

    @property
    def TableEditMode(self):
        """Table editing type. Valid values: `rename` (table mapping); `pt` (additional table sync).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableEditMode

    @TableEditMode.setter
    def TableEditMode(self, TableEditMode):
        self._TableEditMode = TableEditMode


    def _deserialize(self, params):
        self._TableName = params.get("TableName")
        self._NewTableName = params.get("NewTableName")
        self._TmpTables = params.get("TmpTables")
        self._TableEditMode = params.get("TableEditMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag filter

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
        :rtype: list of str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRule(AbstractModel):
    """Topic description

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _PartitionType: Topic partitioning policy. If the topic sync policy is delivering data to multiple custom topics (`TopicType` = `Multi`), the value of this parameter is `Random` (deliver to a random partition). If the topic sync policy is delivering all data to a single topic (`TopicType` = `Single`), this parameter has three valid values: `AllInPartitionZero` (deliver all data to partition0), `PartitionByTable` (partition by table name), `PartitionByTableAndKey` (partition by table name and primary key).
        :type PartitionType: str
        :param _DbMatchMode: Database name matching rule. This parameter takes effect only when `TopicType` is `Multi`. Valid values: `Regular` (match by regex), `Default` (default rule for the remaining databases that cannot be matched by regex). The default rule must be included in the array of matching rules.
        :type DbMatchMode: str
        :param _DbName: Database name, which can only be matched by regex when `TopicType` is `Multi` and `DbMatchMode` is `Regular`.
        :type DbName: str
        :param _TableMatchMode: Table name matching rule. This parameter takes effect only when `TopicType` is `Multi`. Valid values: `Regular` (match by regex), `Default` (default rule for the remaining databases that cannot be matched by regex). The default rule must be included in the array of matching rules.
        :type TableMatchMode: str
        :param _TableName: Table name, which can only be matched by regex when `TopicType` is `Multi` and `DbMatchMode` is `Regular`.
        :type TableName: str
        """
        self._TopicName = None
        self._PartitionType = None
        self._DbMatchMode = None
        self._DbName = None
        self._TableMatchMode = None
        self._TableName = None

    @property
    def TopicName(self):
        """Topic name
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PartitionType(self):
        """Topic partitioning policy. If the topic sync policy is delivering data to multiple custom topics (`TopicType` = `Multi`), the value of this parameter is `Random` (deliver to a random partition). If the topic sync policy is delivering all data to a single topic (`TopicType` = `Single`), this parameter has three valid values: `AllInPartitionZero` (deliver all data to partition0), `PartitionByTable` (partition by table name), `PartitionByTableAndKey` (partition by table name and primary key).
        :rtype: str
        """
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def DbMatchMode(self):
        """Database name matching rule. This parameter takes effect only when `TopicType` is `Multi`. Valid values: `Regular` (match by regex), `Default` (default rule for the remaining databases that cannot be matched by regex). The default rule must be included in the array of matching rules.
        :rtype: str
        """
        return self._DbMatchMode

    @DbMatchMode.setter
    def DbMatchMode(self, DbMatchMode):
        self._DbMatchMode = DbMatchMode

    @property
    def DbName(self):
        """Database name, which can only be matched by regex when `TopicType` is `Multi` and `DbMatchMode` is `Regular`.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def TableMatchMode(self):
        """Table name matching rule. This parameter takes effect only when `TopicType` is `Multi`. Valid values: `Regular` (match by regex), `Default` (default rule for the remaining databases that cannot be matched by regex). The default rule must be included in the array of matching rules.
        :rtype: str
        """
        return self._TableMatchMode

    @TableMatchMode.setter
    def TableMatchMode(self, TableMatchMode):
        self._TableMatchMode = TableMatchMode

    @property
    def TableName(self):
        """Table name, which can only be matched by regex when `TopicType` is `Multi` and `DbMatchMode` is `Regular`.
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PartitionType = params.get("PartitionType")
        self._DbMatchMode = params.get("DbMatchMode")
        self._DbName = params.get("DbName")
        self._TableMatchMode = params.get("TableMatchMode")
        self._TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeInfo(AbstractModel):
    """Billing status information

    """

    def __init__(self):
        r"""
        :param _DealName: Order number
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param _LastDealName: Last order number
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastDealName: str
        :param _InstanceClass: Instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceClass: str
        :param _TradeStatus: Task billing status. Valid values: `normal` (billed or to be billed); `resizing` (adjusting configuration); `reversing` (topping up, which is a short status); `isolating` (isolating, which is a short status); `isolated` (isolated); `offlining` (deleting); `offlined` (deleted); `notBilled` (not billed).
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeStatus: str
        :param _ExpireTime: Expiration time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _OfflineTime: Deletion time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineTime: str
        :param _IsolateTime: Isolation time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateTime: str
        :param _OfflineReason: The cause of deletion
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineReason: str
        :param _IsolateReason: The cause of isolation
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateReason: str
        :param _PayType: Billing mode. Valid values: `postpay` (postpaid); `prepay` (prepaid).
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayType: str
        :param _BillingType: Task billing type. Valid values: `billing` (billed); `notBilling` (free); `promotions` (in promotion).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingType: str
        """
        self._DealName = None
        self._LastDealName = None
        self._InstanceClass = None
        self._TradeStatus = None
        self._ExpireTime = None
        self._OfflineTime = None
        self._IsolateTime = None
        self._OfflineReason = None
        self._IsolateReason = None
        self._PayType = None
        self._BillingType = None

    @property
    def DealName(self):
        """Order number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def LastDealName(self):
        """Last order number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastDealName

    @LastDealName.setter
    def LastDealName(self, LastDealName):
        self._LastDealName = LastDealName

    @property
    def InstanceClass(self):
        """Instance specification. Valid values: `micro`, `small`, `medium`, `large`, `xlarge`, `2xlarge`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceClass

    @InstanceClass.setter
    def InstanceClass(self, InstanceClass):
        self._InstanceClass = InstanceClass

    @property
    def TradeStatus(self):
        """Task billing status. Valid values: `normal` (billed or to be billed); `resizing` (adjusting configuration); `reversing` (topping up, which is a short status); `isolating` (isolating, which is a short status); `isolated` (isolated); `offlining` (deleting); `offlined` (deleted); `notBilled` (not billed).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TradeStatus

    @TradeStatus.setter
    def TradeStatus(self, TradeStatus):
        self._TradeStatus = TradeStatus

    @property
    def ExpireTime(self):
        """Expiration time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OfflineTime(self):
        """Deletion time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def IsolateTime(self):
        """Isolation time in the format of "yyyy-mm-dd hh:mm:ss"
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def OfflineReason(self):
        """The cause of deletion
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OfflineReason

    @OfflineReason.setter
    def OfflineReason(self, OfflineReason):
        self._OfflineReason = OfflineReason

    @property
    def IsolateReason(self):
        """The cause of isolation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolateReason

    @IsolateReason.setter
    def IsolateReason(self, IsolateReason):
        self._IsolateReason = IsolateReason

    @property
    def PayType(self):
        """Billing mode. Valid values: `postpay` (postpaid); `prepay` (prepaid).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BillingType(self):
        """Task billing type. Valid values: `billing` (billed); `notBilling` (free); `promotions` (in promotion).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._LastDealName = params.get("LastDealName")
        self._InstanceClass = params.get("InstanceClass")
        self._TradeStatus = params.get("TradeStatus")
        self._ExpireTime = params.get("ExpireTime")
        self._OfflineTime = params.get("OfflineTime")
        self._IsolateTime = params.get("IsolateTime")
        self._OfflineReason = params.get("OfflineReason")
        self._IsolateReason = params.get("IsolateReason")
        self._PayType = params.get("PayType")
        self._BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class View(AbstractModel):
    """Synced view description

    """

    def __init__(self):
        r"""
        :param _ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        :param _NewViewName: Reserved field. Currently, a view cannot be renamed. Note: This field may return null, indicating that no valid values can be obtained.
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        """View name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        """Reserved field. Currently, a view cannot be renamed. Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewViewName

    @NewViewName.setter
    def NewViewName(self, NewViewName):
        self._NewViewName = NewViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        self._NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewItem(AbstractModel):
    """View object

    """

    def __init__(self):
        r"""
        :param _ViewName: View name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ViewName: str
        :param _NewViewName: View name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NewViewName: str
        """
        self._ViewName = None
        self._NewViewName = None

    @property
    def ViewName(self):
        """View name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def NewViewName(self):
        """View name after migration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NewViewName

    @NewViewName.setter
    def NewViewName(self, NewViewName):
        self._NewViewName = NewViewName


    def _deserialize(self, params):
        self._ViewName = params.get("ViewName")
        self._NewViewName = params.get("NewViewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        