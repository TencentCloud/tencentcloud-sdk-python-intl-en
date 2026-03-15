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
        


class CreateDBSBackupRequest(AbstractModel):
    r"""CreateDBSBackup request structure.

    """

    def __init__(self):
        r"""
        :param _BackupMethod: <p>Backup method: physical, snapshot. this value should be consistent with the backupMethod in the api response of DescribeDBSBackupPolicy.</p>enumeration value:<ul><li> physical: physical backup</li><li> snapshot: snapshot backup</li></ul>
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
        r"""<p>Backup method: physical, snapshot. this value should be consistent with the backupMethod in the api response of DescribeDBSBackupPolicy.</p>enumeration value:<ul><li> physical: physical backup</li><li> snapshot: snapshot backup</li></ul>
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


class DescribeDBSAvailableRecoveryTimeRequest(AbstractModel):
    r"""DescribeDBSAvailableRecoveryTime request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>db instance ID.</p>
        :type InstanceId: str
        :param _BackupSetId: <p>Backup set ID. the value comes from the DescribeDBSBackupSets api response.</p>
        :type BackupSetId: int
        """
        self._InstanceId = None
        self._BackupSetId = None

    @property
    def InstanceId(self):
        r"""<p>db instance ID.</p>
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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupSetId = params.get("BackupSetId")
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
        :param _InstanceId: Instance ID, for example: tdsql3-42f40429.
        :type InstanceId: str
        :param _DbName: Database name, obtained via the DescribeDatabases api.
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        r"""Instance ID, for example: tdsql3-42f40429.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""Database name, obtained via the DescribeDatabases api.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
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
        :param _InstanceId: Passthrough input parameter.
        :type InstanceId: str
        :param _DbName: Database name.
        :type DbName: str
        :param _Tables: Table list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tables: list of DatabaseTable
        :param _Views: View list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Views: list of DatabaseView
        :param _Procs: Stored procedure list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Procs: list of DatabaseProcedure
        :param _Funcs: Function list.
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
        r"""Passthrough input parameter.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""Database name.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def Tables(self):
        r"""Table list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseTable
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

    @property
    def Views(self):
        r"""View list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseView
        """
        return self._Views

    @Views.setter
    def Views(self, Views):
        self._Views = Views

    @property
    def Procs(self):
        r"""Stored procedure list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DatabaseProcedure
        """
        return self._Procs

    @Procs.setter
    def Procs(self, Procs):
        self._Procs = Procs

    @property
    def Funcs(self):
        r"""Function list.
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
        :param _BackupPolicy: Backup policy.
        :type BackupPolicy: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._BackupPolicy = None
        self._InstanceId = None

    @property
    def BackupPolicy(self):
        r"""Backup policy.
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.BackupPolicyModelInput`
        """
        return self._BackupPolicy

    @BackupPolicy.setter
    def BackupPolicy(self, BackupPolicy):
        self._BackupPolicy = BackupPolicy

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
        :param _IsSuccess: Success status.
        :type IsSuccess: bool
        :param _Msg: Message.
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsSuccess = None
        self._Msg = None
        self._RequestId = None

    @property
    def IsSuccess(self):
        r"""Success status.
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def Msg(self):
        r"""Message.
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
        