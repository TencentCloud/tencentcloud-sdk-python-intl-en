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


class AnalysisInstanceInfo(AbstractModel):
    r"""Analytics engine instance info

    """

    def __init__(self):
        r"""
        :param _ReplicasNum: <p>Number of replicas</p>
        :type ReplicasNum: int
        """
        self._ReplicasNum = None

    @property
    def ReplicasNum(self):
        r"""<p>Number of replicas</p>
        :rtype: int
        """
        return self._ReplicasNum

    @ReplicasNum.setter
    def ReplicasNum(self, ReplicasNum):
        self._ReplicasNum = ReplicasNum


    def _deserialize(self, params):
        self._ReplicasNum = params.get("ReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisRelationInfo(AbstractModel):
    r"""Analytics engine association

    """

    def __init__(self):
        r"""
        :param _PrimaryInstanceId: <p>Source instance Id</p>
        :type PrimaryInstanceId: str
        :param _AnalysisInstanceId: <p>Analysis engine instance Id</p>
        :type AnalysisInstanceId: str
        :param _Status: <p>Analysis engine relationship status</p><p>Enumeration values:</p><ul><li>creating: Creating</li><li>running: Running</li><li>destroyed: Terminated</li></ul>
        :type Status: str
        :param _CreateAt: <p>Creation time.</p>
        :type CreateAt: str
        :param _UpdateAt: <p>Update time.</p>
        :type UpdateAt: str
        """
        self._PrimaryInstanceId = None
        self._AnalysisInstanceId = None
        self._Status = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PrimaryInstanceId(self):
        r"""<p>Source instance Id</p>
        :rtype: str
        """
        return self._PrimaryInstanceId

    @PrimaryInstanceId.setter
    def PrimaryInstanceId(self, PrimaryInstanceId):
        self._PrimaryInstanceId = PrimaryInstanceId

    @property
    def AnalysisInstanceId(self):
        r"""<p>Analysis engine instance Id</p>
        :rtype: str
        """
        return self._AnalysisInstanceId

    @AnalysisInstanceId.setter
    def AnalysisInstanceId(self, AnalysisInstanceId):
        self._AnalysisInstanceId = AnalysisInstanceId

    @property
    def Status(self):
        r"""<p>Analysis engine relationship status</p><p>Enumeration values:</p><ul><li>creating: Creating</li><li>running: Running</li><li>destroyed: Terminated</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PrimaryInstanceId = params.get("PrimaryInstanceId")
        self._AnalysisInstanceId = params.get("AnalysisInstanceId")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveLogInterval(AbstractModel):
    r"""Recoverable time interval

    """

    def __init__(self):
        r"""
        :param _EndTime: End time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _MajorVersion: Major version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MajorVersion: str
        :param _MinorVersion: Minor version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinorVersion: str
        :param _StartTime: Start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        """
        self._EndTime = None
        self._MajorVersion = None
        self._MinorVersion = None
        self._StartTime = None

    @property
    def EndTime(self):
        r"""End time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MajorVersion(self):
        r"""Major version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MajorVersion

    @MajorVersion.setter
    def MajorVersion(self, MajorVersion):
        self._MajorVersion = MajorVersion

    @property
    def MinorVersion(self):
        r"""Minor version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MinorVersion

    @MinorVersion.setter
    def MinorVersion(self, MinorVersion):
        self._MinorVersion = MinorVersion

    @property
    def StartTime(self):
        r"""Start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._MajorVersion = params.get("MajorVersion")
        self._MinorVersion = params.get("MinorVersion")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveLogModel(AbstractModel):
    r"""Archive log object

    """

    def __init__(self):
        r"""
        :param _ArchiveLogId: Archivelog ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ArchiveLogId: int
        :param _BackupDuration: Backup duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupDuration: int
        :param _BackupStatus: Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: str
        :param _EndTime: Backup end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _ErrorMessage: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _ExpiredTime: Expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _FileName: Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileName: str
        :param _FileSize: Backup set file size in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileSize: int
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _StartTime: Backup start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        """
        self._ArchiveLogId = None
        self._BackupDuration = None
        self._BackupStatus = None
        self._EndTime = None
        self._ErrorMessage = None
        self._ExpiredTime = None
        self._FileName = None
        self._FileSize = None
        self._InstanceId = None
        self._StartTime = None

    @property
    def ArchiveLogId(self):
        r"""Archivelog ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ArchiveLogId

    @ArchiveLogId.setter
    def ArchiveLogId(self, ArchiveLogId):
        self._ArchiveLogId = ArchiveLogId

    @property
    def BackupDuration(self):
        r"""Backup duration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupDuration

    @BackupDuration.setter
    def BackupDuration(self, BackupDuration):
        self._BackupDuration = BackupDuration

    @property
    def BackupStatus(self):
        r"""Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def EndTime(self):
        r"""Backup end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ErrorMessage(self):
        r"""Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ExpiredTime(self):
        r"""Expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FileName(self):
        r"""Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""Backup set file size in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def InstanceId(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Backup start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._ArchiveLogId = params.get("ArchiveLogId")
        self._BackupDuration = params.get("BackupDuration")
        self._BackupStatus = params.get("BackupStatus")
        self._EndTime = params.get("EndTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingConfig(AbstractModel):
    r"""ccu range of a serverless instance

    """

    def __init__(self):
        r"""
        :param _RangeMin: <p>Minimum value of ccu</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RangeMin: float
        :param _RangeMax: <p>Maximum value of ccu</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RangeMax: float
        """
        self._RangeMin = None
        self._RangeMax = None

    @property
    def RangeMin(self):
        r"""<p>Minimum value of ccu</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RangeMin

    @RangeMin.setter
    def RangeMin(self, RangeMin):
        self._RangeMin = RangeMin

    @property
    def RangeMax(self):
        r"""<p>Maximum value of ccu</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RangeMax

    @RangeMax.setter
    def RangeMax(self, RangeMax):
        self._RangeMax = RangeMax


    def _deserialize(self, params):
        self._RangeMin = params.get("RangeMin")
        self._RangeMax = params.get("RangeMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupMethodStatisticsModel(AbstractModel):
    r"""Backup method statistical object - provided to backup space statistics API

    """

    def __init__(self):
        r"""
        :param _AutoBackupSize: <p>Auto-backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoBackupSize: int
        :param _AverageSizePerDay: <p>Average size of total backup per day in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerDay: int
        :param _ManualBackupSize: <p>Manual backup size, unit Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackupSize: int
        :param _TotalSize: <p>Total backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._AutoBackupSize = None
        self._AverageSizePerDay = None
        self._ManualBackupSize = None
        self._TotalSize = None

    @property
    def AutoBackupSize(self):
        r"""<p>Auto-backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def AverageSizePerDay(self):
        r"""<p>Average size of total backup per day in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def ManualBackupSize(self):
        r"""<p>Manual backup size, unit Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize

    @property
    def TotalSize(self):
        r"""<p>Total backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._ManualBackupSize = params.get("ManualBackupSize")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupMethodStatisticsOutPut(AbstractModel):
    r"""Backup method statistical object, provided to backup set statistical detail API

    """

    def __init__(self):
        r"""
        :param _AutoBackupSize: <p>Auto-backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoBackupSize: list of int
        :param _ManualBackupSize: <p>Manual backup size, unit Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackupSize: list of int
        """
        self._AutoBackupSize = None
        self._ManualBackupSize = None

    @property
    def AutoBackupSize(self):
        r"""<p>Auto-backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def ManualBackupSize(self):
        r"""<p>Manual backup size, unit Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize


    def _deserialize(self, params):
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._ManualBackupSize = params.get("ManualBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPolicyModelInput(AbstractModel):
    r"""Modify backup policy object.

    """

    def __init__(self):
        r"""
        :param _BackupEndTime: <P>Backup end time.</p>
        :type BackupEndTime: str
        :param _BackupMethod: <P>Backup method: physical physical backup, snapshot snapshot backup</p>
        :type BackupMethod: str
        :param _BackupStartTime: <P>Backup start time</p>
        :type BackupStartTime: str
        :param _EnableFull: <P>Whether full backup is enabled</p>
        :type EnableFull: int
        :param _EnableLog: <P>Whether to enable log backup</p>
        :type EnableLog: int
        :param _FullRetentionPeriod: <P>Full backup retention time can currently only be set to 7 days.</p>
        :type FullRetentionPeriod: int
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _LogRetentionPeriod: <P>Log retention days. currently, can only set retention to 7 days.</p>
        :type LogRetentionPeriod: int
        :param _PeriodTime: <P>Days of the week to perform backup.</p>
        :type PeriodTime: str
        :param _StorageType: <p>Storage type: COS, SNAPSHOT</p>valid values: <ul><li> COS: COS storage</li><li> SNAPSHOT: cloud disk SNAPSHOT</li></ul>
        :type StorageType: str
        """
        self._BackupEndTime = None
        self._BackupMethod = None
        self._BackupStartTime = None
        self._EnableFull = None
        self._EnableLog = None
        self._FullRetentionPeriod = None
        self._InstanceId = None
        self._LogRetentionPeriod = None
        self._PeriodTime = None
        self._StorageType = None

    @property
    def BackupEndTime(self):
        r"""<P>Backup end time.</p>
        :rtype: str
        """
        return self._BackupEndTime

    @BackupEndTime.setter
    def BackupEndTime(self, BackupEndTime):
        self._BackupEndTime = BackupEndTime

    @property
    def BackupMethod(self):
        r"""<P>Backup method: physical physical backup, snapshot snapshot backup</p>
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStartTime(self):
        r"""<P>Backup start time</p>
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def EnableFull(self):
        r"""<P>Whether full backup is enabled</p>
        :rtype: int
        """
        return self._EnableFull

    @EnableFull.setter
    def EnableFull(self, EnableFull):
        self._EnableFull = EnableFull

    @property
    def EnableLog(self):
        r"""<P>Whether to enable log backup</p>
        :rtype: int
        """
        return self._EnableLog

    @EnableLog.setter
    def EnableLog(self, EnableLog):
        self._EnableLog = EnableLog

    @property
    def FullRetentionPeriod(self):
        r"""<P>Full backup retention time can currently only be set to 7 days.</p>
        :rtype: int
        """
        return self._FullRetentionPeriod

    @FullRetentionPeriod.setter
    def FullRetentionPeriod(self, FullRetentionPeriod):
        self._FullRetentionPeriod = FullRetentionPeriod

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogRetentionPeriod(self):
        r"""<P>Log retention days. currently, can only set retention to 7 days.</p>
        :rtype: int
        """
        return self._LogRetentionPeriod

    @LogRetentionPeriod.setter
    def LogRetentionPeriod(self, LogRetentionPeriod):
        self._LogRetentionPeriod = LogRetentionPeriod

    @property
    def PeriodTime(self):
        r"""<P>Days of the week to perform backup.</p>
        :rtype: str
        """
        return self._PeriodTime

    @PeriodTime.setter
    def PeriodTime(self, PeriodTime):
        self._PeriodTime = PeriodTime

    @property
    def StorageType(self):
        r"""<p>Storage type: COS, SNAPSHOT</p>valid values: <ul><li> COS: COS storage</li><li> SNAPSHOT: cloud disk SNAPSHOT</li></ul>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._BackupEndTime = params.get("BackupEndTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStartTime = params.get("BackupStartTime")
        self._EnableFull = params.get("EnableFull")
        self._EnableLog = params.get("EnableLog")
        self._FullRetentionPeriod = params.get("FullRetentionPeriod")
        self._InstanceId = params.get("InstanceId")
        self._LogRetentionPeriod = params.get("LogRetentionPeriod")
        self._PeriodTime = params.get("PeriodTime")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupPolicyModelOutPut(AbstractModel):
    r"""Backup policy object

    """

    def __init__(self):
        r"""
        :param _BackupEndTime: <p>Backup end time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupEndTime: str
        :param _BackupMethod: <p>Backup method</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupMethod: str
        :param _BackupStartTime: <p>Backup start time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStartTime: str
        :param _DBType: <p>Engine type</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBType: str
        :param _DBVersion: <p>Engine version</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBVersion: str
        :param _EnableFull: <p>Whether full backup is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableFull: int
        :param _EnableLog: <p>Whether to enable log backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableLog: int
        :param _ExpectedNextBackupPeriod: <p>Expected next backup time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectedNextBackupPeriod: str
        :param _FullRetentionPeriod: <p>Full backup retention time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullRetentionPeriod: int
        :param _ID: <p>Policy ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: <p>Instance ID.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _LogRetentionPeriod: <p>Log retention days</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogRetentionPeriod: int
        :param _PeriodTime: <p>Days of the week to perform backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeriodTime: str
        :param _Region: <p>Region</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _PeriodType: <p>Backup cycle type 0:Weekly</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeriodType: int
        """
        self._BackupEndTime = None
        self._BackupMethod = None
        self._BackupStartTime = None
        self._DBType = None
        self._DBVersion = None
        self._EnableFull = None
        self._EnableLog = None
        self._ExpectedNextBackupPeriod = None
        self._FullRetentionPeriod = None
        self._ID = None
        self._InstanceId = None
        self._LogRetentionPeriod = None
        self._PeriodTime = None
        self._Region = None
        self._PeriodType = None

    @property
    def BackupEndTime(self):
        r"""<p>Backup end time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupEndTime

    @BackupEndTime.setter
    def BackupEndTime(self, BackupEndTime):
        self._BackupEndTime = BackupEndTime

    @property
    def BackupMethod(self):
        r"""<p>Backup method</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStartTime(self):
        r"""<p>Backup start time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupStartTime

    @BackupStartTime.setter
    def BackupStartTime(self, BackupStartTime):
        self._BackupStartTime = BackupStartTime

    @property
    def DBType(self):
        r"""<p>Engine type</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

    @property
    def DBVersion(self):
        r"""<p>Engine version</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def EnableFull(self):
        r"""<p>Whether full backup is enabled</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableFull

    @EnableFull.setter
    def EnableFull(self, EnableFull):
        self._EnableFull = EnableFull

    @property
    def EnableLog(self):
        r"""<p>Whether to enable log backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnableLog

    @EnableLog.setter
    def EnableLog(self, EnableLog):
        self._EnableLog = EnableLog

    @property
    def ExpectedNextBackupPeriod(self):
        r"""<p>Expected next backup time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpectedNextBackupPeriod

    @ExpectedNextBackupPeriod.setter
    def ExpectedNextBackupPeriod(self, ExpectedNextBackupPeriod):
        self._ExpectedNextBackupPeriod = ExpectedNextBackupPeriod

    @property
    def FullRetentionPeriod(self):
        r"""<p>Full backup retention time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FullRetentionPeriod

    @FullRetentionPeriod.setter
    def FullRetentionPeriod(self, FullRetentionPeriod):
        self._FullRetentionPeriod = FullRetentionPeriod

    @property
    def ID(self):
        r"""<p>Policy ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogRetentionPeriod(self):
        r"""<p>Log retention days</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LogRetentionPeriod

    @LogRetentionPeriod.setter
    def LogRetentionPeriod(self, LogRetentionPeriod):
        self._LogRetentionPeriod = LogRetentionPeriod

    @property
    def PeriodTime(self):
        r"""<p>Days of the week to perform backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeriodTime

    @PeriodTime.setter
    def PeriodTime(self, PeriodTime):
        self._PeriodTime = PeriodTime

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
    def PeriodType(self):
        r"""<p>Backup cycle type 0:Weekly</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PeriodType

    @PeriodType.setter
    def PeriodType(self, PeriodType):
        self._PeriodType = PeriodType


    def _deserialize(self, params):
        self._BackupEndTime = params.get("BackupEndTime")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStartTime = params.get("BackupStartTime")
        self._DBType = params.get("DBType")
        self._DBVersion = params.get("DBVersion")
        self._EnableFull = params.get("EnableFull")
        self._EnableLog = params.get("EnableLog")
        self._ExpectedNextBackupPeriod = params.get("ExpectedNextBackupPeriod")
        self._FullRetentionPeriod = params.get("FullRetentionPeriod")
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._LogRetentionPeriod = params.get("LogRetentionPeriod")
        self._PeriodTime = params.get("PeriodTime")
        self._Region = params.get("Region")
        self._PeriodType = params.get("PeriodType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSetModel(AbstractModel):
    r"""Backup set object

    """

    def __init__(self):
        r"""
        :param _BackupDuration: Backup set duration, unit sec
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupDuration: int
        :param _BackupMethod: Backup method
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupMethod: str
        :param _BackupName: Backup note name
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupName: str
        :param _BackupProgress: Backup set progress percentage
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupProgress: float
        :param _BackupSetId: Backup set ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupSetId: int
        :param _BackupStatus: Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: str
        :param _BackupType: Backup set type
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupType: str
        :param _DBVersion: Instance version number
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBVersion: str
        :param _EndTime: Backup end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _EndTrxTime: Transaction commit end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTrxTime: str
        :param _ErrorMessage: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _ExpiredTime: Backup expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _FileName: Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileName: str
        :param _FileSize: Backup set file size in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileSize: int
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _ManualBackup: Backup trigger. 0: autobackup; 1: manual.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackup: int
        :param _StartTime: Backup start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        """
        self._BackupDuration = None
        self._BackupMethod = None
        self._BackupName = None
        self._BackupProgress = None
        self._BackupSetId = None
        self._BackupStatus = None
        self._BackupType = None
        self._DBVersion = None
        self._EndTime = None
        self._EndTrxTime = None
        self._ErrorMessage = None
        self._ExpiredTime = None
        self._FileName = None
        self._FileSize = None
        self._InstanceId = None
        self._ManualBackup = None
        self._StartTime = None

    @property
    def BackupDuration(self):
        r"""Backup set duration, unit sec
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupDuration

    @BackupDuration.setter
    def BackupDuration(self, BackupDuration):
        self._BackupDuration = BackupDuration

    @property
    def BackupMethod(self):
        r"""Backup method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupName(self):
        r"""Backup note name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupProgress(self):
        r"""Backup set progress percentage
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._BackupProgress

    @BackupProgress.setter
    def BackupProgress(self, BackupProgress):
        self._BackupProgress = BackupProgress

    @property
    def BackupSetId(self):
        r"""Backup set ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def BackupStatus(self):
        r"""Backup status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupType(self):
        r"""Backup set type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def DBVersion(self):
        r"""Instance version number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def EndTime(self):
        r"""Backup end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EndTrxTime(self):
        r"""Transaction commit end time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTrxTime

    @EndTrxTime.setter
    def EndTrxTime(self, EndTrxTime):
        self._EndTrxTime = EndTrxTime

    @property
    def ErrorMessage(self):
        r"""Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ExpiredTime(self):
        r"""Backup expiration time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FileName(self):
        r"""Backup file name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""Backup set file size in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def InstanceId(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ManualBackup(self):
        r"""Backup trigger. 0: autobackup; 1: manual.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup

    @property
    def StartTime(self):
        r"""Backup start time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._BackupDuration = params.get("BackupDuration")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupName = params.get("BackupName")
        self._BackupProgress = params.get("BackupProgress")
        self._BackupSetId = params.get("BackupSetId")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupType = params.get("BackupType")
        self._DBVersion = params.get("DBVersion")
        self._EndTime = params.get("EndTime")
        self._EndTrxTime = params.get("EndTrxTime")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._InstanceId = params.get("InstanceId")
        self._ManualBackup = params.get("ManualBackup")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSetsReqFilter(AbstractModel):
    r"""filter for backup set queries

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>Backup method, multiple values separated by commas</p><p>Enumeration value:</p><ul><li>physical: Physical backup</li><li>snapshot: Snapshot backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupMethod: str
        :param _BackupStatus: <p>Backup status, multiple values separated by commas. Description of meaning: pending scheduling pending, running running, success success, failed failed</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: str
        :param _BackupType: <p>Backup type, multiple values separated by commas. Description of meaning: full backup full</p><p>Enumeration value:</p><ul><li>full: Full backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupType: str
        :param _ManualBackup: <p>Backup trigger mode</p><p>Enumeration value:</p><ul><li>0: Auto-backup</li><li>1: Manual backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackup: str
        """
        self._BackupMethod = None
        self._BackupStatus = None
        self._BackupType = None
        self._ManualBackup = None

    @property
    def BackupMethod(self):
        r"""<p>Backup method, multiple values separated by commas</p><p>Enumeration value:</p><ul><li>physical: Physical backup</li><li>snapshot: Snapshot backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupStatus(self):
        r"""<p>Backup status, multiple values separated by commas. Description of meaning: pending scheduling pending, running running, success success, failed failed</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def BackupType(self):
        r"""<p>Backup type, multiple values separated by commas. Description of meaning: full backup full</p><p>Enumeration value:</p><ul><li>full: Full backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def ManualBackup(self):
        r"""<p>Backup trigger mode</p><p>Enumeration value:</p><ul><li>0: Auto-backup</li><li>1: Manual backup</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ManualBackup

    @ManualBackup.setter
    def ManualBackup(self, ManualBackup):
        self._ManualBackup = ManualBackup


    def _deserialize(self, params):
        self._BackupMethod = params.get("BackupMethod")
        self._BackupStatus = params.get("BackupStatus")
        self._BackupType = params.get("BackupType")
        self._ManualBackup = params.get("ManualBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStatisticsModel(AbstractModel):
    r"""Backup statistics object

    """

    def __init__(self):
        r"""
        :param _AverageSizePerDay: <p>Average size of total backup per day in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerDay: int
        :param _DataBackupSize: <p>Backup size of data, in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataBackupSize: int
        :param _LogBackupSize: <p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogBackupSize: int
        :param _TotalCount: <p>Total backup count</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _TotalSize: <p>Total backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._AverageSizePerDay = None
        self._DataBackupSize = None
        self._LogBackupSize = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AverageSizePerDay(self):
        r"""<p>Average size of total backup per day in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def DataBackupSize(self):
        r"""<p>Backup size of data, in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataBackupSize

    @DataBackupSize.setter
    def DataBackupSize(self, DataBackupSize):
        self._DataBackupSize = DataBackupSize

    @property
    def LogBackupSize(self):
        r"""<p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize

    @property
    def TotalCount(self):
        r"""<p>Total backup count</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""<p>Total backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._DataBackupSize = params.get("DataBackupSize")
        self._LogBackupSize = params.get("LogBackupSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTypeStatisticsModel(AbstractModel):
    r"""Backup method statistical object, provided to backup set statistical detail API

    """

    def __init__(self):
        r"""
        :param _DataBackupSize: <p>Backup size of data, in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataBackupSize: list of int
        :param _LogBackupSize: <p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogBackupSize: list of int
        """
        self._DataBackupSize = None
        self._LogBackupSize = None

    @property
    def DataBackupSize(self):
        r"""<p>Backup size of data, in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._DataBackupSize

    @DataBackupSize.setter
    def DataBackupSize(self, DataBackupSize):
        self._DataBackupSize = DataBackupSize

    @property
    def LogBackupSize(self):
        r"""<p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._LogBackupSize

    @LogBackupSize.setter
    def LogBackupSize(self, LogBackupSize):
        self._LogBackupSize = LogBackupSize


    def _deserialize(self, params):
        self._DataBackupSize = params.get("DataBackupSize")
        self._LogBackupSize = params.get("LogBackupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    r"""Show the Binlog information of the node.

    """

    def __init__(self):
        r"""
        :param _Sid: Unique ID of the log service
        :type Sid: str
        :param _Type: Log service type
        :type Type: str
        :param _InstanceId: Unique ID of the instance
        :type InstanceId: str
        """
        self._Sid = None
        self._Type = None
        self._InstanceId = None

    @property
    def Sid(self):
        r"""Unique ID of the log service
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def Type(self):
        r"""Log service type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        r"""Unique ID of the instance
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIsolateDBInstancesRequest(AbstractModel):
    r"""CancelIsolateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of isolated instance ids required.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""List of isolated instance ids required.
        :rtype: list of str
        """
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
        


class CancelIsolateDBInstancesResponse(AbstractModel):
    r"""CancelIsolateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: List of successfully isolated instance ids.
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: Isolation removal failed instance Id list.
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""List of successfully isolated instance ids.
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""Isolation removal failed instance Id list.
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class CloneInstanceModel(AbstractModel):
    r"""Clone instance object.

    """

    def __init__(self):
        r"""
        :param _CloneEndTime: Clone task end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneEndTime: str
        :param _CloneId: Clone record ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneId: int
        :param _CloneInsType: Clone instance type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneInsType: str
        :param _CloneInstanceId: Clone instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneInstanceId: str
        :param _CloneInstanceIsDeleted: Whether the clone instance is deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneInstanceIsDeleted: bool
        :param _CloneProgress: Task progress of clone.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneProgress: float
        :param _CloneStartTime: Task start time of the clone.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneStartTime: str
        :param _CloneStatus: Task status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneStatus: str
        :param _CloneTime: Clone time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneTime: str
        :param _CloneType: Clone type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloneType: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _DBType: Engine type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DBType: str
        :param _Region: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _SourceInstanceId: Source instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceInstanceId: str
        """
        self._CloneEndTime = None
        self._CloneId = None
        self._CloneInsType = None
        self._CloneInstanceId = None
        self._CloneInstanceIsDeleted = None
        self._CloneProgress = None
        self._CloneStartTime = None
        self._CloneStatus = None
        self._CloneTime = None
        self._CloneType = None
        self._CreateTime = None
        self._DBType = None
        self._Region = None
        self._SourceInstanceId = None

    @property
    def CloneEndTime(self):
        r"""Clone task end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneEndTime

    @CloneEndTime.setter
    def CloneEndTime(self, CloneEndTime):
        self._CloneEndTime = CloneEndTime

    @property
    def CloneId(self):
        r"""Clone record ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CloneId

    @CloneId.setter
    def CloneId(self, CloneId):
        self._CloneId = CloneId

    @property
    def CloneInsType(self):
        r"""Clone instance type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneInsType

    @CloneInsType.setter
    def CloneInsType(self, CloneInsType):
        self._CloneInsType = CloneInsType

    @property
    def CloneInstanceId(self):
        r"""Clone instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneInstanceId

    @CloneInstanceId.setter
    def CloneInstanceId(self, CloneInstanceId):
        self._CloneInstanceId = CloneInstanceId

    @property
    def CloneInstanceIsDeleted(self):
        r"""Whether the clone instance is deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CloneInstanceIsDeleted

    @CloneInstanceIsDeleted.setter
    def CloneInstanceIsDeleted(self, CloneInstanceIsDeleted):
        self._CloneInstanceIsDeleted = CloneInstanceIsDeleted

    @property
    def CloneProgress(self):
        r"""Task progress of clone.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._CloneProgress

    @CloneProgress.setter
    def CloneProgress(self, CloneProgress):
        self._CloneProgress = CloneProgress

    @property
    def CloneStartTime(self):
        r"""Task start time of the clone.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneStartTime

    @CloneStartTime.setter
    def CloneStartTime(self, CloneStartTime):
        self._CloneStartTime = CloneStartTime

    @property
    def CloneStatus(self):
        r"""Task status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneStatus

    @CloneStatus.setter
    def CloneStatus(self, CloneStatus):
        self._CloneStatus = CloneStatus

    @property
    def CloneTime(self):
        r"""Clone time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneTime

    @CloneTime.setter
    def CloneTime(self, CloneTime):
        self._CloneTime = CloneTime

    @property
    def CloneType(self):
        r"""Clone type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloneType

    @CloneType.setter
    def CloneType(self, CloneType):
        self._CloneType = CloneType

    @property
    def CreateTime(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DBType(self):
        r"""Engine type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

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
    def SourceInstanceId(self):
        r"""Source instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId


    def _deserialize(self, params):
        self._CloneEndTime = params.get("CloneEndTime")
        self._CloneId = params.get("CloneId")
        self._CloneInsType = params.get("CloneInsType")
        self._CloneInstanceId = params.get("CloneInstanceId")
        self._CloneInstanceIsDeleted = params.get("CloneInstanceIsDeleted")
        self._CloneProgress = params.get("CloneProgress")
        self._CloneStartTime = params.get("CloneStartTime")
        self._CloneStatus = params.get("CloneStatus")
        self._CloneTime = params.get("CloneTime")
        self._CloneType = params.get("CloneType")
        self._CreateTime = params.get("CreateTime")
        self._DBType = params.get("DBType")
        self._Region = params.get("Region")
        self._SourceInstanceId = params.get("SourceInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    r"""Value range of the constraint type.

    """

    def __init__(self):
        r"""
        :param _Min: Minimum value when the constraint type is section.
        :type Min: str
        :param _Max: Specifies the maximum value when the constraint type is section.
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        r"""Minimum value when the constraint type is section.
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""Specifies the maximum value when the constraint type is section.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceRequest(AbstractModel):
    r"""CreateCloneInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: <p>Creating an Instance Region</p>
        :type Zone: str
        :param _VpcId: <p>Character type vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>Character type subnetid</p>
        :type SubnetId: str
        :param _SpecCode: <p>Purchase specification</p>
        :type SpecCode: str
        :param _Disk: <p>Node disk capacity (unit: GB)</p>
        :type Disk: int
        :param _StorageNodeNum: <p>Number of storage nodes</p>
        :type StorageNodeNum: int
        :param _InstanceId: <p>Source instance id</p>
        :type InstanceId: str
        :param _InstanceName: <p>Instance name. The required length is 1-60. It can contain Chinese characters, English case, digits, hyphens (-), and underscores (_).</p>
        :type InstanceName: str
        :param _ResourceTags: <p>Tag key-value pair array</p>
        :type ResourceTags: list of ResourceTag
        :param _BackupName: <p>Backup and rollback name</p>
        :type BackupName: str
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
        :type StorageNodeMem: int
        :param _CreateVersion: <p>Create version</p>
        :type CreateVersion: str
        :param _Vport: <p>Create port number</p>
        :type Vport: int
        :param _RecoverTime: <p>Recovery time point</p>
        :type RecoverTime: str
        :param _InstanceType: <p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
        :type InstanceType: str
        :param _StorageType: <p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
        :type StorageType: str
        :param _Zones: <p>Multi-AZ list, Zones[0] refers to the primary AZ</p>
        :type Zones: list of str
        :param _FullReplications: <p>Number of replicas</p>
        :type FullReplications: int
        :param _InstanceMode: <p>Instance mode, normal: standard type; enhanced: enhanced</p>
        :type InstanceMode: str
        :param _SecurityGroupIds: <p>Security group id list</p>
        :type SecurityGroupIds: list of str
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeNum = None
        self._InstanceId = None
        self._InstanceName = None
        self._ResourceTags = None
        self._BackupName = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._CreateVersion = None
        self._Vport = None
        self._RecoverTime = None
        self._InstanceType = None
        self._StorageType = None
        self._Zones = None
        self._FullReplications = None
        self._InstanceMode = None
        self._SecurityGroupIds = None

    @property
    def Zone(self):
        r"""<p>Creating an Instance Region</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>Character type vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>Character type subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SpecCode(self):
        r"""<p>Purchase specification</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>Number of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def InstanceId(self):
        r"""<p>Source instance id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>Instance name. The required length is 1-60. It can contain Chinese characters, English case, digits, hyphens (-), and underscores (_).</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        r"""<p>Tag key-value pair array</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def BackupName(self):
        r"""<p>Backup and rollback name</p>
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def CreateVersion(self):
        r"""<p>Create version</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def Vport(self):
        r"""<p>Create port number</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def RecoverTime(self):
        r"""<p>Recovery time point</p>
        :rtype: str
        """
        return self._RecoverTime

    @RecoverTime.setter
    def RecoverTime(self, RecoverTime):
        self._RecoverTime = RecoverTime

    @property
    def InstanceType(self):
        r"""<p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zones(self):
        r"""<p>Multi-AZ list, Zones[0] refers to the primary AZ</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def FullReplications(self):
        r"""<p>Number of replicas</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def InstanceMode(self):
        r"""<p>Instance mode, normal: standard type; enhanced: enhanced</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def SecurityGroupIds(self):
        r"""<p>Security group id list</p>
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._BackupName = params.get("BackupName")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._CreateVersion = params.get("CreateVersion")
        self._Vport = params.get("Vport")
        self._RecoverTime = params.get("RecoverTime")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._Zones = params.get("Zones")
        self._FullReplications = params.get("FullReplications")
        self._InstanceMode = params.get("InstanceMode")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    r"""CreateCloneInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Clone instance ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _FlowId: <p>Task ID.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Clone instance ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    r"""CreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: <p>Creating an Instance Region</p>
        :type Zone: str
        :param _VpcId: <p>Character type vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>Character type subnetid</p>
        :type SubnetId: str
        :param _SpecCode: <p>Purchase specification</p>
        :type SpecCode: str
        :param _Disk: <p>Node disk capacity (unit: GB)</p>
        :type Disk: int
        :param _StorageNodeNum: <p>Number of storage nodes</p>
        :type StorageNodeNum: int
        :param _Replications: <p>Number of node replicas for storage, up to 5, must be an odd number</p>
        :type Replications: int
        :param _InstanceCount: <p>Instance count. Maximum is 10.</p>
        :type InstanceCount: int
        :param _FullReplications: <p>Number of replicas</p>
        :type FullReplications: int
        :param _CreateVersion: <p>Create an instance version, using the current latest version by default</p>
        :type CreateVersion: str
        :param _InstanceName: <p>Instance name. The required length is 1-60. It can contain Chinese characters, English case, digits, hyphens (-), and underscores (_).</p>
        :type InstanceName: str
        :param _ResourceTags: <p>Tag key-value pair array</p>
        :type ResourceTags: list of ResourceTag
        :param _InitParams: <p>Initialize instance parameters. For example:<br>character_set_server (character set, defaults to utf8),<br>lower_case_table_names (table name case sensitivity, 0 - sensitive; 1 - insensitive, default is 0)</p>
        :type InitParams: list of InstanceParam
        :param _TimeUnit: <p>Time unit, m: month</p>
        :type TimeUnit: str
        :param _TimeSpan: <p>Commodity duration size</p>
        :type TimeSpan: int
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
        :type StorageNodeMem: int
        :param _PayMode: <p>Payment mode. 0 means pay-as-you-go/postpaid, 1 means prepaid.</p>
        :type PayMode: str
        :param _MCNum: <p>Number of control nodes</p>
        :type MCNum: int
        :param _Vport: <p>Custom port</p>
        :type Vport: int
        :param _Zones: <p>Multi-AZ availability zone list</p>
        :type Zones: list of str
        :param _AutoVoucher: <p>Whether to use a coupon.</p>
        :type AutoVoucher: bool
        :param _VoucherIds: <p>Coupon list</p>
        :type VoucherIds: list of str
        :param _InstanceType: <p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
        :type InstanceType: str
        :param _StorageType: <p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
        :type StorageType: str
        :param _AZMode: <p>AZ mode. 1: Single AZ, 2: Multi-AZ non-primary AZ, 3: Multi-AZ primary AZ</p>
        :type AZMode: int
        :param _InstanceMode: <p>Instance mode</p>
        :type InstanceMode: str
        :param _TemplateId: <p>Parameter template id</p>
        :type TemplateId: str
        :param _SQLMode: <p>Compatible mode, enum:MySQL,HBase</p>
        :type SQLMode: str
        :param _AutoScaleConfig: <p>ccu configuration of the svls instance</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        :param _SecurityGroupIds: <p>Bind to security group list</p>
        :type SecurityGroupIds: list of str
        :param _UserName: <p>root userName. The default is dbaadmin in the current version. It will reset to dbaadmin even if a value is passed.</p>
        :type UserName: str
        :param _Password: <p>dbaadmin password</p>
        :type Password: str
        :param _EncryptionEnable: <p>Whether transparent data encryption is enabled. 0: not enabled; 1: enabled</p>
        :type EncryptionEnable: int
        """
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeNum = None
        self._Replications = None
        self._InstanceCount = None
        self._FullReplications = None
        self._CreateVersion = None
        self._InstanceName = None
        self._ResourceTags = None
        self._InitParams = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._PayMode = None
        self._MCNum = None
        self._Vport = None
        self._Zones = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._InstanceType = None
        self._StorageType = None
        self._AZMode = None
        self._InstanceMode = None
        self._TemplateId = None
        self._SQLMode = None
        self._AutoScaleConfig = None
        self._SecurityGroupIds = None
        self._UserName = None
        self._Password = None
        self._EncryptionEnable = None

    @property
    def Zone(self):
        r"""<p>Creating an Instance Region</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>Character type vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>Character type subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SpecCode(self):
        r"""<p>Purchase specification</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>Number of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def Replications(self):
        r"""<p>Number of node replicas for storage, up to 5, must be an odd number</p>
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def InstanceCount(self):
        r"""<p>Instance count. Maximum is 10.</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def FullReplications(self):
        r"""<p>Number of replicas</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def CreateVersion(self):
        r"""<p>Create an instance version, using the current latest version by default</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def InstanceName(self):
        r"""<p>Instance name. The required length is 1-60. It can contain Chinese characters, English case, digits, hyphens (-), and underscores (_).</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ResourceTags(self):
        r"""<p>Tag key-value pair array</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InitParams(self):
        r"""<p>Initialize instance parameters. For example:<br>character_set_server (character set, defaults to utf8),<br>lower_case_table_names (table name case sensitivity, 0 - sensitive; 1 - insensitive, default is 0)</p>
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def TimeUnit(self):
        r"""<p>Time unit, m: month</p>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        r"""<p>Commodity duration size</p>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def PayMode(self):
        r"""<p>Payment mode. 0 means pay-as-you-go/postpaid, 1 means prepaid.</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def MCNum(self):
        r"""<p>Number of control nodes</p>
        :rtype: int
        """
        return self._MCNum

    @MCNum.setter
    def MCNum(self, MCNum):
        self._MCNum = MCNum

    @property
    def Vport(self):
        r"""<p>Custom port</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Zones(self):
        r"""<p>Multi-AZ availability zone list</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def AutoVoucher(self):
        r"""<p>Whether to use a coupon.</p>
        :rtype: bool
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>Coupon list</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def InstanceType(self):
        r"""<p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def AZMode(self):
        r"""<p>AZ mode. 1: Single AZ, 2: Multi-AZ non-primary AZ, 3: Multi-AZ primary AZ</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def InstanceMode(self):
        r"""<p>Instance mode</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def TemplateId(self):
        r"""<p>Parameter template id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SQLMode(self):
        r"""<p>Compatible mode, enum:MySQL,HBase</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def AutoScaleConfig(self):
        r"""<p>ccu configuration of the svls instance</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig

    @property
    def SecurityGroupIds(self):
        r"""<p>Bind to security group list</p>
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UserName(self):
        r"""<p>root userName. The default is dbaadmin in the current version. It will reset to dbaadmin even if a value is passed.</p>
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""<p>dbaadmin password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptionEnable(self):
        r"""<p>Whether transparent data encryption is enabled. 0: not enabled; 1: enabled</p>
        :rtype: int
        """
        return self._EncryptionEnable

    @EncryptionEnable.setter
    def EncryptionEnable(self, EncryptionEnable):
        self._EncryptionEnable = EncryptionEnable


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._Replications = params.get("Replications")
        self._InstanceCount = params.get("InstanceCount")
        self._FullReplications = params.get("FullReplications")
        self._CreateVersion = params.get("CreateVersion")
        self._InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._PayMode = params.get("PayMode")
        self._MCNum = params.get("MCNum")
        self._Vport = params.get("Vport")
        self._Zones = params.get("Zones")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._AZMode = params.get("AZMode")
        self._InstanceMode = params.get("InstanceMode")
        self._TemplateId = params.get("TemplateId")
        self._SQLMode = params.get("SQLMode")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._EncryptionEnable = params.get("EncryptionEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstancesResponse(AbstractModel):
    r"""CreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>Instance ID.</p>
        :type InstanceIds: list of str
        :param _FlowId: <p>Task ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceIds = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        r"""<p>Instance ID.</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._InstanceIds = params.get("InstanceIds")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateDBSBackupRequest(AbstractModel):
    r"""CreateDBSBackup request structure.

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>Backup method: physical, snapshot. This value should be consistent with the backupMethod in the API response of DescribeDBSBackupPolicy.</p><p>Enumeration value:</p><ul><li>physical: Physical backup</li><li>snapshot: Snapshot backup</li></ul>
        :type BackupMethod: str
        :param _BackupType: <P>Backup type: currently, only supports full.</p>
        :type BackupType: str
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _BackupName: <P>Backup notes.</p>
        :type BackupName: str
        """
        self._BackupMethod = None
        self._BackupType = None
        self._InstanceId = None
        self._BackupName = None

    @property
    def BackupMethod(self):
        r"""<p>Backup method: physical, snapshot. This value should be consistent with the backupMethod in the API response of DescribeDBSBackupPolicy.</p><p>Enumeration value:</p><ul><li>physical: Physical backup</li><li>snapshot: Snapshot backup</li></ul>
        :rtype: str
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupType(self):
        r"""<P>Backup type: currently, only supports full.</p>
        :rtype: str
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        r"""<P>Backup notes.</p>
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName


    def _deserialize(self, params):
        self._BackupMethod = params.get("BackupMethod")
        self._BackupType = params.get("BackupType")
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBSBackupResponse(AbstractModel):
    r"""CreateDBSBackup response structure.

    """

    def __init__(self):
        r"""
        :param _BackupSetId: <p>Backup set ID.</p>.
        :type BackupSetId: int
        :param _IsSuccess: <P>Whether it is successful</p>.
        :type IsSuccess: bool
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupSetId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def BackupSetId(self):
        r"""<p>Backup set ID.</p>.
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def IsSuccess(self):
        r"""<P>Whether it is successful</p>.
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

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
        self._BackupSetId = params.get("BackupSetId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class CreateUsersRequest(AbstractModel):
    r"""CreateUsers request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance id</p>
        :type InstanceId: str
        :param _Users: <p>Add user list</p>
        :type Users: list of User
        :param _Password: <p>Unencrypted password</p>
        :type Password: str
        :param _EncryptedPassword: <p>Encryption password</p>
        :type EncryptedPassword: str
        :param _Description: <p>User description</p>
        :type Description: str
        """
        self._InstanceId = None
        self._Users = None
        self._Password = None
        self._EncryptedPassword = None
        self._Description = None

    @property
    def InstanceId(self):
        r"""<p>Instance id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        r"""<p>Add user list</p>
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def Password(self):
        r"""<p>Unencrypted password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptedPassword(self):
        r"""<p>Encryption password</p>
        :rtype: str
        """
        return self._EncryptedPassword

    @EncryptedPassword.setter
    def EncryptedPassword(self, EncryptedPassword):
        self._EncryptedPassword = EncryptedPassword

    @property
    def Description(self):
        r"""<p>User description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._Password = params.get("Password")
        self._EncryptedPassword = params.get("EncryptedPassword")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsersResponse(AbstractModel):
    r"""CreateUsers response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Task ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DBParamValue(AbstractModel):
    r"""Cloud database parameter information.

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name.
        :type Param: str
        :param _Value: Parameter value.
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""Parameter value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataBackupStatisticsModel(AbstractModel):
    r"""Data backup statistics object

    """

    def __init__(self):
        r"""
        :param _AutoBackupCount: Auto-backup count
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoBackupCount: int
        :param _AutoBackupSize: Auto-backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type AutoBackupSize: int
        :param _AverageSizePerBackup: Avg backup size per each, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerBackup: int
        :param _AverageSizePerDay: Avg daily backup size, Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerDay: int
        :param _ManualBackupCount: Manual backup count
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackupCount: int
        :param _ManualBackupSize: Manual backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type ManualBackupSize: int
        :param _TotalCount: Number of data backups
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _TotalSize: Data backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._AutoBackupCount = None
        self._AutoBackupSize = None
        self._AverageSizePerBackup = None
        self._AverageSizePerDay = None
        self._ManualBackupCount = None
        self._ManualBackupSize = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AutoBackupCount(self):
        r"""Auto-backup count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoBackupCount

    @AutoBackupCount.setter
    def AutoBackupCount(self, AutoBackupCount):
        self._AutoBackupCount = AutoBackupCount

    @property
    def AutoBackupSize(self):
        r"""Auto-backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AutoBackupSize

    @AutoBackupSize.setter
    def AutoBackupSize(self, AutoBackupSize):
        self._AutoBackupSize = AutoBackupSize

    @property
    def AverageSizePerBackup(self):
        r"""Avg backup size per each, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerBackup

    @AverageSizePerBackup.setter
    def AverageSizePerBackup(self, AverageSizePerBackup):
        self._AverageSizePerBackup = AverageSizePerBackup

    @property
    def AverageSizePerDay(self):
        r"""Avg daily backup size, Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def ManualBackupCount(self):
        r"""Manual backup count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ManualBackupCount

    @ManualBackupCount.setter
    def ManualBackupCount(self, ManualBackupCount):
        self._ManualBackupCount = ManualBackupCount

    @property
    def ManualBackupSize(self):
        r"""Manual backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ManualBackupSize

    @ManualBackupSize.setter
    def ManualBackupSize(self, ManualBackupSize):
        self._ManualBackupSize = ManualBackupSize

    @property
    def TotalCount(self):
        r"""Number of data backups
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""Data backup size, in Byte
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AutoBackupCount = params.get("AutoBackupCount")
        self._AutoBackupSize = params.get("AutoBackupSize")
        self._AverageSizePerBackup = params.get("AverageSizePerBackup")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._ManualBackupCount = params.get("ManualBackupCount")
        self._ManualBackupSize = params.get("ManualBackupSize")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    r"""Database information

    """

    def __init__(self):
        r"""
        :param _DbName: Database name.
        :type DbName: str
        """
        self._DbName = None

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    r"""Database function information.

    """

    def __init__(self):
        r"""
        :param _Func: Function name.
        :type Func: str
        """
        self._Func = None

    @property
    def Func(self):
        r"""Function name.
        :rtype: str
        """
        return self._Func

    @Func.setter
    def Func(self, Func):
        self._Func = Func


    def _deserialize(self, params):
        self._Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivileges(AbstractModel):
    r"""Database-level permission list

    """

    def __init__(self):
        r"""
        :param _Database: database name
        :type Database: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        """
        self._Database = None
        self._Privileges = None

    @property
    def Database(self):
        r"""database name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Privileges(self):
        r"""Permission list
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    r"""Database stored procedure information.

    """

    def __init__(self):
        r"""
        :param _Proc: Stored procedure name.
        :type Proc: str
        """
        self._Proc = None

    @property
    def Proc(self):
        r"""Stored procedure name.
        :rtype: str
        """
        return self._Proc

    @Proc.setter
    def Proc(self, Proc):
        self._Proc = Proc


    def _deserialize(self, params):
        self._Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    r"""Database table information.

    """

    def __init__(self):
        r"""
        :param _Table: Table name
        :type Table: str
        """
        self._Table = None

    @property
    def Table(self):
        r"""Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table


    def _deserialize(self, params):
        self._Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    r"""Database view information.

    """

    def __init__(self):
        r"""
        :param _View: View name.
        :type View: str
        """
        self._View = None

    @property
    def View(self):
        r"""View name.
        :rtype: str
        """
        return self._View

    @View.setter
    def View(self, View):
        self._View = View


    def _deserialize(self, params):
        self._View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBSBackupSetsRequest(AbstractModel):
    r"""DeleteDBSBackupSets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _BackupSetIdList: <p>Backup set list. the value comes from the DescribeDBSBackupSets api response.</p>
        :type BackupSetIdList: list of int
        """
        self._InstanceId = None
        self._BackupSetIdList = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupSetIdList(self):
        r"""<p>Backup set list. the value comes from the DescribeDBSBackupSets api response.</p>
        :rtype: list of int
        """
        return self._BackupSetIdList

    @BackupSetIdList.setter
    def BackupSetIdList(self, BackupSetIdList):
        self._BackupSetIdList = BackupSetIdList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetIdList = params.get("BackupSetIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDBSBackupSetsResponse(AbstractModel):
    r"""DeleteDBSBackupSets response structure.

    """

    def __init__(self):
        r"""
        :param _Deleted: <P>Number of backups deleted this time.</p>
        :type Deleted: int
        :param _IsSuccess: <P>Whether all are deleted successfully.</p>
        :type IsSuccess: bool
        :param _Total: <P>Total number of backups to be deleted.</p>
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Deleted = None
        self._IsSuccess = None
        self._Total = None
        self._RequestId = None

    @property
    def Deleted(self):
        r"""<P>Number of backups deleted this time.</p>
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def IsSuccess(self):
        r"""<P>Whether all are deleted successfully.</p>
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Total(self):
        r"""<P>Total number of backups to be deleted.</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Deleted = params.get("Deleted")
        self._IsSuccess = params.get("IsSuccess")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DeleteUsersRequest(AbstractModel):
    r"""DeleteUsers request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance id</p>
        :type InstanceId: str
        :param _Users: <p>Batch delete user list</p>
        :type Users: list of User
        """
        self._InstanceId = None
        self._Users = None

    @property
    def InstanceId(self):
        r"""<p>Instance id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        r"""<p>Batch delete user list</p>
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsersResponse(AbstractModel):
    r"""DeleteUsers response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Task ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceDetailRequest(AbstractModel):
    r"""DescribeDBInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
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
        


class DescribeDBInstanceDetailResponse(AbstractModel):
    r"""DescribeDBInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: <p>Instance name</p>
        :type InstanceName: str
        :param _Zone: <p>Region</p>
        :type Zone: str
        :param _VpcId: <p>Character type vpcid</p>
        :type VpcId: str
        :param _SubnetId: <p>Character type subnetid</p>
        :type SubnetId: str
        :param _CreateVersion: <p>Create an instance version</p>
        :type CreateVersion: str
        :param _Vip: <p>Subnet IP</p>
        :type Vip: str
        :param _Vport: <p>Subnet port</p>
        :type Vport: int
        :param _Status: <p>Instance status</p>
        :type Status: str
        :param _Disk: <p>Node disk capacity (unit: GB)</p>
        :type Disk: int
        :param _StorageNodeNum: <p>Number of storage nodes</p>
        :type StorageNodeNum: int
        :param _InitParams: <p>Initialize instance parameters</p>
        :type InitParams: list of InstanceParam
        :param _ResourceTags: <p>Instance tag information.</p>
        :type ResourceTags: list of ResourceTag
        :param _CreateTime: <p>Creation time.</p>
        :type CreateTime: str
        :param _UpdateTime: <p>Update time.</p>
        :type UpdateTime: str
        :param _Replications: <p>Number of storage node replicas</p>
        :type Replications: int
        :param _FullReplications: <p>Number of replicas</p>
        :type FullReplications: int
        :param _CharSet: <p>Character set</p>
        :type CharSet: str
        :param _Node: <p>Node information</p>
        :type Node: list of NodeInfo
        :param _Region: <p>Region of the instance</p>
        :type Region: str
        :param _SpecCode: <p>Instance specification</p>
        :type SpecCode: str
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _StatusDesc: <p>Status description in Chinese of the instance</p>
        :type StatusDesc: str
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
        :type StorageNodeMem: int
        :param _RenewFlag: <p>Renewal flag</p>
        :type RenewFlag: int
        :param _PayMode: <p>Payment mode, 0 pay-as-you-go, 1 prepaid</p>
        :type PayMode: str
        :param _ExpireAt: <p>Expiration time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireAt: str
        :param _IsolatedAt: <p>Isolation time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedAt: str
        :param _InstanceType: <p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _StorageType: <p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageType: str
        :param _Zones: <p>List of instance node availability zones. Zones[0] refers to the primary AZ</p>
        :type Zones: list of str
        :param _DiskUsage: <p>Disk usage of the largest node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskUsage: int
        :param _BinlogStatus: <p>Whether binlog is enabled</p>
        :type BinlogStatus: int
        :param _AZMode: <p>az mode. 1: Single az 2: Multi-az non-primary az mode 3: Multi-az primary az mode</p>
        :type AZMode: int
        :param _StandbyFlag: <p>Disaster recovery flag. 1: No disaster recovery relationship; 2: Primary instance for disaster recovery; 3: Disaster Recovery Standby Instance</p>
        :type StandbyFlag: int
        :param _BinlogType: <p>cdc node type</p>
        :type BinlogType: str
        :param _TimingModifyInstanceFlag: <p>1 means supported, 0 means unsupported</p>
        :type TimingModifyInstanceFlag: int
        :param _ColumnarNodeCpu: <p>cpu cores of the columnar node</p>
        :type ColumnarNodeCpu: int
        :param _ColumnarNodeMem: <p>Columnar node memory size</p>
        :type ColumnarNodeMem: int
        :param _ColumnarNodeNum: <p>Number of columnar nodes</p>
        :type ColumnarNodeNum: int
        :param _ColumnarNodeDisk: <p>Columnar node disk size</p>
        :type ColumnarNodeDisk: int
        :param _ColumnarNodeStorageType: <p>Columnar node disk type</p>
        :type ColumnarNodeStorageType: str
        :param _ColumnarNodeSpecCode: <p>Columnar node specification</p>
        :type ColumnarNodeSpecCode: str
        :param _ColumnarVip: <p>Columnar storage vip</p>
        :type ColumnarVip: str
        :param _ColumnarVport: <p>Columnar vport</p>
        :type ColumnarVport: int
        :param _IsSupportColumnar: <p>Whether the instance supports columnar storage</p>
        :type IsSupportColumnar: bool
        :param _InstanceCategory: <p>Instance type</p>
        :type InstanceCategory: int
        :param _SQLMode: <p>Compatible mode</p>
        :type SQLMode: str
        :param _IsSwitchFullReplicationsEnable: <p>Whether modification of the number of replicas is supported</p>
        :type IsSwitchFullReplicationsEnable: bool
        :param _InstanceMode: <p>Instance type</p>
        :type InstanceMode: str
        :param _DumperVip: <p>dumper vip</p>
        :type DumperVip: str
        :param _DumperVport: <p>dumper vport</p>
        :type DumperVport: int
        :param _AutoScaleConfig: <p>ccu adjustment range of the svls instance</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        :param _TemplateId: <p>Parameter template id</p>
        :type TemplateId: str
        :param _TemplateName: <p>Parameter template name</p>
        :type TemplateName: str
        :param _AnalysisMode: <p>Instance analysis engine mode</p><p>Enumeration value:</p><ul><li>libra: LibraDB analysis engine instance</li></ul>
        :type AnalysisMode: str
        :param _AnalysisRelationInfos: <p>Analysis engine instance relationship</p>
        :type AnalysisRelationInfos: list of AnalysisRelationInfo
        :param _AnalysisInstanceInfo: <p>Analysis engine instance info</p><p>Cpu, Memory, and Disk reuse top-level fields</p>
        :type AnalysisInstanceInfo: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        :param _MaintenanceWindow: <p>Maintenance window configuration</p>
        :type MaintenanceWindow: :class:`tencentcloud.tdmysql.v20211122.models.MaintenanceWindowInfo`
        :param _EncryptionEnable: <p>Whether transparent data encryption is enabled. 0: not enabled; 1: enabled</p>
        :type EncryptionEnable: int
        :param _EncryptionKmsRegion: <p>Real-use kms region for subsequent call to kms service</p>
        :type EncryptionKmsRegion: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceName = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._CreateVersion = None
        self._Vip = None
        self._Vport = None
        self._Status = None
        self._Disk = None
        self._StorageNodeNum = None
        self._InitParams = None
        self._ResourceTags = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Replications = None
        self._FullReplications = None
        self._CharSet = None
        self._Node = None
        self._Region = None
        self._SpecCode = None
        self._InstanceId = None
        self._StatusDesc = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpireAt = None
        self._IsolatedAt = None
        self._InstanceType = None
        self._StorageType = None
        self._Zones = None
        self._DiskUsage = None
        self._BinlogStatus = None
        self._AZMode = None
        self._StandbyFlag = None
        self._BinlogType = None
        self._TimingModifyInstanceFlag = None
        self._ColumnarNodeCpu = None
        self._ColumnarNodeMem = None
        self._ColumnarNodeNum = None
        self._ColumnarNodeDisk = None
        self._ColumnarNodeStorageType = None
        self._ColumnarNodeSpecCode = None
        self._ColumnarVip = None
        self._ColumnarVport = None
        self._IsSupportColumnar = None
        self._InstanceCategory = None
        self._SQLMode = None
        self._IsSwitchFullReplicationsEnable = None
        self._InstanceMode = None
        self._DumperVip = None
        self._DumperVport = None
        self._AutoScaleConfig = None
        self._TemplateId = None
        self._TemplateName = None
        self._AnalysisMode = None
        self._AnalysisRelationInfos = None
        self._AnalysisInstanceInfo = None
        self._MaintenanceWindow = None
        self._EncryptionEnable = None
        self._EncryptionKmsRegion = None
        self._RequestId = None

    @property
    def InstanceName(self):
        r"""<p>Instance name</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        r"""<p>Region</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        r"""<p>Character type vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>Character type subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateVersion(self):
        r"""<p>Create an instance version</p>
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def Vip(self):
        r"""<p>Subnet IP</p>
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""<p>Subnet port</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Status(self):
        r"""<p>Instance status</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Disk(self):
        r"""<p>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeNum(self):
        r"""<p>Number of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def InitParams(self):
        r"""<p>Initialize instance parameters</p>
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def ResourceTags(self):
        r"""<p>Instance tag information.</p>
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CreateTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Replications(self):
        r"""<p>Number of storage node replicas</p>
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def FullReplications(self):
        r"""<p>Number of replicas</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def CharSet(self):
        r"""<p>Character set</p>
        :rtype: str
        """
        return self._CharSet

    @CharSet.setter
    def CharSet(self, CharSet):
        self._CharSet = CharSet

    @property
    def Node(self):
        r"""<p>Node information</p>
        :rtype: list of NodeInfo
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Region(self):
        r"""<p>Region of the instance</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SpecCode(self):
        r"""<p>Instance specification</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StatusDesc(self):
        r"""<p>Status description in Chinese of the instance</p>
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def RenewFlag(self):
        r"""<p>Renewal flag</p>
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        r"""<p>Payment mode, 0 pay-as-you-go, 1 prepaid</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpireAt(self):
        r"""<p>Expiration time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def IsolatedAt(self):
        r"""<p>Isolation time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def InstanceType(self):
        r"""<p>Instance Architecture Type, separate: decoupled architecture; hybrid: peer-to-peer architecture</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zones(self):
        r"""<p>List of instance node availability zones. Zones[0] refers to the primary AZ</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def DiskUsage(self):
        r"""<p>Disk usage of the largest node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def BinlogStatus(self):
        r"""<p>Whether binlog is enabled</p>
        :rtype: int
        """
        return self._BinlogStatus

    @BinlogStatus.setter
    def BinlogStatus(self, BinlogStatus):
        self._BinlogStatus = BinlogStatus

    @property
    def AZMode(self):
        r"""<p>az mode. 1: Single az 2: Multi-az non-primary az mode 3: Multi-az primary az mode</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def StandbyFlag(self):
        r"""<p>Disaster recovery flag. 1: No disaster recovery relationship; 2: Primary instance for disaster recovery; 3: Disaster Recovery Standby Instance</p>
        :rtype: int
        """
        return self._StandbyFlag

    @StandbyFlag.setter
    def StandbyFlag(self, StandbyFlag):
        self._StandbyFlag = StandbyFlag

    @property
    def BinlogType(self):
        r"""<p>cdc node type</p>
        :rtype: str
        """
        return self._BinlogType

    @BinlogType.setter
    def BinlogType(self, BinlogType):
        self._BinlogType = BinlogType

    @property
    def TimingModifyInstanceFlag(self):
        r"""<p>1 means supported, 0 means unsupported</p>
        :rtype: int
        """
        return self._TimingModifyInstanceFlag

    @TimingModifyInstanceFlag.setter
    def TimingModifyInstanceFlag(self, TimingModifyInstanceFlag):
        self._TimingModifyInstanceFlag = TimingModifyInstanceFlag

    @property
    def ColumnarNodeCpu(self):
        r"""<p>cpu cores of the columnar node</p>
        :rtype: int
        """
        return self._ColumnarNodeCpu

    @ColumnarNodeCpu.setter
    def ColumnarNodeCpu(self, ColumnarNodeCpu):
        self._ColumnarNodeCpu = ColumnarNodeCpu

    @property
    def ColumnarNodeMem(self):
        r"""<p>Columnar node memory size</p>
        :rtype: int
        """
        return self._ColumnarNodeMem

    @ColumnarNodeMem.setter
    def ColumnarNodeMem(self, ColumnarNodeMem):
        self._ColumnarNodeMem = ColumnarNodeMem

    @property
    def ColumnarNodeNum(self):
        r"""<p>Number of columnar nodes</p>
        :rtype: int
        """
        return self._ColumnarNodeNum

    @ColumnarNodeNum.setter
    def ColumnarNodeNum(self, ColumnarNodeNum):
        self._ColumnarNodeNum = ColumnarNodeNum

    @property
    def ColumnarNodeDisk(self):
        r"""<p>Columnar node disk size</p>
        :rtype: int
        """
        return self._ColumnarNodeDisk

    @ColumnarNodeDisk.setter
    def ColumnarNodeDisk(self, ColumnarNodeDisk):
        self._ColumnarNodeDisk = ColumnarNodeDisk

    @property
    def ColumnarNodeStorageType(self):
        r"""<p>Columnar node disk type</p>
        :rtype: str
        """
        return self._ColumnarNodeStorageType

    @ColumnarNodeStorageType.setter
    def ColumnarNodeStorageType(self, ColumnarNodeStorageType):
        self._ColumnarNodeStorageType = ColumnarNodeStorageType

    @property
    def ColumnarNodeSpecCode(self):
        r"""<p>Columnar node specification</p>
        :rtype: str
        """
        return self._ColumnarNodeSpecCode

    @ColumnarNodeSpecCode.setter
    def ColumnarNodeSpecCode(self, ColumnarNodeSpecCode):
        self._ColumnarNodeSpecCode = ColumnarNodeSpecCode

    @property
    def ColumnarVip(self):
        r"""<p>Columnar storage vip</p>
        :rtype: str
        """
        return self._ColumnarVip

    @ColumnarVip.setter
    def ColumnarVip(self, ColumnarVip):
        self._ColumnarVip = ColumnarVip

    @property
    def ColumnarVport(self):
        r"""<p>Columnar vport</p>
        :rtype: int
        """
        return self._ColumnarVport

    @ColumnarVport.setter
    def ColumnarVport(self, ColumnarVport):
        self._ColumnarVport = ColumnarVport

    @property
    def IsSupportColumnar(self):
        r"""<p>Whether the instance supports columnar storage</p>
        :rtype: bool
        """
        return self._IsSupportColumnar

    @IsSupportColumnar.setter
    def IsSupportColumnar(self, IsSupportColumnar):
        self._IsSupportColumnar = IsSupportColumnar

    @property
    def InstanceCategory(self):
        r"""<p>Instance type</p>
        :rtype: int
        """
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def SQLMode(self):
        r"""<p>Compatible mode</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def IsSwitchFullReplicationsEnable(self):
        r"""<p>Whether modification of the number of replicas is supported</p>
        :rtype: bool
        """
        return self._IsSwitchFullReplicationsEnable

    @IsSwitchFullReplicationsEnable.setter
    def IsSwitchFullReplicationsEnable(self, IsSwitchFullReplicationsEnable):
        self._IsSwitchFullReplicationsEnable = IsSwitchFullReplicationsEnable

    @property
    def InstanceMode(self):
        r"""<p>Instance type</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def DumperVip(self):
        r"""<p>dumper vip</p>
        :rtype: str
        """
        return self._DumperVip

    @DumperVip.setter
    def DumperVip(self, DumperVip):
        self._DumperVip = DumperVip

    @property
    def DumperVport(self):
        r"""<p>dumper vport</p>
        :rtype: int
        """
        return self._DumperVport

    @DumperVport.setter
    def DumperVport(self, DumperVport):
        self._DumperVport = DumperVport

    @property
    def AutoScaleConfig(self):
        r"""<p>ccu adjustment range of the svls instance</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig

    @property
    def TemplateId(self):
        r"""<p>Parameter template id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>Parameter template name</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def AnalysisMode(self):
        r"""<p>Instance analysis engine mode</p><p>Enumeration value:</p><ul><li>libra: LibraDB analysis engine instance</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def AnalysisRelationInfos(self):
        r"""<p>Analysis engine instance relationship</p>
        :rtype: list of AnalysisRelationInfo
        """
        return self._AnalysisRelationInfos

    @AnalysisRelationInfos.setter
    def AnalysisRelationInfos(self, AnalysisRelationInfos):
        self._AnalysisRelationInfos = AnalysisRelationInfos

    @property
    def AnalysisInstanceInfo(self):
        r"""<p>Analysis engine instance info</p><p>Cpu, Memory, and Disk reuse top-level fields</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        """
        return self._AnalysisInstanceInfo

    @AnalysisInstanceInfo.setter
    def AnalysisInstanceInfo(self, AnalysisInstanceInfo):
        self._AnalysisInstanceInfo = AnalysisInstanceInfo

    @property
    def MaintenanceWindow(self):
        r"""<p>Maintenance window configuration</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.MaintenanceWindowInfo`
        """
        return self._MaintenanceWindow

    @MaintenanceWindow.setter
    def MaintenanceWindow(self, MaintenanceWindow):
        self._MaintenanceWindow = MaintenanceWindow

    @property
    def EncryptionEnable(self):
        r"""<p>Whether transparent data encryption is enabled. 0: not enabled; 1: enabled</p>
        :rtype: int
        """
        return self._EncryptionEnable

    @EncryptionEnable.setter
    def EncryptionEnable(self, EncryptionEnable):
        self._EncryptionEnable = EncryptionEnable

    @property
    def EncryptionKmsRegion(self):
        r"""<p>Real-use kms region for subsequent call to kms service</p>
        :rtype: str
        """
        return self._EncryptionKmsRegion

    @EncryptionKmsRegion.setter
    def EncryptionKmsRegion(self, EncryptionKmsRegion):
        self._EncryptionKmsRegion = EncryptionKmsRegion

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
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreateVersion = params.get("CreateVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Status = params.get("Status")
        self._Disk = params.get("Disk")
        self._StorageNodeNum = params.get("StorageNodeNum")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Replications = params.get("Replications")
        self._FullReplications = params.get("FullReplications")
        self._CharSet = params.get("CharSet")
        if params.get("Node") is not None:
            self._Node = []
            for item in params.get("Node"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._Node.append(obj)
        self._Region = params.get("Region")
        self._SpecCode = params.get("SpecCode")
        self._InstanceId = params.get("InstanceId")
        self._StatusDesc = params.get("StatusDesc")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpireAt = params.get("ExpireAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._Zones = params.get("Zones")
        self._DiskUsage = params.get("DiskUsage")
        self._BinlogStatus = params.get("BinlogStatus")
        self._AZMode = params.get("AZMode")
        self._StandbyFlag = params.get("StandbyFlag")
        self._BinlogType = params.get("BinlogType")
        self._TimingModifyInstanceFlag = params.get("TimingModifyInstanceFlag")
        self._ColumnarNodeCpu = params.get("ColumnarNodeCpu")
        self._ColumnarNodeMem = params.get("ColumnarNodeMem")
        self._ColumnarNodeNum = params.get("ColumnarNodeNum")
        self._ColumnarNodeDisk = params.get("ColumnarNodeDisk")
        self._ColumnarNodeStorageType = params.get("ColumnarNodeStorageType")
        self._ColumnarNodeSpecCode = params.get("ColumnarNodeSpecCode")
        self._ColumnarVip = params.get("ColumnarVip")
        self._ColumnarVport = params.get("ColumnarVport")
        self._IsSupportColumnar = params.get("IsSupportColumnar")
        self._InstanceCategory = params.get("InstanceCategory")
        self._SQLMode = params.get("SQLMode")
        self._IsSwitchFullReplicationsEnable = params.get("IsSwitchFullReplicationsEnable")
        self._InstanceMode = params.get("InstanceMode")
        self._DumperVip = params.get("DumperVip")
        self._DumperVport = params.get("DumperVport")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("AnalysisRelationInfos") is not None:
            self._AnalysisRelationInfos = []
            for item in params.get("AnalysisRelationInfos"):
                obj = AnalysisRelationInfo()
                obj._deserialize(item)
                self._AnalysisRelationInfos.append(obj)
        if params.get("AnalysisInstanceInfo") is not None:
            self._AnalysisInstanceInfo = AnalysisInstanceInfo()
            self._AnalysisInstanceInfo._deserialize(params.get("AnalysisInstanceInfo"))
        if params.get("MaintenanceWindow") is not None:
            self._MaintenanceWindow = MaintenanceWindowInfo()
            self._MaintenanceWindow._deserialize(params.get("MaintenanceWindow"))
        self._EncryptionEnable = params.get("EncryptionEnable")
        self._EncryptionKmsRegion = params.get("EncryptionKmsRegion")
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <p>Filter parameters</p>
        :type Filters: list of InstanceFilter
        :param _Limit: <p>Maximum return count, defaults to 20, maximum 100</p>
        :type Limit: int
        :param _Offset: <p>Offset, which is an integer multiple of Limit.</p>
        :type Offset: int
        :param _EngineType: <p>Specified query engine type</p><p>Enumeration value:</p><ul><li>libra: Column storage engine</li></ul>
        :type EngineType: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._EngineType = None

    @property
    def Filters(self):
        r"""<p>Filter parameters</p>
        :rtype: list of InstanceFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""<p>Maximum return count, defaults to 20, maximum 100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Offset, which is an integer multiple of Limit.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EngineType(self):
        r"""<p>Specified query engine type</p><p>Enumeration value:</p><ul><li>libra: Column storage engine</li></ul>
        :rtype: str
        """
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = InstanceFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Instances: <p>Return to instance list information</p>
        :type Instances: list of InstanceInfo
        :param _TotalCount: <p>Total number of conditions met</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""<p>Return to instance list information</p>
        :rtype: list of InstanceInfo
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""<p>Total number of conditions met</p>
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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    r"""DescribeDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, for example: tdsql3-ow728lmc.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, for example: tdsql3-ow728lmc.
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
        


class DescribeDBParametersResponse(AbstractModel):
    r"""DescribeDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, for example: tdsql3-ow728lmc.
        :type InstanceId: str
        :param _Params: Request the current parameter value of the instance.
        :type Params: list of ParamDesc
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Params = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""Instance ID, for example: tdsql3-ow728lmc.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        r"""Request the current parameter value of the instance.
        :rtype: list of ParamDesc
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

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
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self._Params.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSArchiveLogsRequest(AbstractModel):
    r"""DescribeDBSArchiveLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _ArchiveLogId: <p>Logging ID</p>
        :type ArchiveLogId: int
        :param _EndTime: <p>End time.</p>
        :type EndTime: str
        :param _FilterStatus: <p>Backup status: pending, running, success, failed</p>
        :type FilterStatus: str
        :param _Limit: <p>Limit on number</p>
        :type Limit: int
        :param _Offset: <p>Offset.</p>
        :type Offset: int
        :param _OrderBy: <p>Sorting field, enumerate: StartTime, EndTime, ExpiredTime, FileSize, BackupDuration</p>
        :type OrderBy: str
        :param _OrderType: <p>Sorting method: ASC: sequential, DESC: reverse</p>
        :type OrderType: str
        :param _StartTime: <p>Start time.</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._ArchiveLogId = None
        self._EndTime = None
        self._FilterStatus = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ArchiveLogId(self):
        r"""<p>Logging ID</p>
        :rtype: int
        """
        return self._ArchiveLogId

    @ArchiveLogId.setter
    def ArchiveLogId(self, ArchiveLogId):
        self._ArchiveLogId = ArchiveLogId

    @property
    def EndTime(self):
        r"""<p>End time.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FilterStatus(self):
        r"""<p>Backup status: pending, running, success, failed</p>
        :rtype: str
        """
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def Limit(self):
        r"""<p>Limit on number</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Offset.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>Sorting field, enumerate: StartTime, EndTime, ExpiredTime, FileSize, BackupDuration</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>Sorting method: ASC: sequential, DESC: reverse</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>Start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ArchiveLogId = params.get("ArchiveLogId")
        self._EndTime = params.get("EndTime")
        self._FilterStatus = params.get("FilterStatus")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSArchiveLogsResponse(AbstractModel):
    r"""DescribeDBSArchiveLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Items: <p>Archivelog list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of ArchiveLogModel
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        r"""<p>Archivelog list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ArchiveLogModel
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ArchiveLogModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
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
        


class DescribeDBSAvailableRecoveryTimeResponse(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime response structure.

    """

    def __init__(self):
        r"""
        :param _EndTime: <P>End time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Intervals: <P>Recoverable time interval.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Intervals: list of ArchiveLogInterval
        :param _StartTime: <P>Start time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EndTime = None
        self._Intervals = None
        self._StartTime = None
        self._RequestId = None

    @property
    def EndTime(self):
        r"""<P>End time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Intervals(self):
        r"""<P>Recoverable time interval.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ArchiveLogInterval
        """
        return self._Intervals

    @Intervals.setter
    def Intervals(self, Intervals):
        self._Intervals = Intervals

    @property
    def StartTime(self):
        r"""<P>Start time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

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
        self._EndTime = params.get("EndTime")
        if params.get("Intervals") is not None:
            self._Intervals = []
            for item in params.get("Intervals"):
                obj = ArchiveLogInterval()
                obj._deserialize(item)
                self._Intervals.append(obj)
        self._StartTime = params.get("StartTime")
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupPolicyRequest(AbstractModel):
    r"""DescribeDBSBackupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
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
        


class DescribeDBSBackupPolicyResponse(AbstractModel):
    r"""DescribeDBSBackupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Items: <p>Backup policy list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of BackupPolicyModelOutPut
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        r"""<p>Backup policy list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupPolicyModelOutPut
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupPolicyModelOutPut()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupSetsRequest(AbstractModel):
    r"""DescribeDBSBackupSets request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _BackupSetId: <p>Instance Backup set ID</p>
        :type BackupSetId: int
        :param _EndTime: <p>End time.</p>
        :type EndTime: str
        :param _FilterBy: <p>Filtering Conditions</p>
        :type FilterBy: :class:`tencentcloud.tdmysql.v20211122.models.BackupSetsReqFilter`
        :param _Limit: <p>Query count [0,200]</p>
        :type Limit: int
        :param _Offset: <p>Query offset [0,INF] this time.</p>
        :type Offset: int
        :param _OrderBy: <p>StartTime,EndTime,ExpiredTime,BackupSetId,BackupDuration</p>
        :type OrderBy: str
        :param _OrderType: <p>ASC,DESC</p>
        :type OrderType: str
        :param _StartTime: <p>Start time.</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._BackupSetId = None
        self._EndTime = None
        self._FilterBy = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupSetId(self):
        r"""<p>Instance Backup set ID</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def EndTime(self):
        r"""<p>End time.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FilterBy(self):
        r"""<p>Filtering Conditions</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupSetsReqFilter`
        """
        return self._FilterBy

    @FilterBy.setter
    def FilterBy(self, FilterBy):
        self._FilterBy = FilterBy

    @property
    def Limit(self):
        r"""<p>Query count [0,200]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Query offset [0,INF] this time.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>StartTime,EndTime,ExpiredTime,BackupSetId,BackupDuration</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>ASC,DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>Start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._EndTime = params.get("EndTime")
        if params.get("FilterBy") is not None:
            self._FilterBy = BackupSetsReqFilter()
            self._FilterBy._deserialize(params.get("FilterBy"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupSetsResponse(AbstractModel):
    r"""DescribeDBSBackupSets response structure.

    """

    def __init__(self):
        r"""
        :param _Items: <p>Backup set list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of BackupSetModel
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        r"""<p>Backup set list</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of BackupSetModel
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = BackupSetModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupStatisticsDetailRequest(AbstractModel):
    r"""DescribeDBSBackupStatisticsDetail request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _EndTime: <p>End time.</p>
        :type EndTime: str
        :param _StartTime: <p>Start time.</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._EndTime = None
        self._StartTime = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EndTime(self):
        r"""<p>End time.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""<p>Start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupStatisticsDetailResponse(AbstractModel):
    r"""DescribeDBSBackupStatisticsDetail response structure.

    """

    def __init__(self):
        r"""
        :param _BackupMethodStatistics: <p>Statistics by backup method</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupMethodStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsOutPut`
        :param _BackupTime: <p>Backup time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupTime: list of str
        :param _BackupTypeStatistics: <p>Data type statistics by backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupTypeStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupTypeStatisticsModel`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupMethodStatistics = None
        self._BackupTime = None
        self._BackupTypeStatistics = None
        self._RequestId = None

    @property
    def BackupMethodStatistics(self):
        r"""<p>Statistics by backup method</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsOutPut`
        """
        return self._BackupMethodStatistics

    @BackupMethodStatistics.setter
    def BackupMethodStatistics(self, BackupMethodStatistics):
        self._BackupMethodStatistics = BackupMethodStatistics

    @property
    def BackupTime(self):
        r"""<p>Backup time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupTypeStatistics(self):
        r"""<p>Data type statistics by backup</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupTypeStatisticsModel`
        """
        return self._BackupTypeStatistics

    @BackupTypeStatistics.setter
    def BackupTypeStatistics(self, BackupTypeStatistics):
        self._BackupTypeStatistics = BackupTypeStatistics

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
        if params.get("BackupMethodStatistics") is not None:
            self._BackupMethodStatistics = BackupMethodStatisticsOutPut()
            self._BackupMethodStatistics._deserialize(params.get("BackupMethodStatistics"))
        self._BackupTime = params.get("BackupTime")
        if params.get("BackupTypeStatistics") is not None:
            self._BackupTypeStatistics = BackupTypeStatisticsModel()
            self._BackupTypeStatistics._deserialize(params.get("BackupTypeStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeDBSBackupStatisticsRequest(AbstractModel):
    r"""DescribeDBSBackupStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _EndTime: <p>End time.</p>
        :type EndTime: str
        :param _StartTime: <p>Start time.</p>
        :type StartTime: str
        """
        self._InstanceId = None
        self._EndTime = None
        self._StartTime = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EndTime(self):
        r"""<p>End time.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""<p>Start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSBackupStatisticsResponse(AbstractModel):
    r"""DescribeDBSBackupStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _BackupMethodStatistics: <p>Backup method statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupMethodStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsModel`
        :param _BackupStatistics: <p>Backup set statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.BackupStatisticsModel`
        :param _DataBackupStatistics: <p>Backup statistics.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataBackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.DataBackupStatisticsModel`
        :param _LogBackupStatistics: <p>Log backup statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogBackupStatistics: :class:`tencentcloud.tdmysql.v20211122.models.LogBackupStatisticsModel`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupMethodStatistics = None
        self._BackupStatistics = None
        self._DataBackupStatistics = None
        self._LogBackupStatistics = None
        self._RequestId = None

    @property
    def BackupMethodStatistics(self):
        r"""<p>Backup method statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupMethodStatisticsModel`
        """
        return self._BackupMethodStatistics

    @BackupMethodStatistics.setter
    def BackupMethodStatistics(self, BackupMethodStatistics):
        self._BackupMethodStatistics = BackupMethodStatistics

    @property
    def BackupStatistics(self):
        r"""<p>Backup set statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupStatisticsModel`
        """
        return self._BackupStatistics

    @BackupStatistics.setter
    def BackupStatistics(self, BackupStatistics):
        self._BackupStatistics = BackupStatistics

    @property
    def DataBackupStatistics(self):
        r"""<p>Backup statistics.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DataBackupStatisticsModel`
        """
        return self._DataBackupStatistics

    @DataBackupStatistics.setter
    def DataBackupStatistics(self, DataBackupStatistics):
        self._DataBackupStatistics = DataBackupStatistics

    @property
    def LogBackupStatistics(self):
        r"""<p>Log backup statistics</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.LogBackupStatisticsModel`
        """
        return self._LogBackupStatistics

    @LogBackupStatistics.setter
    def LogBackupStatistics(self, LogBackupStatistics):
        self._LogBackupStatistics = LogBackupStatistics

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
        if params.get("BackupMethodStatistics") is not None:
            self._BackupMethodStatistics = BackupMethodStatisticsModel()
            self._BackupMethodStatistics._deserialize(params.get("BackupMethodStatistics"))
        if params.get("BackupStatistics") is not None:
            self._BackupStatistics = BackupStatisticsModel()
            self._BackupStatistics._deserialize(params.get("BackupStatistics"))
        if params.get("DataBackupStatistics") is not None:
            self._DataBackupStatistics = DataBackupStatisticsModel()
            self._DataBackupStatistics._deserialize(params.get("DataBackupStatistics"))
        if params.get("LogBackupStatistics") is not None:
            self._LogBackupStatistics = LogBackupStatisticsModel()
            self._LogBackupStatistics._deserialize(params.get("LogBackupStatistics"))
        self._RequestId = params.get("RequestId")


class DescribeDBSCloneInstancesRequest(AbstractModel):
    r"""DescribeDBSCloneInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SourceInstanceId: <p>Source instance ID.</p>
        :type SourceInstanceId: str
        :param _DBType: <P>Engine type</p>
        :type DBType: str
        :param _EndCreateTime: <P>Creation end time</p>
        :type EndCreateTime: str
        :param _FilterCloneType: <p>Clone kind: PITR time point BackupSet backup set</p>
        :type FilterCloneType: str
        :param _Limit: <P>Query count [0,200]</p>
        :type Limit: int
        :param _Offset: <p>Query offset [0,INF]</p>
        :type Offset: int
        :param _OrderBy: <p>Sorting field: CloneTime, CreateTime</p>
        :type OrderBy: str
        :param _OrderType: <p>Sorting type: ASC, DESC</p>
        :type OrderType: str
        :param _StartCreateTime: <P>Creation start time</p>
        :type StartCreateTime: str
        """
        self._SourceInstanceId = None
        self._DBType = None
        self._EndCreateTime = None
        self._FilterCloneType = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderType = None
        self._StartCreateTime = None

    @property
    def SourceInstanceId(self):
        r"""<p>Source instance ID.</p>
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def DBType(self):
        r"""<P>Engine type</p>
        :rtype: str
        """
        return self._DBType

    @DBType.setter
    def DBType(self, DBType):
        self._DBType = DBType

    @property
    def EndCreateTime(self):
        r"""<P>Creation end time</p>
        :rtype: str
        """
        return self._EndCreateTime

    @EndCreateTime.setter
    def EndCreateTime(self, EndCreateTime):
        self._EndCreateTime = EndCreateTime

    @property
    def FilterCloneType(self):
        r"""<p>Clone kind: PITR time point BackupSet backup set</p>
        :rtype: str
        """
        return self._FilterCloneType

    @FilterCloneType.setter
    def FilterCloneType(self, FilterCloneType):
        self._FilterCloneType = FilterCloneType

    @property
    def Limit(self):
        r"""<P>Query count [0,200]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>Query offset [0,INF]</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""<p>Sorting field: CloneTime, CreateTime</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>Sorting type: ASC, DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartCreateTime(self):
        r"""<P>Creation start time</p>
        :rtype: str
        """
        return self._StartCreateTime

    @StartCreateTime.setter
    def StartCreateTime(self, StartCreateTime):
        self._StartCreateTime = StartCreateTime


    def _deserialize(self, params):
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._DBType = params.get("DBType")
        self._EndCreateTime = params.get("EndCreateTime")
        self._FilterCloneType = params.get("FilterCloneType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartCreateTime = params.get("StartCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSCloneInstancesResponse(AbstractModel):
    r"""DescribeDBSCloneInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Items: <P>Clone list</p>.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of CloneInstanceModel
        :param _TotalCount: <p>Total</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        r"""<P>Clone list</p>.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CloneInstanceModel
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""<p>Total</p>
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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CloneInstanceModel()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    r"""DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID.
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    r"""DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group description.
        :type Groups: list of SecurityGroup
        :param _VIP: Instance VIP.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VIP: str
        :param _VPort: Instance port.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VPort: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        r"""Security group description.
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        r"""Instance VIP.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        r"""Instance port.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    r"""DescribeDatabaseObjects request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID, such as tdsql3-42f40429.</p>
        :type InstanceId: str
        :param _DbName: <p>Database name, obtained via the DescribeDatabases API.</p>
        :type DbName: str
        :param _Offset: <p>Pagination index</p>
        :type Offset: int
        :param _Limit: <p>Number of items per page</p>
        :type Limit: int
        :param _TableRegexp: <p>Table name matching expression</p>
        :type TableRegexp: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Offset = None
        self._Limit = None
        self._TableRegexp = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID, such as tdsql3-42f40429.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""<p>Database name, obtained via the DescribeDatabases API.</p>
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Offset(self):
        r"""<p>Pagination index</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TableRegexp(self):
        r"""<p>Table name matching expression</p>
        :rtype: str
        """
        return self._TableRegexp

    @TableRegexp.setter
    def TableRegexp(self, TableRegexp):
        self._TableRegexp = TableRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TableRegexp = params.get("TableRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    r"""DescribeDatabaseObjects response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Passthrough input parameter.</p>
        :type InstanceId: str
        :param _DbName: <p>Database name.</p>
        :type DbName: str
        :param _Tables: <p>Table list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of DatabaseTable
        :param _Views: <p>View list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of DatabaseView
        :param _Procs: <p>Stored procedure list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procs: list of DatabaseProcedure
        :param _Funcs: <p>Function list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Funcs: list of DatabaseFunction
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DbName = None
        self._Tables = None
        self._Views = None
        self._Procs = None
        self._Funcs = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Passthrough input parameter.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""<p>Database name.</p>
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        r"""<p>Table list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        r"""<p>View list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        r"""<p>Stored procedure list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        r"""<p>Function list.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseFunction
        """
        return self._Funcs

    @Funcs.setter
    def Funcs(self, Funcs):
        self._Funcs = Funcs

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
        self._DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self._Tables.append(obj)
        if params.get("Views") is not None:
            self._Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self._Views.append(obj)
        if params.get("Procs") is not None:
            self._Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self._Procs.append(obj)
        if params.get("Funcs") is not None:
            self._Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self._Funcs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    r"""DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID, such as tdsql3-ow7t8lmc.</p>
        :type InstanceId: str
        :param _Offset: <p>Pagination index</p>
        :type Offset: int
        :param _Limit: <p>Number of items per page</p>
        :type Limit: int
        :param _DatabaseRegexp: <p>Database name matching expression</p>
        :type DatabaseRegexp: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._DatabaseRegexp = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID, such as tdsql3-ow7t8lmc.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""<p>Pagination index</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of items per page</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DatabaseRegexp(self):
        r"""<p>Database name matching expression</p>
        :rtype: str
        """
        return self._DatabaseRegexp

    @DatabaseRegexp.setter
    def DatabaseRegexp(self, DatabaseRegexp):
        self._DatabaseRegexp = DatabaseRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DatabaseRegexp = params.get("DatabaseRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    r"""DescribeDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Passthrough instance ID</p>
        :type InstanceId: str
        :param _Databases: <p>The database list on the instance.</p>
        :type Databases: list of Database
        :param _TotalCount: <p>Total quantity.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Databases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Passthrough instance ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Databases(self):
        r"""<p>The database list on the instance.</p>
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def TotalCount(self):
        r"""<p>Total quantity.</p>
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
        self._InstanceId = params.get("InstanceId")
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    r"""DescribeFlow request structure.

    """


class DescribeFlowResponse(AbstractModel):
    r"""DescribeFlow response structure.

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


class DescribeInstanceSSLStatusRequest(AbstractModel):
    r"""DescribeInstanceSSLStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
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
        


class DescribeInstanceSSLStatusResponse(AbstractModel):
    r"""DescribeInstanceSSLStatus response structure.

    """

    def __init__(self):
        r"""
        :param _SSLStatus: <p>SSL enable status</p><p>Enumeration values:</p><ul><li>Enabled: SSL is on</li><li>Disabled: SSL is closed</li><li>Enabling: SSL is enabling</li><li>Disabling: SSL is disabling</li></ul>
        :type SSLStatus: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SSLStatus = None
        self._RequestId = None

    @property
    def SSLStatus(self):
        r"""<p>SSL enable status</p><p>Enumeration values:</p><ul><li>Enabled: SSL is on</li><li>Disabled: SSL is closed</li><li>Enabling: SSL is enabling</li><li>Disabling: SSL is disabling</li></ul>
        :rtype: str
        """
        return self._SSLStatus

    @SSLStatus.setter
    def SSLStatus(self, SSLStatus):
        self._SSLStatus = SSLStatus

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
        self._SSLStatus = params.get("SSLStatus")
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    r"""DescribeMaintenanceWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
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
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    r"""DescribeMaintenanceWindow response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _MaintenanceWindow: <p>Ops window time range</p>
        :type MaintenanceWindow: str
        :param _WeekDays: <p>Ops window number of days range</p>
        :type WeekDays: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._MaintenanceWindow = None
        self._WeekDays = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintenanceWindow(self):
        r"""<p>Ops window time range</p>
        :rtype: str
        """
        return self._MaintenanceWindow

    @MaintenanceWindow.setter
    def MaintenanceWindow(self, MaintenanceWindow):
        self._MaintenanceWindow = MaintenanceWindow

    @property
    def WeekDays(self):
        r"""<p>Ops window number of days range</p>
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

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
        self._MaintenanceWindow = params.get("MaintenanceWindow")
        self._WeekDays = params.get("WeekDays")
        self._RequestId = params.get("RequestId")


class DescribeSaleInfoRequest(AbstractModel):
    r"""DescribeSaleInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SrcRegion: <p>Region of the disaster recovery primary instance</p>
        :type SrcRegion: str
        :param _InstanceId: <p>Instance id</p><p>Input this parameter to return the sales information of the availability zone in the region where this instance is located.</p>
        :type InstanceId: str
        :param _InstanceType: <p>Specify the sales information that supports a certain type instance.</p><p>Enumeration value:</p><ul><li>serverless: Returns all regions that support serverless instance type.</li></ul><p>Default value: None</p><p>Currently only support specifying serverless. Import other info or leave it blank to return all sales region information by default.</p>
        :type InstanceType: str
        """
        self._SrcRegion = None
        self._InstanceId = None
        self._InstanceType = None

    @property
    def SrcRegion(self):
        r"""<p>Region of the disaster recovery primary instance</p>
        :rtype: str
        """
        return self._SrcRegion

    @SrcRegion.setter
    def SrcRegion(self, SrcRegion):
        self._SrcRegion = SrcRegion

    @property
    def InstanceId(self):
        r"""<p>Instance id</p><p>Input this parameter to return the sales information of the availability zone in the region where this instance is located.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        r"""<p>Specify the sales information that supports a certain type instance.</p><p>Enumeration value:</p><ul><li>serverless: Returns all regions that support serverless instance type.</li></ul><p>Default value: None</p><p>Currently only support specifying serverless. Import other info or leave it blank to return all sales region information by default.</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._SrcRegion = params.get("SrcRegion")
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleInfoResponse(AbstractModel):
    r"""DescribeSaleInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RegionList: <p>Return marketable region information</p>
        :type RegionList: list of DescribeSaleRegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        r"""<p>Return marketable region information</p>
        :rtype: list of DescribeSaleRegionInfo
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = DescribeSaleRegionInfo()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSaleRegionInfo(AbstractModel):
    r"""Query the sales API. The return type is region information.

    """

    def __init__(self):
        r"""
        :param _Region: <p>English string of Region</p>
        :type Region: str
        :param _ZoneList: <p>Purchasable Zone list</p>
        :type ZoneList: list of DescribeSaleZonesInfo
        :param _RegionName: <p>Region Chinese character string</p>
        :type RegionName: str
        :param _Enable: <p>Whether to sell. 1: sell, 0: do not sell</p>
        :type Enable: int
        :param _AvailableZoneNum: <p>Optional quantity of multiple availability</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableZoneNum: int
        :param _IsSupportedLogReplica: <p>Whether to allow usage log replica</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSupportedLogReplica: bool
        :param _ZoneGroup: <p>Availability zone combination</p>
        :type ZoneGroup: list of DescribeSaleZonesGroup
        :param _IsSupportServerless: <p>Whether serverless is supported</p>
        :type IsSupportServerless: bool
        """
        self._Region = None
        self._ZoneList = None
        self._RegionName = None
        self._Enable = None
        self._AvailableZoneNum = None
        self._IsSupportedLogReplica = None
        self._ZoneGroup = None
        self._IsSupportServerless = None

    @property
    def Region(self):
        r"""<p>English string of Region</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ZoneList(self):
        r"""<p>Purchasable Zone list</p>
        :rtype: list of DescribeSaleZonesInfo
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def RegionName(self):
        r"""<p>Region Chinese character string</p>
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Enable(self):
        r"""<p>Whether to sell. 1: sell, 0: do not sell</p>
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AvailableZoneNum(self):
        r"""<p>Optional quantity of multiple availability</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AvailableZoneNum

    @AvailableZoneNum.setter
    def AvailableZoneNum(self, AvailableZoneNum):
        self._AvailableZoneNum = AvailableZoneNum

    @property
    def IsSupportedLogReplica(self):
        r"""<p>Whether to allow usage log replica</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsSupportedLogReplica

    @IsSupportedLogReplica.setter
    def IsSupportedLogReplica(self, IsSupportedLogReplica):
        self._IsSupportedLogReplica = IsSupportedLogReplica

    @property
    def ZoneGroup(self):
        r"""<p>Availability zone combination</p>
        :rtype: list of DescribeSaleZonesGroup
        """
        return self._ZoneGroup

    @ZoneGroup.setter
    def ZoneGroup(self, ZoneGroup):
        self._ZoneGroup = ZoneGroup

    @property
    def IsSupportServerless(self):
        r"""<p>Whether serverless is supported</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = DescribeSaleZonesInfo()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RegionName = params.get("RegionName")
        self._Enable = params.get("Enable")
        self._AvailableZoneNum = params.get("AvailableZoneNum")
        self._IsSupportedLogReplica = params.get("IsSupportedLogReplica")
        if params.get("ZoneGroup") is not None:
            self._ZoneGroup = []
            for item in params.get("ZoneGroup"):
                obj = DescribeSaleZonesGroup()
                obj._deserialize(item)
                self._ZoneGroup.append(obj)
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleZonesGroup(AbstractModel):
    r"""Query sales regions and recommend availability zone combinations

    """

    def __init__(self):
        r"""
        :param _ZoneNum: <p>Number of availability zones</p>
        :type ZoneNum: int
        :param _Zones: <p>Availability zone combination</p>
        :type Zones: list of str
        :param _SupportTypes: <p>Supported types</p>
        :type SupportTypes: list of str
        :param _AvailableDiskTypes: <p>Supported disk</p><p>Enumeration value:</p><ul><li>CLOUD_TCS: Local disk</li><li>CLOUD_HSSD: Enhanced cloud disk</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableDiskTypes: list of str
        :param _IsSupportServerless: <p>Whether serverless is supported</p>
        :type IsSupportServerless: bool
        """
        self._ZoneNum = None
        self._Zones = None
        self._SupportTypes = None
        self._AvailableDiskTypes = None
        self._IsSupportServerless = None

    @property
    def ZoneNum(self):
        r"""<p>Number of availability zones</p>
        :rtype: int
        """
        return self._ZoneNum

    @ZoneNum.setter
    def ZoneNum(self, ZoneNum):
        self._ZoneNum = ZoneNum

    @property
    def Zones(self):
        r"""<p>Availability zone combination</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def SupportTypes(self):
        r"""<p>Supported types</p>
        :rtype: list of str
        """
        return self._SupportTypes

    @SupportTypes.setter
    def SupportTypes(self, SupportTypes):
        self._SupportTypes = SupportTypes

    @property
    def AvailableDiskTypes(self):
        r"""<p>Supported disk</p><p>Enumeration value:</p><ul><li>CLOUD_TCS: Local disk</li><li>CLOUD_HSSD: Enhanced cloud disk</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AvailableDiskTypes

    @AvailableDiskTypes.setter
    def AvailableDiskTypes(self, AvailableDiskTypes):
        self._AvailableDiskTypes = AvailableDiskTypes

    @property
    def IsSupportServerless(self):
        r"""<p>Whether serverless is supported</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._ZoneNum = params.get("ZoneNum")
        self._Zones = params.get("Zones")
        self._SupportTypes = params.get("SupportTypes")
        self._AvailableDiskTypes = params.get("AvailableDiskTypes")
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaleZonesInfo(AbstractModel):
    r"""Query the sales API. The return type is zone information.

    """

    def __init__(self):
        r"""
        :param _Zone: <p>English string of Zone</p>
        :type Zone: str
        :param _ZoneName: <p>Zone Chinese character string</p>
        :type ZoneName: str
        :param _Enable: <p>Whether to sell, 1: sell; 0: do not sell</p>
        :type Enable: int
        :param _IsDefaultMaster: <p>Whether the default primary AZ is used. 0 means no, 1 means yes.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDefaultMaster: int
        :param _AvailableDiskTypes: <p>Selectable disk types in availability zones</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableDiskTypes: list of str
        :param _SupportTypes: <p>Whether it is an exclusive availability zone</p>
        :type SupportTypes: list of str
        :param _IsSupportServerless: <p>Whether serverless is supported</p>
        :type IsSupportServerless: bool
        """
        self._Zone = None
        self._ZoneName = None
        self._Enable = None
        self._IsDefaultMaster = None
        self._AvailableDiskTypes = None
        self._SupportTypes = None
        self._IsSupportServerless = None

    @property
    def Zone(self):
        r"""<p>English string of Zone</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""<p>Zone Chinese character string</p>
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Enable(self):
        r"""<p>Whether to sell, 1: sell; 0: do not sell</p>
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def IsDefaultMaster(self):
        r"""<p>Whether the default primary AZ is used. 0 means no, 1 means yes.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDefaultMaster

    @IsDefaultMaster.setter
    def IsDefaultMaster(self, IsDefaultMaster):
        self._IsDefaultMaster = IsDefaultMaster

    @property
    def AvailableDiskTypes(self):
        r"""<p>Selectable disk types in availability zones</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AvailableDiskTypes

    @AvailableDiskTypes.setter
    def AvailableDiskTypes(self, AvailableDiskTypes):
        self._AvailableDiskTypes = AvailableDiskTypes

    @property
    def SupportTypes(self):
        r"""<p>Whether it is an exclusive availability zone</p>
        :rtype: list of str
        """
        return self._SupportTypes

    @SupportTypes.setter
    def SupportTypes(self, SupportTypes):
        self._SupportTypes = SupportTypes

    @property
    def IsSupportServerless(self):
        r"""<p>Whether serverless is supported</p>
        :rtype: bool
        """
        return self._IsSupportServerless

    @IsSupportServerless.setter
    def IsSupportServerless(self, IsSupportServerless):
        self._IsSupportServerless = IsSupportServerless


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._Enable = params.get("Enable")
        self._IsDefaultMaster = params.get("IsDefaultMaster")
        self._AvailableDiskTypes = params.get("AvailableDiskTypes")
        self._SupportTypes = params.get("SupportTypes")
        self._IsSupportServerless = params.get("IsSupportServerless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsRequest(AbstractModel):
    r"""DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Search log start time
        :type StartTime: str
        :param _EndTime: End time to retrieve logs
        :type EndTime: str
        :param _LogFilter: Filter criteria.
        :type LogFilter: list of LogFilter
        :param _Limit: Items per page limit
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Order: Sort, selectable: ASC, DESC
        :type Order: str
        :param _OrderBy: Sorting criteria may not be the same as selectable fields used to sort according to business.
        :type OrderBy: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._LogFilter = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._OrderBy = None

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
    def StartTime(self):
        r"""Search log start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time to retrieve logs
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LogFilter(self):
        r"""Filter criteria.
        :rtype: list of LogFilter
        """
        return self._LogFilter

    @LogFilter.setter
    def LogFilter(self, LogFilter):
        self._LogFilter = LogFilter

    @property
    def Limit(self):
        r"""Items per page limit
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
    def Order(self):
        r"""Sort, selectable: ASC, DESC
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        r"""Sorting criteria may not be the same as selectable fields used to sort according to business.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("LogFilter") is not None:
            self._LogFilter = []
            for item in params.get("LogFilter"):
                obj = LogFilter()
                obj._deserialize(item)
                self._LogFilter.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    r"""DescribeSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of logs
        :type TotalCount: int
        :param _Items: Log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Items: list of SlowLogData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of logs
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SlowLogData
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SlowLogData()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSpecsRequest(AbstractModel):
    r"""DescribeSpecs request structure.

    """

    def __init__(self):
        r"""
        :param _FullReplications: <p>Number of replicas. Currently supported range: 1-3. Default is 3.</p>
        :type FullReplications: int
        :param _IsExclusiveInstance: <p>Exclusive instance</p>
        :type IsExclusiveInstance: int
        """
        self._FullReplications = None
        self._IsExclusiveInstance = None

    @property
    def FullReplications(self):
        r"""<p>Number of replicas. Currently supported range: 1-3. Default is 3.</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def IsExclusiveInstance(self):
        r"""<p>Exclusive instance</p>
        :rtype: int
        """
        return self._IsExclusiveInstance

    @IsExclusiveInstance.setter
    def IsExclusiveInstance(self, IsExclusiveInstance):
        self._IsExclusiveInstance = IsExclusiveInstance


    def _deserialize(self, params):
        self._FullReplications = params.get("FullReplications")
        self._IsExclusiveInstance = params.get("IsExclusiveInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecsResponse(AbstractModel):
    r"""DescribeSpecs response structure.

    """

    def __init__(self):
        r"""
        :param _HybridNodeSpecs: <p>Purchasable specification list of peer nodes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type HybridNodeSpecs: list of StorageNodeSpec
        :param _ServerlessCcuSpec: <p>Purchasable specification list of svls nodes</p>
        :type ServerlessCcuSpec: list of ServerlessCcu
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HybridNodeSpecs = None
        self._ServerlessCcuSpec = None
        self._RequestId = None

    @property
    def HybridNodeSpecs(self):
        r"""<p>Purchasable specification list of peer nodes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of StorageNodeSpec
        """
        return self._HybridNodeSpecs

    @HybridNodeSpecs.setter
    def HybridNodeSpecs(self, HybridNodeSpecs):
        self._HybridNodeSpecs = HybridNodeSpecs

    @property
    def ServerlessCcuSpec(self):
        r"""<p>Purchasable specification list of svls nodes</p>
        :rtype: list of ServerlessCcu
        """
        return self._ServerlessCcuSpec

    @ServerlessCcuSpec.setter
    def ServerlessCcuSpec(self, ServerlessCcuSpec):
        self._ServerlessCcuSpec = ServerlessCcuSpec

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
        if params.get("HybridNodeSpecs") is not None:
            self._HybridNodeSpecs = []
            for item in params.get("HybridNodeSpecs"):
                obj = StorageNodeSpec()
                obj._deserialize(item)
                self._HybridNodeSpecs.append(obj)
        if params.get("ServerlessCcuSpec") is not None:
            self._ServerlessCcuSpec = []
            for item in params.get("ServerlessCcuSpec"):
                obj = ServerlessCcu()
                obj._deserialize(item)
                self._ServerlessCcuSpec.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserPrivilegesRequest(AbstractModel):
    r"""DescribeUserPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as tdsql3-5baee8df.
        :type InstanceId: str
        :param _Host: Accessing host allowed for the user. Username+host uniquely determines an account.
        :type Host: str
        :param _UserName: Login username.
        :type UserName: str
        :param _DbName: Database name. If it is \*, query global permission (\*.\*) and ignore the Type and Object parameter.
        :type DbName: str
        :param _Object: The name of the specific Type, for example, when Type is table, it is exactly the table name. If both DbName and Type are function names, Object represents the specific object name and cannot be \* or empty.
        :type Object: str
        :param _ObjectType: Type, can be set to table, view, proc, func, and \*. When DbName is a specific database name and Type is \*, it queries the database permission (i.e., db.\*), ignoring the Object parameter.
        :type ObjectType: str
        :param _ColName: When Type=table, ColName as \* indicates the permission to query the table. If it is a specific field name, it indicates the permission to query the corresponding field.
        :type ColName: str
        """
        self._InstanceId = None
        self._Host = None
        self._UserName = None
        self._DbName = None
        self._Object = None
        self._ObjectType = None
        self._ColName = None

    @property
    def InstanceId(self):
        r"""Instance ID, such as tdsql3-5baee8df.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Host(self):
        r"""Accessing host allowed for the user. Username+host uniquely determines an account.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def UserName(self):
        r"""Login username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DbName(self):
        r"""Database name. If it is \*, query global permission (\*.\*) and ignore the Type and Object parameter.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Object(self):
        r"""The name of the specific Type, for example, when Type is table, it is exactly the table name. If both DbName and Type are function names, Object represents the specific object name and cannot be \* or empty.
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def ObjectType(self):
        r"""Type, can be set to table, view, proc, func, and \*. When DbName is a specific database name and Type is \*, it queries the database permission (i.e., db.\*), ignoring the Object parameter.
        :rtype: str
        """
        return self._ObjectType

    @ObjectType.setter
    def ObjectType(self, ObjectType):
        self._ObjectType = ObjectType

    @property
    def ColName(self):
        r"""When Type=table, ColName as \* indicates the permission to query the table. If it is a specific field name, it indicates the permission to query the corresponding field.
        :rtype: str
        """
        return self._ColName

    @ColName.setter
    def ColName(self, ColName):
        self._ColName = ColName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Host = params.get("Host")
        self._UserName = params.get("UserName")
        self._DbName = params.get("DbName")
        self._Object = params.get("Object")
        self._ObjectType = params.get("ObjectType")
        self._ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserPrivilegesResponse(AbstractModel):
    r"""DescribeUserPrivileges response structure.

    """

    def __init__(self):
        r"""
        :param _Privileges: Permission list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Privileges: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Privileges = None
        self._RequestId = None

    @property
    def Privileges(self):
        r"""Permission list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

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
        self._Privileges = params.get("Privileges")
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    r"""DescribeUsers request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID.
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
        


class DescribeUsersResponse(AbstractModel):
    r"""DescribeUsers response structure.

    """

    def __init__(self):
        r"""
        :param _Users: User list.
        :type Users: list of UserInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        r"""User list.
        :rtype: list of UserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

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
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyInstancesRequest(AbstractModel):
    r"""DestroyInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of isolated instance ids required.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""List of isolated instance ids required.
        :rtype: list of str
        """
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
        


class DestroyInstancesResponse(AbstractModel):
    r"""DestroyInstances response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: List of successfully isolated instance ids.
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: Isolation removal failed instance Id list.
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""List of successfully isolated instance ids.
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""Isolation removal failed instance Id list.
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class ExpandInstanceRequest(AbstractModel):
    r"""ExpandInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _StorageNodeNum: <p>Expand storage nodes to how many nodes. If no change, pass the current number of nodes</p>
        :type StorageNodeNum: int
        :param _Zones: <p>Availability zone list</p>
        :type Zones: list of str
        :param _AZMode: <p>az mode. 1: Single az 2: Multi-az non-primary az mode 3: Multi-az primary az mode</p>
        :type AZMode: int
        :param _PrimaryAZ: <p>AZMode 3 means the primary AZ</p>
        :type PrimaryAZ: str
        :param _FullReplications: <p>Number of replicas, value ranges from 1 to 3</p>
        :type FullReplications: int
        """
        self._InstanceId = None
        self._StorageNodeNum = None
        self._Zones = None
        self._AZMode = None
        self._PrimaryAZ = None
        self._FullReplications = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StorageNodeNum(self):
        r"""<p>Expand storage nodes to how many nodes. If no change, pass the current number of nodes</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def Zones(self):
        r"""<p>Availability zone list</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def AZMode(self):
        r"""<p>az mode. 1: Single az 2: Multi-az non-primary az mode 3: Multi-az primary az mode</p>
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def PrimaryAZ(self):
        r"""<p>AZMode 3 means the primary AZ</p>
        :rtype: str
        """
        return self._PrimaryAZ

    @PrimaryAZ.setter
    def PrimaryAZ(self, PrimaryAZ):
        self._PrimaryAZ = PrimaryAZ

    @property
    def FullReplications(self):
        r"""<p>Number of replicas, value ranges from 1 to 3</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StorageNodeNum = params.get("StorageNodeNum")
        self._Zones = params.get("Zones")
        self._AZMode = params.get("AZMode")
        self._PrimaryAZ = params.get("PrimaryAZ")
        self._FullReplications = params.get("FullReplications")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandInstanceResponse(AbstractModel):
    r"""ExpandInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Asynchronous task ID. You can call the Query Task API to get task status with this ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Asynchronous task ID. You can call the Query Task API to get task status with this ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class Explain(AbstractModel):
    r"""Execution plan

    """

    def __init__(self):
        r"""
        :param _ID: <p>Identifier</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: str
        :param _SelectType: <p>Query type</p><p>Enumeration value:</p><ul><li>SIMPLE: A regular query with no subquery and UNION. Single table or ordinary JOIN is SIMPLE.</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SelectType: str
        :param _Table: <p>Table name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Table: str
        :param _Partitions: <p>Partition</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Partitions: str
        :param _Type: <p>Access type</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _PossibleKeys: <p>Possibly used indexes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type PossibleKeys: str
        :param _Key: <p>Used Indexes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _KeyLen: <p>Used Indexes length</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type KeyLen: str
        :param _Ref: <p>Column or constant to compare with the index</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ref: str
        :param _Rows: <p>Estimate the number of scanned rows</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Rows: str
        :param _Filtered: <p>Estimated percentage of remaining rows after conditional filtering</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Filtered: str
        :param _Extra: <p>Additional information, such as Using index, Using filesort</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        """
        self._ID = None
        self._SelectType = None
        self._Table = None
        self._Partitions = None
        self._Type = None
        self._PossibleKeys = None
        self._Key = None
        self._KeyLen = None
        self._Ref = None
        self._Rows = None
        self._Filtered = None
        self._Extra = None

    @property
    def ID(self):
        r"""<p>Identifier</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def SelectType(self):
        r"""<p>Query type</p><p>Enumeration value:</p><ul><li>SIMPLE: A regular query with no subquery and UNION. Single table or ordinary JOIN is SIMPLE.</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SelectType

    @SelectType.setter
    def SelectType(self, SelectType):
        self._SelectType = SelectType

    @property
    def Table(self):
        r"""<p>Table name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Partitions(self):
        r"""<p>Partition</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Type(self):
        r"""<p>Access type</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PossibleKeys(self):
        r"""<p>Possibly used indexes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PossibleKeys

    @PossibleKeys.setter
    def PossibleKeys(self, PossibleKeys):
        self._PossibleKeys = PossibleKeys

    @property
    def Key(self):
        r"""<p>Used Indexes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def KeyLen(self):
        r"""<p>Used Indexes length</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KeyLen

    @KeyLen.setter
    def KeyLen(self, KeyLen):
        self._KeyLen = KeyLen

    @property
    def Ref(self):
        r"""<p>Column or constant to compare with the index</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ref

    @Ref.setter
    def Ref(self, Ref):
        self._Ref = Ref

    @property
    def Rows(self):
        r"""<p>Estimate the number of scanned rows</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Filtered(self):
        r"""<p>Estimated percentage of remaining rows after conditional filtering</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Filtered

    @Filtered.setter
    def Filtered(self, Filtered):
        self._Filtered = Filtered

    @property
    def Extra(self):
        r"""<p>Additional information, such as Using index, Using filesort</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._SelectType = params.get("SelectType")
        self._Table = params.get("Table")
        self._Partitions = params.get("Partitions")
        self._Type = params.get("Type")
        self._PossibleKeys = params.get("PossibleKeys")
        self._Key = params.get("Key")
        self._KeyLen = params.get("KeyLen")
        self._Ref = params.get("Ref")
        self._Rows = params.get("Rows")
        self._Filtered = params.get("Filtered")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFilter(AbstractModel):
    r"""List filter criteria for instances

    """

    def __init__(self):
        r"""
        :param _Name: Filter key, support InstanceId, VpcId, SubnetId, Vip, Vport, Status, InstanceName, TagKey.
        :type Name: str
        :param _Values: Filter value.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""Filter key, support InstanceId, VpcId, SubnetId, Vip, Vport, Status, InstanceName, TagKey.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    r"""Instance information type

    """

    def __init__(self):
        r"""
        :param _ComputeNodeNum: <p>Number of compute nodes</p>
        :type ComputeNodeNum: int
        :param _Zone: <p>Region</p>
        :type Zone: str
        :param _CreateVersion: <p>Creating an Instance Version</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateVersion: str
        :param _InitParams: <p>Initialize instance parameter</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InitParams: list of InstanceParam
        :param _Status: <p>Instance status: creating, created, initializing, running, modifying, isolating, isolated, destroying, destroyed</p>
        :type Status: str
        :param _InstanceId: <p>Instance id</p>
        :type InstanceId: str
        :param _StorageNodeNum: <p>Number of storage nodes</p>
        :type StorageNodeNum: int
        :param _ResourceTags: <p>Instance tag information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTags: list of ResourceTag
        :param _InstanceName: <p>Instance name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Cpu: <p>cpu cores of the computing node</p>
        :type Cpu: int
        :param _VpcId: <p>Character type vpcid</p>
        :type VpcId: str
        :param _Mem: <p>Computing node mem, in GB</p>
        :type Mem: int
        :param _Vip: <p>Subnet IP</p>
        :type Vip: str
        :param _SubnetId: <p>Character type subnetid</p>
        :type SubnetId: str
        :param _Vport: <p>Subnet port</p>
        :type Vport: int
        :param _Disk: <p>Node disk capacity (unit: GB)</p>
        :type Disk: int
        :param _CreateTime: <p>Instance Creation Time</p>
        :type CreateTime: str
        :param _Region: <p>Region of the instance</p>
        :type Region: str
        :param _StatusDesc: <p>Status description in Chinese of the instance</p>
        :type StatusDesc: str
        :param _MCCpu: <p>CPU cores of the control node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type MCCpu: int
        :param _MCMem: <p>CPU size of the control node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type MCMem: int
        :param _ComputerNodeCpu: <p>CPU cores of the computing node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComputerNodeCpu: int
        :param _ComputerNodeMem: <p>Compute node memory size</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComputerNodeMem: int
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageNodeMem: int
        :param _MCNum: <p>Number of control nodes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type MCNum: int
        :param _RenewFlag: <p>Renewal flag</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _PayMode: <p>Payment mode, 0 pay-as-you-go; 1 annual/monthly subscription</p>
        :type PayMode: str
        :param _AccountTag: <p>User tag, inner: internal user; external: external user</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountTag: str
        :param _InstanceType: <p>Instance Architecture Type, separate: decoupled architecture; hyper: peer-to-peer architecture</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _StorageType: <p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageType: str
        :param _DestroyedAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DestroyedAt: str
        :param _ExpireAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireAt: str
        :param _IsolatedAt: <p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedAt: str
        :param _IsolatedFrom: <p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolatedFrom: str
        :param _Replications: <p>1</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Replications: int
        :param _FullReplications: <p>Number of replicas</p>
        :type FullReplications: int
        :param _AppId: <p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _SubAccountUin: <p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubAccountUin: str
        :param _Uin: <p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _Zones: <p>AZ information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _Nodes: <p>Instance node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nodes: list of InstanceNode
        :param _BinlogStatus: <p>Whether binlog is on</p>
        :type BinlogStatus: int
        :param _CdcNodeCpu: <p>Number of cdc node cores</p>
        :type CdcNodeCpu: int
        :param _CdcNodeMem: <p>cdc node memory size</p>
        :type CdcNodeMem: int
        :param _CdcNodeNum: <p>Number of cdc nodes</p>
        :type CdcNodeNum: int
        :param _AZMode: <p>az mode. 1: Single az, 2: Multi-az non-primary az mode, 3: Multi-az primary az mode</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AZMode: int
        :param _StandbyFlag: <p>Disaster recovery flag. 1: No disaster recovery relationship; 2: Primary instance for disaster recovery; 3: Disaster Recovery Standby Instance</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StandbyFlag: int
        :param _StandbySecondaryNum: <p>Number of connected standby instances (Valid only when StandbyFlag == 2)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StandbySecondaryNum: int
        :param _ColumnarNodeCpu: <p>cpu cores of the columnar node</p>
        :type ColumnarNodeCpu: int
        :param _ColumnarNodeMem: <p>Columnar node memory size</p>
        :type ColumnarNodeMem: int
        :param _ColumnarNodeNum: <p>Number of columnar nodes</p>
        :type ColumnarNodeNum: int
        :param _ColumnarNodeDisk: <p>Columnar node disk capacity (unit: GB)</p>
        :type ColumnarNodeDisk: int
        :param _ColumnarNodeStorageType: <p>Columnar node disk type</p>
        :type ColumnarNodeStorageType: str
        :param _InstanceCategory: <p>Exclusive flags, 1: Primary instance (dedicated), 2: Primary instance, 3: Disaster recovery instance, 4: Disaster recovery instance (dedicated)</p>
        :type InstanceCategory: int
        :param _ExclusiveClusterId: <p>dbdc-xxxxx</p>
        :type ExclusiveClusterId: str
        :param _SQLMode: <p>Compatible mode</p>
        :type SQLMode: str
        :param _InstanceMode: <p>Instance mode</p>
        :type InstanceMode: str
        :param _ClusterId: <p>Instance delivery platform</p>
        :type ClusterId: str
        :param _AutoScaleConfig: <p>Auto-scaling configuration</p>
        :type AutoScaleConfig: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        :param _AnalysisMode: <p>Analytical engine mode</p><p>Enumeration value:</p><ul><li>libra: LibraDB analytical engine mode</li></ul>
        :type AnalysisMode: str
        :param _AnalysisRelationInfos: <p>Analysis engine relationship information</p>
        :type AnalysisRelationInfos: list of AnalysisRelationInfo
        :param _AnalysisInstanceInfo: <p>Analysis engine instance info</p>
        :type AnalysisInstanceInfo: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        """
        self._ComputeNodeNum = None
        self._Zone = None
        self._CreateVersion = None
        self._InitParams = None
        self._Status = None
        self._InstanceId = None
        self._StorageNodeNum = None
        self._ResourceTags = None
        self._InstanceName = None
        self._Cpu = None
        self._VpcId = None
        self._Mem = None
        self._Vip = None
        self._SubnetId = None
        self._Vport = None
        self._Disk = None
        self._CreateTime = None
        self._Region = None
        self._StatusDesc = None
        self._MCCpu = None
        self._MCMem = None
        self._ComputerNodeCpu = None
        self._ComputerNodeMem = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._MCNum = None
        self._RenewFlag = None
        self._PayMode = None
        self._AccountTag = None
        self._InstanceType = None
        self._StorageType = None
        self._DestroyedAt = None
        self._ExpireAt = None
        self._IsolatedAt = None
        self._IsolatedFrom = None
        self._Replications = None
        self._FullReplications = None
        self._AppId = None
        self._SubAccountUin = None
        self._Uin = None
        self._Zones = None
        self._Nodes = None
        self._BinlogStatus = None
        self._CdcNodeCpu = None
        self._CdcNodeMem = None
        self._CdcNodeNum = None
        self._AZMode = None
        self._StandbyFlag = None
        self._StandbySecondaryNum = None
        self._ColumnarNodeCpu = None
        self._ColumnarNodeMem = None
        self._ColumnarNodeNum = None
        self._ColumnarNodeDisk = None
        self._ColumnarNodeStorageType = None
        self._InstanceCategory = None
        self._ExclusiveClusterId = None
        self._SQLMode = None
        self._InstanceMode = None
        self._ClusterId = None
        self._AutoScaleConfig = None
        self._AnalysisMode = None
        self._AnalysisRelationInfos = None
        self._AnalysisInstanceInfo = None

    @property
    def ComputeNodeNum(self):
        warnings.warn("parameter `ComputeNodeNum` is deprecated", DeprecationWarning) 

        r"""<p>Number of compute nodes</p>
        :rtype: int
        """
        return self._ComputeNodeNum

    @ComputeNodeNum.setter
    def ComputeNodeNum(self, ComputeNodeNum):
        warnings.warn("parameter `ComputeNodeNum` is deprecated", DeprecationWarning) 

        self._ComputeNodeNum = ComputeNodeNum

    @property
    def Zone(self):
        r"""<p>Region</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreateVersion(self):
        r"""<p>Creating an Instance Version</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateVersion

    @CreateVersion.setter
    def CreateVersion(self, CreateVersion):
        self._CreateVersion = CreateVersion

    @property
    def InitParams(self):
        r"""<p>Initialize instance parameter</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceParam
        """
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams

    @property
    def Status(self):
        r"""<p>Instance status: creating, created, initializing, running, modifying, isolating, isolated, destroying, destroyed</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""<p>Instance id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StorageNodeNum(self):
        r"""<p>Number of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeNum

    @StorageNodeNum.setter
    def StorageNodeNum(self, StorageNodeNum):
        self._StorageNodeNum = StorageNodeNum

    @property
    def ResourceTags(self):
        r"""<p>Instance tag information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def InstanceName(self):
        r"""<p>Instance name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Cpu(self):
        warnings.warn("parameter `Cpu` is deprecated", DeprecationWarning) 

        r"""<p>cpu cores of the computing node</p>
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        warnings.warn("parameter `Cpu` is deprecated", DeprecationWarning) 

        self._Cpu = Cpu

    @property
    def VpcId(self):
        r"""<p>Character type vpcid</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Mem(self):
        warnings.warn("parameter `Mem` is deprecated", DeprecationWarning) 

        r"""<p>Computing node mem, in GB</p>
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        warnings.warn("parameter `Mem` is deprecated", DeprecationWarning) 

        self._Mem = Mem

    @property
    def Vip(self):
        r"""<p>Subnet IP</p>
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def SubnetId(self):
        r"""<p>Character type subnetid</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vport(self):
        r"""<p>Subnet port</p>
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Disk(self):
        r"""<p>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def CreateTime(self):
        r"""<p>Instance Creation Time</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        r"""<p>Region of the instance</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def StatusDesc(self):
        r"""<p>Status description in Chinese of the instance</p>
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def MCCpu(self):
        warnings.warn("parameter `MCCpu` is deprecated", DeprecationWarning) 

        r"""<p>CPU cores of the control node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MCCpu

    @MCCpu.setter
    def MCCpu(self, MCCpu):
        warnings.warn("parameter `MCCpu` is deprecated", DeprecationWarning) 

        self._MCCpu = MCCpu

    @property
    def MCMem(self):
        warnings.warn("parameter `MCMem` is deprecated", DeprecationWarning) 

        r"""<p>CPU size of the control node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MCMem

    @MCMem.setter
    def MCMem(self, MCMem):
        warnings.warn("parameter `MCMem` is deprecated", DeprecationWarning) 

        self._MCMem = MCMem

    @property
    def ComputerNodeCpu(self):
        warnings.warn("parameter `ComputerNodeCpu` is deprecated", DeprecationWarning) 

        r"""<p>CPU cores of the computing node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ComputerNodeCpu

    @ComputerNodeCpu.setter
    def ComputerNodeCpu(self, ComputerNodeCpu):
        warnings.warn("parameter `ComputerNodeCpu` is deprecated", DeprecationWarning) 

        self._ComputerNodeCpu = ComputerNodeCpu

    @property
    def ComputerNodeMem(self):
        warnings.warn("parameter `ComputerNodeMem` is deprecated", DeprecationWarning) 

        r"""<p>Compute node memory size</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ComputerNodeMem

    @ComputerNodeMem.setter
    def ComputerNodeMem(self, ComputerNodeMem):
        warnings.warn("parameter `ComputerNodeMem` is deprecated", DeprecationWarning) 

        self._ComputerNodeMem = ComputerNodeMem

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def MCNum(self):
        warnings.warn("parameter `MCNum` is deprecated", DeprecationWarning) 

        r"""<p>Number of control nodes</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MCNum

    @MCNum.setter
    def MCNum(self, MCNum):
        warnings.warn("parameter `MCNum` is deprecated", DeprecationWarning) 

        self._MCNum = MCNum

    @property
    def RenewFlag(self):
        r"""<p>Renewal flag</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        r"""<p>Payment mode, 0 pay-as-you-go; 1 annual/monthly subscription</p>
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def AccountTag(self):
        r"""<p>User tag, inner: internal user; external: external user</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountTag

    @AccountTag.setter
    def AccountTag(self, AccountTag):
        self._AccountTag = AccountTag

    @property
    def InstanceType(self):
        r"""<p>Instance Architecture Type, separate: decoupled architecture; hyper: peer-to-peer architecture</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def StorageType(self):
        r"""<p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DestroyedAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DestroyedAt

    @DestroyedAt.setter
    def DestroyedAt(self, DestroyedAt):
        self._DestroyedAt = DestroyedAt

    @property
    def ExpireAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def IsolatedAt(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolatedAt

    @IsolatedAt.setter
    def IsolatedAt(self, IsolatedAt):
        self._IsolatedAt = IsolatedAt

    @property
    def IsolatedFrom(self):
        r"""<p>&quot;0000-00-00 00:00:00&quot;</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IsolatedFrom

    @IsolatedFrom.setter
    def IsolatedFrom(self, IsolatedFrom):
        self._IsolatedFrom = IsolatedFrom

    @property
    def Replications(self):
        r"""<p>1</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Replications

    @Replications.setter
    def Replications(self, Replications):
        self._Replications = Replications

    @property
    def FullReplications(self):
        r"""<p>Number of replicas</p>
        :rtype: int
        """
        return self._FullReplications

    @FullReplications.setter
    def FullReplications(self, FullReplications):
        self._FullReplications = FullReplications

    @property
    def AppId(self):
        r"""<p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SubAccountUin(self):
        r"""<p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def Uin(self):
        r"""<p>Account information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Zones(self):
        r"""<p>AZ information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Nodes(self):
        r"""<p>Instance node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNode
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def BinlogStatus(self):
        r"""<p>Whether binlog is on</p>
        :rtype: int
        """
        return self._BinlogStatus

    @BinlogStatus.setter
    def BinlogStatus(self, BinlogStatus):
        self._BinlogStatus = BinlogStatus

    @property
    def CdcNodeCpu(self):
        warnings.warn("parameter `CdcNodeCpu` is deprecated", DeprecationWarning) 

        r"""<p>Number of cdc node cores</p>
        :rtype: int
        """
        return self._CdcNodeCpu

    @CdcNodeCpu.setter
    def CdcNodeCpu(self, CdcNodeCpu):
        warnings.warn("parameter `CdcNodeCpu` is deprecated", DeprecationWarning) 

        self._CdcNodeCpu = CdcNodeCpu

    @property
    def CdcNodeMem(self):
        warnings.warn("parameter `CdcNodeMem` is deprecated", DeprecationWarning) 

        r"""<p>cdc node memory size</p>
        :rtype: int
        """
        return self._CdcNodeMem

    @CdcNodeMem.setter
    def CdcNodeMem(self, CdcNodeMem):
        warnings.warn("parameter `CdcNodeMem` is deprecated", DeprecationWarning) 

        self._CdcNodeMem = CdcNodeMem

    @property
    def CdcNodeNum(self):
        warnings.warn("parameter `CdcNodeNum` is deprecated", DeprecationWarning) 

        r"""<p>Number of cdc nodes</p>
        :rtype: int
        """
        return self._CdcNodeNum

    @CdcNodeNum.setter
    def CdcNodeNum(self, CdcNodeNum):
        warnings.warn("parameter `CdcNodeNum` is deprecated", DeprecationWarning) 

        self._CdcNodeNum = CdcNodeNum

    @property
    def AZMode(self):
        r"""<p>az mode. 1: Single az, 2: Multi-az non-primary az mode, 3: Multi-az primary az mode</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AZMode

    @AZMode.setter
    def AZMode(self, AZMode):
        self._AZMode = AZMode

    @property
    def StandbyFlag(self):
        r"""<p>Disaster recovery flag. 1: No disaster recovery relationship; 2: Primary instance for disaster recovery; 3: Disaster Recovery Standby Instance</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StandbyFlag

    @StandbyFlag.setter
    def StandbyFlag(self, StandbyFlag):
        self._StandbyFlag = StandbyFlag

    @property
    def StandbySecondaryNum(self):
        r"""<p>Number of connected standby instances (Valid only when StandbyFlag == 2)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StandbySecondaryNum

    @StandbySecondaryNum.setter
    def StandbySecondaryNum(self, StandbySecondaryNum):
        self._StandbySecondaryNum = StandbySecondaryNum

    @property
    def ColumnarNodeCpu(self):
        r"""<p>cpu cores of the columnar node</p>
        :rtype: int
        """
        return self._ColumnarNodeCpu

    @ColumnarNodeCpu.setter
    def ColumnarNodeCpu(self, ColumnarNodeCpu):
        self._ColumnarNodeCpu = ColumnarNodeCpu

    @property
    def ColumnarNodeMem(self):
        r"""<p>Columnar node memory size</p>
        :rtype: int
        """
        return self._ColumnarNodeMem

    @ColumnarNodeMem.setter
    def ColumnarNodeMem(self, ColumnarNodeMem):
        self._ColumnarNodeMem = ColumnarNodeMem

    @property
    def ColumnarNodeNum(self):
        r"""<p>Number of columnar nodes</p>
        :rtype: int
        """
        return self._ColumnarNodeNum

    @ColumnarNodeNum.setter
    def ColumnarNodeNum(self, ColumnarNodeNum):
        self._ColumnarNodeNum = ColumnarNodeNum

    @property
    def ColumnarNodeDisk(self):
        r"""<p>Columnar node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._ColumnarNodeDisk

    @ColumnarNodeDisk.setter
    def ColumnarNodeDisk(self, ColumnarNodeDisk):
        self._ColumnarNodeDisk = ColumnarNodeDisk

    @property
    def ColumnarNodeStorageType(self):
        r"""<p>Columnar node disk type</p>
        :rtype: str
        """
        return self._ColumnarNodeStorageType

    @ColumnarNodeStorageType.setter
    def ColumnarNodeStorageType(self, ColumnarNodeStorageType):
        self._ColumnarNodeStorageType = ColumnarNodeStorageType

    @property
    def InstanceCategory(self):
        r"""<p>Exclusive flags, 1: Primary instance (dedicated), 2: Primary instance, 3: Disaster recovery instance, 4: Disaster recovery instance (dedicated)</p>
        :rtype: int
        """
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def ExclusiveClusterId(self):
        r"""<p>dbdc-xxxxx</p>
        :rtype: str
        """
        return self._ExclusiveClusterId

    @ExclusiveClusterId.setter
    def ExclusiveClusterId(self, ExclusiveClusterId):
        self._ExclusiveClusterId = ExclusiveClusterId

    @property
    def SQLMode(self):
        r"""<p>Compatible mode</p>
        :rtype: str
        """
        return self._SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode):
        self._SQLMode = SQLMode

    @property
    def InstanceMode(self):
        r"""<p>Instance mode</p>
        :rtype: str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def ClusterId(self):
        warnings.warn("parameter `ClusterId` is deprecated", DeprecationWarning) 

        r"""<p>Instance delivery platform</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        warnings.warn("parameter `ClusterId` is deprecated", DeprecationWarning) 

        self._ClusterId = ClusterId

    @property
    def AutoScaleConfig(self):
        r"""<p>Auto-scaling configuration</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AutoScalingConfig`
        """
        return self._AutoScaleConfig

    @AutoScaleConfig.setter
    def AutoScaleConfig(self, AutoScaleConfig):
        self._AutoScaleConfig = AutoScaleConfig

    @property
    def AnalysisMode(self):
        r"""<p>Analytical engine mode</p><p>Enumeration value:</p><ul><li>libra: LibraDB analytical engine mode</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def AnalysisRelationInfos(self):
        r"""<p>Analysis engine relationship information</p>
        :rtype: list of AnalysisRelationInfo
        """
        return self._AnalysisRelationInfos

    @AnalysisRelationInfos.setter
    def AnalysisRelationInfos(self, AnalysisRelationInfos):
        self._AnalysisRelationInfos = AnalysisRelationInfos

    @property
    def AnalysisInstanceInfo(self):
        r"""<p>Analysis engine instance info</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.AnalysisInstanceInfo`
        """
        return self._AnalysisInstanceInfo

    @AnalysisInstanceInfo.setter
    def AnalysisInstanceInfo(self, AnalysisInstanceInfo):
        self._AnalysisInstanceInfo = AnalysisInstanceInfo


    def _deserialize(self, params):
        self._ComputeNodeNum = params.get("ComputeNodeNum")
        self._Zone = params.get("Zone")
        self._CreateVersion = params.get("CreateVersion")
        if params.get("InitParams") is not None:
            self._InitParams = []
            for item in params.get("InitParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InitParams.append(obj)
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._StorageNodeNum = params.get("StorageNodeNum")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._InstanceName = params.get("InstanceName")
        self._Cpu = params.get("Cpu")
        self._VpcId = params.get("VpcId")
        self._Mem = params.get("Mem")
        self._Vip = params.get("Vip")
        self._SubnetId = params.get("SubnetId")
        self._Vport = params.get("Vport")
        self._Disk = params.get("Disk")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._StatusDesc = params.get("StatusDesc")
        self._MCCpu = params.get("MCCpu")
        self._MCMem = params.get("MCMem")
        self._ComputerNodeCpu = params.get("ComputerNodeCpu")
        self._ComputerNodeMem = params.get("ComputerNodeMem")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._MCNum = params.get("MCNum")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._AccountTag = params.get("AccountTag")
        self._InstanceType = params.get("InstanceType")
        self._StorageType = params.get("StorageType")
        self._DestroyedAt = params.get("DestroyedAt")
        self._ExpireAt = params.get("ExpireAt")
        self._IsolatedAt = params.get("IsolatedAt")
        self._IsolatedFrom = params.get("IsolatedFrom")
        self._Replications = params.get("Replications")
        self._FullReplications = params.get("FullReplications")
        self._AppId = params.get("AppId")
        self._SubAccountUin = params.get("SubAccountUin")
        self._Uin = params.get("Uin")
        self._Zones = params.get("Zones")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._BinlogStatus = params.get("BinlogStatus")
        self._CdcNodeCpu = params.get("CdcNodeCpu")
        self._CdcNodeMem = params.get("CdcNodeMem")
        self._CdcNodeNum = params.get("CdcNodeNum")
        self._AZMode = params.get("AZMode")
        self._StandbyFlag = params.get("StandbyFlag")
        self._StandbySecondaryNum = params.get("StandbySecondaryNum")
        self._ColumnarNodeCpu = params.get("ColumnarNodeCpu")
        self._ColumnarNodeMem = params.get("ColumnarNodeMem")
        self._ColumnarNodeNum = params.get("ColumnarNodeNum")
        self._ColumnarNodeDisk = params.get("ColumnarNodeDisk")
        self._ColumnarNodeStorageType = params.get("ColumnarNodeStorageType")
        self._InstanceCategory = params.get("InstanceCategory")
        self._ExclusiveClusterId = params.get("ExclusiveClusterId")
        self._SQLMode = params.get("SQLMode")
        self._InstanceMode = params.get("InstanceMode")
        self._ClusterId = params.get("ClusterId")
        if params.get("AutoScaleConfig") is not None:
            self._AutoScaleConfig = AutoScalingConfig()
            self._AutoScaleConfig._deserialize(params.get("AutoScaleConfig"))
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("AnalysisRelationInfos") is not None:
            self._AnalysisRelationInfos = []
            for item in params.get("AnalysisRelationInfos"):
                obj = AnalysisRelationInfo()
                obj._deserialize(item)
                self._AnalysisRelationInfos.append(obj)
        if params.get("AnalysisInstanceInfo") is not None:
            self._AnalysisInstanceInfo = AnalysisInstanceInfo()
            self._AnalysisInstanceInfo._deserialize(params.get("AnalysisInstanceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    r"""Node information

    """

    def __init__(self):
        r"""
        :param _ID: Primary key
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _NodeId: Node Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: str
        :param _Ip: Instance Ip
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _EniIp: Eni IP of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type EniIp: str
        :param _Port: Instance Port
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _SpecCode: Instance SpecCode
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecCode: str
        :param _NodeName: Instance NodeName
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param _Cpu: Instance Cpu
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _Mem: Instance memory
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mem: int
        :param _Disk: Instance Disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type Disk: int
        :param _Type: Instance type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Status: Instance status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Version: instance version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Zone: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _LocalDNS: Instance LocalDNS
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocalDNS: str
        :param _Region: Instance Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _LogDisk: Instance log disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogDisk: int
        :param _DataDisk: Instance data disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDisk: int
        :param _ZoneID: Zone ID of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneID: str
        :param _SpecName: Instance SpecName
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _Replicas: Instance Replicas
Note: This field may return null, indicating that no valid values can be obtained.
        :type Replicas: int
        :param _Shards: Instance Shards
Note: This field may return null, indicating that no valid values can be obtained.
        :type Shards: int
        :param _DataReplicas: Instance data replica
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataReplicas: int
        :param _Params: Initialize parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type Params: str
        :param _StorageType: Storage medium, CLOUD_PREMIUM: Premium Cloud Disk, CLOUD_SSD: SSD cloud disk, CLOUD_HSSD: HSSD cloud disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageType: str
        """
        self._ID = None
        self._InstanceId = None
        self._NodeId = None
        self._Ip = None
        self._EniIp = None
        self._Port = None
        self._SpecCode = None
        self._NodeName = None
        self._Cpu = None
        self._Mem = None
        self._Disk = None
        self._Type = None
        self._Status = None
        self._Version = None
        self._Zone = None
        self._LocalDNS = None
        self._Region = None
        self._LogDisk = None
        self._DataDisk = None
        self._ZoneID = None
        self._SpecName = None
        self._Replicas = None
        self._Shards = None
        self._DataReplicas = None
        self._Params = None
        self._StorageType = None

    @property
    def ID(self):
        r"""Primary key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeId(self):
        r"""Node Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Ip(self):
        r"""Instance Ip
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def EniIp(self):
        r"""Eni IP of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Port(self):
        r"""Instance Port
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SpecCode(self):
        r"""Instance SpecCode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def NodeName(self):
        r"""Instance NodeName
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Cpu(self):
        r"""Instance Cpu
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""Instance memory
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Disk(self):
        r"""Instance Disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def Type(self):
        r"""Instance type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Instance status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        r"""instance version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Zone(self):
        r"""Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def LocalDNS(self):
        r"""Instance LocalDNS
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LocalDNS

    @LocalDNS.setter
    def LocalDNS(self, LocalDNS):
        self._LocalDNS = LocalDNS

    @property
    def Region(self):
        r"""Instance Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def LogDisk(self):
        r"""Instance log disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LogDisk

    @LogDisk.setter
    def LogDisk(self, LogDisk):
        self._LogDisk = LogDisk

    @property
    def DataDisk(self):
        r"""Instance data disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def ZoneID(self):
        r"""Zone ID of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneID

    @ZoneID.setter
    def ZoneID(self, ZoneID):
        self._ZoneID = ZoneID

    @property
    def SpecName(self):
        r"""Instance SpecName
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Replicas(self):
        r"""Instance Replicas
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Shards(self):
        r"""Instance Shards
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def DataReplicas(self):
        r"""Instance data replica
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DataReplicas

    @DataReplicas.setter
    def DataReplicas(self, DataReplicas):
        self._DataReplicas = DataReplicas

    @property
    def Params(self):
        r"""Initialize parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def StorageType(self):
        r"""Storage medium, CLOUD_PREMIUM: Premium Cloud Disk, CLOUD_SSD: SSD cloud disk, CLOUD_HSSD: HSSD cloud disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._NodeId = params.get("NodeId")
        self._Ip = params.get("Ip")
        self._EniIp = params.get("EniIp")
        self._Port = params.get("Port")
        self._SpecCode = params.get("SpecCode")
        self._NodeName = params.get("NodeName")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._Disk = params.get("Disk")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        self._Zone = params.get("Zone")
        self._LocalDNS = params.get("LocalDNS")
        self._Region = params.get("Region")
        self._LogDisk = params.get("LogDisk")
        self._DataDisk = params.get("DataDisk")
        self._ZoneID = params.get("ZoneID")
        self._SpecName = params.get("SpecName")
        self._Replicas = params.get("Replicas")
        self._Shards = params.get("Shards")
        self._DataReplicas = params.get("DataReplicas")
        self._Params = params.get("Params")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    r"""Initialize instance parameters

    """

    def __init__(self):
        r"""
        :param _Param: config key
        :type Param: str
        :param _Value: Config value
        :type Value: str
        """
        self._Param = None
        self._Value = None

    @property
    def Param(self):
        r"""config key
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""Config value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    r"""IsolateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of isolated instance ids required.
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""List of isolated instance ids required.
        :rtype: list of str
        """
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
        


class IsolateDBInstanceResponse(AbstractModel):
    r"""IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInstanceIds: Isolation successful instance Id list.
        :type SuccessInstanceIds: list of str
        :param _FailedInstanceIds: Isolation failed instance Id list.
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SuccessInstanceIds(self):
        r"""Isolation successful instance Id list.
        :rtype: list of str
        """
        return self._SuccessInstanceIds

    @SuccessInstanceIds.setter
    def SuccessInstanceIds(self, SuccessInstanceIds):
        self._SuccessInstanceIds = SuccessInstanceIds

    @property
    def FailedInstanceIds(self):
        r"""Isolation failed instance Id list.
        :rtype: list of str
        """
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

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
        self._SuccessInstanceIds = params.get("SuccessInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class LogBackupStatisticsModel(AbstractModel):
    r"""Backup statistics object for logs

    """

    def __init__(self):
        r"""
        :param _AverageSizePerBackup: <p>Avg size of each log backup in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerBackup: int
        :param _AverageSizePerDay: <p>Avg daily log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageSizePerDay: int
        :param _TotalCount: <p>Number of log backups</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _TotalSize: <p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: int
        """
        self._AverageSizePerBackup = None
        self._AverageSizePerDay = None
        self._TotalCount = None
        self._TotalSize = None

    @property
    def AverageSizePerBackup(self):
        r"""<p>Avg size of each log backup in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerBackup

    @AverageSizePerBackup.setter
    def AverageSizePerBackup(self, AverageSizePerBackup):
        self._AverageSizePerBackup = AverageSizePerBackup

    @property
    def AverageSizePerDay(self):
        r"""<p>Avg daily log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AverageSizePerDay

    @AverageSizePerDay.setter
    def AverageSizePerDay(self, AverageSizePerDay):
        self._AverageSizePerDay = AverageSizePerDay

    @property
    def TotalCount(self):
        r"""<p>Number of log backups</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalSize(self):
        r"""<p>Log backup size in Byte</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._AverageSizePerBackup = params.get("AverageSizePerBackup")
        self._AverageSizePerDay = params.get("AverageSizePerDay")
        self._TotalCount = params.get("TotalCount")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFilter(AbstractModel):
    r"""Slow log filtering

    """

    def __init__(self):
        r"""
        :param _Type: Filter criterion name.

For example: sql - SQL command details

host - client IP
user - database account;
dbName – Database name;
sqlType - SQL type;
Error code

execTime - Execution time
lockWaitTime - Lock waiting time
ioWaitTime - IO wait time
trxLivingTime - Transaction execution time
Cpu time

threadId - Thread ID
trxId - Transaction ID
checkRows - Number of scanned rows
affectRows - Number of rows affected
sentRows - Number of rows returned
        :type Type: str
        :param _Compare: Filter condition match type. Supported:
INC – Includes (multiple values are in a || relationship before).
EXC - excluding (multiple values are in an && relationship)
EQS – equal to (multiple values before are in a || relationship).
NEQ – not equal to (multiple values are in && relationship)

RG - Range;
        :type Compare: str
        :param _Value: Filter condition matching value. When Compare=RG, for example ["1-100","200-300"].
        :type Value: list of str
        """
        self._Type = None
        self._Compare = None
        self._Value = None

    @property
    def Type(self):
        r"""Filter criterion name.

For example: sql - SQL command details

host - client IP
user - database account;
dbName – Database name;
sqlType - SQL type;
Error code

execTime - Execution time
lockWaitTime - Lock waiting time
ioWaitTime - IO wait time
trxLivingTime - Transaction execution time
Cpu time

threadId - Thread ID
trxId - Transaction ID
checkRows - Number of scanned rows
affectRows - Number of rows affected
sentRows - Number of rows returned
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Compare(self):
        r"""Filter condition match type. Supported:
INC – Includes (multiple values are in a || relationship before).
EXC - excluding (multiple values are in an && relationship)
EQS – equal to (multiple values before are in a || relationship).
NEQ – not equal to (multiple values are in && relationship)

RG - Range;
        :rtype: str
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Value(self):
        r"""Filter condition matching value. When Compare=RG, for example ["1-100","200-300"].
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Compare = params.get("Compare")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaintenanceWindowInfo(AbstractModel):
    r"""Maintenance window configuration

    """

    def __init__(self):
        r"""
        :param _StartTime: 
        :type StartTime: int
        :param _Duration: 
        :type Duration: int
        :param _WeekDays: 
        :type WeekDays: list of str
        """
        self._StartTime = None
        self._Duration = None
        self._WeekDays = None

    @property
    def StartTime(self):
        r"""
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        r"""
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def WeekDays(self):
        r"""
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagRequest(AbstractModel):
    r"""ModifyAutoRenewFlag request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <P>Instance list that needs to be modified</p>.
        :type InstanceIds: list of str
        :param _AutoRenewFlag: <P>1 enables automatic renewal, 0 disables automatic renewal.</p>.
        :type AutoRenewFlag: int
        """
        self._InstanceIds = None
        self._AutoRenewFlag = None

    @property
    def InstanceIds(self):
        r"""<P>Instance list that needs to be modified</p>.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AutoRenewFlag(self):
        r"""<P>1 enables automatic renewal, 0 disables automatic renewal.</p>.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    r"""ModifyAutoRenewFlag response structure.

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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id.
        :type InstanceId: str
        :param _SecurityGroupIds: Security group ID list to modify. an array of one or more security group ids.
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def InstanceId(self):
        r"""Instance id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        r"""Security group ID list to modify. an array of one or more security group ids.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    r"""ModifyDBInstanceSecurityGroups response structure.

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


class ModifyDBInstanceVPortRequest(AbstractModel):
    r"""ModifyDBInstanceVPort request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as tdsql3-5baee8df.
        :type InstanceId: str
        :param _Vport: New VPC port 3308
        :type Vport: int
        """
        self._InstanceId = None
        self._Vport = None

    @property
    def InstanceId(self):
        r"""Instance ID, such as tdsql3-5baee8df.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Vport(self):
        r"""New VPC port 3308
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceVPortResponse(AbstractModel):
    r"""ModifyDBInstanceVPort response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Return the async task FlowId
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Return the async task FlowId
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    r"""ModifyDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, for example: tdsql3-ow728lmc.
        :type InstanceId: str
        :param _Params: Parameter list, each element is a combination of Param and Value.
        :type Params: list of DBParamValue
        """
        self._InstanceId = None
        self._Params = None

    @property
    def InstanceId(self):
        r"""Instance ID, for example: tdsql3-ow728lmc.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Params(self):
        r"""Parameter list, each element is a combination of Param and Value.
        :rtype: list of DBParamValue
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    r"""ModifyDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _TaskID: Task id.
        :type TaskID: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskID = None
        self._RequestId = None

    @property
    def TaskID(self):
        r"""Task id.
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

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
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class ModifyDBSBackupPolicyRequest(AbstractModel):
    r"""ModifyDBSBackupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _BackupPolicy: <p>Backup policy</p>
        :type BackupPolicy: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        """
        self._BackupPolicy = None
        self._InstanceId = None

    @property
    def BackupPolicy(self):
        r"""<p>Backup policy</p>
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        """
        return self._BackupPolicy

    @BackupPolicy.setter
    def BackupPolicy(self, BackupPolicy):
        self._BackupPolicy = BackupPolicy

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        if params.get("BackupPolicy") is not None:
            self._BackupPolicy = BackupPolicyModelInput()
            self._BackupPolicy._deserialize(params.get("BackupPolicy"))
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSBackupPolicyResponse(AbstractModel):
    r"""ModifyDBSBackupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: <p>Whether it is successful</p>
        :type IsSuccess: bool
        :param _Msg: <p>Message</p>
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._Msg = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        r"""<p>Whether it is successful</p>
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Msg(self):
        r"""<p>Message</p>
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._IsSuccess = params.get("IsSuccess")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyDBSBackupSetCommentRequest(AbstractModel):
    r"""ModifyDBSBackupSetComment request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _BackupSetId: <p>Backup set ID. the value comes from the DescribeDBSBackupSets api response.</p>
        :type BackupSetId: int
        :param _NewBackupName: <P>Backup notes.</p>
        :type NewBackupName: str
        """
        self._InstanceId = None
        self._BackupSetId = None
        self._NewBackupName = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupSetId(self):
        r"""<p>Backup set ID. the value comes from the DescribeDBSBackupSets api response.</p>
        :rtype: int
        """
        return self._BackupSetId

    @BackupSetId.setter
    def BackupSetId(self, BackupSetId):
        self._BackupSetId = BackupSetId

    @property
    def NewBackupName(self):
        r"""<P>Backup notes.</p>
        :rtype: str
        """
        return self._NewBackupName

    @NewBackupName.setter
    def NewBackupName(self, NewBackupName):
        self._NewBackupName = NewBackupName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
        self._NewBackupName = params.get("NewBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSBackupSetCommentResponse(AbstractModel):
    r"""ModifyDBSBackupSetComment response structure.

    """

    def __init__(self):
        r"""
        :param _IsSuccess: <P>Whether it is successful</p>.
        :type IsSuccess: bool
        :param _Msg: <P>Modify information</p>.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._Msg = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        r"""<P>Whether it is successful</p>.
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Msg(self):
        r"""<P>Modify information</p>.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._IsSuccess = params.get("IsSuccess")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyInstanceNameRequest(AbstractModel):
    r"""ModifyInstanceName request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id that needs to be modified.
        :type InstanceId: str
        :param _InstanceName: Modified instance name. required length: 1-60. can contain chinese, english uppercase and lowercase letters, digits, -, _.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""Instance id that needs to be modified.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Modified instance name. required length: 1-60. can contain chinese, english uppercase and lowercase letters, digits, -, _.
        :rtype: str
        """
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
        


class ModifyInstanceNameResponse(AbstractModel):
    r"""ModifyInstanceName response structure.

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


class ModifyInstanceNetworkRequest(AbstractModel):
    r"""ModifyInstanceNetwork request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _VpcId: VpcId of the target VPC network
        :type VpcId: str
        :param _SubnetId: Subnet ID of the target VPC network
        :type SubnetId: str
        :param _VipReleaseDelay: VIP retention duration, in hours, value ranges from 0 to 168. 0 means immediate release with a one-minute delay. Not specified, default is 24 hr for VIP release.
        :type VipReleaseDelay: int
        :param _Vip: Assign vip modification. Leave blank for a random vip.
        :type Vip: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._VipReleaseDelay = None
        self._Vip = None

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
    def VpcId(self):
        r"""VpcId of the target VPC network
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID of the target VPC network
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VipReleaseDelay(self):
        r"""VIP retention duration, in hours, value ranges from 0 to 168. 0 means immediate release with a one-minute delay. Not specified, default is 24 hr for VIP release.
        :rtype: int
        """
        return self._VipReleaseDelay

    @VipReleaseDelay.setter
    def VipReleaseDelay(self, VipReleaseDelay):
        self._VipReleaseDelay = VipReleaseDelay

    @property
    def Vip(self):
        r"""Assign vip modification. Leave blank for a random vip.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VipReleaseDelay = params.get("VipReleaseDelay")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNetworkResponse(AbstractModel):
    r"""ModifyInstanceNetwork response structure.

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


class ModifyInstanceSSLStatusRequest(AbstractModel):
    r"""ModifyInstanceSSLStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _Enabled: <p>Whether to enable SSL.</p>
        :type Enabled: bool
        """
        self._InstanceId = None
        self._Enabled = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Enabled(self):
        r"""<p>Whether to enable SSL.</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceSSLStatusResponse(AbstractModel):
    r"""ModifyInstanceSSLStatus response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Async process ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Async process ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyMaintenanceWindowRequest(AbstractModel):
    r"""ModifyMaintenanceWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _StartTime: <p>Ops window start time</p><p>Parameter format: hh:mm:ss</p>
        :type StartTime: str
        :param _Duration: <p>Ops window duration</p><p>Value ranges from 1 to 3</p><p>Unit: hour</p>
        :type Duration: int
        :param _WeekDays: <p>Ops window date</p><p>Enumeration value:</p><ul><li>Monday: Monday</li><li>Tuesday: Tuesday</li><li>Wednesday: Wednesday</li><li>Thursday: Thursday</li><li>Friday: Friday</li><li>Saturday: Saturday</li><li>Sunday: Sunday</li></ul>
        :type WeekDays: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._Duration = None
        self._WeekDays = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""<p>Ops window start time</p><p>Parameter format: hh:mm:ss</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        r"""<p>Ops window duration</p><p>Value ranges from 1 to 3</p><p>Unit: hour</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def WeekDays(self):
        r"""<p>Ops window date</p><p>Enumeration value:</p><ul><li>Monday: Monday</li><li>Tuesday: Tuesday</li><li>Wednesday: Wednesday</li><li>Thursday: Thursday</li><li>Friday: Friday</li><li>Saturday: Saturday</li><li>Sunday: Sunday</li></ul>
        :rtype: list of str
        """
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    r"""ModifyMaintenanceWindow response structure.

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


class ModifyUserPrivilegesRequest(AbstractModel):
    r"""ModifyUserPrivileges request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as tdsql3-5baee8df.
        :type InstanceId: str
        :param _Users: Login username and host information
        :type Users: list of User
        :param _GlobalPrivileges: Global permission
        :type GlobalPrivileges: list of str
        :param _DatabasePrivileges: Database-level permission
        :type DatabasePrivileges: list of DatabasePrivileges
        :param _TablePrivileges: Table-level permission
        :type TablePrivileges: list of TablePrivileges
        """
        self._InstanceId = None
        self._Users = None
        self._GlobalPrivileges = None
        self._DatabasePrivileges = None
        self._TablePrivileges = None

    @property
    def InstanceId(self):
        r"""Instance ID, such as tdsql3-5baee8df.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        r"""Login username and host information
        :rtype: list of User
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def GlobalPrivileges(self):
        r"""Global permission
        :rtype: list of str
        """
        return self._GlobalPrivileges

    @GlobalPrivileges.setter
    def GlobalPrivileges(self, GlobalPrivileges):
        self._GlobalPrivileges = GlobalPrivileges

    @property
    def DatabasePrivileges(self):
        r"""Database-level permission
        :rtype: list of DatabasePrivileges
        """
        return self._DatabasePrivileges

    @DatabasePrivileges.setter
    def DatabasePrivileges(self, DatabasePrivileges):
        self._DatabasePrivileges = DatabasePrivileges

    @property
    def TablePrivileges(self):
        r"""Table-level permission
        :rtype: list of TablePrivileges
        """
        return self._TablePrivileges

    @TablePrivileges.setter
    def TablePrivileges(self, TablePrivileges):
        self._TablePrivileges = TablePrivileges


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self._Users.append(obj)
        self._GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self._DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self._DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self._TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self._TablePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPrivilegesResponse(AbstractModel):
    r"""ModifyUserPrivileges response structure.

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


class NodeInfo(AbstractModel):
    r"""Node information type

    """

    def __init__(self):
        r"""
        :param _IP: <p>Node IP information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IP: str
        :param _Type: <p>Node types, such as sqlengine, tdstore, mc</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _NodeId: <p>Unique identifier of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: str
        :param _Port: <p>Node port information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _Zone: <p>Availability zone of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _Host: <p>Machine ip of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _BinlogInfo: <p>Node log service information</p>
        :type BinlogInfo: list of BinlogInfo
        :param _Cpu: <p>Number of CPUs of the node</p>
        :type Cpu: int
        :param _Mem: <p>Node mem size</p>
        :type Mem: int
        :param _DataDisk: <p>Node disk size</p>
        :type DataDisk: int
        """
        self._IP = None
        self._Type = None
        self._NodeId = None
        self._Port = None
        self._Zone = None
        self._Host = None
        self._BinlogInfo = None
        self._Cpu = None
        self._Mem = None
        self._DataDisk = None

    @property
    def IP(self):
        r"""<p>Node IP information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Type(self):
        r"""<p>Node types, such as sqlengine, tdstore, mc</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NodeId(self):
        r"""<p>Unique identifier of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Port(self):
        r"""<p>Node port information</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Zone(self):
        r"""<p>Availability zone of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Host(self):
        r"""<p>Machine ip of the node</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def BinlogInfo(self):
        r"""<p>Node log service information</p>
        :rtype: list of BinlogInfo
        """
        return self._BinlogInfo

    @BinlogInfo.setter
    def BinlogInfo(self, BinlogInfo):
        self._BinlogInfo = BinlogInfo

    @property
    def Cpu(self):
        r"""<p>Number of CPUs of the node</p>
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        r"""<p>Node mem size</p>
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def DataDisk(self):
        r"""<p>Node disk size</p>
        :rtype: int
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Type = params.get("Type")
        self._NodeId = params.get("NodeId")
        self._Port = params.get("Port")
        self._Zone = params.get("Zone")
        self._Host = params.get("Host")
        if params.get("BinlogInfo") is not None:
            self._BinlogInfo = []
            for item in params.get("BinlogInfo"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self._BinlogInfo.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._DataDisk = params.get("DataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamConstraint(AbstractModel):
    r"""Parameter constraints.

    """

    def __init__(self):
        r"""
        :param _Type: Constraint type, for example enumeration, interval.
        :type Type: str
        :param _Enum: Lists the available options when the constraint type is enum.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enum: str
        :param _Range: Value range when the constraint type is section.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.tdmysql.v20211122.models.ConstraintRange`
        :param _String: Valid values when the constraint type is string.
Note: This field may return null, indicating that no valid values can be obtained.
        :type String: str
        """
        self._Type = None
        self._Enum = None
        self._Range = None
        self._String = None

    @property
    def Type(self):
        r"""Constraint type, for example enumeration, interval.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enum(self):
        r"""Lists the available options when the constraint type is enum.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Range(self):
        r"""Value range when the constraint type is section.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ConstraintRange`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def String(self):
        r"""Valid values when the constraint type is string.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Enum = params.get("Enum")
        if params.get("Range") is not None:
            self._Range = ConstraintRange()
            self._Range._deserialize(params.get("Range"))
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    r"""DB parameter description.

    """

    def __init__(self):
        r"""
        :param _Param: Parameter name.
        :type Param: str
        :param _Value: Current parameter value.
        :type Value: str
        :param _SetValue: The configured value is the same as the value once the parameter takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SetValue: str
        :param _Default: System default value.
        :type Default: str
        :param _Constraint: Parameter limits.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Constraint: :class:`tencentcloud.tdmysql.v20211122.models.ParamConstraint`
        :param _HaveSetValue: Whether a value has been set. false: not set. true: has set.
        :type HaveSetValue: bool
        :param _NeedRestart: true: restart required.
        :type NeedRestart: bool
        :param _Description: Parameter description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._Param = None
        self._Value = None
        self._SetValue = None
        self._Default = None
        self._Constraint = None
        self._HaveSetValue = None
        self._NeedRestart = None
        self._Description = None

    @property
    def Param(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param

    @property
    def Value(self):
        r"""Current parameter value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SetValue(self):
        r"""The configured value is the same as the value once the parameter takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SetValue

    @SetValue.setter
    def SetValue(self, SetValue):
        self._SetValue = SetValue

    @property
    def Default(self):
        r"""System default value.
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        r"""Parameter limits.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ParamConstraint`
        """
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint

    @property
    def HaveSetValue(self):
        r"""Whether a value has been set. false: not set. true: has set.
        :rtype: bool
        """
        return self._HaveSetValue

    @HaveSetValue.setter
    def HaveSetValue(self, HaveSetValue):
        self._HaveSetValue = HaveSetValue

    @property
    def NeedRestart(self):
        r"""true: restart required.
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def Description(self):
        r"""Parameter description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Param = params.get("Param")
        self._Value = params.get("Value")
        self._SetValue = params.get("SetValue")
        self._Default = params.get("Default")
        if params.get("Constraint") is not None:
            self._Constraint = ParamConstraint()
            self._Constraint._deserialize(params.get("Constraint"))
        self._HaveSetValue = params.get("HaveSetValue")
        self._NeedRestart = params.get("NeedRestart")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetUserPasswordInfo(AbstractModel):
    r"""User type for password reset

    """

    def __init__(self):
        r"""
        :param _UserName: <p>Username.</p>
        :type UserName: str
        :param _Host: <p>host</p>
        :type Host: str
        :param _Password: <p>plaintext password</p>
        :type Password: str
        :param _EncryptedPassword: <p>Encryption password</p>
        :type EncryptedPassword: str
        """
        self._UserName = None
        self._Host = None
        self._Password = None
        self._EncryptedPassword = None

    @property
    def UserName(self):
        r"""<p>Username.</p>
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        r"""<p>host</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        r"""<p>plaintext password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptedPassword(self):
        r"""<p>Encryption password</p>
        :rtype: str
        """
        return self._EncryptedPassword

    @EncryptedPassword.setter
    def EncryptedPassword(self, EncryptedPassword):
        self._EncryptedPassword = EncryptedPassword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._EncryptedPassword = params.get("EncryptedPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetUserPasswordRequest(AbstractModel):
    r"""ResetUserPassword request structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Username.
        :type UserName: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Host: Host IP, IP range ending with % to denote permission for all IPs in the range
        :type Host: str
        :param _Password: New password, required length 8-32, include at least two of English, digits and symbols.
        :type Password: str
        :param _EncryptedPassword: Encryption password
        :type EncryptedPassword: str
        """
        self._UserName = None
        self._InstanceId = None
        self._Host = None
        self._Password = None
        self._EncryptedPassword = None

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

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
    def Host(self):
        r"""Host IP, IP range ending with % to denote permission for all IPs in the range
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Password(self):
        r"""New password, required length 8-32, include at least two of English, digits and symbols.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EncryptedPassword(self):
        r"""Encryption password
        :rtype: str
        """
        return self._EncryptedPassword

    @EncryptedPassword.setter
    def EncryptedPassword(self, EncryptedPassword):
        self._EncryptedPassword = EncryptedPassword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._InstanceId = params.get("InstanceId")
        self._Host = params.get("Host")
        self._Password = params.get("Password")
        self._EncryptedPassword = params.get("EncryptedPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetUserPasswordResponse(AbstractModel):
    r"""ResetUserPassword response structure.

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


class ResetUsersPasswordRequest(AbstractModel):
    r"""ResetUsersPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance id</p>
        :type InstanceId: str
        :param _Users: <p>Reset user password list</p>
        :type Users: list of ResetUserPasswordInfo
        """
        self._InstanceId = None
        self._Users = None

    @property
    def InstanceId(self):
        r"""<p>Instance id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Users(self):
        r"""<p>Reset user password list</p>
        :rtype: list of ResetUserPasswordInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = ResetUserPasswordInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetUsersPasswordResponse(AbstractModel):
    r"""ResetUsersPassword response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Task ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    r"""tag parameter

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
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
        


class RestartDBInstancesRequest(AbstractModel):
    r"""RestartDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>Array of instance IDs that must be restarted</p>
        :type InstanceIds: list of str
        :param _RestartTime: <p>Restart time. Leave it blank to restart now.</p>
        :type RestartTime: str
        """
        self._InstanceIds = None
        self._RestartTime = None

    @property
    def InstanceIds(self):
        r"""<p>Array of instance IDs that must be restarted</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RestartTime(self):
        r"""<p>Restart time. Leave it blank to restart now.</p>
        :rtype: str
        """
        return self._RestartTime

    @RestartTime.setter
    def RestartTime(self, RestartTime):
        self._RestartTime = RestartTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RestartTime = params.get("RestartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    r"""RestartDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Async task id.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Async task id.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    r"""Security group details.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _CreateTime: CreationTime, time format: yyyy-mm-dd hh:mm:ss.
        :type CreateTime: str
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name.
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param _Inbound: Inbound rule.
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: Outbound rule.
        :type Outbound: list of SecurityGroupBound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Inbound = None
        self._Outbound = None

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""CreationTime, time format: yyyy-mm-dd hh:mm:ss.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        r"""Security group ID.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""Security group name.
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""Security group remarks
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Inbound(self):
        r"""Inbound rule.
        :rtype: list of SecurityGroupBound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        r"""Outbound rule.
        :rtype: list of SecurityGroupBound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    r"""Inbound and outbound rules.

    """

    def __init__(self):
        r"""
        :param _CidrIp: Source IP or IP range, such as 192.168.0.0/16.
        :type CidrIp: str
        :param _Action: Policy, ACCEPT or DROP.
        :type Action: str
        :param _PortRange: Port.
        :type PortRange: str
        :param _IpProtocol: Network protocol, supports UDP, TCP.
        :type IpProtocol: str
        """
        self._CidrIp = None
        self._Action = None
        self._PortRange = None
        self._IpProtocol = None

    @property
    def CidrIp(self):
        r"""Source IP or IP range, such as 192.168.0.0/16.
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Action(self):
        r"""Policy, ACCEPT or DROP.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PortRange(self):
        r"""Port.
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""Network protocol, supports UDP, TCP.
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol


    def _deserialize(self, params):
        self._CidrIp = params.get("CidrIp")
        self._Action = params.get("Action")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessCcu(AbstractModel):
    r"""ccu specification of a serverless instance

    """

    def __init__(self):
        r"""
        :param _MinCcu: <p>ccu minimum value</p>
        :type MinCcu: int
        :param _MaxCcu: <p>Maximum value of ccu</p>
        :type MaxCcu: list of int
        """
        self._MinCcu = None
        self._MaxCcu = None

    @property
    def MinCcu(self):
        r"""<p>ccu minimum value</p>
        :rtype: int
        """
        return self._MinCcu

    @MinCcu.setter
    def MinCcu(self, MinCcu):
        self._MinCcu = MinCcu

    @property
    def MaxCcu(self):
        r"""<p>Maximum value of ccu</p>
        :rtype: list of int
        """
        return self._MaxCcu

    @MaxCcu.setter
    def MaxCcu(self, MaxCcu):
        self._MaxCcu = MaxCcu


    def _deserialize(self, params):
        self._MinCcu = params.get("MinCcu")
        self._MaxCcu = params.get("MaxCcu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    r"""slow log information

    """

    def __init__(self):
        r"""
        :param _Timestamp: <p>Sql execution time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Timestamp: str
        :param _QueryTime: <p>Sql execution duration (seconds)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueryTime: float
        :param _SqlText: <p>Sql statement</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SqlText: str
        :param _UserHost: <p>Client IP address</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserHost: str
        :param _UserName: <p>Username.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Database: <p>Database name.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _LockTime: <p>Lock duration (seconds)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type LockTime: float
        :param _RowsExamined: <p>Number of scanned rows</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowsExamined: int
        :param _RowsSent: <p>Result set row count</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RowsSent: int
        :param _TransactionId: <p>Transaction ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransactionId: str
        :param _RpcTime: <p>rpc duration</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RpcTime: float
        :param _StorageRpcTime: <p>rpc duration for node interaction with storage</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageRpcTime: float
        :param _RpcRetryDelayTime: <p>rpc retry latency</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RpcRetryDelayTime: float
        :param _NodeId: <p>node Name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: str
        :param _RpcTrace: <p>rpc link tracing</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RpcTrace: str
        :param _TDStoreLockTime: <p>TDStore lock duration</p><p>Unit: seconds</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TDStoreLockTime: float
        :param _TraceId: <p>Global ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type TraceId: str
        :param _Explain: <p>Execution plan</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Explain: list of Explain
        """
        self._Timestamp = None
        self._QueryTime = None
        self._SqlText = None
        self._UserHost = None
        self._UserName = None
        self._Database = None
        self._LockTime = None
        self._RowsExamined = None
        self._RowsSent = None
        self._TransactionId = None
        self._RpcTime = None
        self._StorageRpcTime = None
        self._RpcRetryDelayTime = None
        self._NodeId = None
        self._RpcTrace = None
        self._TDStoreLockTime = None
        self._TraceId = None
        self._Explain = None

    @property
    def Timestamp(self):
        r"""<p>Sql execution time</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def QueryTime(self):
        r"""<p>Sql execution duration (seconds)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._QueryTime

    @QueryTime.setter
    def QueryTime(self, QueryTime):
        self._QueryTime = QueryTime

    @property
    def SqlText(self):
        r"""<p>Sql statement</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SqlText

    @SqlText.setter
    def SqlText(self, SqlText):
        self._SqlText = SqlText

    @property
    def UserHost(self):
        r"""<p>Client IP address</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserHost

    @UserHost.setter
    def UserHost(self, UserHost):
        self._UserHost = UserHost

    @property
    def UserName(self):
        r"""<p>Username.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        r"""<p>Database name.</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def LockTime(self):
        r"""<p>Lock duration (seconds)</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._LockTime

    @LockTime.setter
    def LockTime(self, LockTime):
        self._LockTime = LockTime

    @property
    def RowsExamined(self):
        r"""<p>Number of scanned rows</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RowsExamined

    @RowsExamined.setter
    def RowsExamined(self, RowsExamined):
        self._RowsExamined = RowsExamined

    @property
    def RowsSent(self):
        r"""<p>Result set row count</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RowsSent

    @RowsSent.setter
    def RowsSent(self, RowsSent):
        self._RowsSent = RowsSent

    @property
    def TransactionId(self):
        r"""<p>Transaction ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def RpcTime(self):
        r"""<p>rpc duration</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RpcTime

    @RpcTime.setter
    def RpcTime(self, RpcTime):
        self._RpcTime = RpcTime

    @property
    def StorageRpcTime(self):
        r"""<p>rpc duration for node interaction with storage</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._StorageRpcTime

    @StorageRpcTime.setter
    def StorageRpcTime(self, StorageRpcTime):
        self._StorageRpcTime = StorageRpcTime

    @property
    def RpcRetryDelayTime(self):
        r"""<p>rpc retry latency</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RpcRetryDelayTime

    @RpcRetryDelayTime.setter
    def RpcRetryDelayTime(self, RpcRetryDelayTime):
        self._RpcRetryDelayTime = RpcRetryDelayTime

    @property
    def NodeId(self):
        r"""<p>node Name</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def RpcTrace(self):
        r"""<p>rpc link tracing</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RpcTrace

    @RpcTrace.setter
    def RpcTrace(self, RpcTrace):
        self._RpcTrace = RpcTrace

    @property
    def TDStoreLockTime(self):
        r"""<p>TDStore lock duration</p><p>Unit: seconds</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._TDStoreLockTime

    @TDStoreLockTime.setter
    def TDStoreLockTime(self, TDStoreLockTime):
        self._TDStoreLockTime = TDStoreLockTime

    @property
    def TraceId(self):
        r"""<p>Global ID</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def Explain(self):
        r"""<p>Execution plan</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Explain
        """
        return self._Explain

    @Explain.setter
    def Explain(self, Explain):
        self._Explain = Explain


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._QueryTime = params.get("QueryTime")
        self._SqlText = params.get("SqlText")
        self._UserHost = params.get("UserHost")
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._LockTime = params.get("LockTime")
        self._RowsExamined = params.get("RowsExamined")
        self._RowsSent = params.get("RowsSent")
        self._TransactionId = params.get("TransactionId")
        self._RpcTime = params.get("RpcTime")
        self._StorageRpcTime = params.get("StorageRpcTime")
        self._RpcRetryDelayTime = params.get("RpcRetryDelayTime")
        self._NodeId = params.get("NodeId")
        self._RpcTrace = params.get("RpcTrace")
        self._TDStoreLockTime = params.get("TDStoreLockTime")
        self._TraceId = params.get("TraceId")
        if params.get("Explain") is not None:
            self._Explain = []
            for item in params.get("Explain"):
                obj = Explain()
                obj._deserialize(item)
                self._Explain.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageNodeSpec(AbstractModel):
    r"""Node specification for storage

    """

    def __init__(self):
        r"""
        :param _SpecCode: <p>Specification code</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecCode: str
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
        :type StorageNodeMem: int
        :param _StorageNodeMaxNum: <p>Maximum quantity of storage nodes</p>
        :type StorageNodeMaxNum: int
        :param _StorageNodeMaxDisk: <p>Node disk size capacity limit</p>
        :type StorageNodeMaxDisk: int
        :param _StorageNodeMinNum: <p>Minimum number of storage nodes</p>
        :type StorageNodeMinNum: int
        :param _StorageNodeMinDisk: <p>Node disk size minimum</p>
        :type StorageNodeMinDisk: int
        :param _StorageType: <p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageType: str
        :param _StorageNodeDefaultDisk: <p>Default disk size of storage node for frontend display</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageNodeDefaultDisk: int
        :param _InstanceMode: <p>Specification support billing mode list</p>
        :type InstanceMode: list of str
        :param _DiskTypeCategory: <p>Disk Type CLOUD_DISK: cloud disk LOCAL_DISK: local disk</p>
        :type DiskTypeCategory: str
        """
        self._SpecCode = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._StorageNodeMaxNum = None
        self._StorageNodeMaxDisk = None
        self._StorageNodeMinNum = None
        self._StorageNodeMinDisk = None
        self._StorageType = None
        self._StorageNodeDefaultDisk = None
        self._InstanceMode = None
        self._DiskTypeCategory = None

    @property
    def SpecCode(self):
        r"""<p>Specification code</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def StorageNodeMaxNum(self):
        r"""<p>Maximum quantity of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeMaxNum

    @StorageNodeMaxNum.setter
    def StorageNodeMaxNum(self, StorageNodeMaxNum):
        self._StorageNodeMaxNum = StorageNodeMaxNum

    @property
    def StorageNodeMaxDisk(self):
        r"""<p>Node disk size capacity limit</p>
        :rtype: int
        """
        return self._StorageNodeMaxDisk

    @StorageNodeMaxDisk.setter
    def StorageNodeMaxDisk(self, StorageNodeMaxDisk):
        self._StorageNodeMaxDisk = StorageNodeMaxDisk

    @property
    def StorageNodeMinNum(self):
        r"""<p>Minimum number of storage nodes</p>
        :rtype: int
        """
        return self._StorageNodeMinNum

    @StorageNodeMinNum.setter
    def StorageNodeMinNum(self, StorageNodeMinNum):
        self._StorageNodeMinNum = StorageNodeMinNum

    @property
    def StorageNodeMinDisk(self):
        r"""<p>Node disk size minimum</p>
        :rtype: int
        """
        return self._StorageNodeMinDisk

    @StorageNodeMinDisk.setter
    def StorageNodeMinDisk(self, StorageNodeMinDisk):
        self._StorageNodeMinDisk = StorageNodeMinDisk

    @property
    def StorageType(self):
        r"""<p>Disk Type, CLOUD_HSSD enhanced SSD, CLOUD_TCS local SSD disk</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageNodeDefaultDisk(self):
        r"""<p>Default disk size of storage node for frontend display</p>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageNodeDefaultDisk

    @StorageNodeDefaultDisk.setter
    def StorageNodeDefaultDisk(self, StorageNodeDefaultDisk):
        self._StorageNodeDefaultDisk = StorageNodeDefaultDisk

    @property
    def InstanceMode(self):
        r"""<p>Specification support billing mode list</p>
        :rtype: list of str
        """
        return self._InstanceMode

    @InstanceMode.setter
    def InstanceMode(self, InstanceMode):
        self._InstanceMode = InstanceMode

    @property
    def DiskTypeCategory(self):
        r"""<p>Disk Type CLOUD_DISK: cloud disk LOCAL_DISK: local disk</p>
        :rtype: str
        """
        return self._DiskTypeCategory

    @DiskTypeCategory.setter
    def DiskTypeCategory(self, DiskTypeCategory):
        self._DiskTypeCategory = DiskTypeCategory


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._StorageNodeMaxNum = params.get("StorageNodeMaxNum")
        self._StorageNodeMaxDisk = params.get("StorageNodeMaxDisk")
        self._StorageNodeMinNum = params.get("StorageNodeMinNum")
        self._StorageNodeMinDisk = params.get("StorageNodeMinDisk")
        self._StorageType = params.get("StorageType")
        self._StorageNodeDefaultDisk = params.get("StorageNodeDefaultDisk")
        self._InstanceMode = params.get("InstanceMode")
        self._DiskTypeCategory = params.get("DiskTypeCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivileges(AbstractModel):
    r"""Table-level permissions

    """

    def __init__(self):
        r"""
        :param _Database: DATABASE name
        :type Database: str
        :param _Table: Table name
        :type Table: str
        :param _Privileges: Permission list
        :type Privileges: list of str
        """
        self._Database = None
        self._Table = None
        self._Privileges = None

    @property
    def Database(self):
        r"""DATABASE name
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        r"""Table name
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def Privileges(self):
        r"""Permission list
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges


    def _deserialize(self, params):
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>Instance ID.</p>
        :type InstanceId: str
        :param _SpecCode: <p>Instance specification code</p>
        :type SpecCode: str
        :param _Disk: <p>Node disk capacity (unit: GB)</p>
        :type Disk: int
        :param _StorageNodeCpu: <p>CPU cores of the storage node</p>
        :type StorageNodeCpu: int
        :param _StorageNodeMem: <p>Storage node memory size</p>
        :type StorageNodeMem: int
        :param _StorageType: <p>Disk Type. Pass this parameter when the disk type needs to be modified.</p>
        :type StorageType: str
        """
        self._InstanceId = None
        self._SpecCode = None
        self._Disk = None
        self._StorageNodeCpu = None
        self._StorageNodeMem = None
        self._StorageType = None

    @property
    def InstanceId(self):
        r"""<p>Instance ID.</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpecCode(self):
        r"""<p>Instance specification code</p>
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Disk(self):
        r"""<p>Node disk capacity (unit: GB)</p>
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def StorageNodeCpu(self):
        r"""<p>CPU cores of the storage node</p>
        :rtype: int
        """
        return self._StorageNodeCpu

    @StorageNodeCpu.setter
    def StorageNodeCpu(self, StorageNodeCpu):
        self._StorageNodeCpu = StorageNodeCpu

    @property
    def StorageNodeMem(self):
        r"""<p>Storage node memory size</p>
        :rtype: int
        """
        return self._StorageNodeMem

    @StorageNodeMem.setter
    def StorageNodeMem(self, StorageNodeMem):
        self._StorageNodeMem = StorageNodeMem

    @property
    def StorageType(self):
        r"""<p>Disk Type. Pass this parameter when the disk type needs to be modified.</p>
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpecCode = params.get("SpecCode")
        self._Disk = params.get("Disk")
        self._StorageNodeCpu = params.get("StorageNodeCpu")
        self._StorageNodeMem = params.get("StorageNodeMem")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    r"""UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Task ID.</p>
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""<p>Task ID.</p>
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class User(AbstractModel):
    r"""Database account information

    """

    def __init__(self):
        r"""
        :param _UserName: Username.
        :type UserName: str
        :param _Host: host
        :type Host: str
        """
        self._UserName = None
        self._Host = None

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Host(self):
        r"""host
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    r"""User information type

    """

    def __init__(self):
        r"""
        :param _UserName: Username.
        :type UserName: str
        :param _Description: User description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Host: Host IP, IP range ending with % to denote permission for all IPs in the range
        :type Host: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        """
        self._UserName = None
        self._Description = None
        self._Host = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def UserName(self):
        r"""Username.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Description(self):
        r"""User description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Host(self):
        r"""Host IP, IP range ending with % to denote permission for all IPs in the range
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

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
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Description = params.get("Description")
        self._Host = params.get("Host")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        